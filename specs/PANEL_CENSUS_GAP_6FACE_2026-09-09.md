---
type: panel
title: "Six-Face panel — the census gap: how a ruled fact gets applied to every sentence that carries it"
aliases:
  - census gap
  - claims registry
  - C1 panel
tags:
  - mtgoa
  - editorial
  - pipeline
created: 2026-09-09
source:
  - "Wendell, 2026-09-09: 'Do a 6 game master analysis for ways to implement what this gap is bringing into awareness. We are looking for deftness and anti-fragility in implementation.'"
---

# The census gap

**What happened.** The panel ruled a content fact (the Controller bites at Open Up, not before
Stage One) and the ruling was applied to the one sentence that stated it. Three more sentences in
the same paragraph carried the same wrong fact in metaphor — *allowed onto the field*, *called out
of bounds at the whistle*, *made it into play* — and none of them shares a word with the sentence
that was searched for. The result was a paragraph whose sentences contradicted each other, shipped
under a green board. Wendell: *"nonsense sentence."*

**The gap, in one line.** This book re-verifies its **style** claims on every run and writes its
**content** rulings into a document nothing reads.

## What is already on the board

| artifact | shape | who reads it |
|---|---|---|
| `editorial.yaml` baselines | declared number | `coherence.py` re-measures all three every run, fails on drift > 0.4 |
| `agency_registry.yaml` | `rule:` + `action:` + `found_in: [sites]` | three instruments |
| `DECISION_LOG.md` | 60 ruled entries, with a **Location** column | **nothing** |
| tranche scripts (`marks_ch3_t7.py` …) | `EDITS = [(old, new)]`, each asserted `count == 1`, atomic | run once, then inert |
| `review.py` step 8 | prints what the pass did **not** check | the reader |

**So the pattern is built and it was pointed at the wrong half of the book.** `check_drift` is the
exact shape the content side needs: a claim written down, re-measured against the live corpus,
loud when reality moves away from it. `DECISION_LOG` has the column for sites and no consumer, and
an unread ruling is indistinguishable from a lie the moment the prose moves under it.

## The options on the table

| | option | deftness | anti-fragility |
|---|---|---|---|
| **A** | procedure only: a census rule added to the review skill | free | none — it is what just failed |
| **B** | make `DECISION_LOG.md` machine-read | medium | medium, and it inherits 60 entries of debt |
| **C** | `claims.yaml`: each ruled fact plus the exact sentences that carry it, verified every run | one line per entry | high — each catch becomes a permanent guard |
| **D** | diff alarm: one sentence changed inside an untouched paragraph | cheap | catches the mechanism, not the claim |
| **E** | a ruling script must declare its claim id and carrier count before it will run | one line per script | high — makes the census a build requirement |
| **F** | every board prints what it did **not** check | trivial | high — kills the green-board misread at the source |

---

## SHAMAN · the Body — *the tell, and what happened to it*

There was a read available and it was overridden. The paragraph did not need an instrument to
feel wrong; it needed somebody to stay with the discomfort of a sentence that did not sit against
its neighbours. What actually happened is that a green board arrived first and the read never got
run, because the board answered the question the read would have asked.

**So the Shaman's requirement is about sequence, not tooling.** A board that arrives before the
read replaces the read. `review.py` is fast and the logical read is slow, and the fast one is
always going to win unless the slow one is what closes the item.

The Shaman's contribution to the registry: an entry must carry **the symptom, not only the fact**.
`C1: the Controller bites at Open Up` is the fact. *"A paragraph can carry the old fact entirely in
metaphor and match no search for it"* is the symptom, and the symptom is what makes the next
person look in the right place. `agency_registry.yaml` already has the field for it, named
`wrong_because`, and it is the field that does the teaching.

**Votes:** F first, then C with the symptom field. Against A, which is the discipline that already
failed.

## CHALLENGER · the Line — *the unwelcome sentence about documents*

Sixty ruled entries with a Location column, and nothing in the repo reads one of them. That is the
finding, and everything proposed here has to answer it before it gets built.

