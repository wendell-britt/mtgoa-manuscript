# Amendment — the form metaphor is martial arts, not jazz

**Amends `SPEC_WAVE_AND_FIVE_MOVE_FORM_2026-08-06.md` §2 and Ruling 3.** That spec was
ratified 6–0 by the panel and this overturns part of it, so it gets a document rather than a
commit message.

**Opened by Wendell, 2026-08-11**, during the ch9 punch-up that followed the `WAVE` → `Form`
rename:

> *"I think pushing this into the context that the forms are how martial artists learn their
> fundamentals. I think this is brought up in the book, but it seems like it needs to get
> hammered. Why are we repeating ourselves. Why is this so important to end on. This is the
> impression we want to leave the reader with which is why they will show up in the dojo and
> 1:1 with me. WE can practice the forms as the players develop their own playstyle."*

---

## 1 · What the ratified spec said, and what shipped

**§2 of the 2026-08-06 spec ratified jazz:**

> The book borrows a teaching distinction from jazz training: **Know the form. Know the
> changes.** … This is an instructional lineage, not a claim that the five movements
> originated in jazz.

**Ruling 3** made it binding: *"'Know the form, know the changes' is Wendell's jazz-training
inheritance, explained once in ordinary language."*

**Measured 2026-08-11: the word *jazz* appears in no shipping file.** Not in a chapter, not
in an appendix, not in `ON_THE_SHOULDERS_OF`. **The ruling was never cashed.**

**So the word *Form* has been load-bearing for nine chapters on credit that was never paid.**
The two places it is introduced both decline to say what a form is:

| site | what it says |
|---|---|
| `ch1:260` | *"One form runs through every Face: the Five-Move Form… Every school after uses the same form, then teaches its own changes"* |
| `ch3:284` | *"That structure has a name: the Five-Move Form."* |

**A reader meets a technical term, twice, and is never told which technical term it is.** That
is the defect Wendell is pointing at, and it explains why the rename to `Form` felt flat in
ch9: the noun had no referent to be flat against.

## 2 · The martial-arts frame is already in the book, unnamed

**This is not a new metaphor. It is the one the book is already written in.**

| where | what is already there |
|---|---|
| ~~`ch5:308`~~ | ~~*"I came up in traditions. Martial arts, church, academia."*~~ — **WRONG, corrected 2026-08-11.** See §2a below. |
| `ch9:628` | the section is titled **The Last Rep** |
| `ch9` Move 4 | **Run It Again With One Thing Changed** |
| `ch3:292` marginalia | Maera: *"she has been practising for thirty years… For your first year, run two… **students** who learn two never come back for the other three"* — a sensei in all but name |
| `back_matter/enrollment.md:9`, `acknowledgements.md:21` | **the Allyship Dojo** |

### 2a · Correction — `ch5:308` does not exist and had not for some time

**Found by the ch5 deep reader, 2026-08-11, hours after this document was committed.**

**The line I cited as the strongest evidence is not in the book.** `grep -rn -i martial
manuscript/` returns three hits and all three are mine, written today: `ch1:260`, `ch3:286`,
`ch9:388`. **Zero in ch5.** `ch5:291` now reads *"I came up in traditions. A house, an
archive, a bench: all of them Regent organizations."* `git log -S` puts the removal in
`76e76fb`, the DL-19 author-collision cut — **before this amendment was written.**

**I took the quotation from `SPEC_DL19_AUTHOR_COLLISION_2026-07-31.md`, which records it as
the *before* text of an edit it then applied.** I read a spec's BEFORE column as the shipping
book. **The line I called *"Wendell's own voice, already shipping"* was the line a prior
ruling had already cut.**

**What this does and does not change.**

- **The ruling stands.** Wendell asked for the martial-arts frame directly, in his own words,
  on 2026-08-11. **An author's instruction does not need corroborating evidence from his own
  manuscript**, and it was never the case that the frame depended on ch5 carrying it.
