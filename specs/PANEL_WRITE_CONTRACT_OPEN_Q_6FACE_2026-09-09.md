---
type: panel
title: "Six-Face panel — the three open questions in the write contract"
aliases:
  - write contract open questions
  - normalisation depth
  - the override
  - which copy is true
tags:
  - mtgoa
  - editorial
  - pipeline
created: 2026-09-09
source:
  - specs/SPEC_WRITE_CONTRACT_2026-09-09.md
  - specs/HOSTILE_RCA_REVIEW_6FACE_2026-09-09.md
  - marginalia/insertions.py
---

# The three open questions

**Q1.** Is emphasis inside the containment check or outside it?
**Q2.** Who may override containment, and where is the reason recorded?
**Q3.** DL-89 — which of the two copies of the frame prose is authoritative?

## Measured before anybody argues

- **The proposed Q1 rule was run** against today's three boxing cases. Strip a whole-paragraph
  italic wrapper, then compare remaining emphasis exactly:

| case | before → after | result |
|---|---|---|
| ch5 third note, emphasis deliberately dropped | 4 markers → 0 | **fires** |
| ch7 casebook, pure boxing | 0 → 0 | passes |
| ch5 clause four, bold label kept | 2 → 2 | passes |

- **Q3, the two copies, by activity:** `marginalia/insertions.py` has **8 commits ever**;
  `manuscript/` has **49**. Six to one. The divergence is **67 lines** and `--apply` has not been
  run since it began.
- **`--verify` has three consumers:** `review.py` step 6, `shipcheck.py` category 6, and the
  review skill names it in its seven-step list.

---

## SHAMAN · the Body — *the emphasis case already happened and I reported it by hand*

Q1 is not hypothetical. **I dropped emphasis on two phrases today and told Wendell in prose.** That
is the exact event the check exists for, and the only reason it reached him is that I happened to
notice and happened to mention it. The next person will not.

So the Shaman's answer to Q1 is that emphasis is **meaning, not formatting**. *Not* and *not* are
different sentences. A check that treats them the same is measuring typography.

The proposed rule was run and it fires on the one case that should fire and stays silent on the two
that should not. **It earns its place on the only evidence available.**

**Votes:** Q1 emphasis inside containment, by the wrapper-stripping rule.

## CHALLENGER · the Line — *the override is where this control will die*

Q2 is the question that decides whether any of this survives contact. Every control in this repo
that got evaded was evaded at the moment of use: `quiet` became `careful` because rebuilding the
sentence cost more than substituting a word.

**An override with no friction is not a control. An override with real friction gets routed
around.** The only version that survives is one that is **cheap to write and expensive to hide**.

So: a required reason string, printed on every run, landing in the terminal and the commit. Not
approval-gated, because finding Wendell to place four boxes is how the check gets commented out at
eleven at night.

And the unwelcome addition: **the override must be scoped to a named file, never global.** A global
override turns the contract off for the whole run, which is precisely the shape of the failure it
was written to catch.

**Votes:** Q2 cheap, scoped, loud. Reason required, printed, never silent.

## REGENT · the Inheritance — *eight commits against forty-nine*

Q3 has been answered by six weeks of behaviour and nobody has read the answer out.

`insertions.py` has been touched **eight times**. The manuscript **forty-nine**. Every edit today
went to the manuscript. `--apply` has not run since the divergence began. **The source has never
once won a disagreement, and the one time it was consulted it destroyed approved prose.**

Its value was real and it was in the past: placing forty-seven frame blocks across nine chapters at
build time. That job is finished. What it holds now is a stale second copy of prose that lives
properly somewhere else.

**The Regent's answer: the manuscript is authoritative.** Not as a preference — as a description of
what has been true for six weeks.

**Votes:** Q3 manuscript authoritative. What happens to the source is a second question, and the
Regent will not retire a file in the same breath as ruling the hierarchy.

## ARCHITECT · the Design — *do not retire the file, invert the dependency*

The Regent is right about the hierarchy and wrong about the disposal, and the difference matters.

Three shapes are available:

