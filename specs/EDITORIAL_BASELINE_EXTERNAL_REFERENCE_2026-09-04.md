---
type: spec
title: "Baselines from the genre and the reader"
aliases:
  - external baseline
  - reference corpus
  - stop self-baselining
  - prose_diet baseline
tags:
  - editorial
  - process
  - baseline
  - research
created: 2026-09-04
review: 2026-09-20
source:
  - instruments/prose_diet.py
  - specs/EDITORIAL_PIPELINE_COHERENCE_2026-09-03.md
---

# Baselines from the genre and the reader

**Wendell, 2026-09-04:** *"measuring the book against its own baseline is a crazy thing to do and
MTGOA did it to its detriment — we're still fixing things that should've been caught in editorial
review. We need a more intelligent way… the only one that makes sense is examples from the genre it
fits into, or books our Ideal Client Avatar is used to reading and likes."*

## Findings, ranked

1. **The baseline is self-referential — that is the defect.** `prose_diet.py` (and the telling /
   trailing_and / light_verb targets, before their reframe) sets "normal" to *what the book already
   does*. A ratio of `1.00` reports that the book matches its own average; quality lives on a
   different axis the ratio leaves untouched. So the instrument measures **internal consistency**
   and launders the book's own habits
   into the standard: passive-for-this-book becomes the ruler, so a book made entirely of passive
   sentences reads as perfectly normal to it. This is how MTGOA's numbers ratified MTGOA's tics.

2. **A self-baseline stays blind to what reaches the reader.** The defects a reader feels are
   defects against *what good prose in this lane does*. A yardstick cut from the same clay it
   measures reports internal drift and misses distance-from-good, which is the distance that counts.

3. **The fix is an external reference — a mature, well-understood technique.** The field measures a
   text's **distance from a reference corpus**. Two references fit this book, and they answer
   different questions (below).

## What the field actually does (researched 2026-09-04)

- **Stylometric distance — Burrows's Delta / Cosine Delta.** The standard way to ask "how far is
  this text from that pile of texts." Build a feature vector (frequencies of function words / most
  frequent words, plus countable style features), z-score against a reference set, take the
  distance. Language-independent, holds up across text lengths, decades of use in literary and
  forensic stylometry. This is "how close is my book to the genre / to my reader's shelf," made
  numerical.

- **Biber Multidimensional Analysis (MDA) — the feature set is already ours.** Biber's register work
  counts the very things `prose_diet` counts — **passives, be-verbs, pronouns, subordination, stance
  markers** — and places genres on empirical dimensions (Informational↔Involved,
  Abstract↔Non-abstract, and so on). A clinical case-study novel and a thriller sit at different
  coordinates by design. So the right target for a passive rate is the band the genre occupies on
  that dimension.

- **The tooling exists, open-source.** `BiberPlus` extracts the classic Biber features; **Neurobiber**
  (2025) predicts 96 of them fast and interpretably. So measuring a corpus's style fingerprint is a
  library call today.

- **Comp titles — the publishing-world version of your instinct.** Agents and editors already
  benchmark a manuscript against **comparable titles**: recent, in-genre, audience-matched books —
  precisely "books the Ideal Client Avatar reads and likes." The discipline holds comps to one
  standard: specific, recent, and squarely in the real genre.

## The two references this book needs (both, for different reasons)

| reference | the pile of books | the question it answers |
|---|---|---|
| **Genre band** | in-genre exemplars — the register the book is written *in* (for the AI Psychologist: literary case-study / teaching-story, the Sacks / Yalom lane) | *Is this prose in the right register for this kind of book?* |
| **Reader / ICA band** | books the ideal reader already loves and reads easily | *Will this land the way my reader's ear expects?* |

The genre band keeps the book true to its form; the reader band keeps it readable to the person you
are writing for. A passage can pass one and fail the other. That gap is a real editorial signal.

## Named comps (decided 2026-09-08)

Reader tuned to the **narrative-nonfiction / ideas** reader — the MTGOA-adjacent audience that reads
Sacks and Gawande and expects the case to feel real.

