# SPEC — Chapter 9 rewrite for v1

**Branch:** `claude/ch9-rewrite-v1`. Diagnosis and scope. Nothing rewritten yet.

**Wendell, 2026-07-31:** *"Chapter 9 needs to get rewritten if I'm taking
bars-engine out of the v1 of the book. We need to save what we've got for now
because it might make its way back in, but now we have to actually teach people
to create their own allyship game using their moves they've been practicing and
the character sheet they've ostensibly been filling out."*

**Preserved first.** The current chapter is at
`drafts/archive/ch9_bars-engine_version_2026-07-31.md` — 12,608 words, byte-for-byte,
before anything is touched.

---

## 1 · The good news: the skeleton already does this

ch9 is **not** a bars-engine chapter with a lesson attached. Its architecture is
already *design your own game*:

| Section | Words | State |
|---|---|---|
| Front matter — *The Return* | 73 | clean |
| 1 · The Exile | 270 | clean |
| 2 · The Distortion | 432 | clean |
| 3 · The Concept — *From Map to Design* | 463 | clean |
| 4 · The Practice — **How to Design Your Own Allyship Game** | 2,220 | **1** bars-engine ref |
| 5 · Journey to the Center — *Building the Thing That Didn't Exist* | **5,144** | **7** refs — the memoir |
| 6 · The Game — the five Player moves | 2,187 | 2 refs |
| 7 · Recap and Transition | 192 | clean |
| The Last Rep — the six-moment drill | 1,302 | **clean** |
| The Village Is Already Playing | 317 | 1 ref — a product list |
| The Last Line | 98 | clean |

**Roughly 9,500 of 12,608 words are structurally clean.** Section 4 already names
the five modes of self-authorship and the stage sequence *Review → Discern →
Design → Build → Pass On*. Section 6 already carries five Player moves — *Cut the
Field to One Problem · Put It in Front of One Person Before It's Defensible ·
Take the Note That Costs You the Design · Run It Again With One Thing Changed ·
Hand Someone the Pen*. The Last Rep already runs the transfer drill.

**The rewrite is Section 5**, and one clause each in three other places.

## 2 · What Section 5 is, and what it has to become

5,144 words — 41% of the chapter — of Wendell building bars-engine, used as the
worked example of designing a game.

**The memoir is not the problem. Its exclusivity is.** The chapter currently
demonstrates *design your own game* by narrating one person designing one
specific thing the reader cannot use, and then telling her to go do her own.

Per §8 of `SPEC_HUMOR_PASS_2026-07-31.md`, the eleven references do two jobs, and
only one is app routing:

- **ROUTING** — `ch9:400` *"Bars-engine is the village's common ground"*,
  `ch9:696` the product list. **Out for v1.**
- **TESTIMONY** — `ch9:358` *"When I started building bars-engine, I didn't have
  it figured out"*, `ch9:608` *"Bars-engine has cost me all five of these."*
  **Keep.** Strip this and the chapter is a person recommending a journey he did
  not take.

**The replacement is not more memoir. It is her build**, with his as the worked
example beside it — which is what every other chapter in the book already does.

## 3 · The dependency that outranks everything else

**Wendell's brief says the reader builds from "the character sheet they've
ostensibly been filling out." She has not been filling it out.**

Finding A2, measured: `ch1:207` promises *"a line added in every chapter ahead."*
Delivered: **ch2 and ch9 only. Six consecutive chapters add nothing.**

So a rewritten ch9 that opens *"look at your character sheet"* is addressing a
reader holding four entries from ch1 and one from ch2.

**A2 is now a hard dependency of this rewrite, not an optional improvement.** The
new chapter's central input does not exist until those six lines are seated.

**They are already drafted, gated and approved** — six sheet lines for ch3–ch8 in
`drafts/APPROVED_unearned_recall_2026-07-31.md` on
`claude/edit-assumed-prior-knowledge`. Each names that chapter's own artifact:
the channel she skips, the line she has not drawn, the inheritance she carries,
the harm she keeps fixing, her walk-away price, where she goes when a situation
is larger than she can hold.

