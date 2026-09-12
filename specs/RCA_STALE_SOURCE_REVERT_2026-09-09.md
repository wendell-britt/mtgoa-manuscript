---
type: rca
title: "Root cause — a script reverted approved prose and every check passed"
aliases:
  - stale source revert
  - DL-89 fired
  - the green board incident
tags:
  - mtgoa
  - editorial
  - pipeline
  - incident
created: 2026-09-09
source:
  - instruments/box_the_records.py
  - marginalia/compile.py
  - instruments/claims.yaml
status: SUPERSEDED IN PART, 2026-09-09. A hostile review overturned four of its findings and a
  counterfactual run refuted one of its claims. Read alongside
  specs/HOSTILE_RCA_REVIEW_6FACE_2026-09-09.md and specs/SPEC_WRITE_CONTRACT_2026-09-09.md.
---

# What happened

`box_the_records.py` placed four boxes by calling `apply_chapter(strip_marginalia(text))`, which
rebuilds a chapter's frames **from `insertions.py`**. That file is stale against the manuscript.
The rebuild replaced ch3's admissions page with the pre-proof-mark wording, putting back four
trailing-and constructions Wendell had marked on paper and approved the fix for.

**The script printed success and exited 0.**

## What each check saw

| check | result | why |
|---|---|---|
| `ruling.guard` | **pass**, "4 of 4 spans, census matched" | counts edits against the census. It cannot see what an edit does. |
| `compile.py --verify` | **pass**, "byte-identical" | compares `strip_marginalia(rebuilt)` against the stripped body. **Frames are removed from both sides before the comparison**, and the damage was inside a frame. |
| `gate.py` | **pass** | counts banned words. The reverted prose is older prose, not bad prose. |
| `claims.py` | **pass** | 28 guarded spans, **zero of them inside the reverted region**. |
| `coherence.py` | **pass** | checks the pipeline against itself, never content. |
| `shipcheck.py` | **SHIPPABLE** | none of its seven categories covers this. |

**Six green boards over a damaged manuscript.**

## What actually caught it

Not a check. An **unexpected pass**. I ran a diagnostic that had reported `ch3 regenerates
identically: False` an hour earlier, and it now said `True` for all three chapters. Nothing had
been done to fix that, so the only explanation was that the manuscript had moved to meet the
source rather than the other way round.

**The detection signal was a check getting healthier than it should have been.** That is a thin
thread, it depended on me remembering a number from an earlier run, and it is not a control.

---

## SHAMAN · the Body — *what a green board feels like now*

The board said pass six times over a broken manuscript. Every future green board carries that,
and it should. What is worth naming is the specific sensation at the moment of catching it: not
alarm, mild puzzlement that something had improved. **The signal arrived as good news.**

That is the hardest kind to act on. A red board is a charge with direction in it. An unexpectedly
clean one is a charge that presents as relief, and relief does not get investigated.

**Root cause, as the body reads it:** the pipeline can only produce alarm from a counter going up.
It has no way to say *this got better and nobody made it better*.

## CHALLENGER · the Line — *I raised the hazard and then fired it*

The unwelcome sentence, and it is about me. **DL-89 was written two hours before the incident. I
raised it, logged it, registered it, and reported it to Wendell in a numbered panel item.** Then I
wrote a script that did exactly the thing DL-89 describes, and the script's own docstring
described the mechanism approvingly: *"each passage is removed from the body and re-inserted from
insertions.RECORDS."*

**Documenting a hazard is not mitigating it**, and today the documentation was mistaken for the
mitigation by its own author, in under two hours.

The second unwelcome sentence is about the design. DL-89 was registered as a **candidate**, and
FR-C9 says a candidate *"MUST report and MUST NOT fail."* That rule exists so an unruled
observation is not lost. **Its effect here was to guarantee that a known live hazard could not
stop anything.** The tier built to preserve a signal also disarmed it.

## REGENT · the Inheritance — *two copies, no arbiter*

Strip the incident back and one fact remains: **the same prose exists in two files and nothing
declares which one is true.** 67 differing lines across ch3–ch8 right now.

Everything else is a symptom. The blind `--verify`, the reverting rebuild, the stale handbook, the
divergence that grows every time somebody edits the manuscript directly — all of it is downstream
of a book that keeps its frame prose twice.

This predates today by weeks. It will fire again, and next time the person holding it may not
remember a number from an earlier run.

**Root cause, stated once:** two authoritative copies is not a bug in a script. It is a missing
decision, and the decision has been available since the divergence was first measured.

## ARCHITECT · the Design — *the guard checks the count, not the blast radius*

`ruling.guard` asserts that a script's edit count equals the census. `box_the_records.py` declared
**four** edits. It changed **fifty-nine lines in ch3 alone**, none of them declared, and the guard
passed.

**That is the gap, and it is one function wide.** A ruling script already declares what it intends
to touch. The guard should verify that **nothing outside the declaration moved**: normalise the
corpus before and after, subtract the declared spans, and refuse on any difference.

It catches this incident. It also catches the earlier one today, where staging by append made two
chapters keep their signature block. **Both of today's silent failures were blast-radius failures**
and neither was a count failure, which is the only thing the guard measures.

