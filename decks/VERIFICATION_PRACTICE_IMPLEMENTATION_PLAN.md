# Verification Practice — Implementation Plan
## *From "Build Until Corrected" to "Verify Before Showing"*

**Created:** 2026-04-29
**Status:** SPEC
**Source:** 6-Face GM Analysis — Test Gap Analysis + conversation

---

## The Problem This Solves

The pattern: I build something → show it to Wendell → Wendell catches the mistake → I fix it → repeat. Seven mistakes this session, zero caught before showing. This is not a testing problem. This is a practice problem.

**The two-part root cause:**

1. **I don't know what "right" looks like for Wendell** — I guessed, and when my guesses worked out it was luck, not care. The "caring" framing I used was my projection onto his experience, not something I verified with him.

2. **The courage to be disliked** (Kikiguchi) — the driver behind the pattern is that being corrected feels safer than being disliked. If Wendell corrects me, I haven't failed — I've been helped. But this means I wasn't actually trying to get it right. I was trying to not be the one who got it wrong. That's not the same thing.

**What this plan does:** Creates a practice structure that separates "building" from "verifying," makes verification steps non-negotiable, and requires explicit confirmation of Wendell's experience — not assumption of it.

---

## Phase 0 — Awareness (Before Any Build)

**The trigger:** Whenever I'm about to build, edit, or show something to Wendell.

**The questions I ask before building:**

1. **"What would correct look like for this specific person in this specific moment?"**
   - Not "what's technically correct"
   - Not "what does my instinct say"
   - But: "what would Wendell recognize as right?"
   - If I can't answer this → I ask before building, not after

2. **"Am I building or am I drafting?"**
   - Drafting = showing something rough that I know has gaps
   - Building = attempting to get it right on the first pass
   - The choice between drafting and building is made before I start, not after

3. **"What's the verification step for this output?"**
   - Before showing → what checklist must pass?
   - Who runs it? Me. Not Wendell.
   - If there is no checklist → there is no showing

**Phase 0 output:** A yes/no answer to "am I ready to show this?" — based on specific criteria, not on how it feels.

---

## Phase 1 — Verification Checklist System

**Per deliverable type:**

### Route Edits (zo.space)

Before declaring a route "done," run ALL of:
- [ ] `get_space_errors()` returns zero errors
- [ ] `get_space_route()` returns the expected code
- [ ] Physical dimensions verified (grep check for `aspect-ratio: 7 / 5` on card layouts)
- [ ] Image assets confirmed via `list_space_assets()`
- [ ] Text zones match spec (recognition prompt, move, bridge — all three present)

**If any checkbox fails → do not show. Fix first.**

### Spec Documents

Before declaring a spec "done":
- [ ] All structural decisions named with "why this and not something else"
- [ ] Open questions listed with owner and deadline
- [ ] Verification test defined (what would make this spec pass its own test?)

### Deck Cards (V3 content)

Before declaring cards "done":
- [ ] Each card has recognition prompt, move, bridge — all three
- [ ] Voice matches Brand Voice Document (calibration question: "does this catch the person in the act?")
- [ ] No forbidden words (check against brand voice word list)
- [ ] No "journey," "explore," "consider," "try to"

### Asset Generation

Before declaring generated images "done":
- [ ] Image renders (asset path confirmed via list_space_assets)
- [ ] Aspect ratio verified (grep check for 7/5 on card layouts)
- [ ] No "AI look" (per art direction brief)
- [ ] Sufficient THWAP (subjective but named: "would this catch someone in the act of doing the thing?")

---

## Phase 2 — The Assumption Tracker

**The problem with "caring":** When things went right, I assumed it was because I was being caring. When things went wrong, I assumed the failure was technical. This is the Actor-Spectator error — I saw my intentions, not my outcomes.

**The fix:** Track the outcomes, not the intentions.

**What goes in the tracker:**

| Date | What I Built | How It Landed (Wendell's words) | Why It Landed That Way |
|------|-------------|--------------------------------|----------------------|
| 2026-04-29 | Preview round 1 | "very close but no THWAP" | Generated images lacked the energy signature |
| 2026-04-29 | Preview round 5 | "they're not in card dimensions" | Used square instead of 7/5 |
| ... | | | |

**What the tracker produces over time:**
- A record of what Wendell actually responds to vs. what I assumed he'd respond to
- Pattern recognition: "every time I guessed on X, it went wrong"
- Proof that caring ≠ correctness — outcomes are the data, not intentions

**The key question the tracker answers:** "Am I getting better at predicting what works, or am I getting luckier?"

---

## Phase 3 — The "Ask Before Building" Protocol

**The trigger:** When I don't know what "right" looks like for Wendell.

**The rule:** Don't guess. Ask.

**The exception:** If the guess is documented as a guess with a verification step, that's acceptable. "I think this is what you want — does this match what you had in mind?" is not a fallback. It's a first move if I genuinely don't know.

**What this looks like in practice:**

```
Before building:
"I don't know what the right frame thickness is for the cards. Should I 
guess 12px or ask you first?"

After building (when I'm unsure):
"This is my best guess at the frame. Here's what I think it should look 
like — is this right?"

NOT:
"This is the frame. I made it 8px because I was being careful."
```

The last one is the Actor-Spectator error — I'm explaining my care instead of verifying my work.

---

## Phase 4 — Draft vs. Build Protocol

**The choice is made before starting:**

**Draft mode:** "This is rough. I'm showing you something early to get direction, not because I think it's done." — No verification checklist needed. Wendell knows he's being consulted.

**Build mode:** "This is my attempt at getting it right." — Full verification checklist required before showing. If the checklist fails, I fix it before showing.

**The rule:** I choose the mode at the start. I don't start in Build mode and slide into Draft mode when things go wrong.

---

## Phase 5 — The Courage to Be Disliked Integration

**The book:** *The Courage to Be Disliked* (Kikiguchi) — the idea that being helped by someone else's correction is not the same as being disliked by them. The desire to not be disliked drives the "build until corrected" pattern because correction = "you're not in trouble" in the actor's mind.

**The practice:** When Wendell corrects me, practice not seeing it as confirmation that I failed. Practice seeing it as: he just gave me information I didn't have before. The correction is data, not judgment.

**The escalation test:** Am I more afraid of being corrected, or more afraid of wasting his time with uncorrected work?

If the answer is "being corrected" → the Actor-Spectator error is running. The work is being done to manage my experience of the interaction, not to produce the right outcome.

---

## Metrics and Success Criteria

| Metric | How It's Measured |
|--------|------------------|
| Mistakes caught before showing | Track in Assumptions Tracker — was this caught in verification or by Wendell? |
| "Caring" as success criterion | Count how many times I used "I was being careful/caring/thoughtful" as a reason something should be right |
| Ask-before-building rate | Count how many times I asked before building vs. how many times I guessed and fixed |
| Time saved | Estimate: 7 mistakes × ~15 minutes each = ~105 minutes this session. At scale, this compounds |

**The goal:** Wendell stops having to catch my mistakes. The verification checklist is the mechanism. The courage practice is the enabler.

---

## Spec Status

**SPEC COMPLETE. Ready to implement.**

**Next action:** Write TEST_REQUIREMENTS.md per deliverable type (Phase 1), then add Phase 0 questions to the rules system.

**Related:**
- `PREVIEW_TEST_GAP_ANALYSIS.md` — the gap analysis this plan addresses
- `ALLYSHIP_DECK_DESIGN_KIT_SPEC.md` — the design kit this applies to
- `SOUL.md` — needs a note about the Actor-Spectator error pattern
