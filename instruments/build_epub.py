# -*- coding: utf-8 -*-
"""
Convert the manuscript to EPUB, and refuse to emit one that reads badly on a phone.

The ebook is the shipping format, so this is the last instrument between the book
and a reader.

    python3 instruments/build_epub.py            # build build/MTGOA_<date>.epub
    python3 instruments/build_epub.py --check    # build, verify, delete

## Two things this found by converting, which reading would not have

**The YAML trap.** The first version of the build would not convert at all.
Pandoc reads a `---` horizontal rule as the start of a YAML metadata block, and
ch8 carries

    ---
    **Alchemy Move 2: Game-Switcher**
    Altitude-arrogance: **Anger** → *Triumph*

so pandoc parsed `Altitude-arrogance:` as a YAML key, found a value starting with
`*`, read it as an alias reference, and died with exit 64. The manuscript is
correct markdown; the extension is what misfires, so `markdown-yaml_metadata_block`
turns it off. `typeset.py` now resolves every rule in the book before pandoc sees
it, so the trap is no longer reachable — the flag stays because the cost of being
wrong about that is a build that dies with no ebook and a cryptic exit code.

**Reflow.** A fenced block becomes `<pre>`, and `<pre>` does not reflow. The five
`Try this now` exercises were fenced, the widest line ran 98 characters, and a
phone gives you about 40. The practices were the part of the book most likely to
arrive clipped, which is the opposite of what they are for, since the reader this
book is written for stops for a named move with a practice and skims everything
else. They are now ordinary lists, and PRE_BUDGET keeps them that way.

## What it checks now

The frame is the third thing, and it is the one that would fail silently. Each
chapter is a document by one character annotated by another, carried by five
devices that are five different HTML comments in canon and five different classes
after `typeset.py`. If any of that fails to survive the conversion, the ebook
still builds, still opens, still reads — as one voice instead of two. So the
device counts in the EPUB are checked against the counts `typeset.py` resolved,
per device, and a mismatch fails the build.
"""
import io, os, re, sys, glob, uuid, zipfile, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BOOK = os.path.join(HERE, "book")
BUILD = os.path.join(ROOT, "build")

FILTER = os.path.join(BOOK, "epub.lua")
CSS = os.path.join(BOOK, "epub.css")

TITLE = "Mastering the Game of Allyship"
SUBTITLE = "How to Show Up, Clean Up, Wake Up, and Grow Up — and Keep Playing"
AUTHOR = "Wendell Britt"
PUBLISHER = "Wendell Britt"
RIGHTS = "Copyright © 2026 Wendell Britt. All rights reserved."

# Pandoc's markdown, minus the extension that cannot parse this book.
FORMAT = "markdown-yaml_metadata_block"

# No ISBN is assigned — `MANIFEST.md` records that as a decision, not an oversight,
# and an ebook ships without one. The identifier still has to be stable across
# builds, or every rebuild looks like a different book to a library. Pandoc mints
# a random UUID when you let it, so the identifier is derived here instead: same
# title, same URN, every time, on every machine.
IDENTIFIER = "urn:uuid:%s" % uuid.uuid5(uuid.NAMESPACE_URL,
                                        "https://masteringallyship.com/" + TITLE)

# `<pre>` is the one construct that cannot reflow, so the budget is zero and a rise
# is a failure rather than a note. Raising this number is a decision about the
# reader's phone.
PRE_BUDGET = 0

# Tables reflow, badly. They are legitimate here — the polarity and channel tables
# carry real content — so this is a reported number and not a gate. It is here so
# that a table arriving in a chapter that had none gets noticed.
#
# It read 14 until 2026-08-01, and four of those fourteen were not tables. A `---`
# above a pair of lines is a valid multiline-table rule in pandoc's markdown, so
# four passages of Chapter 8 — the Game-Switcher, Diagnostician, and Returner
# alchemy moves — were being set as tables in every build. `typeset.py` resolves
# the rules before pandoc reads them, and the count is the true one now.
TABLE_EXPECTED = 10

DEVICES = ("marginalia", "epigraph", "handbook", "signature", "postcard",
           "sectionsubtitle", "scenebreak", "centered")


def newest(pattern):
    files = sorted(glob.glob(os.path.join(BUILD, pattern)))
    return files[-1] if files else None


