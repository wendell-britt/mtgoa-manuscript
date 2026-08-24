---
type: survey
title: "MTGOA Course — what already exists"
aliases:
  - course substrate survey
tags:
  - course
  - mtgoa
  - bars-engine
  - cyoa
created: 2026-08-21
review: 2026-08-25
source:
  - johnair01/bars-engine @ e5a62b9e
  - marketing/KICKSTARTER_UPDATE_2026-08-11.md
---

# The MTGOA course — what already exists

**Wendell, 2026-08-21:** *"create a handoff to creating a course for MTGOA based on the book…
this to be something that could ultimately replace the book… the stepping stone to actually
creating the game… deep planning and research on selfhosted digital courses CYOA adventure tech…
The BIG shift is that the course is actually going to make use of the effective allyship formula.
So this is where people will learn how to use their superpowers."*

**This is the survey, not the plan.** It exists because two of the plan's premises turned out to
be different from how they were described, and a handoff written on the wrong premises would cost
more than the day it saved. **Read §1 and §2 before anything gets designed.**

---

## 1 · The Effective Allyship Formula is real, and it is not in the book

**It lives in the engine.** `src/lib/technique-library/canonical-operations.ts:28`, id
`tech-allyship-formula`, tagged `moves: ['grow_up', 'show_up']` and attributed to the book:

> **The Effective Allyship Formula** — *"The book's master four-step procedure for doing allyship
> sustainably."*
>
> 1. **Identify your superpower.**
> 2. **Identify who needs that superpower.**
> 3. **Enroll allies to help you help those people.**
> 4. **Show up consistently.**

**The phrase does not appear anywhere in the manuscript.** Not in the nine chapters, not in the
eight appendices, not in the front or back matter, not in `specs/`, not in `decks/`. Searched
2026-08-21 against the shipping text.

**That is not a defect. It is the reason a course can replace the book.**

The book is organised as a **curriculum** — six Faces in altitude order, five moves, thirty game
moves, a hundred and twenty cards. It teaches a vocabulary. The Formula is organised as a
**campaign** — four steps a person runs, in order, ending in showing up for named people. It
sequences that vocabulary into an act.

| | the book | the Formula |
|---|---|---|
| ordered by | what there is to know | what the learner is doing |
| unit | chapter | step, with an artifact at the end of it |
| ends at | the reader knows the six Faces | somebody specific has been shown up for |
| Steps 1–2 draw on | ch3–ch8, the superpower quiz | |
| Step 3 draws on | the Connector, Appendix B, `enrollment` | |
| Step 4 draws on | Show Up, the Form, the deck | |

**So the course is not the book with videos.** It is the same material re-cut along the learner's
line of action rather than the author's line of instruction. **That reordering is the product.**

**One thing to rule before design starts:** the Formula's own source line calls it *"the book's
master procedure"* for a book that never names it. Either the phrase enters the book in a future
printing, or the course introduces it as the thing the book was building toward. **Both are
defensible; they are different products.** See §5.

## 2 · The CYOA and course tech is largely already built

**The research question is not what to build or buy. It is what the engine already does.**
`johnair01/bars-engine` at `e5a62b9e` carries, today:

**Authoring and runtime**

```
src/lib/cyoa/                types, blueprint-prompt-library, filter-choices,
                             build-contract, face-move-passages
src/lib/cyoa-build/          schemas
src/lib/cyoa-composer/       merge-overrides, branch-point-detection,
                             adaptive-resolver, checkpoint-persistence
src/lib/modular-cyoa-graph/  graph assembly
src/lib/onboarding-cyoa-generator/
src/app/cyoa/generate        an authoring surface
src/app/cyoa-intake/[id]     a player runner
```

**Persistence** — Prisma models already in the schema:

| model | what it holds |
|---|---|
| `Adventure` | slug, title, status, visibility, `startNodeId`, campaign refs |
| `AdventureTemplate` | `passageSlots`, `composerStepOverrides` — **a reusable course shape** |
| `PlayerAdventureProgress` | `currentNodeId` + `stateData`, unique per player+adventure — **resume** |
| `PlayerChapterProgress` | enter count, **`barCount`**, completed, per chapter |
| `MicroTwineModule` | `tweeSource` + `canonicalJson` + `htmlArtifact` — **Twine already interoperates** |
| `ThreadProgress`, `PackProgress`, `GrowthScene` | further progress and scene state |

