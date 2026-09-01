---
type: assessment
title: "PDF 2.0 measured against the build — what is already true, what is work, what is blocked"
aliases:
  - pdf 2.0 assessment
  - pdf spec assessment
tags:
  - product
  - mtgoa
  - pdf
  - production
created: 2026-09-01
review: 2026-09-08
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - instruments/build_pdf_ebook.py
---

# PDF 2.0 measured against the build

**The spec arrived on 2026-08-31 written from the product side. This is what the pipeline
actually produces today, measured rather than assumed**, so the work can be scheduled against
real numbers.

**Built for this:** `build/MTGOA_2026-09-01_trade_ebook.pdf` — 388 pages, 5.09 MB, 6 × 9 in
at 432 × 648 pt, 11 pt body.

---

## The headline

**Four of the fifteen acceptance criteria already pass. Two are one line of code. Nine are
real work, and three of those nine cannot start until Wendell owns a URL.**

**One requirement the spec treats as hard turns out to be reachable in the pipeline** — see §4.

## 1 · The scoreboard

| # | criterion | today | cost |
|---|---|---|---|
| 1 | title and author in the window title bar | **passes** — `'Mastering the Game of Allyship'` by `'Wendell Britt'` | done |
| 2 | filename matches FR-1 | **fails** — ships as `MTGOA_2026-09-01_trade_ebook.pdf` | one line |
| 3 | any interior page screenshot carries title and URL | **fails** — see §2 | build work |
| 4 | front provenance block before the contents | **fails** — does not exist | prose + component |
| 5 | closing block names what money funds | **fails** — does not exist | prose + component |
| 6 | QR resolves to the tracking URL | **fails** — blocked on FR-7 | blocked |
| 7 | the FR-7 URL appears nowhere else | **fails** — no URL exists | blocked |
| 8 | no DRM, no password, printing unrestricted | **passes** — no encryption, permissions unrestricted | done |
| 9 | under 10 MB | **passes at 5.09 MB** | done |
| 10 | contents and internal links navigate | **fails** — see §3 | build work |
| 11 | text selectable throughout | **passes** — 2,261 characters extract off page 200 | done |
| 12 | tagged, alt text on all images | **fails** — untagged today, but see §4 | build work |
| 13 | grayscale print loses nothing | **untested** — one image in the file, the cover | check |
| 14 | readable at 390 pt viewport | **probably passes** — 11 pt body on a 432 pt page | check on a phone |
| 15 | no link points at an email capture form | **passes vacuously** — there are no links at all | done |

## 2 · FR-3 is the load-bearing one — BUILT 2026-09-01, and one claim here was wrong

**Correction first.** The first version of this section said *"the current design has no footer
at all."* **It has one.** `running-foot()` exists in `mtgoa.typ` and draws a centred folio on
opening pages and on numbered matter. I measured the bottom band of page 200, which is a
running page where the head draws the folio instead and the foot is legitimately empty, and
reported one page as the design.

**The accurate statement, and it is still the finding:** the foot carried a folio and nothing
else, **no page anywhere in the book carried a URL**, and the only identifying line was the
running head.

**What is actually on an interior page:** a single line at the **top**, at y = 34.8 pt, reading
`186  Mastering the Game of Allyship`. The folio and the running head share it, and it sits at
the head rather than the foot.

**Two problems, and the second is the serious one.**

**The line carries no URL.** So a screenshot identifies the book and offers no way to buy it.

**The line only exists on chapters and appendices.** The template's `RUNS-HEAD` is
`("chapter", "appendix")` by deliberate design — *"a two-page copyright with a running head on
it reads as a mistake"* — so **every page of front matter and back matter carries no
identifying mark whatever**. That includes the provenance block FR-4 puts on page ii and the
closing ask FR-5 puts at the end, which are precisely the pages most likely to be screenshotted
and forwarded.

