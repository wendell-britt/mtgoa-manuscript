# Wake Up Suit — Gap Analysis + Implementation Spec
## *V2 → V3: What Exists vs. What Needs to Exist*

**Based on:** 6-Face GM Analysis, 2026-04-28
**Method:** Map current state against each face's requirements, identify gaps, spec V3

---

## How to Read This Document

**"Current" = V2 state.** "Target" = what the 6-face analysis requires. "Gap" = what's missing or wrong. "Spec item" = what V3 must implement to close the gap.

Each face's assessment is weighted equally — the Sage's synthesis is the tiebreaker where faces conflict.

---

## Gap Summary Table

| # | Gap | Severity | Owner | 
|---|-----|----------|-------|
| G1 | Card text too long — main text exceeds 20 words | 🔴 Critical | Architect |
| G2 | Why/When/Allyship paragraphs appended to each card | 🔴 Critical | Architect |
| G3 | Card order doesn't follow milestone developmental arc | 🔴 Critical | Architect |
| G4 | Cross-face references in card text | 🟠 High | Regent |
| G5 | Group language in cards labeled solo-playable | 🟠 High | Regent |
| G6 | Easy/Medium/Hard differentiated by word count, not intensity | 🟠 High | Challenger |
| G7 | "Feel" used as verb on cognitive cards (♣️ 3, ♣️ 9) | 🟠 High | Challenger |
| G8 | Psychographic too narrow — fawning types only | 🟡 Medium | Challenger |
| G9 | Allyship dyad absent — only self-side present | 🟠 High | Diplomat |
| G10 | Anger channel missing from suit | 🟡 Medium | Shaman |
| G11 | Body as evidence removed — somatic overcorrected against | 🟡 Medium | Shaman |
| G12 | "How to Read" preamble required for cards to function | 🔴 Critical | Regent |

---

## Detailed Gaps

### G1 — Card text too long
**Current:** ♣️ A Easy: "Name one thing you just did in this interaction — before you decided whether it was right."
**Count:** 17 words — PASSES borderline
**But ♣️ A Medium:** "Name the thing you just said or did — and notice whether it was what you actually felt or what you thought was expected."
**Count:** 23 words — FAILS, max 20
**And ♣️ 4 Medium:** "Name one thing you believe about allyship that you inherited — before you decided whether it was true."
**Count:** 21 words — FAILS, max 20
**Most Hard variants:** 25+ words — all FAIL

**Spec requirement:** Main text max 20 words. Context and Result are additional single lines, not counted in the 20.

---

### G2 — Why/When/Allyship paragraphs appended
**Current architecture:**
```
Card title
Main text (one sentence)
Why: paragraph
When: paragraph
Allyship use: sentence
```

This produces a card that requires 5 elements to function. The user has to read the preamble to understand how to read the card. The card cannot stand alone.

**Target architecture:**
```
Card title
Main text (one sentence, max 20 words)
Context: one line (specific scenario)
Result: one line (what shifts)
```

All three answers are embedded IN the card text, not appended to it. The preamble is gone. The "How to Read" section is one line.

**Spec requirement:** Delete all Why/When/Allyship use paragraphs. Extract the content into compressed Context + Result lines. If a card's meaning isn't recoverable from 20 words + 2 lines, the card doesn't have a center — rewrite it.

---

### G3 — Card order doesn't follow milestone arc
**Current order:** A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

**Target order (developmental arc):**
1. A — I just did something I'm not aware of
2. 2 — I do this by default, not by design
3. 4 — I inherited this belief
4. 6 — I know but don't do
5. 3 — Here's what it costs
6. 5 — Here's who goes missing because of it
7. 7 — And it's from my history
8. 8 — And I'm doing it to them right now
9. 9 — And I've been deferring the naming
10. 10 — And the room knows but isn't saying
J — Performance is visible before I'm in it
Q — Noticing without deciding keeps the pattern
K — The cost of performance is higher than letting it go

