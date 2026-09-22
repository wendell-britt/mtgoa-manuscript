---
type: panel
title: "Six Faces on the remaining open decisions"
aliases:
  - open decisions panel
  - lineage decisions round two
tags:
  - mtgoa
  - editorial
  - pipeline
  - integration
created: 2026-09-22
source:
  - specs/EDITORIAL_LINEAGE.md
  - specs/INTEGRATION_PLAN_2026-09-11.md (Phase 1, Phase 2 item 2)
  - specs/DECISION_LOG.md (DL-107, DL-108, DL-109)
  - publishing-base/README.md on branch publishing-base-v0.1 (PR #20)
status: run, six of six, on Wendell's word after DL-109. One question the last panel could not
  answer is now measured. Recommendations, not rulings, except where a manifest already decided.
---

# Six Faces on the remaining open decisions

**Wendell, 2026-09-22:** *"let's do a 6 game master analysis on any open decisions."*

A full sweep first, not just the two the lineage page already named. The decision log's ledger has
no unratified entries. Every "awaiting Wendell" hit outside it traces to `specs/SPEC_FINISHING_PASS
_2026-07-29.md`, written two days before the decision log existed; its R9 (placeholder tokens) is
independently confirmed closed — `grep -c "⟦" manuscript/*.md appendices/*.md` returns nothing —
and nothing else in that file is referenced anywhere since. **It is dead history, not an open
decision, and this panel does not resurrect it.** Three questions are live. Two were named by the
last panel. The third is new: today's sync surfaced a condition the integration plan set in writing
and nobody has checked since.

## Measured before anybody argues

| question | measured | what it shows |
|---|---|---|
| **D1 — base and core, one thing or two?** | unchanged since the last panel: PR #20's checklist, 5 of 36, unedited since 08-15 | Carried forward — see `specs/PANEL_LINEAGE_OPEN_QUESTIONS_2026-09-22.md`. |
| **D2 — is the voice kit built from the core?** | unchanged: `voice_lint.py` shares no code with `gate.py`/`prose_diet.py`/`fragment.py` | Carried forward, same source. |
| **D3 — does the base's two-books condition hold now?** | the base's own text: *"Once two books implement the same interfaces, the genuinely shared code can be moved into a dedicated publishing repo/template."* MTGOA (v34) and `wendell-britt-fear-to-joy-manuscript` (v34, confirmed 2026-09-22, DL-108) both run editorial-core today. | **The condition counts books, not siblings-of-MTGOA.** The 09-11 plan read it as "two Library books besides MTGOA," which DL-108 disproved. Read as written, it needs two books total and MTGOA is one of them. **Two.** |
| **D3, continued** | Phase 1's own added condition (hostile review, 09-11): *"proceeds only when those two are named and shown running it."* | Both are named, both are shown: `editorial.yaml` in each repo, diffed by hand today, not asserted. |

---

## SHAMAN · the Body — *D3 is not the same shape as D1 and D2*

Sit with the difference before arguing it. D1 and D2 are readings of ambiguous evidence — the base
and core could be one thing or two, the kit's claim could be forgiven as loose language or held to
the letter. Both took a Face's judgment last time and will again. **D3 is not that.** It is a
sentence with a number in it — *"once two books"* — and a count that either meets the number or
doesn't. The felt difference: D1 and D2 are still worth a panel's time. D3 is worth a sentence and
a decision, not six paragraphs of interpretation.

**Recommendation: answer D3 first, plainly, and spend the panel's real attention on D1 and D2.**

## CHALLENGER · the Line — *steelman D3's "no," then watch it fail*

The strongest case for waiting: *the base's authors meant a pattern, not an instance — one other
book proves nothing about whether the interfaces generalize, and MTGOA is the book the interfaces
were extracted *from*, so it shouldn't get to count as evidence for its own generalization.*

Test it against the actual words. The base doesn't say "two books besides the reference
implementation." It says "two books implement the same interfaces" — and MTGOA re-implementing its
own interfaces after extraction, in a second project that never saw MTGOA's one-off history, **is
itself the proof the interfaces generalize.** A book with 731 words and one chapter installed the
same 27 files, unmodified, and got a working board. That is a stronger signal than the steelman
gives it credit for, precisely because Fear to Joy is small and new and still matched.

**The steelman fails. Recommendation: D3 is yes**, and the count needed nothing more than what
DL-108 already found.

## REGENT · the Inheritance — *what Phase 1 actually costs, now that D3 is yes*

Phase 1's three steps, named in the plan and never executed because its own condition wasn't
checked: create `wendell-britt/editorial-core`, push the v34 tree, add `VERSION`; give
`coherence.core` a remote to read (`core_repo:` beside `core_home:` in the manifest) so a check that
today declines to guess can instead compare against something; tag the release. **None of this is
new work invented by this panel — it was already written down, blocked on a condition D3 just
cleared.**

What it inherits, if done: every future clone of MTGOA or Fear to Joy gets a `core` check that
means something, instead of `ok clean` on an unreachable path. What it costs: a repository Wendell
has to own and version going forward, and the honest admission that `sync_core.py` — referenced
everywhere, seen nowhere in this session — needs to exist inside it, not just be assumed.

**Recommendation: Phase 1 is ready to run.** Its three steps are mechanical and its blocking
condition is met.

## ARCHITECT · the Design — *D1 and D2, unchanged, and why they still aren't D3*

Nothing measured today moves D1 or D2. The base still doesn't know the core exists in its own
bookkeeping; the kit still shares no code with what it claims to copy. Restating the last panel's
structural finding rather than re-deriving it: **D1 is a design choice with two buildable shapes and
different costs** (name the core by version, versus a permanently synced interface); **D2 is a
choice between making a false claim true or rewriting it to stop being false** — not a design
trade-off, a correction either way. Treating D1 and D2 with D3's confidence would be the same
mistake the 09-11 plan made in the other direction: escalating a measured question. These two are
not measured to a single answer, and a panel that pretends otherwise is doing what got the last
plan withdrawn.

**Recommendation: no change to the prior recommendations.** D1: two things, base names the core by
version. D2: the kit was never a copy; make it true or rewrite it.

## DIPLOMAT · the Table — *what Wendell is actually being asked, three times*

Three different kinds of ask, and they should be presented as three, not folded into one paragraph:

1. **D3 wants a yes.** The condition is met; ratifying it authorizes Phase 1's three steps.
2. **D1 wants a choice between two buildable designs**, with a stated default (two things) that a
   panel recommends but does not get to rule.
3. **D2 wants a choice between two ways to stop a document from lying**, not a design preference —
   whichever way, the kit's README changes.

**Recommendation: put D3 to Wendell as a yes/no with a one-line consequence (unblocks Phase 1);
put D1 and D2 as the standing two, unchanged in shape from the last panel.**

## SAGE · the Board — *the pattern across all three*

Twice now a "decision for Wendell" turned out to already be answered by something written down
earlier — `zero` by the manifest on 09-11, and now the two-books condition by the base's own README
on 09-22. **The pattern is not that Wendell over-delegates. It's that this pipeline keeps writing
conditions into specs and then not checking them when the world changes underneath.** DL-108
changed the world. Nobody reopened Phase 1 to check its own stated trigger until this panel did.

**The board's ruling: check every standing condition before adding a new question to Wendell's
list**, the same discipline `editorial.yaml:38` already forced onto `zero`. Going forward, a
"blocked on X" note is itself a small debt — something to re-check on the next relevant fact, not
just carried as prose until a panel stumbles onto it.

**Votes:** D3 — yes, Phase 1 unblocked. D1 and D2 — unchanged, carried forward as recommendations
for Wendell to rule.

---

## Consensus, six of six

**D3 is answered, not merely recommended: the base's two-books condition is met**, by the base's own
text, counting MTGOA and Fear to Joy. **Phase 1 is ready to run** — create the `editorial-core`
repository, add `core_repo:` to the manifest, tag the release — pending only Wendell's word to do it,
since it creates a new repository and this session does not do that unasked.

**D1 and D2 are unchanged from the panel of earlier today.** D1: recommend two things, the base
naming the core by version for any book with a manuscript. D2: recommend the kit's "copied verbatim"
claim either become true (a mechanical re-derive step) or be rewritten to what actually holds.
Neither is ruled; both wait on Wendell.

## What the panel refuses

It does not treat D3 with the same uncertainty as D1 and D2 — a measured count is not a judgment
call, and hedging on one to match the shape of the other two would be the Sage's finding turned
against itself. It does not create the `editorial-core` repository without being told to, even
though it says the condition to do so is met — creating a repository is Wendell's action, not a
panel's. And it does not reopen `SPEC_FINISHING_PASS_2026-07-29.md`'s R1–R9 as live decisions: R9
is independently confirmed closed, and the other eight have no trace in the ninety-plus rulings
made since, which is its own kind of answer.
