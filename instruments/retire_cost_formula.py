# -*- coding: utf-8 -*-
"""retire_cost_formula -- DL-94. "It cost you X" leaves the handbooks.

Wendell, 2026-09-09, on a draft where I had fixed the object of the clause: *"'It cost you being
taken for reasonable.' it cost is the problem here. Pronoun collapsing against a weak word
pointing at something almost tangible."*

Three defects in four words, and I had been repairing the fifth. **`It`** reaches back to a whole
preceding clause rather than a noun. **`cost`** is a weak verb doing metaphorical accounting.
**The object** is a half-abstraction -- *the position of the reasonable one*, *your standing as*,
*their read of you as* -- neither a thing nor an idea, and the three go soft together.

THE BOOK PROVED IT ITSELF. 24 cost lines across ch3-ch8. **23 name a status you stop having.
Exactly one names a countable thing** -- ch6:619, *"it cost you a fortnight of arguing with
people who like the arrangement"* -- and that one reads clean, same pronoun and same verb. The
formula was never the problem on its own; it collapses when the price is a status.

FIRST REPAIR REFUSED. I proposed `You gave up X` across all 24. Wendell: *"you gave up is just
replacing one tired phrase with another. We need to vary the way we say things. I do think the
grammar is now correct but we need variation."* **The grammar was the reader as subject, a real
verb, and a plain object. The uniformity was a second defect wearing the first one's clothes.**

So: 24 distinct constructions. *gave up* three times across ch3/ch5/ch7, *stopped* three times
across ch4/ch5/ch8, *lost* once, and nine other shapes used once each. **Nothing repeats inside a
chapter.** `The proof is that` stays uniform in all 24 and is the entry's anchor.

TWELVE DANGLING ANDS. Half the lines were embedded as *", and it cost you…"* hanging off a
sixty-word move clause. Wendell: *"modify the dangling ands."* All twelve become their own
sentence, so every entry now runs move / price / proof in three stops.

ONE WAS BACKWARDS AND ONLY SHOWED WHEN THEY WERE LAID SIDE BY SIDE. ch3:844, *"It cost you the
exposure of naming a need you might be wrong about."* Exposure is not what the move cost you; it
is what the move did to you. The old sentence says you lost your exposure.

    python3 instruments/retire_cost_formula.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "/tmp/claude-0")
from ruling import guard                     # FR-E1
from edits94 import E                        # the 24 declared (file, old, new) spans

CLAIM = "DL-94"
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
            sys.stderr.write("REFUSED: span matched %d times (need 1) in %s.\n  %s\n"
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
                             % os.path.basename(path))
            sys.exit(3)
    for path, old, new in EDITS:
        if old in staged[path] or new not in staged[path]:
            sys.stderr.write("REFUSED: a declared edit did not take.\n  %s\n" % old[:70])
            sys.exit(4)

    for path, text in staged.items():
        io.open(path, "w", encoding="utf-8").write(text)
    print("cost formula retired: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))

    # DL-92's standing rule: count the thing you claim to have removed.
    pat = re.compile(r"[Ii]t cost you\b[^.]{12,}\.")
    left = sum(len(pat.findall(io.open(p, encoding="utf-8").read())) for p in staged)
    ands = sum(io.open(p, encoding="utf-8").read().count(", and it cost you") for p in staged)
    print("cost-formula lines remaining: %d (want 2 -- ch4:546 and ch7:584 are quoted"
          "\n  dialogue, declared out of scope, not handbook prices)" % left)
    print("dangling ', and it cost you': %d (want 0)" % ands)


if __name__ == "__main__":
    main()
