# -*- coding: utf-8 -*-
"""revert_p3 -- DL-105. DL-103 is reverted. The pointers come back.

Wendell, 2026-09-10, on the P3 sweep: *"honestly I'm ok with the book announcing its own
structure so long as the pointers are true. This might've been too aggressive a violation.
Everything is more abstract."*

**He is right and the criterion he gives is better than the rule I applied.** I read P3 as *the
book must not narrate its own structure* and swept on that. The result reads worse in exactly the
way he names: taking out the referent leaves the sentence floating.

    So Chapter 3 does two jobs.          ->  Two jobs, then.
    What this chapter trains is clarity  ->  The training is clarity
    this chapter is unusual in the book  ->  you are fluent in one of them

**Each of those replaced a thing with a nothing.** *Chapter 3* is a specific object; *then* is
not. *This chapter* is a place; *the training* is an abstraction. **The sweep that was supposed to
remove abstraction added it**, which is the fourth time today a rule of mine has been the wrong
rule and the first time one made the prose worse rather than merely incomplete.

**What the row actually is, restated on his criterion: a pointer that is not true.** Not a pointer.
*"Chapter 3 gives that exchange a name and a form"* is a claim that can be checked against ch3, and
it is either right or it is not. That is a different and better job, and it needs an instrument
rather than a sweep.

**TWO CHANGES DO NOT COME BACK, because neither was a signpost defect.** *"Every move in this
chapter is an instrument for making that sentence true"* stood word-for-word in ch7 and ch8; the
duplication was a P6 finding wearing P3's clothes. ch7 keeps the original sentence and **ch8 now
reads "That sentence is what every move in this chapter is for"** -- same pointer, same claim,
different shape. And `xref.py`'s widened search stays: `copyright.md` naming Appendix G twice was
always a real route and the check was under-counting.

    python3 instruments/revert_p3.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p3_revert import E

CLAIM = "DL-105"
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
        # A revert restores text that CONTAINS what it replaces -- "I name their source when they
        # arrive a few pages on." is a prefix of that sentence plus the pointer that follows it.
        # The usual "old must be absent" half is meaningless there and would refuse every
        # restoration; where old is inside new, only the "new is present" half can be asserted.
        if new not in staged[path] or (old not in new and old in staged[path]):
            sys.stderr.write("REFUSED: a declared edit did not take.\n  %r\n" % old[:70])
            sys.exit(4)
    for path, text in staged.items():
        io.open(path, "w", encoding="utf-8").write(text)
    print("P3 reverted: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))


if __name__ == "__main__":
    main()