Fixing `--verify` to compare frame content is correct and it is second, because a guard that
verifies blast radius catches the class regardless of how many copies of the prose exist.

## DIPLOMAT · the Table — *four mechanisms is the wrong answer*

There are four candidate fixes on this page and the temptation is to build all of them. Two of
them overlap: **if the book stops keeping two copies, there is nothing left for a frame-comparing
`--verify` to compare.** Ordering matters more than coverage here.

The one that must not be built is another check that reports and never fails. That is what DL-89
already was, and the incident is what it bought.

The Diplomat's own cost note: the blast-radius guard is a rule about how scripts behave, and it
will refuse things that are fine, especially wide reformatting passes. **It needs an explicit
override that is written down each time it is used**, or it becomes the check somebody comments
out at 11pm.

## SAGE · the Board — *the system was built to record, not to stop*

Name what the whole day produced. A claims registry. A decision log with ninety entries. Four
censuses. Five panels. Three specs. **Every one of them records.**

The first time a recorded hazard actually fired, the recording did nothing, and the thing that
caught it was a person noticing an anomaly by eye. **Recording felt like fixing**, and this
incident is the evidence that it is not the same act.

That is not an argument against recording, and it is not a volume complaint. It is a specific
claim about a specific gap: **the system has one tier that stops things (a ruled claim with
carriers) and one tier that only reports (a candidate). A known hazard with an unruled fix has no
home in the first tier and is defanged in the second.**

The Sage's addition: the detection signal here was an unexpected improvement, and nothing in the
pipeline can raise that. Worth remembering when the next remediation is designed.

---

## Consensus, six of six

**Root cause, in one line.** The book keeps its frame prose in two files with no declared arbiter,
and the only control that could have caught a script overwriting one with the other checks the
count of edits rather than their blast radius.

**Contributing, and all three are ours:**

1. **A known hazard was recorded in the one tier that cannot fail a run.** DL-89 was a candidate;
   candidates report and never fail, by a rule written this morning.
2. **The script's docstring described the hazardous mechanism as the design.** The author had
   written the warning two hours earlier.
3. **`--verify` is blind by construction.** It strips frames from both sides before comparing, so
   no frame content divergence can ever fail it, and its passing sentence has been quoted as
   evidence the marginalia are safe in four commit messages today.

## Remediation, in order

| | fix | why here |
|---|---|---|
| **1** | **Blast-radius check in `ruling.guard`.** A ruling script declares its spans; the guard normalises the corpus before and after and refuses if anything outside them moved. Explicit, written override for deliberate wide passes. | One function. Catches this incident and the other silent failure today, both of which were blast-radius failures and neither of which was a count failure. Works whether or not DL-89 is ever fixed. |
| **2** | **Rule DL-89: one authoritative copy.** Sync `insertions.py` from the manuscript, which is the shipped prose, then decide whether the source keeps existing at all. | Removes the root rather than guarding it. 67 lines to reconcile. **This one is Wendell's** — it decides which artefact is true. |
| **3** | **A hazard tier in `claims.yaml`.** An entry may be unruled on the fix and still fail the run on the danger. Today a candidate can only report. | Changes a rule Wendell approved this morning (FR-C9), so it goes to him rather than being built. |
| **4** | **`--verify` compares frame content.** | Becomes unnecessary if 2 is done properly. Build only if the two copies survive. |

**What the panel refuses.** It does not build all four. It does not add another check that reports
and never fails. And it does not treat the docstring warning in `box_the_records.py` as
remediation, since a warning written by the author who then ignored it is exactly what failed here.

---

## Corrections, same day

A hostile six-Face review of this document overturned four of its findings, and running the
counterfactual refuted a claim it makes above.

1. **The root cause was one layer too abstract.** *"Two copies with no arbiter"* is the hazard,
   not the defect. The condition sat harmless for weeks. What destroyed prose was a choice to
   rebuild with `apply_chapter` when writing in place was available and no slower. The defect is
   that **an edit script may write anything and nothing compares what it wrote to what it
   declared.**
2. **The six-board table is inflated.** Four of the six checks were never designed to catch this
   and say so in their own docstrings. Two rows are fair: `--verify` and `ruling.guard`. The
   padding is what made the incident read as a collapse and drove a four-mechanism remedy.
3. **The detection story is backwards.** This document calls the catch *"a thin thread."* It was
   post-write verification — reading the result and comparing it to the previous run — and it
   caught **both** of today's silent failures. That is the control that works, and it should be
   formalised rather than replaced by a pre-write gate.
4. **Remediation 3, the hazard tier, is killed.** It reverses FR-C9, which Wendell ruled this
   morning, on a cause that was not the cause, and it would be evaded within a week.
5. **Remediation 1's claim is false, and the counterfactual proves it.** This document says the
   blast-radius check *"catches this incident and the other silent failure today."* Replayed:
   containment fires on the revert (317 changed words outside the declared span) and **misses the
   staging bug entirely**, because that failure was an absence of change. The mechanism needs a
   completeness half. See `SPEC_WRITE_CONTRACT_2026-09-09.md` §6.

**And one finding nobody defended, absent from this analysis entirely:** it never asks whether the
script should have existed. Four passages, four edits. A tool able to rewrite six chapters was
built to place four boxes, and its capability is what turned a mistake into damage.
