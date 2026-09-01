---
type: copy
title: "The two PDF blocks — front provenance and closing ask"
aliases:
  - pdf blocks
  - provenance block
  - closing ask
tags:
  - marketing
  - mtgoa
  - pdf
created: 2026-09-01
review: 2026-09-15
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - marketing/DECISION_FUNNEL_2026-09-01.md
---

# The two PDF blocks

**FR-4 and FR-5 of `SPEC_PDF_2.0`.** Both went through the full review pass, since both are
customer-facing.

---

## FR-4 · The front provenance block

**Page ii or iii, before the contents. 96 words.**

If you bought this book, thank you. Somebody has to pay for a book before anybody can tell them whether it was worth the money, and you went first.

If somebody handed you this file, they meant to. They gave you a gift. No page in here is going to ask you to prove you paid, because nobody locked the file. Read it as you would read a book you owned, since you do.

One ask waits at the end, where you can decide what the book turned out to be worth. Until then it is yours.

### Why it does not mention the course

**D-6 says the ask must serve both readers without making the buyer feel asked twice**, and
`EC-5` says to test that specifically. **The cheapest way to pass both is to put no ask here
at all.** This block welcomes and it names the gift, and the last line tells the buyer exactly
where the ask lives so it does not ambush them at the end.

**P-3 is satisfied by a sentence with a doer.** *"They gave you a gift"* rather than *"It was
a gift"* — the first version scored `expletive` 5.21 on the one sentence the principle
requires, and the fix names who did it.

**And *"since you do"* is the blessing D-5 asks for.** No watermark, no rights notice, and the
line grants the ownership rather than describing a tolerance.

## FR-5 · The closing ask block

**The final content pages, before the appendices. 244 words.**

The book hands you the moves. Running them is a different matter, and thirty days is roughly how long a form takes to stop needing your attention.

You can start those thirty days at masteringallyship.com/book. One move a day, worked against something already happening in your own life, and at the end you have a campaign of your own. Campaign is the book's word for a run of connected sessions with a through-line, which is what a Game Master runs. Chapter 1 tells you that you are one.

If you paid for this file, the course is already yours. Open that page and it lets you in.

If somebody handed you this file, the course is open to you too. Sign up with an email and it costs nothing. Pay what the book turned out to be worth if you would rather, and thirty dollars is where most people land, though nothing stops you setting it higher. Buy the course on its own if that is cleaner.

Two other moves help and neither one costs money. A review on Amazon puts the book in front of people who are searching for exactly this and do not know it exists yet; if you bought the book somewhere else, the review posts as unverified and carries less weight, which is worth knowing now rather than after. Sending the book to one person who needs it is how it has travelled this far, and the Amazon link carries it as well as the file does.

Pass it on. That was always the plan.

### The three moves, and what each requirement bought

| element | requirement | how it lands |
|---|---|---|
| what paying gets you | replaces the struck FR-5 item 1 | the course, named as a thing the reader receives rather than as a budget |
| the amount | FR-5 item 2 | *"thirty dollars is where most people land, though nothing stops you setting it higher"* — D-1's floor and D-2's open ceiling in one sentence |
| the free ways in | FR-5 item 3, FR-6, P-5 | signup, review, forward — three, and the first is the strongest |

**`EC-7` is handled honestly rather than optimistically.** *"the review posts as unverified and
carries less weight, which is worth knowing now rather than after."* The edge case says to set
the expectation rather than overpromise, and a reader who finds out afterwards trusts the next
ask less.

**`EC-8` is handled in half a clause.** *"the Amazon link carries it as well as the file does"*
— forwarding the listing is a sale, and the block should not imply the file is the only way to
pass the book on.

**`D-4` is obeyed by omission.** Amazon appears twice and neither mention is a jab. The review
is framed by what it does mechanically, which is put the book in front of people searching.

## The review pass

**Step 0 · ELI5, written first.** *If you paid, thanks. If a friend sent you this, that was on
purpose and you are welcome to it. At the end there is a thirty-day course, and you can get in
by paying, or by signing up, or by buying it on its own. If you have no money, a review and a
forward both help.*

**Steps 0b to 7, both blocks.** `voice` clean · `gate` clean · `slop shapes` 0 · fragments **0
MID, 0 NEG** · pronouns **0 orphans, 0 distant**.

| | be | copula | waste | zombie | expletive | passive | empty | inchoative |
|---|---|---|---|---|---|---|---|---|
| front | 0.82 | 0.86 | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| closing | 1.07 | 0.86 | 1.09 | 0.00 | 0.00 | 0.00 | 0.82 | 0.00 |

**Four defects the counters passed and the slop reading caught.**

| found | why it was wrong | fix |
|---|---|---|
| *"which is what you have been doing all along without calling it that"* | **`MANUSCRIPT_FILE_CANON:154`** — narrates the reader's unnamed history back to her as fact | *"Chapter 1 tells you that you are one."* The claim moves from her past to the book |
| *"though the box has no ceiling"* | *the box* is a Gumroad payment field, invisible to somebody reading a printed page | *"nothing stops you setting it higher"* |
| *"is the move that got the book to you in the first place"* | **True only for the gift reader.** For a buyer it is simply false, and D-6 forbids a block that quietly addresses one of the two | *"is how it has travelled this far"* |
| *"That is what waits at masteringallyship.com/book"* | *That* pointed loosely at the preceding sentence | *"You can start those thirty days at…"* — a doer and a named object |

**One reported fragment, and it is the tagger.** `3a` flags *"Chapter 1 tells you that you are
one."* as a LANDING fragment, because the tagger reads **`tells` as a plural noun** rather than
a verb. That is the per-instance unreliability `fragment.py`'s own docstring documents — *runs/NNS*,
*fades/NNS* — and the sentence is plainly complete. **Recorded rather than acted on**, and
LANDING is legal regardless.

**Step 3.5 · stance.** Person — second person throughout, no first-person plural. Doer — every
verb has somebody doing it; no get-passives. Back-pointer — no vague openers. Membrane — no
fiction present.

## One structural decision these blocks force

**Both belong in the shareable PDF and neither belongs in the print interior.** *"If somebody
handed you this file"* is false in a paperback, and *"nobody locked the file"* means nothing on
paper.

**So they need the same fork the share line already has.** `build_pdf.py --share-url=` produces
a separate interior; these two components should be included on that path and left out of the
print build. **Adding them unconditionally would repaginate the print book**, which currently
sits at 387 pages with a proof already ordered against it.

**That is a build change and it is not made yet.** The prose is ready; where it goes in the
spine, and how the two builds diverge, is the next decision.
