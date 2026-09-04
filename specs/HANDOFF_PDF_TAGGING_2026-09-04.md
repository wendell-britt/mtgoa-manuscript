---
type: handoff
title: "Tagging the PDF edition — why the flag alone fails, and the change that works"
aliases:
  - pdf tagging handoff
  - struct tree handoff
  - ac-12 handoff
tags:
  - product
  - mtgoa
  - pdf
  - production
  - accessibility
created: 2026-09-04
review: 2026-09-11
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - specs/ASSESSMENT_PDF_2.0_2026-09-01.md
  - instruments/build_pdf.py
  - instruments/build_pdf_ebook.py
  - instruments/book/mtgoa.typ
---

# Tagging the PDF edition

**Written from a session that could read this repo and could not build it.** No `typst`,
no `pymupdf`, no `pypandoc`, and no network to install them. So every claim below about
the *source* was read out of the files and every claim about the *output* is a prediction
that the next session has to verify. The verification commands are given at each step and
they are the point of the document.

---

## 1 · Two corrections to a report given in chat on 2026-09-04

**FR-1 and FR-2 are already implemented and were reported as open. That was wrong.**
`build_pdf_ebook.py` sets `subject`, `keywords` and `producer` on top of title and author,
and saves the share edition under `SHARE_FILENAME` rather than the build stamp — all of it
on the `--share` path, with the requirement numbers in the comments. The grep that produced
the earlier report searched the wrong terms. Nothing is owed on the metadata pass.

**What is left of "tagging and metadata" is the tagging, and it is not a flag.**

---

## 2 · The finding — an amendment to ASSESSMENT_PDF_2.0 §4

§4 tested `pdf_standards=["a-2b"]` against the 387-page interior, got `tagged: True`, and
concluded that half of AC-12 is available today. **The test is correct and the conclusion
does not survive the rest of the pipeline.**

`build_pdf_ebook.py` opens a **new** document, draws the cover on page 1, and calls
`insert_pdf` to bring the interior in:

```python
out = pymupdf.open()
page = out.new_page(width=W, height=H)
...
page.insert_image(rect, filename=cover)
out.insert_pdf(src, links=True, annots=True)
```

**PyMuPDF does not merge or preserve `StructTreeRoot`.** Issue #2469, filed 2023-06-14,
still open, labelled enhancement. The maintainers' description of the current behaviour
names this exact case: creating a new PDF and appending others loses the structure
information entirely.

So turning the flag on produces **a tagged interior and an untagged shipped file.** §4's
measurement would keep reading `tagged: True` at the point it was taken, and the artifact
handed to a reader would fail. That is the worst shape a check can have, and it is the same
defect class as the hard-coded component map that §4's own file records: *a page number is
not a verification.*

**There is a second consequence.** The cover never passes through Typst — it is drawn by
pymupdf — so there is nowhere in the template to hang its alt text. The one image in the
book is invisible to the only tool that can tag it.

---

## 3 · The change

**Move the cover into the share interior, and stop rebuilding the document downstream.**

The template already has the mechanism: `SHARE-URL` is a pandoc variable that is empty for
print and set for the PDF edition, precisely so the two interiors can differ. The cover
takes the same route. The print interior is untouched and still carries no cover, which is
what `build_pdf_ebook.py`'s docstring correctly insists on — the press takes a separate wrap.

**The cover is a two-page leaf, not one page, and that is the load-bearing decision.**

Every parity rule in the template counts physical pages: `pagebreak(to: "odd", weak: true)`
at `mtgoa.typ:364` puts openers on rectos, and `let verso = calc.even(loc.page())` at
`mtgoa.typ:189` decides which side of the running head carries the book and which carries
the chapter. **A one-page cover flips both for the whole book.** An even-page cover leaf —
the artwork on a recto, a blank verso behind it, which is how a physical book works — leaves
every parity rule true and reduces the change to one arithmetic fix in `folio()`.

---

## 4 · The diff

Line numbers are anchors from the 2026-09-04 state of the branch, not patch offsets.

### 4.1 · `instruments/book/mtgoa.typ` — the cover variables

Add beside `SHARE-URL` (currently line 213). Empty strings are the print case; pandoc
substitutes an unset variable to the empty string, which the SHARE-URL comment already
records and relies on.

