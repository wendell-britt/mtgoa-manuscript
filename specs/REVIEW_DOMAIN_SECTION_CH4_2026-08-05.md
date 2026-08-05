# REVIEW — ch4's domain section against the voice documents

**2026-08-05. Wendell:** *"let's do a review process to make sure this coheres with our
voice documents."*

Ruled against `marginalia/specs/VOICE_SYNTHESIS.md`, `specs/VOICE_ANCHOR.md`,
`marginalia/specs/BALDWIN_VOICE_SPEC.md`, `marginalia/specs/HUMOR_GRID.md`, and
`marginalia/specs/REVISION_INSTRUMENT.md` Part 1. Control: `ch3:806`–`:896`, measured
under a neutral filename so no register exemption fires.

**Ten findings. Two were structural and neither came from the prose.**

---

## The two the voice pass could not have caught, and they blocked it

### F1 · universal move 1 restated a sentence sitting ten lines above it

The draft's first universal move was **Say it once and count the words afterward** —
*"more words than you needed means you were explaining rather than drawing."*

`ch4:708`, the test on Move 5, already reads:

> **The test:** The line left your mouth without an essay, a justification, or an apology
> attached. Count the words afterward: more than you needed means you were explaining,
> whatever they did in response.

**The section's slot is immediately after that line.** The spec says the three universal
moves are *drawn from the chapter's own material rather than invented*; drawn from is not
the same as repeated, and a reader would have met the same test twice inside one screen.

**Replaced with the charge**, which is the chapter's own Stage 1 and was unused:

> **Draw it at the size it arrived.** The charge tells you how big the crossing was, and
> the auditor's first offer is always to round it down: not a line, a note. Not now,
> later. Not you, somebody closer to it.

The three moves now run **Charge · Aim · Stand**, three of the five stages of
`ch4:293`'s own sequence, which is a better spine than three delivery notes.

**Standing rule for the fan-out:** before writing a universal move, grep the chapter for
the sentence. The template's slot sits ten lines from Section 6's last test, in every
chapter.

### F2 · the seam line does not exist outside ch3

`ch3:806` — *"The moves are what you do. The next question is where."* — is the hinge the
spec calls the slot. **ch4 has no such line.** It runs Move 5's test, a rule, and then
`## Your Twenty Cards`. So do ch5–ch8, presumably.

The seam has to be **written**, not found. It ships verbatim, because the book's seams
repeat on purpose: ch4 already reprints ch3's twenty-cards italic block word for word.

### F3 · the callback invented a mechanism the parable does not have

Draft: *the Challenger speaking first at councils **so the rest of the village could say
what it already knew.*** `ch4:70` says the opposite of that:

> The Challenger would speak first at councils. Not because they were the eldest or the
> wisest but because they could say the thing that needed saying **before anyone else
> could bear to hear it.**

Corrected to canon. The village was not waiting to speak; it could not stand to hear it.

---

## The voice findings

### F4 · the Tell announced its own punchline and then delivered it five more times

The draft opened the Tell with *"a line drawn for the record looks exactly like a line
drawn for the outcome"* — then forked all four bullets on record-versus-outcome, then
closed on **the line drawn for the record instead of for the outcome.**

`VOICE_SYNTHESIS` move 16: **the punchline goes last.** ch3's canon withholds the fork
entirely until the closing line. Rewritten to match: the opener now names the exposure
without naming the fork, and the closer states it once, where it lands.

### F5 · one thousand words with no laugh in them

**This is what `VOICE_ANCHOR` anchor 3 exists to catch.** The anchor is in the set
deliberately — *an anchor with no comedy in it will let the Voice Guardian approve a book
that has stopped being funny.* The draft passed every counter and had no comedy anywhere.

And ch4 is the wrong chapter to lose it in: `ch4:117` is the anchor passage itself, the
I-statements bit, the Humor Grid's **Jerk** working on the page.

Two beats added, both aimed at a practice and never at a person:

> Adding a softener is taking it back. So is a joke. So is *does that make sense?* — a
> question that has never once been about whether it made sense.