def unhyphenate_for_reflow(src):
    """Undo `typeset.py`'s hyphenation rulings. They are a fixed-measure fix.

    `typeset.py` holds two words together with U+2011 NON-BREAKING HYPHEN and
    U+2060 WORD JOINER so the PDF stops setting `desti-` / `nation.` as a line of
    its own. **The EPUB has no measure to break against**, so it inherits the cost
    of those characters and none of the benefit: a reader searching the ebook for
    `destination` would miss nine occurrences, and `open-mindedness` one, because
    U+2060 and U+2011 do not match the characters anybody types.

    Both builders read one intermediate on purpose -- `typeset.py`'s docstring
    calls that the reason the two editions cannot drift on a marginal note -- so
    the inverse belongs here rather than in a second source file. This is the only
    thing the EPUB undoes, and it undoes it because the defect it fixes cannot
    exist in a reflowing book.
    """
    # NOT "MTGOA_TYPESET_*" -- both builders resolve their source with
    # newest("MTGOA_TYPESET_*.md"), so a file named that way is picked up by
    # build_pdf.py on its next run and the PDF silently loses the rulings. Caught
    # 2026-08-13 by re-proofing after the change: trade went back to 2 fragments.
    out = os.path.join(BUILD, "MTGOA_REFLOW_SRC_%s.md"
                       % datetime.date.today().isoformat())
    text = io.open(src, encoding="utf-8").read()
    n11, n60 = text.count(u"\u2011"), text.count(u"\u2060")
    text = text.replace(u"\u2011", "-").replace(u"\u2060", "")
    os.makedirs(BUILD, exist_ok=True)
    io.open(out, "w", encoding="utf-8").write(text)
    print("reflow   %d non-breaking hyphen(s), %d word joiner(s) undone" % (n11, n60))
    return out


def typeset_source():
    rc = subprocess.call([sys.executable, os.path.join(HERE, "typeset.py"), "--write"],
                         cwd=ROOT, stdout=subprocess.DEVNULL)
    if rc != 0:
        sys.stderr.write("typeset.py refused to write. Run it directly for the flags.\n")
        return None
    return newest("MTGOA_TYPESET_*.md")


def expected_devices(src):
    """What `typeset.py` put in. The EPUB has to come out holding the same."""
    text = io.open(src, encoding="utf-8").read()
    return {d: len(re.findall(r"^::: \{\.%s\}$" % d, text, re.M)) for d in DEVICES}


def metadata_file(path):
    io.open(path, "w", encoding="utf-8").write("""<dc:title>%s</dc:title>
<dc:creator opf:role="aut" opf:file-as="Britt, Wendell">%s</dc:creator>
<dc:identifier id="epub-id-1">%s</dc:identifier>
<dc:language>en-US</dc:language>
<dc:publisher>%s</dc:publisher>
<dc:date>%s</dc:date>
<dc:rights>%s</dc:rights>
<dc:description>%s</dc:description>
""" % (TITLE, AUTHOR, IDENTIFIER, PUBLISHER, datetime.date.today().isoformat(),
       RIGHTS, SUBTITLE))


def inspect(epub_path):
    """Tally what actually landed in the XHTML, per file and in total."""
    tags = {"pre": 0, "table": 0, "blockquote": 0, "img": 0, "li": 0, "h1": 0}
    devices = {d: 0 for d in DEVICES}
    docs = []
    with zipfile.ZipFile(epub_path) as z:
        for name in sorted(z.namelist()):
            if not name.endswith((".xhtml", ".html")):
                continue
            text = z.read(name).decode("utf-8", "replace")
            docs.append((name, len(text)))
            for tag in tags:
                tags[tag] += len(re.findall(r"<%s[ >]" % tag, text))
            for d in devices:
                devices[d] += len(re.findall(r'class="[^"]*\b%s\b' % d, text))
    return tags, devices, docs


def cover_image():
    for ext in ("jpg", "jpeg", "png"):
        p = os.path.join(ROOT, "front_matter", "cover.%s" % ext)
        if os.path.exists(p):
            return p
    return None


