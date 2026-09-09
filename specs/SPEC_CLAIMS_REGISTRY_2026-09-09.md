---
type: spec
title: "The claims registry — a ruled fact, every sentence that carries it, and a run that fails when one moves"
aliases:
  - claims registry
  - census gap
  - carrier check
  - what the board does not check
tags:
  - editorial
  - mtgoa
  - process
  - pipeline
created: 2026-09-09
review: 2026-09-23
source:
  - specs/PANEL_CENSUS_GAP_6FACE_2026-09-09.md
  - specs/PANEL_CLAIMS_REGISTRY_OPEN_Q_6FACE_2026-09-09.md
  - specs/EDITORIAL_PIPELINE_COHERENCE_2026-09-03.md
  - specs/DECISION_LOG.md
  - instruments/coherence.py
  - instruments/agency_registry.yaml
status: specified, not built; all three open questions ruled by panel 2026-09-09
---

# The claims registry

**Wendell, 2026-09-09:** *"I don't know what all pass means and I've learned enough not to trust
whatever that is. No confidence that the editorial system I built was used."* Then: *"And what
needs to have been there to avoid this?"*

**The gap in one line.** This book re-verifies its **style** claims on every run and writes its
**content** rulings into a document nothing reads.

`coherence.py` re-measures all three declared baselines against the live corpus every run and
fails on drift beyond tolerance. `DECISION_LOG.md` holds sixty ruled entries, has a **Location**
column, and has no consumer anywhere in the repo. A ruling nothing re-checks is indistinguishable
from a lie the moment the prose moves under it.

---

## 1 · What went wrong, precisely

A panel ruled a content fact: the shadow Controller bites at Open Up, not before Stage One. The
ruling was applied to the one sentence that **stated** the fact. Three further sentences in the
same paragraph **assumed** it, in metaphor:

| carrier | shares a word with "before Stage One"? |
|---|---|
| "a feeling being allowed onto the field" | no |
| "a charge that got called out of bounds at the whistle" | no |
| "every stage assumes the feeling made it into play" | no |
| "end the whole practice before Stage One" | yes — the only one a search finds |

One of four was edited. The paragraph then argued against itself and shipped under a green board.

**Two distinct failures, and only one of them is about editing.**

- **The census failure.** The ruling was never written as a fact plus the sites that depend on it,
  so applying it to one site looked identical to applying it to all of them.
- **The reporting failure.** The board named the checks that ran and said nothing about the
  classes of defect no instrument covers, so "all pass" carried an implication nothing had earned.

## 2 · Why a search cannot be the census

A claim carried in metaphor has **no searchable surface**. Three of the four carriers above share
no vocabulary with the claim they carry. This is the load-bearing constraint on the whole design:

> **The census is a read. The registry makes the read durable. Nothing in this spec discovers a
> carrier; every mechanism here protects carriers a person has already found.**

Any requirement below that appears to promise discovery is out of scope, and §7 says so in as
many words.

## 3 · Scenarios

**S1 · A ruling is made.** A content fact is decided. Before any edit, the paragraphs that state
or assume the old fact are read and listed. The ruling is recorded as one registry entry: the
fact, why it was easy to miss, and the exact spans that carry it. The applying script declares
the claim and the carrier count and refuses to run if the two disagree.

**S2 · Somebody edits a carrier six months later.** A copyedit touches one of the four spans. The
next run goes red and names the claim, the fact, and the span. The editor either restores the
span, or updates the entry because the wording legitimately changed. Either way they have been
shown what the sentence was load-bearing for.

**S3 · A reader of the board.** Any board — draft or book-wide — ends with a line naming what
nothing in the pass checked. "All pass" is no longer available as a summary, because the board
states its own boundary.

**S4 · A ruling is applied to one of four carriers.** The script refuses to write. Nothing lands.

## 4 · Requirements

Each is testable. `MUST` is a build requirement; `MUST NOT` is a refusal the panel already ruled.

### F · The boundary line — *ships first, costs one function*

- **FR-F1** Every board `review.py` prints, on both the draft and book-wide paths, MUST end with a
  line naming the classes of defect nothing in the pass checks.
- **FR-F2** That text MUST come from one declaration in `review.py`, not be written per board, so
  a future instrument cannot silently shrink it.
- **FR-F3** The boundary MUST name at least: whether every sentence in a paragraph is committed to
  the same claim; whether a ruled fact is carried anywhere else; whether the sentence is true;
  whether this is the right paragraph at all.
- **FR-F4** The line MUST print on a clean run. A boundary that appears only on failure teaches
  nothing.

*Precedent: `review.py` step 8 already does this once, for the slop pass. This generalizes it.*

