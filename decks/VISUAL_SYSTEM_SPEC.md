# Visual System Spec — Allyship Deck
## *Geometry, Space, Color, and Typography Rules*

---

## What This Document Is

The visual system is the art direction that makes 52 cards look like one product. Not "here are some inspiration images" — here are the rules that produce consistent decisions.

The test of this document: give it to a contractor, have them design one card without reference images, compare to V3 cards. If it looks like it belongs, the spec worked. If it looks slightly off, the spec needs more rules.

---

## Card Anatomy

### Poker Size

- **Dimensions:** 3.5" × 2.5" (88.9mm × 63.5mm)
- **Bleed:** 0.125" (3.175mm) on all sides
- **Safe area:** 3.25" × 2.25" (82.55mm × 57.15mm) — content must stay inside
- **Corner radius:** 0.125" (3.175mm)

These are non-negotiable print specs. Any vendor needs these exact numbers.

---

### The Three Zones (Spatial Rules)

The card has three content zones. Each has a defined position and proportion.

```
┌─────────────────────────────────────────┐
│  SUIT SYMBOL (top, ~15% of card height) │
│─────────────────────────────────────────│
│                                         │
│  RECOGNITION PROMPT (top third)         │
│  Bold. Smaller type. Uppercase OK.      │
│                                         │
│─────────────────────────────────────────│
│                                         │
│  THE MOVE (center, most visual weight)  │
│  Large. Bold. Verb-first.                │
│  This is the largest text on the card.  │
│                                         │
│─────────────────────────────────────────│
│                                         │
│  ALLYSHIP BRIDGE (bottom third)         │
│  Smaller, lighter. One sentence.         │
│                                         │
└─────────────────────────────────────────┘
```

**Zone proportions by card area:**
- Recognition prompt: 20% of card surface
- The move: 40% of card surface
- Allyship bridge: 20% of card surface
- Suit symbol + card back indicator: 10%
- Breathing room: 10%

**Spatial rule:** The move has visual dominance. If the move and the recognition prompt are the same size, the card is wrong. The move is the headline. Everything else serves it.

---

### Card Back

The card back is the product's first impression. When face-down on the table, it should communicate:

1. This is a deck with a point of view
2. Something warm and specific, not generic
3. The suit structure is implied but not stated

**Card back elements:**
- Large suit symbol (dominant, centered or offset per suit identity)
- Deck name: "How to Be an Ally to Wendell" in small text
- No card number on back (numbers only on face)

**Card back spec test:** A card face-down on the table should feel like it belongs to this deck and no other. If it could be any tarot deck, the card back needs more specificity.

---

## Suit Symbols

Each suit has a distinct geometric identity. Readable at poker size. Memorizable from a glance.

### ♣️ Wake Up — Triangle-Up (Ground)

**Geometry:** Equilateral triangle pointing upward.

**Why:** The triangle pointing up is the oldest symbol for rising — waking, rising, ascending. It reads as "ground and direction." The ally wakes up to what's underneath.

**Color:** Dark green. Hex: #1B4332.

**Size:** Occupies ~15% of card height. Positioned top-center or top-left.

### ♦️ Clean Up — Diamond (Cut)

**Geometry:** 45-degree rotated square (diamond orientation).

**Why:** The diamond is the cut — the moment of reflection where light changes direction. Cleaning up is the cut through the pattern. Also reads as "precious but sharp."

**Color:** Dark red. Hex: #9D0208.

**Size:** Same as ♣️. Consistent geometry across suits.

### ♥️ Grow Up — Heart

**Geometry:** Classic heart shape. Not stylized. Not corporate. A real heart — slight asymmetry, not perfectly symmetrical.

**Why:** The heart is the only suit symbol that requires no explanation. It's also the one that carries the most kitsch risk. The design solution: real and slightly imperfect, not clip-art.

**Color:** Dark rose. Hex: #9D0208 (shared with ♦️).

**Note:** ♥️ and ♦️ share the same color. This is intentional. Both suits are about interior work. The shape distinguishes them, not the color.

### ♠️ Show Up — Triangle-Down (Action)

**Geometry:** Equilateral triangle pointing downward.

**Why:** The downward triangle is the oldest symbol for descent — action, grounding, arriving. The ally shows up by going toward, not rising. Direction distinguishes ♠️ from ♣️.

**Color:** Dark navy. Hex: #1B2A4A.

---

## Color System

### Per-Suit Colors

