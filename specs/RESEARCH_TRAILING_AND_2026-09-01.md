---
type: research
title: "The trailing and — what it is, why I keep doing it, and how to stop"
aliases:
  - trailing and
  - loose sentence
  - comma and
created: 2026-09-01
review: 2026-09-15
source:
  - marketing/PDF_BLOCKS_2026-09-01.md
  - instruments/trailing_and.py
---

# The trailing *and*

**Wendell, 2026-09-01**, on a sentence of mine — *"Running them is a different matter, and
thirty days is roughly how long a form takes to stop needing your attention"*:

> *"this trailing 'and' construction needs to go. I don't want to see it anymore in any writing
> that I want to have generated."*

---

## 1 · What it is, and it already has a name

**The construction is a comma, a coordinating conjunction, and a second independent clause:**

```
[independent clause] , and [independent clause]
```

**Strunk names it in 1918 and bans a run of them.** Rule 14, *Avoid a succession of loose
sentences*, is about exactly this shape and no other:

> *"This rule refers especially to loose sentences of a particular type, those consisting of
> two co-ordinate clauses, the second introduced by a conjunction or relative."*

**He also names the connectives**, which is the list to watch for: *"using as connectives
**and**, **but**, and less frequently, **who, which, when, where, and while**."*

**His diagnosis is the sentence worth memorising.** The replacements he offers — simple
sentences, two clauses joined by a semicolon, periodic sentences, three-clause sentences —
are to be chosen *"whichever best represent **the real relations of the thought**."*

**That is the whole defect in five words.** English gives you a full set of connectives that
each commit to a relationship: *because* asserts cause, *once* asserts sequence, *though*
asserts concession, *which* asserts dependency. **`and` commits to nothing.** It says only
*here is another one*. So a writer reaching for `and` where a subordinator belongs is
declining to say how two ideas relate — usually because they have not worked it out.

### The technical frame, for the cases where it is correct

**Parataxis** places clauses side by side as equals and leaves the relation unstated.
**Hypotaxis** subordinates one to another and states it. Neither is a defect. **A style is a
ratio between them**, and mine has drifted paratactic without anybody choosing that.

**Joseph Williams is on the other side of this and it is worth knowing why**, because it stops
the rule being applied stupidly. He calls coordination *"the foundation of a gracefully shaped
sentence"* — provided the coordinated elements are **parallel in grammar and in sense**, and
ordered shorter to longer. **That is not what I produce.** I coordinate two unparallel
observations, which is parataxis wearing coordination's clothes.

## 2 · Measured, because a style complaint without a number is an opinion

**Detector: a comma, a coordinator, and a following finite clause.** Run across the prose I
generated in this repo in the last two weeks, against the manuscript as a control.

| corpus | sentences carrying it | rate |
|---|---|---|
| **documents I generated** | **206 / 806** | **25.6%** |
| the manuscript, hand scan | 980 / 6,407 | 15.3% |
| **the manuscript, by the instrument** | **783 / 5,643** | **13.9%** |
| `DECISION_FUNNEL_2026-09-01.md`, written today | 17 / 41 | **41%** |
| `ASSESSMENT_PDF_2.0_2026-09-01.md` | 17 / 62 | 27% |
| `CHECKLIST_PHYSICAL_PROOF_2026-08-29.md` | 15 / 54 | 28% |

**One sentence in four, against one in seven in the book.** The two book figures differ
because the hand scan counted headings and table rows; **13.9% is the number the instrument
produces and the one new prose is held to.** The habit is mine rather than the
house voice's, and the worst document is the one I wrote this morning.

## 3 · The two species I actually produce

**Reading the hits rather than counting them, they are not one habit but two.**

### Species A — the appended second observation

> *"That is more moving parts than serving the page, **and** it breaks the first time someone
> shares the post-redirect link."*

> *"It has the shape of an annual report dropped onto the last page, **and** it changes
> register at the worst possible moment."*

**Two separate criticisms bolted together.** The real relation is enumeration — *there are two
problems with this* — and `and` hides that rather than stating it. The reader gets a list
disguised as a sentence.

### Species B — the ranking tag, and this one is a template

> *"Two errors, **and the second is worse than the first**."*
> *"There is now a third, **and it is the strongest of them**."*
> *"He is right, **and his third reason is the strongest one**."*
> *"Two problems, **and the second is the serious one**."*
> *"The recommendation, **and it is not the cheapest line in that table**."*

**Twenty-three instances of this exact formula in two weeks of my output**, most of them the
literal string `, and it is the` followed by a superlative.

**It is worse than Species A and the reason is not grammatical.** The ranking tag **announces
a hierarchy instead of enacting one.** If the second error is worse, the fix is to lead with
it, or give it its own paragraph, or put it last where the stress falls. Saying *"and the
second is worse"* is telling the reader about an ordering I declined to build. **It is the
structural equivalent of explaining a joke.**

**It also flatters.** *"and it is the strongest of them"* positions the writer as having
already weighed the set. That is the same move `/no-ai-slop` bans as faux-insight, arriving
through the grammar instead of through the vocabulary, which is why `slop_shapes.py` never
saw it.

## 4 · Why it keeps showing up

**`and` is the only connective that requires no analysis.** Every other one commits: *because*
to cause, *so* to consequence, *once* to sequence, *though* to concession. **`and` is the null
hypothesis of connectives**, and it is always available, at any point in any sentence, without
knowing yet what you think.

