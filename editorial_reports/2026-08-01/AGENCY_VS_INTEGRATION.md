# Compare and contrast — Wendell's patterns against the measured one

> **Updated 2026-08-01, batch five.** A third pattern arrived and it is neither of
> the two below: **the prose explains itself before it is challenged.** 81 sites,
> `instruments/preempt.py`, board in `PREEMPT_BOARD.md`. It is independent of both
> the agency defect and the integration cost, which now makes three separate
> passes. See §8.

Wendell, 2026-08-01, asked for his read-through findings to be set against what
the instruments have been asserting. This is that comparison. Two real defects,
and they turn out **not** to be the same defect, which was my prediction and was
wrong.

---

## 1 · What his twelve notes have in common

Nine of the twelve are one thing, and he named it himself in note N29:

> *"definitions don't ask things of people. The book in general has a
> misattributed agent problem."*

| Line | Who is acting |
|---|---|
| the guilt never **tells** you | an emotion, performing a speech act |
| Allyship … **springs** the trap | a practice, setting a mechanism |
| the question **flips** underneath you | a question, moving |
| **It** scores how you actually behave | an unnamed *it*, judging |
| The damage **starts** | an abstraction, beginning |
| The help never **lands** | an abstraction, arriving — and no agent at all |
| Nothing in **it asks** whether you are good / the definition **guards** | a definition, interrogating and protecting |
| the game **would rather** you not notice | a game, preferring |
| I **ran this book** on guilt | a book, run like an engine on a feeling |

**And one runs the other way**, which sharpens the pattern rather than breaking
it. *"You answered those questions with myths"* — his note is that the myths
**emerge** to make sense of hard questions. There the book hands the *reader*
deliberate agency for something involuntary.

So the pattern is not "abstractions act." It is **agency is assigned to whoever
is not doing it** — to the guilt, the game, the definition, or to a reader who
did not choose.

One of the twelve is a different kind of finding: *"Every game runs on a
currency"* is a **claim error**, not an agency defect. What games run on is
attention; *arcade* games run on tokens. That belongs with `rescan.py`'s claim
errors.

---

## 2 · What the instruments asserted

`density.py`, after the hostile review: the reading cost is **integrative, not
decoding**. Measured against the five `VOICE_ANCHOR.md` passages Wendell selected
as the book at its best:

| | book | anchors |
|---|---|---|
| sentence transitions opening on new information | **79%** | 57% |
| propositional idea density | 0.456 | 0.500 |

The prose states rather than connects. Each sentence is short, propositionally
thin, and starts on new material.

---

## 3 · Where they agree

Both say the reader is doing work the prose should have done, and both point at
the same repair: **put a person in the subject and say how this sentence relates
to the last one.** Williams' Paramedic Method — already in `AGENTS.md` as the
standing rule for be-verbs — is the single move that serves both. *Who is kicking
whom.*

Both also fail the same control in the same direction. Against the voice anchors:

| | book | anchors | gap |
|---|---|---|---|
| sentences with no person as subject | **64%** | 54% | 10 points |
| transitions opening on new information | **79%** | 57% | 22 points |

---

## 4 · Where they part, and this is the useful bit

**I predicted misattributed agency would be the mechanical cause of the
integration cost.** The reasoning: a sentence whose subject is an abstraction has
no person in it, so it cannot pick up a person from the sentence before, so it
must open on new information.

Measured directly, that is false:

| Sentence subject | transitions | opens on new information |
|---|---|---|
| a person | 1,640 | **79%** |
| not a person | 2,757 | **78%** |

**One point apart.** A sentence with a human subject is just as likely to strand
the reader. The two defects are independent, which means:

- They need **two passes, not one.** Fixing the agency will not move the 79%.
- The integration gap is **more than twice the size** of the agency gap, measured
  against the same control.
- A sweep that put people into subjects and stopped there would produce a book
  that still reads hard, and would look like it had been fixed.

---

## 5 · Where the instruments failed him

**`prose_diet.py` has had an `agency` check since July. Against Chapter 1 it
returns zero** — the chapter where Wendell found nine agency defects by reading it.

