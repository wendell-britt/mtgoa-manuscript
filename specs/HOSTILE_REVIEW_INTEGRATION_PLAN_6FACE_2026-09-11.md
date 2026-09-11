---
type: panel
title: "Hostile review — the integration plan of 2026-09-11"
aliases:
  - hostile review integration plan
  - integration plan review
  - publishing base vs editorial core
tags:
  - mtgoa
  - editorial
  - pipeline
  - integration
created: 2026-09-11
source:
  - specs/INTEGRATION_PLAN_2026-09-11.md
  - specs/001-publishing-base/spec.md (branch publishing-base-v0.1, PR #20)
  - instruments/coherence.py check_core
  - editorial_reports/TOOLKIT_INSTALL_ZERO_TARGET_2026-09-11.md
status: run, six of six. Two claims in the plan broke; a third mechanism the plan never saw is the finding.
---

# Hostile review of the integration plan

**Wendell, 2026-09-11:** *"do a hostile review of the integration plan."*

The standing rule applies: a review that only argues is weak here. Every claim below that could be
run was run against the fetched remotes before a Face spoke, and the ones that broke are named as
broken. **The plan was written by the reviewer four hours earlier. That is the bias, stated.**

## Measured before anybody argues

| the plan claimed | measured | holds? |
|---|---|---|
| branch → master merges clean | `git merge` in a worktree: no conflicts; the merged tree runs **gate 0 · claims PASS · round-trip + frames · xref 0/0 · toolchain pass · SHIPPABLE · coherence fails `zero` only** — identical to the branch | **yes** |
| master's two commits touch only `voice_lint.py` | `git diff --stat merge-base..master`: 1 file, 45+/9− | **yes** |
| `coherence.core` is "green while looking at nothing" | `check_core` compares manifest `core_version` to installed `CORE_VERSION` (32 = 32) and **silently skips** the third comparison when `core_home` is unreachable; prints `core ok clean` | **half.** Two of three numbers are checked. The skip is real and unannounced. |
| PR #20 is "four merges stale … close or rebase" | PR #20 is **Publishing Base v0.1** — a spec, tasks, `AGENTS.template.md` and a portable `REVIEW_GATE.md`; *"Emotional First Aid will be the first clean instantiation"* | **broke.** The plan dismissed the design document for the thing it was planning. |
| `emotional-first-aid` has "no editorial footprint … last, or not at all" | `main` is a README. **`setup/publishing-base-v0.1`** (08-18) carries `AGENTS.md`, `editorial/REVIEW_GATE.md`, `editorial/EFA_RULES.md`, eight six-Face reviews, three specs — the base instantiated | **broke.** EFA is the proving ground, not the afterthought. |
| the reports' siblings are not the GitHub siblings | friendcraft's `flirtcraft/` is five YAML files of game data; its `manuscript/` is 294 words; no repo is named *AI Psychologist* | **yes**, and still unresolved: they live somewhere this session cannot see. |
| nothing tests that the two fragment counters agree | `grep voice_lint instruments/`: nothing | **yes — and it is three, not two.** friendcraft's `voice_lint.py` differs from master's by 253 lines and from the branch's by 217, with no `VERB_S`. |
| "leave `zero` red on master" is a decision for Wendell | `editorial.yaml:38` — *"The house policy: ZERO. Every hit is a defect until it is resolved in the prose or accepted, one at a time"* | **broke.** Already ruled. The plan escalated a decided question. |

**One finding no Face argued for, because a measurement produced it.** Pointing the branch's
instruments at another repository's files measured the wrong book. `trailing_and.py
$EFA/manuscript/*.md` — a glob that matched nothing — silently ran MTGOA's own corpus and reported
MTGOA's numbers as EFA's. On friendcraft's 294 words it reported `stale=84`: MTGOA's ledger, read
against a stranger's text. **Every instrument resolves `ROOT`, the manifest and the ledger from its
own file location, never from the files it was handed.** The plan's Phase 3 would have walked three
books into that.

---

## SHAMAN · the Body — *the plan never read the thing it was replacing*

The plan opens with *"check the work on all the branches."* It listed PR #20 in a table, called it
stale, and recommended closing it — **without opening it.** It is the Publishing Base: the
month-old design for exactly what the plan was written to do, with a proving ground already
running in EFA.

That is not a gap in the survey. It is the survey's method failing at the one branch that
mattered: age was read as staleness. The branch is old *because it is upstream* of everything
that came after.

**Votes:** the plan is withdrawn as written. Phase 0 survives because it was measured; the rest is
re-derived from three mechanisms, not two.

## CHALLENGER · the Line — *three mechanisms, and the plan chose the newest by default*

Lay them side by side, in the order they were made:

| | made | shape | for | state |
|---|---|---|---|---|
| **voice-kit** | 08-10 | `voice_lint.py` + two skills, stdlib only | product copy (bars-engine, friendcraft) | installed in friendcraft 09-01, **before** PR #23's fix |
| **Publishing Base v0.1** | 08-15 | a contract: repo layout, review-gate *sequence*, `AGENTS` template; *"each book supplies its own rules, thresholds, exceptions"* | every Wendell Britt book | instantiated in EFA 08-18; **PR #20 open, unmerged** |
| **editorial-core v32** | 09-10/11 | instruments by copy, `sync_core.py`, manifest-driven `editorial.yaml` | book projects in The Library | installed in MTGOA via PR #24; **the core itself is uncommitted, on one disk** |

**editorial-core is Publishing Base's Phase 3, built on another branch without citing it.** The
base's task list says *"Identify which MTGOA checks are truly generic; port generic checks behind
book-local configuration"* — unchecked. `editorial.yaml` **is** that book-local configuration.
`sync_core.py` **is** that port. The work was done. The task list does not know.

And the base's own rule for when to make a shared repo — *"once two books implement the same
interfaces, the genuinely shared code can be moved into a dedicated publishing repo"* — the plan's
Phase 1 proposes to do **before** a second book on GitHub has implemented anything. The reports say
two Library books already run v32. **If that is true the condition is met; if it is not, Phase 1 is
premature by the base's own standard.** The plan did not ask.

**Votes:** Phase 1 stands only if the two Library books are named and shown running v32. The base
and the core are reconciled *in one document* before either moves.

## REGENT · the Inheritance — *EFA was demoted for having nothing on `main`*

The plan looked at `main`, saw a README, and ranked EFA last. **EFA's book is on a branch because
the base told it to be**: the base's Phase 2 is *"Create repository. Seed the Publishing Base
files. Add EFA-specific `AGENTS.md`…"* — and `setup/publishing-base-v0.1` has done four of those
nine. It has eight six-Face reviews of a first chapter and no `manuscript/` yet, because
*"Add `manuscript/00-introduction.md` from the approved Author-stage draft"* is the next unchecked
box.

So EFA is not the last sibling. **It is the one that has been following the contract, and the plan
proposed to sync it with a core that does not know the contract exists.**

**Votes:** EFA moves to first among the siblings, and the sync it gets is *the base's Phase 3*, with
editorial-core as the implementation — not a copy dropped over a repo that has its own `editorial/`
directory already.

## ARCHITECT · the Design — *the instruments cannot be pointed at another book*

The measurement at the top is the Architect's whole finding. `HERE = dirname(__file__)`;
`ROOT = HERE/..`; the manifest, the ledger, the corpus, the exceptions all resolve from there.
**An instrument run from MTGOA on EFA's files measures MTGOA and consults MTGOA's ledger.** Worse:
a glob that matches nothing falls through to *the book*, so the wrong answer arrives with no error.

This is not a Phase 3 detail. It means **"install the core into each repo" is the only shape that
works today**, and it means every number a report quotes for a sibling was produced *inside that
sibling's tree*, which is the one place this session cannot see. The reports may be right. They are
unverifiable from here.

Two mechanical conditions, then, on any sync:

1. **Every instrument takes `--root`**, defaulting to `HERE/..`, so a check can be run against a
   tree from outside it and the ledger it consults is that tree's.
2. **An empty corpus is a hard error, not a fallthrough.** Zero files matched is the single most
   common way to measure the wrong thing and be told nothing.

And on `check_core`: when `core_home` is unreachable it must **say so** — `core ok (home
unreachable; 2 of 3 compared)` — rather than `ok clean`. The plan's claim was half right and the
half that was right is the half that matters.

**Votes:** Phase 3 is blocked on the two conditions above. `check_core` reports its skip.

## DIPLOMAT · the Table — *the plan asked Wendell three questions and one was already answered*

*"Leave `zero` red on master"* is line 38 of `editorial.yaml`: the house policy is zero, every hit
is a defect until resolved or ledgered. **The manifest ruled it on 2026-09-11 and the plan escalated
it the same day.** That is the Sage's finding from the write-contract panel — *escalation looked
like deference and functioned as delay* — arriving for the fourth time in three days.

The other two questions are real. *Core-built or separate-lineage voice kit* is a design call the
README argues one way and the drift argues the other. *Where Flirtcraft and AI Psychologist live*
cannot be measured from here, and the Diplomat will not pretend the fingerprint attempt worked: it
measured MTGOA twice.

But there is a fourth question the plan did not ask and should have, because it decides the
others: **is Publishing Base the contract that editorial-core implements, or are they competitors?**
The base says *sequence*; the core says *instruments*. Read together they are one thing — the
core's `review.py` runs the base's steps 3–6 and the base's steps 0–2 and 7 are a person. Read
apart they are two roadmaps for the same books.

**Votes:** two questions to Wendell, not three; the fourth added; `zero` stays red because it was
already ruled.

## SAGE · the Board — *the plan is a symptom of the thing it was about*

Three mechanisms for portable editorial review, made in three months by three sessions, each
without reading the last: the voice kit does not know the base exists, the base does not know the
core exists, the core's reports cite neither. **The plan added a fourth document to the pile and
recommended closing the second.**

That is the integration problem, and it is not a merge problem. The merge is clean. **The problem
is that the account has three answers to "how does a book get reviewed" and no one document says
which is upstream of which.** Until that document exists, every sync is a copy of one lineage into
a repo that may already carry another — which is precisely what would have happened to EFA.

So the Sage's ruling is procedural and it comes before any phase: **one page, in this repo, naming
the three mechanisms, their dates, what each owns, and the order they inherit in.** Base as
contract; core as the instruments that implement the contract's steps 3–6; voice kit as the
stdlib-only export for repos that will never install the core. Written down, then everything else
in the plan is re-derived from it.

**Votes:** the lineage document first. Phase 0 proceeds because it is independent of it and
measured. Everything after Phase 0 waits.

---

## Consensus, six of six

**The plan is withdrawn as written and Phase 0 survives.** The merge is clean and the merged tree
runs the same board as the branch; that was measured twice. **Open the PR.** `zero` stays red on
master because `editorial.yaml:38` already ruled it, not because the plan recommended it.

**PR #20 is not closed. It is the upstream.** Publishing Base v0.1 is the contract every Wendell
Britt book inherits; editorial-core v32 is that contract's Phase 3, built without citing it; the
voice kit is the stdlib export for repos that will never carry the core. **One lineage page states
this in the repo before anything else moves**, and the base's task list is updated to show Phase 3
done by other hands.

**EFA moves from last to first.** It has been following the contract since 08-18 and has a
`setup/publishing-base-v0.1` branch four tasks deep. What it needs is the core as the base's Phase 3
— installed into a repo that already has an `editorial/` directory, without overwriting it.

**Phase 3 is blocked on two mechanical conditions, both found by measurement:** every instrument
takes `--root`, and an empty corpus is a hard error. Until then a sibling cannot be measured from
outside its own tree, which means every sibling number in every report is unverifiable from here
and the plan should have said so.

**`check_core` says what it skipped.** `ok clean` while the third comparison never ran is the same
shape as `--verify` over stale frames and `light_verb` over four invisible phrases: a green line
over an unlooked-at half, the third instrument this week.

**Two questions to Wendell, not three**, plus one the plan missed: whether base and core are one
thing or two. The `zero` question is withdrawn as already answered.

## What the panel refuses

It does not close PR #20. It does not sync a sibling from outside its tree until the instruments
can be pointed at one. It does not rank a book by what is on `main` when its contract puts the work
on a branch. It does not escalate a question the manifest has ruled. And it does not let the plan's
author — this reviewer — count *"the merge is clean"* as the plan being right, because the merge
was the one part nobody doubted.
