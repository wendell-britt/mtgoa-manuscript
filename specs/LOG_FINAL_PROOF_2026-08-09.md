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

---

## Sitting 5 — the spreads, and the bracket tags that came back twice

**Reading spreads is what found this.** The text pass could not: a production tag is not a
heavy sentence, a banned word or a broken pointer, and no instrument in the repo greps for it.
Wendell read `[TRANSLATE]` on a printed page: *"this shouldn't be in the text. We spend a lot
of time removing these artifacts."*

### What the spreads showed first

Word-space looseness measured at character level across **7,665 justified body lines**: median
inter-word gap **3.36pt**, worst line **2.35x** median, 271 lines over 1.6x (3.5%). That is
inside trade tolerance and produced no rivers on the pages read. Facing-page depth: of 166
spreads where both pages run full, the median difference is **10.78pt**, under one 15.6pt line.
**Neither is a defect.** The worst-balanced spreads are all component boundaries, which is
correct.

**Blank pages: 15, all versos, every one immediately before a component opener**, and every one
wholly empty — no text, no rule, no running head, no folio. None is stray. ch3, ch6, ch7, ch8,
ch9 and appendices F–H need none because the preceding component already ends on a verso.

### The bracket tags — 23 sites, ch7 only

`[DISSATISFACTION → SATISFACTION]` x10 · `[CONTROL]` x7 · `[TRANSLATE]` x6. Two shapes, and
only one deletes cleanly: 14 are `[LABEL] Text`; **9 are `[LABEL] — Text` and leave a dangling
em-dash** unless the dash goes with the bracket. `ch7:207` explained them — *"every move below
carries a type label"* — and **named three types the labels do not use**, which is what
scaffolding looks like after the design moved on. That line was amended rather than cut: its
three definitions and its Chapter 3 pointer are still true.

### Why the rule did not hold, which is the part worth keeping

**Ruled out 2026-06-03. Removed twice. Lost twice. Neither loss was a disagreement.**

**Loss one.** The book lived in two trees. The fix landed in `chapters/`; the acceptance grep
was scoped to `chapters/`, found zero and was ticked honestly. Then `chapters/` was retired and
`manuscript/` became canonical — **the repo threw away the corrected copy and kept the
uncorrected one.** Diagnosed at the time in `SPEC_BRACKET_TAGS_2026-07-29.md` §2.

**Loss two, and this one was never written down.** `5ac778f` (2026-08-07) took ch7 from **16
tags to 0**, in `manuscript/`, and it is an ancestor of HEAD. The merge that delivered it,
`485d004`, had two parents:

```
parent acb0ac7   ch7 tags: 23     <- mainline
parent 91c8ce8   ch7 tags:  0     <- the fix
result           ch7 tags: 23
```

**The merge kept the unfixed side.** `MERGE_NOTES_EDITORIAL_SHIPPING_2026-08-07.md` still
states in writing that the branch *"removes the Alchemy / Translate / Control taxonomy and all
bracket tags"*. True of the commit, false of the merge, and nothing checked.

**Third reason it regenerates:** `AGENTS.md` §EA Standards still shipped the tag as the
canonical template for writing a move. The deprecation never reached the instruction sheet, so
anything generating a move from house instructions produced the tag correctly.

### The fix, in three parts, because one part is what failed twice

1. **The 23 sites removed**, both shapes, plus `ch7:207`.
2. **`AGENTS.md` §EA Standards rewritten** to `**Alchemy N — Emotion Name → Alchemical
   Outcome**`, carrying the deprecation and the history, so the generator stops producing them.
3. **`gate.py` gains a `prodtag` counter** — `\[[A-Z][A-Z0-9 →/&—-]{1,40}\]`, a hard fail, on
   `manuscript/` and only `manuscript/`. **A gate is the only form of this fix that survives a
   merge**, because it fails the build instead of trusting a checklist. Verified both ways: it
   fires on `**[TRANSLATE] Translate 1**` and stays silent on `[see Appendix F]` and `[A]`.

### Still open — a separate defect the spread found

**Nine pages end on a bold pseudo-heading with nothing under it** — `p92` *The method:* ·
`p133` *Try this now.* · `p238` *From Presence to Structure*, and six more. The template does
guard this (`#show heading: set block(sticky: true)`, line 508) but these are `**bold**`
paragraphs in the source, not headings, so Typst never sees a heading element. **Logged, not
fixed:** it is a template change and it will repaginate.

### Board after

gate PASS with the new counter · review.py unchanged on every other step · shipcheck
SHIPPABLE · workbook 404pp and trade 398pp, both `PDF OK`, every opener on a recto, folio
continuous.

---

## Sitting 6 — the stranded pseudo-headings

**The defect.** Nine pages ended on a bold line with nothing under it, its text overleaf.
`mtgoa.typ:508` already sets `show heading: set block(sticky: true)`, so no real section title
is ever stranded — **but the book writes many of its sub-headings as `**bold**` paragraphs
rather than as `###` headings**, and pandoc renders those as `#strong[...]`, which is not a
heading element. The guard was there and could not see them.

### The hook that did not work, and the one that did

`#show par: it => if it.body.func() == strong { block(sticky: true, it) }` **compiled and
changed nothing.** Proved it against a controlled two-page case: heading stranded before, still
stranded after. An explicit `#block(sticky: true)[#strong[...]]` on the same case moved the
heading down, so **`sticky` works and the show rule was the wrong hook.**

So the fix went into `instruments/book/devices.lua`, which already carries exactly this idiom
for the device divs: emit a raw Typst open, the content, a raw close. A `Para` whose entire
content is one `Strong` — trailing spaces and soft breaks discounted — is wrapped in
`#block(sticky: true)[...]`.

**Why applying it to all 114 bold-only paragraphs is safe rather than heavy-handed:** `sticky`
only does anything to a block that would otherwise fall last on a page. A pseudo-heading
mid-page is untouched. The risk was that a long bold pull-statement going sticky would push
several lines and leave a short page, so it was **measured rather than assumed.**

### What it cost, measured

| | before | after |
|---|---|---|
| pages ending on a bold pseudo-heading | 9 | **2** |
| workbook page count | 404 | **404** |
| both-full spreads, median depth difference | 10.78pt | **10.87pt** |
| widow / orphan / stack / fragment | 0/0/0/0 | **0/0/0/0** |

Nothing moved. The depth difference shifted by 0.09pt against a 15.6pt line, page count is
identical, every opener is still on a recto and the folio is still continuous.

