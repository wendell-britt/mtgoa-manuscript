# -*- coding: utf-8 -*-
"""The true proofread — the pass that can only run on the typeset page.

    python3 instruments/proofread.py                      # the workbook proof
    python3 instruments/proofread.py --pdf build/X.pdf    # any built interior
    python3 instruments/proofread.py -v                   # every site, not the head

`SPEC_FINAL_PROOF_2026-08-07.md` §1 splits the work three ways and says the third
one *"cannot run yet — it needs the PDF, not the markdown."* This is that pass.
It reads the built interior rather than `manuscript/`, because **every defect it
looks for is created by typesetting and none of them exists in the source.**
A widow is not a bad sentence. It is a good sentence that landed in the wrong
place, and it moves the moment anything above it changes length.

## Why this is a separate instrument from build_pdf.py

`build_pdf.py --check` already refuses to emit a PDF whose chapter openers land
on a verso, whose folio skips, or whose blank leaves carry a running head. Those
are **structural** and the template can prove them from its own record.

Widows, orphans, runts and hyphen stacks cannot be proved that way. They are
properties of where the text happened to break, they need the rendered page, and
there are 404 of those. **This exists so a person looks at eleven pages instead
of four hundred.**

## What it finds, and the trade's definitions

The words get used loosely and backwards; these are the compositor's meanings.

**Orphan** — a paragraph's *first* line stranded alone at the *foot* of a page.
The reader turns the page to find the paragraph. Mnemonic: an orphan is alone at
the start, with no past.

**Widow** — a paragraph's *last* line stranded alone at the *head* of a page,
with no past either. It is the worse of the two, because the eye reads a lone
line under a running head as a heading.

**Runt** — a paragraph's last line carrying one short word. Not a page-break
defect, so it is reported at a lower tier: it is a hyphenation-and-tracking fix
and it survives repagination, which is why it is worth a separate pass.

**Hyphen stack** — three or more consecutive lines ending in a hyphen. Two is
normal; three is the number the trade calls a ladder and most house styles cap
at two.

## The geometry it reads, and why it is safe to hard-code

Body text sets at x0 **97.2** with a first-line indent to **111.0** and a measure
ending near **471**. Anything else on the page — the shaded handbook panels, the
marginalia blocks, tables, headings, running heads and folios — sits at a
different x0 or a different size, so **restricting to those two left edges at the
body size isolates running prose exactly.** The numbers come out of the preset,
so a different trim wants a different pair; `--pdf` re-derives them per file
rather than assuming the workbook.

**A paragraph is detected by its shape, never by its text.** Indent starts one;
a line short of the measure ends one. That is why this reads the same on a page
of dialogue as on a page of exposition, and why it does not care what the words
say.

## What it deliberately does not report

**Rivers, loose lines and bad rags** are real proofreading defects and a machine
reading extracted text cannot see them honestly. They want the eye on the proof
PNGs. Reporting a guess would put noise on a board whose whole value is that it
is short — the lesson `HANDOFF_FINAL_PROOF_2026-08-07.md` paid three rounds for.
"""
import io, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

BODY_SIZE_TOL = 0.35
FULL_LINE = 6.0            # points shy of the measure and a line still counts full
RUNT_WORDS = 1             # a last line of this many words is a runt
HYPHEN_STACK = 3


def load(path):
    try:
        import pymupdf
    except ImportError:
        sys.stderr.write("pymupdf missing. pip install pymupdf\n")
        return None
    return pymupdf.open(path)


def geometry(doc):
    """Body size, and the left/indent/right triple **for each page parity**.

    **Margins are mirrored**, so the binding edge swaps sides every leaf and the
    body's left edge takes two values, not one. The first version of this file
    averaged them into a single number and silently read only half the book —
    every page of the other parity fell outside the x0 filter and was skipped,
    and the board came back a clean 0/0 because nothing had been looked at.
    Derive per parity, always.
    """
    sizes = collections.Counter()
    for page in doc:
        for b in page.get_text("dict")["blocks"]:
            if b["type"]:
                continue
            for l in b["lines"]:
                sizes[round(l["spans"][0]["size"], 1)] += 1
    body = sizes.most_common(1)[0][0]

    geo = {}
    for parity in (0, 1):
        lefts, rights = collections.Counter(), collections.Counter()
        for n, page in enumerate(doc):
            if (n + 1) % 2 != parity:
                continue
            for b in page.get_text("dict")["blocks"]:
                if b["type"]:
                    continue
                for l in b["lines"]:
                    if abs(round(l["spans"][0]["size"], 1) - body) > BODY_SIZE_TOL:
                        continue
                    lefts[round(l["bbox"][0], 1)] += 1
                    rights[round(l["bbox"][2], 1)] += 1
        left = lefts.most_common(1)[0][0]
        # The first-line indent is the *most frequent* left edge to the right of
        # the margin, never the nearest one. Taking the minimum picks up the list
        # indent, which sits between the two -- and then every numbered step in
        # the book reads as a paragraph opening and the orphan board fills with
        # list items.
        indent = next((x for x, _ in lefts.most_common()
                       if left < x < left + 30), left + 13.8)
        geo[parity] = (left, indent, max(rights))
    return body, geo


def body_lines(page, folio, body, geo):
    """Running prose only: the two body left edges at the body size.

    Everything else on the page — shaded panels, marginalia, tables, headings,
    running heads, folios — sits at another x0 or another size, so this isolates
    the text whose breaks are worth ruling on.
    """
    left, indent, right = geo[folio % 2]
    out = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"]:
            continue
        for l in b["lines"]:
            if abs(round(l["spans"][0]["size"], 1) - body) > BODY_SIZE_TOL:
                continue
            x0 = round(l["bbox"][0], 1)
            if abs(x0 - left) > 0.6 and abs(x0 - indent) > 0.6:
                continue
            out.append({"x0": x0, "x1": l["bbox"][2], "y": l["bbox"][1],
                        "text": "".join(s["text"] for s in l["spans"]),
                        "indented": abs(x0 - indent) <= 0.6,
                        "full": l["bbox"][2] >= right - FULL_LINE})
    out.sort(key=lambda r: r["y"])
    return out


