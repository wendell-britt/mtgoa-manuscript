# The production pipeline — PDF and EPUB

Two deliverables out of one manuscript. Nothing here edits `manuscript/`.

```bash
pip install pypandoc-binary typst      # or: pip install -r instruments/requirements.txt

python3 marginalia/compile.py --apply  # the frame is part of both editions
python3 instruments/build_book.py      # is the book complete?
python3 instruments/typeset.py         # can it be set? — the transforms and the flags
python3 instruments/build_pdf.py       # -> build/MTGOA_<date>_trade.pdf   (6x9)
python3 instruments/build_pdf.py --trim=all      # every trim preset
python3 instruments/build_epub.py      # -> build/MTGOA_<date>.epub
```

## The trim presets

| preset | trim | type | outside margin | pages |
|---|---|---|---|---|
| `trade` (default) | 6 × 9in | 11/16 | 0.70in | 347 |
| `workbook` | 7.5 × 9.25in | 12/17 | 1.35in | 355 |
| `workbook-9` | 7.5 × 9.00in | 12/17 | 1.35in | 363 |

`workbook` is the trim *The Artist's Way* and most workbooks print at, and a
standard size at both KDP and IngramSpark. It is not the trade page enlarged: 11pt
across 7.5in is a line nobody wants to track back from, so the type goes up, and
the outside margin becomes a working rail rather than white space — on a book
whose method is stopping to do something, the reader needs somewhere to do it.

`workbook-9` exists because retail listings quote 9 and 9.25 interchangeably. Ship
`workbook` unless a printer says otherwise.

Geometry lives in `PRESETS` at the top of `book/mtgoa.typ`. Everything else in
that file is a multiple of the preset's body size, so one design serves all three
and the build verifies that the preset it asked for is the one the document
reports.

Both builders call `typeset.py --write` themselves, so a stale intermediate cannot
be shipped by accident. `build/` is gitignored; the artifacts are derived.

## The four layers, and what each one is allowed to decide

| | file | question it answers |
|---|---|---|
| 1 | `instruments/build_book.py` | Is every component of the book present? |
| 2 | `instruments/typeset.py` | Can it be set — and what did the manuscript leave ambiguous? |
| 3 | `instruments/build_pdf.py` + `book/mtgoa.typ` + `book/devices.lua` | The print interior |
| 3 | `instruments/build_epub.py` + `book/epub.lua` + `book/epub.css` | The ebook |

Layer 2 exists because the two format builders were otherwise going to answer the
same questions separately and answer them differently. A marginal note has to be
the same device in both editions, and a chapter has to open under the same title.

**Layer 2 flags, it does not rule.** A transform lands in `typeset.py` only when
the answer is a fact about typesetting. Where the manuscript is genuinely
ambiguous, it reports a `RULING` and sets the file anyway.

## What the manuscript hands over, and what happens to it

**Five frame devices, all wearing a blockquote.** `<!-- MARGINALIA -->`,
`<!-- EPIGRAPH-BYLINE -->`, `<!-- HANDBOOK -->`, `<!-- SIGNATURE -->`,
`<!-- POSTCARD -->` — correct in the repository, where they stay greppable and
strippable, and unusable in a converter, which sees one grey slab. Each becomes a
classed div, and the two designs style them apart by measure, rule, and space —
never by colour, because a third of readers are on e-ink.

**One chapter heading form, carrying two decks.** `# CHAPTER N: THE FACE — clause`
over the italic subtitle, ruled on master 2026-08-01, closing §6 of
`SPEC_PRINT_READINESS_2026-07-29.md`. Before that canon opened chapters four ways
and `typeset.py` carried a hand-written title per chapter to paper over it. It
reads the heading now; a chapter that does not match the form is a BLOCKER. Both
designs set the three lines in descending size so they read as a hierarchy rather
than as the same thing said three times.

**251 horizontal rules doing two jobs.** 188 sit before a heading, which already
supplies the break. 2 open a component body with nothing above them to separate —
the residue of the provenance headers `build_book.py` strips. 61 are real scene
breaks and become a centred ornament.

**Eleven lists that markdown does not read as lists.** A lead-in with the items
directly under it and no blank line between is one paragraph to any converter, so
`This might look like:` came out with its four items run inline and the hyphens
reading as stray dashes. Obsidian renders the list, which is why it survived —
the vault shows the author what the author meant. Five of the eleven are the five
channel entries in Appendix C.

