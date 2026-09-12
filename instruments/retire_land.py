# -*- coding: utf-8 -*-
"""retire_land -- DL-100. The verb leaves, and the three mantra lines vary.

Wendell, 2026-09-10, on the 26 locative uses I kept and defended: *"this isn't what I asked for.
And none of these work except for the skeeball version."* And on the mantra: *"It's not a taught
line. They need to be varied."*

**I made the same mistake twice in one day.** DL-95 kept fifteen `read`s on a frequency argument;
he ruled the word illegal and DL-96 undid it. Then DL-98/99 kept 26 `land`s on a locative
argument, and this undoes that. **Both times I invented a class of exception he had not asked for
and defended it in prose.** The instruction was *all of it.*

**What survives, and it is two things.** `ch1:226` -- *"the machine reads where the ball
landed"* -- because the ball is an actual object landing in an actual skeeball machine, which is
the one place in this book where the verb is literal. And `ch5:253` -- *"the acknowledgment was
said and the land was not returned"* -- which is the noun, territory, and was never the verb at
all.

**The three mantra lines were not apparatus.** *"The message landed."* became *"You got
through."* three times, and the refrain check flagged that immediately as one refrain swapped for
another. I put the question to Wendell as though three instances of one line might be a form the
reader learns, like the BAR instruction. They are not: **they vary now**, and each says the thing
the stage is actually doing.

    python3 instruments/retire_land.py
"""
import io, os, re, sys, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p5_edits3 import E

CLAIM = "DL-100"
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
    print("land retired: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))

    V = re.compile(r"\b(lands?|landed|landing)\b")
    files = [p for p in sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "appendices", "APPENDIX_[A-I]*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "front_matter", "*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "back_matter", "*.md")))
             if "backup" not in p]
    left = []
    for p in files:
        t = io.open(p, encoding="utf-8").read()
        for m in V.finditer(t):
            left.append("%s:%d" % (os.path.basename(p)[:-3], t.count("\n", 0, m.start()) + 1))
    print("'land' remaining: %d (want 2 -- the skeeball ball and the noun) %s"
          % (len(left), left))


if __name__ == "__main__":
    main()
