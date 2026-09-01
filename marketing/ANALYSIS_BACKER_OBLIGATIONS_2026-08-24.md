---
type: analysis
title: "What the 361 backers actually bought"
aliases:
  - backer obligations
  - what backers bought
tags:
  - marketing
  - mtgoa
  - kickstarter
  - fulfilment
  - course
created: 2026-08-24
review: 2026-08-31
source:
  - "Drive: Mastering the Game of Allyship - All rewards - 2023-11-20 1930 UTC - easyship.csv"
---

# What the 361 backers actually bought

**Wendell, 2026-08-24:** *"My hypothesis is that many people don't want to read ebook and are
still waiting for the physical book."*

**Confirmed, and it is most of them.** Counted from the easyship reward export in Drive
(2023-11-20), 397 reward lines across 361 distinct backer numbers.

| | backers | |
|---|---|---|
| **Owed a printed book** | **247** | **68%** |
| Digital only, never bought print | 114 | 32% |

Physical counts anyone holding *Physical Edition of the Book*, *Physical Edition + Enamel Pin*,
*Course + Physical Book + Enamel Pin*, or *Group Coaching + All Prior Rewards*.

## What this does to the reading of the last week

**The slow ebook redemption is not a failure. It is the correct behaviour of the list.**

Two-thirds of these people did not buy an ebook. They bought a physical object, and the ebook is
a substitute being offered while they wait. **A backer who ignores a free ebook link is not
disengaged — they are waiting for the thing they paid for.**

So the diagnosis that #30 was built to settle — checkout versus deliverability — **had a third
answer neither branch allowed for**, and the most likely of the three. Redemption should be read
against the **114** digital backers, not against 371. Seven of 114 is 6%; seven of 371 is 1.9%.
**The same seven people are a different story depending on the denominator, and the denominator
was wrong.**

## The full obligation list, including two nobody has mentioned

| owed | backers | state |
|---|---|---|
| **Printed book** | **247** | manuscript print-ready, ~$6,000 unfunded |
| **Online course** | **53** | **being built right now in `bars-engine`** |
| **Audiobook** | **16** | **nothing in the repo. No plan, no file, no mention** |
| **Workbook** | **16** | **does not exist and has never been started** — see the correction below |
| Group coaching | 8 | inside *All Prior Rewards* |
| Enamel pin | 94+ | across three tiers |

**Two of these have never come up in any planning this session.**

**Correction, 2026-08-24.** This document first recorded the workbook as *"the 7.5×9.25in trim
builds at 395pp — a print product, same blocker."* **That is wrong, and it is a category error.**
Wendell: *"we actually have to create a workbook. The 'workbook' you're referring to is just the
books dimensions."*

`--trim=workbook` is a **wider-margin edition of the same nine chapters**, produced so a reader
can write in the gutter. **It is not a workbook.** Sixteen people bought a distinct product —
exercises, prompts, space to work — **and it has never been started.** Reading a build target as
a shipped product turned an unbuilt obligation into a solved one, which is the same failure shape
as reporting a code live when it was not redeemable.

**The audiobook is the sharper one.** Sixteen people paid for an audiobook in 2021. The build
pipeline makes a PDF and an EPUB and has never made audio. `build_book.py` does not know it
exists. **It is an undelivered promise with no owner, no plan and no line in any spec**, and it
has been invisible because nothing in the repository refers to it.

**The course one is an opportunity rather than a debt.** Fifty-three people already paid for a
course, three years ago, and a course is being authored this week. See below.

**Ruled 2026-08-24 — the audiobook has two candidate paths.** Wendell: *"either doing my own
audiobook or having an AI do the audiobook for me using my voice. We'd need to price out that
later option."* Costed in `marketing/ANALYSIS_AUDIOBOOK_2026-08-24.md`.

## The print-run number should be re-derived

#29 told 371 people:

> *"a run of 500 copies, plus freight, plus shipping to all of you, comes to roughly **$6,000**"*

**The obligation is 247 copies, not 371 and not 500.** A 500-copy run may still be right — short
runs price badly per unit, and stock for speaking events has its own value — but **the sentence
should say what it is buying.** *A run of 500 covers the 247 I owe and leaves stock to sell at
events* is a stronger and more honest version of the same ask, and it makes the $6,000 legible
instead of asking the reader to take it on faith.

**Re-check the quote against 247 before the next update repeats the number.**

## The 53 answer the course's hardest problem

`course/HANDOFF_COURSE_BUILD_2026-08-22.md` §0 established that the highest-leverage completion
intervention is a named accountability partner (85%), that self-paced with no social layer runs
5–15%, and that Wendell's 2020 course finished under ten percent.

**Fifty-three people have already paid for this course.** That is not a marketing list, it is a
cohort with a shared origin, a three-year wait, and a debt owed to them — and the completion
research says a cohort finishes at **64%** against **48%** for the same material self-paced.

**Ruled 2026-08-24 — the invitation waits.** Wendell: *"I'll invite the 53 after the 30 days of
the course is up."* So the cohort is not a launch lever for an unfinished course; it is what the
finished thirty days gets pointed at. **The thing to protect in the meantime is that the 53 are
not spent on a partial product.**

**So the course's first cohort does not need to be recruited. It needs to be invited.** It also
resolves, in the most concrete way available, the enrollment gap the handoff flagged as the thing
that decides whether the course works: **the live floor has 53 candidate members who already
belong to each other by history.**

**One caution.** They bought *"Online Course"* in 2021 — a course-shaped thing about being a
better ally. What is being built is the Formula's five modules on a thirty-day spine. Chapter 9
already tells the story of why the product changed, and #29 told it to all of them. **The
difference has to be named to this group specifically before they are invited**, not discovered
by them at the door.

## One number to settle

**This export says 361 distinct backers. The public copy says 371.** Neither is verified against
the Kickstarter dashboard, and the export is from 2023, so it may predate or exclude some
backers. **371 is in print in #29, #30 and the drafted Gumroad page.** Worth one look at the
dashboard so every future use of the number is the same number.

## What I could not check

- **Gumroad's current redemption count.** Egress is blocked to gumroad.com; the count has to be
  pulled by hand and read against **114**, not 371.
- **Whether any audiobook work exists outside this repo.** Nothing in `mtgoa-manuscript` refers
  to one. `The Library/` is unreachable from here and may know differently.
- **Whether the 2023 export is the final backer list.** It is the only per-backer reward data
  available to this session.