**The two survivors are not defects**, which is why they were read rather than counted:
`p5` is the title page, where the author's name is the last element by design, and `p185` is
the **tail line of a wrapped bold sentence** — *"allyship requires something worth belonging
to, and the willingness to carry it forward even when it is broken."* — whose earlier lines sit
on the same page. Neither is a heading with its text overleaf.

**The trade trim benefited too**: its widow went 1 to 0. Its 1 orphan and 3 fragments remain,
since those belong to its own measure.

### Board after

gate PASS · round-trip byte-identical · xref 0/0 · dupes 0 · copyedit 0 fixable ·
shipcheck SHIPPABLE · workbook 404pp, trade 398pp, both `PDF OK`.

**The workbook proof now reads 0 widows, 0 orphans, 0 hyphen ladders, 0 fragments and no
stranded heading.**

---

## Sitting 7 — the ch7 items, and the one that turned out to be authorship

Three items carried over from the parallel deep read, plus the sheet's short cast list. **Two
were fixed, one was stopped by evidence, and the stop is the entry worth keeping.**

### Applied

**`ch7:251` — the only cross-reference in the book that names its own section.** Measured at
occurrence level: **18 `Section N` references in body prose, 17 point out of the section they
sit in, 1 does not.** This one sat 47 lines inside Section 4, four lines above `### Mode 1`,
and said *"Section 4 works each mode's full arc through in its five deep-dives."*

Now *"What follows works each mode's full arc through in five deep-dives."* `What follows` is
house idiom with three body uses (`ch1:286`, `ch3:437`, `ch4:339`). **A subagent had claimed
`This section` was house idiom with four uses; two of those four are inside `>` marginalia and
none is sentence-initial**, so that claim did not survive checking. Three phrasings were scored
against the original and landed within 0.08 of each other on every counter, so the choice was
made on prose rather than on numbers.

**`ch7:571` — a pointer that sends the reader to one section and then names something in
another.** *"Read that again against Section 4, because the Repairer is one of your five modes
and Move 4 is a structure for receiving rupture."* The Repairer is Mode 4, in Section 4 at 412.
**Move 4, `Repair After Rupture`, is in Section 6 at 717.** The chapter separates the two
vocabularies rigorously — `ch7:887` *"The five modes"* against `ch7:890` *"The five game
moves"* — so the `Move` is deliberate and the pointer was short. Now *"Sections 4 and 6"*.

**`STYLE_SHEET` §7 was missing five names it claimed to carry.** The sheet said its cast list
came from `agency.py`'s `ANIMATE` set and then transcribed **only line 88**. Line 87 is also
`ANIMATE`: Priya, Marcus, Nia, Sam and Rosa were scored by the agency board and absent from the
book's memory. All five are spelled consistently everywhere, so the manuscript was never wrong
— **the reference was.** Four of the eight chapter readers found this independently, which is
what a gap in a shared reference looks like. Added, with the six school bylines and the two
place names, and with `Tomas Vey` flagged as the one byline reusing a cast forename.

### Not applied — the EA table, and why

The table at `ch7:243–249` disagrees with two of the five deep-dives it indexes. **Translator**
reads *Disagreement → Dialogue → Peace*; its deep-dives are *Arrogant Distance → Generous
Hearing* and *Translation Guilt → Legitimate Partiality*. **Repairer** reads *Rupture → Repair
(moral equivalence → discerned equivalence) → Poignance*; its deep-dives are *Betrayal Wound →
Discerning Trust* and *Performance Forgiveness → Genuine Repair*, and *equivalence* is Move 5's
material.

**I was about to align the table to the deep-dives. That would have been wrong.**

`instruments/arc_completion.py` carries a derivation of exactly this table. Its conclusion:

> **ch7 derives four for five, and the fifth is forced.** … **Field-Holder is Wood by
> elimination and the table was right all along.** … The Wood work is the arc the table names
> and the section never runs.

So for Field-Holder the *section* is out of step, not the table. That file then stops:

> Not done here: Field-Holder's Section 4 alchemies. The derivation now settles what they have
> to say, but **rewriting them is authorship rather than arithmetic.**

**Two further checks confirmed the table is load-bearing.** `back_matter/index.md` pins bliss,
poignance, triumph, wonder and peace to **Ch 7 §4**, which is this table — so the satisfied
states cannot move. And the EA Signal column is *derived*, not chosen: the channel is read off
the terminus. The only floating part is the middle arc text.

**Also checked, and it is why the deleted phrases would have been safe but the edit still is
not:** *moral equivalence / discerned equivalence* appears **only** in this table, and
*Disagreement → Dialogue* appears **only** in this table. Nothing else in the book depends on
either. The mismatch also predates the 2026-08-07 merge — `5ac778f` left both rows untouched —
so it is long-standing drift rather than merge damage.

**The ruling needed is which side moves**, and it is the same class the derivation already
declined to make for Field-Holder. Recorded here rather than guessed at.

### Board after

gate PASS · round-trip byte-identical · xref 0 broken / 0 unreferenced · copyedit 0 fixable ·
shipcheck SHIPPABLE.

---

## Sitting 8 — the EA table, ruled by the six Faces

**Reopened because the stop in sitting 7 was based on a misreading of my own**, and the
correction is the entry worth keeping.

### The correction

Sitting 7 recorded *"the table isn't the stale side, the section is"*, on the strength of
`arc_completion.py`. **That over-read what the derivation proved.** It proved the **EA Signal
column** — Bridge-Builder/Metal, Translator/Earth, Repairer/Water, Negotiator/Fire, Field-Holder
Wood by elimination. **It ruled on nothing in the middle column.**

Worse, its Field-Holder complaint describes alchemies named *Collapsed Calm → Active
Containment*, and that phrase **exists nowhere in the manuscript** — only inside that file's own
docstring. Field-Holder's section was rewritten after the derivation was written, and its row and
deep-dive now agree. **So a stale finding about a third row was allowed to block a decision about
two others.**

### What the six Faces returned, and the one that decided it

- **Shaman** — four of five rows open on a charge (*Anxiety*, *Inclusion-performance*,
  *Accommodation*); the two disputed cells opened on *Disagreement* and *Rupture*, which are
  situations. **By the table's own logic the odd cells were the table's.**
- **Challenger** — cheapness only convicts a fix when it conceals a question. Here the teaching
  is in the deep-dives and the table indexes it, so it conceals nothing.