**Built.** `running-foot()` now carries `Mastering the Game of Allyship · masteringallyship.com/book`
at 7.5 pt in luma 110, on every page that is not a deliberate blank, while the head keeps the
folio and running head exactly where they were. **387 pages, 373 carry the line, and the 14
that do not are the inserted blank leaves** — verified page by page, every one of them empty.

**That is a deliberate reading of FR-3's "every page."** A blank leaf carrying a URL would be
the printing error the whole `is-blank` machinery exists to prevent, and it would be the same
defect as a running head on a blank verso. **The rule as built is: every page with content.**

**It does not repaginate.** 387 pages before and after, every opener still on a recto, folio
still continuous.

**It forks the artifact rather than replacing it, too.** `build_pdf.py --share-url=` produces
`MTGOA_<date>_trade_share.pdf` alongside the plain print interior, because a trade paperback
does not carry a URL on all 387 of its pages and both files have to exist at once.
`build_pdf_ebook.py --share` reads the share interior and refuses rather than silently falling
back — picking the wrong interior produces a file that looks right and carries no URL anywhere.

## 3 · There are zero hyperlinks in the file

**Measured: 0 links across all 388 pages, internal or external.**

**The 336-entry outline is a different mechanism** and the distinction matters for FR-11. The
outline is the reader's sidebar, it works, and `build_pdf_ebook.py` was written to fix exactly
that. The contents page itself is unclickable, though, every cross-reference in the text is
dead, and there is nowhere for FR-10's outbound links to attach.

**`masteringallyship.com` already appears eight times in the body text** as plain text with no
link. So NFR-5's *"every link appears as readable text as well as a hyperlink"* is currently
half-satisfied by accident — readable text, no hyperlink.

## 4 · NFR-3 is achievable in the pipeline, and this is the finding worth acting on

**The spec calls accessibility non-optional and the current file is untagged.** The obvious
assumption is that tagging means a post-process through Acrobat, which would put a manual step
between every rebuild and every release.

**Tested against the installed Typst 0.15 on the real 387-page interior, not on a toy file.**

```
pdf_standards=["a-2b"]   OK   tagged: True   2.47 MB
pdf_standards=["ua-1"]   PDF/UA-1 error: the first heading must be of level 1
```

**So half of AC-12 is available today.** PDF/A-2b compiles this book and emits a
`StructTreeRoot`, which is the "tagged document" an accessibility checker looks for.

**PDF/UA-1 fails on one precise, fixable defect** — the first heading in the document is not a
level 1. That is a heading-hierarchy change that touches the front matter and could disturb the
336-entry outline, so it is real work rather than a flag, and it wants doing deliberately
rather than folded into this batch.

**So PDF/UA-1 turns accessibility into a build gate rather than an aspiration.** The compiler
refuses to produce the file until the alt text is there, which is a far better mechanism than a
checker run after the fact and forgotten. **The file has exactly one image — the cover — so the
first pass is one alt string.**

**Do this early rather than late.** It changes the compile call, and discovering at the end
that a standard rejects part of the design is the expensive order.

## 5 · The URLs, settled 2026-09-01, and one risk to FR-7's own purpose

**Wendell:** *"the tracking url is masteringallyship.com/book. We'll need to actually create
this route."* And a second: *"masteringallyship.com/course … takes people to a 30 day course
I'm creating as part of the book promotion campaign."*

**FR-7 is settled and FR-10 has its destination.** Both are now in the file.

**The route does not exist yet, and that gates release rather than build.** The PDF is correct
with the URL in it today; **shipping it before `/book` resolves points 373 pages and a QR code
at a 404.** Build now, release after the route is live.

### SUPERSEDED 2026-09-01 — the funnel settles this, see `marketing/DECISION_FUNNEL_2026-09-01.md`

