---
type: decision
title: "The funnel — three doors, and the one that decides whether any of it is measurable"
aliases:
  - funnel
  - book funnel
  - course gate
created: 2026-09-01
review: 2026-09-08
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - specs/ASSESSMENT_PDF_2.0_2026-09-01.md
  - course/HANDOFF_COURSE_BUILD_2026-08-22.md
---

# The funnel — three doors, and the one that decides whether any of it is measurable

**Wendell, 2026-09-01**, in three sentences that settle the architecture:

> *"anyone who gets to this page from the PDF should have access to the course material. They
> will need to unlock it with a donation or at least by signing up with their email. Otherwise
> they can buy the course as an add-on… if they go to the top of the website it will take them
> to the book sales page… Either purchase will give them log-in access to the course page…
> if someone shares a PDF they will get sent to the course page and have the ability to buy
> the course or buy the book."*

---

## The architecture as described

| door | who arrives | what they see | what they get |
|---|---|---|---|
| **`masteringallyship.com`** | anyone | the book sales page | buy print or digital, and **either purchase unlocks the course** |
| **`/book`** | a reader holding the PDF | course access, and the book if they want a copy of their own | unlock by donation, by email, or buy the course as an add-on |
| **`/course`** | anyone with an entitlement | the thirty-day course | login-gated once it is wired to `bars-engine` |

**The load-bearing insight underneath it is right and worth naming: a person holding the PDF
already has the book.** Selling them the book is the wrong offer. **The course is the one offer you have
that they do not**, which is why the shared-copy door opens on the course and
not on the store. That is a better funnel than the spec described, and it came from him.

## The one failure that will happen silently, and the fix is a routing choice

**If `/book` redirects to `/course`, US-5 stops being answerable.**

FR-7 exists for one reason: *"I want to know how much revenue arrives from people holding a
copy someone gave them."* That works only while `/book` traffic is separable from everyone
else's. **A plain redirect merges the two streams the moment it fires**, and after that the
course page cannot tell a forwarded-PDF reader from someone who clicked through from the
store.

**The fix is to serve rather than redirect.** `/book` renders the PDF-reader's page — course
first, book second — at its own path. Same content as `/course` can share, different URL,
and the arrival is counted before anything else happens.

**If a redirect is unavoidable for build reasons**, it has to carry a parameter that survives
into the session (`/course?from=pdf`), and the analytics have to read it. That is more moving
parts than serving the page, and it breaks the first time someone shares the post-redirect
link.

**Two facts make the printed URL settled either way.** It is already in **373 pages** of
the built file, and NFR-5 wants it short and memorable because it prints as readable text for
anyone offline. **`/book` stays.** What changes is what `/book` serves.

## One tension with FR-10, and a way to keep both

**FR-10 says no outbound link points at a bare email capture form**, and the opt-in *"lives on
the hub as one item among several."* **Gating the course behind an email signup is close to
that line.**

**It stays on the right side of it if the page leads with the course and offers three unlock
paths** — donate, sign up, or buy as an add-on. Three doors is a choice; one door with an
email field is a capture form wearing a course as bait. **The difference is visible on the
page in about a second**, which is roughly how long the reader spends deciding.

## What this settles for the PDF's closing block

**FR-5's third element now has a concrete answer.** The non-money actions were an Amazon
review and a forward. **There is now a third, and it is the strongest of them: sign up and
the course opens.** That gives the reader who cannot pay something real rather than a
consolation, which is exactly what principle P-5 asks for.

### FR-5's first element is cut — ruled 2026-09-01

**Wendell:** *"I don't know if we need all of this. It might be useful for a kickstarter
backer, but really if someone is wanting to know about the funding of the organization they
should be signing up to volunteer for the non-profit. I don't know if any other book that
provides that information inside the book itself."*

**He is right, and his third reason is the strongest one.** A funding breakdown inside a trade
book answers a question the reader never asked. It has the shape of an annual report dropped
onto the last page, and it changes register at the worst possible moment — somebody has just
finished 387 pages and the last page they read should not be a budget.

### The principle I leaned on is false, and it is not his — corrected 2026-09-01

**Wendell:** *"'pay-what-feels-right only works when the reader knows what they are funding.'
I didn't write this and I don't agree with it. It doesn't make any sense."*

**Two errors, and the second is worse than the first.**

**1 · I attributed it to him.** The line is P-4 at `SPEC_PDF_2.0_2026-08-31.md:88`, in the
document he handed me, and I called it *"his own P-4"* and *"yours."* **A pasted document is
not line-by-line authored by the person pasting it**, and I had no basis for that inference.
The spec's shape — numbered FR/NFR/EC tiers, a sources list — reads like something drafted
with assistance, which is exactly the case where authorship should be asked rather than
assumed.

**2 · I rescued it instead of testing it.** My previous version said *"P-4 survives, because
it was conflating two different questions"* and then reinterpreted it into something true.
**That is the move where a stated principle gets preserved by rewriting what it meant**, and
it is worse than accepting a bad principle, because it launders one.

**Tested, it is false.** *Only works when* is an absolute, and the counter-examples are
everywhere: buskers, tip jars, Bandcamp, itch.io, *In Rainbows*. **None of them tell you what
the money funds and all of them work.** People pay what feels right because they valued what
they got, not because they were briefed on its budget.

**What is narrowly true is a different claim.** Naming a use can raise average giving in
*charitable* contexts, which is a literature about donations rather than about paying for a
product you already have. **It can also lower it**, by converting a gift into a transaction
the payer starts auditing.

**The outcome does not change and his original reason was the better one all along.** Cut the
funding statement because no trade book carries one and the reader never asked — not because
of a two-questions distinction propping up a principle that should have been struck.

**The accountability version already has a home, too.** `back_matter/kickstarter_backers.md`
is in the book, and the updates carry the money story to the people who are owed it. **The
disclosure is not being lost, it is being put where its audience already is.**

**The org-funding question routes to the volunteer signup**, exactly as he said. Anyone who
actually wants to know how the nonprofit is funded is a person who would volunteer, and
sending them to a signup is a better outcome than a paragraph they skim. **One line on the
`/book` page, not in the book.**

**So the closing block is now three moves, not four:** what paying gets you, the suggested
amount with no ceiling, and the free ways in. **It got shorter, which on a last page is
almost always the right direction.**

## What this does not settle

**Per-chapter course links.** The campaign-template idea — *"repurpose that 30 day challenge
into a book campaign template that people can use to develop their own allyship campaigns as
they work through each of the chapters"* — implies a link per chapter, and the spec
contemplates two blocks and a footer. **That is a much larger change to the interior**, and it
should be decided rather than discovered mid-build.

**The entitlement plumbing.** *"Either purchase will give them log-in access"* means the store
has to hand an entitlement to `bars-engine`, and KDP sales cannot do that at all — Amazon does
not tell you who bought. **So the print and Kindle buyers have no automatic path in**, and the
honest options are a code printed in the book or a manual claim form. Worth naming now because
it is invisible until the day someone with a paperback asks why they cannot log in.

**53 backers are already owed the course.** `ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md`. Their
entitlement predates all of this and has to survive whatever gate gets built.
