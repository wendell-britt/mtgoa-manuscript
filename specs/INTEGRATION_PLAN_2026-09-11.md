---
type: plan
title: "Integration plan — the proof branch, the shared core, and the kits, 2026-09-11"
aliases:
  - integration plan
  - branch integration
  - editorial-core landing
tags:
  - mtgoa
  - editorial
  - pipeline
  - integration
created: 2026-09-11
review: 2026-09-18
source:
  - editorial_reports/TOOLKIT_INSTALL_ZERO_TARGET_2026-09-11.md
  - editorial_reports/LIGHT_VERB_TO_CORE_2026-09-11.md
  - editorial_reports/GATE_DIET_DATA_TO_MANIFEST_2026-09-11.md
  - editorial_reports/FRAGMENT_REFEREE_2026-09-10.md
  - editorial.yaml
  - instruments/core_meta.py
status: measured, not executed, then REVISED the same day by a hostile review that broke two of its claims. Nothing merged, nothing pushed to master, no PR opened.
---

# Integration plan

> **Revised 2026-09-11 after `HOSTILE_REVIEW_INTEGRATION_PLAN_6FACE_2026-09-11.md`, six of six.**
> Two claims in the first draft broke under measurement and are struck below in place rather than
> erased. **PR #20 is not stale; it is Publishing Base v0.1, the contract upstream of everything
> here, with a proving ground already running in EFA.** **EFA is not last; it is first.** And the
> `zero` question was already ruled by `editorial.yaml:38` and is withdrawn. The three mechanisms —
> base (08-15), voice kit (08-10), core (09-11) — are reconciled in one lineage page before any
> phase after Phase 0 moves. See §5 as revised.

**Wendell, 2026-09-11:** *"check the work on all the branches and come up with an integration plan.
There's been a lot of work done on fixing and making the editorial review accessible from all of my
book projects."*

Everything below was measured on 2026-09-11 against the fetched remotes. Where a number is
quoted, the command that produced it is named. **Nothing was merged and nothing was pushed to
`master`.** The one repair made in passing: this session's clone had been left on a detached HEAD
by a read-only checkout; it is back on the branch, at origin.

---

## 1 · The branches, as they stand

| branch | head | date | what it is |
|---|---|---|---|
| `master` | `8c2ab20` | 09-11 | the proof line. **Pre-toolkit**: no `editorial.yaml`, no `coherence.py`, no `claims.py`, 60 DL rows. PR #23 fixed the voice kit's fragment `-s` hole in `export/voice-kit/tools/voice_lint.py`. |
| `claude/book-pdf-epub-production-ybxa11` | `55b0a71` | 09-11 | **the integration branch.** This session's editorial work (DL-78 → DL-105) **plus PR #24**, which Wendell merged into it: the core v32 install and the zero-target manifest. 160 commits ahead of master. |
| `editorial/trailing-and-onto-proof-2026-09-10` | `4da54c1` | 09-11 | PR #24's source. Fully contained in the branch above. Done. |
| `publishing-base-v0.1` | `cec5c00` | 08-15 | **open PR #20 — Publishing Base v0.1.** ~~Stale.~~ **Struck by the review:** it is the portable house contract (repo layout, review-gate sequence, `AGENTS` template), with EFA as *"the first clean instantiation"*. It is upstream of the core, not behind it. |
| `claude/fragment-ban`, `claude/post-merge-fixes` | | 09-01 | PRs #21/#22, merged to master and onto the branch. Done. |
| `claude/sales-page-analysis-t2qr`, three `claude/*-2026-08-13` | | 08/09 | merged or superseded; nothing unique left (`git log master..` empty or specs only). |

**The test merge, branch → master: clean, zero conflicts** (`git merge --no-commit` in a
worktree). Master is two commits ahead, both confined to `export/voice-kit/tools/voice_lint.py`,
which the branch never touched — so master's fix wins automatically.

## 2 · The two boards, measured