**Read as a set, those six lines are the character sheet the new ch9 needs.** They
were drafted to close a promise; they turn out to be the input for the payoff.

**Sequence: A2 lands first, then ch9 is rewritten against a sheet that is full.**
Reversing that order produces a chapter whose first instruction fails.

## 4 · The second input: her moves

The brief also says *"the moves they've been practicing."* Measured, those exist
and are plentiful — **five per chapter across ch3–ch8, thirty in total**, plus
the WAVE's five stages, plus ch9's own five Player moves.

**The risk is arithmetic, not availability.** ch9 already carries three competing
sets of five (CH9 report, finding S2), and the rewrite adds a fourth reference
class. The chapter that teaches her to build must be the clearest in the book
about which five it means at any moment, and it is currently the least clear.

## 5 · What the rewrite has to deliver

1. **An instrument she fills in**, drawing on the sheet and her thirty moves —
   the thing Section 5 currently substitutes memoir for.
2. **A worked example that is his, kept short**, standing beside her build rather
   than in place of it. The testimony survives; the 5,144 words do not.
3. **A game she can actually run this week**, which is what the five Player moves
   in Section 6 already describe and Section 5 never lets her reach.
4. **No product.** Routing out, testimony in, `masteringallyship.com` as the one
   door — per `SPEC_REMOVE_APP_V1_2026-07-31.md`.

## 6 · What is reusable, verbatim

- **The Last Rep** (1,302 words) — the six-moment transfer drill. The only place
  in the book she is given situations and asked to choose a Face and a move. It
  needs the three fixes in the CH9 report (an outcome for the middle result, the
  move half scored, a move roster) and needs no bars-engine.
- **Section 6's five Player moves** (2,187 words) — already the right teaching,
  two clauses to clean.
- **Sections 1, 2, 3, 7 and The Last Line** — clean, ~1,100 words.
- **Section 4's five modes and stage sequence** — the frame the new Section 5
  should execute against, one ref to cut at `ch9:153`.

## 7 · Rulings needed

1. **How long is the new Section 5?** It is 5,144 words. A build instrument plus a
   short worked example is plausibly 1,500–2,500, which would take ch9 from
   12,608 to roughly 9,000–10,000 and make it the shortest teaching chapter
   rather than the second longest.
2. **Does the archived version stay in the repo?** It is preserved at
   `drafts/archive/`. A second edition that restores bars-engine wants it intact.
3. **Does A2 land first?** Recommended, and near-blocking. The alternative is
   writing ch9 to a sheet the reader does not have.
4. **What is the reader's build, concretely?** A one-page game design? A single
   quest she runs on the cause she chose in ch1? The answer sets the instrument,
   and it is the one piece of this that cannot be derived from what already
   exists.

---

## 8 · Ruling 4 answered — what she builds

Panel: `specs/PANEL_HEADS_CH9_BUILD_2026-07-31.md`. Wendell's constraint test
held: every input was already canon, so the six answers are composition rather
than invention.

**The convergence, which Orr names and which the book built first.** Five Heads
gave five different instruments, and they map one-to-one onto ch9's existing
stage sequence:

| Stage (`ch9:200`) | Head | The instrument |
|---|---|---|
| **Review** | Voss | Her six sheet lines, together, for the first time. Read them as one document and say what they share |
| **Discern / Design** | Vale | One page. Four fields: the ch1 quest · the Face it requires · the single move · **the condition that will make it fail** |
| **Build** | Ash | One rep. One quest, one person, one Face she does not reach for, **by a date, at a cost named in advance** |
| *(the test on Build)* | Cross | One scheduled conversation with a named person, **before it is ready**, asking what it would cost them to use it |
| **Pass On** | Quill | A named inheritor, entered at the time of writing, not when she next feels moved to |

