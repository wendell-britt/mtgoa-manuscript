---
type: panel
title: "Six-Face panel — what to do next, with DL-89 closed"
aliases:
  - what next after DL-89
  - the marks are the input
  - ADJ tier refused
tags:
  - mtgoa
  - editorial
  - pipeline
created: 2026-09-09
source:
  - specs/DECISION_LOG.md
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
  - instruments/article.py
  - instruments/claims.yaml
status: ruled, six of six
---

# What next

DL-89 is closed. Six rulings landed today. The question on the table is what the next unit of
work is, and the panel is bound by Wendell's correction from this morning: *"This is productivity
for productivities sake… an assumption of productivity that I haven't made or asked for."* **The
panel is not deciding how to produce more. It is deciding what produces alignment.**

## Measured before anybody argues

- **49 spans changed today**, across six rulings. **22 in chapters Wendell has marked on paper.
  27 — 55% — in chapters nobody has ever marked.** Every one of those 27 was found by taking a
  ch3 mark and asking where else the shape occurs.
- **The proof marks cover ch2 and ch3 only**, pp.36–95. That is **24,741 words of 113,656: 22%
  of the book. 78% has never been read on paper.**
- **Yield per mark is the highest in the system.** Roughly thirty highlighted fragments in ch3
  produced six rulings, one retired formula spanning six chapters, one retired phrase, one
  instrument, one new instrument tier, and the DL-89 close.
- **Still open:** `DL-86` (one sentence, 41 words of subject before its verb), `DL-88` (needs one
  sentence from Wendell about a `[?]` mark), `DL-73` (already resolved in `termdebt.py`; its log
  cell still reads HELD).
- **Measured and unswept:** **248 ADJ sites**, **93 ROLE sites**.
- **No counter exists** for how often one word is asked to carry a paragraph. That hole was found
  by Wendell reading, not by anything here.
- `shipcheck.py`: **SHIPPABLE — no blocker outstanding.**

## The options as stated

| | option | whose hands |
|---|---|---|
| **A** | Wendell marks ch4–ch9 on paper | Wendell's |
| **B** | sweep the 248 ADJ sites | mine |
| **C** | sweep the 93 ROLE sites | mine |
| **D** | build a repetition counter | mine |
| **E** | close DL-86, DL-88, DL-73's stale cell | mine, except DL-88 |
| **F** | run the ch2–ch3 **mark patterns** against ch4–ch9 | mine |
| **G** | stop; it is shippable | nobody's |

---

## SHAMAN · the Body — *the marks are the only real signal in the room*

Everything that worked today started as a highlighter on paper. Not one of the six rulings began
with an instrument. `article.py` found sites; **it never once told anybody which sites mattered.**
Wendell did, four times, each time one layer below where I was working.

So the Shaman's read is that the input is upstream and it is scarce. 22% of the book has been
marked. The other 78% is unread by the only reader whose marks have ever produced a ruling.

**But the Shaman will not vote A**, and the reason matters. A is Wendell's labour, and this panel
was asked what *we* do next. Recommending that the author go and work is not a finding; it is a
way of having no finding. What the Shaman can say is that **nothing I build in the next hour will
be worth one page of ch6 with a highlighter through it**, and that the measurement says so rather
than my opinion.

**Votes:** F. It is the only option that turns marks already made into coverage of chapters not
yet marked, and it needs nobody but me.

## CHALLENGER · the Line — *refuse the ADJ tier out loud*

B is the option that will get chosen by drift if nobody says no, because it is the biggest number
on the board and the easiest to start. **248 sites.** So: no.

The ADJ tier was built with a note against it, in its own docstring, saying the wide version
produced 455 hits in ch3 alone and was thrown away because *a check that cries 455 times gets
switched off*. **248 is the same object at half the volume.** And the tier is explicitly the
low-precision one — it cannot tell a deliberate quotation of a social phrase from a lapse.

Sweeping it means reading 248 paragraphs and changing perhaps fifteen, and the other 233 readings
are how a person stops trusting the instrument. **Worse: I would be the one deciding which
fifteen**, on a tier the docstring says reports and does not grade.

C is the same shape with a smaller number and a better reason to leave it: the ROLE tier exists
because **Wendell** spotted what it measures, and its 93 sites are mostly the handbook formula we
just rewrote. Let it sit until somebody reads a chapter and hates one.

**Votes:** B refused, on its own docstring. C deferred. F.

## REGENT · the Inheritance — *what has already been paid for and not yet collected*

The Regent's question is always what the book already owns.

It owns **thirty proof marks on ch2 and ch3**, and it has collected on them twice: once by fixing
the marked lines, and once today by asking what the marks *predict*. **The second collection was
worth more than the first — 27 spans against 22.** That yield has not been exhausted; it was
stopped when the day ran out, not when the marks ran dry.

Concretely, the mark set names shapes that were never searched beyond where they were found:
`DL-86`'s forty-one-word subject was censused in ch3 only, and its own log cell says a book-wide
census *"needs an instrument rather than a phrase search"*. That is one shape. There are others
in the ledger with the same footnote.

