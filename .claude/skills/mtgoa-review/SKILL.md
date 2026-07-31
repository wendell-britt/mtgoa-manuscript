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

**1 · gate — hard fail.** Banned words (`rooms`, `quiet`, `genuinely`), sentence-initial
*And*/*But*, glued em-dashes, negative stacks, live `⟦tokens⟧`. Any hit is a defect. Fix it,
do not argue with it. A live token is the one thing standing between a placeholder and the
typesetter.

**2 · diet — a number for a thing you cannot see by eye.** Be-verbs, copula openings, waste
words (*it / this / that / there*), zombie nouns, expletive openers, each as a ratio against
the book's own baseline. Over 1.30 is heavy.

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
