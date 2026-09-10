---
type: table
title: "Mark-pattern table — what the ch2–ch3 proof marks predict about the rest of the book"
aliases:
  - mark pattern table
  - P1-P7
  - the table
tags:
  - editorial
  - mtgoa
  - proof
created: 2026-09-09
review: 2026-09-16
source:
  - specs/SPEC_MARK_PATTERN_TABLE_2026-09-09.md
  - specs/PANEL_MARK_PATTERN_TABLE_OPEN_Q_6FACE_2026-09-09.md
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
  - instruments/markpatterns.py
status: seven rows filled. Two RULED, two CLEAR, two OPEN, two UNSEARCHABLE — nothing swept.
---

# The mark-pattern table

**Wendell has read 22% of this book on paper.** ch2 pp.25–52 and ch3 pp.53–95: 24,741 words of
113,656. The other **88,915 words have never been marked.**

On 2026-09-09, 49 spans changed across six rulings. **27 of them — 55% — landed in chapters nobody
has marked**, and every one was found by taking a ch3 mark and asking where else the shape occurs.
This table is that question asked deliberately instead of by accident.

**The table records. It does not authorise.** A filled row is a measurement. It becomes work when
Wendell rules it, and a row may sit indefinitely without that being a debt.

**Every count here comes from `python3 instruments/markpatterns.py`.** None is written from memory.
That rule exists because on the day this was built I made four wrong scope claims — five sites when
there were ten, nineteen licensed when there were eighteen, eleven lines when there were ten, thirty
PRO sites when there were twenty-four.

**Ruled scope: everything that ships.** The panel ruled ch1–ch9 only, on the argument that the
appendices are apparatus rather than reading voice. **Wendell overruled it, 2026-09-10: *"The
checklists should cover the appendices."*** Six Faces agreed with each other and were wrong about
whose book it is. The appendix list now comes from `profile.corpus` rather than a raw glob, which
also removed an editorial review that lives in `appendices/` and is not in the book.

---

## The board

| row | shape | ch1–9 | apparatus | **unmarked** | verdict |
|---|---|---:|---:|---:|---|
| **P1** | interprets the observation — the *", and [what it means]"* tack-on | — | — | — | **UNSEARCHABLE** |
| **P2** | concludes for the reader — the verdict stamp | — | — | — | **UNSEARCHABLE** |
| **P3** | manages the reader's path — the signposts | 23 | 9 | **15** | **OPEN** |
| **P4** | undercuts itself — the hedges | 2 | 0 | **1** | **CLEAR** · DL-88 |
| **P5** | gestures with a nothing-word — the vague verb | 20 | 7 | **14** | **SWEPT** · DL-98/99 |
| **P6** | repeats a line as a refrain until it stops carrying weight | 1 | 0 | **0** | **CLEAR** |
| **P7** | construction scaffolding left in the reader's text | 0 | 0 | **0** | **RULED** · DL-84 |

*apparatus = shipping appendices, front matter, back matter — **ruled since 2026-09-10**.*
*unmarked = sites in chapters nobody has read on paper, i.e. everything but ch2 and ch3.*

---

## P1 · interprets the observation

**shape** — the writing steps in front of the concrete material to say what it meant. The
*"…, and [what it means]"* tack-on.
**marks** — *"and it should not"* · *"and they walk away having lost their own say in it"* ·
*"and the trade feels like safety."*
**search** — none of usable precision.
**scope** — attempted as a trailing-clause regex. Any pattern broad enough to catch these returns
several hundred sites, most of them ordinary compound sentences. `trailing_and.py` (review step 3d)
counts the construction; it cannot tell a tack-on from a clause that carries its own weight.
**verdict — UNSEARCHABLE.** *Recording that is the row's finding. A fabricated count is worse than
an empty cell.* This row is closed to searching and open to a reader.

## P2 · concludes for the reader

**shape** — the verdict stamp. A sentence that tells the reader what to think about the sentence
before it.
**marks** — *"The care underneath is real"* · *"All four are real allyship"* · *"Both are true"* ·
*"It is a form. You sign it"* · *"That is burnout."*
**search** — none of usable precision.
**scope** — the marked instances share no lexical shape. *"Both are true"* and *"That is burnout"*
are four-word declaratives indistinguishable by regex from every legitimate four-word declarative
in the book.
**verdict — UNSEARCHABLE.** Same finding as P1, and for the same reason: **this is a judgement
about what a clause is doing, not about what it contains.**

## P3 · manages the reader's path

