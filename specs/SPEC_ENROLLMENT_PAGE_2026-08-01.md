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

## 3b. REVISION — the real offer stack arrived

**Wendell supplied `MTGOA_Backend_Offer_Stack__Dojo_and_Cohort.md`, 2026-08-01.**
The draft was rebuilt against it. Three doors became four, and the two
`WENDELL:` slots are closed.

| Offer | Price | Role |
|---|---:|---|
| Ebook | $15 | entry — irrelevant here, she already owns the book |
| Oracle Deck | $22 | practice tool |
| Allyship Dojo | $99/month | recurring practice container |
| Cohort | $2,500 | application-based transformation container |
| 1:1 with Wendell | $150 | one 90-minute call, a bridge while the cohort is dark |

The source document names the book-buyer sequence itself — *"Do not lead with
another book sale"* — and the draft follows it: deck, Dojo, cohort, 1:1.

**What the offer stack replaced in the draft.** The middle offer had been *"the
classes,"* my inference from `PRODUCTION_PLAN`'s *"Classes are terms."* The real
product is the **Allyship Dojo**, monthly, four domain tracks that map onto the
four domains in Appendix A, running alchemy → trainable skill → Wake Up through
Show Up → quest. That mapping is better than what I invented, because the reader
has already met the architecture.

**The Dojo section also takes the source's own positioning formula** — *offer =
surface desire + sabotaging belief + emotional satisfaction + superpower* — for
one beat rather than four, since running it on every door would produce exactly
the patterned rhythm the slop pass exists to catch. The belief is stated as
*"doing it alone is what proves you were up to it,"* phrased as a claim about the
practice rather than about the reader, which keeps `gate.py`'s A0 counter at 0.

### Five conflicts this surfaced

1. **Certification is in the book and absent from the offer stack.** The book
   promises it three times — `ch9:159`, `ch9:192`, `ch9:698` — and
   `about_the_author.md` says he *"certifies others to run them."* The stack has
   no certification line; the nearest thing is the cohort producing *"the
   capacity to become an Allyship Game Master."* **The book cannot promise a
   product that does not exist.** The draft routes that language into the cohort
   and stops short of promising a credential. Either certification becomes a real
   offer or the three ch9 sites need softening. **Wendell's call.**
2. **Cohort duration is unresolved** — the source says 12 weeks in the operating
   code and six months in the workshop-series document, and rules explicitly:
   *"Do not publish either duration as final."* The draft says **"run in a
   season,"** which is true under both.
3. **The Dojo may not be live at print.** The source says *"$99/month when
   available."* A printed page pointing at a closed door is worse than no page.
   The draft's routing line handles this: *"with what each one costs and what is
   open right now."*
4. **Print permanence, and this is why no price appears.** $99/month and $2,500
   are current operating figures with three open decisions behind them, and a
   physical book cannot be repriced. Every figure routes to
   masteringallyship.com. **Recommend keeping it that way even for the $22 deck**
   — one rule is easier to hold than an exception.
5. **Naming.** *Allyship Dojo* and *Oracle Deck* appear **nowhere** in the
   manuscript, and *Dojo* has no in-world gloss. `PRODUCTION_PLAN`'s diegetic
   instinct is right, and a page that never says the product's real name cannot
   convert, because the reader will not recognise it on the site. The draft uses
   the real names and lets the surrounding prose carry the fiction. Worth a
   deliberate ruling rather than a default.

## 4. Measurement

Taken while the draft was staged at `back_matter/enrollment.md`, then moved out.

- **`gate.py` — GATE PASS**, every counter 0 on all four surfaces including
  `matter`.
- **`build_book.py`** — gaps drop from **2 to 1**. Only Kickstarter backers
  (DL-16) remains.
- **`placeholders.py`** — **3 hits, down from 5.** Both `WENDELL:` slots are
  gone: prices and calendar route to the site rather than into print. The three
  remaining are the pre-existing ch1/ch7 blockers.
- **`prose_diet.py`** — every counter under 1.30:
  be 0.98 · copula 1.23 · waste 1.09 · zombie 0.70 · expletive 0.99 ·
  **passive 0.00**. The first pass read passive **1.56**; three constructions had
  a hidden doer (*"was written to make possible"* → *"I wrote this book to make
  possible"*; *"cannot be delivered in a book"* → *"no book can deliver that"*;
  *"the money is well spent"* → *"the money buys anything"*).
- **668 words.**

## 5. Open

- **The certification question (conflict 1) is the one that matters** — it is a
  promise the book makes three times against a product the stack does not list.
- Ruling on real product names versus in-world names (conflict 5).
- Placement question: `about_the_author.md` currently calls Wendell *"the builder
  of bars-engine, the app this book routes to."* That line is already on the
  app-removal cut list and sits on the page immediately before this one.

## 6. To land it

    git mv drafts/DRAFT_enrollment_page_2026-08-01.md back_matter/enrollment.md

One command, after approval. It touches no chapter, so DL-18 does not hold it.
