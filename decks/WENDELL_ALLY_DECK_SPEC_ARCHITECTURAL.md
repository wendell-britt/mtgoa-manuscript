# Deck Spec Architectural — Structural Changes
## *The Two Changes That Require a New Document*

**Source:** WENDELL_ALLY_DECK_SPEC_6FACE_ANALYSIS.md, 2026-04-28
**Applies to:** WENDELL_ALLY_DECK_SPEC.md
**Status:** Architectural — for V3 card writing

---

## Why These Need a Separate Document

These changes affect the core structure of the deck. They are not in-place edits — they change how the suits relate to each other and what each suit is for. They need their own design contract before any cards get written against them.

---

## Structural Change 1 — ♦️ Clean Up: The Split

### What the Interview Said

*"Clean up also unblocks the allyship target. If your target has self-sabotage, none of your allyship will land."*

*"People can't give what they don't have. They can't take me to anywhere they haven't been before."*

*"When their feelings matter more than mine and I have to hold them as they are trying to help me."*

### What It Means

The ♦️ suit was designed to clear the ally's self-sabotaging beliefs — the 6 beliefs held by the Controller gate. That's one function.

But the interview reveals a second function: recognizing when the PERSON they're helping has self-sabotage, and adjusting the approach accordingly. If the ally can't read self-sabotage in the other person, they will keep offering help that keeps failing — and not understand why.

### The Two Modes

**♦️ Clean Up (Self-Clearing):**
- Question: "Is MY self-sabotage blocking this allyship?"
- Move: Surface and dissolve one of the 6 beliefs
- Cards: For working on your own patterns
- Example recognition prompt: "Did you just say 'I'm not sure I have anything useful to offer' before offering anything?"

**♦️ Clean Up (Target-Reading):**
- Question: "Does THE PERSON I'm helping have self-sabotage blocking them?"
- Move: Recognize the pattern in the other, adjust the approach, find the crack
- Cards: For reading what's actually blocking the other person
- Example recognition prompt: "Did they just decline help they actually need — because it feels safer than accepting it?"

### Design Decision Required

**How do we represent two modes within one suit?**

Option A — Split into two ♦️ halves:
- Cards 1-5: Self-clearing
- Cards 6-10: Target-reading
- Simple implementation, clear structure

Option B — Add a second ♦️ with different color backing:
- Two ♦️ cards in the deck
- One answers to self-clearing, one to target-reading
- More complex physically, clearer in use

Option C — Each card explicitly names its mode in the recognition prompt:
- No structural change
- Cards are distinguished by their recognition prompt, not their suit
- Simplest implementation — the card tells you which mode it's in

**Recommendation: Option C.** Let each card carry its mode in the recognition prompt. No structural overhead. The card does the work of distinguishing itself.

### Card Count Implication

If ♦️ has two modes at 5 cards each: 10 cards total for ♦️. If ♥️ and ♠️ get similar scrutiny, the 52-card constraint may reduce further. The Regent flagged this in the 6-face analysis: the right cards matter more than the full deck.

---

## Structural Change 2 — Suit Sequence: Simultaneous, Not Linear

### What the Spec Currently Says

Section 3.5 presents the suits as a sequence:
> ♣️ Wake Up (1-10) → ♦️ Clean Up (1-10) → ♥️ Grow Up (1-10) → ♠️ Show Up (1-10)

This implies the ally reads cards in order, develops in sequence, uses one suit at a time.

### What the Moment Actually Requires

In a single 3-minute window, an ally might need to:
1. Notice their own self-sabotage is active (♦️ self-clearing)
2. Notice the other person's self-sabotage is blocking the help (♦️ target-reading)
3. Stay in the conversation despite discomfort (♥️ Grow Up)
4. Make a specific, honest offer (♠️ Show Up)
5. Track whether the offer landed (♣️ Wake Up)

All four suits, all at once, in three minutes.

The sequential suit structure will produce sequential cards. Sequential cards can't serve a non-linear moment. The suit structure is the wrong metaphor.

### The Alternative Model

**Suits are not a sequence. Suits are a palette.**

The ally reaches for the color the moment needs — not in order, not one at a time. The deck provides options. The moment decides which card gets drawn.

This doesn't mean the deck is random. The recognition prompt is the filter: "Would a person in the moment know to reach for this card?" If yes, the card is in the right deck. Whether they draw it before or after other cards is not controlled by the suit sequence — it's controlled by the moment's needs.

### What This Changes

1. **Card ordering within suits stays** — the learning arc within each suit still has an order. Wake Up cards 1-10 still progress from "catch the override" to "name what you're noticing." That internal order is the arc.

2. **Suit order across suits goes** — the ♣️ → ♦️ → ♥️ → ♠️ sequence is removed from the spec. The suits are presented as parallel, not sequential.

3. **The face card sequence goes** — J (Activate) → Q (Deepen) → K (Complete) is a linear sequence. In a simultaneous model, the face cards need to be understood differently. They are not a progression. They are the same move at different scales: individual moment (J), session (Q), relationship (K). This needs a redesign.

4. **The entry trigger is still the moment** — the buyer enters through recognition. The suit structure is the ally's palette once they're in, not the buyer's path through the product.

---

## What Stays the Same

- Three-component card anatomy (Recognition / Move / Bridge)
- Three-test framework (Recognition / Action / Allyship bridge)
- Field guide format (pocket, phone)
- Specific-first / general-second sequencing
- Physical form constraint ($25-35, poker size)

---

## Architectural Summary

| Change | Before | After |
|--------|--------|-------|
| ♦️ suit function | Self-clearing only | Self-clearing + target-reading |
| ♦️ card structure | 10 cards, one mode | 10 cards, each names its mode |
| Suit sequence | Linear ♣️→♦️→♥️→♠️ | Parallel palette model |
| Face cards | J→Q→K progression | Same move, three scales |
| Card count constraint | 52 (forced) | Right cards, not full deck |

---

## Spec Status After These Changes

**WENDELL_ALLY_DECK_SPEC.md + WENDELL_ALLY_DECK_SPEC_V2_CHANGES.md + this document = complete V3 design contract.**

V3 cards can now be written against the complete design contract.

---

*Architectural spec complete. Next: V3 ♣️ Wake Up cards.*
