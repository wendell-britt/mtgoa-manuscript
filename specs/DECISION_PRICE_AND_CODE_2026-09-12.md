---
type: decision
title: "Two physical channels — $30 on Amazon, $40 from Wendell, both carrying the course"
aliases:
  - paperback price
  - course code
  - oq-1
tags:
  - product
  - mtgoa
  - pricing
  - funnel
created: 2026-09-12
review: 2026-09-19
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - specs/SPEC_BOOK_PAGE_2026-09-08.md
  - marketing/ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md
  - marketing/DECISION_FUNNEL_2026-09-01.md
---

# Two rulings, 2026-09-12

**Wendell:** *"Paperback list price is $40. Print and kindle will have a code in the book
for the course."*

---

## 1 · The paperback lists at $40 — OQ-1 closed

KDP pays 60% of list minus the printing cost. At $40 against the confirmed $5.60 print cost
that is **$18.40 a copy**, against $12.40 at the $30 list the spec carried as provisional.

**It also holds the Kindle where it was put.** The 70% royalty tier requires the ebook list
sit at least 20% below the print list. Twenty percent below $40 is $32, so $9.99 clears it
with room, and the gap between the two editions is now fourfold — which is the property the
spec wanted from the Kindle in the first place: the cheap way in rather than the real
product.

### A correction to a number given in chat on 2026-09-08

**I said a 500-copy run at $40 returns $9,200. That treats all 500 as Amazon sales and it
is wrong.**

`ANALYSIS_BACKER_OBLIGATIONS_2026-08-24` puts the obligation at **247 printed books owed to
Kickstarter backers**, fulfilled with author copies at cost rather than sold. So a 500-copy
run is 247 obligations and **253 sellable copies**.

| | |
|---|---|
| 253 sellable copies at $40 on Amazon | **$4,655.20** |
| 247 backer copies at $5.60 author cost | **$1,383.20** plus shipping |

**The run size is not settled by this ruling and should be argued against 247 rather than
500.** `ANALYSIS_BACKER_OBLIGATIONS` already says so: *"a run of 500 covers the 247 I owe
and leaves stock to sell."*

### Where the $30 still stands

**The Gumroad floor is unchanged.** D-1 and D-2 are about the digital edition and this
ruling does not touch them.

---

## 2 · Print and Kindle carry a code — the entitlement gap closed

`SPEC_BOOK_PAGE` §5 named this as the one unsolved part of course access, because Amazon
does not say who bought. **The ruling takes the printed-code option over the manual claim
form.**

### It is one code per edition, not one per copy

**KDP does not print variable data.** Every copy of an edition carries the same string, so
the code is a shared secret from the moment one reader posts it. That is a property of the
decision rather than a defect in it, and it wants a deliberate answer on the `bars-engine`
side rather than a surprise later: **one redemption per account, and a rate limit.** The
grant itself already exists — `src/lib/book-access.ts` gates on `book-digital` via
`hasCapability`.

### It must not appear in the shareable PDF

**A code printed in the share PDF is public the first time somebody forwards the file**, and
forwarding is the whole design. The PDF reader does not need it: they reach the course
through `/book`, which is what that page is for.

So the code is a **print-and-Kindle** element, and that is a third target rather than a
second. `SPEC_CLOSING_SEQUENCE` §5 already asks for components that are share-only; this
asks for one that is everything-but-share.

### `back_matter/enrollment.md` is where it goes

That page is already on the spine, already titled "What Comes Next," and already
**print-only** under the 2026-09-08 ruling that moved the ladder to `/book`. Putting the
code there adds no component and needs no new spine entry — it only needs enrollment
restored to the Kindle target as well as print.

**One mechanism note.** `build_pdf.py` and `build_epub.py` both read the single intermediate
`typeset.py` resolves, so print, share PDF and EPUB currently share one spine. **Including a
component in two targets and excluding it from the third is a spine change**, not a
template variable.

### Two checks before the print run

**Repagination.** The print interior sits at 387 pages with a proof ordered against it.
Adding lines to enrollment reflows that page and may push the count. Build and compare
before committing to the run.

**The code has to exist first.** The string printed in the book cannot change afterwards,
so `bars-engine` needs to hold it before the interior is final — the same constraint that
governs the `/book` route, arriving earlier because print has a longer lead time than a web
page.

