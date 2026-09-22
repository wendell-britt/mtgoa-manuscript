---
type: panel
title: "Six Faces on the lineage page's three open questions"
aliases:
  - lineage panel
  - base core one or two
tags:
  - mtgoa
  - editorial
  - pipeline
  - integration
created: 2026-09-22
source:
  - specs/EDITORIAL_LINEAGE.md
  - specs/001-publishing-base/tasks.md on branch publishing-base-v0.1 (PR #20)
  - export/voice-kit/tools/voice_lint.py vs instruments/gate.py, prose_diet.py, fragment.py
  - mcp list_repos (account-wide, 2026-09-22)
status: run, six of six. Recommendations, not rulings — the lineage page names all three as Wendell's.
---

# Six Faces on the lineage page's three open questions

**Wendell, 2026-09-22:** *"have the 6 game masters weigh in on the open questions."*

The standing rule: measure before a panel sits. Everything in the table below was run today, after
fast-forwarding to master and correcting the lineage page's version number. None of it decides the
three questions — the lineage page named them as Wendell's, and a panel recommending itself into a
Face's decision is the exact failure the hostile review of 2026-09-11 caught the last plan making.

## Measured before anybody argues

| question | measured | what it shows |
|---|---|---|
| **Q1 — one thing or two?** | PR #20's `tasks.md`: 5 of 36 boxes checked, unedited since 2026-08-15 | The base's own bookkeeping does not know editorial-core exists. It still lists "port generic checks" as future work eleven days after the core did it, on a different branch, without telling this one. |
| **Q2 — kit built from core, or separate?** | `export/voice-kit/tools/voice_lint.py` has no function or constant in common with `instruments/gate.py`, `prose_diet.py`, or `fragment.py` — `EMPTY_HEAD`, `fragments()`, `looks_like_prose()` are independent re-implementations, not copies | The README's claim — *"copied verbatim… when the book's counters change, re-copy them"` — is not what the file shows. It is a parallel build that happens to agree on shape. |
| **Q2, continued** | The kit was not touched by the v33 sync (`0396d8d`, `density.py`/`fragment.py` only) or by friendcraft's fix history | Three fragment counters exist (core's, the kit's, friendcraft's stale copy) and a version bump to one has never once propagated to the other two. |
| **Q3 — where do the siblings live?** | `list_repos`, account-wide, today: `wendell-britt/flirtcraft` is a real private repo, pushed 2026-09-16 — a Next.js app, no `instruments/`, not a manuscript project. No repository anywhere is named *AI Psychologist*. | Flirtcraft exists and is not a sibling of this pipeline — it has no editorial system to sync. The second name has no referent at all. |
| **Q3, continued** | `wendell-britt/wendell-britt-fear-to-joy-manuscript`, pushed **today**, 2026-09-22 | A fourth repository this account holds, named like a book, never mentioned in any report so far. Out of scope for this session to open without being added; named here because a panel on "where do the siblings live" that doesn't report a same-day repo push is not measuring. |

---

## SHAMAN · the Body — *Q1: two jobs, felt as two jobs*

Read the base's contract and the core's manifest side by side without the vocabulary. The base
says: *before you touch prose, know who may approve it, where drafts live, what "canon" means.*
The core says: *here is a sentence; does it hedge, does it tell instead of show, does it repeat.*
One is about **permission and custody**. The other is about **the sentence in front of you.** A
person can answer the first without ever running a counter, and can run every counter in
`editorial.yaml` without ever knowing who is allowed to approve the result.

That is not one job wearing two names. It is two jobs that happen to sit in the same repository
because the first book to need either built its own of both.

**Recommendation: two things, in a strict order.** The base governs whether a change may become
canon. The core measures whether a change is any good. A book can have the first without the
second — EFA does, right now — but never the second without the first, because a counter with no
approval rule around it is a number nobody is accountable to.

## CHALLENGER · the Line — *Q2: "copied verbatim" does not survive the file*

Steelman the README first: *maybe "copied verbatim" meant the counters' logic, not the byte
content — ported by hand, same behavior, different code shape.* Test it. `EMPTY_HEAD` in the core
is a single compiled pattern reused across three files; the kit's `EMPTY_HEAD` is its own pattern,
matching a narrower list, missing forms the core added after 08-10. `fragments()` in the kit takes
a `max_words` argument the core's equivalent doesn't have. These are not stylistic differences. A
sentence the core would flag can pass the kit clean, and the hostile review already proved it: the
kit's own `-s` hole needed a **separate** fix, PR #23, discovered independently of the core ever
having the same hole.

The steelman fails. **This is not a copy that drifted. It was never a copy — it was a fork with a
copy's name on it**, and the name is why nobody has audited it since 08-10.

