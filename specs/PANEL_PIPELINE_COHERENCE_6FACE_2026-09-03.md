---
type: panel
title: "6 Game Master Analysis — the editorial pipeline, its coherence, and its portability"
aliases:
  - pipeline panel
  - coherence panel
  - six faces pipeline
created: 2026-09-03
review: 2026-09-10
source:
  - specs/EDITORIAL_PIPELINE_COHERENCE_2026-09-03.md
  - specs/PANEL_WHAT_NEXT_6FACE_2026-09-01.md
  - specs/REDTEAM_WRITE_WITHOUT_THESE_ISSUES_2026-09-02.md
---

# 6 Game Master Analysis — the pipeline, checked and made to travel

**Wendell, 2026-09-03:** *"Let's get a 6 game master analysis of this question"* — the question
being the one this thread has lived in: **how to check the editorial pipeline is coherent and
consistent, and use it across every project he writes.**

**The state, so the panel rules on facts rather than on mood.** This session built, in order:
`light_verb.py` (the red-team's buildable half), `coherence.py` (the pipeline's self-check),
`editorial.yaml` (the per-project profile), and the refactor that made `gate.py`, `telling.py`,
`trailing_and.py` and `light_verb.py` read that profile. The pipeline now runs ~13 prose
instruments, an orchestration, a manifest, and a self-check wired as book step 9. All of it is
committed and pushed to `claude/book-pdf-epub-production-ybxa11`.

**The last recorded backer ledger (from the 2026-09-01 panel, two days old):** 361 backers
waiting since 2023; 247 owed a printed book, ~$6,000 unfunded; four outreach sends that gate that
$6,000 three weeks overdue; update #31 drafted since 2026-08-22 and unsent; `/book` and `/course`
still 404, and the PDF prints `/book` on 373 pages. **The panel does not assume these are
unchanged; it flags that nothing this session touched them.**

| | Question |
|---|---|
| **Q1** | Was building the coherence-and-portability system the right work this session? |
| **Q2** | Is the manifest the right design, or gold-plating a tool with one user and one book? |
| **Q3** | *"Multiple projects"* — a real, imminent need, or a someday that justified building now? |
| **Q4** | How much editorial infrastructure is enough? Where is the stop line? |
| **Q5** | How does this system rot or mislead, and does the self-check actually prevent it? |
| **Q6** | Does the pipeline integrate into the editorial operating system, or is it another practice with no call site? |

---

## SHAMAN · the Body — *What to Do With What You Feel*

**Read the field before the plan. What is actually happening in the author's body?**

**Relief, and it is honest relief.** The pipeline work came from a real wound: draft after draft
passed every instrument and Wendell's eye still caught the telling, the dead verb, the defect one
layer deeper. *"There must be a way to write without these issues."* Building `coherence.py` and
the manifest is what the hands do when the felt problem is *the rules keep slipping* — you make
the rules hold still. That is not nothing. **The frustration was real and the build answers it.**

**It is also the tractable job again.** The Shaman said it two days ago and will not unsay it:
when the debt is too big to face in one movement, the hands go to the one small completable
job. A coherence checker completes. It passes green. It gives the exact hit of mastery that
247 unshipped books withhold. **Both are true — the wound is real and the work is also a place to
stand that is not the debt.**

**Shaman's ruling:** Q1 — the work was real, not procrastination, but notice the body chose the
completable one again. The tell is that it felt *good* to finish, and shipping the book will not
feel good, it will feel like exposure.

---

## CHALLENGER · the Line — *Who Pays When Nobody Says No*

**The unwelcome part, out loud: this is the third straight session inside the instruments, and
the manifest serves a project that does not exist.**

Two days ago the Challenger's line was *no more instruments until the four sends go out.* Since
then: a red-team, a light-verb detector, a coherence checker, a manifest refactor. **All of it
real work. None of it a send, a dollar, or a book in a hand.** The four outreach emails that gate
the $6,000 were three weeks overdue at the last panel. They are now three weeks and two days.

**On Q3 — *"use it on multiple projects"* is the exact shape of premature.** It is a reason to
build infrastructure now for a need that has not arrived. There is no second manuscript in
production. *Allyship at Work* is unstarted by the author's own ruling. **A portability layer for
one project is a bridge to an island nobody lives on yet**, and the Challenger has seen this
move: the most defensible way to keep building is to build for a future that always needs one
more tool first.