---

## 3 · What this leaves open

**OQ-2, fulfillment for direct print orders.** Untouched. At a $40 list the Amazon copy nets
$18.40, which is the number any direct-channel alternative now has to beat.

**Run size.** Argue it against 247.

**The `/book` path split**, and **per-chapter course links**, both still open in
`SPEC_BOOK_PAGE`.


---

# SUPERSEDED, same day — $30, and the gate becomes a survey

**Wendell, 2026-09-12, correcting §1 and reshaping §2:** *"The KDP physical copy should have
the $30 pricetag. The Kindle Copy comes with a link without the code for people to buy the
course (if they get it for free we can still make $$$ off of it). Physical copies all come
with the course. Anyone who has physically touched a book gets a copy, and we can just have
a brief survey of how they got there so we can track how people are entering the funnel."*

## The architecture as ruled

| edition | price | what it carries | course |
|---|---|---|---|
| Paperback (KDP) | **$30** | a code | included |
| Kindle (KDP) | $9.99 | a link, no code | sold |
| PDF (Gumroad, PWYW) | $30 floor | `/book` | included via the page |

**The principle underneath it, in his words:** *anyone who has physically touched a book
gets a copy.* The physical object is the entitlement.

## What $30 costs against $40

**60% of list minus the $5.60 print cost is $12.40 a copy, not $18.40.**

| | $30 | $40 |
|---|---|---|
| royalty per copy | **$12.40** | $18.40 |
| 253 sellable copies of a 500 run | **$3,137.20** | $4,655.20 |

**The difference is $1,518 across the run**, and the 247 owed to backers are unaffected
either way because they are fulfilled at author cost rather than sold.

**The Kindle stays legal.** The 70% tier needs the ebook at least 20% below print list.
Twenty percent below $30 is $24, so $9.99 clears with room.

## The code stops being a lock and becomes a doorbell

**§2 above treated the shared code as a leak to be rate-limited. Under this ruling the leak
is the intent.** Everyone who claims gets in, so the code's job is to mark the reader as
someone holding a book rather than to prove it. **One redemption per account is still worth
having** — it keeps one person from claiming forty times — but blocking a stranger who found
the code is no longer a goal.

**One constraint from §2 dissolves.** The string no longer has to be a secret generated and
held in `bars-engine` before the interior is final. It has to exist, and it has to resolve.

**The Kindle's link is a sale, not a claim.** Same page, different offer: the print reader
claims, the Kindle reader buys.

## The survey is the instrument, and it reaches where nothing else does

**FR-7's tracking URL only separates PDF holders from everyone else.** It cannot tell an
Amazon paperback buyer from somebody who picked the book up at a talk, found it in a
bookstore, or was handed it by a friend — **and those are exactly the paths Amazon hides**,
since it never says who bought.

**So the survey is not redundant with FR-7. It covers the hole FR-7 cannot reach.** That is
the strongest argument for it and it should be written down before somebody trims it as
duplicate tracking.

### One design decision it forces

**Before access or after.** A survey ahead of the course is friction on the thing being
given away; a survey after is data that may never arrive. **Not decided here.**

### What it should ask

Enough to name the entry path and no more. Where the book came from — Amazon, a bookstore, an
event, a gift, a backer reward — is the question the funnel needs answered.

## What this changes elsewhere

**`SPEC_PDF_2.0` OQ-1 now reads $30**, re-patched the same day.

**`SPEC_BOOK_PAGE` §2 needs a third arrival.** The page currently serves the PDF reader.
It now also serves a print reader claiming with a code and a Kindle reader arriving to buy,
and the three see different things.

**OQ-2 gets harder, not easier.** At $30 the Amazon copy nets $12.40, so a direct channel
has a lower bar to clear — but the direct copy also has to carry the course, which the
Gumroad PWYW edition already does through `/book`.


---

# CORRECTED, same day — there are two physical channels, not one price

**I read the $30 and the $40 as competing answers to one question. They are two different
channels and both are live.** Everything above that computes a single paperback number is
wrong; this section replaces that arithmetic.

**Wendell:** *"The KDP print on demand physical copies are $30 they come with a code for the
book. The Kindle Copies don't but push people to the page where they can buy the course. The
KDP copies, from the RUN am making are going to be printed and sent to me to sell (also for
$40). I'm doing a bit of a discount for people who find the book through amazon and not
through my own marketing efforts."*

