---
type: spec
title: "The mark-pattern table — what Wendell's marks predict about the chapters he has not marked"
aliases:
  - mark pattern table
  - pattern table
  - P1-P7
tags:
  - editorial
  - mtgoa
  - proof
created: 2026-09-09
review: 2026-09-16
source:
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
  - specs/PANEL_WHAT_NEXT_AFTER_DL89_6FACE_2026-09-09.md
  - specs/DECISION_LOG.md
status: specified. Worked example run on two of the seven rows, and the run changed the spec.
---

# The mark-pattern table

**Wendell, 2026-09-09:** *"Create a spec for what you think should be done next. It's not clear
from the message."* Fair. The panel ruled *"do F"* and F was a direction, not a thing.

## 1 · What this is

A **table with seven rows**, one per pattern the ch2–ch3 proof marks name, in a file. Each row
carries the shape, the marks that name it, the search that finds it, what that search counted, how
much of the count sits in chapters nobody has marked, and a verdict.

**That is the whole deliverable.** Not a sweep. The table is the artefact; sweeping is what may or
may not follow, one row at a time, on a ruling.

## 2 · Why this and not something else

**The number that decided it.** 49 spans changed on 2026-09-09 across six rulings. **22 sit in ch2
and ch3, which Wendell has marked on paper. 27 — 55% — sit in chapters nobody has ever marked**,
and every one of the 27 was found by taking a ch3 mark and asking where else the shape occurs.

**78% of the book — 88,915 words of 113,656 — has never been read on paper.** The marks are the
highest-yield input in the system and they cover 22% of it. This table is the only way to spend the
marks already made on the pages they were never made on.

**Seven patterns already exist** at the bottom of `PROOF_MARKS_CH2_CH3_2026-09-09.md`, written as a
working list on 2026-09-09 and never searched beyond the pages they came from — except P7, the
scaffolding, which was ruled and applied, and P6, which today's `the read` work touched by accident
rather than by plan.

## 3 · What this is not

- **Not a to-do list.** *(Diplomat's condition, carried from DL-89 and repeated in the what-next
  panel.)* **The table records; it does not authorise.** A filled row is a measurement. It becomes
  work only when Wendell rules it, and a row may sit indefinitely without that being a debt.
- **Not a new instrument.** Rows are searches. Whether any row earns an instrument is answered by
  what its row measures. **A counter built before its row is filled is the 455-hit mistake** —
  `article.py`'s own docstring carries that story.
- **Not the ADJ sweep.** Refused by panel on the tier's own docstring: 248 sites is the 455-hit
  object at half volume, on the tier that explicitly reports and does not grade.
- **Not a substitute for Wendell marking ch4–ch9.** It is what can be done without that. The panel
  named the marks as the real input and named them as his alone to schedule.

## 4 · Requirements

### The rows

- **FR-M1** Exactly **seven rows**, `P1`–`P7`, one per pattern in `PROOF_MARKS_CH2_CH3`. New
  patterns get new ids; **a row is never deleted**, because a row that came back clear is a result.
- **FR-M2** Each row MUST carry: the **shape** in one sentence; the **marks** that name it, quoted;
  the **search**; the **total count**; the **count outside ch2–ch3**; and a **verdict**.
- **FR-M3** The verdict is one of: **CLEAR** (searched, nothing outside the marked chapters worth
  a reader), **OPEN** (sites found, awaiting a ruling), **RULED** (a `DL-` id, in the last column),
  or **UNSEARCHABLE** (no search of usable precision exists — see FR-M5).

### The counts

- **FR-M4** Every count MUST be produced by a **committed script**, never by a number written in
  prose. On 2026-09-09 I made **four wrong scope claims in one day** — five sites when there were
  ten, nineteen licensed when there were eighteen, eleven lines when there were ten, thirty PRO
  sites when there were twenty-four. Three were caught by a script's closing recount and one by
  Wendell. **A number in a cell that no script produces is a number I remembered.**
- **FR-M5** A row whose search cannot reach usable precision MUST be marked **UNSEARCHABLE** and
  MUST NOT carry a count. **P1 and P2 are expected here**: *"the `…, and [what it means]` tack-on"*
  and *"the verdict stamp"* are judgements about what a clause is doing, and any regex for them
  returns hundreds. Recording that honestly is the row's result. Faking a count is worse than an
  empty cell.
- **FR-M6** Each row's scope line **records the method, never the territory**. No row may claim
  completeness. *(Standing rule, `SPEC_CLAIMS_REGISTRY`.)*

### The relationship to the registry

- **FR-M7** A row that becomes **RULED** gets a `DL-` id and an entry in `claims.yaml` by the
  existing rules. **One id namespace.** The table does not become a second decision log; its last
  column points into the first.