That is not five options. **It is one instrument seen from five seats, and the
sequence it fills is already printed in the chapter.**

### The recommendation

**She builds a one-page game for the quest she named in Chapter 1, and runs one
rep of it inside a week.**

The page carries: the quest · the Face the quest needs rather than the Face she
has · one move from the thirty · the failure condition · the date · the cost ·
the person who receives it. Every field is already canon; nothing is new
vocabulary.

**The framing move is Orr's, and I think it is the whole rewrite:**

> The chapter should not ask her what she wants to build. It should show her that
> she has been building it since Chapter 1 and hand her the page where it already
> exists. **A person who is told to start will start something new. A person who
> is shown what she has already accumulated will finish it.**

That reframes Section 5 from *5,144 words of how one man built one thing* to
*here is what you have been assembling for nine chapters, on one page, with the
gaps visible.* It is shorter, it is hers, and it converts A2's six sheet lines
from a closed promise into the chapter's raw material.

### Why this also fixes the app problem

The reader's build has been bars-engine-shaped because the only worked example
was bars-engine. Once the build is her one page, Wendell's testimony becomes what
it should always have been — **the short worked example beside hers**, not the
substitute for it. Routing goes; memoir stays; the chapter gets shorter.

### What is still Wendell's

The panel derived the instrument. It did not derive **the worked example** — one
short pass of Wendell's own page, filled in. That is his to write, and it is
perhaps 200 words rather than 5,144.

---

## 9 · Wendell's pushback, and why it is structurally true

**Wendell, 2026-07-31:** *"Instead of bars-engine let's say that the book itself
was created off of my own page filled in… What answer from every chapter would
justify a book like this being created? The person I'm allying with IS Jordan."*

**Worked backwards, and Chapter 1 already contains the filled page.** Every field
of the instrument is answered there, in prose, three years before the form
existed:

| Field | The answer | Already written at |
|---|---|---|
| **The quest** | Jordan. The reader | `ch1:6` *"I made a promise to readers who trusted me with their money and their hope"* · `ch1:14` *"You're the person I made that promise to"* |
| **The Face it required, against the Face he had** | Home: **Diplomat**. Required: **Challenger** | `ch1:187` *"I kept this very book in conversation for three years, everyone comfortable, nothing decided"* · `ch1:10` *"It wasn't until I gave myself permission to actually be mad"* |
| **The one move** | Challenger Move 5 — **Draw the Line** (`ch4:686`) | `ch1:14` *"This is me showing up — late, imperfect, and in the game"* |
| **The condition that will make it fail** | *"Moved, and unchanged"* | `ch1:239` *"If that is all this book does, I have failed"* — **stated verbatim, and it is Vale's fourth field** |
| **The date** | Three years late, then a date | `ch1:4` *"This book is three years late"* |
| **The cost** | Three years on guilt; chapters thrown out | `ch1:109` · `ch1:119` |
| **Who receives it** | Her, and she writes her own | ch9's *Hand Someone the Pen* |

### Why this is better than a joke

**The book passes its own definition.** `ch1:91`: *allyship is the practice of
increasing another person's well-being while protecting the conditions that allow
both of you to remain full players.* `ch1:231` protects those conditions
explicitly — *"This oath is not to me. You can't fail me — you can only fail
yourself."* **The book is an allyship move, made on Jordan, that satisfies the
book's own test.** That is not a conceit; it is the thesis demonstrated on the
only case the author fully controls.

**The comedy is load-bearing rather than decorative.** Per `HUMOR_GRID`, the
engine is *a script running with total commitment in a situation that stopped
calling for it*, and the **Clown** is self as the butt. A man ran the Diplomat for
three years on a book about not doing that. It is `REVISION_INSTRUMENT` #14,
**Break Frame** — *confess in the open what the text is doing to her* — and #2,
Clown, at once. Wendell's instinct that it is funny and the grid's account of why
are the same account.