- **The other supports hold, and I verified each against the file rather than against a
  spec:** `ch9:628` **The Last Rep** · `ch9` Move 4 **Run It Again With One Thing Changed** ·
  `ch3:292`'s marginalia teacher of thirty years with **students** · the **Allyship Dojo** in
  `enrollment.md:9` and `acknowledgements.md:21`.
- **One argument in §3 is weakened and should be read as weakened.** Reason 2 claimed the
  sense was already load-bearing *"in Wendell's own biography."* **It is not, in the
  shipping book.** Reasons 1 and 3 are untouched.

**The general lesson, which is the same one this whole pass keeps teaching.** A spec is a
record of a decision, not a copy of the book. **Three documents cite the martial-arts
explanation as `ch3:284`; the sentence is at `ch3:286`** — the same off-by-two propagated
through all three, which means they were written from each other rather than from the file.
**Quote the file.**

**The commercial surface already carries it.** `enrollment.md` names the Dojo and the
coaching; `DL-49` took the acknowledgements off this edition's spine, which makes the
enrollment page the **only** place the Dojo appears. **The book ends by pointing at a mat it
has never described.**

## 3 · Why jazz loses rather than shares

**The ratified Diplomat verdict blocks running both:**

> *"Can a reader who does not know jazz or martial arts use the distinction without being
> asked to learn another theory? Yes, if each practice receives its own first encounter and
> the form/changes image is explained in ordinary language, **not made into a second
> taxonomy**."* — **Verdict: explain the metaphor once.**

**Two metaphors for one noun is the second taxonomy that panel blocked.** So one of them
takes the slot. Martial arts takes it for three reasons:

1. **Nothing in the manuscript changes to make room.** Jazz was ratified and never written.
   There is no prose to unwind — only a spec line.
2. **The martial-arts sense is already load-bearing elsewhere in the product**, in Wendell's
   own biography (`ch5:308`), in ch9's section titles, in the marginalia's teacher, and in
   the name of the thing readers are being sent to.
3. **It answers the question jazz does not.** Jazz's *form and changes* explains why the same
   structure recurs across six different Faces — a **breadth** claim, and ch1's job. Martial
   arts explains **why you run the same five moves forever and that this is not remedial** —
   a **depth** claim, and ch9's job. Wendell's question was *"why are we repeating
   ourselves,"* which is the second one.

**What survives from §2 unchanged:** the five movements are still credited to Ken Wilber's
*Finding Radical Wholeness*; the metaphor is still an instructional inheritance rather than
a claim of origin; it is still explained exactly once.

**What `changes` becomes.** `ch1:260`'s *"teaches its own changes"* was jazz vocabulary
(chord changes). It survives untouched as ordinary English — *its own changes* reads
correctly without the jazz sense, and nothing else in the book depends on the term.

## 4 · The two passages

**Site one — `ch3:284`, immediately after *"That structure has a name: the Five-Move Form."***
This is the once. Without it, ch9's close lands as new information in the last five pages.

> *Form* is the martial artist's word, and it is the exact one. A form is a fixed order of
> moves you run alone, slowly, ten thousand times, so that on the day something comes at you
> fast your body already knows where it is going. Nobody graduates out of it. The beginner
> runs the form and the master runs the form, and what separates them lives inside the same
> five moves.

**Site two — `ch9:386`, the close.** Answers both of Wendell's questions on the page. The
first paragraph replaces the existing one; the second is new.

> The same five moves run a conversation with your mother, a decade of a partnership, and one
> election. **The Form doesn't change size.** That is why you learn it once rather than
> collecting a separate practice for every table you sit down at: your parenting, your work,
> the group chat and the town hall and the pandemic and whatever arrives after it, same five
> moves, wildly different stakes. The morning pass trains you for the rest of the day because
> there is no other pass.
>
> This is the part of a martial art that looks like nothing from outside. Everyone on the mat
> runs the same form, which is exactly what makes it possible to see what any one person is
> doing with it. Your playstyle is what shows up inside the form once you stop thinking about
> it: the move you reach for first, the one you dodge, the timing nobody taught you. Six
> Faces, five moves, and no two people run them alike. So the form is what you practice, and
> your game is what the practice reveals, which is also why the last of it goes faster with
> somebody watching. Alone you can drill the moves. It takes another pair of eyes to tell you
> what you do with them.

