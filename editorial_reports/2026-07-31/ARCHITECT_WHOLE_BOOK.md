# BOOK ARCHITECT — whole-book scan

**2026-07-31.** Role 1 of the Lean Editorial OS, run against canon
`manuscript/ch1.md`–`ch9.md` with the marginalia frame stripped. Diagnosis only;
no prose was changed. Five findings, which is the cap. **A sixth, A6, was added after the chapter
passes surfaced it from three directions; it outranks the original five.**

> **Line-number convention, corrected 2026-07-31.** Every `chN:LINE` below refers
> to the file **as it sits on disk, with the marginalia frame applied** — what you
> see when you open it. An earlier version of this report cited numbers from the
> stripped body text, because the scan was run stripped; those were off by up to 92
> lines in the framed chapters. All citations have been remapped by searching the
> quoted text rather than by applying an offset. Chapter 1 carries no frame, so its
> numbers were never affected. The chapter-level reports in this directory use the
> same on-disk convention.

Every finding below is a **promise made in Chapter 1 and measured against the
eight chapters that follow it**, or a **prerequisite that arrives after the
reader needs it**. Both are structural by definition: neither can be fixed by
rewording the sentence where it surfaces.

**Method note.** Two candidate findings were discarded before this list.
`chain2.py` reported zero moves in ch1–ch4; `grep` shows ch3–ch9 each carry
exactly five `### Move N:` headings, so that was a parser artifact. An earlier
count of the character-sheet thread missed `ch2:560` because that chapter says
*the sheet* rather than *character sheet*. Both corrections are the toolkit's
standing rule working: never trust a detector without inspecting specimens.

---

## A1 · The Three Games are promised as the book's spine and never appear again

**Locations.** `ch1:149`, `ch1:173`; zero occurrences in `ch2`–`ch9`.

> `ch1:149` — "Allyship reaches you as three games running at once: the lucky
> breaks you cannot schedule, the skills you can actually build, and the love
> that keeps you coming back. **Everything ahead is built to strengthen your
> hand in all three** — to keep you present for the breaks when they come, to
> sharpen the moves that are yours to make, and to deepen the passion that
> keeps you at the machine long after discipline would have quit."

> `ch1:173` — "So take the one you brought with you and sort it, once. Where is
> it Chance… Where is it Skill… Where is it Passion…"

Measured: `game(s) of chance` · `game(s) of skill` · `game(s) of passion` each
return **0 hits across all eight subsequent chapters.**

**Reader consequence.** Jordan is given a taxonomy, told the remaining 108,000
words are built on it, and made to perform a sorting exercise on the one cause
she was told to carry through the book. The output of that exercise is never
requested again. The chapter that most needs it is ch9, where she designs her
own game and the Chance/Skill/Passion distinction would tell her which parts of
her design she can control.

**Why structural, not preference.** The sentence is a falsifiable claim about
the book's architecture, and the book falsifies it. No rewording of `ch1:149`
makes the taxonomy load-bearing; either later chapters use it or the claim is
withdrawn.

**Disposition — fix locally.** `ch1:149`'s "everything ahead" can become an
accurate claim about what ch1 itself does, at a cost of roughly one sentence.
Seating the taxonomy across eight chapters is second-edition work.

**Disproving evidence.** The three games carried under other vocabulary —
*luck*, *practice*, *love* — doing the same discriminating work in later
chapters. A loose search did not find it, but this is the finding most exposed
to a synonym I did not think to check.

---

## A2 · The character sheet promises a line every chapter and collects two

**Locations.** `ch1:197`, `ch1:207`, `ch2:560`, `ch9:682`. Nothing in ch3–ch8.

> `ch1:207` — "That is the sheet for now. It fills in as you play: a superpower
> you will only spot in motion, an autopilot pattern you will catch yourself
> running, **a line added in every chapter ahead.**"

> `ch2:560` — "**Add a line to the sheet before you go.** In Chapter 1 you wrote
> down the myth that runs you hardest… Underneath it, write the daemon that took
> the joystick first…"

> `ch9:682` — "you have just watched your autopilot run. **Chapter 1 told you
> this would happen and left a line open on your character sheet for it.** Fill
> it in now…"

Promised: eight additions, one per chapter after ch1. Delivered: **two — ch2 and
ch9**, with six consecutive silent chapters between them.

**Reader consequence.** The character sheet is the book's record of the reader's
own transformation, and it is the artifact ch9 turns back to at the close. When
ch9 says *Chapter 1 left a line open for this*, it is addressing a reader whose
sheet has four entries from ch1 and one from ch2, not a filled page. The payoff
machinery is built for an accumulation the middle of the book never performed.
This is also the book's answer to its own diagnosis — Jordan's stated drop-off
trigger is claims without practice.

**Why structural, not preference.** The defect is distributed across six
chapters and located in none of them. `ch1:207` is not wrong as a sentence; it
is wrong as a description of ch3 through ch8.

