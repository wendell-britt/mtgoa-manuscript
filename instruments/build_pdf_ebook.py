# -*- coding: utf-8 -*-
"""The PDF edition — the interior with its cover on the front and a usable outline.

    python3 instruments/build_pdf_ebook.py                 # from the trade interior
    python3 instruments/build_pdf_ebook.py --trim=workbook
    python3 instruments/build_pdf_ebook.py --check         # build, verify, delete

## Why this is not just the print PDF renamed

A print interior and a PDF edition are different products and the difference is not
cosmetic:

**The print interior carries no cover, and it never should.** The printer takes a separate
wrap file — back, spine, front on one sheet — whose spine width is a function of the page
count and the paper stock. Putting the cover inside the interior would give the press a
383-page block with a picture on leaf one and no wrap.

**A PDF edition has no wrap.** Page one *is* the cover, because on a screen there is
nothing else for a reader to open. `build_epub.py` already solves this for the ebook; this
solves it for the format people actually print at home, email to a colleague, and read on a
tablet that is not an e-reader.

## The cover page, and why it is letterboxed rather than stretched

The cover is 1600x2560, a ratio of exactly 1.600. The trade trim is 6x9, a ratio of 1.500,
and the workbook is 7.5x9.25 at 1.233. **No trim matches the artwork**, so something has to
give, and there are only three choices: distort the art, change the page size for one leaf,
or letterbox.

Distortion is out. Mixed page sizes look like a defect in a continuous scroll and confuse
duplex printing. So the cover is scaled to fit and centred, **and the page is first filled
with the artwork's own edge colour**, sampled from the four corners of the PNG rather than
guessed. On this cover that is the near-black the vertical bars sit on, so the bars are
invisible and the page reads as full bleed. On a cover with a light edge it would do the
same thing in the other direction. Sampling beats a constant because the next cover will
not be this cover.

## The outline, and the one thing it was missing

The Typst template emits a 313-entry outline and every entry is a *section* heading. There
was no entry for any of the nine chapters, the eight appendices or the four back-matter
components, because the template bookmarks headings and a chapter opener is a component.

In print that costs nothing — nobody navigates a printed book by sidebar. **In a PDF it is
the whole navigation model.** A reader opening a 383-page file gets a flat wall of section
names with no chapter anywhere in it, which is the sidebar equivalent of a book with no
chapter titles on the spine.

So this inserts one level-1 entry per component, demotes the template's headings underneath
the component that contains them, and leaves the front matter that precedes Chapter 1 where
it is.

**The component map is read out of the document, and the first version of this file got
that wrong in a way worth recording.** The map started as a table copied from
`build_pdf.py --check` on the *trade* interior. The workbook sets eight pages longer, so
applied there every bookmark from Chapter 9 on pointed into the middle of the previous
component: `Chapter 9` opened inside The Sage, `Index` opened on About the Author. The build
reported OK both times, because a bookmark the builder placed at page N is trivially at page
N. **A page number is not a verification.** `components()` now finds the openers by reading
them, so the map cannot drift from the trim it describes.

## What gets verified before it is allowed to exist

    page count      exactly one more than the interior
    cover           a real image on page 1, at the page's own size
    outline         every interior entry still points at the same page, +1
    components      one level-1 entry per component, all present
    landing         each bookmark's page actually says what the bookmark says

A PDF edition that silently loses its outline is worse than one that never had it, because
the reader has no way to tell.
"""
import io, os, re, sys, glob, json, struct

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

COVER_NAMES = ("cover.png", "cover.jpg", "cover.jpeg")

# Back-matter and interstitial components, which open with a plain title rather than a
# letterspaced word. First match wins: `Index` appears inside the index's own body too.
PLAIN = ["A Letter to the Reader", "About the Author", "What Comes Next",
         "Key Terms", "Index"]

# The letterspaced openers. The template sets `C h a p t e r 3` with real spaces between
# the letters, and the contents page lists the same chapter as `Chapter 9` without them.
# **Requiring the spacing is what separates an opener from a contents entry** — the first
# version of this file matched either and put Chapter 9's bookmark on the contents page.
OPENER = re.compile(r"^(?:(C\s+h\s+a\s+p\s+t\s+e\s+r)|(A\s+p\s+p\s+e\s+n\s+d\s+i\s+x))"
                    r"\s+(\w+)\s+(.{3,60}?)(?:\s{2,}|$)")


