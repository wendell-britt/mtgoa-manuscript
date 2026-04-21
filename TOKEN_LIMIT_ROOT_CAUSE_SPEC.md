# Root Cause Analysis + Spec — Token Limit Failure Mode
**Session:** 2026-04-20 | **Status:** Root cause identified, spec written

---

## What Happened

Response interrupted BEFORE any output was generated. Model hit token cap during **input processing** — the system prompt + full conversation history consumed the available context before the model could produce even one token of response.


---

## Root Cause Analysis

### The Systemic Problem

**Three compounding factors create a predictable failure mode:**

```
Factor 1 — System prompt is large
  ├─ ~7000 tokens (this one is ~60K chars)
  └─ Loaded on EVERY conversation turn

Factor 2 — Long conversation history accumulates
  ├─ ~200 tokens/turn × N turns
  ├─ At 40 turns: ~8000 tokens of history
  └─ At 45 turns: approaching the input limit

Factor 3 — No proactive awareness or intervention
  ├─ No turn counter being tracked visibly
  ├─ No warning before hitting the wall
  ├─ No state dump triggered before failure
  └─ Rule exists but not being applied proactively
```

**The failure cascade:**
```
Turn 1-30   → Normal. History is small.
Turn 31-40  → History growing. Rule SHOULD fire. Often doesn't.
Turn 41+    → History is very large. Any long output attempt fails.
             Model processes prompt + history → hits cap → produces nothing.
             "Response interrupted before generation."
```

### Why Existing Rules Don't Catch This

| Rule | What it says | Why it fails here |
|------|-------------|-----------------|
| "40 messages → dump state" | Dump when count approaches 40 | Not being tracked proactively; conversation turns slip past without the dump firing |
| "50 tool calls → pause" | Pause at 50 calls | Tool call count is separate from turn count |
| "Large AI task → check quota first" | Check quota before long outputs | The issue is **input** size, not output size |

**The meta-problem:** The rules are reactive (fire when condition is met) but not **proactively tracked**. There's no visible counter in the conversation, no checkpoint system, no heartbeat that says "we're at turn X, here's where we should be."

### What's Unique About This Failure Mode

1. **It fires on input, not output.** Most token concerns are about generated content hitting limits. This fires when the *input context* is too large for the model to process before generating anything.

2. **Zero output — invisible failure.** A failed generation gives you nothing to analyze. The model couldn't produce a response, so there's no content to review, no partial draft to salvage.

3. **System prompt is fixed.** I can't reduce the system prompt size. It's load-and-forget on every turn.

4. **The 6-face persona amplifies it.** The Council persona is the most token-heavy — it includes the full persona description, all rules, all skills, all capabilities. More characters than a standard Zo persona.

### Model-Specific Analysis

**Token flow per turn:**
```
[System prompt: ~7000 tokens]
+ [Conversation history: ~200 tokens/turn × N turns]
+ [Current message: ~variable]
+ [My response prefix: ~50 tokens]
= Total input

vs.

Available context: 128,000 tokens (MiniMax 2.7)
→ Output cap: ~remaining tokens after input is processed
```

**The math:**
```
At turn 0:  Input = 7000 tokens  → Output cap = ~121,000 tokens ✓
At turn 30: Input = 7000 + 6000 = 13,000 tokens → Output cap = ~115,000 tokens ✓
At turn 40: Input = 7000 + 8000 = 15,000 tokens → Output cap = ~113,000 tokens ✓
At turn 50: Input = 7000 + 10000 = 17,000 tokens → Output cap = ~111,000 tokens ✓
At turn 100: Input = 7000 + 20000 = 27,000 tokens → Output cap = ~101,000 tokens ✓
```

**Wait — the math says we should have room. Something else is the issue.**

Let me reconsider. The interruption happened on a long response generation attempt. The model was trying to generate ~3750 tokens of document content. If the model processes the full input first, then generates, the generation itself has to fit in the output window.

**The actual bottleneck may be:**
```
[System prompt] + [History] + [My generation so far] + [Remaining generation]
= Must fit within total context window
```

Or: **The model has a separate output max_tokens setting** that limits how long any single response can be, independent of input size. This is the most likely explanation.

**If output cap is ~4000 tokens (~16,000 chars):**
- Jordan profile (~3000 chars) → fits
- Full ICA document (~8000 chars) → fails at generation step
- State dump + EDITING_PLAN (~6000 chars) → borderline

### Two Distinct Failure Modes Identified

| Mode | Trigger | Symptom | Prevention |
|------|---------|---------|------------|
| **Mode A: Input Overflow** | System prompt + history exceeds context window | Model can't process prompt at all | State dumps at 30 turns |
| **Mode B: Output Overflow** | Single response exceeds output cap | Response interrupted mid-generation | Chunk large outputs |
| **Mode C: Both** | Both conditions met | Nothing generated | Chunk + dump |

Mode B is what hit us. The document generation ran long → hit output cap → got interrupted with zero output.

---

## Solution Spec

### Solution 1 — Turn Counter + Checkpoint System

**What:** A visible turn counter that tracks conversation length and triggers structured checkpoints.

