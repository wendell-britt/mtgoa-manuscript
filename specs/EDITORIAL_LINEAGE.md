---
type: lineage
title: "Editorial lineage — which mechanism is upstream of which"
aliases:
  - editorial lineage
  - base core voice kit
  - which review system
tags:
  - mtgoa
  - editorial
  - pipeline
  - integration
created: 2026-09-12
source:
  - specs/HOSTILE_REVIEW_INTEGRATION_PLAN_6FACE_2026-09-11.md (the Sage's ruling)
  - specs/INTEGRATION_PLAN_2026-09-11.md (Phase ½)
  - publishing-base/README.md and editorial/REVIEW_GATE.md on branch publishing-base-v0.1 (PR #20)
  - editorial.yaml, instruments/core_meta.py, editorial_reports/TOOLKIT_INSTALL_ZERO_TARGET_2026-09-11.md
  - export/voice-kit/README.md
status: written 2026-09-12 on Wendell's word. The inheritance order is an assumption until he rules base-and-core one thing or two.
---

# Editorial lineage

**Why this page exists.** Three mechanisms for portable editorial review were made in three months
by three sessions, none reading the last. The voice kit does not know the base exists; the base
does not know the core exists; the core's reports cite neither. On 2026-09-11 an integration plan
added a fourth document and recommended closing the second. The hostile review of that plan ruled:
*one page, in this repo, naming the three mechanisms, their dates, what each owns, and the order
they inherit in — before anything else moves.* This is that page. It is not dated in its filename
because it is meant to be corrected in place, and every correction is a log row.

## The three mechanisms

| | made | where it is | shape | owns | consumers |
|---|---|---|---|---|---|
| **Publishing Base v0.1** | 2026-08-15 | branch `publishing-base-v0.1`, **PR #20, open**, unmerged | a contract: ten editorial principles, a repo layout, the review-gate *sequence* (steps 0–7, four outcomes), an `AGENTS` template | what every Wendell Britt book repo must guarantee; *"each book supplies its own rules, vocabulary, thresholds, and voice references"* | **Emotional First Aid**, branch `setup/publishing-base-v0.1` (2026-08-18): `AGENTS.md`, `editorial/REVIEW_GATE.md`, `editorial/EFA_RULES.md`, seven drafts of a first chapter, eight reviews, three specs. No `manuscript/`, no `instruments/` yet. |
| **editorial-core v32** | ruled an object 2026-09-09; installed 2026-09-11 (PR #24) | `../editorial-core` in The Library, **one disk, no repository in the account carries it** | instruments by copy, `sync_core.py`, one manifest per project (`editorial.yaml`), one ledger per project (`editorial_exceptions.yaml`) | the measurements: gate, telling, trailing_and, light_verb, fragment, polysyndeton, slop_shapes, prose_diet, antecedent, and `coherence.py`'s board over them. 24 core modules in MTGOA's `instruments/`; the project's own files (`build_book.py`, `review.py`, `claims.py`, `markpatterns.py`) are not core. | MTGOA at v32. The install report names two other Library books; they are not on GitHub under any visible name and nothing here can verify them. |
| **voice kit** | 2026-08-10 | `export/voice-kit/` on `master` | `voice_lint.py` (stdlib only) plus two skills, `no-ai-slop` (MIT, Peter Yang, verbatim, licence travels with it) and `house-voice` | the counters from `gate.py`, `prose_diet.py` and `empty_head.py`, *copied verbatim so the site and the book cannot drift*, for repos with customer-facing copy and no manuscript | `johnair01/bars-engine` (its stated target); **friendcraft**, where `tools/voice_lint.py` reached `main` on 2026-09-09 (#17). |

## The order they inherit in

This is the page's ruling, and it is an **assumption** until the decision below is taken:

1. **The base is the contract.** Everything downstream implements it or explicitly declines a
   clause. Its inheritance rule is the house rule: *books inherit the Publishing Base principles,
   not another book's local rules.* MTGOA's banned-word list, Calrunia frames, chapter forms and
   production syntax do not travel unless a book adopts them by name.
2. **The core is the base's Phase 3, built without citing it.** The base's task list says *identify
   which MTGOA checks are truly generic; port generic checks behind book-local configuration* —
   both unchecked. `editorial.yaml` is that book-local configuration and `sync_core.py` is that
   port. Against the base's review gate, the core implements **step 2** (hard local gate: `gate.py`
   over the manifest's `banned:`), **step 3** (prose-drift diagnostics: the counters), **step 5**
   (repair check: rerun the board) and the manuscript-wide checks of **step 7** (`coherence.py`,
   `shipcheck.py`). It assists step 4 (`slop_shapes` finds the discrete shapes; the reading is
   still a reading). Steps 0, 1, 4 and 6 are a person. *Earlier documents said "steps 3–6"; that
   was imprecise and this page corrects it.*
3. **The voice kit is the stdlib export of the core's step 2 and 3 counters** for repos that will
   never carry a manuscript or the core, with the step 4 skill alongside. Its own README states
   the dependency: *when the book's counters change, re-copy them rather than re-deriving them.*
   It is downstream of the core, not a sibling of it.

Written as one line: **base → core → voice kit.** A book gets the base; a book with a manuscript
gets the core installed into it; a repo with only copy gets the kit.

## What is measured, not remembered

- **The base's own condition for a shared repo is not yet met on GitHub.** *"Once two books
  implement the same interfaces, the genuinely shared code can be moved into a dedicated
  publishing repo."* MTGOA runs v32. EFA has the base's `editorial/` directory and no instruments.
  The two Library books the reports name cannot be seen from any clone.
- **Three fragment counters, and nothing tests that they agree.** The core's `fragment.py` (NLTK);
  the kit's `voice_lint.py`, where PR #23 closed the `-s` hole on 2026-09-11 with a hand list,
  `VERB_S`; and friendcraft's copy of the kit, which predates PR #23 and has no `VERB_S`. Plain
  `diff` between friendcraft's copy and the kit on `master` today: 73 lines.
- **`check_core` compares two of three numbers and says `ok clean`.** When `core_home` is
  unreachable — every clone but one — the third comparison is skipped without saying so.
- **The instruments cannot yet be pointed at another book.** Every instrument resolves its root,
  manifest and ledger from its own file location, and an empty corpus glob falls through to this
  book. A sibling can only be measured from inside its own tree.

## What this page decides, and what it leaves to Wendell

**Decided by this page**

- PR #20 is not closed. It is upstream. It is rebased or merged when its base is refreshed.
- PR #20's `tasks.md` should show Phase 1's three unchecked boxes done (the template, the gate and
  the README exist on the branch), Phase 2 unblocked (the EFA repository exists since 2026-08-16),
  and Phase 3's first two boxes **done by editorial-core, 2026-09-11, on another branch.** That
  edit lands on PR #20's branch, which this session does not push to without the word.
- EFA is first among the siblings, not last. What it needs is the core installed as the base's
  Phase 3, into a repo that already has an `editorial/` directory, without overwriting it.
- No sibling is synced from outside its own tree until every instrument takes `--root` and an
  empty corpus is a hard error.

**Left to Wendell**

1. **Are the base and the core one thing or two?** This page assumes one: the base is the
   contract, the core is its instruments. If two, this page says which wins and the rest of it is
   rewritten.
2. **Is the voice kit built from the core, or a separate stdlib lineage?** Its README says
   re-copied from the core. The drift says separate. The counters have already forked once.
3. **Where do Flirtcraft and AI Psychologist live?** The reports name them as running v32. No
   repository in the account carries either name, and friendcraft's `flirtcraft/` is five YAML
   files of game data.

## Corrections log

| date | correction |
|---|---|
| 2026-09-12 | Page written. "Steps 3–6" in the plan and the review corrected to steps 2, 3, 5 and 7 against the gate's actual text. The review's "installed in friendcraft 09-01" is not reproducible from the clone as it stands; the kit reached friendcraft's `main` on 2026-09-09 (#17). |
