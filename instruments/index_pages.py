# -*- coding: utf-8 -*-
"""
index_pages.py -- the print index, with page numbers.

    python3 instruments/index_pages.py            # two-pass build: PDF -> pages -> PDF
    python3 instruments/index_pages.py --dry      # report the page map, write nothing
    python3 instruments/index_pages.py --check    # verify the index in the newest PDF

## Why this exists

`index_build.py` writes the index with locators of chapter and section (`Ch 7 §6`), and its
header says *at print the compositor substitutes pages*. Nothing did. The printed chapters
carry no section numbers (the reader-facing headings lost them on 2026-09-09), so a reader
holding the paperback could find the chapter and not the section. Wendell, 2026-09-24:
*use page numbers.*

## How it works

The index is the last component of the book, so changing its length cannot move any page
before it. That makes a two-pass build sound:

  1. `build_pdf.py` builds the interior with the ordinary section-locator index.
  2. This file reads the PDF text, finds every page a term appears on (the same term list
     and regexes as `index_build.py`, so the two indexes agree on what an entry is), and
     writes `build/index_pages.md`.
  3. `build_pdf.py` runs again with `MTGOA_INDEX_PAGES` pointing at that file. `build_book.read`
     substitutes it for `back_matter/index.md` in this build only. The ebook and every other
     consumer keep the section locators, which are the right address where there is no page.
  4. The finished PDF is read back and every cited page is checked to hold its term.

Page numbers are the printed folios (roman for the front matter, arabic from Chapter 1).
Running heads and folios are clipped out before matching, so a chapter's title in the head
of every page does not make its own name appear on every page.

Where a term is taught (PRIMARY in `index_build.py`) its first page inside that chapter or
section is bold. A term on more than SATURATED_PAGES pages gets its taught page and the
words *and throughout*, the same rule `index_build.py` applies to locators.
"""
import io, os, re, subprocess, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "marginalia"))

import index_build as ib

SATURATED_PAGES = 12
OUT = os.path.join(ROOT, "build", "index_pages.md")
ENV = "MTGOA_INDEX_PAGES"

TABLE_ROW = re.compile(r"^(\S+)\s+(front|chapter|appendix|back|contents)\s+(\d+)\s", re.M)


def _pymupdf():
    try:
        import pymupdf
        return pymupdf
    except ImportError:
        import fitz
        return fitz


def build_pdf(with_index_file=None):
    """Run build_pdf.py; return (stdout, path of the newest trade PDF)."""
    env = os.environ.copy()
    env.pop(ENV, None)
    if with_index_file:
        env[ENV] = with_index_file
    r = subprocess.run([sys.executable, os.path.join(HERE, "build_pdf.py")],
                       capture_output=True, text=True, cwd=ROOT, env=env)
    sys.stdout.write(r.stdout[-400:])
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-1500:])
        sys.exit("build_pdf.py failed (%d)" % r.returncode)
    pdfs = sorted(glob.glob(os.path.join(ROOT, "build", "*_trade.pdf")), key=os.path.getmtime)
    return r.stdout, pdfs[-1]


def components(stdout):
    """slot -> (kind, first PDF page), in book order, from build_pdf's own table."""
    rows = [(m.group(1), m.group(2), int(m.group(3))) for m in TABLE_ROW.finditer(stdout)]
    return sorted(rows, key=lambda r: r[2])


def roman(n):
    out = ""
    for v, r in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out += r
            n -= v
    return out


def norm(s):
    return re.sub(r"\s+", " ", s)


