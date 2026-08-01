// ===========================================================================
// MTGOA — print interior. A pandoc Typst template: the body variable near the
// bottom is where the converted manuscript lands, and everything above it is the
// book design. Do not name that variable in a comment — pandoc interpolates it
// wherever it appears, comment or not, and the first draft of this file set the
// entire manuscript twice, once inside this sentence.
//
// Read `instruments/build_pdf.py` first — it says why Typst and not LaTeX, and
// it owns the checks that decide whether a rendered PDF is allowed to ship.
//
// Trim is 6x9in, the US trade size this book is priced and positioned for.
// Margins are mirrored, so `inside` is the binding edge and swaps sides every
// page. Fonts are the two Typst embeds — no system font is referenced anywhere
// in this file, which is the whole reason a build on a fresh container produces
// the same PDF as a build on Wendell's machine.
// ===========================================================================

#let TRIM-W = 6in
#let TRIM-H = 9in

// Inside runs wider than outside because the gutter eats it. 0.95in is sized for
// perfect binding at this page count; a spiral or a thinner book would want less.
#let MARGIN = (inside: 0.95in, outside: 0.70in, top: 0.85in, bottom: 0.90in)

#let SERIF = "Libertinus Serif"
#let MONO = "DejaVu Sans Mono"

#let BODY-SIZE = 11pt
#let BODY-LEAD = 0.62em

// Hairlines only, and no grey text anywhere in the body. Grey type screens to a
// halftone on a print-on-demand press and comes back muddy at this size.
#let HAIR = 0.4pt + luma(40)
#let HAIR-SOFT = 0.4pt + luma(140)

#let OPENER-MARK = <mtgoa-opener>
#let BOOK-TITLE = "$title$"

// Which kinds carry a running head. Front and back matter run headless — a
// two-page copyright with a running head on it reads as a mistake.
#let RUNS-HEAD = ("chapter", "appendix")


// --------------------------------------------------------------- page furniture
//
// The folio and the running head are both computed by querying the opener marks
// rather than by reading state. A `state` read inside a header resolves at the
// top of the page, before any update in that page's own body has happened, so
// Chapter 1's own opening page would have printed a roman numeral. `query` has
// no such ordering problem: every mark's location is already known.

#let openers-before(loc) = {
  query(OPENER-MARK).filter(o => o.location().page() <= loc.page())
}

#let opener-on(loc) = {
  query(OPENER-MARK).find(o => o.location().page() == loc.page())
}

// Is this one of the leaves Typst inserted to push a chapter onto a recto?
//
// It has to be answered, because Typst prints the running head and the folio on
// the blank it makes, and a blank verso carrying furniture is a printing error on
// every one of them.
//
// The first attempt tested the parity itself — `context { if calc.even(here()
// .page()) { page[] } }` — and that is a feedback loop: inserting the page
// changes the parity that decided to insert it. Typst reported `document did not
// converge within five attempts` and ten chapters opened on a verso anyway.
//
// This asks a question with a fixed answer instead. Every opener drops a tail
// mark before it breaks, so the tail lands on the last page of the component
// that just ended. A generated blank is then exactly a page with a tail
// immediately behind it, an opener immediately ahead of it, and nothing on it.
#let is-blank(loc) = {
  let p = loc.page()
  let opens = query(OPENER-MARK).map(o => o.location().page())
  if opens.contains(p) { return false }
  let tails = query(<mtgoa-tail>).map(t => t.location().page())
  tails.contains(p - 1) and opens.contains(p + 1)
}

// The physical page where arabic numbering restarts, and the first page that
// shows a folio at all. Half title, title, and copyright are counted and not
// numbered, which is how every trade book does it.
#let arabic-origin(loc) = {
  let m = query(OPENER-MARK).find(o => o.value.id == "chapter-1")
  if m == none { none } else { m.location().page() }
}

#let folio-origin(loc) = {
  let m = query(OPENER-MARK).find(o => o.value.id == "contents")
  if m == none { 1 } else { m.location().page() }
}

#let folio(loc) = {
  let p = loc.page()
  if p < folio-origin(loc) { return none }
  let origin = arabic-origin(loc)
  if origin == none or p < origin {
    numbering("i", p)
  } else {
    numbering("1", p - origin + 1)
  }
}

