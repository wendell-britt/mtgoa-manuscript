---
type: panel
title: "Six-Face panel — the three open questions in the claims registry spec"
aliases:
  - claims registry open questions
  - carrier failure gating
  - claim id namespace
tags:
  - mtgoa
  - editorial
  - pipeline
created: 2026-09-09
source:
  - specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md
  - specs/PANEL_CENSUS_GAP_6FACE_2026-09-09.md
  - instruments/shipcheck.py
  - instruments/rescan.py
  - specs/DECISION_LOG.md
---

# The three open questions

**Q1.** Does a carrier failure block the press, or only the board?
**Q2.** What namespace do claim ids live in? The spec proposed `CLM-nn` because `C1` collides.
**Q3.** Who may add an entry?

## What is already on the board

- **`shipcheck.py`:** *"A blocker is something that makes the artefact wrong or incomplete in a
  reader's hands. Everything else is quality, and quality does not stop a press."* Its six
  categories share one property nobody has stated: **every one of them is unambiguous.** A live
  placeholder token is wrong. A broken round-trip is wrong. There is no reading under which the
  finding is fine.
- **`rescan.py` rank 0:** *"1 CLAIM ERROR — a stated fact is wrong"*, with the comment *"both the
  cheapest to fix and the most expensive to ship, so it leads."* **The vocabulary this spec needs
  already exists in the repo**, and it already ranks first.
- **`DECISION_LOG.md`:** ids run to **DL-77**. The C1 ruling has no id at all, because it was made
  in a panel file rather than the log.

---

## SHAMAN · the Body — *what a red board feels like on the fourth false alarm*

Ask what happens in the body of the person who sees the failure. A carrier failure will most often
mean somebody improved a sentence and did not update an entry. That is filing, and filing that
stops a press produces one feeling, which is resentment, and one behaviour, which is muting.

**The muting is the danger and it is silent.** Nothing in this repo would record that a check got
worked around; the `quiet` → `careful` substitution is on file precisely because the evasion left
no trace. A control that fires ambiguously at maximum stakes trains the person to make it stop
rather than to read it.

**So the Shaman's requirement is about the signal's honesty.** A carrier failure does not mean *a
ruling is broken*. It means *a span this book decided something about has moved*. Those are
different sentences and only the second one is true. Design the response to the true sentence.

On Q3: the census gets done in the moment of noticing, and if there is nowhere to put an
observation that has not been ruled yet, it is lost. **There must be a place for an unruled
carrier list.**

**Votes:** board, not press. Open entry with a candidate tier.

## CHALLENGER · the Line — *who pays for my filing*

The unwelcome sentence about Q1: **most carrier failures will be my bookkeeping, not your
contradiction.** Putting that in front of the press means Wendell pays, in stopped work, for the
registry being out of date. That is a cost transfer dressed as rigour, and it is the exact shape
of control this book already rejected once.

The unwelcome sentence about Q2 is aimed at the spec I wrote: **`CLM-nn` is the second dead
document arriving in a new coat.** The census gap panel said do not write a register that nothing
reads, and the answer to a collision is not a new namespace. `C1` collides because it was borrowed
from a per-chapter error slot in the working list. That is an argument against `C1`, not an
argument for inventing a parallel numbering scheme that will need a mapping table by Christmas.

On Q3: **gating entries to Wendell makes the registry thin, and a thin registry is worse than no
registry**, because it implies a coverage it does not have. A reader of `claims.yaml` with six
entries will assume the other rulings were checked and found clean.

**Votes:** board, not press. Kill `CLM`. Open entry.

## REGENT · the Inheritance — *the log is the thing to inherit*

Q2 is the Regent's question and it has one answer. **A claim is a decision.** The book already has
a decision log with sixty-plus ruled entries, a Location column, and ids up to DL-77. The right
move is not to build a register beside it. It is to make `claims.yaml` **the machine-readable half
of the decision log**, keyed by the same ids.

Three things fall out at once, and this is the strongest argument in the session:

1. The collision evaporates. Nothing is ever called `C1` again; the Controller ruling becomes
   **DL-78**, the next number in the only sequence this book has.
2. **The inert document becomes load-bearing.** The census gap panel's finding was that sixty
   rulings sit unread. Keying the live check to their ids is the one change that makes reading them
   compulsory, and it repairs the original defect rather than routing around it.
3. There is one place to look, forever. A person asking *what did we decide about the Controller*
   has one index, not two with a join between them.

On Q3, the Regent's field is `ruled_by`. **A ruling without a name attached does not survive its
author**, and provenance is the whole difference between a decision and an opinion that got
applied.

**Votes:** DL-nn, one namespace. Open entry with `ruled_by` required.

## ARCHITECT · the Design — *stop tuning one check and build two*

Q1 has been framed as a threshold question — how bad does a carrier failure have to be — and
threshold questions are what you get when one signal is carrying two meanings. **Split the signal.**

| what is true | ambiguous? | where it belongs |
|---|---|---|
| a carrier span has moved | **yes** — broken ruling, or improved sentence with a stale entry | fails `review.py` and `coherence.py` |
| a claim's status reads `1 of 4` | **no** — the work was started and not finished | **`shipcheck.py`, a blocker** |

