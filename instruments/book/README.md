# The production pipeline — PDF and EPUB

Two deliverables out of one manuscript. Nothing here edits `manuscript/`.

```bash
pip install pypandoc-binary typst      # or: pip install -r instruments/requirements.txt

python3 marginalia/compile.py --apply  # the frame is part of both editions
python3 instruments/build_book.py      # is the book complete?
python3 instruments/typeset.py         # can it be set? — the transforms and the flags
python3 instruments/build_pdf.py       # -> build/MTGOA_<date>.pdf   (6x9 interior)
python3 instruments/build_epub.py      # -> build/MTGOA_<date>.epub
```

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

**Four chapter heading styles.** `SPEC_PRINT_READINESS_2026-07-29.md` §6 has
carried this open since July. `typeset.py` normalises for display only, pinned to
`RAW_HEADING` so a chapter renamed upstream fails the build instead of quietly
printing under its old name.

**251 horizontal rules doing two jobs.** 188 sit before a heading, which already
supplies the break. 2 open a component body with nothing above them to separate —
the residue of the provenance headers `build_book.py` strips. 61 are real scene
breaks and become a centred ornament.

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
  against U+FFFF found `五行` in Appendix G, which sets here only because this
  container happens to carry a CJK font.
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

**The EPUB drops the half title and the generated contents.** A half title is a
leaf protecting the title page and an ebook has no leaves; the contents is a print
component, and a reader already has a nav document plus pandoc's TOC. Both are
still in the PDF.

**The EPUB identifier is derived, not random.** Pandoc mints a fresh UUID per
build, which makes every rebuild a different book to a library. No ISBN is
assigned — that is a decision on record in `MANIFEST.md`, not an oversight.

## Open, and waiting on Wendell

Run `python3 instruments/typeset.py --flags` for the live list.

- **`五行` in Appendix G** prints as two boxes. Transliterate, or commit a CJK font
  and widen the stack.
- **Thirteen joined lines** in ch2, ch4, and ch8, where two authored lines are set
  as one because markdown folds a single newline into a space. Obsidian renders
  the break, so the vault does not show what prints. Chapter 8's five are the ones
  that read wrong. Four of them were being set as *tables* before this pipeline
  existed — a `---` above a pair of lines is a valid multiline-table rule.
- **Chapter 2's heading tail**, `— Why Allyship Keeps Failing (and Where to
  Start)`, dropped for display because ch2 is the only chapter carrying both that
  and an italic subtitle.
- **No cover.** `front_matter/cover.jpg` or `.png` is picked up automatically when
  it exists.
- **Two GAP components**, from `build_book.py`: the Kickstarter backer list and the
  enrollment page.