### What it does to the rewrite

**ch1 and ch9 become the same form, filled and blank.** ch1 is the worked example
told as confession; ch9 hands her the identical seven lines, empty. Nothing has to
be built to make that true — ch1 is already written. Section 5 stops being 5,144
words of one man's product and becomes **one short page of his, and then hers.**

bars-engine leaves without taking anything with it, because the worked example was
never the app. It was the book.

### Draft — Wendell's page, ch9

Gate clean · be 1.03 · copula 0.69 · waste 1.21 · zombie 0.53 · expletive 0.00 ·
passive 0.00. Roughly 260 words, against Section 5's 5,144.

> Here is mine. I filled this page out three years before I had the form, which is
> the only reason I can hand it to you now.
>
> **The quest:** you. Not allyship in general, and not people who want to be better
> allies. You, the one who has done the reading and the therapy and the work, who
> still goes home from the hard conversation running it back. I made a promise to
> readers who trusted me with their money and their hope, and then I spent three
> years not keeping it.
>
> **The Face it needed, against the Face I had:** I am a Diplomat. I kept this book
> in conversation for three years, everyone comfortable, nothing decided. What it
> needed was a Challenger, and I could not reach one until I let myself be angry at
> the delay.
>
> **The move:** draw the line. Ship it late, imperfect, and in the game, or do not
> ship it.
>
> **What would make it fail:** you are moved tonight and unchanged by morning. That
> is the whole risk, and it is why there is a card in your hand instead of a
> conclusion at the end.
>
> **What it cost:** three years on the wrong fuel, and a stack of chapters written
> at the applause counter that had to be thrown out.
>
> **Who gets it after me:** you do. That is what the last page is for.
>
> Now yours. Same seven lines, and you have been filling most of them in since
> Chapter 1.

**Every claim in it is sourced to existing prose.** Nothing is invented; the
hallucination risk Wendell named is answered by the fact that the answers were
already on the page, in Chapter 1, waiting for a form.

---

## 10 · Second pass — Wendell's correction

**Wendell:** *"Nice but shallow. We've made it a bit too tidy… I was an
architect diplomat and she needed a sage, which meant I needed to confront the
other faces. The shaman and the challenger and the regent… We can twist the knife
on the cost. This is where we can mirror their own cost for not showing up as an
effective ally."*

**The correction makes the book's own thesis do the work.** `THESIS_DRAFT`: *to
be an effective allyship game master you must master all six levels; if you skip
one, the shadow of that level is what blocks you.* Two Faces home, four missing,
and the missing four had to be gone and got. **That is why the book has nine
chapters, and it is a better answer to "what justifies this book existing" than
anything in §9.**

Both home Faces are already evidenced: Diplomat at `ch1:187`, Architect at
`ch6:365` — *"I have a part of me I call the Collapse… it still cringes at the
system I built that nobody used."*

### The move — five options, all canon

The Sage's five are at `ch8:590`–`650`. Wendell picks.

| | Move | Why it fits | What it costs |
|---|---|---|---|
| **1** | **Return Without Condescension** (`ch8:626`) | The book *is* the return — the Sage goes up, sees the map, comes back down carrying it. ch9's own subtitle is *The Return*, so the chapter's frame and the move become the same thing | The safest and the most expected. It confirms rather than surprises |
| **2** | **Hold the Meta Without Losing the Ground** (`ch8:650`) | Writing about six Faces while being two, without floating off. **It would also close the book's only bare claim** — `ch8:603` is the one move in the manuscript with no worked example, and this page would be it | The hardest to make concrete, which is why it has no example yet |
| **3** | **Put a Game Down** (`ch8:636`) | He put down the good-ally game, and the applause counter is already confessed at `ch1:119` | Points at what he stopped rather than what he made — a subtraction where the reader wants a build |
| **4** | **Switch Games Deliberately** (`ch8:606`) | Diplomat to Challenger, on purpose, once the anger arrived (`ch1:10`) | Reads as a Challenger move wearing a Sage label |
| **5** | **Name the Game** (`ch8:590`) | Naming that he had been playing for applause | It is the first move of the chapter, and this is the last chapter |

