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

`inchoative` was added 2026-08-02 for the same reason, and it is the **third** counter
added because tightening an earlier one pushed the defect somewhere nothing was looking.
Assume there is a fourth. `go / goes / went / gone` + adjective means *become* —
`goes cold` unpacks to `is cold now` — but it has the shape of a verb of motion, so the
eye reads it as something happening and `be` and `copula` cannot see it at all:

```
"The meeting goes cold. The table goes careful."     be 0.00   copula 0.00
"The meeting is cold.  The table is careful."        be 4.97   copula 3.44
```

Identical sentences. **So driving `copula` down rewards moving copulas into `go`.** The
counter scores only inanimate subjects, because the construction is legal when a person
becomes something (`you go cold`, `ch2:358`) and is a defect when the subject cannot act
(`the meeting that goes sideways`). Book baseline 0.30 per thousand; ch2 runs 1.07.

It is low-frequency, so **the ratio is noise on anything short and the `-v` site list is
the output.** Two hits in a 300-word draft reads as 22x and means nothing.

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
| inchoative | *the meeting goes cold*, *a conversation that goes wrong* | ask who did it. *Everybody at the table starts picking their words.* If nobody did it, the sentence is a state report and probably wants cutting |

**The agency fix has one characteristic failure, and it is worse than the defect.** Added
2026-08-02 after three occurrences in one session. Wendell, on the third: *"all of your
changes keep reintroducing issues that we've removed from the text. They don't know the
loop. Whatever produces this assertion has got to go."*

Here is what produces it. Promoting an agentless abstraction requires a subject, and **the
nearest available subject is always the reader** — so *A familiar loop keeps running*
becomes *You know the loop*, which is `MANUSCRIPT_FILE_CANON:154` broken in five words.
The counters all improve. The sentence is now a lie about somebody's life.

**Assert her capacities, never her pathologies.** `ch1:22` says *You are the one who moves*
— a claim about who she is, which the book has earned. *You know the loop* claims she has a
recurring private failure, which nothing has earned and nothing can. The A0 gate counter
guards one corner of this (`you were taught / told / raised / trained`) and four fixed
phrases are all it has.

**The body is the worst place to reach for a subject, and it is the first place you will
reach.** Added 2026-08-02, one turn after the rule above, because the same move came back
wearing a body. A draft turned *the bracing fired exactly when it should* into *your body
braced exactly when it should* — the nominalization gone, and a claim about somebody's
somatic experience in its place. Wendell: *"you can't narrate someone's somatic experience.
What is actually being described here and describe it. Don't make up how someone is
feeling."*

Sensation is unfalsifiable and unshared, which is what makes it such an easy subject and
such a bad one. **Ask what is actually being described.** In that sentence it was the
reflex outrunning the decision, and whether that is correct — a mechanism and a judgement,
both of which the book can assert. *"You are out of its path before you have decided
anything. When the danger is real, the Protector does not wait for you, and it should
not."* Observable outcome, named mechanism, the book's verdict in the book's voice, and
nothing invented about anyone's chest.

**Four legal subjects when the abstraction has to go:**

| | |
|---|---|
| a conditional | *Run both at once and most of the attention goes to how you are landing* |
| the open menu, `ch1:22` | *a meeting, or a group chat, or a Sunday dinner* |
| a third party who really acts | *No one reports back* beats *the signal drops out* |
| nobody — cut it | a state report with no doer is often a sentence the passage does not need |

**3 · slop.** Run `/no-ai-slop` on the draft. It is a reading rather than a measurement, so no
instrument can do it. Then **re-run step 2**, because a slop edit changes the numbers.

**Run it against `eval.md`, not only against the pattern list in its `SKILL.md`.** Added
2026-08-02, because half of it was skipped. A ch2 draft was audited against the patterns —
colon reveals, dramatic fragments, em dashes — reported clean, and put in front of Wendell
carrying an invented scene: *"Six of you built the group to hold exactly this."* His reply
was four questions the draft could not answer. *Why six? Who are you? Which group? To hold
exactly what?*

`eval.md` check 1 is the one that catches it — *does the edit preserve the point **without
adding claims, examples, stats*** — and it is step 4 of that skill's own workflow. The
pattern list finds bad sentences. `eval.md` finds invented ones.

**Two failures the whole pass is blind to, both of which shipped past it:**