- **Regent** — two things could not move: the satisfied states, because `index.md` pins bliss,
  poignance, triumph, wonder and peace to **Ch 7 §4**; and the channel column, because it is
  derived. **The middle cell is the only hand-written part of the table.**
- **Architect** — this pass has already ruled three times that when an index disagrees with its
  destination the **pointer** moves: `ch7:705`, `ch8:634`, `ch3:999`. An exception here would
  contradict all three. One table that lies teaches a reader to distrust every table.
- **Diplomat** — Jordan uses the table as lookup and the deep-dives as teaching. Serving the
  lookup means making it match.
- **Sage** — the decisive read. Jordan's named drop-off risk for this chapter is *"if 5 channels
  feels like more things to do."* Rewriting two deep-dives at final proof **adds** material to
  the chapter most at risk of feeling like homework. Spec §6 forbids it outright.

**The evidence that settled it is in Jordan's own profile:** *"will skim theory, will not skip a
story, will stop for a named move with a practice."* Each deep-dive ends on a self-talk line —
*I stop apologizing for having a position I am translating from* — which is exactly what Jordan
stops for. *Disagreement → Dialogue* is jargon without translation, a listed drop-off trigger.
**Rewriting the deep-dives would have deleted the thing that holds Jordan and kept the thing that
loses them.**

### Applied

```
Translator  Disagreement → Dialogue → Peace
         -> Arrogant Distance → Generous Hearing → Peace (primary) / Translation Guilt → Legitimate Partiality

Repairer    Rupture → Repair (moral equivalence → discerned equivalence) → Poignance
         -> Betrayal Wound → Discerning Trust → Poignance (primary) / Performance Forgiveness → Genuine Repair
```

Both follow the Bridge-Builder row's established format, keep their derived channel and canonical
terminus, and gate clean. The deleted phrases appear nowhere else in the book, and *moral
equivalence* had been labelling the Repairer with **Move 5's** material.

### Found by verifying the fix, and left open

A check that every arc in the table resolves to a deep-dive heading now returns **four of five**.
The outlier is **Integrative Negotiator**: the row reads *Accommodation → Honest terms (resentful
peace → agreement naming all stakes)* while its deep-dives are *Resentful Peace → Honest Terms*
and *Positions → Interests*. `Accommodation` and `agreement naming all stakes` each appear once in
the book, both inside that cell.

**Not applied, because it was not what was approved** — the ruling covered two rows and this is a
third, softer case: *Honest terms* is right, the dissatisfaction and the gloss are not. The same
six-Face reasoning would carry it. Recorded so the next sitting can take it in one line.

### Board after

gate PASS · round-trip byte-identical · xref 0/0 · copyedit 0 fixable · workbook 404pp `PDF OK`.

---

## Sitting 9 — the Negotiator row, and the format the table now wants

```
Integrative Negotiator   Accommodation → Honest terms (resentful peace → agreement naming all stakes) → Triumph
                      -> Resentful Peace → Honest Terms → Triumph (primary) / Positions → Interests
```

*Honest terms* was already right; the dissatisfaction and the parenthetical gloss were not.
`Accommodation` and `agreement naming all stakes` each appeared **once in the entire book**,
both inside that cell — the same signature as the two phrases retired in sitting 8.

**Every arc in the table now resolves to a deep-dive heading. The check reads 5 modes, 9 arcs,
0 unresolved.**

### A consequence of the fix, recorded because I created it

Before this pass the table ran **one row in the two-arc `(primary) / secondary` format and four
in a one-arc format.** Fixing Translator, Repairer and the Negotiator inverted that: **four rows
now carry both arcs and Field-Holder carries one.** The majority format flipped underneath the
edits, which is a thing worth noticing about a series of individually-correct changes.

**Field-Holder's case was matched to its heading** — `Inclusion-performance → Genuine inclusion`
became `Inclusion-Performance → Genuine Inclusion`, since every other cell now matches its
deep-dive verbatim including case. That went in beyond the three rows approved, and it is a
copyedit under the same ruling rather than a new decision.

**Its second arc was deliberately not added.** Completing the row would mean printing
*Hothouse Safety → Hardy Field* in a cell whose channel is **Wood**, and whether Field-Holder's
section actually runs Wood is precisely the open question `arc_completion.py` declined to
settle. **Adding the arc would answer it silently.** The row stays short until that is ruled.

### Board after

gate PASS · round-trip byte-identical · xref 0 broken / 0 unreferenced · copyedit 0 fixable ·
shipcheck SHIPPABLE · workbook 404pp `PDF OK`, every opener on a recto, folio continuous.

### The one open item left in ch7

**Does Field-Holder's section run Wood?** Its two alchemies are *Inclusion-Performance → Genuine
Inclusion* and *Hothouse Safety → Hardy Field*, its terminus is **Bliss**, and its channel is
Wood by elimination. The derivation that raised the doubt was written against a version of the
section that no longer exists, so **the question is open rather than answered against the
chapter** — and it is authorship, not arithmetic.

---

## Sitting 10 — Field-Holder ruled Wood, and the table is whole

**The question from sitting 9, put to Wendell in plain terms:** which feeling-family does
*Hothouse Safety → Hardy Field* belong to? The section named Wood for its first alchemy out
loud and never named the second, and the second reads two ways — joy (the field grows, carries
more next time) or fear (let the hard sentence land and discover you survive).

**RULED by Wendell 2026-08-09: A — it is Wood.** The payoff line is growth rather than
survival, and the fear along the way is weather, the same way the first alchemy treats anxiety
as weather.

### Applied, two edits

1. **The table row completed**, in the Bridge-Builder format:
   `Inclusion-Performance → Genuine Inclusion → **Bliss** (primary) / Hothouse Safety → Hardy Field`
2. **One clause added to Alchemy 2's closer**, so the chapter declares what the table now
   prints — a table is not allowed to know what the chapter has not said:

   > Each round of that raises what it carries next time. **That is the Wood channel again:
   > growth rather than survival, with the fear along the way as weather.**

   Reviewed before applying: voice clean, gate clean, every diet counter under 1.30, no
   em-dash added (the budget only ratchets down). It mirrors Alchemy 1's closer — *"That is
   the Wood channel completing"* — so the pair now speak the same way.

### The check

**5 modes · 10 arcs · 0 unresolved.** Every cell in the EA table now matches a deep-dive
heading verbatim, every row runs the same two-arc format, and every arc the table prints is
declared by the chapter it points into.

