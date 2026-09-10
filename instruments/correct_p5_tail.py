# -*- coding: utf-8 -*-
"""correct_p5_tail -- DL-102. Wendell's five corrections to DL-101, two of them restorations.

  1. *"I think neither bill pays for anything is more correct"* -- I had written *does anything*,
     which drops the money the sentence is about. The passage is two bills, priced.
  2. *"keep metabolized"* -- ch2's demon.
  3. *"keep metabolize"* -- Appendix E's 3-2-1.
  4. *"alchemized poignance emerges. - it becomes doesn't take into account that work takes place
     in the process"*
  5. *"people who have worked through their pain"* -- I had inverted the particle.

**METABOLIZE STAYS, AND THAT REVERSES DL-97.** I built a BORROWED tier in `light_verb.py`
specifically for it, on the reasoning that a verb lifted from chemistry and run on a feeling is a
wrong verb rather than a weak one. **Wendell has now ruled the opposite twice in one message.**
The tier's other work stands -- it was one of four causes of that instrument's hole -- but its
only vocabulary is now a word the book keeps on purpose. Recorded rather than deleted: see
DL-102's entry for what happens to the tier.

**And number 4 is the correction that is about meaning rather than diction.** *"it becomes"*
describes a state change with nobody doing anything. **Alchemy is work**, and the book is named
for it. *"Alchemized, Poignance emerges"* puts the labour back in the sentence.

    python3 instruments/correct_p5_tail.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p5_edits5 import E

CLAIM = "DL-102"
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
    print("P5 tail corrected: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))


if __name__ == "__main__":
    main()