- **Fabricated specificity.** `MANUSCRIPT_FILE_CANON:154` — *never narrate the reader's
  unnamed history back to her as fact.* A definite article or a headcount standing over a
  blank is worse than the abstraction it replaced, because vagueness at least admits what
  it is. `gate.py`'s A0 counter matches four fixed phrases and nothing else. The legal
  form is `ch1:22`: an open menu (*a meeting or a dinner or a group chat*), generic
  actors, and the specificity loaded into **what happens** rather than into invented
  particulars. **You cannot make a hypothetical concrete by adding details.**
- **Banned words routed around.** The sentence wanted *the table goes quiet*; `quiet` is
  banned; `careful` went in instead, a word that does not collocate with *go* and so means
  nothing; the gate passed clean. The ban exists to force the sentence to be rebuilt, and
  substituting a synonym evades the work it was there to cause. `inchoative` tags six of
  these as LAUNDER and that is the nearest a machine gets. **If a banned word is the word
  the sentence wants, the sentence is wrong, not the word.**

**4 · Once it lands**, run the book-wide pass:

```
python3 instruments/review.py
```

Seven steps: gate, diet, em-dash budget, seam sweep, citation audit, `compile.py --verify`,
empty head. All seven must be `ok` before committing a manuscript change.

## The empty head noun — the defect a repair pass creates while fixing another one

Added 2026-08-03. Wendell: *"we've got to solve this definite article issue once and for all.
It's the new AI slop issue that our passes are creating faster than we can get rid of them."*
Narrowed by him one turn later: *"'empty head noun' is what I'm looking for… It's not in my
writing style to use the word 'thing' because of how unspecific it is."*

**`the X` is a presupposition.** It tells the reader *you already know which one I mean.*
Legal four ways: an antecedent, a referent unique in the world, a clause that supplies it on
the spot, or canon the book has taught her. When none holds it is the same lie as *"you know
the loop"* — grammar asserting shared knowledge that was never established.

**The article is the symptom. The empty head noun is the disease.** `the field`, `the charge`,
`the table` are contentful heads — the noun names something and the reader can picture it.
`the thing`, `the part`, `the piece`, `the work`, `the others` are placeholders: the modifier
does all the work, which is what it means for a head noun to contribute nothing.

**A restrictive clause is aggravating, not exculpating.** `the thing that charges the field`
is worse than `the thing.`, because the clause is carrying the meaning the noun refused to.
`marginalia/review.py`'s comment says the opposite — *"'the thing that gets done' is fine"* —
and that written exemption is why it caught 4 of 106 sites.

**Why this is our defect specifically.** Every agency repair evicts an abstraction from a
subject slot and has to put something back. The cheapest legal filler is a definite noun
phrase with a human-shaped head and no antecedent. One 23-edit R-B pass produced `the people
it concerns`, `the work`, `everybody involved` and `both camps` — four new ones while removing
twenty-three old ones. **Assume every repair pass you run has this byproduct and check for it
before showing the batch.**

Run `instruments/empty_head.py` — it is step 7 of `review.py` on both paths. It tests the
condition rather than matching strings, so it catches the phrase nobody has written yet, which
is the only version of "once and for all" that holds. `Say the Thing Under the Thing` is a
named move in ch3 and ch4 and is carved out.

**When it fires, name the noun.** Not a synonym for `thing` — the actual referent. If you
cannot name it, that is the finding: the sentence does not know what it is about yet.

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

## Ship state is a different question

`review.py` and `rescan.py` answer *is this prose good* and *what does this finding cost*.
Neither answers *can the book ship*, and from 2026-08-01 that is the question that ranks:

```
python3 instruments/shipcheck.py        # the board
python3 instruments/shipcheck.py -v     # every blocking site
```

Six categories, ordered by DL-20: app routing, placeholders, build gaps, gate, em-dash
budget, marginalia round-trip. A blocker is something that reaches a reader wrong or
incomplete. Everything else is quality, and quality does not stop a press.

**Run it before proposing work.** A quality finding that outranks a blocker in your
attention is the failure this instrument exists to prevent.

## What this does not replace

`specs/SPEC_EXAMPLES_2026-07-31.md`, `SPEC_TWO_HANDS`, `SPEC_FACE_TARGETS` and
`HEAD_VOICE_DIAL` say what the prose has to *do*. This pass only says whether it is heavy,
off-gate, or across the membrane. A passage can pass every check here and still be the wrong
paragraph.