- **FR-M8** The table is **re-runnable**. Its counting script prints every row's current count, so
  a row that was CLEAR in September can be re-checked after new prose lands without anybody
  re-deriving the search.

## 5 · The shape of a row

```
P4 · the hedges
  shape    the writer undercutting what was just said, in the writer's own voice
  marks    "I have guessed wrong in both directions" · "and I could be wrong"
           "I have not solved it. I teach here anyway."
  search   20 first-person hedge phrases, case-insensitive, manuscript + front matter
  count    2 total · 0 outside ch2-ch3
  scope    phrase list built from the four marked instances plus sixteen near neighbours.
           Cannot see a hedge phrased in words not on the list.
  verdict  CLEAR
  ruling   DL-88 (the one instance, ch3 Oreve, ruled and applied 2026-09-09)
```

## 6 · Acceptance

| # | test | expected |
|---|---|---|
| **A1** | a row carrying a count with no script behind it | rejected by review; FR-M4 |
| **A2** | P1 given a regex that returns 300+ hits | row is UNSEARCHABLE, no count |
| **A3** | a row searched with zero sites outside ch2–ch3 | **CLEAR, and the row stays in the table** |
| **A4** | a RULED row | has a `DL-` id and an entry in `claims.yaml` |
| **A5** | re-run the counting script after new prose | every row reports a current count |
| **A6** | a row deleted because it produced nothing | rejected; FR-M1 |

## 7 · The worked example, run

Per the standing rule: **a spec proposing a mechanism is not specified until its worked example has
been run, in writing.** Two rows were filled on 2026-09-09, before this spec was written, and the
run changed it.

**P4, the hedges.** 20 phrases, manuscript and front matter. **2 sites in the whole book, both
legitimate:** `ch3:44` is inside the admissions form, where *"I have been wrong about who was past
it"* is a Head admitting something on a filed document — the form's entire purpose; and `ch4:686`
quotes a hedge as the thing not to do (*"Most people bury their lines in qualifiers"*). **Verdict
CLEAR.** The one real instance was `ch3`'s Oreve note, which Wendell ruled today as DL-88.

**P3, the signposts.** 10 phrase families. **23 sites, 15 of them outside ch2–ch3** — *"Appendix G
says where to read her"* at `ch6:238`, *"that combination is what this chapter trains"* at
`ch8:615`, *"Every move in this chapter is an instrument for…"* at `ch8:857`. **Verdict OPEN.**

**What the run changed in this spec.** I wrote the first draft assuming every row would open work,
because that is what the day had done — *one true sentence* recurred in two chapters, the cost
formula in six. **P4 does not recur at all.** So:

- **FR-M3 gained CLEAR as a first-class verdict** and **FR-M1 forbids deleting a row.** Proving a
  pattern does *not* reach the unmarked chapters is a result, and a table that quietly drops its
  empty rows is a table that only ever grows a to-do list.
- **FR-M5, UNSEARCHABLE, exists because of the precision spread the run exposed.** P4's phrase list
  is high precision and returned 2. P3's is medium and returned 23 with maybe half worth a reader.
  **P1 and P2 have no precision available at all** at this shape, and pretending otherwise would
  put a fabricated number in a cell.

## 8 · Order of work

1. **Write the table file**, seven rows, five of them empty. Empty is legal and visible.
2. **Fill the rows that have a runnable search** — P3, P5, P6 — with a committed counting script.
3. **Mark P1 and P2 UNSEARCHABLE** unless a search of real precision turns up.
4. **P7 is already RULED**; record its id and close it.
5. **Stop.** Hand Wendell seven filled or honestly-empty rows. **Nothing is swept without a
   ruling.**

## 9 · Open questions

- **Q1** P6 is *"repeats a line as a refrain until it stops carrying weight."* Today's `the read`
  work — 23 uses of one word in one chapter — is the same shape at word rather than sentence scale.
  **One row or two?** The searches are different and the defect may be one thing.
- **Q2** Should the table cover **front matter, back matter and the appendices**, or only ch1–ch9?
  The marks came from chapter pages. P3's signposts would certainly appear in front matter, where
  they may be doing a legitimate job.
- **Q3** P5, the nothing-word verb, overlaps `light_verb.py` (review step 3f) and `slop`. **Is the
  row a new search or a reading of an existing counter's output?** If the counters already see it,
  the row's value is the verdict, not the count.

## 10 · What this spec refuses

It does not sweep anything. It does not build a counter before a row asks for one. It does not
delete a row that produced nothing. It does not put a number in a cell that no script produced. And
it does not treat the table as permission — **each row waits for a ruling, or it sits.**
