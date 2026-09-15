# -*- coding: utf-8 -*-
"""One chapter, set for marking up on paper or a tablet.

    python3 instruments/build_markup.py 4        # build/MTGOA_ch4_<date>_markup.pdf
    python3 instruments/build_markup.py 4 --keep-src

## Why this exists

Wendell, 2026-09-15: *"it will be easier if you just build the chapter we're working on at a
time for me to mark up."*

Marking the whole book to check one chapter means finding ch4 inside 387 pages, and every
rebuild moves the page numbers under the marks already made. A chapter on its own starts at
page 1 and stays there.

## What it reuses rather than reimplements

Everything, the same way `build_sample.py` does. `typeset.py` normalises the source and
`build_pdf.py` converts and compiles, so this file cannot set from a different source than the
book does. **The chapter is selected by filtering `build_book.SPINE`**, so a chapter renamed
in the spine is renamed here.

**Patch `ts.bb.SPINE`, never an imported `build_book`.** `typeset.py` loads its own private
copy through importlib, so a module imported here is a different object and patching it does
nothing — it silently sets the whole book instead. `build_sample.py` shipped that bug once and
its docstring records it. The component count below is the check that catches it.

## Trim

`workbook` — 7.5 x 9.25in, 12/17 type, **1.35in outside margin**. `book/README.md` calls that
margin "a working rail rather than white space", which is exactly what a markup proof wants.
The trade 6x9 gives 0.70in and leaves nowhere to write.

## What this is not

Not a deliverable. It carries no cover, no front matter, no back matter, and its page numbers
do not correspond to the book's. It exists to be written on.
"""
import io, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BUILD = os.path.join(ROOT, "build")
sys.path.insert(0, HERE)

TRIM = "workbook"


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("-")]
    if len(argv) != 1 or not argv[0].isdigit():
        sys.stderr.write("usage: build_markup.py N        (N = chapter number 1-9)\n")
        return 2
    label = "Chapter %s" % argv[0]

    try:
        import typst
    except ImportError as e:
        sys.stderr.write("missing dependency: %s\n" % e)
        return 1

    import typeset as ts
    import build_pdf as bp

    keep = [row for row in ts.bb.SPINE if row[1] == label]
    if len(keep) != 1:
        sys.stderr.write("expected exactly one %r row in build_book.SPINE, found %d\n"
                         % (label, len(keep)))
        return 1
    rel = keep[0][2]

    original, ts.bb.SPINE = ts.bb.SPINE, keep
    try:
        comps, tally, flags = ts.components()
        md = ts.to_markdown(comps)
    finally:
        ts.bb.SPINE = original

    # The check build_sample.py had to add after setting the whole book and reporting OK.
    if len(comps) != 1:
        sys.stderr.write("spine filter failed: %d components set, expected 1\n" % len(comps))
        return 1

    blockers = [f for f in flags if f[0] == "BLOCKER"]
    for lvl, lab, msg in blockers:
        sys.stderr.write("BLOCKER %s: %s\n" % (lab, msg))
    if blockers:
        return 1

    if not os.path.isdir(BUILD):
        os.makedirs(BUILD)
    stamp = datetime.date.today().isoformat()
    slug = os.path.splitext(os.path.basename(rel))[0]
    src = os.path.join(BUILD, "MTGOA_%s_MARKUP_SRC_%s.md" % (slug, stamp))
    typ = os.path.join(BUILD, "MTGOA_%s_%s_markup.typ" % (slug, stamp))
    dest = os.path.join(BUILD, "MTGOA_%s_%s_markup.pdf" % (slug, stamp))
    io.open(src, "w", encoding="utf-8").write(md)

    if not bp.to_typst(src, typ, TRIM):
        return 1

    compiler = typst.Compiler(typ, root=ROOT, font_paths=[bp.FONTS],
                              ignore_system_fonts=True)
    try:
        _, warnings = compiler.compile_with_warnings(output=dest)
    except Exception as exc:
        sys.stderr.write("\nCOMPILE FAILED\n%s\n" % exc)
        return 1
    for w in warnings or []:
        sys.stderr.write("typst warning: %s\n" % w)

    for f in (src, typ):
        if os.path.exists(f) and "--keep-src" not in sys.argv:
            os.remove(f)

    words = len(io.open(os.path.join(ROOT, rel), encoding="utf-8").read().split())
    try:
        import pymupdf
        pages = pymupdf.open(dest).page_count
    except Exception:
        pages = "?"
    print("markup proof — %s" % os.path.relpath(dest, ROOT))
    print("  %s, %s, %s words, %s pages, %s trim, 1.35in outside margin"
          % (label, rel, words, pages, TRIM))
    return 0


if __name__ == "__main__":
    sys.exit(main())