**Genre band — the clinical-teaching register the prose must pass as** (already named in
`style/CASE-STUDY-GENRE.md`):

- Egan, *The Skilled Helper*
- Freud, *Studies on Hysteria*
- Rogers, the Chicago verbatims (Mrs. Oak; Herbert Bryan)
- a PCSP teaching case *(open-access)*
- a BMJ / CARE case report *(open-access)*

PCSP and BMJ Case Reports publish open-access, so this band is measurable with texts already in the
clear — a practical head start on building it.

**Reader / ICA band — narrative nonfiction of mind and institution:**

- Sacks, *The Man Who Mistook His Wife for a Hat* — case study as literature
- Gawande, *Being Mortal* — institutions and the vulnerable, humane and clear; the ideas reader's
  canon, and thematically next door to this book's benevolent-violence premise
- Yalom, *Love's Executioner* — therapy cases, warmth under a clinical frame; closest to Bekele's
  intended temperature
- van der Kolk, *The Body Keeps the Score* — the book already on this audience's shelf; anchors what
  "serious but readable" means to them

### The tension the two bands exist to expose

The genre band is cold and formal by design; the reader band is warm and accessible. This book's
register is the cold one on purpose — the institutional voice enacting benevolent violence is the
horror. So the reader band will read the prose as *too formal for a Gawande reader*, and that gap is
the signal worth having: it measures the **readability tax of the conceit**, chapter by chapter.
Where the coldness carries the horror, the tax is worth paying; where it only distances the reader
for no payoff, that is a line to warm. The gap is the instrument. Erasing it everywhere would erase
the book.

## Hostile-review hardening (2026-09-09)

A red-team pass found the first bands standing on weak scaffolding; all of it is now fixed in code:

- **Contaminated comps.** The genre comps carried reference lists, DOIs and journal boilerplate; a
  reader comp was a *translation* with a page-number TOC ingested as prose. Fix: `corpus_clean.py`
  strips non-prose, `build_bands` runs every comp through it, the BMJ set was re-extracted paragraph-
  only, and the translated comp was swapped for a native one (Maeda's *Laws of Simplicity*).
- **min/max edges — and a false claim.** The band used min/max, which is set by one outlier and only
  *widens* with more comps; the spec had claimed the opposite. Fix: the band is now **median + Q1..Q3**
  (interquartile), which tightens as the sample grows.
- **No call site.** The bands had no check — the failure this pipeline exists to prevent. Fix:
  `coherence.py`'s `reference` check re-measures the comps and compares to the stored band, and a
  `scorer:` version stamp (prose_diet.SCORE_VERSION) fails the board if a band was measured with a
  counter version that no longer matches — both negative-tested.
- **Still open, honestly:** the counters under the band are prose_diet's heuristic regexes (a Biber-
  validated feature set would be firmer), and the samples are small (n=3 reader / n=4 genre). The
  headline verdict survived a leave-one-out test regardless, but more native comps is the real fix.

## How a project sets its bands (the command)

`instruments/build_bands.py` does the measure-and-emit step, so a new project sets a band without
hand-written arithmetic:

1. **Pick the comps** — the one step nothing automates (genre = the register to pass as; reader =
   what the ideal reader reads, at its readable end).
2. **Get the texts** as plain-text `CORPUS.txt` — owned copies or public-domain / open-access
   sources. Only the numbers are stored; the text stays on your machine.
3. **Measure**: `python3 instruments/build_bands.py reader <comp> <comp> <comp> --sources DIR`. Each
   comp is a file, a directory holding `CORPUS.txt`, or a slug resolved under `--sources`. It cleans
   each comp, prints every comp's rates, the band (median + Q1..Q3), and a ready-to-paste
   `reference:` block stamped with the scorer version and sources for coherence to re-check.
4. **Paste** that block into `editorial.yaml`. prose_diet reads it next run; a project with no band
   keeps its built-in baseline, so the change is additive and reversible.

