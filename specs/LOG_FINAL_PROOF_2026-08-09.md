# Log — the final proof

**The running record of the pass specified in `SPEC_FINAL_PROOF_2026-08-07.md`**, opened
2026-08-09 on branch `claude/mtgoa-final-proof-1sizjz` (which carries the merged final-proof
commits from `claude/book-pdf-epub-production-ybxa11`).

Governed by `specs/HANDOFF_FINAL_PROOF_2026-08-07.md` and `specs/STYLE_SHEET.md`. One entry
per sitting. **What is written here is what happened, including what was rejected and why** —
a log that records only the accepted edits loses the reason the rejected ones were wrong.

---

## Board at open

`review.py` twelve steps: one LOOK — step 0 voice, 4 BLOCK / 129 WARN, the standing
adjudicated surface — and step 7e xref reporting **0 broken · 2 unreferenced**.
`shipcheck.py` **SHIPPABLE**, all six blockers clear.

---

## Sitting 1 — Appendix B and D get on-ramps

**The item.** `xref.py` step 7e reported both appendices shipping with nothing in the
manuscript pointing at them. Ruled 2026-08-07 (`STYLE_SHEET.md` §Ruled item 4): they get
pointers. **The one item in this pass that adds prose rather than regularising it.**

### Where each one went, and why there

**Appendix D → `ch3`, closing the Somatic Markers section.** The chapter whose work it
continues is the Shaman's: D exists for the moment the WAVE-Spiral will not start. That
section already ends on precisely that failure — *"you might be thinking the WAVE-Spiral
instead of practicing it. Come back to the body"* — and D is the three ways back. It also
joins ch3's existing appendix cluster (C at 457, E at 624, F at 653), which is where a reader
has already been taught to look for the toolkit.

**Appendix B → `ch9`, closing "The five moves are the map. The practice is the walking."**
B opens *"You crossed the forest. You met the Faces. You know the moves. This is the game
board"* — a post-walk address — and its eight quests are keyed to chapters 2 through 9. The
section it now closes argues that a list of moves is not a practice. **B is the answer to that
argument rather than a coda to it**, which is why it went there instead of after "Try It Now —
Sixty Seconds", the other candidate.

### The lines

```
ch3  *Three practices for a charge that won't move on request, one to raise it, one to
      settle it, one to read what it wants: Appendix D: Emotional Alchemy Practices.*

ch9  *Eight quests, one for each chapter of the walk, and four campaigns you can run with
      other people: Appendix B: Quests & Campaigns.*
```

Both use the house cross-reference form — italic line, description, colon, `Appendix X:` and
the appendix's H1 verbatim — matching the seven existing pointers at `ch3:457`, `ch3:624`,
`ch3:653`, `ch4:217`, `ch5:284`, `ch6:225`, `ch7:200`.

### What the review pass returned

ELI5 written first; both lines say what the plain version says and nothing more. `gate` clean ·
`voice` clean · `empty_head` 0/0/0 · slop detect names no pattern. Stance pass (all five):
address stays second person, no first-person plural, no get-passives, no borrowed move
performed unnamed, neither line opens with a back-pointer, and both are apparatus rather than
either voice — the same class as the C/E/F pointers, so the membrane is untouched.

**One counter reads heavy and was allowed to stand.** `waste 1.37` on the ch3 line, from the
three instances of *it* in *one to raise it, one to settle it, one to read what it wants*. All
three point at *a charge* inside the same sentence, the sample is 55 words, and the skill's own
ruling is that `waste` has a floor as well as a ceiling. A line that never says *it* has stopped
pointing at things.

### Two things deliberately not done

- **The ladder is not named** anywhere near either line. The six Faces are the integral
  altitudes and the concealment is deliberate; the reveal lives in `ON_THE_SHOULDERS_OF`.
- **D's pointer stays an invitation, never a prescription.** That appendix carries a standing
  note that it is the book's one deliberate somatic exception and has to read as a page the
  reader chooses to open. The line describes what is there and instructs nobody to breathe or
  to feel.

### The third change, which is not prose

`instruments/build_book.py:153` keeps `NAMED_REFERENCES` — the map of appendices the body cites
by title rather than by letter — so a title-based pointer cannot rot into a dead end before
print. It held C, E and F. These two pointers make B and D title-citing, so both were added.

### Board after

`review.py` step 7e: **0 broken · 0 unreferenced — clean.** All other steps unchanged.
`shipcheck.py` SHIPPABLE. `build_book.py` spine complete, 137,783 lines, 47 marginalia blocks
applied, the two standing OPTIONAL gaps (dedication, backers) unchanged.

**Item 1 of the handoff's "what is left" is closed.**
