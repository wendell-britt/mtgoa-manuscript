# -*- coding: utf-8 -*-
"""
Convert the assembled manuscript to EPUB, and refuse to emit one that reads badly
on a phone.

The ebook is the shipping format, so this is the last instrument between the book
and a reader. It exists because two things were discovered by conversion rather
than by reading, and neither would have surfaced any other way.

**The YAML trap.** `build_book.py`'s output would not convert at all. Pandoc reads
a `---` horizontal rule as the start of a YAML metadata block, and ch8 carries

    ---
    **Alchemy Move 2: Game-Switcher**
    Altitude-arrogance: **Anger** → *Triumph*

so pandoc parsed `Altitude-arrogance:` as a YAML key, found a value starting with
`*`, read it as an alias reference, and died with exit 64. The manuscript is
correct markdown. The extension is what misfires, so `markdown-yaml_metadata_block`
turns it off. That flag is not optional and not a preference — without it there is
no ebook.

**Reflow.** A fenced block becomes `<pre>`, and `<pre>` does not reflow. The five
`Try this now` exercises were fenced, the widest line ran 98 characters, and a
phone gives you about 40. The practices were the part of the book most likely to
arrive clipped, which is the opposite of what they are for, since the reader this
book is written for stops for a named move with a practice and skims everything
else. They are now ordinary lists, and PRE_BUDGET keeps them that way.

    python3 instruments/build_epub.py            # convert the newest build/
    python3 instruments/build_epub.py --check     # report only, write nothing
"""
import io, os, re, sys, glob, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BUILD = os.path.join(ROOT, "build")

# Pandoc's markdown, minus the extension that cannot parse this book. Anything
# added here should be justified in the docstring above, not just switched on.
FORMAT = "markdown-yaml_metadata_block"

META = [
    "--metadata", "title=Mastering the Game of Allyship",
    "--metadata", "creator=Wendell Britt",
    "--metadata", "lang=en",
    "--toc", "--toc-depth=2",
]

# A ratchet, the same shape as instruments/emdash_budget.json. `<pre>` is the one
# construct that cannot reflow, so the budget is zero and a rise is a failure
# rather than a note. Raising this number is a decision about the reader's phone.
PRE_BUDGET = 0

# Tables reflow, badly. They are legitimate here — the polarity and channel tables
# carry real content — so this is a reported number and not a gate. It is here so
# that a table arriving in a chapter that had none gets noticed.
TABLE_EXPECTED = 14


def newest_build():
    files = sorted(glob.glob(os.path.join(BUILD, "MTGOA_PRINT_*.md")))
    if not files:
        sys.stderr.write("No build/MTGOA_PRINT_*.md. Run build_book.py --write first.\n")
        return None
    return files[-1]


def count_tags(epub_path):
    """Tally the constructs that decide whether this reads on a phone."""
    tags = {"pre": 0, "table": 0, "blockquote": 0, "img": 0, "li": 0}
    with zipfile.ZipFile(epub_path) as z:
        for name in z.namelist():
            if not name.endswith((".xhtml", ".html")):
                continue
            text = z.read(name).decode("utf-8", "replace")
            for tag in tags:
                tags[tag] += len(re.findall(r"<%s[ >]" % tag, text))
    return tags


def main():
    check_only = "--check" in sys.argv
    src = newest_build()
    if src is None:
        return 1

    try:
        import pypandoc
    except ImportError:
        sys.stderr.write("pypandoc missing. pip install pypandoc-binary\n")
        return 1

    out = os.path.join(BUILD, os.path.basename(src).replace(".md", ".epub"))
    print("source  %s (%d bytes)" % (os.path.relpath(src, ROOT), os.path.getsize(src)))
    try:
        pypandoc.convert_file(src, "epub3", outputfile=out, format=FORMAT, extra_args=META)
    except Exception as exc:
        # Keep the whole message. The YAML failure named a line number, and that
        # line number is what made it a ten-minute fix instead of a bisect.
        sys.stderr.write("\nCONVERSION FAILED\n%s\n" % exc)
        return 1

    tags = count_tags(out)
    print("epub    %s (%d bytes)" % (os.path.relpath(out, ROOT), os.path.getsize(out)))
    print("-" * 62)
    for tag in ("pre", "table", "blockquote", "img", "li"):
        print("  %-11s %d" % ("<%s>" % tag, tags[tag]))
    print("-" * 62)

    problems = []
    if tags["pre"] > PRE_BUDGET:
        problems.append("%d <pre> block(s), budget %d. A fenced block does not "
                        "reflow; on a phone it clips or side-scrolls."
                        % (tags["pre"], PRE_BUDGET))
    if tags["blockquote"] == 0:
        problems.append("no <blockquote>: the marginalia frame is stripped. "
                        "Run `python3 marginalia/compile.py --apply`, rebuild, retry.")
    if tags["table"] != TABLE_EXPECTED:
        print("NOTE: %d tables, expected %d. Not a failure — check the new one "
              "reads on a narrow screen." % (tags["table"], TABLE_EXPECTED))
    if tags["img"] == 0:
        print("NOTE: 0 images. The book ships text-only until the figures exist.")

    if check_only:
        os.remove(out)
        print("--check: removed the artifact.")

    if problems:
        print("\nEPUB FAIL")
        for p in problems:
            print("  " + p)
        return 1
    print("\nEPUB OK — reflows, frame present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
