# Deck Spec V3 — Structural Resolutions + App Layer
## *Two Open Decisions Closed + The App as the Real Product*

**Source:** WENDELL_ALLY_DECK_SPEC_6FACE_ANALYSIS.md, 2026-04-28
**Applies to:** WENDELL_ALLY_DECK_SPEC.md + WENDELL_ALLY_DECK_SPEC_ARCHITECTURAL.md
**Status:** COMPLETE — V3 design contract finalized

---

## Resolution 1 — ♦️ Clean Up: Option C, With One Refinement

**Decision:** Each card explicitly names its mode in the recognition prompt.

**Option C confirmed.** The recognition prompt does the work of distinguishing the mode. No structural overhead, no physical deck complexity. The card tells the reader what game it's in.

**Refinement added:** Cards whose recognition prompt is about the TARGET (other person's self-sabotage) get a subtle visual marker — a small diamond icon in the recognition prompt corner. This is optional for the physical deck (print consideration) and native to the app UI. It serves the ally in the moment who is scanning cards quickly.

**Resulting ♦️ structure:**

| Mode | Recognition question | Card type | Example prompt |
|------|---------------------|-----------|---------------|
| Self-clearing | "Is MY self-sabotage blocking this allyship?" | The card names the ally's pattern | "Did you just say 'I'm not sure I have anything to offer' before offering anything?" |
| Target-reading | "Does THE PERSON I'm helping have self-sabotage blocking them?" | The card names the target's pattern | "Did they just decline help they actually need — because accepting feels dangerous?" |

**Both modes in the same suit, same deck position (♦️), same card count (10).** The ally learns to read both once they're in the suit.

---

## Resolution 2 — Face Cards: Scales, Not Sequence

**Decision:** J/Q/K are the same move at three scales. Not Activate → Deepen → Complete (linear). Scale 1 → Scale 2 → Scale 3 (simultaneous).

**What the move is:**
> Name what you notice. Let it land without fixing it. Return to the moment.

**The three scales:**

| Card | Scale | The move | Recognition prompt |
|------|-------|---------|-------------------|
| **♦️ J** | Individual moment | Name one thing you just noticed in this exchange | "What's the most recent thing you noticed — and did you say it?" |
| **♦️ Q** | Session | After a session of allyship work, name what's actually shifted | "What happened in this conversation that wasn't here at the start?" |
| **♦️ K** | Relationship | At a milestone or transition, name what this relationship has taught you | "What have you learned about this person that you couldn't have learned any other way?" |

**What changes:** The face cards are no longer a progression. They're a calibration tool. The ally (or the target) reaches for the scale that matches the moment they're in — not the next card in a sequence.

**What stays:** J still activates (something just happened). Q still deepens (something just shifted). K still completes (something just concluded). But the sequence is chosen by the moment, not by the card order.

---

## The App as the Real Product

**What the physical deck is:** A field guide. 52 cards, poker size, $25-35. In your pocket or purse. For the moment that matters.

**What the app is:** The full product. Everything the physical deck points to but can't contain.

**Why this matters for design:**

The physical deck is a trailer. It creates the desire. The app delivers what the trailer promises. This means:

1. **The physical deck and the app are one product, two form factors.** Not two separate products. The app is the deck with more pages turned, more branches taken, more depth available. Someone who buys the deck and loves it should feel the pull toward the app. Someone who downloads the app and uses it daily should feel the pull toward the physical artifact.

2. **The app can do things the deck can't.** Specifically:
   - **Branching:** "I noticed my ally just did [this]. What card do I reach for next?" The app can offer contextual next-cards based on what just happened. The deck can't.
   - **Audio/video:** A 30-second audio note from Wendell on each card. The ally hears the voice, not just the words. The card gains warmth through the recording.
   - **Bars-engine wiring:** The app can log which cards the ally draws, track patterns over time, surface insights about their development arc. "You've drawn the 'check your capacity' card 11 times in the last month. That's data." The deck can't.
   - **The 6 belief unlock sequences:** Each of the 6 self-sabotaging beliefs can have a full sub-routine in the app — a short guided session that walks the ally through recognizing and dissolving that specific belief. The card names the belief. The app takes them through it.
   - **The listening practice loop:** The app can offer a "practice with me" mode — the ally listens to a scenario, tries the response, then hears what Wendell would have wanted. Not a test. A practice.

3. **The app is free or low-cost.** The physical deck is the revenue product. The app is the depth that makes the deck worth buying — and the reason the homies don't just screenshot the cards.

**App tier suggestion (for later):**

| Tier | Price | What's included |
|------|-------|----------------|
| **Free** | $0 | All 52 card prompts, audio on each card, no branching |
| **Pro** | $5-10/mo | Branching, practice loops, 6-belief unlock sequences, bars-engine tracking |
| **Gift** | Included with physical deck purchase | Pro access for 1 year, card linked to deck purchase |

---

## Updated Product Architecture

```
PHYSICAL DECK                    APP
─────────────                    ───
52 cards, poker size       ←→    Full card library + audio
Recognition + Move + Bridge      Contextual branching per card
Solo + dyad play modes     ←→    Solo + dyad + group play modes
Static practice arc        ←→    Adaptive practice arc
No tracking               ←→    Pattern tracking + bars-engine wiring
Limited warmth (text)     ←→    Audio warmth (Wendell's voice on each card)

PHYSICAL DECK (revenue)    ←→    APP (depth + retention)
$25-35                            Free tier + Pro subscription
```

---

## Updated Suit Architecture (Final)

| Suit | Function | 10 cards cover |
|------|----------|--------------|
| ♣️ Wake Up | Listening — track where the other person is AND where they're trying to go | 10 moments of good listening |
| ♦️ Clean Up | Self-clearing + target-reading — dissolve YOUR blocker, READ the other's blocker | 10 moments across both modes |
| ♥️ Grow Up | Capacity expansion — increase your developmental range so the allyship can land | 10 capacity expansions |
| ♠️ Show Up | Doing the work — specific, honest, bounded offers that don't collapse | 10 doing-it moves |

**Face cards (J/Q/K) are the same move at three scales: moment / session / relationship.**
**♦️ has two modes (self and target) named in each card's recognition prompt.**
**Suits are a palette, not a sequence.**

---

## Spec Status

**This document + WENDELL_ALLY_DECK_SPEC.md + WENDELL_ALLY_DECK_SPEC_V2_CHANGES.md = complete V3 design contract.**

No further structural decisions needed. V3 ♣️ Wake Up cards can be written.

---

*V3 design contract complete. Ready for card writing.*