**Disposition — structural decision required.** Either narrow `ch1:207` to
promise what the book delivers, or seat one sheet line at the close of each of
ch3–ch8. The second is six insertions of two to three sentences each, at the
existing chapter-end position ch2 already models — the pattern is written, it
simply stops. **Recommend the second if any prose work happens after ship**; it
is the highest reader-value-per-word item in this scan and ch2:560 is the
template.

---

## A3 · One of the ten myths is never taken apart

**Locations.** `ch1:68`, `ch1:73`.

> `ch1:68` — "every one of these myths is a solvable puzzle, and **this book
> hands you the moves to take each one apart.**"

The ten, mapped against where each is dismantled:

| Myth (`ch1:72–81`) | Taken apart at |
|---|---|
| being good *(master)* | `ch1:91` — the definition replaces it |
| **helping the less powerful** | **nowhere** |
| fixing the problem | `ch6:325`, `ch6:533` |
| sacrificing yourself | `ch5:442` |
| paying down what you owe | `ch1:30`, `ch1:34` — the debt frame |
| being seen doing it | `ch1:119` — the applause counter |
| saying the right words | `ch3:671` |
| following the right people | `ch4:525`, `ch4:727` |
| never causing harm | `ch7:120`, `ch7:463`, `ch7:703` |
| having the right framework | `ch8:470`, `ch8:674` |

*helping the less powerful* returns **zero hits** in ch2–ch9 on a loose search
(`less powerful`, `the powerless`, `helping the less`).

