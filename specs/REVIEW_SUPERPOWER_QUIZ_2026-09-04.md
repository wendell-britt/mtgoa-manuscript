---
type: review
title: "Is the Superpower Quiz doing its job? A review against the ontology and the player"
aliases:
  - superpower quiz review
  - quiz usefulness
  - is the quiz useful
tags:
  - marketing
  - mtgoa
  - course
  - review
created: 2026-09-04
review: 2026-09-18
source:
  - johnair01/bars-engine (src/lib/superpowers, src/components/superpowers)
  - instruments/character_sheet.html
  - specs/retired/APPENDIX_G_BELIEF_TO_SUPERPOWER_MAP.md
---

# Is the Superpower Quiz doing its job?

**Wendell, 2026-09-04:** *"an opportunity to explore how the superpower quiz is doing its job. I
made it months ago and I think our ontology is sound enough we can review whether it's actually
useful for players."*

**I read the live code in `johnair01/bars-engine`.** The scorer, the item bank's structure, the
seven superpower definitions, the reveal copy, the lead capture, and the design specs
(`superpower-quiz-design/`, including a `BARNUM_CHECK.md`).

**The verdict, up front: it is a well-built instrument, and the honest problem is that its job has
never been measured on a real player.** The design is careful — the scoring is sound, the copy has
a real anti-horoscope discipline, and the seven superpowers are grounded in the book's own
emotional-alchemy ontology. What is missing is not craft. It is evidence. **Nobody knows how the
results actually distribute, how often the quiz is confident, or whether takers agree with what it
tells them** — because none of that is recorded. The launch is the instrument that would answer it.

---

## What is solid (do not rebuild this)

- **The scorer is honest.** `score.ts` uses percent-of-max per superpower (so an unbalanced item
  bank is normalised away), a fixed non-random tie-break, and it reports **primary + secondary +
  margin + a confidence flag** rather than a single forced label. A near-tie reads as *"Strategist,
  with a Coach wing,"* which is the right humility for a typology.
- **The anti-Barnum work is real.** `BARNUM_CHECK.md` tests each description for falsifiability, a
  behavioral (not adjectival) claim, a **shadow that a reader could reject**, and cross-distinctness
  from its neighbor. The copy holds up — *"half your best work looks, from the outside, like
  nothing happened at all"* (Connector) is specific and losable, not flattery-for-everyone.
- **The ontology is not arbitrary.** Each superpower is defined by an **emotion arc** from the
  book's five channels (Strategist = Fear→Clarity, Disruptor = Anger→Triumph) and one or more
  **allyship domains** (RAISE_AWARENESS, DIRECT_ACTION…). The quiz is a real expression of the
  book's system, not a personality-quiz skin bolted on.

**So the review is not "fix the quiz." It is "find out if it lands, and close one coherence gap
before the launch sends strangers through it."**

## Three findings

### 1 · The real gap — it has never been measured on players *(highest value)*

**There is no analytics on the quiz result.** `leads.ts` saves the lead and emails the result;
nothing records the *distribution* of outcomes. That leaves three questions unanswered, and they
are exactly the "is it useful" questions:

- **Distribution.** Does the item bank secretly funnel most people to one or two superpowers? A
  typology where 60% of takers get "Alchemist" is not diagnostic, however good the copy is. Twelve
  items scoring seven types is tight; whether they discriminate evenly is an empirical fact nobody
  has.
- **Confidence rate.** The scorer flags a result "not confident" when the top-two margin is under
  0.10 (`CONFIDENCE_THRESHOLD`, itself marked *Open Q #1* in the code). If a large share of real
  takers land under that line, the quiz is guessing more than it admits — and the threshold needs
  tuning against data, not intuition.
- **Agreement.** Do people say *"yes, that's me"?* The Barnum doc's own open action item is a live
  A/B: show a taker a *foreign* superpower and confirm they rate their own as the better fit. That
  test has never been run.

**The launch is the instrument.** Real strangers will take this quiz as the pre-work. Logging the
anonymized result — primary, secondary, margin, confident, orientation — turns the launch into the
validity study the quiz has been owed since it was built. That is the single highest-value change,
and it is a few lines, not a redesign.

### 2 · A terminology collision to reconcile before the book funnels people through it

**The quiz calls a superpower your "Face." The book and the character sheet do not.** In the
reveal, `homeFace` is set to the top *superpower's* label and the promise reads *"the Face you
ranked last."* But `instruments/character_sheet.html` has a **"Home face" field whose values are
the six Game Masters** — Shaman, Challenger, Regent, Architect, Diplomat, Sage — **and a separate
"Superpower" field.** So a launch reader can take the quiz, be told their "home Face" is
*Connector*, then open a book whose Faces are *Shaman / Challenger / …* and meet two different
systems wearing one word.

**This needs a ruling, not a guess.** Either the seven superpowers and the six Faces are one
system (then the reveal should say so and map them) or they are two layers — the individual gift
versus the group role — in which case **the reveal should stop calling the superpower a "Face"**
and the lead field should be renamed off `homeFace`. The fix is small; the confusion, at the exact
moment a reader crosses from quiz to book, is not. *(Verify against Chapter 9, which the reveal
cites as arguing "the avoided Face is the more interesting half" — that line has to mean the same
"Face" the reader just got.)*

### 3 · The next step is built for a logged-in player, not a cold launch visitor

**The reveal's richer handoffs assume an account.** The result persists to a logged-in player's
`CampaignMembership` and loadout, and points at the "Take this move in The Crossing" campaign. A
launch visitor arriving cold from a Partiful text is **logged out** — they get the reveal and the
email, which is fine, but the deeper value (the saved sheet, the campaign) is gated behind a
sign-in they have no reason to do yet. **For the launch, confirm what a logged-out finisher sees
next is worth their time on its own** — the emailed result and a single clear invitation (the book
PDF, the course preview), not a CTA that needs an account to pay off.

## What to actually do

1. **Instrument it for the launch.** Log the anonymized result on every completion (primary,
   secondary, margin, confident, orientation). Cheap, and it is the only way the launch answers the
   question Wendell is asking. Read the distribution after the first fifty takers.
2. **Rule on the "Face" collision and apply the small fix** — rename or map — before the pre-work
   goes live, so quiz and book agree on what a Face is.
3. **Optionally run the Barnum A/B** the design already specced: one foreign-type description shown
   to a sample, confirm they prefer their own.
4. **Confirm the logged-out finisher's next step** is self-contained.

**What not to do: rebuild it.** The instrument is good. The work is to measure it, name one word
consistently, and let the launch tell you the truth the design could only assume.