| | `master` today | the branch today |
|---|---|---|
| gate | 0 | 0 (`EDITORIAL … unresolved=0`) |
| claims registry | **absent** | PASS, 26 claims, 100+ spans guarded |
| round-trip + frames | body only | body **and** frames match (DL-89) |
| xref | — | 0 broken · 0 unreferenced |
| toolchain | — | all cases pass |
| shipcheck | SHIPPABLE | SHIPPABLE |
| coherence | **absent** | 9 checks ok · `reference` n/a · **`zero` FAILS: 335 unresolved** |
| DL rulings | 60 | **85** |
| manuscript words | 115,422 | **112,793** (−2,629) |

**The `zero` failure is the honest state and it is the only red on the branch.** telling 198,
light_verb 52, slop_shapes 40, fragment 38, polysyndeton 7. PR #24's own report says it plainly:
*"This is the debt that was always there. The proof-line instruments surfaced it as a baseline and
never counted it to zero."* Master does not fail this check because master cannot run it.

## 3 · Where the shared core actually is — the finding that shapes the plan

`editorial.yaml` says `core_home: ../editorial-core`. Every reconciliation report says the v32
core *"lives in `editorial-core/` in The Library"* and is *"committed as one editorial-core v32
release **after the PR**, with the two siblings synced. Nothing is pushed."*

**It is not in any repository in the account.** `list_repos` returns 29 repositories; none is an
editorial core. `core_meta.home_version("../editorial-core")` returns `None` here, and
`coherence`'s `core` check passes **by declining to guess** — its documented behaviour when the
core tree is unreachable. So the check that is supposed to catch a stale core is green in every
clone that is not Wendell's laptop.

**The "siblings" in the reports are not the sibling repositories on GitHub.**

| report says | GitHub has |
|---|---|
| *Flirtcraft* — a book, measured at light_verb 1, trailing_and 72 | `wendell-britt/flirtcraft` — a Next.js app; no `instruments/`, no manifest, last push 08-30 |
| *AI Psychologist* — a book, light_verb 5, trailing_and 104 | **no repository by that name** |
| — | `friendcraft-manuacript` — a `manuscript/` dir and one branch, `claude/voice-kit` (09-01, 1 commit): the voice-kit skills + `voice_lint.py`, **installed before PR #23's fix** |
| — | `emotional-first-aid` — ~~no editorial footprint~~ **struck:** `main` is a README, but `setup/publishing-base-v0.1` (08-18) carries `AGENTS.md`, `editorial/REVIEW_GATE.md`, `EFA_RULES.md`, eight six-Face reviews and three specs. **The base, instantiated.** No `manuscript/` yet — that is its next unchecked task. |

So there are **two book projects that exist only in The Library**, one **core that exists only in
The Library**, and one kit installed into a GitHub repo **with a known hole**.

## 4 · ~~Two~~ Three kits, drifting

**Revised:** the review found a third, and it is the oldest of the three that matters most.

| | made | shape | for | state |
|---|---|---|---|---|
| voice-kit | 08-10 | `voice_lint.py` + two skills, stdlib only | product copy | in friendcraft since 09-01, **pre-#23**, and 253 lines from master's copy — a third fragment-counter lineage |
| **Publishing Base v0.1** | 08-15 | a contract: layout, review-gate *sequence*, `AGENTS` template | every book | instantiated in EFA 08-18; **PR #20 open** |
| editorial-core v32 | 09-11 | instruments by copy, `sync_core.py`, `editorial.yaml` | Library books | in MTGOA via PR #24; **the core is uncommitted, on one disk** |

**editorial-core is Publishing Base's Phase 3** — *"identify which MTGOA checks are truly generic;
port generic checks behind book-local configuration"* — built on another branch without citing it.
`editorial.yaml` is that configuration. The base's task list still shows the box unchecked.

The repo carries two portability mechanisms and they have already diverged once:

- **`editorial-core`** (`sync_core.py`, v32): the full instrument set, manifest-driven, for book
  projects. Its `fragment.py` had the `-s` hole closed on 2026-09-01.
- **`export/voice-kit`** (`voice_lint.py` + two skills): the small stdlib-only kit for product-copy
  repos (`johnair01/bars-engine`, friendcraft). Its copy of the fragment counter had the same hole
  closed **separately** by PR #23 on 2026-09-11 — with a different fix (a hand list, `VERB_S`).

