# Handoff — the final proof

**Paste the block at the bottom into a new chat.** Everything above it is the context that
block refers to.

---

## Where things stand

**Branch:** `claude/book-pdf-epub-production-ybxa11`. **Master is `8822692`** plus whatever
has merged since; this branch is ahead by the final-proof commits and clean.

`review.py` runs twelve steps and reads clean. `shipcheck` is **SHIPPABLE** on all six
blockers. The prep for the proof is done; **the proof itself has not started.**

## What was built today, and why each exists

| step | instrument | the defect that caused it |
|---|---|---|
| 7b | `ranking.py` | the fragment negation *"Not willpower, not determination:"* — invisible to the voice linter and to `gate.py`'s `stacks`, both of which need sentence boundaries |
| 7c | `dupes.py` | three paragraphs shipping twice, all from merges, all of which passed every other check |
| 7d | `copyedit.py` | an American book carrying British spellings to its last pass — *is this the same word we used last time*, which nothing else asked |
| 7e | `xref.py` | the index pointing three terms at `Ch 7 §2` after ch7's table moved, and a renamed move that would have vanished from the index on rebuild |

**All four report; none gates.** Each was narrowed at least once after a first run that was
mostly false positives — `ranking.py` 26→9, `copyedit.py` 47→8 then 8→0, `dupes.py` 34→0.
**A board that is mostly noise trains you to skim it**, and that lesson cost three rounds
today. Keep it.

## The two documents that govern the pass

- **`specs/SPEC_FINAL_PROOF_2026-08-07.md`** — what the pass is, the trade distinction
  between line edit / copyedit / proofread, and the nine-step per-chapter order. **§4 step 8
  is the pass**; steps 1–7 exist so step 8 is not spent catching what a regex could.
- **`specs/STYLE_SHEET.md`** — the book's memory. US spelling, straight apostrophes, serial
  comma (ruled 2026-08-07), the observed number practice, the compound-modifier rule, the
  naming-vs-instructing rule for moves *and* domains, the cast list, cross-reference format.

## What is left, in order

**1 · Appendix B and D need on-ramps.** `xref.py` reports both as shipping and pointed at
from nowhere. Wendell ruled they get them: *"we can find points in the text that pushes
people to the appendix B & D."* **B is the quests-and-campaigns workbook — the part the
reader is meant to actually run.** D is the emotional alchemy practices. Each wants a pointer
from the chapter whose work it continues. **This is the one remaining item that adds prose
rather than regularising it.**

**2 · The deep read, ch1 through ch9, one chapter per sitting.** This is the actual pass and
nothing built today substitutes for it. Every highest-value finding today came from Wendell
reading: *"Not x but y is sneaking in"* · *"the faces ARE altitudes"* · *"this should've
already been ruled on and changed."*

**3 · Then the true proofread**, on the built PDF rather than the markdown — page counts,
breaks, running heads, widows and orphans. Different job, different artifact.

## Two trivial rulings still open

`...` vs `…` (2 against 4), and `first-year` hyphenation (3 hyphenated, 2 open). Neither
blocks anything.

## Things a fresh session will not know and would waste time rediscovering

- **The six Faces ARE the integral altitudes** — Shaman/Magenta, Challenger/Red,
  Regent/Amber, Architect/Orange, Diplomat/Green, Sage/Teal, in chapter order. **The
  concealment is deliberate**: the ideal reader is Green and allergic to hierarchical
  language. A savvy reader is meant to find it; a regular reader has overcome the allergy by
  the time she does. **Do not name the ladder in the body.** The reveal already exists, in
  `ON_THE_SHOULDERS_OF`, sourcing ch8's Teal language to Laloux. I proposed writing *"a Face
  is not a level"* into ch1 and it was exactly backwards.
- **`ch9:348` and `ch9:352` will keep tripping `humor.py`** and must stay. They are the
  depression-well passage and the Captain Save-a-Kid admission — testimony, not jokes. ch9's
  ruling is *no butt*, not *no first person*.
- **Marginalia hands may spell British.** `copyedit.py` already exempts `>` blocks.
- **`Kit` is deliberately excluded from `agency.py`'s `ANIMATE` set** — `ch8:598` uses it as
  an object and admitting it would flip an agentless finding rather than suppress it.
- **Branch cleanup is blocked on tooling, not decisions.** `swmp78`, ~24 dead branches and
  `archive/swmp78-2026-08-01` are all safe to delete; the git proxy 403s on ref deletion and
  the GitHub MCP server has no delete-branch tool. **Needs the GitHub UI or a local clone.**

---

## The prompt

> Picking up the final proof of *Mastering the Game of Allyship* in
> `/home/user/mtgoa-manuscript`, branch `claude/book-pdf-epub-production-ybxa11`.
>
> **Read these three first, in order:** `specs/HANDOFF_FINAL_PROOF_2026-08-07.md`,
> `specs/SPEC_FINAL_PROOF_2026-08-07.md`, `specs/STYLE_SHEET.md`. The handoff has the
> context that will otherwise cost you an hour to rediscover — in particular that the six
> Faces are the integral altitudes and the concealment is deliberate, so **do not name the
> ladder in the body.**
>
> Then run `python3 instruments/review.py` and `python3 instruments/shipcheck.py` to see the
> board. Twelve steps; four of them (`ranking`, `dupes`, `copyedit`, `xref`) were built
> yesterday for this pass and report rather than gate.
>
> **Two jobs, in this order.**
>
> **First: Appendix B and D need on-ramps.** `xref.py` step 7e reports both as shipping with
> nothing in the manuscript pointing at them. Appendix B is the quests-and-campaigns
> workbook — the part the reader is meant to run — and D is the emotional alchemy practices.
> Find the right place in the chapter whose work each one continues, draft the pointer, run
> it through the `mtgoa-review` skill, and **show me the diff before applying it.**
>
> **Then: the deep read, ch1 first, one chapter per sitting.** Mechanical checks clear first
> so the read is a read. Batch the fixes per chapter and show the diff before applying.
> Nothing in the instruments substitutes for the read — every real finding yesterday came
> from a person reading.
>
> Standing rules: never show unreviewed prose · show the diff before any edit to prose
> already in the manuscript · record what happens in a doc.