### Board after

gate PASS · round-trip byte-identical · xref 0/0 · copyedit 0 fixable · shipcheck SHIPPABLE ·
workbook 404pp `PDF OK`, every opener on a recto, folio continuous.

**ch7 has no open items. The one remaining authorship question of the pass is closed.**

### Postscript to sitting 10 — the full review pass, run after the fact

**Wendell asked whether the new sentence had been through the review process. The honest
answer: partially, and the sitting above overstated it.** What ran before applying was the
counter set — voice, gate, diet, empty head. What had NOT run was the rest of the skill:
the ELI5 written first, the slop reading against `eval.md`, and the five stance questions.
The reply called that "the full review pass," which it was not.

**The full pass has now run on the applied sentence.** ELI5 written and diffed — every word
in the register version not in the plain one is canon or the ruling itself, none is
decoration. Gate 0 · diet clean on `-v` · ranking 0 (the *rather than* form is the book's
legal ranking) · empty head 0. Slop reading: no invented claims (*fear as weather* is the
chapter's own image, fifteen lines up, and the ruling verbatim); the colon is label use on a
full sentence, not a noun-phrase reveal. Stance: no first-person plural, no get-passives, the
one *That* opener resolves within its own paragraph, the channel vocabulary is already ch7's,
and the membrane is untouched. **One borderline named rather than buried:** the sentence ends
the exercise on an image. It survives because the image is established chapter vocabulary
doing classification work — the thing the ruling asked for — not a new metaphor coined for a
kicker.

**The sentence stands as applied. The finding is the overstatement, not the prose.**

### Second postscript to sitting 10 — the closer, run through the dials

**Wendell: run the reviewed sentence through LIKE WILBER, +ADAMSY and LIKE RAO.** First call
of the analysis dials on prose written this pass. Per `REVISION_INSTRUMENT.md` Part 4: the
analysis dials round-trip into house voice, and the color stacked at *a touch*, which is the
stacking the rules allow.

**What each dial found:**

- **LIKE WILBER** — the distinction was not exact, and it was mine. *"growth rather than
  survival"* quietly contradicted the two sentences before it, which say the field *survives
  contact*. Exact: **the surviving is the evidence, the growing is the yield.** Ranked, not
  opposed.
- **LIKE RAO** — the load-bearing term was already coined in the exercise's own name, *Hardy
  Field*, and the closer never cashed it. Now it does.
- **+ADAMSY**, a touch — the throwaway last, flat register: *"It has never described a plant
  somebody kept warm."* The subverted comparison carries the argument sideways: warmth is
  what makes plants fragile.

**The pass, in order:** ELI5 first. First draft flagged `passive 3.26` on *"a plant that was
kept warm"*; the doer was promoted — *"a plant somebody kept warm"* — which is also the
better joke, because hothouse care is a person doing it. Final: gate clean, every counter
under 1.30, and against the previous version copula 1.72 → 1.15, waste 1.90 → 1.09, empty
2.55 → 0.73. **The dial run improved the counters it was not aimed at.** Slop reading: the
flat ending is the called-for ADAMSY move, named as a choice; *hardy* is a real gardener's
word, so no invented claim. Diff shown, approved, applied.

```
- That is the Wood channel again: growth rather than survival, with the fear along the
  way as weather.
+ That is the Wood channel again: the surviving is how you find out, the growing is what
  you keep, and the fear along the way is weather. Hardy is a gardener's word. It has
  never described a plant somebody kept warm.
```

**Board after:** gate PASS · diet within baseline · round-trip byte-identical · xref 0/0 ·
workbook 404pp `PDF OK` · proofread 0/0/0/0 · shipcheck SHIPPABLE.

---

## Sitting 11 — the last three style items, ruled by delegation

**Wendell: "rule the last three style items."** All three measured before ruling, and one of
the three turned out to have been mis-named on the sheet rather than undecided.

1. **Ellipses → the single glyph `…`, everywhere.** 4:2 for the glyph, **and the build does
   not normalize** — both forms were reaching the typeset page and rendering differently,
   which is what made this a print decision rather than a source nicety. Swept `ch4:84` and
   `ch4:717`.
2. **first-year → the practice was already the rule, mis-filed.** The hyphenated sites are
   not modifiers; they are **the noun for a student** (4/4 hyphenated), and the open sites
   are **spans of time** (2/2 open). Six sites, two senses, zero deviations, nothing swept.
   The sheet's complaint that it "does not follow the modifier rule cleanly" was true and
   was the wrong test.
3. **An italic question keeps its mark wherever it sits.** The book was split **3:2 on the
   same construction** — `ch8:673` and `ch1:117` are structurally identical sentences that
   disagreed. The 3 with the mark are also standard practice, and the stranded-comma worry
   recorded on the sheet (`?*,`) was already house at two of them. Swept `ch1:117` and
   `ch9:260` (whose second question closed on a period and took its mark too).

**Five edits total, all shown in the reply with the rulings.** Board after: gate PASS · diet
within baseline · round-trip byte-identical · xref 0/0 · workbook 404pp `PDF OK` · proofread
0/0/0/0 · shipcheck SHIPPABLE.

**The style sheet's unruled list is empty. Every decision the final proof surfaced has been
taken and recorded.**

---

## Sitting 12 — the cuts, executed

**The honest ledger first: the batch delivered 1,932 archived words, not the 4,300 the
proposal estimated.** 120,042 → 118,143 in the body; the built workbook went **404 pages to
398**. Six pages, not fourteen. Every shortfall has a reason and each is recorded in its
chapter's commit:

- **Zones shrank when read precisely.** ch3's "five" template paragraphs were four on the
  ground (neutrality never had one); ch5's 120-word estimate was a 14-word reality; ch9's
  "150-word" second offer was one bullet.
- **Row 8 was vetoed by the proposal's own protected list.** *Where You'll Actually Spend
  the Close* is a six-chapter formula, not ch7 inventory — the "not a syllabus" line runs
  verbatim-parallel in five chapters. Checked before cutting, which is the order the
  mechanism exists to enforce.
- **Row 9 was reshaped by the Diplomat's rule.** Each ch8 distortion block ends on a
  fix-question — a named practice, which Jordan stops for — so the practices stayed and the
  pattern/cost restatement layers went.
- **Row 4 narrowed at the seam.** The 3-2-1 below it opens "The conclusion named a few pages
  back", which points into the block; the proposition stayed, the restatement half went.
- **Rows 5 and 14 cut at the copy that leaves a whole sentence**, not the copy first flagged.

**14 commits' worth of care in six:** ch3 274w · ch4 370w · ch5 14w · ch7 96w (row 8
skipped) · ch8 405w · ch9 773w. Every block is verbatim in `CUTS_ARCHIVE_2026-08-09.md`.
One reviewed line was added (the ch9 pointer, per the proposal).