// One page, one folio. The header and the footer are two functions and each one
// has to decide independently, so the rule that says which of them draws it lives
// here rather than in either of them — the first version let both conclude yes and
// every opening page printed its number twice.
//
//   blank   a leaf inserted to reach a recto: nothing at all
//   head    a running page inside a chapter or appendix: running head, folio out
//           on the trimmed edge
//   foot    an opening page, or any front or back matter page: folio centred
//           below, no head
//   none    the half title, title page, and copyright, which are counted and
//           never numbered
#let page-role(loc) = {
  if is-blank(loc) { return "blank" }
  if folio(loc) == none { return "none" }
  if opener-on(loc) != none { return "foot" }
  let cur = openers-before(loc)
  if cur.len() == 0 { return "none" }
  if RUNS-HEAD.contains(cur.last().value.kind) { "head" } else { "foot" }
}

#let running-head() = context {
  let loc = here()
  if page-role(loc) != "head" { return }

  // Verso carries the book, recto carries the chapter. The folio sits on the
  // outside edge in both cases, which is the corner a thumb finds.
  let v = openers-before(loc).last().value
  let f = folio(loc)
  let verso = calc.even(loc.page())
  let left-slot = if verso { f } else { smallcaps(v.title) }
  let right-slot = if verso { smallcaps(v.book) } else { f }

  block(width: 100%, {
    set text(size: 9pt, tracking: 0.04em)
    grid(columns: (auto, 1fr, auto),
      align(left, left-slot), [], align(right, right-slot))
  })
}

#let running-foot() = context {
  let loc = here()
  if page-role(loc) != "foot" { return }
  align(center, text(size: 9.5pt, folio(loc)))
}


// ------------------------------------------------------------------- the devices
//
// Five frame kinds, five treatments. `instruments/typeset.py` decides which block
// is which; this decides what each one looks like. None of them sets italic:
// the source already carries it inside the marked-up prose, and `#emph` toggles,
// so an italic container would flip the whole note upright.

#let dev-marginalia(body) = block(
  width: 100%,
  above: 1.5em, below: 1.5em,
  inset: (left: 1.1em, y: 0.2em),
  stroke: (left: HAIR-SOFT),
  breakable: true,
  {
    set text(size: 9.4pt)
    set par(leading: 0.58em, spacing: 0.95em, justify: false, first-line-indent: 0pt)
    body
  },
)

#let dev-epigraph(body) = block(
  width: 100%,
  above: 0.6em, below: 2.2em,
  inset: (left: 1.6em, right: 1.6em),
  breakable: true,
  {
    set text(size: 9.7pt)
    set par(leading: 0.60em, spacing: 0.95em, justify: false, first-line-indent: 0pt)
    body
    v(0.9em)
    align(center, line(length: 18%, stroke: HAIR-SOFT))
  },
)

// A document inside the document — the admissions handbooks are filed papers, so
// they get a frame and a tint rather than an indent.
#let dev-handbook(body) = block(
  width: 100%,
  above: 1.6em, below: 1.6em,
  inset: 1.0em,
  stroke: HAIR-SOFT,
  fill: luma(248),
  radius: 1pt,
  breakable: true,
  {
    set text(size: 9.7pt)
    set par(leading: 0.60em, spacing: 0.95em, justify: true, first-line-indent: 0pt)
    body
  },
)

#let dev-signature(body) = block(
  width: 100%,
  above: 1.4em, below: 1.8em,
  breakable: false,
  align(right, {
    set text(size: 9.2pt, tracking: 0.02em)
    set par(leading: 0.55em, spacing: 0.8em, justify: false, first-line-indent: 0pt)
    body
  }),
)

// Correspondence, not instruction. Narrower than the measure and centred, so it
// sits on the page like something that arrived rather than something filed.
#let dev-postcard(body) = align(center, block(
  width: 82%,
  above: 1.8em, below: 1.8em,
  inset: 1.0em,
  stroke: HAIR-SOFT,
  breakable: false,
  {
    // The card is centred on the page; the writing on it is not.
    set align(left)
    set text(size: 9.5pt)
    set par(leading: 0.60em, spacing: 0.95em, justify: false, first-line-indent: 0pt)
    body
  },
))