**Card 3 and 4 are misplaced relative to the milestone logic.** Card 3 (Feel the cost) should come AFTER Card 6 (Know but don't do) — cost only lands after knowing. Card 4 (Name the inheritance) should come early — the inheritance is the root of the pattern.

**Spec requirement:** Reorder all 13 cards to match the developmental arc above. The sequence tells a story. Each card builds on the last.

---

### G4 — Cross-face references in card text
**Current:** "The Diplomat who can't name their walk-away price has no price."
**Current:** "The Challenger's first move is to name what others won't."
**Current:** "The Regent holds the structure while the Diplomat holds the field."

These references are embedded in card text. They require knowledge of the other suits to understand. The Wake Up suit must stand alone.

**Spec requirement:** Remove all face-name references from card text. Cross-suit connections are handled in the Face Lenses section only. Card text should be comprehensible to someone who has never heard of the other suits.

---

### G5 — Group language in solo-playable cards
**Current:** "Let the room receive that." / "The room knows but isn't saying." / "The room as a whole."

If the deck is solo-playable, these phrases need alternatives for solo play. "Let the room receive that" could become "Say it out loud and let it land without explanation."

**Spec requirement:** Every card with group language gets a solo-variant phrase. Mark group vs. solo with a tag: `[solo]` or `[group]`. Default to solo. Group language only in group-play variants.

---

### G6 — Easy/Medium/Hard = word count, not intensity
**Current:**
- Easy: "Name one thing"
- Medium: "Name one thing and notice whether"
- Hard: "Name the last time and notice whether and track across three"

Harder = more words = more cognitive load. This is not intensity. This is volume.

**Target intensity markers:**
- Easy: Near-surface. Name the pattern. No admission required.
- Medium: Mid-pattern. Admit you're in it. Some cost acknowledgment.
- Hard: Near-wound. Close to the thing you're avoiding naming. High personal exposure.

**Example — ♣️ A reworked:**
- Easy: "Name one thing you just did." (surface — what behavior)
- Medium: "Name one thing you just did — and whether it was automatic." (mid — automatic vs. chosen)
- Hard: "Name the thing you just did that you already knew you were doing." (near-wound — the awareness-without-action pattern)

**Spec requirement:** Redefine Easy/Medium/Hard by proximity to wound, not volume. Each variant should feel like a different emotional risk, not a different word count.

---

### G7 — "Feel" wrong verb on cognitive cards
**♣️ 3 — Feel the cost:** The practice is intellectual cost-tracking, not somatic feeling. "Feel" will trigger "I feel like I should help" patterns in fawning types.

**♣️ 9 — Feel what you've been deferring:** Same problem. This is about naming deferred decisions, not somatic feeling.

**Spec requirement:** Rename to Track (♣️ 3) and Name (♣️ 9). "Feel" is reserved for cards where the practice genuinely requires the body as evidence — not as meditation, as data source.

---

### G8 — Psychographic too narrow
**Current:** Cards written for Enneagram 2/6/6 with fawning patterns. Hard = "go deeper into vulnerability."

**The other half of the audience:** Orange/Red types who harden instead of fawn. For them, the allyship problem is too much edge and not enough warmth. Hard = "softer" not "deeper." A hard variant that says "go closer to the wound" would be alienating to someone whose wound is the inability to be soft.

**Spec requirement:** Each card needs two psychographic variants, not one. Tag cards:
- `[fawning]` = for 2/6/6 types (default if untagged)
- `[hardening]` = for Orange/Red types who need to soften

The card asks the same question but from opposite entry points. This is not Easy/Medium/Hard — it's a dimension the player self-selects on.

---

### G9 — Allyship dyad absent
**Current:** Every card looks at the self side only. "Name what it cost you." "Name what you inherited." "Notice what you did."

**The missing half:** What does your pattern do to the person you're allied to? When you override yourself, what happens to them? When you perform care, what do they receive?

**Spec requirement:** At least 4 cards (A, 3, 5, 8) must include the other person as a named presence, not an abstract "them." The question "what does my pattern do to them?" should be visible in the card text or context line.

Example — ♣️ A, dyad-aware version:
- Easy: "Name one thing you just did — and notice whether it was for them or for you."
- Context: "After someone tells you about a problem and you feel the urge to fix it."
- Result: "You see the difference between what they need and what you're doing."

---

### G10 — Anger channel missing
**The psychographic was psychospiritually abused by allyship culture.** This means there is specific, named anger at: being told to make themselves small, being given bad tools, being depleted by a framework that didn't resource them.

No card gives access to this anger. The suit is all pattern-naming and cost-tracking. No card says: *You were hurt by this. Name the thing that hurt you.*

**This is not a gap to fill in every card.** One or two cards in the suit should have a variant that accesses the wound-at-the-abuse layer. This is a Hard variant reserved for players who've been through it.

**Spec requirement:** Add one [anger] variant to at least two cards — cards 3 and 6. These access the wound at the layer of spiritual abuse, not just the pattern layer.

---

### G11 — Body as evidence overcorrected
**V1 was too somatic** (feet on floor, three breaths). V2 removed somatic almost entirely. The body is actually relevant to allyship — as a data source for "is this my pattern or is this real?"

**The right use of body:** Not as a meditation object. As a piece of evidence. "Where do you feel that in your body?" is relevant when the answer would disambiguate between "this is my pattern reacting" and "this is something real happening now."

**Spec requirement:** In at least 3 cards, include "and where in your body" as a variant marker — not a main instruction, a disambiguation tool. Mark with `[body]` tag.

---

### G12 — "How to Read" preamble required
**Current state:** The cards cannot be used without reading the preamble first. If someone draws ♣️ 7 without context, they don't know what to do with it.

**Target:** A child could draw a card and do what it says without any introduction.

**Spec requirement:** Delete the "How to Read Each Card" section. Replace with one line below the suit title: *"Each card names a pattern and gives you the move to catch it."* If a card needs a manual to function, rewrite the card.

---

## Implementation Spec for V3

### Format Architecture

```
# ♣️ Wake Up — [Suit tagline, one line]

[One-line instructions — not a preamble]

### ♣️ [N] — [Pattern name]

**Easy:** [Main text — max 20 words] [tags]
*Context: [one line — specific scenario]*
*Result: [one line — what shifts]*

**Medium:** [Main text — max 20 words] [tags]
*Context: [one line]*
*Result: [one line]*

**Hard:** [Main text — max 20 words] [tags]
*Context: [one line]*
*Result: [one line]*

### ♣️ J / ♣️ Q / ♣️ K — [Name]
[Card text — max 2 sentences. Constraint line if applicable.]
```

**Tags:** `[solo]` `[group]` `[fawning]` `[hardening]` `[body]` `[anger]`
Multiple tags allowed. Default is solo + fawning if untagged.

---

### Card Order (Locked for V3)

| Card | Pattern | Milestone |
|------|---------|-----------|
| ♣️ A | Catch the override | I just did something I'm not aware of |
| ♣️ 2 | Spot the game move | I do this by default, not by design |
| ♣️ 4 | Name the inheritance | I inherited this belief |
| ♣️ 6 | Know but don't do | I know but don't do |
| ♣️ 3 | Track the cost | Here's what it costs |
| ♣️ 5 | Notice who's absent | Here's who goes missing |
| ♣️ 7 | Find the split | And it's from my history |
| ♣️ 8 | Catch the savior | And I'm doing it to them |
| ♣️ 9 | Name the deferral | And I've been deferring the naming |
| ♣️ 10 | See the weather | The room knows but isn't saying |
| ♣️ J | Activate | Performance is visible before you're in it |
| ♣️ Q | Deepen | Noticing without deciding keeps the pattern |
| ♣️ K | Complete | The cost of performance is higher than letting it go |

---

### Quality Gates (must pass before card is final)

**QG1 — Self-contained:** Can the card be played by someone who has never read the deck? Test: cover the context line, read only the main text. Is it actionable? If no, rewrite.

**QG2 — Allyship-specific:** Could this card fire in a meditation app with no allyship content? If yes, it's wrong. Test: swap "allyship" for any other context — does the card still make sense? If yes, it's not allyship-sharpped enough.

**QG3 — Solo-playable:** Does every card work alone? If the card requires a group to receive or witness it, it must have an explicit solo variant.

**QG4 — Word count:** Main text ≤ 20 words. Context ≤ 20 words. Result ≤ 20 words. No exceptions.

**QG5 — Intensity, not volume:** Easy/Medium/Hard differentiated by proximity to wound. A reader should be able to tell which variant is Hard without counting words.

**QG6 — Dyad present:** At least 4 cards (A, 3, 5, 8) include the other person explicitly. "Them" is not enough — the other person must be a named presence in the scenario.

---

### Tags Reference

| Tag | Meaning | Required? |
|-----|---------|-----------|
| `[solo]` | Works alone | Default |
| `[group]` | Requires group to receive | Only for group-specific cards |
| `[fawning]` | Fawning/2/6/6 entry point | Default |
| `[hardening]` | Hardening/Orange/Red entry point | One per suit minimum |
| `[body]` | Involves body as data source | 3+ cards per suit |
| `[anger]` | Accesses wound-at-abuse layer | 2 cards per suit |

---

## What V3 Is Not

- Not new content — the pattern names are correct, keep them
- Not a redesign of the milestone framework — that's sound
- Not a rewrite of the psychographic — that's accurate
- V3 is a compression and architecture pass on the existing V2 content

## What V3 Is

- 13 cards, compressed to spec format
- All 12 gaps closed
- All 6 quality gates passed
- Card order matches milestone arc
- Solo-play verified for every card
- Allyship dyad present in at least 4 cards

---

## Next Action

**Build V3** — apply the format architecture, card order, quality gates, and tag system to the V2 content. The V2 content is the source. The spec is the filter. Every V2 card that can't pass the quality gates gets rewritten, not carried over.