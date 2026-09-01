---
type: readnotes
title: "Proof read-notes for v2 — Wendell's highlighter flags, located and diagnosed"
aliases:
  - proof read notes
  - v2 intake
  - highlighter flags
tags:
  - editorial
  - mtgoa
  - v2
  - proof
created: 2026-09-01
review: 2026-09-08
source:
  - manuscript/ch1.md
  - specs/RESEARCH_TRAILING_AND_2026-09-01.md
---

# Proof read-notes for v2

**Wendell is reading the physical proof with a highlighter, one chapter at a time, marking
"things that have problems with them from a gut check."** A highlight is a symptom report, not a
diagnosis. The job here is to name what the gut is reacting to on each span, then propose a fix.

**Nothing in this file is applied.** Every proposed fix is a draft for approval. The manuscript
is untouched. Applied only per Wendell's call, span by span.

**Proof is in sync with the manuscript.** `ch1.md` last changed 2026-08-13, before the proof was
built, so every flag is live and none is already addressed.

---

## Chapter 1 — "The Infinite Arcade", pages 12–13 (ch1.md 143–167)

### The two threads, because the ten flags are not ten unrelated problems

**Thread A — the metaphor loses discipline in this stretch.** The chapter runs on one picture:
the arcade — floor, tokens, machines, prize counter, bouncers. In this tail, new metaphors arrive
cold or clash with each other, and half the flags are the reader asking *which picture am I in?*

**Thread B — the trailing *and*, and it is measured.** This 25-sentence stretch runs **24.1%**
trailing coordination against the book's **13.9%** baseline — nearly double, and `trailing_and.py`
marks it HEAVY. **Six of the ten flags sit on the construction.** The gut caught the passage the
instrument would have.

**A third, softer, and bigger than a line fix.** The "owners" turn at 163–165 shifts register
from concrete arcade prose into abstract political-economy — *arrangement*, *dividend*, *collect*,
*budget line*. Three flags land there. That may be a structural question rather than a line one.

### The ledger

| # | line | highlighted span | what the gut caught | move | status |
|---|---|---|---|---|---|
| 1 | 143 | *…and that difference runs the whole economy.* | **"the economy" arrives cold** — first use, no economy established yet — and a big claim buried in a trailing-*and* clause | cut the grand clause, let the concrete sentences after it carry the point | **proposed** |
| 2 | 147 | *The shortcut works, which is the honest problem with it. It just pays nothing.* | a staged paradox — works / is the problem / pays nothing — that takes three beats to reconcile; *"the honest problem"* reads as a flex | linearise the logic | **proposed, low confidence** |
| 3 | 149 | *A door like that changes the question.* | **"a door like that" points at no door** — the prior sentence was a *diagram*, and the door was 8 lines back at 139. Classic say-the-noun handwave | name the door — the fast, shape-matching gate from 139 | **proposed** |
| 4 | 149 | *…asks for far more, and it needs a history behind it before it lands at all.* | trailing-*and*, a three-*it* stack, all abstract, and it defers to Chapter 7 mid-thought | split, concrete the verbs, decide if the ch7 preview stays | **needs your read** |
| 5 | 153 | *They are holding lines, drawn long ago by parts of them they have never met.* | **two metaphors at once** — *line* = a defended boundary, *parts of them* = internal parts — and *line* here clashes with *line* = queue at 167 | either it is too dense, or it is a keeper and you flagged the clash. **Which?** | **needs your read** |
| 6 | 155 | *…and praise has a shape to it. Somebody stands above you and grades you.* | *"has a shape to it"* is vague setup delaying the concrete image; trailing-*and* on *"was praise, and praise has a shape"* | cut the setup, lead with the shape | **proposed** |
| 7 | 157 | *That is the test, and you can run it on anything anybody hands you.* | trailing-*and* softening a line that should land hard | split it | **proposed** |
| 8 | 163 | *…Those are the owners, and keeping that shelf stocked is how they collect.* | the register shift into systems-critique; *"how they collect"* is the most compressed clause in it; trailing-*and* | line fix is easy; the real question is whether the abstract turn belongs at the chapter's close | **needs your read** |
| 9 | 165 | *Call it the fluency dividend: what an arrangement earns every hour you spend getting better at describing it.* | coined term + colon-definition + *"an arrangement earns"* (agency on an abstraction). Same abstract register as 8 | keep the coinage, or cut it for the plain version | **needs your read** |
| 10 | 167 | *…anybody who tells you they have is selling you a better place in the same line.* | **"the same line" (a queue) collides with "holding lines" (a boundary) at 153**; trailing-*and* on *"worked that out, and…"* | the queue reading is well-grounded in the prize-counter; the clash resolves by fixing 5, not this. Linked to 5 | **linked to 5** |

### The proposed fixes, spelled out

**All drafts. None applied. Each keeps the staccato and the second person; the point is to give
the reader one picture at a time and stop softening the hard landings.**

**#3 · 149 — the clearest.**
> was: *A door like that changes the question.*
> now: **A door that reads you before you speak changes the question.**

Names which door — 139's *"it checks you against the shape, before anybody has said much."*

**#6 · 155.**
> was: *What I collected there for years was praise, and praise has a shape to it. Somebody stands above you and grades you.*
> now: **What I collected there for years was praise. Praise has a shape: somebody stands above you and grades you.**

Splits the trailing-*and*; the colon delivers the shape the first clause promised, so the vague *"has a shape to it"* is gone.

**#7 · 157.**
> was: *That is the test, and you can run it on anything anybody hands you.*
> now: **That is the test. You can run it on anything anybody hands you.**

**#1 · 143.**
> was: *The first two you do. The third you are, and that difference runs the whole economy.*
> now: **The first two you do. The third you are. Doing leaves a record somebody else can check.**

Cuts *"and that difference runs the whole economy"* — the grand claim the following sentences already prove. Alternate, if you want a landing rather than a cut: *"The third you are, and that difference is the one this whole chapter turns on."*

**#2 · 147 — low confidence, offered lightly.**
> was: *The shortcut works, which is the honest problem with it. It just pays nothing.*
> now: **The shortcut works. That is the temptation. It pays nothing.**

Makes the logic linear instead of a paradox to decode. If the paradox was the point, leave it.

### The three that need your read before I draft

- **#5 (holding lines)** and **#9 (fluency dividend)** are among the strongest lines on the
  page. A gut can flag a strong line for two opposite reasons — *too opaque* or *showing off* —
  and I cannot tell which from the mark. Which is it?
- **#8 / #9 together** are the abstract "owners" turn. If the flag is *this got too abstract for
  the end of Chapter 1*, that is a structure call, not a line fix, and it wants the Book
  Architect rather than a rewrite of two clauses.
