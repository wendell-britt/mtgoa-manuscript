# -*- coding: utf-8 -*-
"""
agency_w1.py — the W-1 conversions.

Wendell ruled W-1 on 2026-08-02: **license `want` only, not the intention class.**

  LICENSED   want (and the pure-vector cousins seek, aim). The current model
             defines each channel as a directed movement, and `wants` is the
             natural English word for a vector with an object. It describes
             where the current is going, not what it thinks.

  ILLEGAL    every other intention verb -- tries, decides, refuses, promises,
             convinces, means to. These ascribe deliberation, and a channel
             that deliberates is a channel with a mind.

Three sites stand untouched under the license, and all three would have been
damaged by R5: "which Fire wants and almost never gets" (ch4:242), "because
Water wanted to be met and you asked to win instead" (ch4:604), and "what the
feeling wants to build" (ch2:189).

Three more clear on verb SENSE rather than license: "fear meant something",
"anger meant something", "what the feeling means" all use `mean` in the
semantic sense -- signified -- not the intentional one. Right lemma, wrong
sense, same shape as the "pattern shows" clearance in the Grade 6 batch.

That leaves these two, both in ch3 connective tissue, neither in a protected
passage. The liturgical register never once reaches for an intention verb
across its 15-18 instances, which is why this ruling costs the signature device
nothing.

    python3 instruments/agency_w1.py --dry
    python3 instruments/agency_w1.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    # `means to teach` is an aim the feeling is pursuing. `has to teach` names
    # what is available in it without giving it a plan -- and `teach` is the
    # liturgical register's own verb, so the sentence lands closer to the
    # chapter's protected passages, not further from them.
    ("manuscript/ch3.md",
     "helps you know what the feeling means to teach, and what move to make next.",
     "helps you know what the feeling has to teach, and what move to make next."),

    # `kept trying to deliver` is effortful and repeated: psychology, not
    # direction. `carrying` is directional, which Grade 3 holds outright.
    # The noun is repeated rather than pronouned -- `it` could read back to
    # the not-feeling rather than the fear.
    ("manuscript/ch3.md",
     "which meant they also missed the intelligence fear kept trying to deliver.",
     "which meant they also missed the intelligence the fear was carrying."),
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