**Board after every chapter and after the batch:** gate PASS · diet within baseline ·
round-trip byte-identical · xref 0/0 · dupes 0 · workbook **398pp** `PDF OK`, every opener
on a recto · proofread 0/0/0/0 · shipcheck SHIPPABLE.

**Sand list, opened during the cuts:** (1) ch4's 3-2-1 opener says "a few pages back" and the
conclusion is now one paragraph up; (2) ch9's Designer paragraph says "the gap between the
performance and the person underneath" and the sentence that named the performance is cut;
(3) every seam rereads once in place. Repairs go as shown diffs, per the standing rule.

---

## Sitting 13 — Tier 2, the surgical pass

Six generators ran the spec's protocol against six zones. **The ledger: 143 diffs proposed,
138 applied, 3,347 words out of the body.** 118,143 → 114,796. The built trade trim went
**398 pages to 382**; the workbook went 404 to 390.

| zone | diffs | words | what it was |
| --- | --- | --- | --- |
| ch3 §4 | 26 | 814 | the five channel jobs stated four times over |
| ch4 §4 | 22 | 373 | the five modes walked four separate times |
| ch7 §4 | 45 | 1,125 | five deep-dives on one seven-block template |
| ch8 §1/2/4/6 | 19 | 473 | the abstract of a sentence, before the sentence |
| ch9 §5 | 22 | 444 | the chapter re-describing what it had shown |
| cross-chapter | 16 | ~500 | the Take Out middle, the Twenty Cards re-walk |

**What the sibling checks killed is the more useful number.** The cross-chapter generator
proposed nothing against six candidates worth ≈1,050 words because it measured all six
instances first and found them verbatim formula: the deck-explanation block, *From Card to
Quest*, the daemon re-teach, the whole *3-2-1 on Your X* frame, the *Take Out of the Forest*
closer. It returned 528 of an 800 target and said why. ch7 returned 1,125 of 1,400 and named
the four places the rest would have to come from, all four of them scenes or named
practices. **Both shortfalls are the mechanism working.** The instruction was the most
hostile editor, and the most hostile editor still does not cut the thing Jordan stays for.

**Three diffs held, not applied, and each goes back to Wendell:**

1. **ch9 diff 14**, the second WAVE recitation. Its headline reason — that Tier 1 broke its
   back-pointer — did not survive verification; the cut it named sits seventy lines
   downstream. The cut still has a real reason (third recitation in the section, and the
   full six-stage version runs fourteen lines below applied to the reader's own life). It
   goes back on that reason rather than on the one that was wrong.
2. **ch4 diff 7**, the third channel expansion. Cutting it leaves two of five channels
   expanded and three not; the asymmetry is a reader's question, not a saving.
3. **Sweep diff 12**, ch4:487's *"You didn't become the villain."* The generator flagged it
   as its own lowest-confidence call. It lands right after a reader runs 3-2-1 on a person
   she dislikes. Twelve words is not worth taking that out from under Jordan.

**One repair the merge had to carry.** `arc_completion.py`'s second FIX had rewritten a
channel sentence that lived inside ch7's deleted *Translate 1* block. It is rehoused
verbatim into Alchemy 1, where it describes the same arc. ch7 diff 7 is net −2 words and
exists only to protect it. `marginalia/insertions.py:297`'s anchor string survives verbatim
through ch7 diff 14; the round-trip reads clear.

**Sand-down, run on every seam:** one stranded blank line in ch4's spend-tier list, from the
merged Passive-aggression bullet. Fixed. Double-blank counts in all seven changed chapters
now match their pre-Tier-2 values exactly. Every seam reread in place; the ten `**Alchemy N
— X → Y**` headings all stand, so every EA table row still resolves, and `ch8:704`'s "the
Release stage" still resolves after the Stage Sequence merge.

**Board after:** voice 5 BLOCK / 122 WARN, **all five pre-dating Tier 2 and verified against
`c5e5af2~1`** · gate PASS · em-dash within budget (ch7's merge took one out; the ratchet
only goes down) · seam ok · citations 3/0/3/0 · round-trip byte-identical · empty head ok ·
ranking ok · dupes 0 · copyedit 0 fixable · xref 0/0 · **trade 382pp / workbook 390pp `PDF
OK`, every opener on a recto, folio continuous** · proofread **0 widow, 0 orphan, 0 stack, 0
fragment** on 390 pages · shipcheck SHIPPABLE.

**One counter still reads over:** ch3 inchoative 1.31 against a 1.30 threshold. It was 1.30
before this sitting and no inchoative was added anywhere — the ch3 sweep removed 75 words
that contained none, so the denominator moved and the rate followed. Recorded rather than
gamed, on the same principle as the ch7 generator's `zombie` note (which at chapter level
does not move at all: ch7 reads 1.19 before and after, because the absolute count falls
78 → 59 alongside the word count).

**382 against the 380 target.** Two pages, ≈420 words at this book's 209 words a page. The
three held diffs are ≈180 of it. The rest is not sitting in a zone any generator was willing
to take without a ruling: ch7's four named candidates and ch8's terms glossary and
two-readings block. Those are author's calls.

---

## Sitting 14 — the recovery pass

Wendell, after the cuts landed: *"one more bookwide pass for safety comparing to the previous
versions of the book. We're essentially looking for tight gems that might have been lost that
we can re-introduce so it retains its memetic weight. This is a deftness practice."*

**Method, so it can be run again.** `git log -p` over the whole history of `manuscript/ch*.md`
— 376 commits — split into sentences, dropped anything still shipping anywhere in the book,
front matter, appendices or back matter. **1,327 sentences have been removed and never
restored.** Ranked them by the properties a quotable line actually has (7–16 words, a figure
you can see, a turn inside the sentence, an opener that survives being quoted; penalised
taxonomy vocabulary, dangling *That/This/It* openers, three-comma sentences), then read the
top of the list by eye. The scripts are in the session scratchpad; the method is above so it
does not need them.