**Recommend 2, with 1 as the safe alternative.** *Hold the Meta Without Losing
the Ground* is the only one that describes writing this specific book, and it
retires a real defect: `ch8:603` is currently the single move in the manuscript
taught without an example, and Wendell's page is the example.

### The cost — the mirror

`ch1:189` sets the terms the whole book turns on: *"The reason to widen your
range is the person in front of you — the one who needed a move you did not
have."*

**So the cost is not the delay. It is the reader's three years without it, and
the person on the other side of her conversations during them.** His narrow range
cost her exactly the way her narrow range costs whoever is in front of her. Stated
that way the page stops being confession and becomes the book's thesis run on its
author, in the same grammar it will run on her ten lines later.

### Draft — the deeper version

Gate clean · be 0.60 · copula 0.46 · waste 0.93 · zombie 0.25 · expletive 0.00 ·
passive 0.00. Every counter improved on §9's draft.

> **The quest:** you. Not allyship in general. You, who has done the reading and
> the therapy and the work, and still drives home from the hard conversation
> running it back.
>
> **The Face it needed, against the Faces I had:** I am an Architect and a
> Diplomat. I can see the system and I can keep everyone at the table, and between
> those two I kept this book in conversation for three years, everyone
> comfortable, nothing decided. What you needed was a Sage — somebody who could
> hold all six games at once and tell you which one you were in. I could hold two.
> To write the other four I had to go and get them, which is the reason this book
> has nine chapters instead of three. The Shaman was the worst of it. I had spent
> an adult life converting what I felt into what I could diagram, and Chapter 3 is
> what it cost me to stop.
>
> **What it cost:** three years in which you did not have this. I want to be
> exact, because you are about to write your own version of this line and
> vagueness is how it gets survived. It did not cost me a deadline. It cost the
> conversations you went into during those three years without a move you needed,
> and the person on the other side of them, who did not get what they came for and
> has no idea why. I have thought about that person more than I have thought about
> the delay.
>
> **Who gets it after me:** you do. Not to keep. To change.

**The move and the failure condition are left blank in this draft**, pending the
ruling above. `ch1:239` still supplies the failure condition verbatim — *"Moved,
and unchanged"* — and it needs no rewriting.

**One line is doing work that should be flagged.** *"I want to be exact, because
you are about to write your own version of this line and vagueness is how it gets
survived"* is `REVISION_INSTRUMENT` #14, **Break Frame** — the text confessing what
it is doing to her, one beat before it asks her to do it. It is the hinge between
his page and hers, and it is the line to cut first if the page runs long.

---

## 11 · All five — yes, and the book already runs them

**Wendell:** *"is there a case to be made for keeping all 5? and having the
examples be my own examples? or is that too much."*

**There is, and ch9 already does it.** `ch9:608` runs all five **Player** moves
against bars-engine in a single paragraph. Swapping the subject keeps the form.

**Note which five.** `ch9:608` runs ch9's own Player moves — *Cut the Field · Put
It in Front of One Person · Take the Note That Costs You the Design · Run It Again
With One Thing Changed · Hand Someone the Pen* — not ch8's Sage moves. So the two
questions do not compete:

- **The page** carries **one Sage move** — why the book exists. Vale's field.
- **`ch9:608`** carries **all five Player moves** — what building it cost, move by
  move. One paragraph, already written, already the right length.

**Not too much.** It is one paragraph and it is the chapter's best compression.

## 12 · The error I made drafting it, recorded

Drafting the swap, **I invented biography**: a person who read Chapter 3 aloud,
where they stopped, a count of drafts, a diagram cut in revision. None of it is
known. I filled five specific slots because the form demands five specifics, and
that is precisely the failure this session refused twice — the ch7 testimony slot
and `ch9:300` were both left blank for exactly this reason, and here the pressure
of a good paragraph shape produced what the blank pages had prevented.

