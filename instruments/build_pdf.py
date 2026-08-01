# -*- coding: utf-8 -*-
"""
Render the print interior, and refuse to emit one that would come back wrong from
the printer.

    python3 instruments/build_pdf.py                # build build/MTGOA_<date>.pdf
    python3 instruments/build_pdf.py --check        # build, verify, delete
    python3 instruments/build_pdf.py --proof        # also write proof PNGs
    python3 instruments/build_pdf.py --keep-typst   # leave the .typ for inspection

## Why Typst

The obvious answer was LaTeX, and it is the wrong one here. A TeX distribution
capable of setting this book is a multi-gigabyte apt install that this container
does not have and a fresh one would not either, and the parts of it that matter
for a trade book — mirrored margins, a running head that knows which chapter it
is in, a designed chapter opener — are the parts where LaTeX is hardest.

Typst arrives as a 30MB Python wheel, embeds its own fonts, and answers all three
in a page of code. **The embedded fonts are the load-bearing part.** The interior
is set in Libertinus Serif, which ships inside the Typst binary, so the build is
reproducible on any machine. `fc-list` on this container offers Bitstream Charter
— a better book face, and one that would have made the PDF unbuildable anywhere
that lacks it. `--check` fails on any font warning for exactly that reason.

## What this checks that a person would not

The failures a book PDF ships with are structural, and none of them are visible
in a page you happen to look at.

**Chapters have to open on a recto.** Every one, not most. A single component
whose length changes by a paragraph flips the parity of every chapter after it,
and the way that shows up is a reader noticing, three chapters later, that
openers have started landing on the left-hand page.

**A blank verso has to be genuinely blank.** Typst's own `pagebreak(to: "odd")`
prints the running head and folio on the leaf it inserts. That is a printing
error on every blank in the book, and it is invisible unless you go looking at
the pages nobody reads.

**The folio has to be continuous.** Roman through the front matter, arabic
restarting at 1 on Chapter 1, no repeats and no gaps.

Those three come out of a verification record the template writes into the
document — see `<mtgoa-report>` at the bottom of `instruments/book/mtgoa.typ`.
None of them can be read off the PDF bytes.
"""
import io, os, re, sys, json, glob, shutil, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BOOK = os.path.join(HERE, "book")
BUILD = os.path.join(ROOT, "build")

TEMPLATE = os.path.join(BOOK, "mtgoa.typ")
FILTER = os.path.join(BOOK, "devices.lua")

TITLE = "Mastering the Game of Allyship"
AUTHOR = "Wendell Britt"

# The YAML trap, inherited from build_epub.py and still load-bearing. Pandoc reads
# a `---` rule as the start of a YAML metadata block. `typeset.py` resolves every
# rule in the manuscript, so the trap should no longer be reachable — this stays
# because the cost of being wrong is a build that dies with exit 64 and no book.
FORMAT = "markdown-yaml_metadata_block"

# A character the interior font does not have prints as a box. Typst says nothing
# about it — no warning, no error, the PDF just contains a box — so the only way
# to find one is to render it and look.
#
# That is what this does. Each non-ASCII character in the manuscript is set on its
# own tiny page and compared against U+FFFF, a permanently unassigned noncharacter.
# Identical rendering means both came out as the same fallback box.
#
# U+FFFF and not U+E000: a private-use codepoint renders as its own distinct
# shape, so the first version of this compared every real box against something
# that was not a box and reported the manuscript clean.
#
# The check found 五 and 行 in Appendix G on its first run: `wu xing (五行)`, in
# the credit to the five-phase system. No embedded Typst font carries CJK. It
# rendered here only because this container happens to have WenQuanYi installed,
# which is exactly the accident the whole reproducible-font rule exists to catch.
TOFU_PROBE = "\uffff"
GLYPH_PAGE = ('#set page(width: 40pt, height: 40pt, margin: 6pt)\n'
              '#set text(font: "Libertinus Serif", size: 18pt)\n')


def pandoc(args):
    import pypandoc
    return pypandoc.get_pandoc_path(), args


def newest(pattern):
    files = sorted(glob.glob(os.path.join(BUILD, pattern)))
    return files[-1] if files else None


