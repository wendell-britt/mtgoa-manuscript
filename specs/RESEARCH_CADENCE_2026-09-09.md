---
type: research
title: "The cadence detector — the two sentence-molds the eye caught and the counters missed"
aliases:
  - cadence
  - cadence detector
  - sentence molds
tags:
  - mtgoa
  - instruments
  - review
created: 2026-09-09
review: 2026-09-23
source:
  - instruments/cadence.py
  - instruments/review.py (step 3g)
  - proof photos, ch3 pp.66-95 (Wendell's highlights)
---

# The cadence detector

**Wendell, 2026-09-09, on the ch3 proof.** He highlighted the whole back half of the chapter
(pp.66–95, Section 4 through the recap) and wrote *"Rework"* in the margin. The marks were not
logic breaks, and `dupes.py` was already clean, so they were not repeated ideas either. They were
two sentence-shapes, run until the prose went monotone.

## The two molds

- **VERDICT.** A short demonstrative-copula sentence that lands a summary: *"That is the
  mechanism." "It was not." "The Grow stage is the integration."* The chapter reaches for it
  after almost every teaching beat.
- **COMPOUND.** A clause tacked on with `, and …`: *"…and the picking exhausts you." "…and it
  cost you the safety of being the one who never breaks the surface."*

They interlock into one default sentence: **"X, and Y. That is Z."** Read once, each shape is
fine. Run for twenty pages, the content keeps advancing while the rhythm hammers a single note,
and the reader tires even where the argument is sound.

## Why the existing counters missed it

`telling.py` (step 3e) targets the copula-**label** that pins a property on a person or object.
`trailing_and.py` (step 3d) targets the sentence-final trailing "and" and the ranking "and."
Measured across ch3 lines 620–940, `telling.py` flagged **2** and `trailing_and.py` flagged **1**.
The eye flagged scores. The molds here are mid-sentence coordinations and demonstrative verdicts
that both instruments average away. A rate that smooths the rhythm cannot see a rhythm problem.

## What the detector measures

`cadence.py` reads body paragraphs (it skips marginalia frames, headings and tables), splits
sentences, and counts the two molds per paragraph. It reports a per-file rate for each mold and
lists the densest paragraphs, ranked by combined load. Wired as **review step 3g**. Baseline at
first run: ch2 `verdict 8.4/100, compound 20.3/100`; ch3 `verdict 10.9/100, compound 15.1/100`.
Its densest ch3 paragraphs (933 the recap, 690 the parable, 665, 826) are the paragraphs Wendell
highlighted most heavily, which is the check that it measures what he marked.

## The caveat, on the tool itself

**It is a locator, not a target to minimise.** Breaking a run-on into short sentences trades a
COMPOUND for a VERDICT on purpose: the demo rework of paragraph 826 dropped compounds and raised
verdicts, and read better for it. The good verdicts earn their drumbeat (*"That is the myth this
chapter breaks"*). Chase the number down and the voice flattens, which is the Goodhart failure the
Flesch pass already taught once this session. The detector finds the dense windows. The ear rules
on the rewrite, and it preserves deliberate parallel structure (the four-domain markers, the
five-move markers) while it breaks the accidental monotone.

## Sourcing

The molds are Wendell's own reading of the printed proof, corroborated by the counts above. The
detector is plain Python over the manuscript files; it pulls no external list. It sits in the same
lineage as `trailing_and.py` and `telling.py`: an instrument built for a pattern the eye caught
that the earlier instruments could not.
