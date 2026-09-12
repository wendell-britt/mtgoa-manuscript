# -*- coding: utf-8 -*-
"""sweep_p5_land -- DL-98, tranche 1. The marked shape: `land` plus a manner word.

Wendell, 2026-09-10: *"sweep the 59 P5 sites"*, then *"all of it."*

P5's mark, 2026-09-02: *"'lands warm' -- what the fuck does landing warm mean? Land is another
one of those nothing words that gets overused."*

**29 of the 59 are that exact shape**: `land` handed a manner word that says nothing about what
happened. *lands wrong*, *lands clean*, *landed badly*, *lands correctly*, *lands simpler*. Each
one is replaced by what actually occurs -- the sentence goes badly, the line is correct, the
truth is heard as care, the person takes it hard.

**Not in this tranche, and kept:** 11 locative uses where the image is live and carries meaning
(*"a decision lands on the person with the least power to absorb it"*, *"the cost lands on the
people the design is for"*); the literal skeeball (*"the machine reads where the ball landed"*);
and two false positives the instrument cannot help -- *"the land was not returned"* is the noun,
*"trade them for a prize"* is an actual arcade counter.

**Tranche 2 is `sweep_p5_land_2.py`**, the reception sense across the rest of the book. The row
is 59 sites and the word is 103, so sweeping the row alone would have left 44 standing -- which
is the mistake DL-95 made with `read` and DL-96 had to undo.

One span sits inside a framed block in ch8, so `compile.py --verify` goes stale and `--regen`
runs after. That is DL-89 working.

    python3 instruments/sweep_p5_land.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p5_edits import E

CLAIM = "DL-98"
HERE = os.path.dirname(os.path.abspath(__file__))
EDITS = [(os.path.join(HERE, os.pardir, "manuscript", f), o, n) for f, o, n in E]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)
    staged = {}
    for path in dict.fromkeys(p for p, _, _ in EDITS):
        staged[path] = io.open(path, encoding="utf-8").read()
    for path, old, new in EDITS:
        if staged[path].count(old) != 1:
            sys.stderr.write("REFUSED: span matched %d times (need 1) in %s.\n  %r\n"
                             % (staged[path].count(old), os.path.basename(path), old[:70]))
            sys.exit(2)
        staged[path] = staged[path].replace(old, new, 1)
    for path, text in staged.items():
        b, a = io.open(path, encoding="utf-8").read(), text
        for p, old, new in EDITS:
            if p == path:
                b = b.replace(old, "", 1); a = a.replace(new, "", 1)
        if norm(b) != norm(a):
            sys.stderr.write("REFUSED: prose changed outside the declared spans in %s.\n"
                             % os.path.basename(path)); sys.exit(3)
    for path, old, new in EDITS:
        if old in staged[path] or new not in staged[path]:
            sys.stderr.write("REFUSED: a declared edit did not take.\n  %r\n" % old[:70])
            sys.exit(4)
    for path, text in staged.items():
        io.open(path, "w", encoding="utf-8").write(text)
    print("P5 tranche 1 applied: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))


if __name__ == "__main__":
    main()
