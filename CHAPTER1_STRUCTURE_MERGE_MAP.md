# Chapter 1 Structure — Merge Map
**Created:** 2026-04-14
**Purpose:** Where each new system integrates into the existing Chapter 1 outline

---

## The Core Question This Answers

Where does THE FOREST (8 Gates/Village structure), EMOTIONAL ALCHEMY (5 channels + 15 moves), and the renamed VOICES framework go — and in what order?

---

## Where Each System Lives

| System | Source File | Primary Chapter |
|--------|------------|-----------------|
| The Forest / 8 Gates | `bars-engine/docs/handbook/THE_FOREST.md` | Ch 1 (origin) + Ch 7 (integration) |
| 5 Emotional Channels | `bars-engine/.agent/context/emotional-alchemy-interfaces.md` | Ch 1 (introduced) + Ch 7 (mastered) |
| 15 Alchemy Moves | `bars-engine/.agent/context/emotional-alchemy-ontology.md` | Ch 1 (first taste) + each chapter (practice) |
| Renamed Voices (8 Gates) | `bars-engine/docs/handbook/THE_FOREST.md` | Ch 1 (Gate 1) + Ch 7 (all 8) |
| 6 Game Master Faces | `bars-engine/.specify/specs/game-master-face-sentences/spec.md` | Ch 1–6 (one per chapter) |
| WAVE Loop | `MTGOA_TEAL_080525.md` (existing) | Ch 1 (mechanical intro) |
| BARs Reflection | `bars-engine/docs/handbook/BARs.md` | Ch 1 (first prompts) |
| Vibeulons | `bars-engine/docs/handbook/BARs.md` | Ch 7 (integration + game connection) |

---

## Proposed Merge — Chapter 1 Structure

### CURRENT Chapter 1 Opening (from MTGOA_TEAL_080525.md):
```
Introduction — What is the Allyship Game?
MetaSkills
  Infinite Arcade Metaphor
  Games of Chance / Skill / Passion
  Tokens (Emotional Resources + Time)
  Tickets (Emotional Payout)
  WAVE Loop
Chapter 1 — Waking Up To Your Superpower
  Opening Hook (Wichita origin story)
  Defining an Allyship Superpower
  What Makes a Superpower? (Innate / Honed / Playstyle)
  Examples of Allyship Superpowers
  The Role of Backstory
  Reflection Exercise
  Meeting the Inner Resistance
  Superpowers Are Rooted in Leverage
  The Shortcut to Mastery
  The Power of Playstyle
  Key Takeaway
```

### MERGED WITH — New Systems — Recommended Order:

```
CHAPTER 1: THE FOREST AND THE VILLAGE
=====================================
[NEW — URGENCY SECTION] ← "The World Is Not Fine"
  → Sits BEFORE the Infinite Arcade — primes the reader's dissatisfaction
  → Sets up why the Forest is necessary
  → Channels: Fear → Frustration → Grief → Anger → Commitment
  → Satisfied state at end: Excitement (opportunity)

[KEPT — Infinite Arcade] ← "The Game You're Entering"
  → Introduce tokens, tickets, WAVE loop
  → Shaman face is the interpretive lens here (mythic/threshold language)
  → This is the village entry point

[NEW — Village/Forest Structure] ← "Why We Go to the Forest First"
  → THE FOREST framework doc goes here
  → Name the failure modes: (1) trying to fix village without Forest, (2) anti-hero trap
  → This is the structural explanation — WHY this book is different

[KEPT — Origin Story] ← "Where This Framework Came From"
  → Wichita story stays (it's already strong)
  → Connect to Shaman face explicitly: "This is what learning to feel the field looks like in practice"
  → The origin story IS the first example of someone who went through the Forest and came back

[NEW — 8 Gates Preview] ← "The 8 Gates of the Forest"
  → Introduce all 8 gates briefly (names + what each guards)
  → Protectors appear as: "The voice that says 'it is not safe here'"
  → Emphasize: Gate 8 (Vulnerable Child) is where the superpower lives
  → Promise: "We'll meet each gate in depth. This chapter starts with Gate 1."

[NEW — Gate 1: Protector (Full Passage)] ← "The First Voice"
  → Full Protector Gate section (from `CHAPTER1_PROTECTOR_GATE_DRAFT.md`)
  → This is the PROOF that the framework works — a complete teaching in one gate
  → Body-first: "the body decides before the mind catches up"
  → Epiphany Bridge structure: Old Story → Encounter → Pivot → New Story
  → BARs reflection prompts at end

[KEPT — Superpower Definition] ← "The Gift in the Damage"
  → Keep existing teaching on what a superpower is
  → Connect to Vulnerable Child (Gate 8): "Your superpower is what the Vulnerable Child has been holding this whole time"
  → This is the payoff — the reader understands their origin IS their superpower

[NEW — 5 Emotional Channels Introduction] ← "The Weather of the Forest"
  → Name all 5 channels briefly
  → Show them in table format (from Passage 3 voice notes)
  → Emphasize: "Every gate has weather. The channels color how each voice speaks."
  → This is the mechanical spine introduced early so it can be used throughout

[KEPT — Reflection Exercise] ← "Finding Your Origin Story"
  → Keep existing reflection prompts
  → Add new prompt: "Which gate have you been avoiding? What is it protecting you from?"
  → Add new prompt: "What does your body feel like when you're in the village vs. the Forest?"

[NEW — Chapter 1 BARs Prompts] ← "Your First BARs"
  → 3 prompts: Breakthrough / Action / Reflection
  → Breakthrough: "What did you realize in this chapter?"
  → Action: "What is one thing you'll do differently starting today?"
  → Reflection: "How did the material land in your body? Where do you feel it?"
```