| Suit | Name | Hex | Usage |
|------|------|-----|-------|
| ♣️ | Forest green | #1B4332 | Suit symbol, accents |
| ♦️ | Deep red | #9D0208 | Suit symbol, accents |
| ♥️ | Rose | #9D0208 | Suit symbol, accents |
| ♠️ | Navy | #1B2A4A | Suit symbol, accents |

**Note:** ♦️ and ♥️ share a color. The shape does the区分 work.

### Background

- **Card face:** Warm off-white. Hex: #F8F5F0.
- **Card back:** Slightly darker warm tone. Hex: #EDE8E0.
- **Not pure white.** Pure white is clinical. The warm tone reads as handmade, specific, human.

### Typography Colors

- **Recognition prompt:** Near-black. Hex: #1A1A1A.
- **The move:** Pure black. Hex: #000000. (Visual weight = bold)
- **Allyship bridge:** Dark gray. Hex: #4A4A4A. (Lighter than move = hierarchy)
- **Suit symbol:** Matches suit color (see above).

---

## Typography

### Typefaces

**Primary (The move):** Something with a strong vertical axis. Readable at large size. Not a display font — this is not a poster.

**Recommendation:** Freight Text, GT Walsheim, or Untitled Sans. Something with enough character to feel human without being quirky.

**Avoid:** Montserrat, Open Sans, Roboto, or any font that's been used by a SaaS company as their brand font in the last five years.

**Recognition prompt:** Same family as the move, but lighter weight and smaller size.

**Allyship bridge:** Same family, smaller, italic or light weight. It should feel like an annotation, not a command.

**Suit symbol:** Geometric (custom or drawn) — not a font character.

### Type Sizes (Relative)

| Element | Size rule |
|---------|-----------|
| The move | Largest. 18-24pt equivalent at 3.5" width |
| Recognition prompt | 10-12pt equivalent. Bold weight |
| Allyship bridge | 9-10pt equivalent. Light or italic |
| Suit label (face) | 8pt. Uppercase |

**Type rule:** The move is always larger than the recognition prompt. If they're the same size, redesign.

---

## Card Face Layout

### Face Card Indicators (J / Q / K)

- Face cards have a visual badge or overlay that marks them as face cards
- J = small indicator (no special text)
- Q = same indicator, no special text
- K = crown motif or "KING" in small text (the sovereign question)

**Rule:** Face cards don't have different content structure. Same three zones. The J/Q/K designation is visual, not structural.

### Card Number

- Small, unobtrusive. Top-left or top-right corner.
- Does not compete with the move for visual attention.

---

## Box and Packaging

The box is the product's second impression (after the card back).

**Box design:**
- Same warm off-white as card face
- Deck name in clean sans-serif
- Small heart icon or deck motif
- No stock imagery
- No blurbs or testimonials on the box

**What the box communicates:** This was made by a specific person with specific taste. Not a product line. Not a publisher. A person.

**Box interior:** Cards held in a tray. Optional: a small card with the shuffle ritual ("Draw when the moment arrives").

---

## Tactile Spec

**Paper:** 300gsm cardstock (or equivalent). Not glossy — matte or soft-touch laminate.

**Finish:** Soft-touch laminate on card faces. This adds warmth and durability. It's the tactile equivalent of "fire and peace."

**Card back:** Same stock, same finish. Consistent throughout.

**Corner radius:** 0.125" on cards. Box corners may be sharper (0.25").

---

## The Print Vendor Problem

Poker size cards require precise specifications. A vague brief = a wrong result.

**Minimum vendor brief must include:**
- Exact dimensions: 3.5" × 2.5"
- Bleed: 0.125" all sides
- Safe area: 0.125" inside trim
- Color space: CMYK or RGB (vendor preference)
- Paper: 300gsm
- Finish: soft-touch laminate (both sides)
- Quantity tiers requested
- Proof required before full run

**Vendor shortlist candidates:**
- ArtCardPrint
- MakePlayingCards
- PrintRunner
- PsPrint

---

## The AI Generation Problem

AI image generators will produce generic allyship imagery if given generic prompts. The deck's visual identity must be strong enough to reject bad AI outputs.

**AI visual rules:**
- No stock photo aesthetic
- No flat illustration style
- Warm, slightly imperfect photography or geometric abstraction
- If using AI for production imagery: heavy stylization required to avoid generic look

**The art direction brief (Section 5) is the answer to this problem.** It defines what the deck should NOT look like, which gives AI tools a veto.

---

## Spec Status

Visual System Spec complete.

**Next:** QR Page Spec (audio, go deeper, practice scenario per card).
