# -*- coding: utf-8 -*-
"""The free sample — Chapter 1, set from the shipping manuscript, with the cover on it.

    python3 instruments/build_sample.py                 # build/MTGOA_<date>_sample.pdf
    python3 instruments/build_sample.py --no-cover      # the old shape, chapter first
    python3 instruments/build_sample.py --check         # build, verify, delete

## Why this exists

The sample sitting on `masteringallyship.com` was generated 2026-07-13 and the chapter has
moved a long way since. Measured against the shipping `manuscript/ch1.md` on 2026-08-10:

    sample 7,245 words · current 9,130 words · 67.7% similar

Whole passages in it are gone from the book, its PDF metadata still says *"Chapter 0"*, and
its closing page ends on a live `[ URL / QR ]` placeholder — the exact artifact class the
final proof spent three rounds removing from the book itself. **It is the first thing a new
reader downloads, and it is a third of a draft out of date.**

## The one design decision, and why it needed no copy

The old sample appended a hand-written *PLAYING ALONG* block after the chapter, and that
block is where the placeholder lived. It is not needed any more: `ch1.md` now ends with its
own *Playing along* line pointing at **masteringallyship.com**, authored, reviewed, and
carrying no placeholder.

**So the sample is the chapter and nothing else.** No marketing copy is written here, which
means there is no second copy of it to drift. If the funnel later wants a different closing
page, it belongs in the manuscript where the review pass can see it, not in this file.

## What it reuses rather than reimplements

Everything. `typeset.py` normalises the source, `build_pdf.py` converts and compiles, and
the cover is placed by the same letterbox-into-the-artwork's-own-edge-colour routine as
`build_pdf_ebook.py`. **The single chapter is selected by filtering `build_book.SPINE`**,
so the sample cannot set from a different file than the book does, and a chapter renamed in
the spine is a chapter renamed here.

Trim is `workbook-9` — 7.5x9.00in — which is what the old sample was set at and is already
a preset in `mtgoa.typ`. A sample is read on a screen, so it takes the wider measure.
"""
import io, os, re, sys, glob, shutil, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BUILD = os.path.join(ROOT, "build")
sys.path.insert(0, HERE)

