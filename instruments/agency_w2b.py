# -*- coding: utf-8 -*-
"""
agency_w2b.py — the two W-2 residuals the first pass missed.

Both surfaced on the post-batch scan. Same ruling: navigation with mechanical or
directional verbs is licensed; perception, intention, speech and social-causal
on the book or chapter are not.

ch3:501 carries two constructions in one sentence and they are NOT the same:

    "Chapter 1 named the fuel; this chapter teaches you to make it."

`named` is a speech verb and `teaches` is social-causal, so both are illegal --
but the sentence's job is navigation and it should still read as navigation
after the repair. The line already spends `handed` ("the fuel economy Chapter 1
handed to the Shaman to finish") 400 characters earlier, so reusing it here
would knock. `left you` is directional, licensed, and keeps the handoff.

    python3 instruments/agency_w2b.py --dry
    python3 instruments/agency_w2b.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ("manuscript/ch3.md", "nav + you",
     "Chapter 1 named the fuel; this chapter teaches you to make it.",
     "Chapter 1 left you the fuel; here you learn to make it."),

    ("appendices/ON_THE_SHOULDERS_OF.md", "I",
     "which is exactly why this book proposes redesigning the game "
     "rather than trying harder inside the old one.",
     "which is exactly why I propose redesigning the game "
     "rather than trying harder inside the old one."),
]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, _t, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, _t, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, n, before[:88]))

    for path, target, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s  [-> %s]" % (path, target))
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
