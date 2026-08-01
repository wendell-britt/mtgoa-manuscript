# SPEC — DL-17, the enrollment page

**Created 2026-08-01.** Branch `claude/edit-enrollment-page`. Draft filed at
`drafts/DRAFT_enrollment_page_2026-08-01.md`. **Not applied** — `back_matter/`
is a shipping surface and takes nothing without Wendell's approval.

---

## 1. The brief that already existed

`marginalia/specs/PRODUCTION_PLAN.md:70`:

> The deck is the practice set. Classes are terms. Working with you is working
> with a Game Master. **The fiction makes the commercial layer diegetic**, which
> resolves the standing problem of not wanting to run Orange sales language: it
> is not a pitch, it is an invitation into a world that already exists in the
> reader's hands.

`build_book.py:104` seats it as **the last page of the book**, after About the
Author. So it is the final thing the reader reads.

## 2. Research — how these pages are built, and what to take

### The commercial spine, from course-sales practice

The standard high-converting outline runs: transformation-focused headline →
the problem → the offer as bridge, broken into modules → social proof → FAQ and
objection handling → price with a payment plan → one clear call to action. A
pre-headline qualifies the visitor. Length scales with price: 500–1,000 words
under $100, 1,500–2,500 up to $500, 2,500–4,000 above that. Guidance is
consistent that a guarantee buried in small text reads as *"you do not believe in
your own product."*

**Taken:** qualification, one clear first action, objection handling, the price
in plain sight.
**Left:** modules, social proof, urgency, and the length. This is a page in a
book the reader already bought, not a page competing for a cold click, and the
whole point of `PRODUCTION_PLAN`'s ruling is that Orange sales language is off.

### Green — belonging, and disqualification as trust

The pattern across coach and practitioner pages: you are not trying to convince
every reader; you make it easy for the right reader to recognise themselves and
decide. Being explicit about who an offer *is not* for reads as honesty rather
than lost conversion, in a category where the purchase is high-trust and
personal. The anti-hype variant is described as *"not hyped, not sold, just
clear."*

**Taken:** an explicit *Not for you if* line on each of the three, and permission
to buy nothing. This is also already the book's ethos — the Heads decline
students, and `PANEL_HEADS_CH9_BUILD` has Elian on record that eleven years of
cases never produced one where asking first cost more than asking after.

### Teal — evolutionary purpose, self-management, wholeness

Laloux's three breakthroughs are self-management, wholeness, and evolutionary
purpose: the organisation *"has a purpose of its own,"* and members *"listen and
understand where the organisation is naturally drawn to go"* rather than predict
and control it.

**Taken, and it is the page's spine:**

1. **The three offers are not a ladder.** No funnel, no tier stack, no
   graduation. The reader routes herself. That is self-management applied to a
   back-matter page instead of an org chart.
2. **The thing exists whether or not she joins.** The village was already playing
   and does not need her admiration. Evolutionary purpose, and it is already
   canon at `ch9:698`.
3. **No scarcity, stated out loud.** No closing cohort, no expiring bonus. The
   page gives its reasoning rather than just declining the tactic: a practice
   taken on because a clock was running gets dropped when the clock stops.
4. **The succession beat.** Certification framed as handing the method off, which
   is `ch9:159` and `ch9:192` already, and is the clearest Teal move available —
   the purpose outliving the founder.

## 3. Structure of the draft

| Section | Job | Provenance |
|---|---|---|
| Opening | Names where she actually stands: a sheet in her handwriting, a quest from ch1, six Faces she can tell apart live | `ch1:199`, `ch1:205` |
| *"Not a ladder"* | Kills the tier read before it forms | Teal, self-management |
| The deck | What it is, private use before public | `ch9:694` |
| The classes | A term, run the way the schools run them | `front_matter/headmasters_letter.md` verbatim on the shape of a term |
| Coaching + certification | The succession | `ch9:159`, `ch9:698` |
| Three *Not for you if* lines | Qualification, and the book's own ethos | Green |
| *Start with the deck* | The single call to action the research is unanimous about | `ch9:702` |
| *What none of this is going to do* | Anti-scarcity, with the reasoning shown | Teal |
| Permission to buy nothing | *"If none of the three is right, that is a legitimate outcome of reading this book"* | Green |
| The address | Plain contact, no form | — |

**The app is absent**, per the v1 removal ruling. `ch9:698`'s middle offer was
bars-engine and the non-profit; the classes take that seat, which is what
`PRODUCTION_PLAN` intended (*"Classes are terms"*).

## 4. Measurement

Taken while the draft was staged at `back_matter/enrollment.md`, then moved out.

- **`gate.py` — GATE PASS**, every counter 0 on all four surfaces including
  `matter`.
- **`build_book.py`** — gaps drop from **2 to 1**. Only Kickstarter backers
  (DL-16) remains.
- **`placeholders.py`** — 2 new `author-slot` hits, which is the rule working.
  Prices and term length are Wendell's to supply and are not draftable.
- **`prose_diet.py`** — after three fixes, all six counters under 1.30:
  be 1.07 · copula 1.11 · waste 1.07 · zombie 0.54 · expletive 1.13 · passive 0.53.
  First pass read passive **1.56**; three constructions had a hidden doer
  (*"was written to make possible"* → *"I wrote this book to make possible"*;
  *"cannot be delivered in a book"* → *"no book can deliver that"*; *"the money
  is well spent"* → *"the money buys anything"*). The one remaining passive is
  *"signed up to be practised on"*, lifted from the Headmaster's letter.
- **612 words.**

## 5. Open

- **`WENDELL:` prices** for all three, and whether the deck ships or pre-orders.
- **`WENDELL:` the length of a term**, and when the next one opens.
- Placement question: `about_the_author.md` currently calls Wendell *"the builder
  of bars-engine, the app this book routes to."* That line is already on the
  app-removal cut list and sits on the page immediately before this one.

## 6. To land it

    git mv drafts/DRAFT_enrollment_page_2026-08-01.md back_matter/enrollment.md

One command, after approval. It touches no chapter, so DL-18 does not hold it.