**On Q4 — the stop line was three commits ago.** `coherence.py` catching the 749/302 drift was
the last build that paid for itself. Everything after — the manifest, the four refactored
instruments, the negative test — is quality the reader will never feel.

**Challenger's ruling:** Q1 — no, or at least: enough. Q3 — the second project is a hypothesis,
not a customer. Send the four before the next instrument.

---

## REGENT · the Inheritance — *What You Inherited, and What You Do With It*

**What was inherited is a pile of tools that already runs on memory.** Seventeen panels, a
hundred-plus instrument files, four editorial roles that map to no Face. The 2026-09-01 panel
found the six Faces themselves have no call site. **This session's work is, unusually, the
Regent's kind of move**: `coherence.py` makes the inherited pile *transmissible* — it is the
damage report and the working method in the same hand, which is the Regent's whole test for
whether an inheritance is being passed well.

**On Q2 — the manifest is a genuine inheritance repair.** The baselines lived in three Python
constants and the banned list inside `gate.py`; a person inheriting this could not find them.
Pulling them into one declared file is exactly *make the inheritance receivable*. That earns its
place.

**On Q3 — but a second obligation is being inherited before the first is discharged.** The
Kickstarter promised one book to 361 people. *"Anything I'm writing must follow these rules"*
commits the author, without saying so, to a standard across a body of future work while the founding promise
sits open. **The Regent has seen where that goes: it produced the three-year silence.** Building
the system that governs the next four projects is a way of already living in them.

**Regent's ruling:** Q2 — the manifest is honest inheritance work, keep it. Q3 — do not build
the second project's governance until the first project's debt has a payment plan with a date.

---

## ARCHITECT · the Design — *Fixing the Condition Instead of the Person*

**The condition, plainly: the pipeline was coherent by luck, and luck is not a design.** Every
wired step happened to resolve, every baseline happened to match, and nothing enforced any of it.
`coherence.py` fixes the condition rather than the person — it makes the next edit safe by
construction instead of by carefulness. **That is the correct move and it is cheap, an afternoon,
and it already caught a real defect.** The Architect signs it.

**On Q2 — the manifest is right design and the Architect will defend it against the Challenger.**
One source of truth for the profile, read by the instruments and validated by the self-check, is
not gold-plating; it is the difference between a tool and a script. The negative test proving the
checks bite is what separates a real check from a comment. **This is the cheapest correct version
of it.**

**On Q4 — and the Architect draws the stop line the Challenger wants, for a structural reason.**
The manifest carries *data that varies*. `review.py`'s step sequence is *control flow* and was
correctly left in Python. **The next builds — the submodule, the pip package, extending
`coherence` to every instrument — are all speculative until a second project exists to force
them.** Building them now optimizes a bottleneck that is not the bottleneck. The Architect's own
law: which single build discharges the most obligation. `coherence.py` discharges *zero* backer
obligations. It only pays if tool-building is the constraint, and it is not.

**Architect's ruling:** Q2 — right design, keep it. Q4 — the stop line is here: no distribution
layer until a second project is real. Q1 — the coherence check was worth it; the portability
work was correct but optional, and optional was the wrong tier this month.

---

## DIPLOMAT · the Table — *Why Being Good at Care Is Only Half of It*

**Who is at this table, and who does the pipeline serve?**

**On Q1 and Q3 — the manifest's beneficiary is a reader who does not exist yet.** The people at
the table are 361 backers. None of them is served by a coherence checker. The reader who *is*
served by the portability layer is the reader of the next project — a project with no
manuscript, no backers, no date. **Care aimed at a future table is still care, but it is not care
for the people already seated**, and the book is unambiguous that you cannot pay one table's debt
with attention to another.

**The half that is real:** the *prose* instruments — telling, light-verb — do reach the current
reader. The passage Wendell keeps rewriting is for the 247. So the pipeline is not all
future-facing; its output lands on the page the backer will hold. **The split is between the
instruments (serve the current reader) and the meta-work — coherence, manifest, portability
(serve a future one).** This session was mostly the second kind.

**On Q6 — the one move the Diplomat will credit without reservation:** `coherence.py` is wired
as step 9. Unlike the six Faces, unlike the seventeen panels, **it has a call site.** It will run
whether or not anyone remembers it. That is the book's own doctrine finally applied to the
system that makes the book.

