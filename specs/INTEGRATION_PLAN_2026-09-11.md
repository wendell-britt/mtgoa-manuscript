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
status: measured, not executed. Nothing merged, nothing pushed to master, no PR opened.
---

# Integration plan

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
| `publishing-base-v0.1` | `cec5c00` | 08-15 | **open PR #20**, base at `de6d4e4` — four merges behind master. Stale. |
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
| — | `emotional-first-aid` — no editorial footprint |

So there are **two book projects that exist only in The Library**, one **core that exists only in
The Library**, and one kit installed into a GitHub repo **with a known hole**.

## 4 · Two kits, drifting

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

### Phase 0 — land the branch on `master` (this repo, this week)

1. **Merge `origin/master` into the branch.** Clean; brings PR #23's `voice_lint.py` fix. Run the
   full board. *(mechanical; I can do it on the word.)*
2. **Open the PR, branch → master.** One PR. The body names the 25 rulings, the toolkit install,
   and the 335 in one sentence each, and **states that `coherence` will fail `zero` on master
   after the merge**, because master will finally be able to count.
3. **Do not silence `zero` to get a green merge.** `shipcheck` is the ship gate and it passes;
   `coherence.zero` is the editorial debt board and it should stay red until the prose is worked.
   Moving the seven targets to `reporting:` would be the `quiet`→`careful` evasion at repo scale.
4. After merge: delete `editorial/trailing-and-onto-proof-2026-09-10`, `claude/fragment-ban`,
   `claude/post-merge-fixes`. **Close PR #20** or rebase it — four merges stale and it predates the
   toolkit entirely.

**Risk:** none technical. **Decision for Wendell:** item 3.

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

### Phase 3 — bring the siblings onto the same board

For each project that has prose and no manifest — in this order:

1. **`friendcraft-manuacript`** (has `manuscript/`, has a voice-kit branch, is on GitHub).
   `sync_core --apply` from the Phase-1 repo; write `editorial.yaml` (project, corpus, banned,
   targets); commit `editorial_exceptions.yaml` empty; run `coherence`. The board will fail `zero`
   on day one, which is the point.
2. **Flirtcraft and AI Psychologist in The Library.** The reports already carry their v32 numbers
   (light_verb 1 / 5; trailing_and 72 / 104), so the install exists locally and needs a repo each,
   or a home inside an existing one. **Decision for Wendell:** where these two live on GitHub.
3. **`emotional-first-aid`** last, or not at all: it has no editorial footprint and nothing in the
   reports names it.

Each install is one commit per repo with the report shape PR #24 used: what the install did, the
manifest, the board measured before and after, what did not move.

### Phase 4 — the debt (ongoing, not integration)

The 335 in MTGOA; the equivalents the siblings will surface. Rewrite or ledger, one at a time.
This is the editorial pass, and the mark-pattern table's honest boundary still applies: P1 and P2
are unsearchable, and **78% of MTGOA has never been read on paper**.

---

## 6 · What this plan refuses

It does not merge anything on its own authority. It does not open the PR before Wendell has seen
that `coherence` will go red on master. It does not move zero targets to reporting to make a
board green. It does not sync a sibling from a core that exists only as files on one disk. And it
does not treat the GitHub `flirtcraft` as the book the reports call Flirtcraft — they are not the
same thing, and the plan would have pointed a sync at a Next.js app.

## 7 · Ready on the word

- **Phase 0, items 1–2:** merge master in, run the board, open the PR. Mechanical, clean, measured.
- **Phase 2, item 1:** the two-counter diff. Read-only.
- **Phase 2, item 3:** the friendcraft re-export. One commit on a branch that already exists.

Everything else waits on a repo that is not on GitHub yet.
