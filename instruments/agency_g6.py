# -*- coding: utf-8 -*-
"""
agency_g6.py — the Grade 6 systemic block.

The C1 corollary's actual target: the book confronts reified systemic agency, it
does not accommodate it. Culture does not train, reward or punish. People do
those things, and the pattern is the name for what their doing leaves behind.

Scan found 21 candidates. Adjudicated:

  7  real defects, fixed here
  7  School-as-agent -- a CLASS DECISION, held for Wendell (see below)
  5  "the pattern shows" -- CLEARED, intransitive
  2  "a game teaches" -- CLEARED under C1, mechanism on the page

CLEARED, intransitive (ch4:531, ch5:531, ch6:400, ch8:330, ch8:564):
    "Look at the sequence, not the verdict, the only place the pattern shows."
`shows` here is intransitive -- the pattern is VISIBLE, it is not perceiving
anything. Registry lists `show` under perception because "shows you what
matters" is transitive and aimed. No agency is ascribed in these five, so C1 has
nothing to trace. This includes ch8:330, which the ch8 ledger flagged as a
liturgical lookalike; on a closer read the verb sense is wrong for that charge.

CLEARED under C1 (ch2:218, ch2:224):
    "A game teaches differently. It gives you a map, lets you make a move,
     shows you what happened, and lets you try again with better information."
The mechanism is on the page in the very next clause. That is the Token/Ticket
shape the spec holds up as correct, not the defect.

HELD for Wendell -- the School class (7 sites, ch3 x2, ch5, ch6, ch7, ch8 x2):
    "Everything the School of the Body teaches argues for keeping it calibrated."
Six in-world institutions, each with a named Head who does the teaching, so R1
is trivially available. But this is the same institutional-metonymy shape as
W-2's book/chapter, and W-2 got a narrow license rather than a blanket
conversion. Parity is a registry question and C2 reserves it.

    python3 instruments/agency_g6.py --dry
    python3 instruments/agency_g6.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    # ch1 -- culture rewards. R1. The praisers are people; name them and the
    # subject shortens rather than lengthens.
    ("manuscript/ch1.md", "R1",
     "The selflessness the movement culture rewards is the same mechanism that empties you out.",
     "The selflessness everyone praises is the same mechanism that empties you out."),

    # ch2 -- the diagnostic triad. Two of three bullets hand the verb to an
    # abstraction while the first one models the correct form. Restoring the
    # people also tightens the parallel: me -> them -> them.
    ("manuscript/ch2.md", "R1",
     "- What pattern does this group reward when things get uncertain?\n"
     "- What pattern does this system punish when someone tells the truth?",
     "- What pattern do the people here reward when things get uncertain?\n"
     "- What pattern do they punish when someone tells the truth?"),

    # ch2 -- structure trains. R6 to the reader, who is the one being trained.
    # Keeps the two-beat and the closing word.
    ("manuscript/ch2.md", "R6",
     "That structure trains performance. It does not train play.",
     "Trained that way, you perform. You do not play."),

    # ch6 -- document-speech, twice in one sentence. R2 both times.
    ("manuscript/ch6.md", "R2",
     "what the system says about itself.",
     "the system's own account of itself."),

    ("manuscript/ch6.md", "R2",
     "hold the field when the map does not tell the whole story, stay in relationship "
     "when the structure says the relationship should be working and it is not.",
     "hold the field when the map leaves out half the story, stay in relationship "
     "when the structure should be making that relationship work and it is not."),

    # Appendix A -- structure includes / structure needs.
    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md", "R6",
     "that the structure includes people who wouldn't otherwise be at the table.",
     "that people who wouldn't otherwise be at the table end up at it."),

    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md", "R2",
     "wise about what the structure needs without being in it.",
     "wise about what the structure lacks without being in it."),
]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, _op, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, _op, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, n, before[:88]))

    for path, op, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s  [%s]" % (path, op))
        print("  --  %s" % before.replace("\n", "\n      "))
        print("  ++  %s" % after.replace("\n", "\n      "))

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