#let dev-sectionsubtitle(body) = block(
  width: 100%, above: -0.35em, below: 1.1em,
  {
    set text(size: 10.2pt)
    set par(leading: 0.58em, spacing: 0.8em, justify: false, first-line-indent: 0pt)
    body
  },
)

// The 63 mid-prose rules. A printed line across the measure reads as a divider
// between parts; these are scene breaks inside one argument, so they get the
// conventional mark instead.
#let scenebreak() = block(width: 100%, above: 1.3em, below: 1.3em,
  align(center, text(size: 10pt, tracking: 0.7em, "···")))

#let horizontalrule = block(width: 100%, above: 1.3em, below: 1.3em,
  align(center, line(length: 22%, stroke: HAIR-SOFT)))


// ------------------------------------------------------------------- the openers

#let opener(kind: "front", label: "", title: "", subtitle: "", id: "",
             book: BOOK-TITLE) = {
  // Dropped before the break, so it lands on the last page of the component that
  // just ended. `is-blank` above reads these; nothing else does.
  [#metadata(id) <mtgoa-tail>]

  // The copyright page is the one component that must land on a verso: it backs
  // the title page, and a leaf between them would be a printing error.
  if id == "half-title" {
    // First page of the book. Nothing to break away from.
  } else if id == "copyright" {
    pagebreak(weak: true)
  } else {
    pagebreak(to: "odd", weak: true)
  }

  [#metadata((kind: kind, id: id, label: label, title: title, book: book)) <mtgoa-opener>]

  // Everything a display page draws goes inside one block, and the reason is the
  // paragraph after it. `first-line-indent: (all: false)` skips the indent on the
  // first paragraph after a block-level element — but `align(center, text(..))`
  // is a paragraph, not a block, so the opening line of every component whose
  // title happened to be a bare line of text came out indented. That was six of
  // the seven appendices and both back-matter pages, flush in some places and
  // indented in others with nothing in the design saying why.
  let drop = if id == "half-title" { 2.2in
    } else if id == "title-page" { 1.7in
    } else if kind == "chapter" or kind == "appendix" { 0.9in
    } else { 0.35in }

  let below = if id == "title-page" { 0em
    } else if kind == "chapter" or kind == "appendix" { 1.5em
    } else { 1.4em }

  v(drop)
  block(width: 100%, above: 0em, below: below, align(center, {
    if id == "half-title" {
      text(size: 15pt, tracking: 0.14em, smallcaps(title))
    } else if id == "title-page" {
      text(size: 23pt, tracking: 0.03em, title)
      if subtitle != "" {
        v(0.9em)
        block(width: 78%, text(size: 11.5pt, style: "italic", subtitle))
      }
    } else if kind == "chapter" or kind == "appendix" {
      if label != "" {
        text(size: 9.5pt, tracking: 0.22em, smallcaps(label))
        v(0.85em)
        line(length: 12%, stroke: HAIR)
        v(1.1em)
      }
      text(size: 19pt, tracking: 0.06em, smallcaps(title))
      if subtitle != "" {
        v(1.0em)
        block(width: 84%, text(size: 11pt, style: "italic", subtitle))
      }
    } else {
      // Front and back matter: same family, quieter. No drop, no rule.
      text(size: 15pt, tracking: 0.08em, smallcaps(title))
      if subtitle != "" {
        v(0.8em)
        block(width: 84%, text(size: 10.5pt, style: "italic", subtitle))
      }
    }
  }))
}

// The title page's byline is authored content, not a template string, so it comes
// through the body like any other prose and needs centring where it lands.
#let dev-centered(body) = block(width: 100%, above: 1.6em, below: 0em, align(center, {
  set par(justify: false, first-line-indent: 0pt)
  body
}))


// ------------------------------------------------------------------ the contents
//
// Built by querying the opener marks, not by `#outline`, because the openers are
// designed pages rather than headings — a heading would have printed twice, once
// as itself and once inside the opener.
//
// Listing starts after the contents page. Nothing that precedes a table of
// contents appears in one.