Three-plus comps of a few thousand words each; the tool flags a band built from fewer.

## Recommended architecture

1. **Pick 5–10 comps per band** (specific, recent, in-lane). Measure them once with the Biber
   feature set. Store **only the measured statistics** — a band (median and spread) per feature —
   in the manifest, e.g. `reference: { genre: {...}, reader: {...} }`. Keep the text itself out of
   it; the numbers are all the comparison needs. Storing statistics instead of prose also sidesteps
   copyright.

2. **The instrument reports distance and direction.** "Passive sits above the genre band by X" or
   "below the reader band by Y." Direction is the whole point: too passive for the genre and too
   terse for the reader call for opposite fixes.

3. **It surfaces, the author rules — the same stance as the rest of the pipeline.** A deviation from
   the band is a candidate to question, and the author decides whether to close the gap. Accepted
   deviations go in the exceptions ledger, exactly as elsewhere.

## The guardrail (why "match the corpus" would be its own mistake)

Research on style-matching is blunt: **forcing prose toward a target corpus homogenizes voice** and
dilutes the markers that make a writer distinct. So the goal is to **flag deviation worth
questioning** and leave the closing of the gap to the author. A band — the range the genre occupies —
together with a surface-and-let-the-author-rule stance, is what keeps this from sanding the book down
to genre-average. The reference shows where the edge of the lane is; the
driving inside it stays the author's.

## These stay absolute — keep them off the band

The reframe applies only to the **distribution-shaped** measures (passive / be-verb / telling /
trailing-and rates). The **rule-shaped** checks stay absolute, and "the genre does it too" is no
defence for them: sentence-initial *And*/*But*, glued em-dashes, live placeholders, production tags,
banned voice words, and **fragments** are defects at any rate. A genre band is a target for texture;
a mechanical defect is still a defect inside it.

## Decisions and what remains

- **Comps — DECIDED 2026-09-08.** Both bands named above; reader tuned to the narrative-nonfiction /
  ideas reader.
- **One band or two — DECIDED: both.** The genre band is nearly free (already named in the style
  doc), and the gap between the two is the point (see the tension section).
- **Which features sit on a band, which stay absolute — proposed, confirm.** Distribution-shaped on a
  band (passive / be-verb / telling / trailing-and rates); rule-shaped absolute (fragments, banned
  words, sentence-initial *And*/*But*, glued em-dashes).
- **Distribution model — proposed, confirm.** Median + interquartile band per feature.
- **Next build step.** Acquire the four reader-band texts (locally; store stats only) and pull the
  two open-access genre exemplars, run the Biber feature set over each, write the two bands into the
  AI-Psychologist manifest, and point `prose_diet` at distance-from-band.

## Sources

- Burrows's Delta / Cosine Delta and stylometric distance: [Computational Literary Studies methods](https://methods.clsinfra.io/corpus-author.html); [stylometric similarity in literary corpora](https://academic.oup.com/dsh/article/38/1/277/6659069)
- Biber Multidimensional Analysis: [Dimensions of Register Variation (Biber)](https://www.researchgate.net/publication/2416390_Dimensions_of_Register_Variation_A_Cross-Linguistic_Comparison_Douglas_Biber); [Fiction — one register or two?](https://www.jbe-platform.com/content/journals/10.1075/rs.19006.egb)
- Tooling: [Neurobiber: Fast and Interpretable Stylistic Feature Extraction](https://arxiv.org/abs/2502.18590); [Blablablab/neurobiber (HuggingFace)](https://huggingface.co/Blablablab/neurobiber)
- Comp titles: [How to Pick Comp Titles (Alyssa Matesic)](https://www.alyssamatesic.com/free-writing-resources/how-to-pick-comp-titles); [What Makes a Good Comp Title? (Inkshift)](https://inkshift.io/resources/comparable-titles)
- Homogenization risk: [The Homogenizing Effect of Large Language Models on Human Expression](https://arxiv.org/html/2508.01491v1)
