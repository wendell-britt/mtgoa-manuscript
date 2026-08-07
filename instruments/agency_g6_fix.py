# -*- coding: utf-8 -*-
"""
agency_g6_fix.py — Wendell's two corrections to the Grade 6 batch, 2026-08-02.

Both of my rewrites were wrong and both for reasons worth recording.

ch2. I wrote "Trained that way, you perform. You do not play." The original
contrast was performance against play as CAPACITIES -- "That structure trains
performance. It does not train play." Dropping `train` collapsed a capacity into
an act: not-playing is a description of a moment, not-learning-to-be-playful is
the thing the training costs you. Wendell's line restores the capacity reading
and keeps the person holding the verb.

Appendix A. I wrote "that people who wouldn't otherwise be at the table end up
at it." The `it` has no referent -- I had removed `the structure`, which was the
only noun `it` could point back to, and left the pronoun stranded. A dangling
pronoun is the same defect class this audit exists to remove, arrived at from
the other direction. Wendell's line names the outcome instead of pointing at a
noun that is no longer there.

    python3 instruments/agency_g6_fix.py --dry
    python3 instruments/agency_g6_fix.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ("manuscript/ch2.md",
     "Trained that way, you perform. You do not play.",
     "Trained that way, you perform. You do not learn to be playful."),

    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
     "Gift: can hold enough genuine relationship across real difference that people "
     "who wouldn't otherwise be at the table end up at it.",
     "Gift: can hold enough genuine relationship across real difference that people "
     "who would otherwise be left out find themselves with a space at the table."),
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
