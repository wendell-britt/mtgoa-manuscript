# -*- coding: utf-8 -*-
"""
Ruling 5 — do quests end in a capture, or does the capture get a named home?

**They end in a capture. The named home already exists.**

`SPEC_REMOVE_APP_V1` §5 poses this as an open question, and the appendix answers it
without needing a decision. Every routing tail names a quest that is already the heading
of the block it sits in:

    ### Quest 1 — The Forest Walk
    ...
    3. Capture each day's gate, one line.  → app: *The Forest Walk.*

Verified mechanically before cutting: all twelve tail names appear in their own block's
heading, none is unique to the tail. So the tag was never carrying the name. It was
repeating it as a pointer.

**The ICA test decides the rest.** `SPEC_WORKBOOK_SCOPE.md:53` sets the standard: *"a
reader without a coach can complete every exercise alone."* Reading alone, she gets the
quest's name from the heading, the work from steps one and two, and a complete capture
instruction from step three. The tail added a destination she cannot reach and a name she
already had. Removing it costs her nothing and removes the one thing in the block she
could not act on.

**One stale claim goes with it.** The header carried *"Each quest routes to the app for
BAR capture. The bars-engine quest structures named below must exist before this appendix
goes to press. Coordinate before press."* `build_book.strip_provenance` already keeps that
off the printed page, so it was never a print defect, but it asserts a press dependency on
a product that is not shipping. Left in the source it would block a press that has no
reason to wait.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, os.pardir, "appendices", "APPENDIX_B_QUESTS_CAMPAIGNS.md")

TAIL = re.compile(r" → app: \*[^*]*\*")
STALE = ("**Timing dependency:** Each quest routes to the app for BAR capture. The "
         "bars-engine quest structures named below (`→ app: [Quest Name]`) must exist "
         "before this appendix goes to press. Coordinate before press.\n")


def main():
    t = io.open(P, encoding="utf-8").read()

    names = re.findall(r" → app: \*(.+?)\.?\*", t)
    heads = re.findall(r"^### (?:Quest \d+ — )?(.+)$", t, re.M)
    orphan = [n for n in names if not any(n.rstrip(".") in h for h in heads)]
    if orphan:
        print("ABORTED — these names exist only in the tag, so cutting would lose them:")
        for n in orphan:
            print("  " + n)
        return 1

    t, cut = TAIL.subn("", t)
    if STALE in t:
        t = t.replace(STALE, "", 1)
        stale = 1
    else:
        stale = 0
        print("note: the timing-dependency line did not match; left alone")

    if "--dry" not in sys.argv:
        io.open(P, "w", encoding="utf-8").write(t)
    print("%d routing tail(s) + %d stale dependency %s"
          % (cut, stale, "checked" if "--dry" in sys.argv else "cut"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