TRIM = "workbook-9"
CHAPTER = "Chapter 1"


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    want_cover = "--no-cover" not in argv

    try:
        import typst, pymupdf
    except ImportError as e:
        sys.stderr.write("missing dependency: %s\n" % e)
        return 1

    import typeset as ts
    import build_pdf as bp
    from build_pdf_ebook import (find_cover, png_size, edge_color,
                                 components as ebook_components)

    # --- select the one component, from the spine the book itself uses
    #
    # Patch `ts.bb`, NOT an imported `build_book`. typeset.py loads its own private
    # copy through importlib so the spine has exactly one definition, which means a
    # module imported here is a DIFFERENT object and patching it does nothing. The
    # first version of this file did that, silently set the entire 400-page book,
    # and reported SAMPLE OK -- because every check it ran passes on the whole book
    # too. Hence the component check below.
    keep = [row for row in ts.bb.SPINE if row[1] == CHAPTER]
    if len(keep) != 1:
        sys.stderr.write("expected exactly one %r row in build_book.SPINE, found %d\n"
                         % (CHAPTER, len(keep)))
        return 1
    original, ts.bb.SPINE = ts.bb.SPINE, keep
    try:
        comps, tally, flags = ts.components()
        md = ts.to_markdown(comps)
    finally:
        ts.bb.SPINE = original

    blockers = [f for f in flags if f[0] == "BLOCKER"]
    if blockers:
        for lvl, label, msg in blockers:
            sys.stderr.write("BLOCKER %s: %s\n" % (label, msg))
        return 1

    if not os.path.isdir(BUILD):
        os.makedirs(BUILD)
    stamp = datetime.date.today().isoformat()
    src = os.path.join(BUILD, "MTGOA_SAMPLE_SRC_%s.md" % stamp)
    typ = os.path.join(BUILD, "MTGOA_%s_sample.typ" % stamp)
    dest = os.path.join(BUILD, "MTGOA_%s_sample.pdf" % stamp)
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

    problems, notes = [], []
    for w in warnings:
        msg = str(getattr(w, "message", w))
        if "font" in msg.lower():
            problems.append("font warning — not reproducible: %s" % msg)

    body_pages = pymupdf.open(dest).page_count

    # --- the cover, by the same rule as the PDF editions
    if want_cover:
        cover = find_cover()
        if cover is None:
            problems.append("no cover at front_matter/cover.{png,jpg}")
        else:
            interior = pymupdf.open(dest)
            W, H = interior[0].rect.width, interior[0].rect.height
            out = pymupdf.open()
            page = out.new_page(width=W, height=H)
            bg, _, spread = edge_color(cover)
            page.draw_rect(page.rect, color=bg, fill=bg, width=0)
            cw, chh = png_size(cover) or (1600, 2560)
            s = min(W / cw, H / chh)
            dw, dh = cw * s, chh * s
            page.insert_image(pymupdf.Rect((W - dw) / 2, (H - dh) / 2,
                                           (W + dw) / 2, (H + dh) / 2), filename=cover)
            toc = interior.get_toc()
            out.insert_pdf(interior, links=True, annots=True)
            out.set_toc([[l, t, p + 1] for l, t, p in toc])
            out.set_metadata({
                "title": "Mastering the Game of Allyship — Chapter 1",
                "author": bp.AUTHOR,
                "subject": "The Infinite Arcade — the free sample chapter",
                "producer": "MTGOA build_sample.py",
            })
            tmp = dest + ".tmp"
            out.save(tmp, deflate=True, garbage=3)
            interior.close(); out.close()
            shutil.move(tmp, dest)
            notes.append("cover %dx%d, edge rgb(%d,%d,%d), spread %d/255"
                         % (cw, chh, bg[0] * 255, bg[1] * 255, bg[2] * 255, spread))

    # ---- verification
    d = pymupdf.open(dest)
    text = "\n".join(p.get_text() for p in d)
    flat = re.sub(r"\s+", " ", text)

    # The defect the old sample shipped with. A placeholder in a public download is
    # worse than one in a draft, because nobody is going to proof it again.
    tags = re.findall(r"\[[A-Z][A-Z0-9 /&—-]{1,40}\]", text)
    if tags:
        problems.append("%d placeholder tag(s) in the sample: %s"
                        % (len(tags), ", ".join(sorted(set(tags))[:3])))

    # It has to actually be the shipping chapter, not a stale copy sitting in build/.
    cur = io.open(os.path.join(ROOT, "manuscript", "ch1.md"), encoding="utf-8").read()
    for probe in ("This book is three years late.",
                  "Find the hundred-and-twenty-card deck"):
        if probe not in cur:
            problems.append("probe missing from manuscript/ch1.md: %r" % probe[:40])
        elif re.sub(r"\s+", " ", probe) not in flat:
            problems.append("probe missing from the built sample: %r" % probe[:40])

    if want_cover and not d[0].get_images(full=True):
        problems.append("page 1 carries no image — the cover did not land.")

    # The check the first version did not have. A sample is defined by what it
    # LEAVES OUT, so verifying it "contains chapter 1" passes on the whole book and
    # proves nothing.
    #
    # Counting NAMES is not the check either -- the first attempt at this flagged
    # "The Shaman" and "The Challenger", both of which are Faces chapter 1 names in
    # its own prose. The signal is an OPENER, and build_pdf_ebook.components() is
    # already the tested detector for one: the template letterspaces `C h a p t e r`
    # on an opener and sets it plain everywhere else.
    found = ebook_components(d)
    if len(found) != 1 or not found[0][2].startswith("Chapter 1"):
        problems.append("expected exactly one component (Chapter 1), found %d: %s — "
                        "the spine filter did not take"
                        % (len(found), ", ".join(c[2] for c in found[:4]) or "none"))

    ch1_words = len(io.open(os.path.join(ROOT, "manuscript", "ch1.md"),
                            encoding="utf-8").read().split())
    words = len(re.findall(r"[A-Za-z’'-]+", text))
    if words > ch1_words * 1.6:
        problems.append("sample runs %d words against ch1's %d — too long to be one chapter"
                        % (words, ch1_words))
    notes.insert(0, "%s trim · %d pages%s · ~%d words"
                 % (TRIM, d.page_count, " (1 cover + %d)" % body_pages if want_cover else "",
                    words))
    notes.append("metadata: %r" % (d.metadata or {}).get("title"))
    notes.append("outline %d entries" % len(d.get_toc()))
    d.close()

    for f in (src, typ):
        if os.path.exists(f) and "--keep" not in argv:
            os.remove(f)
    if check and os.path.exists(dest):
        os.remove(dest)
        notes.append("--check: removed the artifact.")

    print("sample — %s" % os.path.relpath(dest, ROOT))
    for n in notes:
        print("  " + n)
    print()
    if problems:
        for p in problems:
            print("  BLOCKER  " + p)
        print("\n%d problem(s) — nothing shipped." % len(problems))
        return 1
    print("SAMPLE OK — Chapter 1 from the shipping manuscript, no placeholders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