| | shape | consequence |
|---|---|---|
| **a** | retire `insertions.py` | breaks `--verify`, which has three consumers including a shipcheck category. Removing a ship blocker to fix a divergence is a bad trade. |
| **b** | keep both, declare the manuscript authoritative, **regenerate `insertions.py` from it** | the source can never be stale, because it stops being a source. `--apply` becomes idempotent and safe. Nothing downstream breaks. |
| **c** | keep both, declare the source authoritative | requires running `--apply`, which reverts 67 lines of approved prose. Refused on sight. |

**b is the answer.** The file keeps its consumers and loses its authority. `--apply` stops being a
loaded weapon because there is nothing in the source that did not come from the manuscript.

On Q1 the Architect adds only that the rule must be **one function**, testable in isolation, and it
already is — it was run against three cases before this panel sat.

**Votes:** Q3 shape **b**. Q1 as proposed. Q2 with the reason as a required argument, so it cannot
be omitted by forgetting.

## DIPLOMAT · the Table — *count how often the override will be needed*

Before ruling Q2, ask how often the thing gets used. If containment fires on every ordinary edit,
the override becomes routine and stops meaning anything.

Today's evidence: **three boxing operations, and the proposed rule fires on one.** That one was a
real change I had to explain in prose anyway. That is a good rate. It suggests the override will be
rare, which is what makes a required-reason design workable.

The Diplomat's condition on Q3: **shape b must not add a step to ordinary editing.** If regenerating
the source becomes something a person has to remember after every manuscript edit, it will be
forgotten and the divergence returns wearing a new hat. It has to be automatic or it has to be part
of a check that already runs.

**Votes:** Q2 required reason, no approval gate. Q3 shape b, on the condition that regeneration is
not a remembered step.

## SAGE · the Board — *name what Q3 really is*

Q3 has been carried as an open question through three documents today and described each time as
*"Wendell's, because it decides which artefact is true."* **That framing is what kept it open.**

It is not a question about truth. It is a question about which file the work goes into, and the
work has been going into the manuscript six times more often than the source since June. **The
decision was made by everyone's behaviour and never written down**, which is the same shape as the
treatise promise: a claim on the page that the practice stopped honouring.

So the Sage's contribution is procedural. **Stop escalating decisions that behaviour has already
made.** Write them down, show the measurement, and let Wendell overrule the record if it is wrong.
Escalation looked like deference and functioned as delay, and the delay is what let the hazard sit
long enough to fire.

**Votes:** Q3 ruled on the measurement, subject to Wendell's overrule. Q1 and Q2 as above.

---

## Consensus, six of six

**Q1 · Emphasis is inside containment, by the wrapper-stripping rule.** Strip a whole-paragraph
italic wrapper and any leading bold label, then compare remaining emphasis exactly. It fires on the
one case today that should have fired and stays silent on the two that should not, which is the only
evidence available and it was run before the panel sat. Emphasis is meaning; *not* and *not* are
different sentences.

**Q2 · The override is cheap to write, scoped to one named file, and impossible to hide.** A
required reason string, printed on every run so it reaches the terminal and the commit. **No
approval gate**, because a control that needs a person found is a control that gets commented out.
**No global form**, because turning the contract off for a whole run is the shape of the failure it
exists to catch. Today's rate suggests overrides will be rare, which is what makes the design hold.

**Q3 · The manuscript is authoritative, and `insertions.py` is regenerated from it rather than
retired.** Eight commits against forty-nine. The source has never won a disagreement and destroyed
approved prose the one time it was consulted. Retiring it would break `--verify`'s three consumers
including a shipcheck category, so it keeps its consumers and loses its authority. `--apply` becomes
idempotent because nothing in the source will not have come from the manuscript.

**One condition attached, from the Diplomat:** regeneration must not be a step a person has to
remember after editing. Automatic, or folded into a check that already runs, or the divergence
returns under a new name.

**One procedural finding, from the Sage, that outlives this spec.** Q3 was escalated through three
documents as a question about truth. It was a question about where the work goes, and behaviour had
answered it in June. **Escalation looked like deference and functioned as delay.** Where a
measurement already shows the answer, write it down and let Wendell overrule the record.

## What the panel refuses

It does not retire `insertions.py`, which would remove a ship blocker to fix a divergence. It does
not gate the override behind approval. It does not treat emphasis as typography. And it does not
carry Q3 to a fourth document.