Its pattern requires a literal `the`, then one of twenty listed nouns, then one of
eighteen listed verbs. It cannot match a bare abstract subject (*Allyship springs
the trap*), and its noun list holds none of the abstractions this book is built
from: guilt, shame, help, harm, damage, definition, game, myth, trap. The check
was not wrong; it was too small to find anything, and it had been reporting clean.

`instruments/agency.py` replaces it, on real part-of-speech tags: **207 Tier-1
sites** — an abstraction with a mental or speech verb, which cannot be metaphor —
and 293 Tier-2 candidates where it might be.

**A caveat on the count.** The subject finder walks to the first finite verb and
takes the last nominal before it, so a relative clause fools it: *"The people
you've been most loyal to in this work already knew the vocabulary"* is reported
as `work knew`. The rate is trustworthy; individual Tier-1 sites need a reader.

---

## 6 · What the measurement says that the reading did not

**Chapter 1 is not the worst chapter for this.** It has the *lowest* agentless
rate of the nine at 53%. Wendell found nine defects there because that is the
chapter he is reading.

| ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|
| 53% | 66% | 67% | 62% | 60% | **71%** | **68%** | 59% | 56% |

**Chapters 6 and 7 are where this lives** — the Architect and the Diplomat, which
are also the two most systems-flavoured chapters, where an abstraction acting is
the easiest sentence to write. Appendix A runs 84%.

---

## 7 · What follows

1. **Two passes, sequenced.** Agency first — it is the one Wendell can see and
   rule on, and 207 Tier-1 sites is a finite list. Integration second, and it is
   the bigger number.
2. **The unit differs.** Agency is a sentence-level fix. Integration is a
   *transition*-level fix; rewriting single sentences will not move it.
3. **Read ch6 and ch7 for agency**, not ch1.
4. **The currency claim** (`ch1:101`) goes to `rescan.py` as a claim error.
5. **Do not run these as one sweep.** They score independently, and a combined
   pass would report the agency fix as progress on the reading cost.

---

## 8 · The third pattern — the prose explaining itself

Wendell, batch five:

> *"an emergent pattern is where the work is explaining itself before it is
> challenged. Instead of anticipating objections, validating them and writing the
> text on purpose, we've created modes that collapse that process and make insane
> sentences."*

**81 sites**, in three shapes: 69 meta-narration (`Here is the…`, `I will say it
plainly`), 9 phantom contrast (`the real prize`, `the one nobody can take back`),
1 unfounded appeal (`every arcade you have ever played`), 2 objections staged
inside the claim.

| ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|
| **15** | 2 | 13 | 12 | 4 | 7 | **15** | 2 | 10 |

### It is a third defect, not a face of the other two

- **Not agency.** *"Here is the good news"* has a perfectly ordinary subject. The
  problem is that the sentence announces a move instead of making it.
- **Not integration.** These sentences are heavily connected — over-connected.
  They spend their words on the join and never arrive at the thing being joined.

So: **three passes, three units of work.** Agency is a sentence-level fix.
Integration is a transition-level fix. This one is a *drafting-process* fix —
Wendell's own diagnosis, that anticipating an objection, granting it and answering
it are three acts of writing, and collapsing them into one sentence is what
produces the defect.

### The part that should not have needed a reader

The repository's own `/no-ai-slop` skill has banned this family since it was
written, by name: **throat-clearing openers** (*"Here's the thing," "Let me be
clear"*) and **faux-insight setups** (*"This is the part most people skip," "Here's
what nobody tells you"*).

**No instrument has ever checked for it.** `gate.py`, `line_scan.py`,
`prose_diet.py` and `marginalia/review.py` carry no rule of this shape — grep
returns nothing. The skill is run by hand on new prose; the 69 sites already in
the manuscript predate it and were never swept. That is the same failure mode as
`prose_diet.py`'s agency check reporting zero: a rule exists, nothing enforces it
over the body, and the defect accumulates while the board reads clean.

### Two of the earlier notes belong here

`N05` — *"Here is the part worth sitting with"* — and `N30` — *"Here is the part
the game would rather you not notice"* — were filed under other headings. Both are
this pattern. N30 is both: an abstraction with a mental verb **and** a
faux-insight frame, which is why one sentence can need two different fixes.