def main():
    verbose = "-v" in sys.argv
    pdf = None
    for i, a in enumerate(sys.argv):
        if a == "--pdf" and i + 1 < len(sys.argv):
            pdf = sys.argv[i + 1]
        elif a.startswith("--pdf="):
            pdf = a.split("=", 1)[1]
    if pdf is None:
        found = sorted(glob.glob(os.path.join(ROOT, "build", "*workbook.pdf")))
        if not found:
            sys.stderr.write("no workbook PDF in build/. Run build_pdf.py --trim=workbook\n")
            return 1
        pdf = found[-1]

    doc = load(pdf)
    if doc is None:
        return 1
    body, geo = geometry(doc)
    pages = [body_lines(p, n + 1, body, geo) for n, p in enumerate(doc)]

    # The lowest content of any kind on each page. An orphan candidate has to be
    # the last thing on its leaf: `ch3:69` ends on a one-line paragraph that
    # fills the measure and is followed by a marginalia block, and without this
    # it reads as a paragraph running over the break. It is not one -- the eye
    # on the rendered page is what caught it, and this is that judgement encoded.
    floors = []
    for page in doc:
        ys = [b["bbox"][3] for b in page.get_text("dict")["blocks"]]
        floors.append(max(ys) if ys else 0.0)

    widows, orphans, runts, stacks = [], [], [], []
    whole_word_runts = []

    for n, lines in enumerate(pages):
        folio = n + 1
        if not lines:
            continue
        prev = pages[n - 1] if n else []
        nxt = pages[n + 1] if n + 1 < len(pages) else []

        # A paragraph runs on across the leaf only if the page before it ended
        # on a full line. A short last line means the paragraph closed there.
        carried_in = bool(prev) and prev[-1]["full"]
        carries_out = lines[-1]["full"] and bool(nxt) and not nxt[0]["indented"]

        # --- hyphen ladders
        run = 0
        for l in lines:
            if l["text"].rstrip().endswith(("-", "\u2010", "\u00ad")):
                run += 1
                if run >= HYPHEN_STACK:
                    stacks.append((folio, run, l["text"].strip()[-44:]))
            else:
                run = 0

        # --- runts, split into the tier that matters and the tier that does not.
        # A one-word last line is ordinary typography and the book has 139 of
        # them; listing those buries the three that are defects. A last line that
        # is the *back half of a hyphenated word* is always wrong -- the reader
        # gets `ation.` alone under four hundred words of argument.
        for i, l in enumerate(lines):
            closes = (i + 1 >= len(lines)) or lines[i + 1]["indented"]
            if not (closes and not l["full"] and l["text"].strip()):
                continue
            if len(l["text"].split()) > RUNT_WORDS:
                continue
            if i + 1 >= len(lines) and carries_out:
                continue
            if i and lines[i - 1]["text"].rstrip().endswith(("-", "\u2010", "\u00ad")):
                runts.append((folio, l["text"].strip()))
            else:
                whole_word_runts.append(folio)

        # --- WIDOW: the paragraph carried in closes on this page's first line
        if carried_in and not lines[0]["indented"]:
            closes = (len(lines) == 1) or lines[1]["indented"]
            if closes:
                widows.append((folio, lines[0]["text"].strip()[:66]))

        # --- ORPHAN: this page's last line opens a paragraph that runs over
        at_foot = lines[-1]["y"] >= floors[n] - 40
        if carries_out and lines[-1]["indented"] and at_foot:
            orphans.append((folio, lines[-1]["text"].strip()[:66]))

    print("proofread — %s" % os.path.relpath(pdf, ROOT))
    lo, li, lr = geo[1]
    vo, vi, vr = geo[0]
    print("  %d pages · body %.1fpt · measure %.0fpt · indent %.1fpt"
          % (doc.page_count, body, lr - lo, li - lo))
    print("  mirrored margins: recto x0 %.1f · verso x0 %.1f" % (lo, vo))
    print()
    print("  WIDOW  %4d   a paragraph's last line alone at the head of a page" % len(widows))
    print("  ORPHAN %4d   a paragraph's first line alone at the foot of a page" % len(orphans))
    print("  STACK  %4d   three or more hyphenated line-ends in a row" % len(stacks))
    print("  FRAGMENT %2d   a last line that is the back half of a hyphenated word" % len(runts))
    print("           %d one-word last lines not listed — ordinary typography" % len(whole_word_runts))

    def show(title, rows, fmt):
        if not rows:
            return
        print("\n  %s" % title)
        for r in (rows if verbose else rows[:14]):
            print("    " + fmt(r))
        if not verbose and len(rows) > 14:
            print("    ... %d more, run -v" % (len(rows) - 14))

    show("WIDOW", widows, lambda r: "p%-4d %s" % (r[0], r[1]))
    show("ORPHAN", orphans, lambda r: "p%-4d %s" % (r[0], r[1]))
    show("STACK", stacks, lambda r: "p%-4d %d in a row ...%s" % (r[0], r[1], r[2]))
    show("FRAGMENT", runts, lambda r: "p%-4d %r" % (r[0], r[1]))

    total = len(widows) + len(orphans) + len(stacks)
    print("\n%d page-break finding(s) - %d fragment(s) - reporting only, a person rules each one"
          % (total, len(runts)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
