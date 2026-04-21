# Ch5 S6 + S7 Cleanup Spec
**Created:** 2026-04-21
**Chapter:** Ch5 — Architect (Orange)
**Trigger:** S4+S5 rewrite complete; S6 and S7 have stale language that needs updating to match the new framework

---

## What Needs Fixing

### S6 (The Game) — Last Line Problem
**Current text:**
> "That's the Architect's game. Five moves. The map that makes you unnecessary. The leverage point instead of the brute-force push. The unstated assumption instead of the obvious one. The handoff instead of the dependency. The minimum instead of the masterpiece. The refactor instead of the defense."

**Problem:** "Five moves" here refers to the S6 game moves (Find the Leverage Point, Name the Unstated Assumption, Design for Handoff, Ship the Minimum, Refactor Kindly). This is correct — but the old chapter also used "five moves" to describe the transcend taxonomy in S4, which we just removed. The reader coming from S4 might think "five moves" still refers to Complexity→Elegance etc. The language has a ghost.

**Fix:** Retain "Five moves" since S6 genuinely has five moves. But add a clarifying bridge so it reads as referring to the S6 game moves, not the old S4 taxonomy. Options:
- Keep the line but add a transitional phrase: "...the refactor instead of the defense. These five moves are how the Architect plays to win."
- Or simply keep as-is — the S4 section no longer mentions "five moves," so the ghost may not actually haunt. Assess whether this actually confuses or if the context is clear enough.
**Recommendation:** ~~Keep the line.~~ **Revise: Add one clarifying word.** "That's the Architect's game. Five distinct moves. The map that makes you unnecessary..." — "distinct" signals these are the game moves, not the modes. Small but cheap to add. Eliminates potential confusion without adding meaningful length.

**Pattern captured from 6-face analysis:** After any major section rewrite, run a ghost-check on all remaining sections before declaring the chapter clean.

---

### S7 (Recap and Transition) — Two Problems

**Problem 1 — "the moves" is vague:**
> "You have the 5 modes, the stage sequence, the moves, and the 8 gates."

**Problem 2 — "Each mode is an emotional alchemy channel" phrasing could mislead:**
> "Each mode is an emotional alchemy channel at the Architect altitude — Mapmaker (Metal/Fear), Engineer (Earth/Neutrality), Strategist (Fire/Anger), Inventor (Wood/Joy), Optimizer (Water/Sadness)."

The phrasing "emotional alchemy channel" is close enough to "emotional alchemy channel" (Shaman's canonical system) that it could cause confusion. The modes are emergent types shaped by EA, not direct channels in the Shaman sense. The spec says "citeable against the canonical five" but the phrasing should signal this is the Architect's own form, derived from EA, not the same thing as Shaman's channels.

---

## What Stays

- "Structural generosity is the Architect's superpower" — ✅ keep
- "The Architect wins when the system works without them" — ✅ keep
- "5 modes, the stage sequence, the 8 gates" — ✅ keep structure, fix "the moves"
- "And here's why this matters for what comes next" — ✅ keep (transitions to Diplomat)
- "Now you're ready for the Diplomat" — ✅ keep

---

## S7 Fix — Proposed

**Replace the "moves" line with:**
> "You have the 5 modes, the stage sequence, and the 8 gates. Five ways logic moves at the Architect altitude — Mapmaker (Metal/Fear), Engineer (Earth/Neutrality), Strategist (Fire/Anger), Inventor (Wood/Joy), Optimizer (Water/Sadness) — each one a different way the design instinct learns to read reality. And you have the 8 gates walk, which is the WAVE-Spiral applied to your own inner design work."

**What changed:**
- Removed "the moves" (vague)
- Changed "Each mode is an emotional alchemy channel" to "Five ways logic moves at the Architect altitude" (avoids conflating with Shaman's canonical channels)
- The parenthetical listing of each mode with its canonical emotion is retained (readers need the EA hook)
- Added "each one a different way the design instinct learns to read reality" — brief, grounded, connects the modes to the practice

---

## Output Target

Two targeted edits:
1. S7 one-line fix (the "moves" → "and the 8 gates" rewrite)
2. S6 last line — assess whether "Five moves" actually needs clarification; recommended to keep as-is

No structural changes. No new content. Just language alignment.

---

## Verification

After edit:
- [ ] S7 no longer says "the moves" in the recap
- [ ] S7 mode listing still includes all 5 modes with their canonical emotions
- [ ] S6 "Five moves" still present (referring to S6 game moves)
- [ ] Chapter reads without internal contradiction

---

## Files to Update

- `ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md` — S7 one-line edit
- `ch5-ARCHITECT/CH5_REWRITE_SPEC.md` — add this as a new section: "S6+S7 Cleanup — Post-Rewrite Language Alignment"