**Recommendation: stop calling it copied and decide which claim the README should make.** Either
re-derive the kit's counters from the core mechanically (a script, run at every core release, so
"re-copy them" becomes true) or rename the relationship to what it is — a separate, permanently
maintained lineage that promises *agreement in shape*, not *agreement in code* — and drop the line
that tells a reader something false about how safe it is to trust the kit unaudited.

## REGENT · the Inheritance — *Q3: one sibling is real and it isn't a sibling*

The reports that named "Flirtcraft" as a book running the shared core were checked twice now and
both times the repo they point at turned out to be something else: first, a directory of five YAML
game files inside friendcraft's repo; today, a Next.js product repo with no editorial machinery at
all. Two different wrong answers to the same question is not a fluke of missing access — it is a
report that was never reading a repository, only repeating a name.

*AI Psychologist* fares worse: nothing, in two searches ten days apart, months apart in the
account's own history.

**Recommendation: the two-siblings claim in the toolkit-install report is retracted until a repo is
named and opened.** Not "cannot verify" — retracted, the same way a claim gets struck when the
evidence contradicts it twice. And the fourth repository this account pushed to today deserves one
sentence from Wendell, not an assumption from this panel: is `fear-to-joy-manuscript` the missing
sibling, a new book, or unrelated. This panel does not open it without being told to.

## ARCHITECT · the Design — *what Q1's answer costs, mechanically, either way*

If Wendell rules **one thing**: the base's repo-contract must gain an `editorial/` slot that names
which core version a book runs, and `coherence.py`'s `core` check becomes load-bearing everywhere,
not just in MTGOA. That means porting the `--root` and empty-corpus-is-error fixes the hostile
review already required for Phase 3 — no way around it, because "one thing" means the base cannot
ship without knowing the core is there.

If Wendell rules **two things**: the base needs nothing from the core, and a book may adopt the
contract with zero instruments — which is EFA's exact state right now, seven weeks along and
correct by that reading. The core then never needs the base to exist; it already doesn't reference
it anywhere in `editorial.yaml` or `core_meta.py`.

**Both readings are buildable. Neither is free, and they are not the same shape of not-free.** One
thing costs Phase 3's mechanical work up front. Two things costs a permanent duplicate of "how do I
know if I should install the core" living in two documents that must be kept in sync by hand — the
same failure mode that produced this panel.

**Recommendation: two things, with the base required to say, in its own contract text, that a book
with a manuscript inherits the core by name.** That keeps the systems separable — the Architect's
job is to notice when separable is worth keeping — while removing the silent duplication.

## DIPLOMAT · the Table — *what is actually Wendell's, after the measuring*

Q1 and Q2 both got a recommendation above because the evidence points one way hard enough to state
it plainly, the way `editorial.yaml:38` was already decided and the 09-11 plan was wrong to
re-ask it. **Q3 does not get a recommendation, because the evidence this time doesn't converge —
it only rules things out.** Flirtcraft is ruled out as a sibling. AI Psychologist is ruled out as
existing under that name. What's left is a real question with a real fourth repository sitting
under it, unopened.

**The one question actually left open for Wendell, cleanly:** which of the two readings above —
base needs the core by name, or base and core stay wholly separable — and whether
`fear-to-joy-manuscript` is the answer to Q3 or a different conversation entirely.

## SAGE · the Board — *what changes on the lineage page*

Two of three questions move from "left to Wendell" to "recommended, his to ratify or override,"
because a panel that measures and then still writes "who knows" about a question the measurement
answered is doing the same thing the 09-11 plan did with `zero`. The third stays open, correctly,
because retracting a false claim is not the same as producing a true one.

**The page should read, after this panel:**

- Base and core are **two things.** The base is silent on the core today; it should name the core
  by version wherever a book has a manuscript, without requiring a book that has none to install it.
- The voice kit is **not** a copy of the core, whatever its README says. Either make the claim true
  with a mechanical re-derive step, or change the claim.
- Flirtcraft and AI Psychologist are **not** the two siblings the toolkit-install report named. That
  report's claim is retracted, not merely unverified. A fourth repository pushed today is
  unaccounted for and is Wendell's to identify.

---

## Consensus, six of six

**Q1 — two things**, with the base naming the core by version for any book that has a manuscript.
**Q2 — the kit was never a copy**; the README's claim is false as written and should either become
true (a mechanical re-derive at every core release) or be rewritten to say what actually holds.
**Q3 — not decided, because it can't be from here.** Both previously reported siblings are ruled
out on fresh evidence, and a fourth, unexplained repository exists as of today.

## What the panel refuses

It does not rule Q1 or Q2 as decided the way `editorial.yaml:38` is decided — these are
recommendations the page marks as Wendell's to ratify, not facts a manifest already states. It does
not guess at `fear-to-joy-manuscript`'s contents without being told to open it. And it does not
let "two searches found nothing" read as "cannot verify" when the honest word is *retracted*.