#let contents-page() = context {
  let self = query(OPENER-MARK).find(o => o.value.id == "contents")
  let start = if self == none { 0 } else { self.location().page() }

  let rows = query(OPENER-MARK).filter(o => (
    o.location().page() > start and o.value.id != "contents"))

  set par(justify: false, first-line-indent: 0pt, leading: 0.55em)
  let last-kind = none
  for o in rows {
    let e = o.value
    let p = folio(o.location())
    if last-kind != none and e.kind != last-kind { v(0.7em) }
    last-kind = e.kind

    block(width: 100%, above: 0.55em, below: 0em, {
      grid(columns: (1fr, auto), column-gutter: 0.8em,
        {
          if e.label != "" and e.kind in ("chapter", "appendix") {
            text(size: 9pt, tracking: 0.12em, smallcaps(e.label))
            h(0.6em)
          }
          text(size: 11pt, e.title)
        },
        align(bottom + right, text(size: 10pt, if p == none { "" } else { p })),
      )
    })
  }
}


// ------------------------------------------------------------------- pandoc glue
//
// Pandoc's Typst writer emits `#emph`, `#strong`, `#link`, `#quote`, `#figure`
// and `#table`, all built-ins, plus `#horizontalrule`, which is not — it is
// defined above. Term lists and table inset come from pandoc's own default
// template and are kept verbatim so a definition list still renders.

#show terms.item: it => block(breakable: false)[
  #text(weight: "bold")[#it.term]
  #block(inset: (left: 1.5em, top: -0.4em))[#it.description]
]


// ------------------------------------------------------------------- the document

#set document(title: "$title$", author: "$author$")

#set page(
  width: TRIM-W,
  height: TRIM-H,
  margin: MARGIN,
  header: running-head(),
  footer: running-foot(),
  numbering: none,        // the folio is drawn by the furniture above
)

#set text(font: SERIF, size: BODY-SIZE, lang: "en", hyphenate: true)

// Indented paragraphs, no space between them, first one after a break flush —
// the trade-book default, and the reason `all: false` is set.
#set par(
  justify: true,
  leading: BODY-LEAD,
  spacing: BODY-LEAD,
  first-line-indent: (amount: 1.15em, all: false),
)

// `sticky` keeps a heading with the text under it, so no section title is ever
// the last line on a page.
#show heading: set block(sticky: true)

#show heading.where(level: 2): it => block(above: 2.0em, below: 0.9em, {
  set text(size: 12pt, weight: "regular", tracking: 0.05em)
  smallcaps(it.body)
})

#show heading.where(level: 3): it => block(above: 1.5em, below: 0.7em, {
  set text(size: 11pt, weight: "bold")
  it.body
})

#show heading.where(level: 4): it => block(above: 1.2em, below: 0.5em, {
  set text(size: 11pt, weight: "regular", style: "italic")
  it.body
})

// A table that cannot break is a table that overflows. The polarity and channel
// tables run long.
#show figure: set block(breakable: true)
#show figure.where(kind: table): set figure(gap: 0.9em)

#set table(stroke: none, inset: (x: 0.55em, y: 0.42em))
#show table: set text(size: 9.6pt)
// Pandoc centres the whole table, and centring propagates into the cells. These
// are text columns; they read from the left edge.
#show table: set align(left)

#set list(indent: 0.6em, spacing: BODY-LEAD, marker: [–])
#set enum(indent: 0.6em, spacing: BODY-LEAD)

#show quote.where(block: true): it => block(
  width: 100%, above: 1.3em, below: 1.3em, inset: (left: 1.4em, right: 0.8em),
  {
    set text(size: 10.2pt)
    set par(leading: 0.58em, spacing: 0.9em, first-line-indent: 0pt)
    it.body
  },
)

#show raw: set text(font: MONO, size: 9pt)

$body$

// The build's verification record. `build_pdf.py` queries this label to check
// that every chapter opened on a recto, that the folio sequence is unbroken, and
// that the contents page numbers are real — none of which can be seen from the
// PDF bytes. `metadata` is a zero-size element, so it costs no page.
#context [
  #metadata((
    pages: counter(page).final().first(),
    openers: query(<mtgoa-opener>).map(o => (
      id: o.value.id,
      kind: o.value.kind,
      label: o.value.label,
      title: o.value.title,
      page: o.location().page(),
    )),
  )) <mtgoa-report>
]
