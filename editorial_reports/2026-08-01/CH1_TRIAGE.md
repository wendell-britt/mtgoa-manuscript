# Chapter 1 — the 41 open notes, grouped by defect

**2026-08-03.** Wendell: *"group them by defect first."* The notes were filed in
reading order, which is how they arrived and the wrong order to work them in: six of
them are one decision, and eight more are another.

**Two rulings collapse 16 of the 41.** Groups C and D need no ruling at all — they are
mechanical, they all have instrument coverage now, and they can be swept in one pass.
Group E is the expensive one and it is where the real editorial judgement lives.

---

## A · The opening tells the reader who they are — **8 notes, 1 ruling**

`N12` `N13` `N14` `N15` `N16` `N17` `N18` `N21`

Every one of these is the same move at `ch1:16`–`:30`: the book opens by asserting the
reader's history and rank.

| | |
|---|---|
| `N12`–`N14` | *You are a Game Master. You have been running your own allyship campaign for years.* Cut or explain; clunky; reason withheld |
| `N15` | *You have done this before.* **"Done what before? Hates all intros like this."** |
| `N17` | *That was the beginner's game. You graduated from it years ago.* A claim about the reader's rank |
| `N18` | *You've had the conversations. You've done the reading. You've carried the weight.* Also robotic rhythm |
| `N21` | *You answered those questions with myths.* Agency assigned to the reader for something involuntary |

**`N16` already contains the ruling and it is the most valuable sentence in the whole
note file:**

> *It assumes a secret competence, which is not the point of the book. Unconscious
> skills can be brought to bear, but what people actually experience is a pressure to
> do good that they cannot satisfy.*

So the question is one thing: **does the opening stop flattering the reader and start
naming the pressure?** Rule that once and all eight rewrite together, because they sit
in six consecutive paragraphs.

`assumed.py` measures the class: **ch1 runs 36 assertions against 1 invitation**, the
worst ratio in the book.

---

## B · Misattributed agency — **8 notes, 1 ruling**

`N22` `N23` `N24` `N27` `N29` `N30` `N43` `N45`

Wendell named this himself at `N29`: **"The book in general has a misattributed agent
problem."** `agency.py` exists because of this note.

| | |
|---|---|
| `N22` | *guilt tells you* — guilt is a signal, the feeling that you are bad is the myth |
| `N23` | *allyship springs a trap* — it does not spring anything |
| `N24` | *the question flips* — it does not flip |
| `N27` | *where help lands* — no agent in the sentence |
| `N29` | *the definition asks* — definitions do not ask things of people |
| `N30` | *the game wants* — **"Games can't want things like this. We're talking about the shadow game designers."** |
| `N43` | *a game turns the lights on* — **"A game sets the conditions for the players to do it, or the game designers do."** |
| `N45` | *a game turns it* — same |

**`N30` and `N43` both point at the same replacement: the designers.** That is not a
copy-edit, it is a claim the book has never made, and Wendell flagged it as possibly
load-bearing:

> *"The larger game is figuring out how to find out who the designers are and change
> their game."*

**The ruling: does ch1 name the designers?** If yes, eight sentences get a subject and
the book gains an argument. If no, eight sentences get rewritten around the abstraction
and nothing is gained but accuracy.

---

## C · Pre-emption and throat-clearing — **6 notes, no ruling needed**

`N33` `N35` `N36` `N40` `N44` `N47`

All six are cuts or near-cuts, all six have instrument coverage, and none needs a
decision. `preempt.py` catches five of them by name today; three of its shapes were
added *because* of these notes.

`N33` is the odd one — *the real prize is the one nobody can take back* is a phantom
contrast whose other half was never established, so it needs a replacement rather than
a deletion.

---

## D · Surface shapes — **4 notes, no ruling needed**

`N37` `N38` `N39` `N42`

The `shapes.py` family, and the instrument was built from these four notes.
`N38` binary contrast, `N39` and `N42` definite-article series, `N37` a verb run to cut.
Book-wide there are 27 binary contrasts and 48 definite-article series; **ch1 carries
10 of the series, the most of any component.**

---

## E · Passages that need rewriting rather than repair — **5 items, and the real cost**

| | | |
|---|---|---|
| `N28` | the scoreboard passage | **CUT**, ruled |
| `N34` | the prize passage `ch1:121` | *"Whole passage needs rewriting"* — the reader does not know what line was held or what was repaired |
| `N45`+`N46` | `ch1:149`–`:151` as one stretch | **ELI5 needed** |
| `N41` | the three-years story | Lands **six** times in ch1 (`:4 :10 :87 :109 :141 :187`) plus twice in the author's note. Condense |
| `N65` | *Which Game Are You Playing* | **Structural.** Theory end to end. Two epiphany bridges, in different places. `EPIPHANY_BRIDGE_CH1.md`. **Blocked on two memories from Wendell** |

**`N41` interacts with group A.** The three-years repetition and the assumed-competence
opening live in the same paragraphs, so the opening is one job rather than two.

---

## F · Singles — **10 notes, mostly small**

| | |
|---|---|
| `N08` | *made me feel like a worse ally* |
| `N09` | add a contraction |
| `N10` | flagged, reason withheld |
| `N11` | *This is me showing up* — what is *this*? |
| `N19` | the game frame is used before it is set up |
| `N20` | *do not come empty-handed* — denying negation, and what was in their hands is never said |
| `N25` | the diagnostic parenthetical — non-specific *it* |
| `N26` | *the problems begin when one of them becomes the whole definition* |
| `N31` | **CL-1, a claim error.** Games run on attention; arcade games run on tokens. `CLAIM_ERRORS.md` |
| `N32` | *run a book on an emotion* → *I used the energy of guilt to write the book* |

---

## The order that costs least

1. **Rule A and B.** Sixteen notes, two decisions, and B may hand the book an argument.
2. **Sweep C and D.** Ten notes, no decisions, one pass, every one instrumented.
3. **Work F.** Ten small ones, independent of everything else.
4. **Then E**, which is the writing, and `N65` stays blocked until Wendell supplies the
   two memories the epiphany bridges need.
