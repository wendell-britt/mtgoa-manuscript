# Preview Card Spec — Poker Ratio Rules
## *The thing I keep getting wrong*

---

## The Mistake

I built `/ally-deck/preview` with square cards (`aspect-ratio: 1/1` or `padding-bottom: 100%`). Playing cards are NOT square. This is not a design preference — it is a physical fact.

---

## Poker Size Spec

```
Physical card: 3.5" × 2.5"
Aspect ratio:   3.5 / 2.5 = 1.4  (7:5 ratio)
In CSS:         aspect-ratio: 7 / 5
NOT:            aspect-ratio: 1 / 1  (square — WRONG)
NOT:            aspect-ratio: 3 / 2   (too wide — WRONG)
```

---

## Verification Checklist

Before saving ANY card layout to zo.space, I must run:

```python
# Check the aspect-ratio value in the code
grep -n "aspect-ratio\|padding-bottom" <file>

# Correct example:
aspect-ratio: 7 / 5;  ✅

# Wrong examples:
aspect-ratio: 1 / 1;   ❌ Square
aspect-ratio: 3 / 2;   ❌ Too wide
padding-bottom: 100%;  ❌ Square trick
padding-bottom: 66.67%; ❌ Close but not exact
```

---

## Frame Thickness

```
Border: 12px solid [suit-color]
Not:    2px                               (too thin)
Not:    border-radius only               (no border)
```

---

## What the Card Frame Must Look Like

```
┌──────────────────────┐ ← 12px suit-color border
│                      │
│   ♣ WAKE UP          │ ← suit icon + name, white text, suit color
│                      │
│  ┌────────────────┐  │
│  │                │  │
│  │   IMAGE        │  │ ← IMAGE = fills frame, no additional border
│  │                │  │
│  │                │  │
│  └────────────────┘  │
│                      │
│  "Recognition text"  │ ← smaller, lighter
│                      │
│  "The move"          │ ← larger, bold
│                      │
│  "Bridge"            │ ← smallest, lightest
│                      │
└──────────────────────┘
```

**Key:** The suit-color border IS the frame. The image fills the frame without its own border.

---

## Image Sources

Images live in `Images/` on workspace. When uploading to zo.space assets:

| Image | Workspace path | zo.space asset path |
|---|---|---|
| clubs-A-wake-up.jpg | `/home/workspace/Images/clubs-A-wake-up.jpg` | `/images/clubs-A-wake-up.jpg` |
| diamonds-A-clean-up.jpg | `/home/workspace/Images/diamonds-A-clean-up.jpg` | `/images/diamonds-A-clean-up.jpg` |
| hearts-A-grow-up.jpg | `/home/workspace/Images/hearts-A-grow-up.jpg` | `/images/hearts-A-grow-up.jpg` |
| spades-A-show-up.jpg | `/home/workspace/Images/spades-A-show-up.jpg` | `/images/spades-A-show-up.jpg` |

Always use the `update_space_asset` path. Do NOT use hotlinked URLs.

---

## How to Not Make This Mistake in the Future

1. **Every time I edit a card layout** — run the grep check above
2. **Before saving to zo.space** — verify `aspect-ratio: 7 / 5` is in the code
3. **When the user says "card"** — assume poker ratio unless they specify otherwise
4. **If I'm unsure** — say "I'm about to use [X] ratio — correct?" before building

This is not optional. The verification step is the rule.

---

## Spec Status

**Active** — applies to all card layout work on `/ally-deck`