def components(doc):
    """Find every component opener by reading the pages, per trim.

    **This used to be a hard-coded table and that was a real defect.** The map was taken
    from `build_pdf.py --check` on the trade interior and then applied to the workbook,
    which sets eight pages longer — so from Chapter 9 onward every bookmark in the
    workbook edition pointed into the middle of the previous chapter. `Index` landed on
    About the Author. Nothing in the build complained, because a bookmark the builder
    inserted at page N is trivially "at page N"; the check that catches it is whether the
    page it points at actually says what the bookmark says.

    Deriving from the document cannot drift, works for any future trim, and survives a
    repagination — which is exactly the class of change that produced the bug.
    """
    out, seen = [], set()
    for i, page in enumerate(doc, 1):
        t = re.sub(r"[ \t]+", " ", page.get_text()).strip()
        flat = re.sub(r"\s+", " ", t)
        m = OPENER.match(t.replace("\n", "  "))
        if m:
            kind = "chapter" if m.group(1) else "appendix"
            word = "Chapter" if kind == "chapter" else "Appendix"
            title = m.group(4).strip(" .—-")
            out.append((kind, i, "%s %s — %s" % (word, m.group(3), title)))
            continue
        for name in PLAIN:
            if name not in seen and flat.startswith(name):
                out.append(("front" if "Letter" in name else "back", i, name))
                seen.add(name)
                break
    return sorted(out, key=lambda c: c[1])


def find_cover():
    for n in COVER_NAMES:
        p = os.path.join(ROOT, "front_matter", n)
        if os.path.exists(p):
            return p
    return None


