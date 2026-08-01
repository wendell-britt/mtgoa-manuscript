# -*- coding: utf-8 -*-
"""
Editorial pass, 2026-08-01 — three ch9 claim errors, five edits.

Taken from `editorial_reports/2026-07-31/CH9.md` after re-deriving every finding against
the current page. Tonight's work moved ch9 enough that the report's line numbers are all
stale and two of its eight claim errors have changed state: **C6 is already fixed** (zero
occurrences of *altar* anywhere in the manuscript) and **C4 is half fixed** (ch9 now says
*BARs* once, where the report measured zero). Re-deriving before proposing is the point
of the quoted-anchor convention.

**C3 · the WAVE's sixth beat.** Canon at `MANUSCRIPT_FILE_CANON.md:103`: *"Every stage
sequence is five beats."* ch3 teaches five. ch9 recites the WAVE four times, and at
`ch9:284` it already handles the return correctly, outside the list: *"Then you come back,
and coming back is what turns one pass into a practice."* Two sites still use the colon
form the five beats use, which makes *come back* parse as a sixth stage. The reader
problem is arithmetic she can check: the deck is five moves crossed against four domains,
and a sixth beat sends her looking for a row of cards that does not exist. Fixed by
matching ch9:284's construction, not by adding an explanation.

**C8 · six operations.** *Operation* is defined once, at `ch3:822`, and used in ch9 as
current vocabulary roughly ninety thousand words later. The report's disposition is *fix
locally* and its own note says the sentences survive without the word. The arithmetic is
untouched: five moves, four domains, six Faces, a hundred and twenty cards.

**C2 · the gate scan.** Wendell's Vulnerable Child ruling this session -- *"the vulnerable
child is the player"* -- resolved the part of C2 that mattered, and `ch2:434` now seats
her at the center as the player rather than as a daemon. Two residues were left.

The first is the count: ch2 says seven daemons, ch9 says eight gates, and nothing
reconciles them. Naming the eighth as her makes the ruling visible in the prose.

The second is not in the report and turned up on a read. The scan tells her to find *"the
Face that showed up most in your building work"* and then presents eight **daemons**. The
closing exercise of the book asks her to look for the wrong category of thing. *Took the
joystick* is ch2:432's own phrase and is what ch3's new sheet line already calls it.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # ---- C3 · the return is not a sixth beat ---------------------------------
    ("ch9.md",
     "Show up: do the next version. Then come back: notice what shifted. What you "
     "learned.",
     "Show up: do the next version. Then you come back, and notice what shifted and "
     "what you learned."),

    ("ch9.md",
     "Then come back: notice what happened, what shifted, what you learned.",
     "Then you come back, and notice what happened, what shifted, what you learned."),

    # ---- C8 · retire an operation the reader met once, 90,000 words ago -------
    ("ch9.md",
     "Five moves crossed against four domains, six operations deep.",
     "Five moves crossed against four domains, once for each of the six Faces."),

    ("ch9.md",
     "and skillful organizing, run through all six operations, one per Face.",
     "and skillful organizing, run once for each of the six Faces."),

    # ---- C2 · the eighth gate, and the category the scan asks for -------------
    ("ch9.md",
     "a gate scan. Eight gates, eight questions. One of them is live in you right now: "
     "the Face that showed up most in your building work.",
     "a gate scan. Eight gates, eight questions: the seven daemons, and then you. One of "
     "them is live in you right now, the one that took the joystick while you were "
     "building."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