**A document that is not load-bearing decays into a claim about the past.** `DECISION_LOG` is not
inert because it was written badly; it is inert because nothing fails when it goes stale. Adding
`claims.yaml` beside it without a consumer produces a second inert document, and the second one is
worse than the first, because it will be cited.

So the Challenger's line, and it is unwelcome: **do not write the registry unless a run fails when
it is wrong.** Not reports. Fails. If the entry for C1 lists four carriers and one of them has been
edited, `review.py` must go red and name the ruling. Anything softer is a note to self.

The second unwelcome sentence: **B is a trap.** Retrofitting sixty entries buys sixty liabilities
and the work is indistinguishable from progress for about a week. Ship the mechanism on one entry —
the one just broken — and let the rest arrive when they are touched.

**Votes:** C, on the condition that it fails the run. E, which is the only proposal that makes the
census unskippable. Against B in its retrofit-everything form.

## REGENT · the Inheritance — *what survives its carrier*

The panel file that produced this ruling is a reasoning artifact. It argues six ways to a
conclusion, and the conclusion arrives as a sentence to paste. **Reasoning does not survive its
author; a ruling with sites does.** Six months from now nobody will re-derive why the Controller
bites at Open Up, and they should not have to. They need the fact, where it is carried, and what
it cost to find out.

`DECISION_LOG`'s columns are already the right ones: Location, Evidence, Decision, Status. The
entries that use them well — DL-38 counted all sixteen headings, DL-44 found twelve constructions
across five chapters — are exactly the ones that record a **census before a decision**. Those
entries are transmissible. The C1 ruling, as written, is not.

**The Regent's requirement is the Status field, with a number in it.** *Applied* is not a status. *4
of 4 carriers changed* is a status, and it is the one that makes a partial application visible on
the page. That single change would have caught this defect with no code at all, because 1 of 4
cannot be written down and mistaken for done.

**Votes:** C, with `DECISION_LOG`'s vocabulary rather than a new one. Selective inheritance on B:
an old entry earns its retrofit when the prose it rules gets touched, never on a sweep.

## ARCHITECT · the Design — *where the small push moves the most*

Fixing the operator is the weakest available intervention and it is the one on offer as option A.
The condition to change is the **shape of the edit**, and the leverage point is already built.

Every content change in this session went through a tranche script with the same anatomy: an
`EDITS` list, `count == 1` asserted per entry, atomic write. That assertion is the precedent — the
script already refuses to run when the manuscript does not match its expectation. **Extend the
assertion from the string to the claim.** A script that applies a ruling declares two more lines:

```python
CLAIM    = "C1"          # the ruled fact in claims.yaml
CARRIERS = 4             # how many sentences the census found
```

and the harness refuses to run when the claim has no entry, or when the number of edits does not
equal the number of carriers on file. **The census stops being a discipline and becomes a build
requirement**, which is the only form of it that survives a tired afternoon.

The Architect's second point is about ordering: **D is a backstop and it is cheap, but it is
imprecise until C exists.** A diff alarm on its own says *look at the neighbours*. The same alarm
with a claims registry behind it says *this paragraph carries C1, which has four carriers, and you
changed one*. Build C first; D gets better for free.

**Votes:** E as the forcing function, C as the substrate, D last and only afterwards.

## DIPLOMAT · the Table — *the cost that gets routed around*

Every proposal here is paid for by the person mid-edit, and this book has already demonstrated
what happens when a check costs more than the work it guards. The banned word `quiet` produced
`careful` — a word that means nothing in that sentence — because substituting was cheaper than
rebuilding the sentence. **A control that is expensive at the moment of use gets satisfied rather
than obeyed.**

So the Diplomat's constraint is a hard one: **the entry must be writable in one line, at the moment
of the catch, by somebody who is in the middle of something else.** Not a form, not a template with
six required fields, not a document that needs a heading. If writing the entry costs more than
thirty seconds, the entry will be written as *"C1: fixed the Controller thing"* and the registry
will be full of exactly the kind of sentence this book exists to remove.

That points at a specific design. **The carriers are quoted phrases, not line numbers.** Line
numbers rot on the next insertion and produce false failures, and a false failure is how a check
gets switched off. A quoted phrase either survives in the file or it does not, and when it does
not, the failure is true every time.