**It is a hedge against the stress position.** English puts weight at the end of a sentence.
Stopping after the first clause commits to that clause being the point. Adding `, and …`
defers the commitment and softens the landing — which feels safer and reads as less certain.

**It manufactures a rhythm that sounds considered.** A two-beat sentence has balance, and
balance passes for thought. Strunk's word for what a run of them produces is *"mechanical
symmetry and sing-song."*

**The house voice supplies cover, too.** This project's register runs on bolded declaratives and
paired observations, so `X, and Y` sounds on-voice even when the `and` is doing nothing.
**That is the most dangerous reason**, because it means the tic passes a voice check.

## 5 · Remediations, worked on my own sentences

**Strunk's list, modernised, in the order to try them.**

| move | when | worked example |
|---|---|---|
| **Split** | the second clause carries its own claim | *"Running them is a different matter. Thirty days is roughly how long a form takes to stop needing your attention."* |
| **Subordinate** | there is a real relation to name | *"Running them takes longer, because a form needs about thirty days to stop asking for your attention."* |
| **Reduce to a phrase** | the second clause modifies rather than asserts | *"Running them takes about thirty days, long enough for the form to stop needing your attention."* |
| **Semicolon** | parallel in grammar and in weight | *"Reading the moves takes an evening; running them takes thirty days."* |
| **Colon** | the second delivers what the first promises | *"Running them has a price: thirty days before the form stops needing your attention."* |
| **Cut the first clause** | the trailing clause was the only content | *"A form takes about thirty days to stop needing your attention."* |
| **Enumerate** | Species A — it was a list | *"Two problems. It adds moving parts, and it breaks…"* → *"It adds moving parts. It also breaks the first time somebody shares the post-redirect link."* |
| **Restructure** | Species B — the ranking tag | delete the tag and **move the important item to the stress position** |

**The last row is the only one that is not a sentence edit.** A ranking tag cannot be fixed
inside its own sentence, because the defect is that the paragraph is in the wrong order.

## 6 · Where the construction is correct, so the rule does not become superstition

**Parataxis is a craft technique with a long pedigree, and banning it outright would be a
worse error than the tic.**

| tradition | what the `and` does | why it works there |
|---|---|---|
| **The King James Bible** | *"And God said… and there was light"* | Polysyndeton flattens hierarchy deliberately. Events arrive in their own weight, none subordinated to another |
| **Hemingway** | *"there were pebbles and boulders, dry and white in the sun, and the water was clear and swiftly moving"* | The iceberg theory. The `and` adds and never explains, and the withheld explanation is the point |
| **Cormac McCarthy** | long paratactic runs | Refuses the narrator's judgement about which event mattered |
| **Legal and technical** | enumerated conditions | Coordination is the meaning; subordinating would change it |
| **Spoken register** | *"I went down there and he wasn't in"* | Speech is paratactic by nature, and dialogue that subordinates sounds written |

**The distinguishing test is intention and repetition.** Polysyndeton is a decision, repeated
on purpose, doing work no other structure does. **Mine is an unmarked default at 25%, which is
neither.**

**Strunk himself allows the single instance.** *"Although single sentences of this type may be
unexceptionable… a series soon becomes monotonous."* **The rule is about rate, not about
occurrence** — which is exactly what an instrument can measure and a reader cannot.

## 7 · The house rule

**In anything generated for this project: a trailing coordinate clause is a candidate, and the
ranking tag is a defect.**

- **Ranking tags** — `, and it is the [superlative]` and its relatives — **are cut on sight.**
  There is no correct instance. Reorder the paragraph instead.
- **Species A** gets one of the eight moves in §5, chosen by which relation is true.
- **A deliberate paratactic run stays**, and gets said out loud in the record so a later pass
  does not "fix" it.
- **The target is the manuscript's own rate**, 13.9%, not zero. Zero would be a different and
  equally mechanical voice.

**`instruments/trailing_and.py` measures it and `review.py` runs it**, because this project has
learned twice now that a rule with no call site is a rule nobody keeps.

## 8 · What I could not verify

**I could not read Strunk's primary text.** Wendell sent the Gutenberg edition and
`gutenberg.org` is blocked by this environment's egress proxy, as are the four other
full-text mirrors I tried. **The quoted passages come from search-result extracts** of Rule 14,
and they are consistent across independent sources, which is not the same as reading the page.
**Check the wording against the Gutenberg text before quoting it anywhere public.**

**Williams, Hemingway and the King James characterisations are likewise second-hand** for this
session. The measurement in §2 and the reading in §3 are mine and are reproducible with
`instruments/trailing_and.py`.

**Sources.** [Strunk, *The Elements of Style*, 1918 — Gutenberg](https://www.gutenberg.org/files/37134/37134-h/37134-h.htm) ·
[Rule 14 discussion](https://www.oocities.org/mdmorrissey/loose.htm) ·
[Loose sentence](https://en.wikipedia.org/wiki/Loose_sentence) ·
[Parataxis](https://en.wikipedia.org/wiki/Parataxis) ·
[Williams, *Style*](https://www.clc.hcmus.edu.vn/wp-content/uploads/2015/11/Style_-_Joseph_M._Williams_Joseph_Bizup.pdf) ·
[Parataxis and hypotaxis in literature](https://bookishbay.com/parataxis-and-hypotaxis/) ·
[LitCharts on parataxis](https://www.litcharts.com/literary-devices-and-terms/parataxis)
