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
| **editorial-core v34** | ruled an object 2026-09-09; installed in MTGOA 2026-09-11 (PR #24); synced to v33 2026-09-11 evening (`density.py`, `fragment.py`); synced to v34 2026-09-22 (DL-109, version-only) | `../editorial-core` in The Library, **one disk, no repository in the account carries it** | instruments by copy, `sync_core.py`, one manifest per project (`editorial.yaml`), one ledger per project (`editorial_exceptions.yaml`) | the measurements: gate, telling, trailing_and, light_verb, fragment, polysyndeton, slop_shapes, prose_diet, antecedent, and `coherence.py`'s board over them. 24 core modules in MTGOA's `instruments/`; the project's own files (`build_book.py`, `review.py`, `claims.py`, `markpatterns.py`) are not core. | **MTGOA**, board fully drawn to zero 2026-09-14. **`wendell-britt/wendell-britt-fear-to-joy-manuscript`, confirmed 2026-09-22**, also at v34. |
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

- **The base's own condition for a shared repo is now met, once.** *"Once two books implement the
  same interfaces, the genuinely shared code can be moved into a dedicated publishing repo."*
  MTGOA and `wendell-britt-fear-to-joy-manuscript` both run core v34, confirmed 2026-09-22 (DL-109)
  — two real books on the shared instruments. EFA has the base's `editorial/` directory and no
  instruments: two books on the core, a third on the base, none yet on both.
- **The v33 → v34 release changed nothing but its own number.** Every one of the 27 shared core
  files compared byte-identical between MTGOA and Fear to Joy except `core_meta.py`'s version line
  — confirmed before syncing, not assumed. Either v34 is a capability release with no code yet (the
  release-severity doc in `core_meta.py` names this shape: *"adds capability, reports and waits"*)
  or Fear to Joy's own instruments are themselves stale against whatever v34 actually is. This page
  cannot tell which from two projects that agree with each other; it can only report that a sync
  that changes only a number is not evidence the number means nothing.
- **The zero-target debt PR #25 shipped as red is now clean.** The 335 unresolved hits it merged
  onto `master` (telling 198, light_verb 52, slop_shapes 40, fragment 38, polysyndeton 7) were
  drawn to zero across five commits, 2026-09-11 through 2026-09-14, and the twelve exceptions
  ledgered on Wendell's behalf during that drawdown were ratified by him on 2026-09-14. `coherence`
  passes clean on `master` today, `zero` included. This did not touch the base/core/kit
  relationship above — it is a prose and ledger drawdown, not a lineage change.
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

**Recommended by the six-Face panel of 2026-09-22** (`specs/PANEL_LINEAGE_OPEN_QUESTIONS_2026-09-22.md`)
— **recommendations, not rulings.** They do not overrule the "assumes one" line above; they replace
the assumption with a measured recommendation Wendell can ratify or reject.

1. **Two things, not one.** The base governs whether a change may become canon; the core measures
   whether a change is any good. A book can have the base without the core — EFA does, today — but
   the panel holds the reverse should not happen silently. Recommends: the base's contract names the
   core by version for any book that has a manuscript, without requiring a core-less book to install
   one. *(If Wendell rules one thing instead, the "order they inherit in" section above is rewritten
   and Phase 3's `--root`/empty-corpus conditions become load-bearing for the base itself, not only
   for a sibling sync.)*
2. **The kit was never a copy.** Its `EMPTY_HEAD`, `fragments()`, and related counters share no code
   with the core's `gate.py`/`prose_diet.py`/`fragment.py` — independent re-implementations that
   happen to agree on shape, not the "copied verbatim" the README claims. The v33 sync (`density.py`,
   `fragment.py`) never touched the kit. Recommends: either make the claim true (a mechanical
   re-derive step run at every core release) or rewrite the README to promise agreement in shape,
   not in code.

**Resolved 2026-09-22 — Wendell:** *"fear-to-joy-manuscript is the missing sibling."*

3. **Where do Flirtcraft and AI Psychologist live?** Neither is the sibling the toolkit-install
   report meant. `wendell-britt/flirtcraft` is a real repo (private, pushed 2026-09-16) — a Next.js
   product app, no `instruments/`, not a manuscript project. `friendcraft-manuacript`'s `flirtcraft/`
   is five YAML files of game data. No repository anywhere is named *AI Psychologist*. **The report's
   claim was aimed at the wrong pair of names; the project it meant is real.** `wendell-britt/wendell-
   britt-fear-to-joy-manuscript`, cloned and checked 2026-09-22: `editorial.yaml` (`core_version: 34`
   — at the time, one release ahead of MTGOA's 33 — `core_home: "../editorial-core"`),
   `editorial_exceptions.yaml` (its own ledger, all scanners empty — a clean book, not yet drawn
   down), `instruments/` (29 files, the lean core set with none of MTGOA's ~170 book-specific
   one-offs), `marginalia/compile.py` byte-identical to MTGOA's. `manuscript/the-skeptic.md`, 731
   words, one chapter. **No `AGENTS.md`, no `README.md`, no `editorial/` directory** — it runs the
   core with no trace of the Publishing Base contract, which is itself evidence for Q1: a book can
   have the core with nothing of the base around it. **MTGOA synced to v34 the same day (DL-109);
   both projects now agree.** The sync was version-only: every shared core file was already
   byte-identical, so nothing in MTGOA's instruments actually changed except the number.

## Corrections log

| date | correction |
|---|---|
| 2026-09-12 | Page written. "Steps 3–6" in the plan and the review corrected to steps 2, 3, 5 and 7 against the gate's actual text. The review's "installed in friendcraft 09-01" is not reproducible from the clone as it stands; the kit reached friendcraft's `main` on 2026-09-09 (#17). |
| 2026-09-22 | Core row updated v32 → v33 (mechanism-only sync, `density.py`/`fragment.py`, 2026-09-11). Zero-target debt line added: the 335 hits PR #25 merged as `coherence` red were drawn to zero by 2026-09-14 and the twelve ledger entries ratified the same day. The three decisions below are unchanged — nothing in the ten intervening commits touched the base, the core's relationship to it, or the two named siblings. |
| 2026-09-22 | Six-Face panel run on the three open questions (`specs/PANEL_LINEAGE_OPEN_QUESTIONS_2026-09-22.md`). Recommendations added for Q1 (two things) and Q2 (the kit was never a copy) below the "assumes one" line, marked as Wendell's to ratify. Q3's siblings claim retracted on fresh evidence; a fourth, unexplained repository surfaced the same day. |
| 2026-09-22 | Wendell named `wendell-britt-fear-to-joy-manuscript` as the missing sibling. Repo added to session scope and cloned. Confirmed: genuinely runs editorial-core, at **v34** — ahead of MTGOA's v33 — with no Publishing Base files at all. The core row and Q3 above are corrected in place; MTGOA is now the version behind, unsynced. |
| 2026-09-22 | MTGOA synced to v34 (DL-109), on Wendell's word. Diffed first: all 27 shared core files were already byte-identical to Fear to Joy's copies; the sync changed `core_meta.CORE_VERSION` and `editorial.yaml`'s `core_version` and nothing else. Full board re-run clean, `zero` included. Every reference to MTGOA running v33 above corrected to v34; the "MTGOA is behind" line removed as no longer true. |