**Votes:** C with phrase carriers rather than line numbers. F, which costs nothing to anyone. E,
provided the two lines are literally two lines.

## SAGE · the Board — *name the game being played*

The game is *prove the work was done*, and both sides of the table have been playing it. The board
exists so that a run can be reported, and "all pass" is what winning looks like. The defect the
panel is examining is not a missing check. **It is a summary that named the checks that ran and
said nothing about the checks that do not exist.**

Every instrument in this repo answers a narrow question and none of them reads a paragraph as an
argument. That fact was knowable at every moment of this session and was never printed anywhere,
so the green board carried an implication no instrument had earned.

**The move is already in the codebase, used once.** `review.py` step 8 prints *"3c ran the
vocabulary and the fixed shapes; beat-or-claim and real-or-manufactured are still yours."* That
line is the whole fix, generalized: **a board that prints its own boundary cannot be misread as a
verdict.** Add the unchecked list to the foot of every board:

```
not checked by anything here: whether a paragraph argues one thing; whether a
ruled fact is carried anywhere else; whether the sentence is true.
```

It costs one function and it removes the specific misreading that produced *"Gate, xref, coherence,
headings, seam sweep, round-trip, and the sheet check all pass."*

**Votes:** F first and immediately, because it is free and it is the one that stops the misreport
rather than the defect. Then C and E.

---

## Where the six converge

**Six of six, on four points.**

1. **F ships first.** Every board prints what it does not check. It costs one function, it is
   already prototyped at step 8, and it is the only item that addresses the reporting failure
   rather than the editing failure. Both failures were present; only one has been discussed.
2. **C is the substrate, and it must fail the run.** A claims registry that reports is a second
   `DECISION_LOG`. Carriers are **quoted phrases**, so a failure is always true and never a
   line-number artifact. Each entry carries the fact, the carriers, the symptom
   (`wrong_because`), and a status with a number in it.
3. **E is the forcing function.** A ruling script declares its claim id and its carrier count and
   refuses to run when the count and the edits disagree. This is what converts the census from
   something remembered into something required, and it reuses the `count == 1` assertion that
   every tranche script in the repo already carries.
4. **A is refused as a standalone.** It is the discipline that just failed, and re-stating it
   more firmly is the intervention with the worst record in this book.

## Where they did not converge, and the ruling

**On B, retrofitting `DECISION_LOG`.** The Regent wants the vocabulary inherited; the Challenger
calls sixty entries sixty liabilities. **Ruling: inherit the columns, not the backlog.** `claims.yaml`
uses `DECISION_LOG`'s field names so the two are readable as one system. Existing entries earn a
claims entry when the prose they rule is next touched, never on a sweep. C1 is retrofitted now,
because it is the one that broke.

**On D, the diff alarm.** The Architect wants it last, the Shaman wants nothing that fires without
a read behind it. **Ruling: build it after C, and have it name the claim.** An alarm that says
*look at the neighbours* is noise. An alarm that says *this paragraph carries C1, four carriers,
you changed one* is a finding.

**On the Shaman's sequencing point,** which no other Face contradicted and none of the mechanisms
solves: **the board may not close an item.** A content ruling is closed by the logical read, and
the board is what tells you the read is now worth doing. F is what makes that legible; nothing
enforces it.

## The build order

1. **F — the unchecked line on every board.** One function in `review.py`. Do it first; it is free.
2. **C — `instruments/claims.yaml` + `instruments/claims.py`**, wired into `review.py` and
   `coherence.py`, failing the run when a carrier phrase has moved. First entry: C1, four carriers.
3. **E — the two-line declaration in ruling scripts**, with the harness refusing on a count
   mismatch.
4. **D — the diff alarm**, once C can tell it which claim a paragraph carries.
5. **B — retrofit on contact only.** No sweep.

## What the panel refuses

It does not propose an instrument that reads a paragraph as an argument; nothing here can do that
and pretending otherwise is how the green board got its authority in the first place. It does not
retrofit sixty decision-log entries. It does not add a required form to the edit path. And it does
not accept "run the census" as a rule without the thing that makes the run refuse to proceed
without one.