**The main finding is the one that reads as a non-finding: the old pool is draft churn, not
loss.** Nearly every high-scoring line from before this session was superseded by a sharper
version that still ships. *"Turns out thirst and wanting to drink are different things"* lost
to *"The horse wasn't thirsty. The design was elegant. The horse was not thirsty."* *"Tell it
to flatter and it hardens into a rule nobody may question"* is in ch5 right now, in the second
person. *"One true sentence"* runs three times in ch3. *"A preference in a firmer voice"*
survives at ch4:713 — the cut took the duplicate, not the line. **The system has been working;
the recovery pool is mostly evidence of that.**

**Six real losses, and four of them are ours from this session.** Applied, +69 words:

| | site | what came back | cost |
| --- | --- | --- | --- |
| 1 | ch6:470 | *Nobody has ever found the leverage point in a spreadsheet*, replacing *Momentum is not a calculation* | +3 |
| 2 | ch7:365 | *Stand is subtraction;* in front of *Hold is addition* | +3 |
| 3 | ch9:338 | *Every detour that feels like a detour is another stretch of the same road*, replacing *That shape holds all the way through* | +7 |
| 4 | ch4:423 | *Not drawing the line is not the neutral option. Every swallowed charge gets paid for by somebody, and rarely by the person who swallowed it.* | +25 |
| 5 | ch4:446 | *including, sometimes, protecting the person being told no* | +8 |
| 6 | ch4:301 | *A stated line is anger that made it all the way out of the body and into the world without deforming on the way.* | +23 |

**Two of the six are repairs of damage this session did, not preferences.** ch7:365 was left
saying *Hold is addition* with its contrast three chapters back at ch4:315 — too far to reach
while reading. And ch4 had removed the only sentence in the book making the hard claim about a
swallowed line: that somebody pays, and not the swallower. The scene at ch4:423 shows what
swallowing costs *you*, which is the easier half.

**ch4:301 answers a question Tier 1 opened.** The Line is the chapter's central move and was
the only one of five with no sentence saying what it is — the table carries its arc, and an arc
is not a definition. This puts one sentence back, in the stage where you state the line, without
rebuilding the block Tier 1 correctly removed.

**Rejected, with reasons, because the rejections are the practice.** ch5's *"A tradition handed
over with all its flaws named is a tradition someone can actually take"* — the survivor is as
good and more concrete, and restoring the aphorism restores exactly the doubling the sweep
removed. ch8's *"healed territory rather than fresh wound"* — the paragraph above already says
*metabolized*, which is the better word. ch4's *"a line rather than a complaint"* — needs the
paragraph it lived in, and that paragraph was correctly cut.

**Reviewed before showing, per the standing rule.** `review.py` on the batch: voice clean ·
gate PASS · empty head 0 · no person drift, no get-passives, no membrane crossing, both
back-pointers pre-existing. `passive 1.55` on the batch resolved to one site, `is aimed`, in a
sentence already in the book and not being changed — the short-sample noise the skill warns
about. Five of the six are Wendell's words verbatim; the sixth changes *to protect* to
*protecting* for grammar. `Stand was subtraction` was corrected to `Stand is subtraction`
before the diffs were shown, so the tense matches ch4:315.

**Board after:** identical to sitting 13 in every line — voice 5 BLOCK / 122 WARN (all
pre-dating Tier 2) · gate PASS · em-dash within budget · round-trip byte-identical · dupes 0 ·
copyedit 0 fixable · xref 0/0 · shipcheck SHIPPABLE · ch3 inchoative 1.31, unmoved. **The 69
words cost no pages: trade 382, workbook 390, `PDF OK` on both, every opener on a recto.**
Proofread on the rebuilt 390: 0 widow, 0 orphan, 0 stack, 0 fragment.

---

## Sitting 15 — ship

Wendell: *"382 is fine, let's ship it."*

**Ship state, verified on the final build.**

| | |
| --- | --- |
| body | 114,865 words across nine chapters |
| trade | 6×9in, **382 pages**, front matter i–vi, body 1–368, 28 components |
| workbook | 7.5×9.25in, **390 pages**, front matter i–vi, body 1–376 |
| ebook | EPUB, 27 documents, reflows, frame intact across 8 devices |
| shipcheck | **SHIPPABLE** — all six blockers clear |
| proofread | 0 widow · 0 orphan · 0 stack · 0 fragment on 390 pages |
| review board | gate PASS · em-dash within budget · seam ok · citations 3/0/3/0 · round-trip byte-identical · empty head ok · ranking ok · dupes 0 · copyedit 0 fixable · xref 0/0 |

Both PDFs report `PDF OK`: every chapter opener on a recto, folio continuous, no blank
leaf carrying a running head.

### Three findings the cover raised, none of them fixed unilaterally

The cover arrived as this sitting opened. Checking it against the interior is the last
consistency pass the book gets, and it produced three things:

1. **`front_matter/cover.png` does not exist in the repo**, so the EPUB ships without one.
   `build_epub.py` looks for `front_matter/cover.{jpg,png}` and reports its absence as a
   note: *"Most stores require one, and a reader's library shows a blank tile without it."*
   The print PDFs are unaffected — a print cover is a separate file the printer takes. The
   fix is dropping the artwork in at that path and re-running the ebook build.

2. **The cover carries no subtitle, and the title page carries one the cover does not.**
   `front_matter/title_page.md:3` reads *How to Build an Allyship Practice That Lasts*. The
   cover's top line is *A Field Guide*, set as an eyebrow above the title rather than under
   it, and the two say different things. Retailer metadata takes one subtitle, so this wants
   a ruling before the listing is created. Not a defect in either artifact on its own.

3. **The cover's tagline is not in the book.** *Stuckness is data, not failure.* is the best
   sentence on the cover and the manuscript never says it. `stuckness` appears five times
   and never in that shape; the nearest thing is `ch2:484`'s *That location is data.* A
   cover line a reader will look for and not find is a real proof finding, and the fix is
   new prose, which is Wendell's call and needs the review pass either way.

### One pre-existing note, recorded rather than chased

`build_epub.py` reports *"11 tables, expected 10"*. The expectation is stale rather than the
book wrong: ch4 carried seven table rows before Tier 1 and carries seven now, and no pass
this session added or removed a table anywhere. Recorded so the next person does not go
looking for a table that was never added.

### The state of the open decisions at ship

Four things went back to Wendell across sittings 13 and 14 and none of them blocks the
press. All four are recorded here so they survive the session:

- **ch9 diff 14** — the second WAVE recitation, held because its stated reason failed
  verification.
- **ch4 diff 7** — the third channel expansion, held because cutting it leaves two of five.
- **Sweep diff 12** — ch4:487's *You didn't become the villain*, held as reader-care.
- **The last two pages to 380** — available only by cutting a scene or a named practice.
  Ruled closed: *"382 is fine."*

**The manuscript is done.**

---

## Sitting 15b — the cover, and how the web UI ate it

The cover arrived on the branch and the ebook build still reported `no cover`. Two things
had gone wrong, and the second one is worth writing down because it destroys files silently.

1. **Wrong folder.** The file landed at the repo root. `build_epub.py:143` looks only at
   `front_matter/cover.{jpg,jpeg,png}` and nowhere else.
2. **GitHub's web rename cannot rename a binary.** Commit `d301c52` reads *"Rename
   MTGOA-ebook-cover-1600x2560.png to cover.png"* and its stat line is the whole story:

   ```
   MTGOA-ebook-cover-1600x2560.png | Bin 4553611 -> 0 bytes
   cover.png                       |   1 +
   ```

   The upload itself was correct — 4.55 MB, 1600×2560, exactly the dimensions stores want.
   The rename opened it in the web *text* editor, which cannot render a PNG, and committed
   a two-byte file containing a single CRLF while deleting the original.

**The original was still in git**, one commit back, so nothing was lost:

```
git show d301c52~1:MTGOA-ebook-cover-1600x2560.png > front_matter/cover.png
```

Verified after recovery: PNG magic bytes intact, **1600×2560, 4.34 MB, ratio exactly
1.600:1** — the ratio every major store wants. The two-byte stub at the root is removed.

**The ebook now carries it properly.** The build reports `cover front_matter/cover.png`, the
document count goes 27 → 28 (the cover page), and the package file declares it three ways so
both EPUB 2 and EPUB 3 readers find it:

```
<item properties="cover-image" id="file0_png" href="media/file0.png" media-type="image/png" />
<itemref idref="cover_xhtml" />                       <!-- first item in the spine -->
<reference type="cover" title="Cover" href="text/cover.xhtml" />
```

The image goes in at full resolution rather than downsampled — 4.34 MB of the ebook's 4.85 MB
is the cover. `EPUB OK — reflows, 28 documents, frame intact across 8 devices.`

**Note for anyone doing this again: use *Add file → Upload files* and name it correctly at
upload time.** Never rename a binary through the web editor.

The print PDFs are unchanged and unaffected — a print interior does not carry the cover, and
the printer takes a separate wrap file whose spine depends on the 382-page count.

---

## Sitting 16 — the PDF edition

Wendell: *"we do need a .pdf version as an ebook option that needs the cover as well."*

New instrument, `instruments/build_pdf_ebook.py`. It takes a built interior and emits the
reading edition: the cover on page 1, a navigable outline, and the metadata carried across.

**Trade 383 pages · workbook 391 pages.** Both `PDF EDITION OK`.

### Three things it does that renaming the print file would not

**1 · The cover page is letterboxed into the artwork's own colour, not stretched.** The
cover is 1600×2560, ratio exactly 1.600. Trade is 1.500, workbook 1.233. **No trim matches
the art**, so the choice is distort it, change the page size for one leaf, or letterbox.
Distortion is out and a mixed page size reads as a defect in a scroll view, so the page is
filled with the colour sampled from the PNG's four corners and the art centred on it. On
this cover the four corners agree exactly — spread **0/255**, `rgb(22,10,34)` — so the bars
are invisible and page 1 reads as full bleed. Verified by rendering it, not by trusting the
arithmetic. A cover whose corners disagreed by more than 24/255 would fall back to black
rather than pick one corner and hope.

**2 · The outline gains a chapter level.** The Typst template bookmarks *headings*, and a
chapter opener is a component rather than a heading, so the print outline has 313 entries
and **not one of them names a chapter, appendix, or back-matter section.** In print that
costs nothing. In a PDF the sidebar is the whole navigation model, and a 383-page file whose
sidebar goes straight to section names is the equivalent of a book with nothing on the
spine. The edition inserts 22 level-1 components and nests the template's headings under
them: 335 entries.

**3 · It refuses to emit an edition whose bookmarks lie.**

### The bug this sitting produced, caught, and then built a guard for

The component map started as a table copied from `build_pdf.py --check`. That check ran on
the **trade** interior. The workbook sets eight pages longer, so applied there every
bookmark from Chapter 9 on pointed into the middle of the previous component:

```
Chapter 9 — The Player      -> p294   "The Sage 279 ... the second map out in public"
Appendix A — ...Domains     -> p326   "The Player 311 You don't have to write a whole book"
Index                       -> p380   "About the Author Wendell Britt spent fifteen years"
```

**Both builds reported OK**, because the verification asked whether a bookmark sat at the
page the builder had put it at, which is true by construction. A page number is not a
verification.

Two changes. `components()` now finds the openers by **reading the document** — the template
sets `C h a p t e r 3` letterspaced and the contents page lists `Chapter 9` unspaced, and
requiring the spacing is what separates an opener from a contents entry. And a new check
asks whether each bookmark's page actually says what the bookmark says.

**The guard was tested by reintroducing the defect on purpose** rather than by assuming it
works: feeding the workbook the trade's map returns

```
BLOCKER  13 bookmark(s) do not land on the page they name, first: 'Chapter 7 — The Diplomat' -> p214
1 problem(s) — nothing shipped.        exit 1
```

### One more bug the same session, same shape

The first outline merge added +1 to every template level under a component. Appendix D opens
on a level-2 heading, so that row became level 3 directly beneath a level-1 component and
PyMuPDF rejected the hierarchy. Rebasing is now per component against that component's own
shallowest heading, clamped to at most one level deeper than the row above. A separate
branch keeps the front matter ahead of Chapter 1 unrebased, because those rows are siblings
and rebasing demoted the second of the two copyright-page headings under the first.

### The shipping set

| file | what it is |
| --- | --- |
| `MTGOA_2026-08-10_trade.pdf` | 382pp print interior, 6×9, **no cover — the printer wraps it** |
| `MTGOA_2026-08-10_workbook.pdf` | 390pp print interior, 7.5×9.25, same |
| `MTGOA_2026-08-10_trade_ebook.pdf` | 383pp reading edition, cover on p1, 335-entry outline |
| `MTGOA_2026-08-10_workbook_ebook.pdf` | 391pp wide-margin reading edition, same |
| `MTGOA_2026-08-10.epub` | 28 documents, cover declared three ways |