def main():
    check_only = "--check" in sys.argv

    try:
        import pypandoc
    except ImportError:
        sys.stderr.write("pypandoc missing. pip install pypandoc-binary\n")
        return 1

    src = typeset_source()
    if src is None:
        return 1
    src = unhyphenate_for_reflow(src)
    print("source   %s (%d bytes)" % (os.path.relpath(src, ROOT), os.path.getsize(src)))

    os.makedirs(BUILD, exist_ok=True)
    stamp = datetime.date.today().isoformat()
    out = os.path.join(BUILD, "MTGOA_%s.epub" % stamp)
    meta = os.path.join(BUILD, "epub_metadata_%s.xml" % stamp)
    metadata_file(meta)

    args = ["--wrap=preserve",
            "--lua-filter=%s" % FILTER,
            "--css=%s" % CSS,
            "--epub-metadata=%s" % meta,
            # One file per component. Without this the whole 120,000 words arrive
            # as a single XHTML document, which several readers will not paginate.
            "--split-level=1",
            # Pandoc's own title page duplicates the one in `front_matter/`.
            "--epub-title-page=false",
            "--toc", "--toc-depth=2",
            "--metadata", "title=%s" % TITLE,
            "--metadata", "author=%s" % AUTHOR,
            "--metadata", "lang=en-US"]

    cover = cover_image()
    if cover:
        args += ["--epub-cover-image=%s" % cover]

    try:
        pypandoc.convert_file(src, "epub3", outputfile=out, format=FORMAT,
                              extra_args=args)
    except Exception as exc:
        # Keep the whole message. The YAML failure named a line number, and that
        # line number is what made it a ten-minute fix instead of a bisect.
        sys.stderr.write("\nCONVERSION FAILED\n%s\n" % exc)
        return 1

    tags, devices, docs = inspect(out)
    want = expected_devices(src)

    print("epub     %s (%d bytes)" % (os.path.relpath(out, ROOT), os.path.getsize(out)))
    print("-" * 66)
    print("  %-14s %s" % ("documents", len(docs)))
    for tag in ("h1", "pre", "table", "blockquote", "img", "li"):
        print("  %-14s %d" % ("<%s>" % tag, tags[tag]))
    print("-" * 66)
    print("  %-16s %6s %6s" % ("device", "source", "epub"))
    for d in DEVICES:
        print("  %-16s %6d %6d%s" % (d, want[d], devices[d],
                                     "" if want[d] == devices[d] else "   <-- MISMATCH"))
    print("-" * 66)

    problems, notes = [], []

    if tags["pre"] > PRE_BUDGET:
        problems.append("%d <pre> block(s), budget %d. A fenced block does not "
                        "reflow; on a phone it clips or side-scrolls."
                        % (tags["pre"], PRE_BUDGET))

    lost = [(d, want[d], devices[d]) for d in DEVICES if want[d] != devices[d]]
    if lost:
        problems.append("the frame did not survive conversion: "
                        + "; ".join("%s %d in, %d out" % t for t in lost)
                        + ". The ebook would read as one voice instead of two.")

    if want["marginalia"] and devices["marginalia"] == 0:
        problems.append("no marginalia in the output. Run "
                        "`python3 marginalia/compile.py --apply` and rebuild.")

    if tags["h1"] < 15:
        problems.append("%d <h1> across the book — the components did not split. "
                        "Check --split-level." % tags["h1"])

    if tags["table"] != TABLE_EXPECTED:
        notes.append("%d tables, expected %d. Not a failure — check the new one "
                     "reads on a narrow screen." % (tags["table"], TABLE_EXPECTED))
    if tags["img"] == 0:
        notes.append("0 images. The book ships text-only until the figures exist.")
    if cover is None:
        notes.append("no cover: front_matter/cover.{jpg,png} is absent. Most "
                     "stores require one, and a reader's library shows a blank "
                     "tile without it.")
    else:
        notes.append("cover %s" % os.path.relpath(cover, ROOT))

    for n in notes:
        print("  " + n)

    if check_only:
        os.remove(out)
        os.remove(meta)
        print("  --check: removed the artifact.")

    if problems:
        print("\nEPUB FAIL")
        for p in problems:
            print("  " + p)
        return 1
    print("\nEPUB OK — reflows, %d documents, frame intact across %d devices."
          % (len(docs), sum(1 for d in DEVICES if devices[d])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
