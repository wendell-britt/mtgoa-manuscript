---
name: mtgoa-review
description: Run the MTGOA review pass on prose before it lands in the manuscript. Use after generating or rewriting ANY prose for this book — a chapter passage, an Example, a handbook, a margin note, front matter — and before applying it or committing. Also use when asked whether a draft is heavy, wordy, slop, or off-voice.
---

# The MTGOA review pass

**This runs after every generation. Not sometimes.**

The rule exists because it was broken. On 2026-07-31 Wendell read a batch of freshly written
Examples and said: *"this is doing a lot of the things with the definite article and too many
'is' and such. Do we have a repeatable review process that should be being applied after we
generate text?"* The instruments existed. The sequence did not, and `prose_diet.py` — the one
that measures exactly what he had caught — had not been run once on any prose generated that
session. Three pieces had already shipped heavy.

## Do this

```
python3 instruments/review.py DRAFT_FILE        # before it lands
```

Then read the output and act on it, in this order.

**0 · ELI5 first — write the passage twice.** Before drafting in register, write the
same passage the way you would explain it to a five-year-old. Plain words, a person
doing something, no house vocabulary. Then write the register version, and keep the
ELI5 open beside it.

Two things fall out, and both are cheap:

- **If you cannot write the ELI5, you do not have the passage yet.** Stop and work out
  what it says before spending words on how it says it.
- **The diff between the two versions is the audit.** Every word in the register version
  that is not in the ELI5 is either doing work or it is style. Ask which, one at a time.

Wendell, 2026-07-31, after an ELI5 explained a passage better than the passage did:
*"These ELI5 are violating the stylistic rules, but they are getting at the essence. We
need to split the difference on this."* Measured on that pair, the ELI5 broke exactly one
counter — `waste`, at 1.42 against the chapter's 0.58 — and it broke it because it used
pronouns, which is the same reason it was readable. The register draft that scored 0.06
on the same counter was the unreadable one.

**So `waste` has a floor as well as a ceiling.** Aim for the chapter's own band, roughly
0.5 to 0.9. A passage that almost never says *it* has stopped pointing at things.


