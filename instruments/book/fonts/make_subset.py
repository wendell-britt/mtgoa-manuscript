# -*- coding: utf-8 -*-
"""
Build the two-glyph CJK font the interior needs, and nothing more.

Appendix G credits the five-phase system as **wu xing** (五行). No font embedded
in the Typst binary carries CJK, and Typst gives no warning for a glyph it cannot
set — it draws a box. On this container the characters render only because a
system CJK font happens to be installed, which is exactly the accident that
`ignore_system_fonts=True` exists to prevent.

So the two glyphs get committed. Two, not a font: this subsets IPAGothic down to
五 and 行 and nothing else, which is **2,752 bytes**. A full CJK face is 6MB and
would be 6MB of a book that has two Chinese characters in it.

    python3 instruments/book/fonts/make_subset.py

Requires `fonttools` and IPAGothic on the machine — neither is needed to *build*
the book, only to regenerate this file. The output is committed, so a normal build
never runs this.

## Why IPAGothic

It is what was reachable. Noto Serif CJK is the better match for a book set in
Libertinus, and it is under the SIL Open Font License, which is the friendlier
licence — but every route to it from this container is blocked (403 from GitHub,
404 from gstatic). IPAGothic is on the machine, is licensed for this, and is a
sans beside a serif, which for two characters inside a Latin parenthetical is a
difference nobody will notice. Wendell ruled the sans acceptable on 2026-08-01.

## What the licence requires, and how this satisfies it

The output is a Derived Program under the IPA Font License v1.0, and Article 3
Paragraph 1 attaches four conditions to redistributing one. All four are met here:

  (1)(b)  the file that allows further modification — this script
  (2)     the means to replace the derived font with the original — this script
          again, which names the source font and the exact transformation
  (3)     the derived font is licensed under the same agreement — see LICENSE.txt
          in this directory, which covers the .ttf and nothing else in the repo
  (4)     the name of the licensed program appears in no name of the derived
          program — hence FAMILY below, and the output filename

Embedding the glyphs in the printed PDF is use, not redistribution of a font
program, and carries none of this.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

SOURCE = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
OUTPUT = os.path.join(HERE, "MTGOA-CJK-Subset.ttf")

# Article 3.1(4): no part of the source font's name may appear in the derived
# font's name. This string is also what `mtgoa.typ` asks for by name, so the two
# have to agree.
FAMILY = "MTGOA CJK Subset"

# Everything the book needs. Add a character here only when the manuscript gains
# one — `build_pdf.py` reports any character the interior cannot set, so a new one
# announces itself.
GLYPHS = "五行"


def rename(font, family):
    """Rewrite every name record that carries a family or full name."""
    for record in font["name"].names:
        # 1 family, 4 full name, 6 PostScript, 16 typographic family
        if record.nameID in (1, 4, 16):
            record.string = family
        elif record.nameID == 6:
            record.string = family.replace(" ", "")


def main():
    try:
        from fontTools.ttLib import TTFont
        from fontTools import subset
    except ImportError:
        sys.stderr.write("fonttools missing. pip install fonttools\n")
        return 1

    if not os.path.exists(SOURCE):
        sys.stderr.write(
            "Source font not found: %s\n"
            "Install it (Debian: fonts-ipafont-gothic) or point SOURCE at a CJK "
            "font you are licensed to subset, and update LICENSE.txt to match.\n"
            % SOURCE)
        return 1

    font = TTFont(SOURCE)
    options = subset.Options()
    options.name_IDs = ["*"]
    options.name_legacy = True
    options.name_languages = ["*"]

    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=GLYPHS)
    subsetter.subset(font)

    rename(font, FAMILY)
    font.save(OUTPUT)

    print("%s  ->  %s" % (SOURCE, os.path.relpath(OUTPUT, HERE)))
    print("family %r, glyphs %r, %d bytes"
          % (FAMILY, GLYPHS, os.path.getsize(OUTPUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