**shape** — the signposts. The writer steering the reader through the book instead of writing it.
**marks** — *"Hold these three words, because the whole book turns on them"* · *"This chapter is
the threshold map"* · *"The deeper truth is this:"* · *"Chapter 3 gives you both"* · *"and Chapter
9 tells that part"* · *"Appendix G says where."*
**search** — 10 phrase families. `markpatterns.py P3`.
**count** — **23 in ch1–ch9 · 9 apparatus · 15 unmarked.**
**scope** — a phrase list built from the six marked instances plus four near neighbours. Cannot see
a signpost phrased in words not on the list, and does not distinguish a pointer that earns its place
from one that manages.
**verdict — OPEN.** The unmarked sites include *"Appendix G says where to read her"* `ch6:238`,
*"that combination is what this chapter trains"* `ch8:615`, and **the same sentence twice in two
chapters** — *"Every move in this chapter is an instrument for making that sentence true"* at
`ch7:884` and `ch8:857`. **The 9 apparatus sites are now ruled too**, on Wendell's overrule of
2026-09-10. A pointer in an appendix may still be what an appendix is for; that is a reading, not
an exemption, and it is made site by site rather than by category.

## P4 · undercuts itself

**shape** — the hedges. The writer taking back what was just said, in the writer's own voice.
**marks** — *"I have guessed wrong in both directions"* · *"and I could be wrong"* · *"It is not
one"* · *"I have not solved it. I teach here anyway."*
**search** — 20 first-person hedge phrases, case-insensitive. `markpatterns.py P4`.
**count** — **2 in ch1–ch9 · 0 apparatus · 1 unmarked.**
**scope** — phrase list from the four marked instances plus sixteen near neighbours. Cannot see a
hedge phrased in words not on the list.
**verdict — CLEAR.** Both remaining sites are legitimate. `ch3:44` is inside the admissions form,
where *"I have been wrong about who was past it"* is a Head admitting something on a filed
document — the form's whole purpose. `ch4:686` quotes a hedge as the thing not to do: *"Most people
bury their lines in qualifiers."*
**ruling — DL-88**, 2026-09-09. The one real instance was ch3's Oreve note, and Wendell ruled it:
*"the real defect is the closing hedge 'I have thought about it more than is useful' commenting on
the anecdote instead of ending it."* **P4 is the first of the seven patterns he ruled on directly.**

## P5 · gestures with a nothing-word

**shape** — the vague verb. A nothing-word doing the work a real verb should.
**marks** — *"how you are landing"* · *"lands hard"* · *"the feeling runs clean"* · *"it trades
contact for control"* · *"vigilance buys aim"* · *"metabolize."* Wendell, 2026-09-02: *"'lands warm'
— what the fuck does landing warm mean? Land is another one of those nothing words."*
**search** — the six marked phrase shapes and their inflections. `markpatterns.py P5`.
**count** — **20 in ch1–ch9 · 7 apparatus · 14 unmarked**, after DL-98 and DL-99. Before the sweep: 59 · 13 · 49.
**scope** — matches the phrase shapes, not the judgement. Known false positives in the count:
*"the land was not returned"* `ch5:253`, *"trade them for a prize"* `ch1:123`. A reader clears each
site; the number is a ceiling, not a finding.
**verdict — OPEN. The row's finding about the instrument is closed: DL-97, 2026-09-10.**

> **`light_verb.py` was built from this pattern and covered one phrase of five.** Probed before
> and after the fix:
>
> | marked phrase | before | after |
> |---|---|---|
> | lands / landing | flagged | flagged |
> | runs clean | **INVISIBLE** | flagged |
> | trades X for Y | **INVISIBLE** | flagged |
> | buys X | **INVISIBLE** | flagged |
> | metabolize | **INVISIBLE** | flagged |
>
> **Four separate causes and only one was a missing word.** `ABSTRACT` held generic English —
> *praise*, *shame*, *fear* — and none of the book's own abstractions. `DEADV` covered motion and
> placement but no transaction verb, so *buys* and *trades* had nothing to match. `metabolize` is
> a *wrong* verb rather than a weak one and needed a third tier. And **`sites()` skipped every
> sentence of three words or fewer** — *"Vigilance buys aim."* is three words, and so is *"That is
> burnout."*, which is a P2 mark. That filter was hiding the book's flattest register for one hit
> in 449 sentences.
>
> **The probe now runs on every `markpatterns.py` invocation and prints a REGRESSION line if the
> count drops below 5 of 5.** The hole cannot close over silently again.

The panel refused to widen the instrument inside the table build *(Q3)* and Wendell ruled it the
next morning: *"fix the light_verb hole."* **Then he swept the row**: *"sweep the 59 P5 sites"*,
and on being shown that the row is 59 sites while the word `land` is 103, *"all of it."*

**DL-98 took the 29 sites carrying a manner word. DL-99 took the reception sense across the rest
of the book, 41 more. `land` went 103 → 26, and the 26 are locative** — a cost landing on the
people a design is for, a feeling landing in the body, the skeeball ball, and the book quoting
the hedge it criticises. **Sweeping the row alone would have left 44 standing**, which is the
mistake DL-95 made with `read`. The row's boundary is not the word's boundary.