That is two fragment counters again, ten days after *"One fragment counter"* was the title of a
commit. Nothing tests that they agree.

---

## 5 · The plan

### Phase 0 — land the branch on `master` (this repo, this week) — *survives the review*

1. **Merge `origin/master` into the branch.** Clean; brings PR #23's `voice_lint.py` fix. Run the
   full board. *(mechanical; I can do it on the word.)*
2. **Open the PR, branch → master.** One PR. The body names the 25 rulings, the toolkit install,
   and the 335 in one sentence each, and **states that `coherence` will fail `zero` on master
   after the merge**, because master will finally be able to count.
3. **`zero` stays red on master.** ~~Decision for Wendell.~~ **Struck: already ruled** —
   `editorial.yaml:38`, *"The house policy: ZERO. Every hit is a defect until it is resolved in the
   prose or accepted, one at a time."* The plan escalated a decided question.
4. After merge: delete `editorial/trailing-and-onto-proof-2026-09-10`, `claude/fragment-ban`,
   `claude/post-merge-fixes`. ~~Close PR #20.~~ **Struck. PR #20 is not closed; see Phase ½.**

**Risk:** none technical — the merged tree was run and carries the branch's board exactly.

### Phase ½ — the lineage page (before anything after Phase 0) — *added by the review*

One page in this repo naming the three mechanisms, their dates, what each owns, and the order they
inherit in: **base as contract; core as the instruments that implement the contract's review-gate
steps 3–6; voice kit as the stdlib export for repos that will never carry the core.** Then PR #20's
`tasks.md` is updated to show Phase 3 done by other hands, and PR #20 is **merged or rebased —
never closed.** Until this page exists, every sync copies one lineage into a repo that may already
carry another, which is exactly what Phase 3 below would have done to EFA.

**Decision for Wendell, the one the first draft missed:** are the base and the core one thing or
two? The page assumes one. If two, the page says which wins.

### Phase 1 — make the core an object that exists off one laptop (before any sibling sync)

1. **Create `wendell-britt/editorial-core` and push the v32 tree from The Library**, with
   `VERSION` = 32 and `sync_core.py` in it. *Wendell's — the tree is on his machine, and every
   report defers exactly this step to "after the PR".*
2. **Give `coherence.core` a remote to read.** Add `core_repo:` beside `core_home:` in
   `editorial.yaml`; when the local tree is absent, the check reads `VERSION` from the repo instead
   of declining. Until then, every CI run and every remote clone reports a green `core` check that
   has looked at nothing.
3. **Tag the release** `core-v32` at the commit that matches the instruments installed by PR #24.
   `core_meta.CORE_VERSION` already travels with the copy; the tag is the other half.

**Why this is Phase 1 and not Phase 3:** the reports say the siblings will be *"synced to v32 in
the same change."* A sync from an uncommitted tree is a copy of a copy. The core becomes its own
object first — the six-Face ruling of 2026-09-09 the `core_meta` docstring cites.

**Condition added by the review.** The base's own rule is *"once two books implement the same
interfaces, the genuinely shared code can be moved into a dedicated publishing repo."* The reports
say two Library books already run v32. **Phase 1 proceeds only when those two are named and shown
running it**; otherwise it is premature by the base's standard. And `check_core` **reports its
skip** — `core ok (home unreachable; 2 of 3 compared)`, not `ok clean` — before the core moves,
because today it is a green line over an unlooked-at half.

### Phase 2 — reconcile the two kits

1. **Measure before deciding.** Run core `fragment.py` and voice-kit `voice_lint.py` over the same
   inputs — ch1–9 and the 231 bars-engine copy files PR #23 measured on — and diff the site lists.
   PR #23 reports its residual honestly (*"the ambiguous 3sg tail … a stdlib heuristic cannot
   resolve"*); the diff says how far the two counters are apart today.