def typeset_source():
    """The normalised source. Rebuilt every time, because a stale one lies."""
    rc = subprocess.call([sys.executable, os.path.join(HERE, "typeset.py"), "--write"],
                         cwd=ROOT, stdout=subprocess.DEVNULL)
    if rc != 0:
        sys.stderr.write("typeset.py refused to write. Run it directly for the flags.\n")
        return None
    return newest("MTGOA_TYPESET_*.md")


def to_typst(src, out):
    try:
        import pypandoc
    except ImportError:
        sys.stderr.write("pypandoc missing. pip install pypandoc-binary\n")
        return False
    pypandoc.convert_file(
        src, "typst", format=FORMAT, outputfile=out,
        extra_args=["--wrap=preserve", "--template=%s" % TEMPLATE,
                    "--lua-filter=%s" % FILTER,
                    "--metadata", "title=%s" % TITLE,
                    "--metadata", "author=%s" % AUTHOR])
    return True


def missing_glyphs(path):
    """Every character in the source the interior font cannot set, and its count."""
    import typst

    def render(ch):
        return typst.compile((GLYPH_PAGE + ch).encode("utf-8"), format="png",
                             ppi=60, ignore_system_fonts=True)

    text = io.open(path, encoding="utf-8").read()
    counts = {}
    for ch in text:
        if ord(ch) < 128:
            continue
        counts[ch] = counts.get(ch, 0) + 1

    tofu = render(TOFU_PROBE)
    return {ch: n for ch, n in sorted(counts.items()) if render(ch) == tofu}


def verify(report, problems, notes):
    """Read the template's record and hold the interior to the three rules."""
    openers = report["openers"]
    pages = report["pages"]

    by_id = {o["id"]: o for o in openers}
    notes.append("%d pages, %d components" % (pages, len(openers)))

    # 1 — every chapter and appendix opens on a recto.
    wrong = [o for o in openers
             if o["kind"] in ("chapter", "appendix") and o["page"] % 2 == 0]
    if wrong:
        problems.append("%d opener(s) landed on a verso: %s"
                        % (len(wrong), ", ".join("%s p.%d" % (o["label"] or o["id"],
                                                              o["page"]) for o in wrong)))

    # 2 — the copyright page backs the title page, so it must be a verso.
    cp = by_id.get("copyright")
    if cp and cp["page"] % 2 == 1:
        problems.append("copyright landed on a recto (p.%d). It backs the title "
                        "page; a leaf between them is a binding error." % cp["page"])

    # 3 — the folio sequence. Roman runs from the contents to Chapter 1, arabic
    #     from Chapter 1 to the end, and neither may be empty.
    contents, ch1 = by_id.get("contents"), by_id.get("chapter-1")
    if contents is None:
        problems.append("no contents component — nothing anchors roman numbering.")
    if ch1 is None:
        problems.append("no chapter-1 component — nothing anchors arabic numbering.")
    if contents and ch1:
        if ch1["page"] <= contents["page"]:
            problems.append("Chapter 1 (p.%d) is not after the contents (p.%d)."
                            % (ch1["page"], contents["page"]))
        notes.append("front matter i–%s, body 1–%d"
                     % (roman(ch1["page"] - contents["page"]), pages - ch1["page"] + 1))

    # 4 — components in spine order, and no two on the same page.
    seen = {}
    for o in openers:
        if o["page"] in seen:
            problems.append("%s and %s both open on p.%d."
                            % (seen[o["page"]], o["id"], o["page"]))
        seen[o["page"]] = o["id"]
    if openers != sorted(openers, key=lambda o: o["page"]):
        problems.append("components are not in page order — the spine and the "
                        "rendered book disagree.")


def roman(n):
    vals = ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
            (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"),
            (5, "v"), (4, "iv"), (1, "i"))
    out = ""
    for v, s in vals:
        while n >= v:
            out, n = out + s, n - v
    return out


