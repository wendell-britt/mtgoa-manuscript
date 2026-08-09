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

---

## Sitting 3 — ch2 through ch9, read in parallel

**Eight readers, one per chapter, read-only, reporting candidates rather than applying them.**
Every candidate was then verified against the text before it reached Wendell, and the
verification is the part of this sitting worth keeping: **two readers were wrong, one of them
caught an error of mine, and my own scope count was wrong twice.**

### What the parallel read is good for, and what it is not

It found **24 defects in one pass** against ch1's four, and the class of finding was the same:
cross-references that resolve and say the wrong thing, one artifact under two names, British
forms in families no instrument carried. **It also generated three conflicts that a single
reader would have resolved silently and wrongly.** The verification step is not optional
overhead; it is where the pass actually happened.

### The three conflicts, and how each resolved

**1 · ch3's reader proposed a fix that is house practice.** It flagged `ch3:134` — *the
villagers didn't stop feeling. It just stopped knowing what to do with feelings* — as a broken
singular pronoun, measuring **11:0** plural subjects inside ch3. ch5's and ch6's readers
independently killed it: the parable transition runs `It` in ch3, ch5 **and** ch6, and only ch4
says `They`. **3:1 house formula, rejected.** A within-chapter count found a real-looking
defect in a cross-chapter formula. **The lesson is the measurement's scope, not its arithmetic.**

**2 · ch5 proposed three fixes that ch6 said needed a ruling first.** Both had the count wrong.
Measuring all 24 `*You're winning when:*` blocks directly: **six** three-item lists with a
conjunction, **zero** taking the serial comma. Every `, and` in that register joins clauses.
So the register was uniformly unpunctuated, and ch5's three-of-six would have made it worse.
Ruled and swept whole.

**3 · ch9's reader caught an error in the L1 ruling I wrote and committed on 2026-08-09.**
Recorded in `STYLE_SHEET` §6 with the error kept. Short version: I generalised from one phrase
at 4:1 to a whole rule and wrote onto the sheet that *"ch9's capitals are all the six Faces"*
without checking ch9's sites. They were not.

**Then I under-counted the sweep twice**, because `grep -n` piped through `cut` shows one line
per match and hides every further occurrence on that line. `ch9:670` alone holds six. The scope
went 7 → 8 → 21 across two corrections. **Count occurrences, not lines** — now in §6.

### Applied

**24 fixes** — ch2 310/317/456 · ch3 152/509/860/999 · ch4 275 · ch6 217/535/607 ·
ch7 66/362/705/791/899 · ch8 105/160/545/634/764 · ch9 474/524/682.

**Three sweeps**: the six domain-block serial commas · 16 `Fixer-Healer` → `Fixer/Healer`
including ch5's section heading · 21 slot-sense `Face` → `face` across ch8 and ch9.

**The four highest-value finds, all invisible to every instrument:**

- **`ch7:705` and `ch8:634` both point at Section 3 for an axis drawn in Section 4.** Found
  independently by two readers. `xref.py` reads 0 broken because Section 3 exists — it proves a
  pointer resolves, never that it is the right one. Every chapter draws its axis in Section 4
  and ch4, ch5, ch6 and ch7:606 all say so.
- **`ch3:999` said the Polarity Map is *first drawn in Chapter 4*.** It is introduced at
  `ch3:630`, and ch4, ch5 and ch7 each open with *"You met the Polarity Map at the School of the
  Body"* — which is ch3. Five independent contradictions, one of them in the next sentence.
- **`ch9:474` calls its subject a Face inside a block headed *a daemon scan*.** The eight items
  under it are the eight daemons; not one is a Face.
- **`ch9:682` called the published deck *BARs*.** `ch1:318` defines a BAR as the reader's own
  card, built *"instead of someone else's checklist"* — so the two names collide on a
  distinction the book draws deliberately. Nine other sites say *cards*.

### The instrument gap, again

Six more British forms, every one found by a reader: *rigour* · *programme* · *instalments* ·
*signalled* · *relabelled* · *disorganised*, plus *per cent*. `copyedit.py` had `organise` and
`organised` and still missed `disorganised` — **the same prefix-shaped hole `towards` left for
`afterwards` in sitting 2.** All but the two-word *per cent* are now in `BRITISH`.

### Board after

`review.py` unchanged on every step; `copyedit` hyphen tier 16 → **15** with the slash sweep;
7e `0 broken · 0 unreferenced`; `shipcheck` **SHIPPABLE**.

### Still open

- **Ellipses** — both `...` sites are `ch4:84` and `ch4:717`; the four `…` are ch3 and ch6.
- **`first-year`** hyphenation.
- ~~**`ch2:33` does not parse.**~~ **CLOSED 2026-08-09.** Wendell supplied the noun: *"files
  that under **private life**, or therapy, or somebody else's field."* The three items are now
  all nouns and the verb reaches all three. It was logged rather than fixed because every
  candidate repair — *private life*, *private work*, *the personal* — changed the register
  differently, and picking one is an author's call rather than a copyeditor's. **The second
  defect in the same sentence is still open:** *those forty minutes* has no antecedent anywhere
  before it — nothing in ch1 or in ch2's first 32 lines describes a forty-minute episode. The
  demonstrative wants either a scene or de-specifying, and both are new material.