### C · The registry — *the substrate*

- **FR-C1** `instruments/claims.yaml` holds one entry per ruled content fact, with: `id`, `fact`
  (one sentence), `wrong_because` (the symptom — why the carriers were easy to miss),
  `carriers` (a list of `{file, phrase}`), `status` (`N of M`), `ruled` (date), `ruled_by`.
- **FR-C1a** `id` MUST be a `DL-nn` id from `DECISION_LOG.md`. There is no second id space.
  `claims.yaml` is the machine-readable half of the decision log, and keying the live check to the
  log's ids is what makes sixty unread rulings load-bearing. The Controller ruling enters as
  **DL-78**. *(Panel 2026-09-09, Q2. Supersedes the withdrawn `CLM-nn` proposal.)*
- **FR-C2** Carriers MUST be verbatim quoted spans. Line numbers MUST NOT appear in a carrier;
  they rot on the next insertion and a false failure is how a check gets switched off.
- **FR-C3** A carrier SHOULD be the shortest distinctive span that carries the claim, not the whole
  sentence, so that routine copyediting does not trip it.
- **FR-C4** `instruments/claims.py` MUST verify that every carrier phrase occurs **exactly once**
  in its named file.
- **FR-C5** A missing or duplicated carrier MUST fail the run with a nonzero exit, naming the
  claim id, the fact, the file, and the phrase. It MUST fail `review.py` and `coherence.py` and
  MUST NOT stop the press. Carrier drift is ambiguous between a broken ruling and an improved
  sentence with a stale entry, and an ambiguous signal that holds a press gets muted rather than
  read. *(Panel 2026-09-09, Q1.)*
- **FR-C5a** Resolving a carrier failure MUST cost one line: restore the span in the prose, or
  update the phrase in the entry. If resolution requires reopening a ruling, the check will be
  resolved by deletion.
- **FR-C9** An entry with no `ruled_by` is a **candidate**: a carrier census nobody has ruled yet.
  `claims.py` MUST report candidates and MUST NOT fail on them. Anyone may add one, because a
  census is a measurement rather than an authority. An entry with `ruled_by` is a **claim**, and
  claims fail. *(Panel 2026-09-09, Q3.)*
- **FR-C10** A claim whose `status` reads `N of M` with `N < M` MUST be a `shipcheck.py` blocker.
  Unlike carrier drift this is unambiguous — the work was started and not finished — and it meets
  shipcheck's own test of *incomplete in a reader's hands*. `rescan.py` already ranks a claim error
  first, as *"the most expensive to ship."*
- **FR-C11** `claims.py` output MUST state its coverage: how many rulings are guarded, and how many
  `DECISION_LOG` entries have no registry entry. A six-entry registry MUST NOT print a board that
  reads like coverage of the book.
- **FR-C6** `claims.py` MUST be wired into `review.py`'s book-wide pass as a numbered step.
- **FR-C7** `coherence.py` MUST gain a check that validates the registry's own shape: every entry
  has at least one carrier, every named file exists, every `status` count equals the number of
  carriers listed, and no two entries share an id.
- **FR-C8** The registry MUST NOT be a reporting-only instrument. The panel's ruling: a document
  that does not fail a run decays into a claim about the past, and `DECISION_LOG` is the proof.

### E · The declaration in ruling scripts — *the forcing function*

- **FR-E1** A script that applies a content ruling MUST declare `CLAIM` and `CARRIERS`.
- **FR-E2** It MUST refuse to run when `CLAIM` has no entry in the registry.
- **FR-E3** It MUST refuse to run when its number of edits does not equal `CARRIERS`.
- **FR-E4** The declaration MUST cost two lines and one import. A control that is expensive at the
  moment of use gets satisfied rather than obeyed, and this book has the `quiet` → `careful`
  substitution on file as the proof.
- **FR-E5** Refusal MUST be atomic: nothing is written, matching the existing tranche-script
  contract.

### D · The diff alarm — *deferred until C exists*

- **FR-D1** Given a working-tree diff, flag any hunk that changes some sentences of a paragraph
  and leaves its neighbours untouched.
- **FR-D2** When the paragraph contains a registered carrier, the finding MUST name the claim and
  its carrier count. *"This paragraph carries DL-78, four carriers, you changed one"* is a
  finding; *"look at the neighbours"* is noise.

### B · Inheritance — *on contact only*

- **FR-B1** `claims.yaml` MUST be **keyed by** `DECISION_LOG`'s ids, not merely styled after its
  fields. The two are one system with a prose half and a machine half. *(Strengthened by the panel
  2026-09-09; the original wording asked only for shared vocabulary.)*
