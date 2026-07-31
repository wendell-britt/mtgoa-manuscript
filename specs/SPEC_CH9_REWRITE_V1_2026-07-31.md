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
