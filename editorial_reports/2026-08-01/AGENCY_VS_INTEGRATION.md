# Compare and contrast — Wendell's patterns against the measured one

> **Updated 2026-08-01, batch five.** A third pattern arrived and it is neither of
> the two below: **the prose explains itself before it is challenged.** 83 sites,
> `instruments/preempt.py`, board in `PREEMPT_BOARD.md`. It is independent of both
> the agency defect and the integration cost, which now makes three separate
> passes. See §8.
>
> **Updated again, batch six.** A fourth, and the cheapest: **surface shapes that
> stand in for a plain statement** — binary contrast, definite-article series,
> determiner run. 221 sites, `instruments/shapes.py`, board in `SHAPES_BOARD.md`.
> All ten notes in that batch land in one section, `ch1:131`–`151`. See §9.

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

`instruments/agency.py` replaces it, on real part-of-speech tags: **177 Tier-1
sites** — an abstraction with a mental or speech verb, which cannot be metaphor —
and 285 Tier-2 candidates where it might be.

**Revised down from 207/294 on 2026-08-03**, when Wendell ruled the seven daemons
into ANIMATE. They had been absent while the six Faces were present, so 30 Tier-1
sites and 9 Tier-2 candidates were the book's own deliberate personification
being counted as defects — `ch2:248` defines a daemon as a part that runs on its
own, and Section 7's walk is *The Protector has the joystick* seven times over.
The agentless rate moves 63% to 61%, and the five voice anchors 54% to 46%.

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
   rule on, and 177 Tier-1 sites is a finite list. Integration second, and it is
   the bigger number.
2. **The unit differs.** Agency is a sentence-level fix. Integration is a
   *transition*-level fix; rewriting single sentences will not move it.
3. **Read ch6 and ch7 for agency**, not ch1.
4. **The currency claim** (`ch1:101`) goes to `rescan.py` as a claim error. **Done** —
   filed as `CL-1` in `CLAIM_ERRORS.md`, and `rescan.py` reads every dated report
   directory now instead of only `2026-07-31/`, which is why it could be filed at all.
   Two prior passes read that sentence closely and neither asked whether it was true;
   the earlier of them graded it **✅ STRONG**.
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

---

## 9 · Batch six — the shapes, and one number that was worse than the note

Ten pastes, `N37`–`N46`. **All ten land in one stretch: `ch1:131`–`151`, which is
the whole of the *Why a Game* section.** The section runs twelve paragraphs and ten
of them are flagged. That is worth saying before any pattern is named — the unit
Wendell is reacting to here is a section, not a set of lines.

### The three-years mention is worse than the note says

`N41`: *"this is the third time we talk vaguely about the 3 years thing and it's
reading as repetitive in a book that's already overlong."*

It is the **sixth** time, all in Chapter 1:

| line | how it lands |
|---|---|
| `ch1:4` | *This book is three years late.* |
| `ch1:10` | *I was holding myself hostage.* |
| `ch1:87` | *I ran it for three years while writing a book that told other people not to.* |
| `ch1:109` | *For three years I ran this book on guilt.* |
| `ch1:141` | *When I said I held myself hostage for three years…* |
| `ch1:187` | *I kept this very book in conversation for three years.* |

*Three years* also lands twice in the author's note before the chapter starts
(`:9`, `:25`), carrying a different claim — the burnout timeline — so a reader meets
the number twice in one sense and six times in another before Chapter 2.

### Three surface shapes, none of which had an instrument

`instruments/shapes.py`, board in `SHAPES_BOARD.md`. **221 sites.**

| Shape | sites | Wendell's words |
|---|---|---|
| binary contrast | 56 | *"Not X but Y — simplify"* (`N38`) |
| definite-article series | 50 | *"definite articles creeping in in a repetitive way with no referent"* (`N39`) |
| determiner run | 115 | *"more of the sentence fragments and definite articles"* (`N42`) |

**Chapter 1 carries 10 of the 50 definite-article series — more than any other
component**, and three of them are inside this one section (`:135`, `:141`, `:151`).
Wendell's question was whether the rule on *the* needs to be stricter. On this
evidence the answer is that the shape concentrates exactly where he is reading.

**The binary-contrast count needs one deduction.** Five of the 56 are the same
sentence — *The tell that a quest is alive is not enthusiasm. It is anticipation
with some dread underneath it.* — closing the quest section of five chapters. That
is one decision, not five defects. It also drifts once: `ch4:744` says *It arrives
as anticipation*, so the refrain is inconsistent in exactly one place.

### The third time a banned family has been found accumulating unmeasured

`/no-ai-slop` bans binary contrasts by name and has since it was written:

> **Binary contrasts.** *"This is not X. It's Y." / "The question isn't X, it's Y."*
> State Y directly.

No instrument checked. That is the same failure as `prose_diet.py`'s agency check
returning zero and as the 69 unmeasured meta-narration sites — but this one has a
sharper edge. **The batch-edit scripts in `instruments/` have repeatedly rewritten
*into* the shape.** `w9_ch5.py:254` turns

> `Not because they're perfect — because removing them would break something real.`

into

> `Not because they're perfect. Because removing them would break something real.`

The em-dash was the target and the em-dash is gone. The binary contrast passed
through the edit untouched, and now reads as deliberate. `w8_batch_a.py`,
`w8_batch_b.py`, `w9_ch4.py`, `w9_ch8.py` and `dl19_moves.py` all do the same thing.
A pass that fixes punctuation inside a banned shape launders the shape.

### One note that is the agency defect again, and one that is bigger than a note

`N43` — *"A game turns the lights on… A game turns it into wonder"* — is `agency.py`
Tier 2 exactly: an abstraction performing a volitional act. Wendell's correction
names the repair precisely: *a game sets the conditions for the players to do this,
or you could even say game designers do.*

Then he goes past the line: **"The larger game is figuring out how to find out who
the designers are and change their game."** That is not a sentence fix. It is a
claim about what the book is for, and Chapter 1 does not currently make it. Filed
with `N43` and flagged here because it is the only note in six batches that proposes
an argument rather than repairs one.

### And one shape that belongs to the pre-emption pass

`N40` — *"The third reason changes everything:"* — *"don't announce what it changes.
If it isn't obvious then we're projecting."* `preempt.py` missed it: no
throat-clearing opener, no phantom comparative. It grades its own payload instead. A
**stakes announcement** shape has been added; it finds **2 sites, both in ch1**, which
is the right size for a shape this specific.

### Where this leaves the pass count

Four now, not three, and the fourth is the cheapest:

1. **Agency** — sentence-level, 177 Tier-1 sites.
2. **Integration** — transition-level, 79% against a 57% control. The biggest.
3. **Pre-emption** — drafting-process-level, 83 sites.
4. **Surface shapes** — phrase-level, 221 sites, and the only one of the four a
   reader can rule on at a glance. It is also the only one with a written rule
   already in the repository that nothing was enforcing.