2. **Decision for Wendell:** is the voice kit *built from* the core (a thin export, versioned with
   `CORE_VERSION`), or a **separate lineage** on purpose (stdlib-only, no NLTK, for repos that
   will never install the core)? The README argues the second — *"almost none of it ports"* — and
   that is a real constraint. If separate: **add the referee's fixture set as a shared test both
   counters must pass**, so the next hole gets closed once.
3. **Re-export to friendcraft.** Its `claude/voice-kit` branch carries the pre-#23 counter. One
   commit: the fixed `voice_lint.py`, the LICENSE travelling with `no-ai-slop`.

### Phase 3 — bring the siblings onto the same board — *blocked, reordered*

**Blocked on two mechanical conditions the review found by measurement.** Pointing the branch's
instruments at another repository's files measured the wrong book: a glob matching nothing fell
through to MTGOA's corpus, and a foreign text was read against MTGOA's ledger (`stale=84`). Every
instrument resolves `ROOT`, manifest and ledger from its own file location. So, first:
(1) **every instrument takes `--root`**, defaulting to `HERE/..`; (2) **an empty corpus is a hard
error, not a fallthrough.** Until then no sibling can be measured from outside its own tree, and
**every sibling number quoted in the reports is unverifiable from here.**

For each project that has prose — in this order, **revised**:

1. **`emotional-first-aid`** — ~~last, or not at all~~ **first.** It has followed the base since
   08-18 and is four tasks into the base's Phase 2. What it gets is the core *as the base's Phase 3*,
   installed beside its existing `editorial/` directory, not over it.
2. **`friendcraft-manuacript`** — has 294 words of `manuscript/` and a `claude/voice-kit` branch
   carrying a pre-#23 counter. The re-export (Phase 2, item 3) before any core install; its
   `flirtcraft/` directory is five YAML files of game data, **not the book the reports call
   Flirtcraft.**
   `sync_core --apply` from the Phase-1 repo; write `editorial.yaml` (project, corpus, banned,
   targets); commit `editorial_exceptions.yaml` empty; run `coherence`. The board will fail `zero`
   on day one, which is the point.
3. **Flirtcraft and AI Psychologist in The Library.** The reports carry their v32 numbers
   (light_verb 1 / 5; trailing_and 72 / 104). The review tried to fingerprint them by running the
   instruments on the GitHub repos and **measured MTGOA twice instead** — see the block above. They
   are not on GitHub under any name this session can see. **Decision for Wendell:** where they live.

Each install is one commit per repo with the report shape PR #24 used: what the install did, the
manifest, the board measured before and after, what did not move.

### Phase 4 — the debt (ongoing, not integration)

The 335 in MTGOA; the equivalents the siblings will surface. Rewrite or ledger, one at a time.
This is the editorial pass, and the mark-pattern table's honest boundary still applies: P1 and P2
are unsearchable, and **78% of MTGOA has never been read on paper**.

---

## 6 · Decisions for Wendell — *two, not three, plus the one the draft missed*

1. **Base and core: one thing or two?** The lineage page assumes one — base as contract, core as
   its Phase 3. If two, which wins.
2. **Voice kit: built from the core, or a separate stdlib lineage on purpose?** The README argues
   separate; three diverging fragment counters argue for a shared fixture test either way.
3. **Where Flirtcraft and AI Psychologist live.** Not measurable from here.

~~Leaving `zero` red on master~~ — withdrawn; `editorial.yaml:38` ruled it.

## 7 · What this plan refuses

It does not merge anything on its own authority. It does not move zero targets to reporting to
make a board green. It does not sync a sibling from a core that exists only as files on one disk,
nor from outside that sibling's tree while the instruments cannot be pointed at one. It does not
close PR #20. It does not rank a book by what is on `main` when its contract puts the work on a
branch. And it does not treat the GitHub `flirtcraft` as the book the reports call Flirtcraft.

## 8 · Ready on the word

- **Phase 0, items 1–2:** merge master in, run the board, open the PR. Mechanical, clean, measured.
- **Phase 2, item 1:** the two-counter diff. Read-only.
- **Phase 2, item 3:** the friendcraft re-export. One commit on a branch that already exists.

Everything else waits on a repo that is not on GitHub yet.