---

## What Gets Cut or Moved

| Existing Content | Decision | Reason |
|-----------------|---------|--------|
| "Games of Chance/Skill/Passion" (detailed) | Move to Chapter 0 | These are framework, not chapter 1 urgency |
| "Meeting Inner Resistance" (detailed) | Integrate into Gate 1 passage | The Protector IS the inner resistance |
| "Superpowers Are Rooted in Leverage" | Keep short | Still useful, tighten it |
| "The Shortcut to Mastery" | Cut | Replaced by Forest/Village structure |
| "Power of Playstyle" | Cut | Can be a sidebar or appendix reference |

---

## What Gets Added (New)

| New Content | Source | Priority |
|------------|--------|---------|
| Urgency section | `CHAPTER1_URGENCY_DRAFT.md` | P0 — write first |
| Forest/Village structure | `bars-engine/docs/handbook/THE_FOREST.md` | P0 — integrate here |
| Gate 1: Protector (full) | `CHAPTER1_PROTECTOR_GATE_DRAFT.md` | P0 — proof of concept |
| 5 Emotional Channels table | `CHAPTER1_EMOTIONAL_ARCHITECTURE.md` | P1 — mechanical spine |
| 8 Gates preview | New drafting needed | P1 — sets up rest of book |
| Chapter 1 BARs prompts | From this map | P2 — end of chapter |

---

## Priority for Tomorrow

**P0 (must exist before drafting the rest of Chapter 1):**
- [ ] Urgency section (`CHAPTER1_URGENCY_DRAFT.md` exists ✅)
- [ ] Forest/Village structure integrated into opening
- [ ] Gate 1 Protector passage (`CHAPTER1_PROTECTOR_GATE_DRAFT.md` exists ✅)

**P1 (needed before Chapter 2):**
- [ ] 5 Emotional Channels system
- [ ] 8 Gates full preview section
- [ ] Voice calibration notes applied to the draft (`voice-calibration-notes.md` exists ✅)

**P2 (needed before manuscript goes to review):**
- [ ] New BARs prompts
- [ ] Cut/move decisions applied to existing content
- [ ] Regent face (Chapter 3) gets full treatment

---

## The Emotional State the Reader Is In After Chapter 1

| Channel | Starting State | Ending State | Move Used |
|---------|--------------|-------------|----------|
| Fear | Anxious about world | Excited (opportunity) | Step Through |
| Anger | Frustrated by failed allyship | Committed (boundary honored) | Achieve Breakthrough |
| Sadness | Grieving wasted effort | Poignantly resolved | Reclaim Meaning |
| Neutrality | Bored/apathetic | Curious | Stabilize Coherence |

**Chapter 1 ends in the reader in a state of COMMITTED EXCITEMENT** — not naive optimism, but the excitement of someone who has a map and knows the terrain.

---

## Files Referenced
- `CHAPTER1_URGENCY_DRAFT.md` ✅
- `CHAPTER1_PROTECTOR_GATE_DRAFT.md` ✅
- `CHAPTER1_EMOTIONAL_ARCHITECTURE.md` ✅
- `voice-calibration-notes.md` ✅
- `bars-engine/docs/handbook/THE_FOREST.md` ✅
- `MTGOA_TEAL_080525.md` (existing manuscript)
