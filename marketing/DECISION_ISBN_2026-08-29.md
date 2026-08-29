---
type: decision
title: "The ISBN — cheapest today, and the one mechanic that decides it"
aliases:
  - isbn
  - isbn decision
  - buy isbn
tags:
  - marketing
  - mtgoa
  - print
  - kdp
created: 2026-08-29
review: 2026-09-05
source:
  - marketing/KDP_LISTING_2026-08-29.md
  - marketing/ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md
  - specs/SPEC_PRINT_READINESS_2026-07-29.md
---

# The ISBN — cheapest today, and the one mechanic that decides it

**Wendell, 2026-08-29:** *"I've already got a cover wrap. What I need now is an ISBN. Let's
find the cheapest one I can get my hands on today."*

**Cheapest today is $0, and it costs nothing later — because of one mechanic.**

---

## The mechanic everything else hangs on

**You cannot change an ISBN on a published KDP book.** Not edit it, not swap it. The only
route is a new edition, which is a new listing that starts at zero reviews and zero rank.

**You can change it freely while the book is in Draft.** And **proof copies can be ordered
from Draft status**, and they print marked *Not For Resale*.

**So the proof does not depend on the ISBN decision at all.** The two things that felt
coupled are not. Take the free one, order the proof today, and the real decision stays open
until the moment you click Publish.

## What each option actually costs

| option | today | publisher of record | travels off the platform |
|---|---|---|---|
| **KDP free ISBN** | **$0** | Amazon | no — KDP only |
| IngramSpark free ISBN | $0 | the imprint **Indy Pub** | no — tied to IngramSpark |
| Draft2Digital free ISBN | $0 | D2D as vendor of record | no |
| **Bowker, single** | **$125** | **you** | yes |
| **Bowker, block of 10** | **$295** — $29.50 each | **you** | yes |

**In the United States only Bowker issues ISBNs**, through `myidentifiers.com`. There is no
second source and no legitimate discount market.

## The recommendation, and it is not the cheapest line in that table

**Take the free KDP ISBN today. Buy the block of ten before you publish.**

**Why the free one today.** It is reversible while the book is in Draft, it costs nothing,
and it removes the last thing standing between you and a proof copy in the post. Nothing
about the proof is affected — it prints *Not For Resale* regardless.

**Why ten rather than one.** The obligations already on the books need more than one ISBN:

| product | ISBN | status |
|---|---|---|
| the trade paperback | 1 | this week |
| the print run for the 247 backers | 1 | a different publisher of record from the KDP edition, so a different ISBN |
| the audiobook | 1 | 16 backers owed |
| the workbook | 1 | 16 backers owed, and not started |
| *Allyship at Work* | 1–2 | `IDEA_ALLYSHIP_AT_WORK_2026-08-27.md` |
| a hardcover, if it ever happens | 1 | speculative |

**Two singles cost $250 and the pack costs $295.** By the second ISBN the pack has almost
paid for itself, and there are at least four coming.

**If $295 is the wrong call this month**, the $125 single is fine and loses only the future
per-unit price. Against a print run that needs roughly $6,000, neither number decides
anything.

## The trap, stated with the way out

**Do not buy a $99 or $110 "ISBN" from a reseller.** They exist and they are cheaper than
Bowker, and the reason is that they come out of somebody else's block — which means **that
company stays the publisher of record in Books In Print forever.** That is the exact thing
you are paying $125 to avoid, so a cheaper one is not a cheaper version of the same product.

**If the price is the problem, the way out is the free KDP ISBN and a bought one later**,
not a cheap one now. A KDP edition published under Amazon's ISBN and a separately printed
trade edition published under yours are **legitimately two products with two ISBNs** — the
standard assigns by publisher and product form, and those differ. Untidy, entirely allowed,
and it defers the whole cost.

## One thing this creates, and it is small

**The interior has no ISBN on the copyright page.** `SPEC_PRINT_READINESS_2026-07-29.md` B3:
*"ISBN lines absent by decision — none assigned."* That was correct when nothing was
assigned.

**It does not block the proof.** A KDP proof does not need it and prints *Not For Resale*.
**It does block the backer edition**, which should carry the ISBN on the copyright page like
any trade book. That is a copyright-page edit and a rebuild, so it belongs on the list
between the proof arriving and the print run going out.

## What I could not verify

**Amazon and Bowker are both unreachable from this session** — every Amazon host answers 403
at the egress proxy, and I read none of these pages directly. Prices and mechanics come from
search-result extracts across several independent publishing sources.

**Two things to confirm in the browser before spending:**

- **The $125 and $295 prices**, on `myidentifiers.com` directly. They are consistent across
  sources but Bowker has raised them before.
- **Delivery speed.** Sources say ISBNs land in the account **immediately at purchase**, and
  separately describe a five-business-day standard processing path with paid priority tiers.
  Those may be the online purchase and the legacy application respectively, but **if you need
  the number today, check before paying** rather than after.

**One exception worth a sentence.** Bowker is the US agency. If you were registering as a
Canadian publisher the ISBNs would be free from Library and Archives Canada, and several
other countries charge little or nothing. Not applicable here, and it is the only way the
$295 goes to zero.

**Sources.** [Bowker / MyIdentifiers, buy
ISBNs](https://www.myidentifiers.com/identify-protect-your-book/isbn/buy-isbn) ·
[KDP on changing or viewing your
ISBN](https://kdp.amazon.com/en_US/help/topic/G8BYTM8CVK74676V) ·
[KDP on proof and author
copies](https://kdp.amazon.com/en_US/help/topic/G7BBN68RYX5UMDZF) ·
[Switching from a free KDP ISBN to your
own](https://nekediting.com/switching-from-a-free-kdp-isbn-to-your-own-everything-you-need-to-know/) ·
[IngramSpark free ISBNs](https://www.ingramspark.com/free-isbns) ·
[Free ISBNs, costs and
trade-offs](https://www.ebookpbook.com/2026/05/16/free-isbns-self-published-book/) ·
[Books.by, how to get an ISBN](https://books.by/guides/how-to-get-an-isbn) ·
[IBPA's Bowker member discount](https://www.ibpa-online.org/page/bowkeridentifiers)