**It did not close P6, and the refrain check said so within the minute.** P6's last site was
*"The message landed."* ×3; all three became *"You got through."* — **a different refrain of the
same length.** The count did not move. See P6's row.

## P6 · repeats a line as a refrain

**shape** — a line repeated until it stops carrying weight.
**marks** — *"The world is not fine."* — ch2 p.25, p.27, p.30.
**search** — any sentence of 16–70 characters occurring 3+ times inside one chapter, with the
exercise apparatus excluded. `markpatterns.py P6`.
**count** — **1 in ch1–ch9 · 0 apparatus · 0 unmarked.**
**scope** — sentence-level and within-chapter, which is the shape Wendell marked. Excludes the 3-2-1
protocol, the BAR instruction and the RECEIPT block by name: **a form the reader learns to recognise
is not a refrain losing weight, and marking one would be vandalism.** Across chapters the same
search returns 37, topped by *"RECEIPT. Sit thirty seconds."* twelve times — all form.
**verdict — CLEAR, with its history, so CLEAR is not read as *never was a problem*.**

- **The named instance was already fixed.** *"The world is not fine."* stood three times when
  Wendell marked it. **It stands twice now**, and nobody recorded that against P6.
- The one remaining site is `ch3:363`, and on 2026-09-10 it changed words without changing shape.
  It was *"The message landed."* ×3; DL-99 rewrote all three as *"You got through."* — **a
  different refrain of the same length, and this check flagged it within the minute.** Recorded
  rather than filtered: adding it to the apparatus list would be tuning a counter to make a
  number go green, which is the evasion this repo already has on file.
- **The open question, and it is one sentence.** All three are the same taught line, said at the
  same stage of the same model — the reader is meant to learn it, the way they learn *"Two
  minutes to capture it as a BAR."* By the panel's own rule a form the reader recognises is not a
  refrain losing weight. **If that holds, the three are apparatus and the row is CLEAR on the
  same ground it already stood on.** If it does not, the three need to differ. Wendell's.

**No word-frequency row exists, and that is a ruling, not an omission.** Today's `the read` finding
— one word 23 times in one chapter — looked like P6 at word scale. It is not, and the measurement
says so: `the read` is **one per 670 words** and does not reach ch3's top twenty. A frequency
counter's top findings would be **game 175 (1 per 85)** in ch8 and **line 141 (1 per 88)** in ch4 —
the two chapters' own subjects. **Wendell found it by reading one word doing three jobs, one of them
hollow. A counter cannot have that, and a counter whose first output is the title of the chapter it
is reading is the 455-hit machine in a new coat.** *(Panel, Q1.)*

## P7 · construction scaffolding

**shape** — the build template left in the reader's text.
**marks** — *"Section 1: Urgency"* (Kotter step 1, verbatim); the `Section N:` numbering in all nine
chapters; *"Recap and Transition"* as a reader-facing heading in eight of them.
**search** — numbered section headings and the repeated template labels. `markpatterns.py P7`.
**count** — **0 in ch1–ch9 · 0 apparatus · 0 unmarked.**
**verdict — RULED · DL-84.** Applied by `strike_scaffolding.py`. Every H2 in ch2–ch9 rewritten, the
numbering moved to an invisible `<!-- SECTION N -->` anchor, `headings.py` built to keep it struck.
**The only one of the seven that is finished.**

---

## What this table refuses

It does not sweep a row. It does not build a counter before a row asks for one — and P6's row is the
worked case, where the measurement said the counter would not find the thing. It does not delete a
row that produced nothing: **P4 and P6 came back CLEAR and both stay**, because proving a pattern
does not reach the unmarked chapters is a result. It does not put a number in a cell that
`markpatterns.py` did not produce. And it does not widen `light_verb.py`, which is P5's
finding and somebody else's ruling. **It no longer refuses verdicts to reference pages** — that
refusal was the panel's and Wendell overruled it the next morning.

## One thing this table did not catch, and it matters

**The rows are searched one at a time and a sentence can sit on two rows. Nothing here notices
that.** P6's last site was a P5 sentence. DL-96 moved 43 `read` nouns while `lands` sat inside
several of the same sentences untouched, because that was a different row. **The same limit is
what nearly made DL-98 stop at 59 sites when the word ran to 103** — the row's boundary is not
the word's boundary, and only Wendell's *"all of it"* caught it. Written down rather than solved.

## What is waiting on Wendell

**Two rows are OPEN and neither is touched.**

- **P3, 15 signpost sites in chapters he has not read.** Including one sentence standing identically
  in ch7 and ch8.
- **P5, 49 sites in unmarked chapters, plus a hole in the instrument built to catch them.**

**And the input this table exists to substitute for: 88,915 words, 78% of the book, never read on
paper.** Nothing in here is worth one marked page of ch6.
