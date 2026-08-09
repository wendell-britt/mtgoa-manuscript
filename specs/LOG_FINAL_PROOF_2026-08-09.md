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

---

## Sitting 2 — ch1, the deep read

**Mechanicals cleared first**, so the read was a read: `copyedit` 0 findings on ch1 ·
`ranking` 0 · `empty_head` 0 · every diet counter under 1.00 (be 0.82, copula 0.91, waste
0.96, zombie 0.49, expletive 0.37, passive 0.81, empty 0.66, inchoative 0.36).
**Everything below came from reading the chapter end to end.**

### Applied

| | site | finding |
|---|---|---|
| 1 | `ch1:282` | **missing serial comma** in *your face, your shadow and your myths*. The 2026-08-07 sweep fixed 7 sites and missed this one. Re-scanned ch1 for the pattern: 32 candidates, 31 false positives on pairs — **the same ~68% rate the sheet recorded** — and this was the one real three-item list |
| 2 | `ch1:204` | `Afterwards` → `Afterward` |
| 3 | `ch1:54` | **a three-item list broken across a sentence boundary.** As printed, *"Not the friends who vote the wrong way, the parents and their casually racist comments."* was a fragment whose negation never reached items two and three, and the colon then glued the third item to a clause it was not the subject of |
| 4 | `ch1:87` | **the myths diagnostic was named two ways, 190 lines apart** — *"a short, unflattering diagnostic at masteringallyship.com"* at 87 and *"The Myths Read"* at 276, a name appearing nowhere else in the book. Named at first mention so 276 resolves |
| 5 | `ch9:514` | `home Face` → `home face`, the L1 ruling |
| 6 | `ch1:181`, `ch2:13`, `ch7:737`, `ch8:730` | the `-wards` sweep, L2 |

**On fix 3, the obvious repair was rejected.** Writing *"not the friends…, not the parents…,
not the coworker…"* restores the list and manufactures exactly the stacked fragment negation
`ranking.py` was built for. Deleting the single `Not` and letting the colon do list-label work
costs one word and creates nothing. **Ran `ranking.py` against the line before and after: 0
both ways**, because its HARD tier needs the doubled *"Not A, not B:"* form — which is
precisely why this site survived every pass.

**`ch1:181` was applied without being shown first**, and that is worth recording as a
deviation. It surfaced while sweeping L2, is the same already-ruled policy, and measures 1
against 0 in a family the book renders American 101 times out of 101. Flagged to Wendell in
the same reply with an offer to revert.

### Logged, not fixed

- **`ch1:254` and `ch1:274` run the same two shadow examples with different verbs** — *draws
  a clean line straight through* / *scorches*, *until nothing can be decided* / *until nothing
  gets decided*. Larger than a sentence, so spec §6 says log. Reads as accidental rather than
  as a callback, and the fix is to make the second an explicit callback or vary the example.
- **`ch1:34`** — *"and that fewer than half of them get that"*. *That* points back across an
  intervening clause. The claim is sourced and rewording a cited sentence wants a ruling.
- **`ch1:214`** opens *"Each of the three"* two lines after `ch1:212` says *"Two different
  games were running that night"*. Back-pointer across a section boundary with a competing
  number in between; resolves at the subheads, so it may be fine as is.
- **`ch1:117`** — question-mark parity inside a paired italic question. Now item 10 on the
  sheet.

### Two candidates that died on measurement

**Both would have been wrong, and only counting told me so.**

- **`ch1:198`, the heading *"Which Game Are You Playing"* with no question mark.** The book
  carries roughly ninety interrogative headings and **not one takes a mark.** House practice,
  not a defect.
- **The double blank line at `ch1:190`.** Other chapters carry 7 to 12 each, and markdown
  collapses it. Invisible in the deliverable.

### The instrument that should have caught fix 2

`copyedit.py` carried `towards` from the day it was built and did not carry `afterwards`.
**Same family, same ruling, one word present and one absent**, and four body sites survived
every pass because of it. Both `afterwards` and `backwards` are now in its `BRITISH` map,
added only after measuring the whole family so the board gains no noise. The board went
`0 fixable` → `1 fixable` → `0 fixable` across the addition and the sweep, which is the
instrument proving it works.

### Board after

`review.py` unchanged on every step, 7e still `0 broken · 0 unreferenced`. `copyedit`
**0 fixable · 16 to read**. `shipcheck` SHIPPABLE.

**ch2 is next.**