**1 · gate — hard fail.** Banned words (`rooms`, `quiet`, `genuinely`), sentence-initial
*And*/*But*, glued em-dashes, negative stacks, live `⟦tokens⟧`. Any hit is a defect. Fix it,
do not argue with it. A live token is the one thing standing between a placeholder and the
typesetter.

**2 · diet — a number for a thing you cannot see by eye.** Be-verbs, copula openings, waste
words (*it / this / that / there*), zombie nouns, expletive openers, passives, and empty
nouns (*thing / something / version / way / part / room*), each as a ratio against the
book's own baseline. Over 1.30 is heavy.

`empty` was added 2026-07-31 because the other six could not see the defect. Driving
`waste` down removes pronouns, and empty nouns move in to replace them. The draft that
prompted it measured 23.1 empty nouns per thousand against 0.0 in both sections it was
written to sit beside, while every existing counter called it clean.

Read the `-v` output for the actual sites rather than guessing:

```
python3 instruments/prose_diet.py -v DRAFT_FILE
```

**The fixes that work, in the order they pay:**

| finding | what it usually is | the move |
|---|---|---|
| expletive | *It was the second after…*, *There are two warnings…* | put a noun in the subject. *The second after did.* *Take two warnings with you.* |
| copula | *X is Y* as the default sentence | find the verb hiding in the sentence and use it |
| zombie | *the dissolution*, *a recognition that* | turn the noun back into the verb it came from |
| waste | *it / this / that* with no clear antecedent | name the thing, or cut the clause |

**3 · slop.** Run `/no-ai-slop` on the draft. It is a reading rather than a measurement, so no
instrument can do it. Then **re-run step 2**, because a slop edit changes the numbers.

**4 · Once it lands**, run the book-wide pass:

```
python3 instruments/review.py
```

Six steps: gate, diet, em-dash budget, seam sweep, citation audit, `compile.py --verify`. All
six must be `ok` before committing a manuscript change.

## Score the set, not the sentence

**Ratios on a short sample are noise.** A single 50-word Example scored `zombie 1.80` on one
occurrence of *the correction*. Below roughly 300 words the counters swing on individual
words and will send you chasing nothing.

**The unit is the batch**: a chapter's five Examples together, a whole letter, a whole
handbook. Score a single passage only to compare two candidate versions of it against each
other, which is what the ratio is genuinely good for.

## Never show unreviewed prose

Added 2026-07-31, one turn after this skill was written, because it was already broken.
A rewritten Example was composed inline in a message to Wendell and put in front of him
without a run. He asked *"was this reviewed before we put it in front of me?"* It had not
been, and it scored **be 1.37, copula 2.06, waste 1.53, zombie 1.55** — heavy on four of five
counters, the worst-scoring prose of that session.

**Prose in a message is prose.** A candidate sentence written inline gets the same pass as a
draft file: write it to a file, run `review.py` on it, then paste it. Composing in the reply
is where the check gets skipped, every time.

## Show the diff before applying a sweep

Added 2026-07-31, after applying twelve edits to ch7 and then four corrections on top of
them, both times without showing Wendell first. He asked: *"Did you already correct those.
I'd like to see the before and after before I approve them."* By then the answer was yes,
twice.

**A sweep is three or more edits driven by one counter, or any edit to prose already in the
manuscript.** For a sweep:

1. **Write the before-and-after out before touching the file**, one row per edit, each one
   quoting **the whole sentence** rather than the fragment the counter highlighted.
2. **Paste it and wait.** A counter finds candidates; only a reader approves them.
3. Apply, then re-run the counter.

**The fragment is enough to find an edit and not enough to judge one.** Four of those twelve
were worse than what they replaced, and every one of the four looked fine as a six-word span:
a correlative broken because only half of a *through … through* pair changed; *settled*
meaning decided rewritten as *settles* meaning coming to rest; a passive replaced by
something vaguer, in a sentence where nobody was doing the losing so there was no doer to
promote. All three read correctly in isolation and wrongly in the sentence.

**Single edits to fresh drafts do not need this.** The cost of the ceremony is only worth
paying where the prose already exists and a reader has already accepted it.

## Registers, and when heavy is correct

**A number is not a verdict.** The baseline is nine chapters of Wendell's expository prose,
and the book has since grown genres it never measured: an annotated charter, a personal
letter, a drill manual, a practitioner's casebook. By the expository ruler every one of those
reads as a defect, and none of them is. They are `marginalia/specs/HEAD_VOICE_DIAL.md` doing
what it was written to do.

So `prose_diet.py` carries a `REGISTERS` table. A named file gets a raised ceiling **on the
counters its genre inflates and on nothing else**, with the date, the ruling and the reason
recorded beside it. Two entries today, both Wendell's on 2026-07-31: the Headmaster's letter
on `be` and `copula`, and Quill's ch5 register on `zombie`, `be` and `expletive`.

**An unnamed file gets the baseline.** Adding a register is a deliberate act by a person with
a reason, never a way to make a batch pass. If new prose scores heavy, the first question is
always *is this the voice or is this drift*, and the default answer is drift.

**Ask before adding one.** A register entry is a standing exemption and only Wendell can rule
one, exactly as with the em-dash budget, which can ratchet down on its own and can only be
raised by him.

## What this does not replace

`specs/SPEC_EXAMPLES_2026-07-31.md`, `SPEC_TWO_HANDS`, `SPEC_FACE_TARGETS` and
`HEAD_VOICE_DIAL` say what the prose has to *do*. This pass only says whether it is heavy,
off-gate, or across the membrane. A passage can pass every check here and still be the wrong
paragraph.