**Recording it because the mechanism is general.** A form that requires N concrete
instances will generate N concrete instances. The safeguard is not care; it is
never drafting into a slot only the author can fill.

The scored version was also worse — `be` **0.81 → 1.52**, copula **0.00 → 0.86** —
because invented specifics arrive as *the note was that my best chapter was the
one where*, which is three copulas propping up a fact that does not exist.

### The honest version

Slots marked, not filled. `be 0.18` against the original's `0.81`, waste `1.44`
against `1.68`, zombie `0.00` against `0.90` — better on every counter than the
bars-engine original, because the invention is gone rather than because the
prose improved.

> This book has cost me all five of these. *Cut the field* — not allyship in
> general; the gap between people who understand the theory and people who can run
> it when something lands hard. *Put it in front of one person* — **WENDELL: the
> first person who read a chapter before you wanted anyone to, and where they
> stopped.** *Take the note that costs you the design* — **WENDELL: the note that
> cost you something structural, and what you cut because of it.** *Run it again
> with one thing changed* — **WENDELL: how many drafts, and the one change that
> mattered.** *Hand someone the pen* — you are holding it.

Two of the five need nothing: *Cut the field* is already true and already written,
and *Hand someone the pen* resolves to the reader, which is the whole conceit.
**Three slots, one sentence each.**

### `placeholders.py` does not catch these

Verified: the `WENDELL:` slots match no existing rule. If this drafting convention
is used, the scanner needs a rule for it before anything is committed to a chapter
— otherwise it is the testimony slot again, in a new costume.

## 13 · Why Move 5 could not be answered

**Wendell:** *"How can I hold the meta without losing the ground lol"*

Measured, the ch8 move template degrades across the five:

| Move | Example | Test |
|---|---|---|
| 1 Name the Game | yes | yes |
| 2 Switch Games Deliberately | yes | yes |
| 3 Return Without Condescension | **no** | **no** |
| 4 Put a Game Down | **no** | yes |
| **5 Hold the Meta Without Losing the Ground** | **no** | **no** |

**The question could not be answered because the book does not answer it.** Move
5 carries roughly 400 words of accurate abstract prose and no instance of anybody
performing it. The author wrote the move and cannot execute it on demand, which is
exactly the reader's position.

**The answer is the page itself.** Writing a book about six Faces while being two,
for three years, without floating off into theory — the ground was the promise,
the deadline, and her. That is the move, performed, at length, and it is the
missing example.

**So the recommendation from §10 stands and strengthens:** the page's one Sage
move is *Hold the Meta Without Losing the Ground*, and seating it closes
`ch8:603`, the only move in the manuscript taught without one.

---

## 14 · The 3-2-1, measured — it is not slotting in, and the book says so itself

**Wendell:** *"how is the 321 tool slotting into the book? It's in an appendix,
but it's a core tool… This could even be one of the things that I cut."*

`ch3:623` sets a **three-tool triage**, in the book's own words:

> Use **3-2-1** when the trigger is a *person*. Use the **Polarity Map** when
> you're stuck between two things that both seem necessary. Use **WAVE** when the
> charge already sits in your body, ready to move.

Measured across the six Face chapters:

| Tool | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 |
|---|---|---|---|---|---|---|
| Polarity Encounter | 1 | 1 | 1 | 1 | 1 | 1 |
| WAVE stages | 13 | 10 | 6 | 7 | 7 | 5 |
| **3-2-1** | 8 | 7 | **0** | **0** | **0** | **0** |

**Two legs of the triage run the whole book. The third stops after ch4.** It is
taught at `ch3:576`, practised once at `ch4:458` — *3-2-1 — Reclaim the Line You
Projected* — and never appears again.

