---
type: panel
title: "Six-Face panel — the questions the spec's own example opened"
aliases:
  - claims registry round two
  - two censuses
  - carrier scope
  - forbidden carriers
tags:
  - mtgoa
  - editorial
  - pipeline
created: 2026-09-09
source:
  - specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md
  - specs/PANEL_CLAIMS_REGISTRY_OPEN_Q_6FACE_2026-09-09.md
  - instruments/shipcheck.py
  - instruments/gate.py
---

# Round two — the spec fails its own seeding example

Q1 to Q3 were ruled. **These four came out of testing the spec against DL-78**, the entry it
proposes to seed itself with, and the first one is a defect in the spec rather than a question
about it.

## The measurement that opened them

DL-78's fact is *the Controller decides how you behave once inside; whether you go in is the
Protector's gate.* The spec seeds the entry with **four carriers**, which were the four spans in
one paragraph that had to change. The fact is actually carried in **eleven spans across seven
files**:

| where | what carries it |
|---|---|
| `ch2:286` | the charter — *"the Controller decides how you live. It sets the standard"* |
| `ch3:628` | *"The Protector decides whether you live. The Controller decides how."* |
| `ch3:640` | two spans in the rebuilt paragraph |
| `ch3:887` | *"behavior is at stake the moment an experience would show, which is Open Up"* |
| `ch4:512` `ch5:523` `ch6:382` `ch7:555` `ch8:540` | five near-identical remit sentences |

**FR-E3 would refuse to run on the very ruling it was written for.** It asserts that a script's
edit count equals the carrier count. Four spans needed changing; eleven carry the fact. The two
numbers are not the same number and the spec treats them as one.

**Q4.** A census has two jobs. Which one is `CARRIERS`?
**Q5.** How far does a census reach, and what makes it complete?
**Q6.** How do you register a ruling whose carriers are absences?
**Q7.** Which boards carry the boundary line, and what makes any of this run?

---

## SHAMAN · the Body — *the two censuses feel different because they are*

One of these is done in dread and the other in relief. Finding what must change is the anxious
pass: miss one and the book contradicts itself. Listing what now carries the fact is the settling
pass, done after the work, when you can see what the book says.

**They are separated by time as well as by purpose.** The edit census exists before the edit and is
finished the moment the script runs. The guard census exists forever after. Collapsing them into
one field is how the spec ended up asserting that a number from before the work equals a number
from after it.

On Q5, the Shaman's warning: **three of DL-78's carriers were found by reading and could not have
been found any other way.** *Onto the field*, *out of bounds at the whistle*, *made it into play*
share no vocabulary with the claim. Whatever scope field this design grows, it must have room for
*"read the whole of ch3 §5 and §6"* and not only for a search string, or it will record the easy
half of the census and imply the hard half was done.

**Votes:** two fields. A scope field that admits reads, not only searches.

## CHALLENGER · the Line — *"complete" is a word this registry may not use*

Q5 has an unwelcome answer: **you can never prove a census is complete, so the entry must not
claim to be.** Eleven carriers today; a twelfth arrives the next time somebody writes the word
Controller. An entry that says *carriers: 11* is read as *there are eleven*, and it will be wrong
within a month.