**F is collecting on an asset already bought.** A is buying another one. The Regent does not vote
against A, but it will not buy before it has collected.

**Votes:** F, then E as cleanup. A is next after F, and it is Wendell's to schedule.

## ARCHITECT · the Design — *F has a design flaw and it is fixable*

The Architect agrees F is right and will not let it be run the way today was run.

Today's method was: notice a shape, grep it, read the hits, rule. That worked six times and it
also produced **four wrong scope claims in one day** — five sites when there were ten, nineteen
licensed when there were eighteen, eleven lines when there were ten, thirty PRO sites when there
were twenty-four. Every one was caught, three of them by a script's own closing recount and one
by Wendell. **The method is sound and the arithmetic around it is not.**

So the Architect's condition on F: **the pattern list is written down before the sweeping starts.**
Not held in the run of the work. A named file, one row per shape drawn from the ch2–ch3 marks,
each row carrying its search, its count, and its verdict. Then a sweep is a table being filled
rather than a memory being trusted, and a miscount is visible as an empty cell.

The second condition: **D is inside F, not beside it.** The repetition hole was found by Wendell
noticing one word 23 times. That is a shape from the mark set, so it belongs in the table as a
row — and whether it becomes an instrument is answered by what the row measures, not decided in
advance. **A counter built before its row is filled is the 455-hit mistake again.**

**Votes:** F, with the pattern table written first. D folded into F as a row. B refused.

## DIPLOMAT · the Table — *who is waiting on whom, and DL-88*

The Diplomat counts what is blocked on somebody.

`DL-88` has been open all day waiting on **one sentence from Wendell** about whether a `[?]` mark
was a mark at all. It is one carrier and one question. It has been carried in three documents and
it will be carried in a fourth unless it is put in front of him plainly, once, at the top of a
reply rather than in the last paragraph.

`DL-73`'s log cell says HELD and the thing was resolved on 2026-08-05 inside `termdebt.py`. **A
board that shows three open items when two are open is a board nobody reads.** That is ten
minutes.

And the Diplomat's condition on F, which is the same one it attached to DL-89: **F must not
become a standing obligation that arrives without asking.** A pattern table with 248 rows in it
is a to-do list I will start working through on my own judgement, which is the failure Wendell
named this morning. **The table records; it does not authorise.** Each row gets ruled or refused
by him, or it sits.

**Votes:** E first, because it is short and it clears the board. Then F, table-first. DL-88 asked
plainly.

## SAGE · the Board — *name what G is really asking*

Six of the seven options are work. **G is the one nobody wants to say out loud**, and the Sage's
job is to say it: `shipcheck.py` reports SHIPPABLE and has done all day, through six rulings that
each changed prose in the shipping book.

That is not an argument for stopping. It is an argument that **shippable and finished are
different words, and only one of them is measured here.** Every green board today was accurate
and none of them was the reason the work happened. The reason was a person with a highlighter.

So the Sage's finding, which outlives this panel: **the pipeline cannot tell you what to do next.
It can only tell you that what you did held.** Asking it for direction is the category error that
produced *"all pass"* this morning, and the honest answer to *what next* comes from the 78%, not
from the instruments.

One procedural note, repeating this morning's because it applied again today: **where a
measurement shows the answer, write it down and let Wendell overrule the record.** F is that.
Nobody needed a panel to know that marks already made were not fully collected.

**Votes:** F, table-first, D inside it. E as cleanup. **A named as the real input, and named as
Wendell's alone to schedule.** B refused. G refused as an answer and kept as a fact.

---

## Consensus, six of six

**Do F, and write the table before sweeping anything.** Take the shapes the ch2–ch3 marks name and
run each one across ch4–ch9, into a named file with one row per shape carrying its search, its
count and its verdict. **55% of what changed today was found this way**, in chapters nobody has
marked, and the vein was not exhausted — the day was. The table exists so a sweep is a table being
filled rather than a memory being trusted, after four wrong scope claims in one day.

**Fold D into F as a row.** The repetition hole is a shape from the mark set. Whether it becomes an
instrument is decided by what its row measures, not before.

**Do E first; it is short.** Close DL-86's one sentence, put DL-88's single question to Wendell
plainly and at the top, and fix DL-73's stale cell, which shows three open items when two are open.

**B is refused on its own docstring.** The ADJ tier's 248 sites are the 455-hit object at half
volume, on the tier that explicitly reports and does not grade. Sweeping it means 233 readings that
change nothing, and me choosing the fifteen. **C is deferred**, not refused: it exists because
Wendell spotted what it measures, and most of its 93 sites are the formula just rewritten.

**A is the real input and it is Wendell's alone.** 78% of the book — 88,915 words — has never been
read on paper. Nothing in the instruments will be worth one marked page of ch6. The panel names this
as a measurement and not as a recommendation, because recommending that the author go and work is a
way of having no finding.

## What the panel refuses

It does not sweep 248 sites because they are countable. It does not build a counter before its row
is filled. It does not treat SHIPPABLE as an answer to *what next*. It does not let the pattern
table become a to-do list I work through on my own judgement — **it records; it does not
authorise.** And it does not carry DL-88 into a fourth document.