**Access control** — `src/lib/book-access.ts` gates the `/handbook` reader on the `book-digital`
entitlement via `hasCapability`, with `FREE_CHAPTER_IDS` as the funnel. **So "course buyers get a
free copy of the book" is an entitlement grant, not a fulfilment problem.**

**And the book→interactive bridge is partly built.** `src/lib/cyoa/face-move-passages.ts` is a
6 Faces × moves grid, each cell carrying a passage, a BAR prompt, a BAR title and a blueprint key.
Its header already enforces the concealed architecture:

> *"The face is IMPLICIT — derived from the portal hexagram, never shown as face vocabulary to the
> player."*

**The single most important thing in that file is what a passage produces: a BAR.** The run does
not end in a score or a checkmark. It ends in an artifact the player wrote.

## 3 · The constraint that outranks every other design decision

**Chapter 9, and the Kickstarter update sent today, both say the same thing in public:**

> *"In 2020 I built a course on this material. Under ten percent of the people who started it
> finished. I did what I always do — doubled down, made more content, pushed harder — and burned
> out at the bottom of a depression well I hadn't noticed I was digging."*

**A second MTGOA course that gets a ten percent completion rate is not a neutral outcome.** It
falsifies the book's central claim in front of the people who bought the book. The failure is
load-bearing testimony now — it is quoted in the sales copy, the outreach pack and the speaking
pitch.

**The engine's artifact model is the answer already sitting there.** The 2020 course failed as
content to be consumed. A CYOA run that emits BARs is content that cannot be consumed passively —
there is nothing to complete except the thing you made. **Completion should be defined as
artifacts produced, not passages seen**, and `PlayerChapterProgress.barCount` is already the
field for it.

**So the metric goes in the design, not in the retro.** Whatever gets built states, before
launch, what completion means and what number would count as failure.

## 4 · What is actually missing

Against the Formula's four steps, here is the honest gap list. **Most of the tech exists; the
course-shaped composition of it does not.**

| Formula step | what exists | what is missing |
|---|---|---|
| 1 · Identify your superpower | the quiz, `SUPERPOWER_DEFS`, the result email, `face-move-passages`, the character sheet | nothing structural — **this step is nearly shippable today** |
| 2 · Identify who needs it | four domains, Appendix A, Appendix B quests, campaign models | the naming exercise itself: a surface where a learner names **actual people**, not categories |
| 3 · Enroll allies | the Connector chapter, `introductions.ts`, the consent gate technique | **the biggest gap.** Enrollment is a two-party act and every surface here is single-player |
| 4 · Show up consistently | BARs, the deck, quests, `ThreadProgress` | a cadence: something that returns, notices absence, and survives a missed week |

**Step 3 is the one to think hardest about**, because it is where the course stops being a course.
Enrolling an ally requires a second human. That is either the course's greatest asset — it is the
book's thesis enacted — or the wall that drops completion to ten percent again.

**And note what step 4 needs that no lesson platform provides:** a relationship with someone who
notices you stopped. That is the Dojo, or it is a cohort, or it is nothing.

## 5 · What only Wendell can rule

**Each of these changes the shape of the build, and none of them is a research question.**

1. **Does the Formula enter the book, or does the course introduce it?** §1. A future printing
   that names it makes the course the book's sequel; leaving it out makes the course the book's
   completion. Different promise to a reader who owns both.
2. **Is the course cohort-based, self-paced, or self-paced with a live floor?** This decides
   step 3 and step 4 entirely, and it is the difference between the 2020 failure mode and the
   Dojo.
3. **What is the price, and does the book come free with it or the other way round?** Today the
   Gumroad book is PWYW anchored at $15 and the deck is $22. A course that includes the book
   changes the whole ladder.
4. **What does completion mean, stated before launch?** §3. Artifacts produced is the candidate.
5. **How much of the game does the course have to be?** It is named as the stepping stone. The
   stepping stone can be a course that uses game tech, or a game that teaches — and the second
   one is much larger.

## 6 · What I could not check

- **The live site.** `masteringallyship.com` and `gumroad.com` are blocked by this environment's
  egress proxy, so everything above is read from the repository at `e5a62b9e`, not from
  production behaviour.
- **Whether the CYOA surfaces are actually running.** The code exists and the models exist. Which
  adventures are seeded, and whether anyone has completed one, is a database question this repo
  cannot answer.
- **The Obsidian vault.** `The Library/` is referenced by the repo and by
  `validate:launch-funnel`, which reports three of its documents as missing sources. Prior course
  thinking may already live there.