So the field records **where you looked**, not what exists. *"Every file matching `Controller
decides`, plus ch3 §5 read in full"* is falsifiable — somebody can re-run it and find the twelfth.
*"Complete"* is not falsifiable and is therefore worthless.

On Q6 the Challenger's line is aimed at `gate.py`. The banned list holds `rooms?`, `quiet`,
`genuinely`, `things?` — four rulings with **no ids and no reasons attached to them in the file**.
Anyone reading `editorial.yaml` today has to go looking for why. That is the absence tier already
built and already rotting, and the fix is one field: **a forbidden phrase carries the DL id that
banned it.** Build the tier, and repair the one that exists while you are there.

**Votes:** scope not completeness. Forbidden tier, with ids, and retrofit the banned list's four.

## REGENT · the Inheritance — *what the next person needs is the search, not the finding*

A finding is a fact about the book on one day. A search is something the next person can run. Of
the two, only the second survives.

So the Regent's answer to Q5 is the same shape as the last panel's answer to Q2: **store the
reproducible thing.** An entry carries `scope`, and where the scope is a grep, the grep is written
out so it can be re-run and the count re-derived. Where the scope was a read, it says which
sections were read and by whom. **A census that cannot be repeated is an assertion, and this
registry exists because assertions rot.**

On Q4: `applied` and `carriers` are different fields because they answer different people.
`applied: 4 of 4` answers *did the work finish*, which is a question about a moment.
`carriers: [11 spans]` answers *what is load-bearing now*, which is a question about the book.

**Votes:** two fields with two names. `scope` stores a runnable search.

## ARCHITECT · the Design — *the spec has a bug; fix the bug before ranking the questions*

Q4 is not a question. **FR-E3 is wrong and has to change**, and the correction is one line: the
script's edit count is asserted against the **applied** count, never against the carrier list.

| field | census | when | what it feeds |
|---|---|---|---|
| `applied: N of M` | the edit census — spans that had to change | before the edit, closed by the script | **shipcheck blocker** when `N < M` (FR-C10) |
| `carriers: [...]` | the guard census — spans that now carry the fact | after the edit, forever | **drift check** in `review.py` and `coherence.py` (FR-C5) |

**Everything the last panel ruled survives this correction**, which is how you know the correction
is right and not a redesign. The ambiguous signal is still the board's; the unambiguous count is
still the press's.

On Q7 the Architect's answer is uncomfortable and short. **There is no hook in this repo.** No
`.claude/settings.json`, no hooks directory, nothing that runs on commit. Every instrument here
fires because a person typed its name, and the one time that discipline failed this session is the
reason this spec exists. Wiring `claims.py` into `coherence.py` is correct and it does not solve
this. **Say so in the spec rather than letting the wiring imply automation that is not there.**

**Votes:** fix FR-E3. Two fields. Name the residual dependency on a person instead of hiding it.

## DIPLOMAT · the Table — *eleven carriers is where this gets abandoned*

The last panel set the constraint: resolution must cost one line. Now look at what eleven carriers
across seven files does to that promise. Rewrite ch5's daemon-door paragraph and the run goes red
on a claim ruled in ch3, about the Controller, in a session about the Regent. That is the moment
somebody deletes an entry.

**So the number matters to adoption, and the fix is in FR-C3, which is already written and needs
teeth.** A carrier is *the shortest distinctive span*, not the sentence. `Controller decides how`
survives every rewording of those five near-identical sentences that keeps the fact; it breaks only
when the fact breaks. Eleven long carriers is a tripwire across the corridor. Eleven short ones is
a guard.

The Diplomat's second point, on Q6: **a forbidden phrase is cheaper to satisfy than a required
one**, because the fix is deletion and deletion is always available. That makes the absence tier
the safest thing here to build, and it should not be treated as the exotic case.

**Votes:** shortest-distinctive-span promoted from SHOULD to MUST. Forbidden tier early.

## SAGE · the Board — *notice what just happened*

The spec was written, ruled by a panel, committed, and it was wrong. It was found wrong in about
four minutes by testing it against the one example it names. Nobody had done that, including two
panels.

**That is the game, and it is the same game as `all pass`:** an artefact that has been reviewed
feels finished, and reviewed is not tested. The census gap panel found sixty unread rulings. This
panel found a spec whose worked example refutes its own requirement. **Both are the same failure:
the artefact was never run against reality.**

So the Sage's addition, and it costs nothing: **every spec in this repo that proposes a mechanism
must name a worked example and check the mechanism against it before the spec is called
specified.** `SPEC_CLAIMS_REGISTRY` had a seeding test in §5 and the test was written but never
performed. Perform it, in the spec, in writing.

On Q7: the boundary line goes on **every board that prints a verdict**, and `shipcheck.py` prints
*"SHIPPABLE — no blocker outstanding"*, which is the most dangerous sentence in the repo. It is
true only within its six categories and reads as a verdict on the book.

**Votes:** boundary on every verdict-printing board, shipcheck included. A performed worked
example as a precondition for calling a spec specified.

---

## Consensus, six of six

**Q4 — two censuses, two fields. FR-E3 is a defect and changes now.**

- `applied: N of M` — the spans that had to **change**. Closed when the ruling script runs. A
  script asserts its edit count against **this**. `N < M` is the shipcheck blocker.
- `carriers: [...]` — the spans that now **carry** the fact and must not drift. Open forever. This
  feeds the board-level drift check.
- DL-78 is therefore `applied: 4 of 4`, `carriers:` eleven spans across seven files.

**Q5 — a census records its scope, never its completeness.** The entry carries a `scope` field
naming the search performed: the grep, written out so it can be re-run, and the sections read in
full where no search could reach. Nothing in the registry may say *complete*. A count is what was
found by a stated method on a stated day.

**Q6 — build the forbidden tier, and repair the one already in the repo.** A carrier may be a
phrase that MUST NOT appear anywhere in the corpus, which is how a ruling like the card cut is
guarded. `gate.py`'s banned list is this tier already, built without ids or reasons, and each of
its four entries earns a DL id. Absence is the cheap case, not the exotic one, because the fix is
always deletion.

**Q7 — the boundary goes on every board that prints a verdict, and the automation gap gets
written down.** `shipcheck.py`'s *"SHIPPABLE — no blocker outstanding"* carries the same misread as
*"all pass"* and gets the same boundary treatment. There is no hook in this repo and nothing runs
on commit; wiring `claims.py` into `coherence.py` does not change that. The spec states the
residual dependency on a person in plain words rather than letting the wiring imply otherwise.

**One addition all six accepted, and it is the Sage's.** A spec that proposes a mechanism is not
*specified* until its worked example has been run against the mechanism **in writing**. This spec's
own §5 named a seeding test that nobody performed, and performing it is what produced this entire
round.

## What changes in the spec

| item | change |
|---|---|
| FR-E3 | asserts edits against `applied`, never against `carriers` — **defect fix** |
| FR-C1 | entry gains `applied`, `carriers`, `scope`; `status` retired into `applied` |
| FR-C3 | shortest distinctive span promoted SHOULD → MUST |
| FR-C12 | forbidden-carrier tier: phrases that must not appear |
| FR-C13 | no entry may assert completeness; `scope` records the method |
| FR-F1 | boundary on every verdict-printing board, `shipcheck.py` included |
| FR-F5 | the spec states that nothing runs without a person; there is no hook |
| §5 | the seeding test is **performed in the spec**, not merely named |
| §9 | `gate.py`'s four banned words earn DL ids |

## What the panel refuses

It does not let the registry claim completeness. It does not let a long carrier stand where a short
one holds. It does not paper over the absence of automation by pointing at the wiring. And it does
not call a spec specified on the strength of two panels when four minutes against its own example
would have refuted it.