class Book:
    """Page texts (running head and folio clipped out) and printed folios for a PDF."""

    def __init__(self, path):
        pm = _pymupdf()
        self.doc = pm.open(path)
        self.n = self.doc.page_count
        w, h = self.doc[0].rect.width, self.doc[0].rect.height
        body = pm.Rect(0, 55, w, h - 55)          # below the running head, above the folio
        self.a, self.b, self.full, self.folio = [], [], [], []
        for p in self.doc:
            raw = p.get_text("text", clip=body)
            self.a.append(norm(raw.replace("-\n", "")))    # a word broken at a line end, joined
            self.b.append(norm(raw.replace("-\n", "-")))   # a real hyphen broken at a line end
            self.full.append(norm(p.get_text("text")))
            self.folio.append(self._folio(p, h))
        self._infer_folios()

    def _infer_folios(self):
        """Pages that print no folio (the copyright page, the openers of some components).

        The sequence is unbroken, so a missing folio is the page's position: roman numerals
        before the page that prints `1`, arabic after it."""
        one = next((i for i, f in enumerate(self.folio) if f == "1"), None)
        if one is None:
            return
        for i, f in enumerate(self.folio):
            if f is None:
                self.folio[i] = roman(i + 1) if i < one else str(i - one + 1)

    @staticmethod
    def _folio(p, h):
        pm = _pymupdf()
        for clip in (pm.Rect(0, 0, p.rect.width, 55), pm.Rect(0, h - 55, p.rect.width, h)):
            for tok in p.get_text("text", clip=clip).split():
                if re.fullmatch(r"\d{1,3}", tok) or re.fullmatch(r"[ivxlc]{1,6}", tok):
                    return tok
        return None

    def hits(self, rx, pages):
        return [i for i in pages if rx.search(self.a[i]) or rx.search(self.b[i])]


