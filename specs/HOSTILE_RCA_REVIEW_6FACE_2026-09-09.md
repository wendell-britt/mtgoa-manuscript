---
type: panel
title: "Hostile review — what the root cause analysis got wrong"
aliases:
  - hostile rca review
  - attacking the incident writeup
tags:
  - mtgoa
  - editorial
  - pipeline
  - incident
created: 2026-09-09
source:
  - specs/RCA_STALE_SOURCE_REVERT_2026-09-09.md
  - instruments/box_the_records.py
  - instruments/ruling.py
---

# Hostile review of the RCA

Six Faces attacking `RCA_STALE_SOURCE_REVERT_2026-09-09.md`. The brief is not to improve it. It is
to find what it is wrong about, what it excuses, and what it invented.

---

## CHALLENGER · the Line — *it blames a condition to avoid naming a choice*

The RCA's root cause is *"the book keeps its frame prose in two files with no declared arbiter."*
That condition is real, it predates today, and **it is not sufficient.** It sat there for weeks and
nothing was destroyed. What destroyed prose was one line of code choosing `apply_chapter` to place
a box.

There was a simpler path. It is the path used on the second attempt: write the block where the
passage already sits. It took no longer, needed no rebuild, and could not have reverted anything.
**Nobody forced the first version. The condition was the hazard; the choice was the defect**, and
an analysis that lands on the condition has quietly converted a decision into weather.

**Verdict: the root cause is one layer too abstract, and the abstraction flatters the author.**

## ARCHITECT · the Design — *"six green boards" is theatre*

The RCA opens with a table of six checks that passed, presented as a systemic failure. **Not one of
those six was ever designed to catch this.** `gate.py` counts banned words. `coherence.py` checks
the pipeline against itself and says so in its own docstring. `shipcheck.py` has seven declared
categories and this is not among them. A check that was never meant to catch X has not failed when
it does not catch X.

Two of the six are fair: `--verify`, which people quote as evidence the marginalia are safe, and
`ruling.guard`, which is the only control that stands between a ruling script and the manuscript.
**The other four are padding**, and padding an incident makes it look like a collapse rather than
one bad line, which is exactly the framing that leads to four new mechanisms.

**Verdict: cut the table to two rows. The inflation drives the over-remediation.**

## SAGE · the Board — *the remediation contradicts the RCA's own finding*

The RCA's Sage section says the system was built to record rather than stop, and that the first
time a recorded hazard fired the recording did nothing. **Then the remediation proposes a new
check, a new tier, and a new comparison.** Three more mechanisms, answering a finding that says
mechanisms have not been the problem.

Worse, it congratulates itself for refusing to build all four, which is the shape of an argument
that has already decided to build three.

Name the game: **an incident caused by machinery is being remediated with machinery, and the
document notices this and proceeds anyway.**

**Verdict: the remediation does not follow from the analysis. At most one new mechanism is
defensible, and it has to be argued for on its own, not inherited from a list.**

## SHAMAN · the Body — *the detection story is dressed up*

The RCA calls the detection *"an unexpected pass"* and *"a thin thread"*, which makes it sound like
intuition. What actually happened is duller and better: **the result of a write was read, and
compared against a number from the previous run.**

That is not a thread. It is the only control that worked today, and **it worked twice** — it also
caught the staging bug in `retire_treatise.py` an hour earlier. Both silent failures were caught
the same way, by reading the result instead of the exit code.

The RCA treats its own working control as an accident and then proposes to replace it with a
pre-write gate. **You do not replace the thing that worked.**

**Verdict: the RCA misidentifies its own success. Post-write verification is the control; formalise
that before adding anything upstream of it.**

## DIPLOMAT · the Table — *the hazard tier is a bad idea and it is Wendell's rule*

Remediation 3 proposes that an unruled entry be able to fail a run. Two objections.

**It reverses a rule Wendell approved this morning**, FR-C9, and the RCA lists that rule under
*"contributing causes, and all three are ours."* Assigning a decision he ruled to *our* causes, and
then proposing to overturn it, is a move that should be visible rather than buried in a table.

**And it would not survive contact.** Candidates exist so an observation is not lost. Let them fail
runs and every unruled observation becomes a blocker; within a week somebody is deleting entries to
get work done, which is the exact evasion pattern this repo already has on file with `quiet` and
`careful`.

**Verdict: kill remediation 3. The candidate tier is not what failed.**

## REGENT · the Inheritance — *no counterfactual was run*

The RCA asserts the blast-radius guard *"catches this incident and the other silent failure
today."* **It does not demonstrate it.** No test, no reconstruction, nothing.

This repo has a standing rule about exactly that, written this morning and already load-bearing:
*a spec that proposes a mechanism is not specified until its worked example has been run against
the mechanism, in writing.* The RCA proposes four mechanisms and runs none of them.

The claim is probably true. Probably is what the rule exists to remove.

**Verdict: unproven. Any remediation must be run against both of today's failures before it is
called specified.**

---

## What survives, six of six

**Held.**

1. **`--verify` is blind by construction** and its passing sentence has been quoted as safety in
   four commit messages. That one is real and it is not padding.
2. **`ruling.guard` checks the count of edits and not their scope.** A script declared four edits
   and changed fifty-nine lines in one chapter. This is the single defect that stands.
3. **The two-copy condition is a real hazard** and it is the thing that made a scope failure
   destructive rather than merely wrong.

**Overturned.**

4. **The root cause was misstated.** It is not the two copies. It is that **an edit script may
   write anything and nothing compares what it wrote to what it declared.** The two copies turned
   an unbounded write into a silent revert.
5. **The six-board table is inflated** and should be two rows.
6. **The detection story is backwards.** Post-write verification is the control that works, twice
   in one day. It should be formalised, not treated as luck and superseded.
7. **Remediation 3, the hazard tier, is killed.** It reverses a rule of Wendell's on a cause that
   was not the cause, and it would be evaded within a week.

**The one thing nobody defended.** The RCA never asks whether the script should have existed. Four
passages, four edits. A tool able to rewrite six chapters was built to place four boxes, and its
capability is what converted a mistake into damage. **Scale the mechanism to the job** is a finding
none of the six can argue against, and it appears nowhere in the original analysis.