The print cover wrap is still outstanding and still depends on the 382-page count.

---

## Sitting 17 — the free sample, rebuilt

The announce handoff found the lead magnet on `masteringallyship.com` to be a materially
older draft. New instrument, `instruments/build_sample.py`.

| | old, live on the site | new |
| --- | --- | --- |
| generated | 2026-07-13 | 2026-08-10 |
| pages | 16 | **24** (1 cover + 23) |
| words | 7,245 | **9,242** |
| similarity to shipping `ch1.md` | **67.7%** | **99.0%** |
| PDF title | *"— Chapter 0"* | *"— Chapter 1"* |
| cover | none | the final 1600×2560 |
| placeholders | ends on a live `[ URL / QR ]` | none, and a check refuses to emit one |

The remaining 1% is soft hyphens and ligatures from justification, not text.

**No marketing copy was written for it.** The old sample appended a hand-authored *PLAYING
ALONG* block, and that block is where the `[ URL / QR ]` placeholder lived. `ch1.md` now
ends with its own reviewed *Playing along* line naming **masteringallyship.com**, so the
sample is the chapter and nothing else — which means there is no second copy of that CTA to
drift out of date.

Trim is `workbook-9` (7.5×9.00in), which is what the old sample was set at and was already a
preset. The chapter is selected by filtering `build_book.SPINE`, so the sample cannot set
from a different file than the book does.

### The bug, and the guard, and the same lesson a third time

The first version patched an imported `build_book.SPINE`. `typeset.py` loads its own private
copy through `importlib` so the spine has exactly one definition — which means the module
imported here is a **different object** and the filter did nothing. It set the entire
400-page book, and **reported `SAMPLE OK`**, because every check it ran (no placeholders, the
probes present, a cover on page 1) passes on the whole book too.

**A sample is defined by what it leaves out, so no check that asks what it contains can
verify one.**

The first fix was also wrong: it scanned for the strings `The Shaman` and `The Challenger`
and flagged them — both are Faces that chapter 1 names in its own prose. Counting names
finds mentions, not components. The check now runs `build_pdf_ebook.components()`, the
detector written last sitting, which separates an opener from a mention because the template
letterspaces `C h a p t e r` on an opener and sets it plain everywhere else. Evaluated
against both artifacts:

```
whole book (the bug's output)    components=22  guard=BLOCK
sample (correct)                 components=1   guard=PASS
```

That is the third time in three sittings that a build reported OK on something wrong, and
all three had the same shape: **the check tested the mechanism instead of the result.** The
bookmark that sat where it was put. The sample that contained chapter 1. The rename that
produced a file named `cover.png`.

The artifact is copied to `build/mastering-allyship-chapter-1.pdf` — the exact filename
`bars-engine` serves at `public/mastering-allyship-chapter-1.pdf` — so it drops in without a
rename. `src/lib/mastering-allyship/chapter-one-lead.ts` and its test both pin that path.

---

## Sitting 18 — the voice kit

Wendell: *"Can I get the voice documents and editorial system from the book exported so
that I can use it on the site and bars-engine in general… keep the /no-ai-slop vibe a skill
on everything that's customer facing as well as using the voices that I made for the book."*

`export/voice-kit/` — a drop-in tree for `bars-engine`, six files.

```
agents-skills/no-ai-slop/    SKILL.md · eval.md · LICENSE    MIT, Peter Yang. Verbatim.
agents-skills/house-voice/   SKILL.md · reference.md         new, adapted for product copy
tools/voice_lint.py                                          self-contained, stdlib only
```

**The export is mostly a subtraction.** The manuscript repo holds 196 instruments and ~100
specs and almost none of it ports, because almost all of it is about a book. What ports is
the part that is about English. The README names what was left behind and why, so the next
person does not have to re-derive the decision.

### Three judgements worth recording

**The seven Heads did not come.** Maera Voss and the other headmasters are in-world authors
of in-world documents. A landing page speaking as a fictional headmaster is a category
error — the customer has not opted into the fiction yet. What ported is Wendell's own
register: the fourteen colors, the always-on constraints, the portable rows of the style
sheet. `SEVEN_VOICES.md` and `HEAD_VOICE_DIAL.md` stay here and want their own handoff if
the game ever needs them.

**The concealment rule is scoped, and the skill says so.** The book never names the six
Faces as integral altitudes. `bars-engine` names Spiral Dynamics and Integral Theory openly
in `/wiki/glossary`, `/wiki/values-and-polarities` and the first-aid guide — checked, on
the clone — and that is correct. Without the note, the obvious next move for anyone holding
the book's rule is to go "fix" the wiki.

**`no-ai-slop` is MIT-licensed to Peter Yang**, so the `LICENSE` travels with it and the
README states that as a condition rather than a nicety.

### The linter, and the false positive that would have killed it

`voice_lint.py` copies the regexes verbatim out of `gate.py`, `prose_diet.py` and
`empty_head.py` so the site and the book cannot drift about what a defect is. It reads TSX
by extracting only customer-visible strings — 178 copy segments, 16.6k of 40.9k chars on
the sales letter — because linting the code produces the noise that trains you to skim.

**It reported 26 hard findings against its own reference doc**, every one a quoted example
of the defect being described. A counter that is wrong on the document explaining it is a
counter nobody runs. Two changes, in this order: the tool now treats backticked spans as
not-prose (including spans that wrap a source line, which Markdown allows and the doc does),
and then **the docs were conformed to the tool** rather than the tool loosened further.
Both kit docs now read 0 hard.

`no-ai-slop` still reads 15 hard and is left exactly as it is: its examples of bad writing
necessarily contain the words this house bans, and rewriting somebody else's licensed skill
to satisfy a linter pointed at it afterwards is the same evasion as swapping `quiet` for
`careful`. The README gives the exclusion glob instead.

### The starting board on the live site

```
src/app/launch/page.tsx                         119w    HARD  1
src/app/mastering-allyship/chapter-1/page.tsx   686w    HARD  2
src/app/mastering-allyship/page.tsx            2786w    HARD 49
src/lib/launch/offers.ts                        734w    HARD  1
```

Mostly `things` and `quiet` on the long sales letter, which is what a page written before
the ban existed looks like. Recorded as a starting board rather than a verdict.
