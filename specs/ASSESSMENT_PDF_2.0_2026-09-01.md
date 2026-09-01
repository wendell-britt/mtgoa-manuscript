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

## 2 · FR-3 is the load-bearing one and it is a real build change

**The spec calls the page footer the only element that survives a screenshot.** It is right,
and the current design has no footer at all.

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

**The remedy is a foot line distinct from the head line**, present on every page including the
matter, carrying the title and the tracking URL, while the existing head line keeps the folio
and the running head where they are. **That is a change to the page furniture in
`design.typ`**, not a content change, and it does not repaginate.

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

**Tested against the installed Typst 0.15, and it does not.** `pdf_standards=["a-2b"]` and
`["a-3b"]` both compile and both emit a `StructTreeRoot`. `["ua-1"]` compiles too, and its
failures are precise:

```
PDF/UA-1 error: missing document title      → the template already sets one
PDF/UA-1 error: missing alt text            → the cover, and any figure
```

**So PDF/UA-1 turns accessibility into a build gate rather than an aspiration.** The compiler
refuses to produce the file until the alt text is there, which is a far better mechanism than a
checker run after the fact and forgotten. **The file has exactly one image — the cover — so the
first pass is one alt string.**

**Do this early rather than late.** It changes the compile call, and discovering at the end
that a standard rejects part of the design is the expensive order.

## 5 · Three decisions blocked on Wendell, and nothing downstream moves without the first

**FR-7, the tracking URL.** A redirect he controls, used nowhere else. **FR-8's QR code encodes
it, FR-4 and FR-5 both print it, and FR-3's footer repeats it 388 times.** Four requirements
wait on one decision, and it is the cheapest decision in the spec.

**FR-10, the companion hub.** The spec puts it out of scope to build and requires that it exist
and be linkable. Until there is a URL, the closing block cannot be written to point anywhere.

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