```typst
// COVER, added 2026-09-04. The PDF edition's page one IS the cover — see
// build_pdf_ebook.py's docstring on why the print interior must never carry one.
// It lives here rather than in pymupdf because a document assembled after the fact
// cannot be tagged: PyMuPDF drops StructTreeRoot on insert_pdf (issue #2469), so a
// post-hoc cover and an accessible file are mutually exclusive.
//
// Two pages, not one. Every parity rule below counts physical pages, and an odd
// cover inverts recto/verso for the whole book.
#let COVER-PATH = "$cover-path$"
#let COVER-ALT = "$cover-alt$"
#let COVER-FILL-HEX = "$cover-fill$"
#let COVER-FILL = if COVER-FILL-HEX != "" { rgb(COVER-FILL-HEX) } else { luma(0) }
#let COVER-PAGES = if COVER-PATH != "" { 2 } else { 0 }
```

### 4.2 · `instruments/book/mtgoa.typ` — the folio offset

`folio()` at line 149 numbers front matter with the raw physical page, so the cover leaf
would shift every roman numeral by two.

```diff
 #let folio(loc) = {
   let p = loc.page()
   if p < folio-origin(loc) { return none }
   let origin = arabic-origin(loc)
   if origin == none or p < origin {
-    numbering("i", p)
+    // The cover leaf is physical pages that the folio sequence does not count.
+    numbering("i", p - COVER-PAGES)
   } else {
     numbering("1", p - origin + 1)
   }
 }
```

**`verso` at line 189 and `pagebreak(to: "odd")` at line 364 need no change.** That is what
the even leaf buys, and it is worth stating so nobody "fixes" them later.

### 4.3 · `instruments/book/mtgoa.typ` — the cover pages

Immediately before the body variable near line 597. `header: none, footer: none` is what
keeps the share line off the artwork; `page-role` is never consulted for these pages.

```typst
#if COVER-PATH != "" [
  #page(margin: 0pt, header: none, footer: none, fill: COVER-FILL)[
    #align(center + horizon,
           image(COVER-PATH, alt: COVER-ALT, fit: "contain", width: 100%, height: 100%))
  ]
  #page(margin: 0pt, header: none, footer: none, fill: COVER-FILL)[]
]
```

### 4.4 · `instruments/build_pdf.py` — pass the cover through

`to_typst()` at line 154. `edge_color()` stays where it is in `build_pdf_ebook.py` and is
imported, because the corner-sampling logic is right and only its consumer moves.

```diff
-def to_typst(src, out, trim, share_url=""):
+def to_typst(src, out, trim, share_url="", cover=None):
...
                     "--variable", "share-url=%s" % share_url,
+                    "--variable", "cover-path=%s" % (cover["path"] if cover else ""),
+                    "--variable", "cover-alt=%s" % (cover["alt"] if cover else ""),
+                    "--variable", "cover-fill=%s" % (cover["fill"] if cover else ""),
                     ])
```

Add a `--cover` flag next to `--share-url=` in the argv loop at line 375, resolving the path
through `build_pdf_ebook.find_cover()` and the fill through `edge_color()`, converted to a
six-digit hex string.

**The alt string, which is the whole of the accessibility work for the one image:**

> Front cover of *Mastering the Game of Allyship* by Wendell Britt.

Wendell should replace that with what he wants read aloud — it is customer-facing text and
takes the standing review pass like any other.

### 4.5 · `instruments/build_pdf.py` — the standard

The compiler call at line 294.

```diff
 compiler = typst.Compiler(typ, root=ROOT, font_paths=[FONTS],
-                          ignore_system_fonts=True)
+                          ignore_system_fonts=True,
+                          pdf_standards=["a-2b"])
```

**Unverified: whether `pdf_standards` belongs on `Compiler(...)` or on `compile(...)` in the
installed typst-py.** §4 recorded the keyword and the result, not the call site. Try the
constructor, and move it to `compile_with_warnings(output=pdf, pdf_standards=["a-2b"])` if
it is rejected.

### 4.6 · `instruments/build_pdf_ebook.py` — stop rebuilding the document

The share path must not create a second document. Replace the `pymupdf.open()` /
`new_page` / `insert_image` / `insert_pdf` block at lines 216–231 with an in-place route,
gated explicitly rather than inferred:

```python
if share:
    # The interior already carries its cover, built by Typst under a PDF standard.
    # Opening it in place is what preserves StructTreeRoot: any route through a new
    # document and insert_pdf drops it (PyMuPDF #2469).
    out = pymupdf.open(interior)
    toc_shift = 0
else:
    out = pymupdf.open()
    ...existing cover-drawing path, unchanged...
    toc_shift = 1
```

Then the outline arithmetic loses its hard-coded `+ 1`:

```diff
-out.set_toc([[lvl, title, pno + 1] for lvl, title, pno in toc])
+out.set_toc([[lvl, title, pno + toc_shift] for lvl, title, pno in toc])
```

and the same substitution applies to the component rows built from `comp` further down.

**The save needs watching.** `out.save(dest, deflate=True, garbage=3)` at line 291 rebuilds
the xref. `StructTreeRoot` is referenced from the catalog and should survive garbage
collection, but that is a prediction. If the assertion in §4.7 fails, drop to `garbage=0`
before looking anywhere else.

### 4.7 · The assertion that makes this permanent

Into the verification block after line 294. **This is the most valuable line in the change,**
because it is the check whose absence let a tagged interior and an untagged product coexist.

```python
if share:
    cat = chk.pdf_catalog()
    if chk.xref_get_key(cat, "StructTreeRoot")[0] == "null":
        problems.append("StructTreeRoot missing — the file would ship untagged.")
    if chk.page_count != src.page_count:
        problems.append("page count %d, expected %d (cover is inside the interior)"
                        % (chk.page_count, src.page_count))
```

Note the second one: the existing check is `src.page_count + 1` and is correct only for the
non-share path. Both branches now need their own expectation.

---

## 5 · The order to work it, and what to check at each step

Each step is verifiable on its own. **Do not batch them** — the parity risk in step 1 and
the standard in step 2 fail in different ways and a combined failure is a bisect.

**1 · Template and cover plumbing (§4.1–4.4), no standard yet.** Build the share interior.

    python3 instruments/build_pdf.py --share-url=masteringallyship.com/book --cover

Check: page count is exactly the old count **plus two**; every opener still reports a recto
in `--check`; the roman folios on the front matter read the same numbers they read before;
pages 1 and 2 carry no running head, no folio, and no share line; page 1 is the artwork,
letterboxed on its own edge colour.

**2 · Turn on the standard (§4.5).** Rebuild. Check: it compiles, the page count is
unchanged from step 1, and the interior reports a `StructTreeRoot`.

**3 · Rewire the ebook script (§4.6) and add the assertion (§4.7).**

    python3 instruments/build_pdf_ebook.py --share --check

Check: the assertion passes; the outline still has one level-1 entry per component; every
bookmark still lands on a page that says what the bookmark says — the existing landing
check covers this and it is the one most likely to break, because the `+1` is gone.

**4 · Only then PDF/UA-1.** It fails on one defect §4 already named — the first heading in
the document is not level 1 — and fixing it touches front matter and could disturb the
336-entry outline. Its own pass, its own commit.

---

## 6 · Two decisions for Wendell

**The blank verso behind the cover.** It can be white or filled with the cover's edge
colour. Filled reads as part of the cover on a screen and costs nothing; white announces
itself as a blank page immediately after the artwork. Recommend filled — the diff in §4.3
already does that.

**Whether the plain, non-share PDF edition should also be tagged.** It keeps the old
route in this change and stays untagged. Making both paths tagged means giving the print
interior a cover variable it is designed not to have. Leaving it is defensible: the share
edition is the product, and the plain one is a convenience build.

---

## 7 · What this does not touch

The two blocks from `marketing/PDF_BLOCKS_2026-09-01.md` are still not wired into
`front_matter/`, `back_matter/`, or `build_book.py`'s spine. **When they are, note that
FR-5 will land next to `back_matter/enrollment.md`**, which is titled "What Comes Next" and
already pitches coaching, speaking, the deck and *Igniting Joy*. Two consecutive closing
pages that both want something is the "asked twice" failure EC-5 names, arriving from a
direction FR-4's two-branch framing does not guard. That needs a sequencing decision and
probably a merge, and it is a separate piece of work from this one.

The `/book` route still does not exist, and it gates release rather than build.
