---
type: handoff
title: "MTGOA Course — build handoff"
aliases:
  - course handoff
tags:
  - course
  - mtgoa
  - bars-engine
  - handoff
created: 2026-08-18
review: 2026-08-25
source:
  - course/SURVEY_SUBSTRATE_2026-08-18.md
  - course/RULING_FORMULA_FIVE_STEPS_2026-08-18.md
---

# MTGOA Course — build handoff

**Open this in a session whose repo is `johnair01/bars-engine`.** A manuscript session can read
that repo but cannot push to it — `add_repo` refuses a cross-owner add — so anything written here
crosses as a patch. Two already have: `specs/patches/0001` and `0002`, both applied.

**Read first:** `course/SURVEY_SUBSTRATE_2026-08-18.md` (what already exists) and
`course/RULING_FORMULA_FIVE_STEPS_2026-08-18.md` (the Formula, ruled to five steps).

---

## 0 · The one thing to understand before designing anything

**The course's own curriculum is its completion mechanism.** That is not a slogan; it is the
finding that should shape every build decision below.

The evidence on why online courses fail is unusually consistent, and it lands exactly on this
project's history:

| intervention | completion |
|---|---|
| self-paced, no social layer | **5–15%** |
| self-paced vs cohort, same platform (Ruzuku) | **48.2% → 64.2%** |
| discussion features present | **43% → 65%** |
| **a named accountability partner** | **85% — the highest of any single intervention** |

**Wendell's 2020 course finished under ten percent.** That is not an outlier or a personal
failing. It is the median outcome for a self-paced content course with no accountability layer,
and it is quoted in Chapter 9, the Kickstarter update sent 2026-08-18, and the speaking pitch.

**Now read step 4 of the Formula: *enroll allies to help you help those people.*** The single
highest-leverage completion intervention known — a named human who expects something of you — is
the same act the course exists to teach. **Module 4 is simultaneously the curriculum and the
retention mechanism.** Build it as one, and the course proves its own thesis by working. Build it
as two, and it fails in the way the book already confessed to.

**So the design rule for everything below: a learner should never be alone at the point the
Formula says to stop being alone.**

## 1 · The Formula, ruled

| # | step | move | module ends when the learner has |
|---|---|---|---|
| 1 | Identify your superpower. | Wake Up | their Face named, and the one they avoid |
| 2 | Identify who needs that superpower. | Open Up | **actual people named**, not categories |
| 3 | Work through what blocks you from using it. | Clean Up | one real block worked, by 3-2-1 or a channel pass |
| 4 | Enroll allies to help you help those people. | Grow Up | **one real ask made of one real person** |
| 5 | Show up consistently. | Show Up | a cadence that survived a missed week |

**Five steps, five moves, one artifact each.** The Formula is the Five-Move Form at campaign
scale — see the ruling for the mapping and why step 3 was always missing.

**Ruled by Wendell 2026-08-18:** the Formula enters the book in a later printing · the course is
self-paced **and** live, running the same material · **self-paced learners get a path into the
live floor.**

## 2 · Do not adopt a course platform, and do not adopt a narrative engine

**Both were researched. Both come back the same way: you already own the substrate.**

**On LMS platforms** — LearnHouse (Next.js + FastAPI + Postgres, self-hostable) and CourseLit
(Next.js) are the credible open-source options, alongside Moodle and Open edX at the heavyweight
end. **Adopting any of them means a second identity model, a second progress store and a second
entitlement system** beside the ones `bars-engine` already runs. The things an LMS would give you
that the engine lacks — cohort scheduling, drip, a discussion surface — are small builds on top of
existing models, not reasons to run two systems.

**On narrative engines** — Twine is the browser-native standard for branching fiction and **you
already interoperate with it**: `MicroTwineModule` stores `tweeSource` alongside `canonicalJson`
and an `htmlArtifact`. Ink is the stronger long-term tool where state gets heavy, and Yarn Spinner
is a Unity-first dialogue system. **None of the three is worth adopting for the course**, because
`cyoa-composer/` already does branch-point detection, adaptive resolution and checkpoint
persistence against your own data model.

**The one place this decision comes back:** the course is named as the stepping stone to the game.
**If the game turns out to need heavy narrative state, Ink is the tool to reconsider** — and the
Twine interop already in the schema is the migration path. Note it; do not act on it now.

## 3 · The gap, honestly

| step | exists | missing |
|---|---|---|
| 1 · superpower | quiz, `SUPERPOWER_DEFS`, result email (`0001`), character sheet, `face-move-passages` | **nothing structural** |
| 2 · who needs it | four domains, Appendix A, Appendix B quests, campaign models | a surface where a learner names **people**, and it persists |
| 3 · blocks | Appendices C/D/E, `emotional-first-aid`, alchemy engine, 3-2-1 | the guided pass, and somewhere for the artifact to land |
| 4 · enroll | `introductions.ts`, the consent gate technique | **the whole two-party act.** Every surface today is single-player |
| 5 · show up | BARs, deck, `ThreadProgress`, `PlayerChapterProgress.barCount` | a cadence that notices absence |

**Plus two cross-cutting builds the rulings created:**

- **Cohort scheduling and a live floor.** Sessions, a roster, attendance. No model exists.
- **The path from self-paced into the live floor at module 4.** Ruled to exist. It is a join, an
  invitation, or a scheduled drop-in — undesigned.