**The last two sentences are the on-ramp**, and they are pitched to match `enrollment.md`'s
own honesty — *"None of it is required. You can run the rest alone… and people do, and it
takes longer"* — rather than overselling the mat. **The book spent nine chapters teaching a
reader to spot a sales move; the close cannot make one.**

## 5 · Review board

| | ch3 passage | ch9 passage | ch3 baseline | ch9 baseline |
|---|---|---|---|---|
| voice | clean | clean | | |
| gate | clean | clean | | |
| `be` | 1.12 | 0.84 | 0.71 | 0.68 |
| `copula` | 0.86 | 1.03 | 0.84 | 0.57 |
| `waste` | 1.00 | 0.92 | 1.03 | 0.95 |
| `zombie` | 0.00 | 0.31 | 0.91 | 0.97 |
| `empty` | 1.01 | 0.67 | 0.78 | 0.86 |
| `ranking` | 0 HARD · 0 SOFT | 0 HARD · 0 SOFT | | |
| `empty_head` | 0 | 2 SOFT, 0.00/1k | | |

**Three things changed after the first run rather than argued with:**

- `gate` failed on **`room`** — *"a separate practice for every room you walk into."* Banned
  word. Now `table`, which is also the book's own furniture (*stay at the table after you
  have named the game*).
- `empty` came in at **1.37**, over ceiling, on `version` twice in one sentence. *The morning
  version / no other version* is now *the morning pass / no other pass* — also the more
  accurate noun, since a **pass** of the Form is the unit ch9 has counted since `:284`.
- `zombie` came in at **1.88** on the ch3 passage: *a fixed **sequence*** → *a fixed **order
  of moves***, and *the whole **difference** between them* → *what **separates** them*.

**Two claims drafted and cut:**

- **`identical cost to run`**, as the third beat of the scale-invariance list. It is the Rao
  cadence and it is false — a decade of a partnership does not cost what one phone call
  costs. Scale invariance is a claim about the **moves**, not the stakes. Buying rhythm with
  a claim the book cannot defend is the trade this whole pass exists to refuse.
- **"Your playstyle is not a layer you add once the form is finished."** A denying negation:
  the layer is not still true at the end of the sentence. Exactly the shape Wendell caught by
  eye on 2026-08-07 and the reason `ranking.py` exists.

## 6 · Dials

**`HUMOR_GRID.md` blocks `+WILBER` and `+RAO` in ch9** — those are parody, and ch9's cells
are **Play · Fondness · Handoff**, no butt. Wendell named Rao and Wilber; what is legal here
is the **analysis** dial, `LIKE RAO` / `LIKE WILBER`, which must round-trip. The
scale-invariance claim is the `LIKE RAO` move and it round-trips: *the practice is
scale-invariant, the stakes are not.* The single joke — *it stops being homework* — is
charge-free, which is what ch9's ruling allows.

## 7 · Consequent edits

- **`SPEC_WAVE_AND_FIVE_MOVE_FORM_2026-08-06.md` §2 and Ruling 3** are superseded by this
  document on the metaphor only. **Everything else in that spec stands**, including the
  WAVE / Five-Move Form split, the Wilber credit, and the two-separate-first-encounters
  requirement.
- **No new instrument catches this class.** A metaphor ratified in a spec and never written
  into prose is invisible to every counter in `instruments/`, the same blind spot that let a
  half-finished rename survive four chapters. **The one-concept-one-name check proposed in
  `SPEC_WAVE_RENAME` §6 should also ask the reverse: which ratified terms were never
  cashed.**
