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
a real anti-horoscope discipline, and the seven superpowers are organised by the book's four
allyship domains. What is missing is not craft. It is evidence. **Nobody knows how the results
actually distribute, how often the quiz is confident, or whether takers agree with what it tells
them** — because none of that is recorded. The launch is the instrument that would answer it.

**One correction to my own first read, because Wendell caught it:** I called the superpowers
*"grounded in a per-superpower emotion arc."* That is wrong, and it matters. **Emotional alchemy
plays on every superpower** — it is a universal layer, not a signature that binds one type to one
channel. See finding 3, because the *code* encodes the binding the ontology rejects.

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
- **The ontology is not arbitrary.** Each superpower is organised by one or more **allyship
  domains** (RAISE_AWARENESS, GATHERING_RESOURCES, SKILLFUL_ORGANIZING, DIRECT_ACTION). That is
  the real grounding, and it is the book's own system, not a personality-quiz skin bolted on.
  *(The `SuperpowerDef` also carries a per-superpower emotion arc — that part is a problem, not a
  strength; see finding 3.)*

**So the review is not "fix the quiz." It is "find out if it lands, and close two naming gaps —
Face versus superpower, and alchemy as universal — before the launch sends strangers through it."**

## Four findings

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

### 2 · The Face collision — the ruling, and the fix

**Superpowers are not Faces, and the quiz should stop saying they are.** In the reveal, `homeFace`
is set to the top *superpower's* label and the promise reads *"the Face you ranked last."* But
`instruments/character_sheet.html` carries **"Home face" (the six Game Masters — Shaman,
Challenger, Regent, Architect, Diplomat, Sage)** and **"Superpower"** as **two separate lines.**
They are two dimensions of one character sheet, not a single axis wearing two names. So a launch reader can
be told their "home Face" is *Connector*, then open a book whose Faces are *Shaman / Challenger /
…*, and meet two systems wearing one word — at the exact moment they cross from quiz to book.

**The ruling (Wendell, 2026-09-04): they are separate layers.** The quiz measures the
**superpower** (one of seven — the individual gift). The **Face** (one of six — the Game Master
role) is a different axis the quiz does not currently measure. Calling the superpower a "Face"
imports the six-role word onto the seven-gift axis. Strip it.

**The fix in bars-engine — copy-only, and deliberately narrow** (`specs/patches/bars-engine-quiz-face-copy.patch`):

- **Changed the player-facing strings only.** The reveal promise (*"the Face you ranked last… the
  avoided Face is the more interesting half"* → *"the superpower you ranked last… the superpower
  you avoid…"*), the email subject (*"Your Face is X"* → *"Your superpower is X"*), and the email
  body's *"the Face you avoid"* → *"the superpower you avoid."* Three files, string literals and
  adjacent comments, no logic.
- **Left the internal identifiers and ESP tags alone on purpose.** `homeFace` / `avoidedFace` are
  function params, and they feed **mailing-list tags** (`face:regent`, `avoids:…`) already in the
  wild. Renaming those would fragment the existing audience for zero player benefit — the reader
  never sees a variable name. The collision is the *text*, and only the text was touched.
- The character-sheet link stays — the **Superpower** line is real; it is just not the **Face** line.
- **Check Chapter 9.** The reveal cites it as arguing *"the avoided Face is the more interesting
  half."* The patch relabels it to *"the superpower you avoid."* If ch9 truly is about an avoided
  *Game Master Face*, the citation points at a different axis and has to move — a content call for
  Wendell, not part of this copy patch.

**The one open question, and it is yours, not the code's:** do the seven superpowers *map* onto the
six Faces (each gift implying a home Face), or are they independent axes each assessed on their
own? The collision fix does not need the answer. A mapping, if one exists, could later let the
reveal show both — *"your superpower is Connector; your Game Master Face is the Diplomat"* — and that
wants a ruling before it is built.

### 3 · The code binds alchemy to each superpower — the ontology says it should not

**`SuperpowerDef` gives every superpower a fixed `emotionArc`** (Connector = Neutrality→Peace +
Sadness→Poignance; Strategist = Fear→Clarity). **That contradicts the ontology: emotional alchemy
plays on *every* superpower, not one channel per type.** A Connector metabolising anger is not off
-model; the code's per-type arc implies they are. This is where I first went wrong reading it, and
it is a real drift, not just my mistake to correct. **Decide what those `emotionArc` / `arc` fields
are for.** If they are a *signature* (the arc this type reaches for first) they should be labelled
as a tendency, never a limit; if they are load-bearing anywhere in scoring or reveal, that is a
binding to remove. Either way the player-facing copy must not imply a superpower owns one emotion.

### 4 · The next step is built for a logged-in player, not a cold launch visitor

**The reveal's richer handoffs assume an account.** The result persists to a logged-in player's
`CampaignMembership` and loadout, and points at the "Take this move in The Crossing" campaign. A
launch visitor arriving cold from a Partiful text is **logged out** — they get the reveal and the
email, which is fine, but the deeper value (the saved sheet, the campaign) is gated behind a
sign-in they have no reason to do yet. **For the launch, confirm what a logged-out finisher sees
next is worth their time on its own** — the emailed result and a single clear invitation (the book
PDF, the course preview), not a CTA that needs an account to pay off.

## What to actually do

1. **Apply the Face rename** (finding 2) before the pre-work goes live. The collision is ruled;
   this is the one change that must land first, because the pre-work funnels strangers from quiz to
   book and the two must agree on what a Face is.
2. **Rule on the per-superpower `emotionArc`** (finding 3) — signature or binding — and scrub any
   player-facing copy that implies a superpower owns one emotion.
3. **Instrument it for the launch** (finding 1). Log the anonymized result on every completion
   (primary, secondary, margin, confident, orientation). Cheap, and the only way the launch answers
   the question Wendell is asking. Read the distribution after the first fifty takers.
4. **Confirm the logged-out finisher's next step** (finding 4) is self-contained.
5. **Optionally run the Barnum A/B** the design already specced: one foreign-type description shown
   to a sample, confirm they prefer their own.

**What not to do: rebuild it.** The instrument is good. The work is to name the axes right (Face vs
superpower, and alchemy as universal), measure it, and let the launch tell you the truth the design
could only assume.