**Column widths that are really dash counts.** In a pandoc pipe table the dashes
in the delimiter row *are* a width spec. `|---------|---------|---------|------------|---|`
in `manuscript/ch3.md` gave the Five Channels table's last column 6% of the
measure, and "The Superpower" set as `The / Su- / per- / power`. Every table in the
book is specified by whatever the author's hyphen key happened to produce, so
`book/tables.lua` overrides all of them and sizes each column by its content, with
a floor at the longest word it has to hold.

## The checks that earn their keep

Every one of these caught something real on its first run.

- **Chapters open on a recto** — `build_pdf.py`. The first version of the recto
  logic tested page parity from inside a context block, which is a feedback loop:
  inserting the blank changes the parity that decided to insert it. Typst reported
  `document did not converge` and ten chapters opened on a left-hand page.
- **A blank verso is blank** — `mtgoa.typ`. Typst prints the running head and the
  folio on the leaf it inserts to reach a recto. `is-blank` finds those leaves by
  querying marks instead of asking about parity.
- **One folio per page** — `mtgoa.typ`. The header and the footer each decided
  independently, both said yes, and every opening page printed its number twice.
- **The interior font can set every character** — `build_pdf.py`. Typst emits no
  warning for a missing glyph; it just draws a box. Rendering each character
  against U+FFFF found `五行` in Appendix G, which was setting here only because
  this container happens to carry a CJK font. Closed 2026-08-01 by committing
  those two glyphs — see `fonts/make_subset.py`, 2.8KB, and the licence beside it.
- **The frame survives conversion** — `build_epub.py`. Per device, in against out.
  A frame that fails to convert produces an ebook that opens, reads, and has one
  voice in it instead of two.
- **Nothing is `<pre>`** — `build_epub.py`, budget zero, inherited. A fenced block
  does not reflow; a phone gives you 40 characters and the widest was 98.

## Design decisions worth knowing before you change them

**Typst, not LaTeX.** A TeX distribution able to set this book is a multi-gigabyte
install; Typst is a 30MB wheel that embeds its own fonts.

**Libertinus Serif, and `ignore_system_fonts=True`.** The interior uses only fonts
embedded in the Typst binary, so the PDF is the same on any machine. This
container offers Bitstream Charter — a better book face, and one that would have
made the build unreproducible. Any font warning fails the build.

**6x9in, mirrored margins**, inside 0.95in for a perfect-bound gutter at this page
count. A different binding wants a different inside margin.

**The contents runs two pages, and that is the design.** Each chapter gets three
lines — Face name, clause, subtitle — rather than the joined
`The Shaman: What to Do With What You Feel` that `build_book.py --toc` prints.
Same content; the plain-text list has one line per entry to work with and a page
does not. Squeezed onto one page it wrapped mid-phrase on six of the nine, which
is what a cramped contents actually looks like.

**The EPUB drops the half title and the generated contents.** A half title is a
leaf protecting the title page and an ebook has no leaves; the contents is a print
component, and a reader already has a nav document plus pandoc's TOC. Both are
still in the PDF.

**The EPUB identifier is derived, not random.** Pandoc mints a fresh UUID per
build, which makes every rebuild a different book to a library. No ISBN is
assigned — that is a decision on record in `MANIFEST.md`, not an oversight.

## Closed 2026-08-01

The pipeline's first three rulings, all landed.

- **The heading form** — settled on master, not here. The pipeline's job was to
  stop guessing: nine hand-written display titles deleted, the form read instead,
  and `build_book.py`'s `toc_title` reused so the two contents pages agree.
  **Worth knowing before you read the July branches:**
  `claude/book-print-readiness-august-ar95mo` commit `6026b06` normalised the same
  headings by *deleting* Chapter 2's clause. This pipeline cherry-picked it, and
  had to back it out hours later — master had ruled the opposite way and given the
  other eight chapters a clause of their own. A branch that answers a question is
  not the branch that answered it last.
- **`五行`.** Two glyphs committed, 2.8KB, in `fonts/`.
- **Chapter 8's five alchemy moves.** Two trailing spaces each, matching the hard
  break Chapter 2's moves and Chapter 4's steps already used. Whitespace only. The
  check had reported thirteen sites; the other eight were already correct, and that
  was the check's defect rather than the manuscript's.

## Open, and waiting on Wendell

Run `python3 instruments/typeset.py --flags` for the live list.

- **No cover.** `front_matter/cover.jpg` or `.png` is picked up automatically when
  it exists.
- **Two GAP components**, from `build_book.py`: the Kickstarter backer list, which
  waits on the export, and the enrollment page, which waits on R1. Both build; both
  are named loudly every run.
