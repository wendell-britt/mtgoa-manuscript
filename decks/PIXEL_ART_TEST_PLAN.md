# Pixel Art Production Test Plan
## *How to validate the system before full production*

---

## The Test Question

Does the spec actually produce cards that:
1. Look like the same deck (coherence)
2. Feel like different suits (distinction)
3. Have THWAP energy (taste)

---

## Test Set — 8 Cards

**Round 1 — Suit Coherence (4 cards):**
- ♣️ A — Catch the override (Soft Attention)
- ♦️ A — Not good enough (Threshold Weight)
- ♥️ A — Stay with it (Safe Expansion)
- ♠️ A — Make a specific offer (Fire and Peace)

**Round 2 — Within-Suit Arc (♣️ only):**
- ♣️ 2 — Spot the smooth (A-K progression)
- ♣️ 5 — Ground before you name (A-K progression)
- ♣️ 10 — Receive without redirecting (A-K progression)
- ♣️ K — Moment Scale (scaled)

---

## Generation Template

Using the Prompter's Script from `PIXEL_ART_PRODUCTION_SPEC.md`:

**♣️ A — Catch the override:**
```
Two figures face to face in warm pixel art, cute witchy aesthetic, cozy magical daily ritual vibe
— held breath, quiet presence, before-speaking moment
— 1 figure, intimate close-up, enclosed but not claustrophobic
— intimate scale, warm interior light, tactile worn texture, soft vignette
— warm ivory dominant, sage green secondary, gentle pixel noise
— no text, soft dithering, cozy warmth
```

**♦️ A — Not good enough:**
```
Single figure at threshold, small object held in warm pixel art, cute witchy aesthetic, cozy magical daily ritual vibe
— threshold weight, block being named, something being set down
— 1 figure at edge, intimate close-up, tension in composition
— intimate scale, warm interior light, tactile worn texture, warm shadow tones
— dusty rose dominant, deep warm brown shadows, gentle pixel noise
— no text, soft dithering, cozy warmth
```

**♥️ A — Stay with it:**
```
Two figures in warmth, hands joining in warm pixel art, cute witchy aesthetic, cozy magical daily ritual vibe
— safe expansion, door opening, quiet earned warmth
— 2 figures, open composition, breathing room
— intimate scale, warm amber light, tactile worn texture, soft vignette
— warm amber dominant, rose highlights, ivory background
— no text, soft dithering, cozy warmth
```

**♠️ A — Make a specific offer:**
```
Hand reaching toward another hand in warm pixel art, cute witchy aesthetic, cozy magical daily ritual vibe
— fire and peace, doing, showing up, honest handoff
— hand reaching, forward-leaning composition, grounded
— intimate scale, warm interior light, tactile worn texture
— deep red dominant, warm cream background, gentle pixel noise
— no text, soft dithering, cozy warmth
```

---

## Success Criteria

| Test | Pass | Fail |
|------|------|------|
| Deck coherence | ♣️ A and ♠️ A clearly same deck | They could be different decks |
| Suit distinction | ♣️ and ♠️ clearly different energy | They feel the same |
| ♣️ internal arc | ♣️ A and ♣️ K feel like same suit, different scale | They feel disconnected |
| THWAP | Each card lands | The card is forgettable |
| Warmth | Card reads as warm throughout | Cold spots, clinical feel |

---

## Decision Points After Round 1

If ♣️ and ♦️ look like the same suit → Layer 3 emotional signatures need more specificity
If cards look generic / no THWAP → Layer 2 treatment needs adjustment
If warm/cool is inconsistent → Color temperature rule not being applied
If intimacy feels off → Composition rules need tightening

---

## Decision Points After Round 2

If ♣️ K doesn't feel like ♣️ suit → Scale rules need specificity
If A-K progression feels random → Figure count progression needs adjustment
If intimacy collapses at higher cards → Spatial rules need fixing

---

## After Both Rounds Pass

Full production: Generate all 52 cards using validated prompt templates.
Contractor brief: Write the visual spec for print vendor using Round 1-2 learnings.