The second row is the answer to Q1 and it satisfies both sides. An incomplete application is
*incomplete in a reader's hands*, which is shipcheck's own test, word for word. It cannot be a
false alarm, because the count is a fact about the registry rather than a guess about the prose.
And `rescan.py` already ranks a claim error first, *"the most expensive to ship"*, so the press
category is not a new judgement. It is an existing one finally wired to something.

On Q2: one namespace, because **a mapping table between two id spaces is a thing that rots and
nobody notices.** On Q3: candidate versus claim is a **field**, not a process. Anything that has
to be remembered by a person will not be.

**Votes:** split the check. DL-nn. Open entry, distinguished by a field.

## DIPLOMAT · the Table — *the check nobody can afford to obey*

Everything here is paid for mid-edit, by somebody in the middle of something else.

Q1, at press stakes, is the maximum version of the failure already on file. A banned word made a
sentence expensive to fix, so the sentence got a synonym instead of a rebuild and the gate went
green on prose that meant nothing. **Raise the stakes on an ambiguous signal and you do not get
more care, you get more evasion.** The evasion at press stakes would be deleting the entry, and a
deleted entry looks exactly like a claim that was never made.

Q3 is the same argument earlier in the pipeline. If adding an entry requires finding Wendell, the
entry does not get added, the census dies with it, and the registry documents whichever weeks he
happened to be available. **Open it, and make the provenance field carry the authority instead of
the process.**

The Diplomat's one addition: **the fix for a carrier failure must be one line.** Update the phrase
in the entry, or restore it in the prose. If resolving a failure means reopening a ruling, the
check will be resolved by deletion.

**Votes:** board, not press. Open entry. One-line resolution as a design constraint.

## SAGE · the Board — *name the game in Q1*

The game being played in Q1 is **make the check important so that it gets respected.** It is a
common move and it fails the same way every time. Importance is not respect. Precision is. A check
that stops a press for a stale phrase teaches everyone that the check is unreliable, and then the
one time it is right, it is ignored.

The second game is in Q2, and this panel nearly played it. **A new register feels like progress in
a way that reading the old one does not.** The census gap panel found sixty unread rulings and the
spec's response was to propose a sixty-first artefact with its own numbering. The Regent's answer
inverts that, and inverting it is the difference between building a system and accumulating one.

The Sage's addition, which no other Face has raised: **the registry must be able to say what it
does not cover.** Six entries in `claims.yaml` must never read as *these are the book's claims*.
It must read as *these six are guarded, and the other seventy-one rulings are not.* That is the
boundary line from item F, applied to the registry's own board.

**Votes:** board, not press, with the status blocker as the Architect frames it. DL-nn. Open
entry. Add coverage to the registry's own output.

---

## Consensus, six of six

**Q1 — split the signal, and only the unambiguous half reaches the press.**

- **Carrier drift** (a registered span no longer appears verbatim, or appears twice) **fails
  `review.py` and `coherence.py`.** It is ambiguous between a broken ruling and an improved
  sentence, and an ambiguous signal may not hold a press.
- **Incomplete application** (a claim whose status reads `N of M` with `N < M`) **is a
  `shipcheck.py` blocker.** It is unambiguous, it is *incomplete in a reader's hands* by
  shipcheck's own definition, and `rescan.py` already ranks a claim error first as the most
  expensive thing to ship.
- **Resolution must cost one line**: restore the span, or update the phrase in the entry.

**Q2 — one namespace, and it is the decision log's.** `claims.yaml` is the machine-readable half of
`DECISION_LOG.md`, keyed by `DL-nn`. `CLM-nn` is withdrawn. The Controller ruling becomes
**DL-78**, written into the log with its Location column populated and its status as a count.
**This is the ruling that makes the inert document load-bearing**, which was the census gap panel's
actual finding.

**Q3 — open, with provenance, in two tiers.**

- A **candidate** is a carrier list with no `ruled_by`. Anyone may add one; a census is a
  measurement, not an authority. `claims.py` reports candidates and does not fail on them.
- A **claim** has `ruled_by` naming Wendell's ruling or the standing panel instruction that
  authorized it. `claims.py` fails on these.
- A candidate is therefore a worklist entry rather than a lost observation, which is the tier the
  Shaman asked for.

**One addition all six accepted.** The registry's own output must state its coverage: *N claims
guarded, M decision-log rulings unregistered.* A short registry must never read as a complete one.

## What changes in the spec

| spec item | change |
|---|---|
| §4 FR-C1 | `id` is a `DL-nn` id; `CLM-nn` withdrawn |
| §4 FR-C5 | carrier drift fails `review.py` and `coherence.py`; press explicitly excluded |
| §4 new FR-C9 | an entry without `ruled_by` is a candidate: reported, never failed |
| §4 new FR-C10 | a claim whose status is `N of M`, `N < M`, is a `shipcheck.py` blocker |
| §4 new FR-C11 | `claims.py` output states coverage against `DECISION_LOG`'s ruling count |
| §4 FR-B1 | strengthened: the registry is keyed by the log, not merely styled after it |
| §8 | Q1, Q2, Q3 resolved; this panel is the record |

## What the panel refuses

It does not make carrier drift a press blocker. It does not create a second id space. It does not
gate entry behind Wendell, which would make the registry a record of his availability. And it does
not let a six-entry registry print a board that reads like coverage.