- **`ch7:251`** is the only cross-reference in the book naming its own section (1 of 18).
- **The `Move 4` / `Section 4` collision at `ch7:571`**, and ch7's EA table disagreeing with two
  of its five deep-dives.
- **`STYLE_SHEET` §7 is short five names** the agency board already scores — Nia, Priya, Marcus,
  Sam, Rosa — plus Ilse Marrow, Jess and the place-names Oreve and Sethen.
- Per-chapter structural notes from all eight reads, logged and not acted on under spec §6.

**The deep read is done, ch1 through ch9. What remains is the true proofread, on the built PDF.**

---

## Sitting 4 — the true proofread, on the built page

**The workbook trim is the proof**, ruled 2026-08-09. `build_pdf.py --trim=workbook`
produces `build/MTGOA_2026-08-09_workbook.pdf` — **404 pages, 7.5x9.25in, 12pt.** The trade
6x9 is 398 and paginates differently from ch4 onward, so a proofread against one does not
transfer to the other.

### The toolchain

`typst` and `pypandoc-binary`, both pip wheels, neither present on this container. Nothing
else is needed: the interior sets in fonts embedded in the Typst binary, which is why
`--check` fails on any font warning and why the build is reproducible off this machine.
`pymupdf` for reading the result back. **`pdfplumber` is unusable here** — its `cryptography`
dependency panics on this image.

### `instruments/proofread.py` — new

`build_pdf.py --check` already proves the structural things from the template's own record:
openers on a recto, folio continuous, blank versos genuinely blank. **Widows, orphans, runts
and hyphen ladders cannot be proved that way.** They are properties of where the text broke,
they need the rendered page, and there are 404 of those. **This exists so a person looks at
four pages instead of four hundred.**

### Two bugs in my own instrument, both of which faked a clean board

**1 · Margins are mirrored, and the first version averaged the two left edges into one.**
Body sets at x0 **72.0** on a recto and **97.2** on a verso. A single derived margin meant
every page of the other parity fell outside the x0 filter and was silently skipped — **the
instrument read half the book and reported `WIDOW 0 · ORPHAN 0`.** A clean board from an
instrument that has not looked at anything is worse than no instrument.

**2 · The indent detector took the nearest left edge instead of the most frequent one**, so
it locked onto the *list* indent at 79.2 rather than the paragraph indent at 85.8. Every
numbered step in the book then read as a paragraph opening, and the orphan board filled with
list items. Both fixes are commented in place.

### One false positive the eye caught and the machine could not

`p69` reported an orphan: *"It worked. The cost landed somewhere the villagers never thought
to look."* It is a **complete one-line paragraph** that happens to fill the measure, followed
by a marginalia block. Width alone cannot separate that from a paragraph running over the
break. **Rendering the page and looking at it is what settled it**, and the rule now requires
an orphan candidate to be the last content of any kind on its leaf.

### The finding, and the fix

**Three paragraphs closed on the back half of a hyphenated word** — `p190` *where.* · `p228`
*ation.* · `p233` *drawal.* Page 214 read *"...impact on the situ-"* / *"ation."*, with
`ation.` alone under a full page of argument.

**The repair is in the template, not the prose**, which is what the proofread stage is for.
`instruments/book/mtgoa.typ` set no line-breaking costs at all, so Typst's default let the
breaker take that trade. Raised to `costs: (runt: 400%, hyphenation: 150%)`.

**Result: all three gone, and one-word last lines fell 139 to 99.** Page count unchanged at
404, every opener still on a recto, folio still continuous — the repair was local.

### Board — the workbook proof is clean

```
WIDOW 0 · ORPHAN 0 · STACK 0 · FRAGMENT 0     404 pages
```

### The trade trim is not clean, and is not the proof

Same template, different measure, so the breaks fall elsewhere: **WIDOW 1** (`p312`, *4. The
Elder*) · **ORPHAN 1** (`p119`) · **FRAGMENT 3** (`p91` *Spiral.* · `p129` *nation.* · `p252`
*mindedness.*). Recorded so that a later decision to ship 6x9 knows the trade edition needs
its own pass rather than inheriting this one. **The costs change helped the workbook and did
not clear the trade**, which is the clearest possible demonstration that page-break defects
belong to a trim and not to a book.

### What this pass still does not check

**Rivers, loose lines and bad rags.** A machine reading extracted text cannot judge them
honestly, and a guess would put noise on a board whose whole value is that it is four lines
long. They want an eye on the proof PNGs, and that is the one remaining piece of the
proofread.