def headings(chapter_md):
    """(section number, heading text) for each <!-- SECTION n --> in a chapter file."""
    text = io.open(chapter_md, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^<!-- SECTION (\d+) -->", text, re.M):
        rest = text[m.end():]
        h = re.search(r"^#{1,6}\s+(.+)$", rest, re.M)
        if h:
            out.append((int(m.group(1)), h.group(1)))
    return out


def key(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def ranges(comps, book):
    """locator label -> list of PDF page indexes (0-based), for chapters, sections, appendices."""
    span = {}
    for i, (slot, kind, first) in enumerate(comps):
        last = (comps[i + 1][2] - 1) if i + 1 < len(comps) else book.n
        span[slot] = list(range(first - 1, last))
    out = {}
    for slot, pages in span.items():
        if slot.startswith("chapter-"):
            n = int(slot.split("-")[1])
            out["Ch %d" % n] = pages
            md = os.path.join(ROOT, "manuscript", "ch%d.md" % n)
            starts, at = [], pages[0]
            for num, head in headings(md):
                k = key(head)
                found = next((p for p in range(at, pages[-1] + 1)
                              if k[:40] in key(book.full[p])), None)
                if found is None:
                    sys.stderr.write("  section %d of Ch %d: heading not found in the PDF (%s)\n"
                                     % (num, n, head[:50]))
                    continue
                starts.append((num, found))
                at = found
            for j, (num, st) in enumerate(starts):
                en = starts[j + 1][1] - 1 if j + 1 < len(starts) else pages[-1]
                out["Ch %d §%d" % (n, num)] = list(range(st, max(st, en) + 1))
        elif slot.startswith("appendix-"):
            out["App %s" % slot.split("-")[1].upper()] = pages
        elif slot == "authors-note":
            out["Author's note"] = pages
    return out


def label(book, i):
    return book.folio[i] or "?"


def compute(book, comps):
    rng = ranges(comps, book)
    skip = set()
    for slot, kind, first in comps:
        if slot == "contents":
            nxt = [c[2] for c in comps if c[2] > first]
            skip |= set(range(first - 1, (nxt[0] - 1) if nxt else first))
    index_first = next(c[2] for c in comps if c[0] == "index") - 1
    skip |= set(range(index_first, book.n))
    pages = [i for i in range(book.n) if i not in skip and book.a[i].strip()]

    entries, problems = [], []
    for group, terms in ib.TERMS.items():
        rows = []
        for display, pat in terms:
            rx = re.compile(pat, re.I)
            hit = book.hits(rx, pages)
            if not hit:
                problems.append("%s: no page in the PDF holds the term" % display)
                continue
            primary = ib.PRIMARY.get(display)
            prim_page = None
            if primary:
                span = rng.get(primary)
                if span is None:
                    problems.append("%s: primary %s has no page range" % (display, primary))
                else:
                    inside = [p for p in hit if p in span]
                    if inside:
                        prim_page = inside[0]
                    else:
                        problems.append("%s: primary %s holds the term in the manuscript "
                                        "but no page in that range does" % (display, primary))
            if len(hit) > SATURATED_PAGES:
                shown = ("**%s**, and throughout" % label(book, prim_page)
                         if prim_page is not None else "throughout")
            else:
                shown = ", ".join(("**%s**" % label(book, p)) if p == prim_page
                                  else label(book, p) for p in hit)
            rows.append((display, shown, len(hit)))
        entries.append((group, rows))
    return entries, problems


def render(entries):
    out = ["# Index", "",
           "Locators are page numbers. **Bold** marks where a term is taught; the rest is "
           "where it gets used.", ""]
    for group, rows in entries:
        out.append("## %s" % group)
        out.append("")
        for display, shown, _n in sorted(rows, key=lambda r: r[0].lower()):
            out.append("**%s** — %s" % (display, shown))
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def cited_ok(book, comps, text):
    """Every page an entry cites must hold its term. Returns a list of failures."""
    fails = []
    term = {d: re.compile(p, re.I) for terms in ib.TERMS.values() for d, p in terms}
    by_folio = {}
    for i, f in enumerate(book.folio):
        if f:
            by_folio.setdefault(f, []).append(i)
    for m in re.finditer(r"^\*\*(.+?)\*\* — (.+)$", text, re.M):
        display, locs = m.group(1), m.group(2)
        rx = term.get(display)
        if rx is None:
            continue
        for tok in re.findall(r"\*{0,2}([0-9]+|[ivxlc]+)\*{0,2}", locs.replace("and throughout", "")):
            pgs = by_folio.get(tok, [])
            if not any(rx.search(book.a[i]) or rx.search(book.b[i]) for i in pgs):
                fails.append("%s cites %s, which does not hold it" % (display, tok))
    return fails


def main():
    dry = "--dry" in sys.argv
    if "--check" in sys.argv:
        pdfs = sorted(glob.glob(os.path.join(ROOT, "build", "*_trade.pdf")), key=os.path.getmtime)
        if not pdfs:
            sys.exit("no build/*_trade.pdf")
        book = Book(pdfs[-1])
        first = next(i for i in range(book.n) if book.a[i].startswith("Index"))
        text = "\n".join(book.a[first:])
        print("index starts on printed page %s; page-locator index present: %s"
              % (book.folio[first], "Locators are page numbers" in text))
        return 0

    print("pass 1 -- section-locator index")
    out1, pdf1 = build_pdf()
    comps = components(out1)
    book1 = Book(pdf1)
    entries, problems = compute(book1, comps)
    text = render(entries)
    n = sum(len(r) for _g, r in entries)
    print("%d entries; %d problem(s)" % (n, len(problems)))
    for p in problems:
        print("  PROBLEM", p)
    if problems:
        sys.exit("ABORT: fix the term list or the page map before printing an index that lies.")
    if dry:
        print(text)
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(text)
    print("wrote %s" % os.path.relpath(OUT, ROOT))

    print("pass 2 -- page-locator index")
    out2, pdf2 = build_pdf(with_index_file=OUT)
    comps2 = components(out2)
    moved = [(a, b) for a, b in zip([c for c in comps if c[0] != "index"],
                                    [c for c in comps2 if c[0] != "index"]) if a[2] != b[2]]
    if moved:
        sys.exit("ABORT: the index changed a page before it (%s). The pass is not sound."
                 % moved[0][0][0])
    book2 = Book(pdf2)
    fails = cited_ok(book2, comps2, text)
    for f in fails:
        print("  FAIL", f)
    if fails:
        sys.exit("ABORT: %d cited page(s) do not hold their term." % len(fails))
    print("final    %s  (%d pages; %d entries, every cited page holds its term)"
          % (os.path.relpath(pdf2, ROOT), book2.n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
