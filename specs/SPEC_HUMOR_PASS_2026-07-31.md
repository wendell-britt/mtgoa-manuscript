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

---

## 7 · Hostile review — where the punch-up opportunities are

**Wendell, 2026-07-31:** *"where are the opportunities to punch up the text… I
don't know if [Rao, Wilber, Adams] are in the humor section or the voice passes."*

### First, the answer to the question

**They are in neither, and the distinction matters.**
`marginalia/specs/REVISION_INSTRUMENT.md` Part 4 splits the dials in two:

| Prose dials — change the sentences | Analysis dials — change what is understood |
|---|---|
| `+ADAMSY` · `+SNICKETY` · `+CLOWN` · `+JERK` · `+CULT LEADER` · `+NAVAL` | `LIKE WILBER` · `LIKE RAO` · `LIKE MILLER` |

**Adams is a humor dial. Wilber and Rao are not.** They are analysis dials, and
the spec's guardrail is explicit: *"An analysis dial always round-trips: it
changes the understanding, and the sentence comes back in house voice.
`LIKE WILBER` is never an instruction to write like Wilber."*

So there is no missing "Rao/Wilber voice pass" to slot into the editorial system.
They are already correctly placed, in the generative instrument, as a third thing
that is neither humor nor voice. **What was missing is that nothing in the
editorial system ever *called* them.**

### The instrument

`instruments/punchup.py` mechanises Part 2 — the six diagnostic checks that
select a color. Checks 1, 3, 4 and 5 are mechanical; 2 and 6 need judgment and
are left to a human. The spec's own routing table names the dial.

```
python3 instruments/punchup.py            # ranked
python3 instruments/punchup.py --ch 9     # one chapter
```

**57 paragraphs score ≥4 of a possible ~8.**

| ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|
| 6 | 2 | 7 | 5 | 5 | 8 | 4 | 8 | **12** |

### A hypothesis I had, tested, and dropped

I expected the flatness to concentrate in the Section 7 recaps — they are
formulaic, and two chapters open theirs with the identical sentence *"The chapter
leaves you holding a practice whose parts fit together"* (`ch3`, `ch4`).

**Measured: 5 of 57 sit in Section 7. Fifty-two are in the body.** The recaps are
not the problem; the flatness is distributed through the teaching itself. Recorded
because it was a good guess and it was wrong.

### The finding that matters — ch9

**ch9 carries the most flat paragraphs in the book, and it is the chapter where
that costs most.** The grid rules ch9's humor as *evidence* rather than charge:

> If comedy is a script running unattended, and at Ch9 nobody is unattended,
> there is nothing left to release. So the jokes stop generating charge and start
> being **evidence**: a person who can be light about a thing is demonstrating
> they are not gripped by it. **Play is the tell.**
>
> Ch3–Ch8 humor metabolizes charge. Ch9 humor is charge-free. **It is the sound
> of someone playing.**

Twelve flat paragraphs in the chapter whose humor *is* the demonstration of
mastery. **ch9 was ruled to sound like someone playing, and it scores as the
least playful chapter in the book.** That is a structural failure of the payoff,
not a shortage of jokes — and it is the same shape as A2 and A6: a chapter 9 that
performs a completion the middle of the book never accumulated.

Top of the list, `ch9:300`, indicated dial **Testimony / +CLOWN**:

> The map also doesn't show you what success looks like from the inside. The
> moment when someone plays bars-engine and something opens in them that you
> recognise…

Nobody present, nothing happening, three abstraction subjects — in a paragraph
about the feeling of watching someone get it.

### The other standing gap, restated as an opportunity

The Jerk is absent book-wide (§2). Sixteen of the 57 route to `+CULT LEADER /
Symmetry`, which the book already writes well — `ch4:115` is proof. **The cheapest
punch-up available is not the missing archetype; it is the one the book is
already good at, applied to paragraphs the instrument has already found.**

### Recommendation, unchanged in shape

**Not before ship.** But when it happens, the order is: ch9 first, because its
flatness breaks a ruled payoff rather than merely costing a laugh; then the
sixteen Cult Leader candidates, because the book has demonstrated it can write
them; and the Jerk last, or never, as a deliberate ruling rather than an
accident.

---

## 8 · The ch9 pass — and a miss in the app inventory it uncovered

### The app inventory undercounted, and ch9 is where it matters

`specs/SPEC_REMOVE_APP_V1_2026-07-31.md` searched for `\bapps?\b` and reported
**one** hit in ch9. It searched the common noun and missed the product name.

**`bars-engine` appears 23 times — eleven of them in ch9**, plus Appendix A, B,
C, F and the author bio. None was in the app-removal scope.

### The distinction that resolves it

ch9's eleven do **two different jobs**, and only one of them is app routing:

**ROUTING — the reader is sent to a product.** In scope for removal.
> `ch9:400` — "When you're ready, a place waits for you. **Bars-engine is the
> village's common ground** — the playground where players arrive after
> finishing…"

**TESTIMONY — Wendell's own story of having built something.** Out of scope, and
**it is the best prose in the chapter.**
> `ch9:358` — "**When I started building bars-engine, I didn't have it figured
> out.** I had a felt sense of what was missing…"
> `ch9:608` — "**Bars-engine has cost me all five of these.** *Cut the field* —
> it is not about allyship in general; it is about the gap between people who…"

**Removing the app must not remove the memoir.** ch9's argument is *build your
version of what this is for your problem*, and it is credible only because the
author built one. Strip the testimony and the chapter is a person recommending a
journey he did not take.

`ch9:610` shows the two jobs colliding in one sentence: *"You don't have to build
bars-engine. You have to build your version of what bars-engine is for your
specific problem."* The first clause routes; the second is the chapter's thesis.

### The punch-up and the app removal are the same edit

`ch9:300` is the highest-scoring flat paragraph in the book — nobody present,
nothing happening, three abstraction subjects — **and it is flat precisely
because it describes the product abstractly**:

> The map also doesn't show you what success looks like from the inside. **The
> moment when someone plays bars-engine and something opens in them that you
> didn't know was closed.** The moment when a player names a feeling they've never
> been able to name before and you realize the game did that.

The indicated dial is **Testimony**, and the paragraph is *about* a felt moment
the author has had. Converting it from a generic *someone* to a specific
remembered instance would fix the flatness and the routing in one edit.

**It cannot be drafted here.** It needs a real moment Wendell watched, which is
the same constraint that ruled the ch7 testimony slot. Flagged for him, not
written.

### Honest correction: ch9's list is shorter than twelve

Reading the twelve rather than trusting the score, **the instrument over-flags**:

- `ch9:167`, `ch9:181` are `**The practice:**` instruction blocks. Correctly
  flat — a list of moves is not supposed to have a person in it.
- `ch9:604` scores as flat and is not. *"Running it. Messing it up. Running it
  again. Running it with someone else watching."* — the anaphora is the play.
  **That paragraph is already doing what the grid asks ch9 to do.**
- `ch9:240` ends on the book's closing question and earns its plainness.

**Worth punching, on a real read: three or four, not twelve.** `ch9:300` leads, and it
is blocked on Wendell's memory rather than on drafting.

This is the same lesson as the recap hypothesis in §7, arriving twice in one
pass: **the score locates candidates, the reading rules them**, and on this
chapter the reading rejected two thirds.