**Diplomat's ruling:** Q1 — the instruments serve the table; the meta-work served the next one.
Q6 — the call site is the plainly good news; the pipeline fixed for itself the exact defect the
last panel named in the Faces.

---

## SAGE · the Board — *Seeing the Whole Board Without Leaving the Table*

**The board has three tracks, and this session ran on the one that gates nothing.**

The 2026-09-01 panel named two: the fulfilment track (proof → print → the 247), gated on money,
and the money track (four sends → engagements → $6,000), gated on nothing. **This session was
neither. It was a third track — tooling — and tooling gates a product only when it sits on that
product's critical path.** The coherence checker does not sit on the book's path; the book was
already print-ready at 387 pages before any of this existed.

**On Q4 — the Sage's rule for tooling: it is legitimate exactly when it is the constraint on
something shipping.** The telling and light-verb detectors *were* on the book's path — they
change the prose the backer reads, and Wendell's own eye proved the defect was shipping. The
coherence checker and the manifest are one level removed: they make the tools cheaper to
maintain, which is only the constraint if tool-maintenance is what is stopping a shipment. **On
this board, nothing ships or fails to ship because of pipeline coherence.**

**On Q3 — the multi-project framing is the tell.** *"Anything I'm writing must follow these
rules"* is a true and good intention, and it is also how the board's centre of gravity shifts
from *finish this* to *build the system that finishes everything*. **The Sage has watched that
shift eat three years.** The rules are worth having. They do not need to be portable until there
is a second project to port them to, and that project is not on the board.

**On Q1 — and the Sage will not pretend the session was worthless.** The light-verb detector
closed the red-team's one buildable recommendation, and the coherence checker caught a live drift
the moment it ran. **The critique is not that the work was bad. It is that the board has an
unblocked money track that has not moved in three weeks, and the week went to the one track that
blocks nothing.**

**Sage's ruling:** three tracks, and the session ran on the only one with no gate below it. The
money track still has no gate and still has not moved.

---

## Where the six converge, and where they do not

**Unanimous:** `coherence.py` was worth building. It fixes a real condition (coherence by luck),
it is cheap, it caught the 749/302 drift on its first run, and — the Diplomat's point — it gave
the pipeline the call site the six Faces still lack. **Nobody on the panel wants it removed.**

**Five to one:** the portability work was premature. The Architect, Challenger, Regent, Diplomat
and Sage all land on *right design, wrong tier this month* — the manifest is cheap and honest and
the distribution layer beyond it is speculative until a second project exists. **Only the
Architect defends the manifest itself without reservation**, and even the Architect draws the
stop line at the distribution layer.

**The real split, worth reading rather than averaging:** the Challenger says the multi-project
need is a hypothesis; the Regent and the Architect say the need is real (Wendell does write
across surfaces — the course, the episodes, the marketing, the next book) but the *timing* is
wrong. **They agree the manifest should exist and disagree on whether building it now was
discipline or avoidance.** The honest reading: it was both, and it was cheap enough that the cost
is not the manifest — it is the four sends the week did not contain.

**The question the panel raises that Wendell did not ask:** *what reached a backer this session?*
Nothing did. Six Faces convened on the coherence of the tool, and the tool's whole purpose is a
book that is still not in a hand. **That is usually the sign the panel found the real one.**

## The order the panel produces

1. **Keep `coherence.py` and the manifest exactly as built.** They are done, cheap, and correct.
   Do not extend them — no submodule, no pip package, no coherence-for-every-instrument — until a
   second project is actually in production.
2. **Send the four outreach emails.** Still the highest-leverage unblocked act on the board;
   gates the $6,000; now three weeks and two days overdue.
3. **Post update #31.** Drafted since 2026-08-22. The silence is the injury, per `ch7:726`.
4. **Stand up `/book` and `/course`** as one static page. The PDF prints `/book` on 373 pages
   against a 404.
5. **When the pipeline calls again, gate it on the book's path.** Build a prose instrument (it
   reaches the reader); defer meta-work (it reaches the next project) until the next project
   exists.

**The one caution, which is the same as last time.** The tools are good. They are also the most
comfortable corner in the house, and the panel has now twice found the author in it while the door
to the money track stands open and unused.
