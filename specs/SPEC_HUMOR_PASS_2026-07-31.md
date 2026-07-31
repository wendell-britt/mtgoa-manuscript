# SPEC — The humor pass

**Branch:** `claude/edit-humor-pass`. One editorial concern, per DL-18.
Diagnosis only. Nothing applied.

**Why this exists.** Wendell, 2026-07-31: *"I don't think our comedy pass has
made it into our editorial passes."* Correct — and the reason turned out to be
more interesting than an oversight.

---

## 1 · The finding

`marginalia/specs/HUMOR_GRID.md` is a complete, ruled comedy architecture:
three archetypes at three scales, a per-chapter distribution policy Wendell
decided on 2026-07-28 with its risks named, and **nineteen drafted jokes, one per
cell, ch2 through ch9.**

**None of the nineteen is in the manuscript.** Measured by direct quote search on
45-character fragments, no regex judgment involved: **0 of 19.**

One was adapted rather than dropped. `ch4:597` carries the Ch4 Clown, rewritten,
**and the rewrite is better than the spec's version**:

> *I killed an idea once in the first ten seconds and called it discernment. It
> was a good call. It has been a good call every time since, which is the part I
> would ask you to sit with, because a thing that is right every time is not
> being tested.*

The spec's draft stopped at *"…which had the additional benefit that I never had
to find out."* The book's version turns the joke into an instrument. **That is
the grid working exactly as designed — and it happened once, in the margin.**

## 2 · The structural consequence, which is the real finding

This is not *"the book needs nineteen jokes."* The grid's own argument is that
the distribution is **a book-length setup with a payoff**:

> **The Jerk-heavy middle is loading the spring. Ch7 releases it.**
>
> The absence in Ch7 only lands because of the abundance before it. Three
> chapters of comfortable laughing at other people's daemons builds a habit; Ch7
> removes the target and leaves her standing there alone… **The Ch7 withdrawal is
> what retroactively earns Ch4 through Ch6.**

Measured, `instruments/humor.py`:

| | ch4 | ch5 | ch6 | ch7 |
|---|---|---|---|---|
| policy | Jerk **heavy** | Jerk **heavy** | Jerk **heavy** | Jerk **NONE** |
| found | 0 | 0 | 0 | 0 |

**ch7's ruling holds, and holds vacuously.** The withdrawal is present because
nothing was ever there to withdraw. **The spring was never loaded**, so ch7's
discipline reads as an absence nobody notices rather than as the payoff it was
designed to be — and the book gets no credit for the one piece of comic restraint
it deliberately ruled.

The grid also names the condition that makes the setup legitimate:

> If the middle chapters feed her developmental superiority and it never turns,
> the book has confirmed the exact shadow it exists to treat.

**That risk is currently zero, for the same reason.** Nothing was fed, so nothing
needs turning. The architecture is neither working nor doing harm; it is absent.

## 3 · What the book is actually doing instead

**The book is funny. It is funny in a different register than the grid.**

Its humor is **Clown and Cult Leader, in Wendell's own voice**, and the best
instance is now anchor 3 in `specs/VOICE_ANCHOR.md`:

> `ch4:115` — *(The workshops teach the scripts. The scripts do not work the way
> the workshops promise, which anyone who has run one in a live moment already
> knows.)* … The village learned to make its nos sound like yeses because yeses
> cost less.

That is a Cult Leader joke — *us*, the village, a process running unattended —
and it was invented for the book rather than taken from the grid.

**What is missing is specifically the Jerk**: third person, someone else's daemon,
the archetype the ch7 payoff depends on. The book instinctively wrote the two
archetypes that point at *me* and *us*, and skipped the one that points at *you*.

That is a defensible instinct rather than a failure. Mocking a third party is the
riskiest of the three, and `HUMOR_GRID` says so itself — Amber contempt in ch5,
Magenta proximity in ch3. **The book avoided the risk and lost the payoff with
it.** That trade is Wendell's to rule on, and it has never been stated as a trade
before.

## 4 · The instrument, and what it cannot do

`instruments/humor.py` — distribution by chapter against the ruled policy.

```
python3 instruments/humor.py          # the table
python3 instruments/humor.py -v       # with specimen lines
```

**Read the limitation before quoting the table.** Its patterns were derived from
the grid's own nineteen specimens, so it answers *did the drafted jokes land*
well and *is this book funny* badly. It missed `ch4:115` on a case-sensitivity
bug, and would have missed it anyway had the phrasing differed. **A zero means
"no grid-shaped joke here", never "nothing funny here."**

The number that needs no instrument is the specimen count: **0 of 19.**

## 5 · Rulings needed

1. **Is the Jerk worth building?** It is the archetype the ch7 payoff depends on
   and the riskiest to write. Three options: build it in ch4–ch6 and earn ch7;
   drop the ch7 ruling and let the book be Clown-and-Cult-Leader throughout; or
   keep both as a second-edition project with the grid already written.
2. **Where do the nineteen live?** They are good, they are ruled, and they are in
   a spec file no reader sees. Second edition, or a companion?
3. **Does `ch4:597` set the pattern?** One adapted specimen, in the margin,
   improved on the way in. If the margin is where the grid's jokes belong, that
   is a smaller and much cheaper job than nineteen body insertions.

## 6 · Recommendation

**Do not add jokes before ship.** Nineteen insertions of new comic prose the
night before delivery is the highest-variance work available, and comedy is the
one register where a miss is worse than an absence.

**Rule 3 first.** If the grid's jokes belong in the marginalia — which `ch4:597`
suggests, and which fits the frame, since the annotator is already the book's
driest voice — then the whole architecture becomes an insertions job in
`marginalia/insertions.py` rather than nine chapters of body prose. That is a
second-edition project with a written spec and one worked example, which is a
good place for it to be.
