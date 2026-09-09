---
type: spec
title: "The write contract — a ruling script proves what it changed and what it did not"
aliases:
  - write contract
  - blast radius guard
  - containment and completeness
tags:
  - editorial
  - mtgoa
  - pipeline
created: 2026-09-09
review: 2026-09-16
source:
  - specs/RCA_STALE_SOURCE_REVERT_2026-09-09.md
  - specs/HOSTILE_RCA_REVIEW_6FACE_2026-09-09.md
  - instruments/ruling.py
  - marginalia/compile.py
status: specified, not built. Worked example run against both of today's failures.
---

# The write contract

Two scripts wrote silently wrong manuscripts today and both reported success. The hostile review
of the incident analysis threw out most of that analysis; what follows is built only on what
survived it.

**The defect, restated after the review corrected it.** Not *"the book keeps two copies."* That is
the hazard that made the damage destructive. The defect is that **an edit script may write anything
and nothing compares what it wrote to what it declared.**

---

## 1 · The two failures this must catch

| | script | what it did | shape |
|---|---|---|---|
| **F1** | `box_the_records.py` v1 | rebuilt each chapter from a stale source and reverted ch3's admissions page to pre-proof-mark wording | **over-write** — changed prose it never declared |
| **F2** | `retire_treatise.py` v1 | staged ch6 and ch7 twice; the second write discarded the first, so two signature blocks never moved | **under-write** — declared work that silently did not happen |

**They are opposite shapes, and that is the whole design constraint.** The incident analysis
proposed a blast-radius check and asserted it caught both. §7 runs it. It catches F1 and misses F2
entirely.

## 2 · What this is not

Ruled out by the hostile review, recorded so they are not re-proposed:

- **Not a hazard tier in `claims.yaml`.** It reverses FR-C9, which Wendell ruled this morning, on a
  cause that was not the cause. Candidates exist so an observation is not lost; let them fail runs
  and every unruled observation becomes a blocker, and entries get deleted to clear work. This repo
  already has that evasion on file.
- **Not a fix to `--verify`'s blindness.** Real, and it becomes unnecessary if the two-copy
  condition is ruled. Build it only if the copies survive.
- **Not four mechanisms.** The review's finding was that machinery caused this and three more
  pieces of machinery is not the answer. **One mechanism.**
- **Not a replacement for reading the result.** Post-write verification caught both failures today.
  It is the control that works and this contract formalises it rather than superseding it.

## 3 · Requirements

### The declaration

- **FR-G1** A ruling script MUST declare its writes as `(file, old_text)` pairs, not as a count.
  This is the shape the tranche scripts already use — `EDITS = [(old, new), ...]` — so the
  declaration is the edit list, made addressable rather than merely countable.
- **FR-G2** The declaration MUST name every file the script may write. A file not in the
  declaration MUST NOT be written.

### Containment — did it change anything it did not declare

- **FR-G3** Before writing, the harness MUST compare each file's normalised text before and after.
  Every difference MUST fall inside a declared `old_text`. Any difference outside one is a refusal.
- **FR-G4** Normalisation MUST ignore line wrapping, quote prefixes and emphasis markers, so that
  boxing a passage or rewrapping a paragraph is not reported as prose change. **Byte-level
  differences outside declared spans MUST be reported and MUST NOT fail**, since reflow is legal
  and silent word substitution is not.

### Completeness — did the declared work actually happen

- **FR-G5** Every declared `old_text` MUST be absent from the written file, and its `new` present.
  A declared edit that did not take is a refusal. **This is the half that catches F2**, and no
  containment check can.
- **FR-G6** The two checks MUST be reported separately. *"Containment ok, completeness failed"* is
  a different fault from its opposite and they have different fixes.

### Refusal

- **FR-G7** Refusal MUST be atomic: nothing written, matching the existing tranche contract.
- **FR-G8** The refusal MUST name the file, the check that failed, and one example difference.
- **FR-G9** An override MUST exist for deliberate wide passes, and it MUST require a written reason
  recorded in the script. A control with no override is a control somebody comments out; a control
  with a silent override is not a control.

### Scope of the mechanism

- **FR-G10** The contract lives in `instruments/ruling.py` beside `guard()`, which already holds
  the census check. **No new instrument.** One import, one call, matching FR-E4's two-line cost.

## 4 · What is a decision, not a mechanism

Two findings survived the review that no code addresses. They belong to Wendell.

- **The two-copy condition, DL-89.** `insertions.py` and the manuscript disagree by 67 lines. The
  contract makes an unbounded write visible; it does not decide which artefact is true. That
  ruling is still open and still his.
- **Scale the mechanism to the job.** Nobody on the panel could argue against it and it appears
  nowhere in the original analysis. Four passages needed four edits. A tool able to rewrite six
  chapters was built to place four boxes, and its capability is what turned a mistake into damage.
  **A script that can do more than the job is a hazard proportional to the difference.**

## 5 · Acceptance

| # | test | expected |
|---|---|---|
| **A1** | replay F1: rebuild ch3 from the stale source, declare only the session log | **containment fails**, naming ch3 and one differing phrase |
| **A2** | replay F2: declare six signature moves, apply four | **completeness fails**, naming the two that did not take |
| **A3** | a correct run of `box_the_records.py` | both checks pass |
| **A4** | reflow a declared paragraph without changing a word | containment passes; byte difference reported, not failed |
| **A5** | write a file not in the declaration | refusal, nothing written |
| **A6** | override with no written reason | refusal |

## 6 · The worked example, run

Per the standing rule: a spec proposing a mechanism is not specified until its worked example has
been run against it, in writing. **Both failures were replayed on 2026-09-09 before this spec was
written, and the run refuted the incident analysis.**

**F1, containment.** Rebuilt ch3 from `insertions.py` as the bad version did, then compared
normalised text against the pre-incident file:

```
words changed anywhere: 317
sample: -qualities, -together -or +qualities +and +will -at -all. +take +one
```

Those words are the admissions page, which the script never declared. **Containment fires.**

**F2, containment.** Replayed the staging bug, where ch6 was left untouched:

```
words changed outside declared spans: 0   -> containment PASSES (wrongly)
declared span "the fourth treatise, submitted by Irix Vale" still present: True
```

**Containment misses it completely.** The script's failure was doing nothing, and a check that
looks for unexpected change cannot see absent change.

**What the run changed in this spec.** The RCA claimed the blast-radius check *"catches this
incident and the other silent failure today."* **That claim is false.** It catches one of two.
FR-G5 exists because the counterfactual was run rather than assumed, and the mechanism is two
halves rather than one.

## 7 · Open questions

- **Q1 · Normalisation depth.** FR-G4 proposes ignoring wrapping, quote prefixes and emphasis so
  that boxing is not flagged as prose change. That also means a change from `*word*` to `word` is
  invisible to containment. Today's boxing did exactly that to two phrases, deliberately. Is
  emphasis inside the containment check or outside it? **Proposed: outside, reported separately.**
- **Q2 · Who may override, and where is the reason recorded?** Proposed: in the script, as a
  required string argument, so it lands in the commit and in review.
- **Q3 · DL-89**, unchanged and still Wendell's: which of the two copies is authoritative.

## 8 · What this spec refuses

It does not build four mechanisms. It does not touch the candidate tier. It does not claim to make
the pipeline safe, since the control that actually caught both failures today was a person reading
the result of a write, and this contract only makes that reading cheap and mandatory rather than
remembered. And it does not assert that the mechanism catches both failures, because it was run
and it does not.