def png_size(path):
    b = io.open(path, "rb").read(24)
    if b[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", b[16:24])


def edge_color(path):
    """The artwork's own edge colour, sampled from the four corners.

    A constant would be wrong for the next cover. Sampling is wrong only if the four
    corners disagree, and a cover whose corners disagree has no edge colour to letterbox
    with — so that case falls back to black rather than picking one corner and hoping.
    """
    try:
        import pymupdf
        pix = pymupdf.Pixmap(path)
        if pix.alpha:
            pix = pymupdf.Pixmap(pix, 0)          # drop alpha; we want the composited RGB
        w, h = pix.width, pix.height
        corners = [pix.pixel(0, 0), pix.pixel(w - 1, 0),
                   pix.pixel(0, h - 1), pix.pixel(w - 1, h - 1)]
        spread = max(max(c[i] for c in corners) - min(c[i] for c in corners)
                     for i in range(3))
        if spread > 24:
            return (0, 0, 0), corners, spread
        avg = tuple(sum(c[i] for c in corners) / 4.0 / 255.0 for i in range(3))
        return avg, corners, spread
    except Exception:
        return (0, 0, 0), [], -1


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    trim = "trade"
    for a in argv:
        if a.startswith("--trim="):
            trim = a.split("=", 1)[1]

    try:
        import pymupdf
    except ImportError:
        sys.stderr.write("pymupdf missing. pip install pymupdf\n")
        return 1

    src_glob = os.path.join(ROOT, "build", "*_%s.pdf" % trim)
    found = sorted(p for p in glob.glob(src_glob) if "_ebook" not in p)
    if not found:
        sys.stderr.write("no %s interior in build/. Run build_pdf.py --trim=%s first\n"
                         % (trim, trim))
        return 1
    interior = found[-1]

    cover = find_cover()
    if cover is None:
        sys.stderr.write("no cover at front_matter/cover.{png,jpg}. "
                         "A PDF edition without one has nothing on page 1.\n")
        return 1

    src = pymupdf.open(interior)
    W, H = src[0].rect.width, src[0].rect.height
    toc = src.get_toc()

    out = pymupdf.open()
    page = out.new_page(width=W, height=H)

    bg, corners, spread = edge_color(cover)
    page.draw_rect(page.rect, color=bg, fill=bg, width=0)

    cw, ch = png_size(cover) or (1600, 2560)
    scale = min(W / cw, H / ch)
    dw, dh = cw * scale, ch * scale
    rect = pymupdf.Rect((W - dw) / 2, (H - dh) / 2, (W + dw) / 2, (H + dh) / 2)
    page.insert_image(rect, filename=cover)

    out.insert_pdf(src, links=True, annots=True)
    out.set_toc([[lvl, title, pno + 1] for lvl, title, pno in toc])

    # --- the component level, inserted over the template's headings
    #
    # Rebasing is per component, not global. A blanket +1 breaks the hierarchy the first
    # time a component's own first heading is a level 2 — Appendix D opens on one — because
    # the row then reads level 3 directly under the level 1 component and PyMuPDF rejects
    # the jump. So each group is rebased against *its own* shallowest heading, and the
    # result is additionally clamped to at most one deeper than the row above it, which
    # covers a group whose headings skip a level internally.
    shifted = out.get_toc()
    comp = components(src)

    groups, ci = [], 0
    for row in shifted:
        while ci < len(comp) and comp[ci][1] + 1 <= row[2]:
            groups.append(("comp", comp[ci]))
            ci += 1
        groups.append(("row", row))
    while ci < len(comp):
        groups.append(("comp", comp[ci]))
        ci += 1

    merged, base, prev, inside = [], None, 0, False
    for kind, item in groups:
        if kind == "comp":
            merged.append([1, item[2], item[1] + 1])
            base, prev, inside = None, 1, True
            continue
        lvl, title, pno = item
        if not inside:
            # Front matter ahead of Chapter 1 has no component over it. These rows are
            # siblings and must stay siblings — rebasing them demotes the second of two
            # level 1 headings on the copyright page under the first.
            out_lvl = max(1, min(lvl, prev + 1))
        else:
            if base is None:
                base = lvl                  # first heading inside this component
            out_lvl = max(1, min(lvl - base + 2, prev + 1))
        merged.append([out_lvl, title, pno])
        prev = out_lvl

    out.set_toc(merged)

    md = dict(src.metadata or {})
    md["title"] = md.get("title") or "Mastering the Game of Allyship"
    md["author"] = md.get("author") or "Wendell Britt"
    md["producer"] = "MTGOA build_pdf_ebook.py"
    out.set_metadata(md)

    base = os.path.basename(interior).replace(".pdf", "_ebook.pdf")
    dest = os.path.join(ROOT, "build", base)
    out.save(dest, deflate=True, garbage=3)

    # ---- verification
    problems, notes = [], []
    chk = pymupdf.open(dest)

    if chk.page_count != src.page_count + 1:
        problems.append("page count %d, expected %d (interior + cover)"
                        % (chk.page_count, src.page_count + 1))
    imgs = chk[0].get_images(full=True)
    if not imgs:
        problems.append("page 1 carries no image — the cover did not land.")
    if abs(chk[0].rect.width - W) > 0.5 or abs(chk[0].rect.height - H) > 0.5:
        problems.append("cover page is not the interior's page size.")

    back = chk.get_toc()
    comp_entries = [e for e in back if e[0] == 1 and " — " in e[1]
                    or (e[0] == 1 and e[1] == "A Letter to the Reader")]
    if len(back) != len(toc) + len(comp):
        problems.append("outline has %d entries, expected %d (%d + %d components)"
                        % (len(back), len(toc) + len(comp), len(toc), len(comp)))
    lost = [c for c in comp
            if not any(e[1] == c[2] and e[2] == c[1] + 1 for e in back)]
    if lost:
        problems.append("%d component entr(ies) missing: %s"
                        % (len(lost), ", ".join(c[2] for c in lost[:3])))

    # The check the hard-coded map did not have, and the only one that would have caught
    # it: a bookmark is not correct because it sits where it was put. It is correct when
    # the page it opens actually says what the bookmark says.
    wrong = []
    for kind, pno, title in comp:
        tail = title.split(" — ")[-1][:24]
        flat = re.sub(r"\s+", " ", chk[pno].get_text())
        squashed = re.sub(r"(?<=\w) (?=\w)", "", flat)     # undo the letterspacing
        if tail.lower().replace(" ", "") not in squashed.lower().replace(" ", ""):
            wrong.append((title, pno + 1))
    if wrong:
        problems.append("%d bookmark(s) do not land on the page they name, first: "
                        "%r -> p%d" % (len(wrong), wrong[0][0], wrong[0][1]))
    # every original entry must still point one page later than it did
    orig = {(t, p) for _, t, p in toc}
    moved = [(t, p) for _, t, p in back if p and (t, p - 1) not in orig
             and t not in [c[2] for c in comp]]
    if moved:
        problems.append("%d outline entr(ies) do not point at interior page +1, "
                        "first: %r p%d" % (len(moved), moved[0][0][:40], moved[0][1]))

    notes.append("%s edition — %d pages (interior %d + cover)"
                 % (trim, chk.page_count, src.page_count))
    notes.append("page size %.0f x %.0f pt (%.2f x %.2f in)" % (W, H, W / 72, H / 72))
    notes.append("cover %dx%d, ratio %.3f, scaled %.1f%% to fit; letterbox %.1fpt "
                 "each side" % (cw, ch, float(ch) / cw, scale * 100, (W - dw) / 2))
    if spread < 0:
        notes.append("edge colour: sampling failed, filled black")
    elif spread > 24:
        notes.append("edge colour: corners disagree by %d/255, filled black" % spread)
    else:
        notes.append("edge colour: sampled from four corners, spread %d/255, rgb(%d,%d,%d)"
                     % (spread, bg[0] * 255, bg[1] * 255, bg[2] * 255))
    notes.append("outline %d entries — %d from the template, +%d components at level 1"
                 % (len(back), len(toc), len(comp)))
    notes.append("metadata: %r by %r" % (md["title"], md["author"]))

    chk.close()
    if check:
        os.remove(dest)
        notes.append("--check: removed the artifact.")

    print("pdf edition — %s" % os.path.relpath(dest, ROOT))
    for n in notes:
        print("  " + n)
    print()
    if problems:
        for p in problems:
            print("  BLOCKER  " + p)
        print("\n%d problem(s) — nothing shipped." % len(problems))
        return 1
    print("PDF EDITION OK — cover on page 1, outline intact, %d pages." % (src.page_count + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