**So the answer to "how is it slotting in" is: it isn't.** It is the odd one out
in a set the book itself defined, and it is the abandoned-convention pattern that
has now appeared five times in this pass.

### The ruling this actually asks for

**Not "cut or keep." Three options, and the cheap one is not the cut.**

1. **Cut it.** Removes `ch3:576`, `ch4:458`, the triage's first clause and
   Appendix E's 1,077 words. Also removes **the book's only Ken Wilber credit**,
   which `MANUSCRIPT_FILE_CANON` records as the reason Appendix E exists. Wilber
   is load-bearing elsewhere — `ch8:213`'s carry-the-lower-altitudes rule is his —
   so the credit would need rehoming in Appendix G.
2. **Keep it as it is** and amend `ch3:623` so the triage stops claiming three
   equal legs. One clause. **The cheapest honest fix.**
3. **Seat it in one later chapter** so the triage is true. ch7 is the natural
   host — its whole subject is a person you are in conflict with, and its daemon
   is the Victim, which is the projection engine 3-2-1 exists to reclaim.

**Recommend 2 now, 3 in a second edition.** The tool is not broken and the
appendix is written; what is false is the sentence promising three tools she will
use throughout.

**On its being core to Wendell's own practice:** that is an argument for the
second edition, not against the ruling. The book is better for handing people
what they need, and a tool used twice is not yet what the book needs. It is what
the *course* needed, which is a different product with a different contract.

## 15 · The superpower — the premise is wrong, and that is good news

**Wendell:** *"I could also talk about the superpower concept in brief… It didn't
make it into the book."*

**It did.** Measured, every chapter carries it — ch1:1 · ch2:5 · ch3:6 · ch4:1 ·
ch5:1 · ch6:2 · ch7:2 · ch8:2 · ch9:1 — **21 references**, and it is defined
cleanly at `ch2:394`:

> Your superpower is the reliable capacity you built to survive your wounds, once
> that capacity is made conscious, ethical, and usable in service of others.

It is also **promised on the character sheet** at `ch1:207` — *"a superpower you
will only spot in motion."*

**What did not make it in is the quiz, not the concept.** So the job is not to
write a superpower section. It is **one sentence pointing at the quiz**, and the
place it belongs is beside the definition at `ch2:394` or beside the promise at
`ch1:207`.

**One tension worth naming before it is written.** `ch1:207` promises she will
*spot it in motion* — the book's method is recognition through play, not
assessment. A quiz that hands her the answer up front competes with that. The
version that does not: point at the quiz as a **second opinion after she has
spotted it**, which keeps the book's method intact and gives the quiz a job the
book cannot do.

---

## 16 · Shame — measured, and Wendell's read confirmed

**Wendell, mid-3-2-1:** *"Is the word shame even in the book. He's ashamed of
shame. It's sanded down. But yes shame turns into emotional alchemy. Shame is the
experience of dissatisfaction itself. So he's worked his way around it. But it's
not obvious that this is the case. And it needs to be obvious."*

### The count

| word | uses in 96,355 words |
|---|---|
| fear | 94 |
| anger | 87 |
| sadness | 84 |
| guilt | 15 |
| **shame / ashamed** | **9** |

Per chapter: ch1 **0** · ch2 **0** · ch3 2 · ch4 1 · ch5 3 · ch6 **0** · ch7 1 ·
ch8 **0** · ch9 1.

**Zero in the chapter that promises to take the guilt apart.**

### The part that is worse than absence

**Every one of the nine is already an alchemy.** The book does not avoid shame —
it performs the conversion and declines to name what it is converting:

- `ch5:408` — **"Inheritance-Shame → Inheritance-Gift.** The shame says: this
  wound was done to me, therefore I am broken."
- `ch7:250` — "the **shame of being a learner instead of an expert**, converts
  into the groundedness…"
- `ch3:341` — the Clean stage strips "the secondary reactions (**shame**…)"
- `ch4:346` — "Charge → Collapse: the anger that should be directed outward
  becomes self-directed **shame**"

