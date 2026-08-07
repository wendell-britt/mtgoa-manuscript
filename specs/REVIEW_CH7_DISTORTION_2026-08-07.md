# Review pass — ch7's Distortion section, lifted from `swmp78`

**2026-08-07.** The section was written on the branch on 2026-08-01 and has never been
reviewed. It predates the `thing` promotion, the beat-placement rule and this session's
diet baseline. **Not applied** — taking it requires the Section 1/2/3 restructure, which
is Wendell's decision.

## Scores

**Control: the five existing Distortion sections** (ch3 ch4 ch5 ch6 ch8), 3,892 words
concatenated. The right comparison, because these are one genre and the expository
baseline is not their ruler.

| | `be` | `copula` | `waste` | `zombie` | `expletive` | `passive` | `empty` | `inchoative` |
|---|---|---|---|---|---|---|---|---|
| raw (branch) | 0.37 | 0.45 | 0.86 | 1.08 | 0.00 | 0.00 | **1.15** | 0.00 |
| **cleaned** | **0.29** | **0.16** | **0.89** | **0.78** | 0.00 | 0.00 | **0.63** | 0.00 |
| the five controls | 0.55 | 0.33 | 0.83 | 1.04 | 0.00 | 1.02 | 0.60 | 2.64 |

**Cleaned reads under the control on six of eight and matches it on the other two.**
`waste` 0.89 sits inside the 0.5–0.9 band, which is the counter with a floor as well as a
ceiling. `gate` PASS. `empty_head` 0 on both tiers. No get-passives, no back-pointer
openers, no first-person plural, no second person.

**340 words against a control range of 537–1186.** ch7's Distortion would be the shortest
of the six by a wide margin. **Flagged and not padded** — inventing a paragraph to hit a
length is the `eval.md` check-1 failure.

## Defects found

**Two that the instruments caught, and both were mine, not the branch's.**

- **`gate` FAIL on `thing`.** My first cleaned draft wrote *"the only thing care was ever
  for."* The word I have been sweeping out of the book all session, put back in by the
  repair pass. Now *"which is what care was always for."*
- **`zombie` 1.35, and it was noise.** Four of seven hits were the `-tion/-ence/-ness`
  suffix heuristic firing on ordinary nouns — *the sentence*, *the question*, *the pattern
  kindness*. **At 340 words the sample is barely above the floor where these counters mean
  anything**, and the fix for the real regression (an expletive construction I had
  introduced) took it to 0.78 on its own.

**Six in the branch's text.**

1. **`preempt`: *"Here's what happened after the Diplomat left:"*** — `\bHere's (?:what|
   where|the)\b`, the meta-narration opener ch1 shed ten of this session. **`preempt.py`
   reported the draft clean because it is board-only** — it ignored the file argument and
   scored the shipped book, the same defect `gate.py` had until 2026-08-05. Found by
   running its regex directly.
2. **A person wobble.** *"arrival became an audition: **you** showed up with a contribution
   ready"* — one second-person clause in an otherwise third-person passage. Two of the five
   controls use `you` only inside quoted speech; ch3 and ch5 address the reader throughout.
   A single bare `you` belongs to neither pattern.
3. **A banned word routed around.** *"makes a **waiting area** rather than a warm place."*
   The sentence wants *waiting room*; `room` is banned; a synonym went in that does not
   collocate and means less. **The ban exists to force a rebuild.**
4. **The closer restated the section's own subtitle.** *"This is what the village does with
   honest terms when the Diplomat is gone"* against the heading four paragraphs up: *What
   the Village Does With Honest Terms When the Diplomat Is Gone.* Same class as `ch3:893`,
   fixed this morning.
5. **A noun that switched mid-argument.** *"What it did not have was a **way** to keep
   people through either one, and the fastest substitute for a **practice** is a mood."*
   `way` is also on the `empty` list.
6. **A mixed metaphor with no doer.** *"Underneath ran a slow leak: the people who held the
   village together did it without saying so"* — a leak does not run underneath, and the
   sentence then makes the leak into the people.

## What the pass did not change

**No claim, example, or figure was added.** Two places changed the image and both are
called out below rather than buried.

**The five moves stay ch7's own.** Checked against all thirty named moves in the book: the
absences the section describes are ch7's Move 2 (*Translate Across Camps* → camps getting
louder in their own languages), Move 3 (*Close with Honest Terms* → another session
scheduled), Move 4 (*Repair After Rupture* → nobody went back), and Move 1 (*Name the
Field* → warmth and vagueness). **No move is borrowed from another Face**, which is the
step-3.5 failure that pulled a ch5 draft to the Sage's altitude.

## The diff

| | branch | cleaned |
|---|---|---|
| 1 | **Here's what happened after** the Diplomat left: the village didn't stop needing people to stay. It just stopped knowing how to say what staying would cost. | After the Diplomat left, the village still needed people to stay. It had stopped knowing how to say what staying costs. |
| 2 | Newcomers still arrived, and arrival became an audition: **you** showed up with a contribution ready | Newcomers arrived and **had to audition**: they came bearing gifts *(image changed)* |
| 3 | **Ruptures hardened by default**, and when **people** stopped turning up | **Nobody went back after a rupture**, and when **the injured** stopped turning up *(doer supplied; "the injured" names who, which the original's logic already required)* |
| 4 | What it did not have was a **way** to keep people | What neither one gave it was a **practice** for keeping people *(matches "substitute for a practice" three words later)* |
| 5 | **Underneath ran a slow leak:** the people who held the village together **did it** | **Underneath it,** the people holding the village together **carried it** |
| 6 | which the village **experienced as a series of** unrelated departures | which the village **read as a run of** unrelated departures |
| 7 | **Notice** what the village kept and what it **dropped** | **Look at** what the village kept and what it **traded** |
| 8 | **What it lost was impact, meaning anything the caring was supposed to move.** | **It gave up impact, which is what care was always for.** |
| 9 | makes a **waiting area rather than a warm place** | **keeps everybody comfortable and moves nobody** |
| 10 | **This is what the village does with honest terms when the Diplomat is gone:** it stops believing | **So** the village stopped believing |
| 11 | **The village never noticed. It** called the pattern kindness | **Nobody noticed. The village** called the pattern kindness |

**Untouched, because they are the section's payload:** *the fastest substitute for a
practice is a mood* · *a count kept long enough starts to feel like a position* ·
*Presence became unconditional, which sounds like love and works like a tax.*

## What taking it still costs

**It cannot be dropped in.** Conforming ch7 to the Face form renames Section 1 to *The
Exile* and pushes the current Section 1's thesis paragraphs down into Section 3.
**`ch7:63`'s thesis and this section's closer make the same argument** — *a staying which
cannot name its terms is a staying without weight* against *presence becomes unconditional,
which sounds like love and works like a tax.* One of them has to give.

**And the branch's ch7 has no 3-2-1 sections**, because it forked before master added
ch7's two. Every one of the six Face chapters has exactly two. The section can be lifted;
the surrounding restructure cannot be taken wholesale.
