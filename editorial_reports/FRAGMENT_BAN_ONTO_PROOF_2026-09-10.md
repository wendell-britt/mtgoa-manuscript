# The fragment ban, reconciled onto the proof line

**Ratified 2026-09-10** as step 2 of the remediation ruling (cast seed 6117, Hexagram 40 →
60): *the proof line is the base; master's fragment pass (PRs #21 and #22) lands on it; where a
proof mark rewrote a sentence, the mark wins and fragment re-checks it.*

Branch `editorial/fragment-ban-onto-proof-2026-09-10`, cut from the proof line at `af8a931`
(DL-105), with `origin/master` (`911359d`) merged in.

---

## Result

| check | untouched proof line | this branch |
|---|---|---|
| `gate.py` (master's fragment counter merged in) | no fragment counter | **PASS — every counter 0** |
| `test_toolchain.py` | pass | **all cases pass** |
| round-trip (`compile.py --verify`) | ok | **ok** — insertions regenerated per DL-89 |
| claims | pass | **pass** — DL-99 phrase re-pointed |
| coherence | pass | pass |
| voice | 6 BLOCK · 129 WARN | 6 BLOCK · **128** WARN |
| slop shapes (reporting) | 44 | 46 — two from master's joins, carried to step 3 |
| trailing_and (proof line's counter) | 696 LOOSE | 703 — seven from master's joins, **carried to step 3** |

**Every sentence both lines added since they split is accounted for.** The proof line added 897
sentences and master added 297. Each one is in the result verbatim, or is on one of the lists
below.

## How the conflicts were resolved

Git reported 35 conflict hunks in 9 files. Those are paragraph-level: this book keeps a paragraph
on one line, so two edits to different sentences of one paragraph collide. Each hunk was re-run
through `git merge-file` (git's own diff3) **one sentence per line**, so an edit to one sentence
never overwrites an edit to another.

**32 sentences were rewritten by both lines. The proof line won all 32**, as ruled. Most were a
proof mark and a fragment fix on the same sentence, or a passage the proof line cut or rebuilt
outright: the phantom deck, the treatise signatures, DL-87's Forest rebuild.

## The fragment re-check: 31 repairs

The merged gate first read **48 fragments**, and none of them came from the merge itself. There
were two sources:

- **collisions where the proof won and the fragment master had fixed was still there**, and
- **proof-line prose the fragment counter had never read.** The proof line added Appendices H
  and I to the gate on 2026-09-09; master's counter arrived on 2026-09-01, on a line that didn't
  have them.

Each repair uses **master's own reviewed wording where master fixed that sentence**, with the
proof mark's words kept, and PR #21's colon lead-in elsewhere. Nothing was cut.

> *They chose efficiency over wisdom. Output over presence. Action over discernment.*
> → *They chose efficiency over wisdom, output over presence, action over discernment.*

> *Colder, too.* (a proof mark on master's *Colder.*) → master's verb, the mark's *too*:
> *They got colder, too.*

> **6. A word from the Head.** *The lines hold now.* → **6. A word from the Head:** *the lines
> hold now.* (DL-99's *hold* kept)

Also: *That is Fire / That is Water* (ch4), *It runs back and forth* (ch3), the capability
move's *in one sentence and the present tense*, *It is emotional pattern and somatic pattern*,
*The table comes next* and **One:** (ch9), and the five Appendix I superpowers
(**Alchemist** *(the Shaman, Chapter 3): spends a charge…*).

### ⚑ For your ratification: the boxed Head's records

This is where two of your rulings meet. **Master de-fragmented these lines on 2026-09-01. Your
proof marks on 2026-09-09 edited the same entries and kept their clipped notation** (*recorded →
wrote down*). The proof session had no fragment counter, so keeping them was never a ruling about
fragments. The ban is the explicit ruling, so it was applied, in master's wording:

- ch3, Maera's session records: *This is the thirty-first session. It arrives in the jaw first,
  then the back of the neck. I wrote down contempt…* · *Sessions thirty-two through four
  hundred and six read: chest, nothing; throat, nothing; hands, nothing.* · *This is the
  present session. The jaw goes at the word correctly.*
- ch5, Quill's charter: **Clause four:** · **Clause five:** · **Clause six:** · *Clause nine
  reads:* · *Second note:* (×2) · *Third note:*
- ch7: *This is case forty-one, with both transcripts, hers first.*

If the records should keep their notation, the reversal is one step: restore those lines and
exempt them in `gate.py` as in-world documents.

### ⚑ For your ratification: Devon's sample sheet (Appendix H)

It's a filled-in form. The file's own typesetting note sets it *"as a form… boxed fields."* A
field label and its value are the form, not prose, which is the same reason editorial-core
exempts the copyright page. **So it is exempted in `gate.py`'s EXEMPT list** with that reason,
not rewritten into sentences.

## Defects found on the way, fixed

- **Appendix H's production note would have printed.** `build_book.py`'s `META_KEY` strips header
  metadata but lacked `Format` and `Typesetting`. *"Set the sheet below as a form… Print artwork
  and the fillable version live at masteringallyship.com"* reached the reader-facing build. This
  is the defect the builder's own comment records for `Book body` on 2026-08-01, two keys short
  this time. Both keys added.
- **`gate.py` read raw files while the builder printed stripped ones**, so the gate scored a
  production note as prose. It now reads appendices and matter through `strip_provenance` and
  scores what prints.
- **`gate.py`'s fragment counter drifted inside blockquotes.** It advanced by one space per
  sentence; every bare `>` line adds another, so hits landed outside their EXEMPT spans (seven
  characters off by the sheet's last field). It now uses the separators' real positions.
- **`built` and `date`** join the counter's verb lists (*"Nobody built that as a reference
  table."*, *"Date every version."*).

## Found, not fixed: pre-existing on the proof line

Both fail identically on the untouched `af8a931`; this merge neither caused nor touched them.

- **`prose_diet`'s register for Quill's charter no longer measures anything.** Commit `3c160c1`
  (*Box the four Head's records*) wrapped the charter in a HANDBOOK block, and `prose_diet`
  strips frame blocks from the scored surface. The anchor matches zero times, and the ratchet
  ceilings you ruled on 2026-07-31 now apply to nothing. **Whether boxed records should be
  scored is yours to rule.**
- **`ch5_memoir_move.py`'s `SECTION4` anchor** points at *"## Section 4: The Practice"*, which
  the scaffolding strike removed from the reader's headings. It's a one-shot applicator whose
  job finished; its guard is what fails.

## Counter gap, recorded

Gate's fragment counter misses a fragment inside a boxed record when the sentence runs on from
the line before it. *"Clause nine."* and *"Case forty-one."* were found by reading, not by the
gate. Tested alone, the counter flags both.

## Carried to step 3

Diffed site by site against the untouched proof line, not remembered. Master's repairs added:

- **trailing_and, a net +7.** There are 11 new sentence keys, some of them existing sites whose
  sentence changed shape. Among them: *"It is not pleasant, but it is fun."* (PR #22's em-dash
  rewrite), *"That is occasionally true, and it is not a reason."*, and *"It could be a hard
  conversation, a call you delayed, or a conflict you replayed after it ended."* (the ch2 list
  master joined).
- **slop_shapes, +2 net, three new not-X-but-Y sites:** *"not pleasant, but"*, *"not relief yet,
  but"*, *"Not to consume the six Faces, but"*.

Step 3 replays the trailing_and pass onto this branch and takes all of them to zero with the rest.

## Not pushed

This branch is local. If the proof session pushes more to `claude/book-pdf-epub-production-ybxa11`,
merge that into this branch before step 3.