**Wendell settled the routing the same day and the risk below survives in a sharper form.**
`/book` stays the printed URL and serves the PDF reader's own page — course access first,
the book second, because a person holding the PDF already has the book. **The failure to
avoid is a redirect:** if `/book` redirects to `/course`, the two traffic streams merge and
US-5 stops being answerable. Serve the page at its own path rather than redirecting to a
shared one.

### The original risk, kept for the record

**FR-7 requires the tracking URL be used *only* inside the PDF** — that is what makes US-5
answerable, because the whole question is how much revenue arrives from people holding a copy
somebody handed them. **`/book` is also the most natural path for the website's own book page**,
and the moment anything else links to it, the number stops answering that question.

**The remedy keeps his URL and costs one routing decision:** reserve `/book` for the PDF and
give the website's book page a different path. The PDF's URL stays short and memorable, which
NFR-5 needs because it is printed as readable text for offline copies, and the measurement
survives. **The alternative — a query parameter on a shared path — is uglier in print and
easier to lose when somebody retypes it from paper.**

### The course link is a bigger idea than a link

**Wendell:** *"repurpose that 30 day challenge into a book campaign template that people can
use to develop their own allyship campaigns as they work through each of the chapters."*

**That is the book's own metaphor cashed, and it is worth naming because it changes what the
link is for.** Chapter 1 tells the reader they are a Game Master. **A Game Master runs a
campaign** — a sequence of connected sessions with a through-line, which is exactly what a
thirty-day challenge is. So `/course` is not a marketing appendage bolted to the back; it is
the reader doing what the book spends 387 pages saying they already do.

**One consequence for FR-10.** The spec has all outbound links pointing at the companion hub
rather than at an email form, and `/course` fits that as a hub item. **A campaign template
worked chapter by chapter implies per-chapter links, though**, which the spec does not currently
contemplate and which would be a much larger change than the two blocks in FR-4 and FR-5.
Worth deciding deliberately rather than discovering during implementation.

**53 backers are already owed a course** — `ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md` — and
`course/HANDOFF_COURSE_BUILD_2026-08-22.md` records that it is already being built in
`bars-engine`. **So `/course` is not a new product, it is a route to one that exists**, which
is the cheap version of this idea rather than the expensive one.

**FR-4 and FR-5, the prose.** Both are customer-facing, so both take the full review pass under
the standing rule, and both need something I do not have: **what the money actually funds**, in
his words. The spec says the print run, the podcast and Campaign Zero scholarships. **Whether
that is the framing he wants printed 388 times is his call, not mine.**

## 6 · Two notes on the spec itself

**§9's Kindle observation is right, and here is the number.** At 5.09 MB and $0.15/MB, the
delivery fee on the 70% tier is **about $0.76 a sale**, against $6.99 gross at $9.99 — so
roughly **11% of the Kindle royalty is file size.** NFR-1 pushes the PDF under 10 MB and the
Kindle build wants it as small as it can be made; the spec is correct that these are opposite
incentives, and the gap is large enough to justify a separate asset treatment rather than one
shared build.

**One correction to a number I published on 2026-08-29.** `CHECKLIST_PHYSICAL_PROOF` says the
book has **30 components**. The build reports **28** — `build_book.py`'s spine has 30 entries
and two are optional and currently absent. Fixed there.

## 7 · The order I would work it

1. **Pick the tracking URL.** One decision, unblocks four requirements, costs nothing.
2. **Turn on PDF/UA-1 and add the cover alt text.** Do it before the new components exist, so
   the standard is a gate every later change has to pass rather than a retrofit.
3. **Add the foot line** with title and URL, on every page including the matter.
4. **Set Subject and Keywords** in the metadata, and rename the output file.
5. **Write FR-4 and FR-5**, through the full review pass, once the funding language is settled.
6. **Wire the links** — contents, cross-references, and the outbound hub links.
7. **Then test the physical claims**: grayscale print, phone viewport, QR scan, screenshot.

**Steps 1 to 4 are a day and they are independent of the prose**, which is the argument for
starting there rather than with the writing.
