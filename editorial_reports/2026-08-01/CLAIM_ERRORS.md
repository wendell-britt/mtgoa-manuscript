# Claim errors — the read-through pass

**2026-08-01.** Filed from Wendell's fourth read-through batch. A claim error is a
stated fact that is wrong: not a line that reads badly, not a line that needs a
ruling, but a sentence the book asserts and the world does not support. It is the
cheapest kind of finding to fix and the most expensive kind to ship, which is why
`rescan.py` sorts it above everything else.

This file is written in the shape `instruments/rescan.py` parses, so the findings
below join the working list and get re-checked against the manuscript on every run.

## Why this file exists at all

`editorial_reports/2026-07-31/CH1_*.md` reports, in its own counts line:

> **Claim-error: none. No demonstrably false statement, number, date, or
> attribution was found in this chapter.**

That was wrong, and the sentence it missed is the first line of a named section.
`appendices/PHASE2_HOSTILE_EDITORIAL_REVIEW.md:60` had looked directly at the same
section a pass earlier, under the heading *Token System — "Every game has a
currency"*, and graded it **✅ STRONG**. It raised one concern, and the concern was
that a later sentence explains rather than shows.

**Two editorial passes read the claim and neither asked whether it was true.** Both
were reading for how the sentence works on a reader. Wendell read it and asked the
other question in four words: *is this true?*

---

## A · CHAPTER 1

### [CL-1] "Every game runs on a currency" is not true of games
- **Location:** ch1:101, opening line of *The Token System — What You're Spending*
- **Evidence:** ch1:101 — "Every game runs on a currency, and the first rule you get to rewrite is what you pay with." · ch1:103 — "In the Arcade the currency is tokens, and they come in two kinds."
- **Reader problem:** A currency is a medium of exchange a player spends to keep playing. Most games have no such thing. Chess, tag, football and go take no payment; a player brings attention, effort and time, and none of those are exchanged for anything. Where a game does have a currency it is usually a design choice about monetisation or scarcity, not a property of games. Wendell's own correction states the true version and the true scope in one line: *"What do games actually run on? Attention. Arcade games run on currency and it's tokens."* So the universal is false and the specific is true — the Infinite Arcade is an arcade, arcades run on tokens, and the section's whole apparatus is sound one level down from where the sentence puts it.
- **Category:** claim-error
- **Disposition:** line edit, scope only
- **What would disprove this:** A definition of *currency* broad enough to cover attention and effort, stated in the book before this line, under which the universal holds. The book does not define the word, and the very next sentence uses it in the narrow sense — *the currency is tokens*.
- **What it costs to fix:** The claim is load-bearing for the section title, the two token kinds, the renewable/non-renewable split, and the ticket economy that follows. None of that depends on the universal; all of it depends on the arcade. Narrowing the sentence to the Arcade leaves the section intact. Replacing *currency* with *attention* throughout would not — tokens are the section's whole conceit.
- **Adjacent, not filed:** `appendices/PHASE2_HOSTILE_EDITORIAL_REVIEW.md:76` records a parallel universal from an earlier draft, *"Every game needs a reward structure."* That sentence is not in the current manuscript; grep finds it only in the review. Recorded here so that a rewrite of CL-1 does not reintroduce the shape it was built in.

---

## What this pass did not do

It did not sweep the book for universals. One claim error was named by a reader, and
one is filed. The shape it belongs to — *every X does Y*, asserted about a category
the book has not defined — has no instrument behind it and was missed by two passes
that read the sentence closely. Whether that shape recurs is an open question and
would need its own scan, not an inference from a single site.