**Reader consequence.** Nine of ten is a strong record, and this is the smallest
finding here — except for which one is missing. *Allyship means helping the less
powerful* is the paternalism myth, the one nearest the book's own definition at
`ch1:91` ("increasing another person's well-being while protecting the
conditions that allow **both of you** to remain full players"). A reader whose
top myth is this one — plausible for Jordan, whose stated fear is *I'm doing more
harm than I know* — is told to write it down in ch1 and never handed the move.

**Why structural, not preference.** `ch1:68` says *each one*. Nine of ten is a
factual gap in a stated inventory, not a stylistic choice.

**Disposition — fix locally.** Either soften `ch1:68`'s "each one", or note
where the reader should take this one apart. It is close to ch7's territory
(harm and the ledger) and to ch5's (sacrifice), and the definition at `ch1:91`
already contains the counter-move.

**Disproving evidence.** A chapter dismantling paternalism without using any of
the searched vocabulary — ch7's harm material is the likeliest place. Worth one
human read of ch7 §3 before acting.

---

## A4 · The altitude colours arrive in Chapter 8, undefined, carrying the ladder

**Locations.** First and effectively only substantive use at `ch8:183`.
`termdebt.py` reports Amber, Orange, Green **NEVER DEFINED**; Teal first used
`ch8:183` and defined `ch8:297`; *altitude* first used `ch3:203`, first defined
`ch7:652` — four chapters of debt.

> `ch8:183` — "Call it *committed seeing*: the capacity to take in **all the
> altitudes — Red, Amber, Orange, Green, Teal** — and still choose to stand
> somewhere."

**Reader consequence.** The sentence asks Jordan to hold a five-term
developmental scale she has never been taught, in the chapter that is supposed
to be her integration. Jordan's #1 documented drop-off trigger is *jargon
without translation*, and this is a five-term scale introduced 100,000 words in.
Two further problems in the same line: the list omits **Magenta**, which appears
zero times in the manuscript though the project's own face table assigns it to
the Shaman, so the ladder named at `ch8:183` does not match the book's six
faces; and the retired Key Terms glossary was where these colours used to be
defined, so retiring it removed the only definition surface without moving the
definitions.

**Why structural, not preference.** A missing prerequisite, arriving eight
chapters after first use, in the chapter that depends on it most.

**Disposition — structural decision required.** Three options: define the scale
where it is first needed; cut the colour vocabulary from `ch8:183` and let
*altitude* carry the idea unlabelled, which costs one clause; or route the
reader to a definition surface. **Cutting is the cheapest and loses least** —
the sentence works without the five colour names.

---

## A5 · The four allyship domains are a taxonomy in ch3 and defined only in an appendix

**Locations.** `ch3:772`, `ch3:791`, `ch3:795`, `ch3:799`. `termdebt.py`:
**NEVER DEFINED** in body text. Definitions live in
`appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md` (3,122 words).

> `ch3:772` — "The parable showed **one of the four: Direct Action**, the true
> thing said to a face."

> `ch3:791`, `703`, `707` — "**Raise Awareness** — the true thing over the right
> thing" · "**Gather Resources** — the real need named" · "**Skillful
> Organizing** — the thing the group won't say"

**Reader consequence.** "One of the four" is a back-reference to a set the
reader has not met. She meets four bolded domain names used as though already
defined, in her first teaching chapter. The appendix that defines them sits
110,000 words later and nothing at `ch3:772` points to it — unlike `ch3:415`,
`ch3:560`, and `ch3:589`, which each route the reader to an appendix by letter.
The routing convention exists in this very chapter and is not applied here.

**Why structural, not preference.** A prerequisite in the wrong location. The
fix is a placement decision, not a wording one.

**Disposition — fix locally.** One appendix pointer in ch3's existing italic
convention closes it. The three sibling pointers in the same chapter give the
exact form to copy.

---

## A6 · The book's one process is promised in ch1, missed in ch2, and assumed in ch3

**Added 2026-07-31 after the chapter passes.** This finding came out of the ch1,
ch2 and ch3 scans converging on the same seam from three directions, and it was
re-verified directly before being written here. **It outranks A1–A5.** Chapter 1
stakes the whole book on there being one repeatable process; this is that
process, and its introduction is misrouted across three chapters.

**Locations.** `ch1:191`; `ch2:476`–`ch2:500`; `ch3:242`, `ch3:244`, `ch3:824`.

> `ch1:191` — "You already have the process that runs every one of these faces:
> **the loop you meet in the next chapter.** Each Game Master takes a chapter to
> teach you their game, **and the loop is how you play it.**"

The next chapter does not contain it. What `ch2:476` delivers is *Five Moves for
the Threshold* — Spot who's holding the joystick · Thank it for the job · Name
the cost · Take the joystick · Log the tape. Those are daemon-handling moves,
and they are good, but they are not the loop that runs the Face chapters. They
return **zero hits in ch1 and in ch3–ch9.**

The loop that actually spines the book is the **WAVE-Spiral**, first named at
`ch3:242` and defined at `ch3:244` — one chapter later than promised.

Measured, the five stage names across the manuscript:

| | ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|---|
| Wake Up | **0** | **0** | 4 | 4 | 2 | 3 | 3 | 3 | 1 |
| Open Up | **0** | **0** | 8 | 3 | 4 | 3 | 5 | 3 | 1 |
| Clean Up | **0** | **0** | 5 | 5 | 2 | 5 | 3 | 3 | 1 |
| Grow Up | **0** | **0** | 4 | 3 | 2 | 3 | 3 | 5 | 1 |
| Show Up | **0** | **0** | 5 | 5 | 4 | 4 | 4 | 4 | 1 |

Then the third beat, which is the one that will cost the reader:

> `ch3:824` — "The deck runs five basic moves, and **you already know all five**,
> because they are the WAVE-Spiral: Wake Up, Open Up, Clean Up, Grow Up, Show
> Up."

**Reader consequence.** Jordan is told in ch1 that one repeatable process is
"the whole design of the book" (`ch1:60`) and that she will meet it in ch2. She
meets a different five in ch2. She meets the real one 580 lines into ch3 and is
then told she already knew it. Being told you already know something you were
never taught is the precise experience the book is written against, and it lands
on the reader whose documented drop-off trigger is *jargon without translation*.
It also undercuts ch1's strongest promise — *you do not have to learn everyone,
you learn one process* — at the moment that promise should be paying off.

**Why structural, not preference.** Three chapters disagree about what the book's
central mechanism is and when the reader receives it. No single sentence is
wrong in isolation; the defect is the routing between them.

**Disposition — fix locally, and it is cheaper than it looks.** No content is
missing. Ch2's five moves are real and earn their place; ch3 teaches the
WAVE-Spiral properly. Three edits close it: point `ch1:191` at where the loop
actually arrives, name ch2's five as what they are rather than as the loop, and
cut the false prior knowledge at `ch3:824`. **Recommend all three regardless of
what else happens**, because this is the book's own central claim about itself.

**Disproving evidence.** A reading in which "the loop" at `ch1:191` legitimately
refers to ch2's threshold moves — arguable, since both are five-beat and ch2 is
where she first runs anything. That reading still leaves `ch3:824` asserting
knowledge of a different five she has not been taught.

---

## Not findings, recorded so they are not rediscovered

- **`chain2.py` "ch1–ch4 no moves"** — parser artifact; ch3–ch9 each carry five.
- **The single bare claim, `ch8:603` "Hold the Meta Without Losing the Ground"
  (299w)** — real but line-level, and belongs to the chapter pass, not here.
- **`winning-when test` appears 4× in ch3 and nowhere else** — a convention that
  starts and stops. Below the Architect threshold; logged for the ch3 pass.
- **ch7 carries zero do-it-now headings**, the only chapter with none. Logged
  for the ch7 pass.

## For the Continuity and Claims Auditor, not the Architect

**The myths change grammatical form between the list and the teardowns.** ch1
lists them as *Allyship means X* (`ch1:72–81`) and the reader is told to write
one down. They are dismantled as *allyship is X* (`ch4:525`, `ch5:442`,
`ch6:325`) and *allyship is a matter of X* (`ch4:727`, `ch6:533`, `ch8:470`,
`ch8:674`). Only ch7 keeps *means* (`ch7:120`). Terminology drift on the item the
reader was instructed to copy verbatim onto her character sheet.
