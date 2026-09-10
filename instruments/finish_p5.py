# -*- coding: utf-8 -*-
"""finish_p5 -- DL-101. The P5 tail: buys, metabolize, the last land, and `shows` -> `shows up`.

Wendell, 2026-09-10: *"'shows in the body' shows up"* and *"continue with the p5s remaining 10."*

**The first correction is mine from an hour earlier.** DL-100 replaced *"where a feeling landed in
the body"* with *"shows in the body"*, and `show` without the particle is the same clipped
register the whole day has been about. Four sites, all mine, all fixed.

**Two survive P5 and both are the same licence as the skeeball ball**: `ch1:123`, *"trade them for
a prize"*, an actual counter traded at an actual redemption desk; and `ch5:253`, *"the land was not
returned"*, the noun.

**I nearly kept four more and did not, because keeping a class and arguing for it is the mistake
of the day.** `buys` in ch1 sits inside the arcade chapter's sustained economy conceit -- *"you
have been paying it off"* is two sentences later -- and `costs you an hour and buys you nothing`
pairs cost with purchase deliberately. Both readings are available and neither was asked for.
**DL-95 kept fifteen `read`s on an argument like that and DL-98/99 kept 26 `land`s on another. Both
were overruled the same day.** So: changed.

    python3 instruments/finish_p5.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p5_edits4 import E

CLAIM = "DL-101"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
EDITS = [(os.path.join(ROOT, f), o, n) for f, o, n in E]


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
    print("P5 tail applied: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))


if __name__ == "__main__":
    main()