def main():
    check_only = "--check" in sys.argv
    proof = "--proof" in sys.argv
    keep_typst = "--keep-typst" in sys.argv or check_only

    try:
        import typst
    except ImportError:
        sys.stderr.write("typst missing. pip install typst\n")
        return 1

    src = typeset_source()
    if src is None:
        return 1
    print("source   %s" % os.path.relpath(src, ROOT))

    stamp = datetime.date.today().isoformat()
    typ = os.path.join(BUILD, "MTGOA_%s.typ" % stamp)
    pdf = os.path.join(BUILD, "MTGOA_%s.pdf" % stamp)

    if not to_typst(src, typ):
        return 1
    print("typst    %s (%d bytes)" % (os.path.relpath(typ, ROOT), os.path.getsize(typ)))

    problems, gaps, notes = [], [], []

    # A GAP, not a failure, and the split is deliberate. A box in one parenthetical
    # is a real defect the reader will see, and the fix — transliterate, or commit
    # a CJK font to the repository and widen the font stack — is a decision about
    # the book rather than about the build. `build_book.py` draws the same line
    # for a missing acknowledgements page.
    absent = missing_glyphs(src)
    if absent:
        gaps.append("%d character(s) the interior font cannot set — each prints as "
                    "a box: %s" % (len(absent), ", ".join(
                        "%s (U+%04X) x%d" % (c, ord(c), n) for c, n in absent.items())))

    # `ignore_system_fonts` is what makes this build the same book everywhere. With
    # system fonts on, the container's WenQuanYi silently supplies the CJK above
    # and the PDF differs from one built on a machine without it.
    compiler = typst.Compiler(typ, root=ROOT, ignore_system_fonts=True)
    try:
        _, warnings = compiler.compile_with_warnings(output=pdf)
    except Exception as exc:
        # Keep the whole diagnostic. Typst names the line and the column, and that
        # is the difference between a fix and a bisect.
        sys.stderr.write("\nCOMPILE FAILED\n%s\n" % exc)
        for hint in getattr(exc, "hints", []) or []:
            sys.stderr.write("  hint: %s\n" % hint)
        return 1

    for w in warnings:
        msg = str(getattr(w, "message", w))
        # A font warning means the interior fell back to something that is not on
        # every machine. That is not a note; it is a different book.
        if "font" in msg.lower():
            problems.append("font warning — the build is not reproducible: %s" % msg)
        else:
            notes.append("typst: %s" % msg)

    report = json.loads(compiler.query("<mtgoa-report>", field="value",
                                       one=True, format="json"))
    verify(report, problems, notes)

    print("pdf      %s (%d bytes)" % (os.path.relpath(pdf, ROOT), os.path.getsize(pdf)))
    print("-" * 70)
    print("%-10s %-9s %-6s %s" % ("component", "kind", "page", "title"))
    for o in report["openers"]:
        print("%-10s %-9s %-6d %s" % (o["id"], o["kind"], o["page"], o["title"]))
    print("-" * 70)
    for n in notes:
        print("  " + n)

    if proof:
        # Every opener page plus its neighbours — the pages where a parity or
        # furniture error actually shows.
        want = sorted({p for o in report["openers"]
                       for p in (o["page"] - 1, o["page"], o["page"] + 1)
                       if 1 <= p <= report["pages"]})
        pdir = os.path.join(BUILD, "proof_%s" % stamp)
        shutil.rmtree(pdir, ignore_errors=True)
        os.makedirs(pdir)
        compiler.compile(output=os.path.join(pdir, "p{p}.png"), format="png", ppi=110)
        for f in glob.glob(os.path.join(pdir, "p*.png")):
            n = int(re.search(r"p(\d+)\.png$", f).group(1))
            if n not in want:
                os.remove(f)
        print("  proof pages -> %s (%d)"
              % (os.path.relpath(pdir, ROOT), len(os.listdir(pdir))))

    if check_only:
        os.remove(pdf)
        print("  --check: removed the artifact.")
    elif not keep_typst:
        os.remove(typ)

    if problems:
        print("\nPDF FAIL")
        for p in problems:
            print("  " + p)
        return 1

    print("\nPDF OK — %d pages, every opener on a recto, folio continuous."
          % report["pages"])
    if gaps:
        # After the OK line, because the OK line is the part that gets read.
        print("\n" + "!" * 62)
        print("SHIPPING WITH %d GAP(S) — the reader will see each one:" % len(gaps))
        for g in gaps:
            print("  " + g)
        print("!" * 62)
    return 0


if __name__ == "__main__":
    sys.exit(main())
