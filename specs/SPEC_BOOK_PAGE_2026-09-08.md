---
type: spec
title: "The /book page — the one destination printed 373 times"
aliases:
  - book page
  - /book
  - pdf landing page
tags:
  - product
  - mtgoa
  - web
  - funnel
created: 2026-09-08
review: 2026-09-15
source:
  - marketing/DECISION_FUNNEL_2026-09-01.md
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - specs/ASSESSMENT_PDF_2.0_2026-09-01.md
  - specs/SPEC_CLOSING_SEQUENCE_2026-09-04.md
  - course/HANDOFF_COURSE_BUILD_2026-08-22.md
---

# The /book page

**`masteringallyship.com/book` is printed on 373 pages of the share interior and encoded in
the closing page's QR code.** It is the only address the PDF carries, it cannot be changed
after a file is forwarded, and as of 2026-09-08 it does not exist. **The route gates
release, not build.**

This spec covers what the page is for and what it holds. It does not cover implementation.

---

## 1 · Who arrives

**A reader holding the PDF.** Somebody gave them the file, or they bought it, and they
reached the end of 387 pages. Both are treated as one audience by the page and separated
only by what they already own.

**Nobody else should arrive here, and that is load-bearing.** FR-7 requires the URL be used
only inside the PDF, because US-5 asks how much revenue arrives from people holding a copy
somebody handed them. **The website's own book page needs a different path.**

**Serve, do not redirect.** `DECISION_FUNNEL` settled this: a redirect to `/course` merges
the two traffic streams the moment it fires, and after that the course page cannot tell a
forwarded-PDF reader from somebody who clicked through from the store. If a redirect is
unavoidable, it carries a parameter that survives into the session and the analytics read
it — more moving parts, and it breaks the first time somebody shares the post-redirect link.

---

## 2 · The offer, in order

**Wendell, 2026-09-01:** *"anyone who gets to this page from the PDF should have access to
the course material. They will need to unlock it with a donation or at least by signing up
with their email. Otherwise they can buy the course as an add-on."*

**The course leads.** A person holding the PDF already has the book; selling them the book
is the wrong offer, and the course is the one thing they do not have.

**1 · The thirty-day course, and three ways in.** Donate, sign up with an email, or buy the
course on its own. Three doors is a choice; one door with an email field is a capture form
wearing a course as bait, and FR-10 rules against pointing the PDF at a bare capture form.
**The difference is visible on the page in about a second**, which is roughly how long the
reader spends deciding.

**2 · A copy of the book, second.** For the reader who was handed the file and wants one of
their own, in print or on Kindle.

**3 · The ladder.** Coaching, speaking, the deck, *Igniting Joy*. **Moved here from
`back_matter/enrollment.md` by the 2026-09-08 ruling** — see
`specs/SPEC_CLOSING_SEQUENCE_2026-09-04.md` §3. `enrollment.md` is the source text for this
section and stays in the print book unchanged.

**The order is the same argument the book's closing page lost.** Free thing first, ladder
second. A reader who just finished the book and lands on four paid offers has been sold to
before being given anything.

---

## 3 · Why the ladder lives here rather than in the file

**Everything on this page can be corrected. Nothing in the PDF can.** Rates change,
availability changes, the deck runs out or gets reprinted, *Igniting Joy* gets a second
edition. A file that keeps getting forwarded for years carries whatever was true on the day
it was built.

**This is the reasoning FR-7 already applies to the destination**, extended to what sits
behind it: the printed URL is a redirect under Wendell's control precisely because the file
is permanent and the target must not be.

---

## 4 · What the page owes the measurement

**One arrival, counted before anything else happens.** US-5 becomes answerable only if
`/book` traffic stays separable from the store's.

**The QR code and the printed line resolve to the same place.** NFR-5 prints the URL as
readable text for offline and printed copies, so the address has to stay short enough to
retype from paper.

**The destination may change; the path may not.** Anything that alters what `/book` serves
is fine. Anything that alters the string is not — it is already in 373 pages of a file that
has been sent to people.

---

## 5 · Open, and blocking

**Entitlement for KDP buyers.** *"Either purchase will give them log-in access to the course
page."* Amazon does not tell you who bought, so print and Kindle buyers have no automatic
path in. The honest options are a code printed in the book or a manual claim form. **A code
in the book is an interior change** and would have to land before the print run.

**53 backers are already owed the course** — `ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md`.
Their entitlement predates every gate described here and has to survive whatever gets built.

**Per-chapter course links.** *"repurpose that 30 day challenge into a book campaign
template that people can use to develop their own allyship campaigns as they work through
each of the chapters."* A link per chapter is a much larger interior change than one closing
page, and it changes what this page is for.

**The org-funding question routes to the volunteer signup**, one line on this page, per the
2026-09-01 ruling that cut the funding statement out of FR-5.

---

## 6 · Release gate

**The PDF is correct with the URL in it today. Shipping it before `/book` resolves points
373 pages and a QR code at a 404.** Build the file now; release after the route is live.