## The four products

| product | price | what it carries | per copy to Wendell |
|---|---|---|---|
| **Amazon print-on-demand** | $30 | code, course included | **$12.40** (60% of list − $5.60 print) |
| **The run, sold by hand** | $40 | code, course included | **$34.40** before his own shipping and fees |
| **Kindle** | $9.99 | a link to buy the course, no code | ~$6.25–$6.75 after the delivery fee |
| **PDF (Gumroad)** | $30 floor, PWYW | `/book` | ~$29 |

**The two physical editions are the same interior.** One is printed by Amazon on demand when
somebody orders; the other is a batch Wendell orders as author copies, ships to himself, and
sells at events, on tour, and through his own audience.

## The run, with the right arithmetic

Author copies bill at print cost times quantity with **no volume discount**, and shipping is
separate — KDP's own page says *"this price is the lowest price we can offer for your book."*

| | |
|---|---|
| 500 copies at $5.60 | **$2,800** plus inbound shipping |
| 247 to Kickstarter backers | no revenue, obligation discharged |
| 253 sold at $40 | **$10,120** |
| **net on the run** | **$7,320** before outbound shipping and payment fees |

**The direct sales pay for the whole run and the backer obligation inside it, with $7,320
left over.** That is a different picture from the one I gave in chat, where I treated the run
as Amazon inventory and got $3,137.

**Amazon print-on-demand sits outside this entirely.** No inventory, no cap, $12.40 a copy,
running as long as the listing is up.

## The pricing logic, stated as ruled

**Amazon buyers pay less than Wendell's own audience.** His reason: *a discount for people
who find the book through Amazon and not through my own marketing efforts.* The stranger who
stumbles on the listing gets the cheaper price; the reader who arrives through the podcast,
the tour or the Dream 100 pays the full $40.

### One structural exposure, named without a recommendation

**The two prices are attached to an identical object, and both are visible to the same
buyer.** Someone who came through the marketing can search Amazon, find the same book with
the same code and the same course for $30, and buy there. That trade is $12.40 to Wendell
instead of $34.40.

**Nothing currently distinguishes the $40 copy from the $30 one** — same interior, same code,
same course. Whether that gap wants closing, and with what, is not decided here.

## What holds from the sections above

**The Kindle stays legal at $9.99.** The 70% tier keys off the Amazon print list, and 20%
below $30 is $24.

**The code is a doorbell rather than a lock**, and the survey is the funnel instrument. Both
unchanged.

**`SPEC_PDF_2.0` OQ-1 reads $30**, which is correct for the Amazon list — the number that
question was always asking about.

## Unverified

**Whether KDP's terms speak to reselling author copies at a price above the Amazon list.**
The author-copy help page covers cost and shipping and says nothing about resale price, and I
did not find a parity clause either way. **Worth reading the KDP Terms of Service before the
run rather than after it.**


---

# RULED 2026-09-14 — the direct copy is signed

**Wendell:** *"Signed copies solves this problem for me."*

**The $40 copy is signed. The $30 Amazon copy cannot be.** That ends the comparison the
section above named: the two prices stop hanging on an identical object, because Amazon
prints on demand and cannot put a pen to the title page.

## What it costs and what it does not touch

**Nothing in the interior changes.** No spine entry, no component, no repagination, no
proof to re-order. This ruling lives entirely outside the print file, which is what makes
it cheap this close to the run.

**It costs signing time.** 253 copies by hand, plus however many of the 247 get signed.

**It has to appear wherever the $40 does.** The word *signed* is the whole differentiator,
so the direct offer carries it or the differentiator does not exist for the buyer deciding
between two tabs.

## Both open questions closed, same day

**Wendell:** *"247 backer copies get signed. Not numbered."*

**Every copy of the run is signed — all 500.** The 247 discharging the Kickstarter
obligation and the 253 sold at $40.

**Nothing is numbered.** Signed is the whole property.

### The scheduling consequence

**500 signatures sit between the run arriving and the first copy shipping.** That is a
single block of Wendell's time on the critical path to W0, and it is the only step in the
physical plan that cannot be delegated, batched down, or done early — the books have to be
in hand first.