## 4 · What to build first, and it is small

**This repo's own backlog warns that it *"generates specs faster than it ships surfaces"* — twenty
documents on 2026-08-10, zero shipped artifacts. So the first slice is deliberately one module.**

**Ship module 1 end to end before designing modules 2–5.**

It is the module that is nearly done: the quiz exists, the result email now sends, the character
sheet exists, `face-move-passages` already maps Face × move, and `PlayerChapterProgress` already
counts artifacts. **What is missing is the wrapper that makes those a module** — an entry, an
ordered path, a persisted artifact, and a visible end.

```
[ ] 1. Seed one Adventure with adventureType = 'course-module', slug 'formula-1-superpower'
[ ] 2. Author its passages against AdventureTemplate.passageSlots
[ ] 3. Entry: the quiz result becomes the module's opening state rather than a dead end
[ ] 4. Artifact: the run emits a BAR — the Face named, the avoided Face named, one sentence
       on where each shows up. PlayerAdventureProgress.stateData already carries the ledger
[ ] 5. End: a visible completion that says what was produced, not what was watched
[ ] 6. Entitlement: grant `book-digital` on course purchase — book-access.ts already gates on it,
       so the free-book promise is a capability grant and needs no fulfilment path
[ ] 7. Instrument it: completion = artifacts produced. Record the number before launch
```

**Then, and only then**, module 4 — because it is the hard one and the one that decides whether
this works. Modules 2, 3 and 5 are comparatively ordinary once 1 and 4 are real.

## 5 · Design constraints that are not negotiable

1. **Completion means artifacts produced, not passages seen.** State the number before launch.
   `PlayerChapterProgress.barCount` is the field. A course that reports completion as
   pages-viewed is measuring the thing that failed in 2020.
2. **Never show Face vocabulary as hierarchy.** `face-move-passages.ts` already enforces this:
   *"the face is IMPLICIT — derived from the portal hexagram, never shown as face vocabulary to
   the player."* The six Faces are the integral altitudes and the concealment is deliberate.
3. **The two versions are one curriculum.** Live is a facilitation layer over the same five
   modules. Anything authored only for live is content the self-paced learner is missing.
4. **The 371 backers were promised no funnel.** `list-contract.ts` enforces it as a data
   structure. A course launch sequence has to respect that exclusion, in code, not in intent.
5. **No apology sentences, no funnel mechanics.** `MTGOA_Copy_Strategy_Spec` §5 and the
   `IDEAL_READER_MATRIX` "what loses her" column govern course copy exactly as they govern the
   book's.

## 6 · The canon patch that goes with this

`src/lib/technique-library/canonical-operations.ts`, `tech-allyship-formula`:

- add step 3, **"Work through what blocks you from using it."**
- widen `moves` from `['grow_up', 'show_up']` to all five
- fix `essence` — it says *"the book's master four-step procedure"* for a book that does not yet
  name it, and the count is now wrong as well

**Small, and it should go across before anything is authored against the old four steps.**

## 7 · Still Wendell's to decide

- **Price, and which product carries which.** Book is PWYW anchored at $15, deck is $22. A course
  that includes the book reorders the whole ladder.
- **How much of the game the stepping stone has to be.** A course using game tech and a game that
  teaches are different sizes of build.
- **What the live floor is** — the Dojo, a cohort with a start date, or a standing weekly room.
  §3's scheduling build depends on the answer.

## 8 · What could not be checked

- **The live site and production data.** `masteringallyship.com` and `gumroad.com` are blocked by
  the manuscript session's egress proxy. Which adventures are seeded, and whether anyone has
  completed a CYOA run, are database questions this repo cannot answer.
- **`The Library/`.** Referenced by the repo and by `validate:launch-funnel`, which reports three
  of its documents as missing sources. Prior course thinking may already live there.

---

## Sources

- [Online Course Completion Statistics 2026](https://www.skillademia.com/statistics/online-course-completion-statistics/)
- [Cohort vs Self-Paced Courses: Completion & Pricing Data (2026) — Ruzuku](https://www.ruzuku.com/learn/articles/cohort-vs-self-paced)
- [Course Completion Rate Benchmarks — Ruzuku](https://www.ruzuku.com/learn/articles/course-completion-rates)
- [Improve Student Success With Cohort-based Courses — Teachable](https://www.teachable.com/blog/improve-student-success)
- [Teachable Alternatives: Self-Hosted LMS for Course Creators 2026](https://thefrontkit.com/blogs/teachable-alternatives-self-hosted-lms-2026)
- [Best Open Source LMS in 2026](https://raccoongang.com/blog/open-source-lms-everything-you-need-know/)
- [Authoring interactive narrative in Twine 2 vs Ink vs Yarn](https://medium.com/@haikus_by_KN/authoring-interactive-narrative-in-twine-2-vs-ink-a-quick-and-dirty-comparison-using-examples-e695eb4dfc3e)
- [Twine vs Yarn Spinner vs Ink vs NarrativeFlow](https://narrativeflow.dev/blog/twine-vs-yarn-spinner-vs-ink-vs-narrativeflow-which-branching-dialogue-tool-is-right-for-your-game/)