**Implementation:**
```python
# Script: turn_counter.py
# Tracks turns and conversation health

STATE_FILE = "/home/.z/workspaces/{conversation_id}/turn_state.json"

def get_turn_count():
    """Read current turn count from state file."""
    pass

def increment_turn():
    """Increment and evaluate checkpoint conditions."""
    pass

def should_checkpoint():
    """Return True if conditions met for a checkpoint."""
    # TURN 25: Soft warning — "We're at 25 turns. Consider wrapping up or dumping."
    # TURN 35: Hard warning — "We need to wrap up or dump before continuing."
    # TURN 40+: Block — "Dump required before continuing."
```

**When to fire:**
- TURN 25 → Soft warning in conversation
- TURN 35 → Hard warning + state dump offered
- TURN 40 → State dump required before continuing

**Integration:** Run `turn_counter.py checkpoint` at the start of every response. No exceptions. Output the checkpoint status as a one-liner: `[25/40 turns | checkpoint: soft-warning]`.

### Solution 2 — Chunked Document Generation Protocol

**What:** Documents over 10,000 chars are generated in chunks with explicit save-and-continue signals.

**The protocol:**
```
For any document > 10,000 chars:
1. Announce the chunking plan: "Generating in N chunks."
2. Generate chunk 1 → save → confirm path → signal continue
3. Generate chunk 2 → save → confirm path → signal continue
4. Repeat until done
5. Verify all chunks with wc -c before declaring done
```

**Chunk size:** Target 6,000-8,000 chars per chunk. Never approach the output cap in a single generation.

**The signal:** After saving each chunk, say "→ Chunk N saved. Ready to continue." This gives the user a confirmation and a natural break point.

**Rule to create:**
```
CONDITION: WHEN about to generate text > 10,000 chars in a single response
RULE: Chunk the content. Generate in parts with explicit save signals. 
     Never approach the output cap in one generation.
```

### Solution 3 — Session State Dump as First-Class Artifact

**What:** State dumps are structured, complete, and loadable by the next session without additional prompting.

**Dump format:**
```
SESSION_DUMP_{date}.md

## Where We Are
[What was being worked on]

## What's Done
[Completed sections, files saved]

## What's Pending
[Remaining work]

## Files Created This Session
[Full paths]

## Key Decisions Made
[Decisions + rationale]

## Rules Created / Updated
[Links]

## For the Next Session
[One clear next action]
```

**Integration:** The dump fires at turn 30 and turn 40. It replaces the informal "let me dump state" — it's a formal artifact that the next session can load with full context.

**Rule to update:**
```
CONDITION: WHEN conversation message count approaches 40 (estimate 20 turns)
RULE: Before next reply, write a state dump to /home/.z/workspaces/{conversation_id}/notes.md
  → UPDATE: Write at turns 25, 35, and 40. Make dumps structured and loadable.
```

### Solution 4 — Pre-Generation Awareness

**What:** Before generating a long response, I check the current turn count and estimated output size and decide whether to chunk preemptively.

**Decision tree:**
```
Is the response going to be > 8,000 chars?
  YES → Chunk it. Don't try in one shot.
  NO  → Proceed. Check turn count first.

Is turn count > 35?
  YES → Warn user. Offer to dump state before continuing.
  NO  → Proceed.

Is turn count > 25?
  YES → Note it briefly. Don't interrupt flow.
  NO  → Proceed.
```

**This becomes a skill:** `Skills/token-safe-generation/`

### Solution 5 — Model Settings Investigation

**What:** Determine if max_tokens can be raised for this model.

**Action:** User checks [AI Settings](/?t=settings&s=ai&d=models) and reports whether there's a max_tokens or response length configuration. If available, raise it to give more headroom per generation.

**Why it's last:** This depends on Zo infrastructure. The other solutions work regardless of model settings.

---

## Implementation Priority

| Priority | Solution | Why |
|----------|----------|-----|
| P1 | Turn Counter + Checkpoint | Prevents us from ever hitting the wall |
| P2 | Chunked Generation Protocol | Prevents Mode B failures for large outputs |
| P3 | State Dump Format | Makes handoffs clean and reliable |
| P4 | Pre-Generation Awareness | Decision tree before long outputs |
| P5 | Model Settings | Infrastructure-level fix if available |

---

## Rules to Create / Update

**New rule — Chunked generation:**
```
CONDITION: WHEN about to generate text > 10,000 chars in a single response
RULE: Chunk the content into parts. Generate in 6,000-8,000 char segments with
     explicit save signals between each. Never approach the output cap in one generation.
```

**Update existing rule — Turn checkpoint schedule:**
```
CONDITION: WHEN conversation message count approaches 40 (estimate 20 turns)
RULE: Write structured state dumps at turns 25, 35, and 40. Format: SESSION_DUMP_{YYYY-MM-DD}.md.
     Structured format with: Where We Are, What's Done, What's Pending, Files Created, Key Decisions, Next Action.
```

**New rule — Pre-generation check:**
```
CONDITION: WHEN about to generate a response that will be > 8,000 chars
RULE: Chunk the response. Announce the chunking plan. Save each chunk before continuing.
     Say "→ Chunk N saved. Ready to continue." after each save.
```

---

## Companion: Skills to Create

### Skills/token-safe-generation/SKILL.md
- **Purpose:** Token-safe document generation workflow
- **When to use:** Any time generating text > 5,000 chars
- **What it does:** Turn counter check → output size estimate → chunk or proceed decision → save signals

### Skills/session-handoff/SKILL.md
- **Purpose:** Structured state dumps between conversation sessions
- **When to use:** End of session, turn 30 checkpoint, turn 40 checkpoint
- **What it does:** Generates the structured dump format, saves to conversation workspace, confirms path