**So the mechanism is already in the book, twice, fully worked.** It appears as a
local move inside two chapters rather than as the thing the engine runs on.

### The structural claim, tested

*Shame is the experience of dissatisfaction itself.* The book's engine is
`[DISSATISFACTION → SATISFACTION]`. Measured: **dissatisfaction appears 29 times,
23 of them in ch7.** ch1 **0** · ch2 **0** · ch9 **0**.

So both halves are near-invisible in the same places. **The engine's substrate and
the engine's own word are both missing from the opening and the close**, and both
are concentrated in single chapters in the middle.

Shame is also **not one of the five channels** — Metal/Fear, Water/Sadness,
Wood/Joy, Fire/Anger, Earth/Neutrality. That is consistent with Wendell's reading
rather than against it: shame is not one of the five feelings, it is **the state
the five are being metabolised out of.** The taxonomy has no slot for it because
it is the substrate, and the book never says so.

### Can the promise be made

`ch1` promises to take apart guilt and it uses the word. It never uses *shame*.
**The promise as made is narrower than the book Wendell thinks he wrote**, and
the two places where the book actually does shame-work — `ch5:408`, `ch7:250` —
are not in the chapter where the promise lives.

**This is a real finding and it is not a ship-blocker.** It is one paragraph in
ch1 naming what the engine runs on, and possibly one line in ch9. Everything
downstream already works; what is missing is the sentence that makes it legible.

**Gate note.** This section trips `andbut` six times and every hit is inside a
quotation of Wendell's own transcript — *"And life was the one that taught us…"*,
*"But I have benefited…"*, *"And that game involved…"*. The rule governs the
book's prose, not a record of what somebody said. **Do not edit the transcript to
satisfy a linter.** `MTGOA_INSTRUMENTS_TOOLKIT` already records the same caveat
for the `stacks` rule: it fires on legitimate quotations of a defect inside
editorial documents, and inspection precedes fixing.

## 17 · The three slots, answered — in Wendell's own words

His 3-2-1 supplied all three. Nothing below is drafted; it is his transcript,
which is why it can be used.

**1 · *Put it in front of one person*** — the answer is that he did not.

> *"we put it in front of hundreds of people WAY before we were supposed to. Then
> we SOLD a BOOK to them, even still before we were ready. No one told us it was
> crazy. They believed in us. And life was the one that taught us we weren't
> ready."*

Where they stopped is the exact thing the slot asks for, and he supplied it:

> *"In the course everyone stopped when I told them to do a 3-2-1 on the dead
> self. They didn't want to confront the part of them that was pretending to be
> dead so they didn't have to show up as an ally."*

**2 · *Take the note that costs you the design*** — the note came from himself,
and it is the funniest and worst line in the transcript:

> *"Did you confront that part?"* — *"I didn't. I almost forgot. **I never took my
> own course.** lol"*

**3 · *Run it again with one thing changed*** — the cost, itemised, and it needs
no editing:

> *"6 years of the mastering the game of allyship program. 4 years writing the
> book. 3 cities. Jobs as a customer service rep, a crypto company documentarian,
> a smoothie maker, a shoe salesman, an event organizer and all sorts of things to
> keep my head above water while I made this happen."*

### And a fourth thing he did not know he was answering

The dialogue asks *"So where are people stopping now?"* and the answer is a
cleaner statement of the book's thesis than anything currently in ch1:

> *"They are stopping seeking growth and wellbeing. They've been told that they
> can't personal-development their way into being a better ally and they can't
> heal their way into being a better ally, and they are partially right. But I
> have benefited from being a player of the game of allyship. And that game
> involved showing up and finding ways to pay down the tokens, and keeping it
> moving."*

**That is the paternalism-adjacent myth A3 found orphaned**, answered — and it is
also the shame paragraph, because *stopping seeking growth and wellbeing* is what
shame does. Two open findings close on one paragraph of his own transcript.