- **FR-B2** Existing decision-log entries MUST NOT be retrofitted on a sweep. An entry earns a
  claims entry when the prose it rules is next touched.

## 5 · Acceptance

Concrete, in order. Each is a command and an expected result.

| # | test | expected |
|---|---|---|
| **A1** | `python3 instruments/review.py <file>` | board ends with the boundary line |
| **A2** | `python3 instruments/review.py` | same boundary line, book-wide path |
| **A3** | `python3 instruments/claims.py` with the registry as shipped | exit 0, every carrier found once |
| **A4** | edit one carrier span in `manuscript/ch3.md`, re-run | exit nonzero, names DL-78, the fact, the file, the phrase |
| **A5** | restore the span, re-run | exit 0 |
| **A6** | duplicate a carrier span elsewhere in the same file | exit nonzero, reports the phrase as ambiguous |
| **A7** | `python3 instruments/coherence.py` with a registry entry whose file does not exist | that check fails and names the entry |
| **A8** | a ruling script declaring `CARRIERS = 4` with one edit | refuses, writes nothing, exit nonzero |
| **A9** | `python3 instruments/review.py` book-wide | the claims step appears on the board as its own row |

**The seeding test, which is the one that matters.** DL-78 is entered with the four carriers from
§1, in their current corrected wording. A5 and A4 together demonstrate the guard that was missing
when the defect was made.

## 6 · What this would have caught, and what it would not

**Would not have caught the original defect.** At the moment of that edit DL-78 did not exist, so
nothing would have fired. Stated plainly because the opposite is the tempting claim: this is not a
detector, it is a ratchet. Its value begins at the first ruling made under it.

**Would catch every later edit to those carriers**, which is the recurrence this book actually
faces: nine chapters, sixty rulings, and prose that keeps moving under decisions taken months ago.

**Would have caught the application error**, via E. Four carriers on file and one edit in the
script is a refusal, and the census becomes a build requirement rather than a discipline.

## 7 · Out of scope — refusals, not omissions

- **An instrument that reads a paragraph as an argument.** Nothing here can do that. Pretending
  otherwise is how the green board acquired authority it never earned.
- **A gate exemption for this file.** `gate.py` flags one banned token in §4, where FR-E4 names the
  `quiet` → `careful` substitution as evidence. That is a mention rather than a use, specs are not
  in the shipping corpus, and no exemption is requested. Recorded so the hit is not read as an
  oversight.
- **Semantic contradiction detection.** Not attempted. The carriers are found by a person.
- **Retrofitting sixty decision-log entries.** Ruled against: sixty entries buys sixty liabilities
  and looks like progress for about a week.
- **A required form on the edit path.** Two lines and one import, or the control gets routed
  around.
- **Replacing the logical read.** The board may tell you the read is worth doing. It may not close
  the item.

## 8 · Open questions — all three resolved by panel, 2026-09-09

- **Q1 · Does a carrier failure block the press, or only the board? RESOLVED by splitting the
  signal.** Carrier drift is ambiguous, so it fails `review.py` and `coherence.py` only (FR-C5). An
  incomplete application — a status of `N of M` with `N < M` — is unambiguous and is a shipcheck
  blocker (FR-C10). The question was a threshold argument because one signal was carrying two
  meanings.
- **Q2 · Claim ids. RESOLVED.** `C1` collides with the working list's per-chapter error class,
  and the spec's first answer — a new `CLM-nn` space — was withdrawn by the panel as a second
  register arriving in a new coat. **One namespace: `DL-nn`.** See FR-C1a.
- **Q3 · Who may add an entry? RESOLVED: open, in two tiers.** A carrier census with no
  `ruled_by` is a **candidate** and is reported, never failed. An entry with `ruled_by` is a
  **claim** and fails the run. Gating entry would make the registry a record of Wendell's
  availability, and a thin registry implies a coverage it does not have. See FR-C9.

## 9 · Build order and status

| | item | state |
|---|---|---|
| 1 | **F** — boundary line in `review.py` | specified |
| 2 | **C** — `claims.yaml` + `claims.py`, wired into `review.py` and `coherence.py`, seeded with DL-78 | specified |
| 3 | **E** — `CLAIM` / `CARRIERS` declaration and the shared refusal helper | specified |
| 3b | **DL-78** written into `DECISION_LOG.md` with its Location column and a counted status | specified |
| 3c | **shipcheck** category for an incomplete application (FR-C10) | specified |
| 4 | **D** — diff alarm, naming the claim | specified, deferred until C ships |
| 5 | **B** — retrofit on contact | standing rule, no work item |

## The standing rule

**A ruling that does not name its carriers has not been applied; it has been started.** The count
is what makes a partial application visible, and *applied* is not a status. *4 of 4* is.
