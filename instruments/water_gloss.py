# -*- coding: utf-8 -*-
"""
water_gloss.py — anchor the one unglossed element subject in the manuscript.

Wendell caught this reading back the three surviving W-1 sites. The question was
whether Fire and Water in those lines were the elements or the emotions. They
are the elements, and that is by design: ch3:441 teaches the mapping in a table
(Metal/Fear, Water/Sadness, Wood/Joy, Fire/Anger, Earth/Neutrality) and ch3:431
flags outright that the correspondences are a remix rather than classical wu
xing. The book uses both names interchangeably from ch3 on.

Two of the three sites are anchored. ch4:283 opens with the heading gloss
"(Fire/Anger -> Triumph)" and closes three sentences later on "anger that made
it all the way out of the body". ch2:189 is not an element at all -- "the
feeling", generic, with "the anger that shows up is signal" two sentences back.

ch4:670 is the outlier, and a full sweep of every chapter says it is the ONLY
place in the manuscript where an element stands as a bare subject with no
emotion word anywhere in the sentence to anchor it:

    Anger delivered as anger lands hard and lands clean, because Fire asks for
    agency and the other person can hand agency over. Hurt delivered as anger
    lands as an attack, and nothing they do can satisfy it, because Water
    wanted to be met and you asked to win instead.

The parallel is anger:Fire :: hurt:Water, and the parallelism carries most of
the load. But `hurt` is never mapped to Water anywhere in the book -- the table
says Sadness, and a grep of ch4 for any hurt/Water or hurt/sad co-occurrence
returns nothing. So the reader makes hurt -> sadness -> Water in one unassisted
hop, in a sentence doing real work.

The fix restores the table mapping in place and leaves the Fire/Water parallel
standing. Comma appositive rather than em-dash: ch4's em-dashes live only in
headings, epigraph attributions and blockquoted marginalia, never as a
parenthetical inside body prose.

`the sadness under it` over `sadness` or `the sadness underneath` because the
book already names a move called Say the Thing Under the Thing (ch3:981), so
the phrasing lands inside the register rather than beside it.

    python3 instruments/water_gloss.py --dry
    python3 instruments/water_gloss.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ("manuscript/ch4.md",
     "because Water wanted to be met and you asked to win instead.",
     "because Water, the sadness under it, wanted to be met and you asked to win instead."),
]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, n, before[:88]))

    for path, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s" % path)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