> a Challenger who draws a line so that a line will have been drawn has run the assessment
> at a higher volume.

The first lands **last in its paragraph**, per move 16. The second sits second-sentence,
which is where ch3's own *"with better production values"* sits — **matching the
template's placement over the general rule, on purpose, recorded here.**

### F6 · two meta-narrations

*the most expensive four seconds **in this chapter*** and *the Challenger comes second
**in this book*** — both the class `preempt.py` scores, and both mislocate the thing: the
silence is in her week, not in the chapter. Now *in any of the four domains* and *comes
second for a reason.*

### F7 · "the count is the tell" collided with `### The Tell`

Twenty-eight lines apart, one of them a heading. Gone with F1.

### F8 · the load-bearing paragraph had no short sentence in it

Five long sentences and nowhere to breathe. ch3's equivalent carries **Both keep the true
thing unsaid.** Split *"which is why it lasts for years"* off into **That is why it lasts
for years.**

### F9 · two hedges in one paragraph

*often* and *almost*. Cut *often*; **more accurately than anyone else at the table** is
the stronger claim and it was being apologised for.

### F10 · no first person anywhere — and ch3's section has none either

Not a defect against the template. Recorded because it is a **set-level** question:
`VOICE_ANCHOR` observes that three of the five anchor passages carry the admission inside
the teaching, and the P0 loss recorded on 2026-07-31 was exactly a chapter running thin
on testimony. **Five new sections at ~1,100 words each is 5,500 words of instruction with
no author cost in it.** At least one should carry a first-person beat. **Wendell's call.**

---

## The board, and what the control says about it

| | gate | be | copula | waste | zombie | expletive | passive | empty | inchoative |
|---|---|---|---|---|---|---|---|---|---|
| **ch4 draft** | PASS | 0.76 | 1.17 | 1.04 | 0.94 | **1.57** | 0.57 | 0.76 | 0.00 |
| **ch3 canon, control** | — | 0.86 | 1.16 | 0.87 | 0.87 | 1.14 | **1.79** | **1.58** | **1.68** |

**The control runs heavy on three counters and the draft on one.** That is the useful
number here: measuring a new section against the book baseline alone would have called
ch3's own shipped template a defect three times over.

**expletive 1.57 is two sentence-initial occurrences in 1,124 words**, and both are ruled:

- *It is only more satisfying.* — the anchor-1 move, a four-word turn after a long
  sentence. Cutting the expletive costs the beat.
- *It is also the easiest thing in the world to lie to yourself about…* — **ch3's own
  sentence**, carried across so the five sections read as a set.

A short section makes a small count into a large ratio. Two instances is the finding.

### `draftprobe.py` — 12 hits, and every class appears in the control

| hit | ruling |
|---|---|
| definite-article series · determiner run | the template's own form; the determiner run **is** `ch3:806` |
| `[the safety] of the accurate private complaint` | deliberate echo of ch3's *the safety of the accurate private read* |
| `[the thing] that needed saying` | `ch4:70`'s own words, licensed by its relative clause |
| `[them]`, `[that]` orphan pronouns | **the identical sentence fires identically in the control** |
| `you did · you drew · you have been` | the section addresses a reader who has done reps |
| `[limit said]`, `[resources said]`, `[markers asked]` | ch3 fires the same three on its own glosses |

**Two hits were mine and both are fixed:**

- **`the size of the thing`** — an empty noun with no antecedent, the exact class Wendell
  caught by eye on 2026-08-03. Now **the size of the crossing**, named nine words earlier.
- **`the refusal that protects somebody's capacity`** — a refusal does not protect
  anybody; a person does. `agency.py` scored it *candidate volitional* three times. Now
  **the no said in your own name**, which is nominal, parallel to *the limit said to the
  person crossing it*, and is the chapter's own governing phrase (`ch4:115`, the clean
  no). The capacity claim was already carried by the marker.

`gate` PASS · `fragment` clean · `preempt` clean.
