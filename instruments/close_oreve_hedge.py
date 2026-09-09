# -*- coding: utf-8 -*-
"""close_oreve_hedge -- DL-88. The Oreve note ends instead of commenting on itself.

Wendell, 2026-09-09, closing the one mark that could not be ruled from the mark: *"the real defect
is the closing hedge 'I have thought about it more than is useful' commenting on the anecdote
instead of ending it."*

**This resolves the `[?]` and it names which of two readings was right.** The ledger offered the
invented particular -- *eleven days* -- or the hedge. The particular stays and earns its place:
eleven days against a practice so old that a clerk cannot date it is the note's whole point. The
hedge was the annotator telling the reader how much the story mattered to him rather than letting
it land.

**Pattern 4 in PROOF_MARKS_CH2_CH3, the hedges**, alongside *"I have guessed wrong in both
directions"*, *"and I could be wrong"*, *"I have not solved it. I teach here anyway."* This is the
first of the seven mark patterns Wendell has ruled on directly, which is why the pattern table
spec built alongside it opens on this one.

The replacement is an observation about the world rather than about the annotator's own mental
process -- the distinction being enforced all day. Pure deletion was the alternative and is
recorded here: *"We were there eleven days."* alone lands, and it leaves the paragraph thin.

    python3 instruments/close_oreve_hedge.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard

CLAIM = "DL-88"
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

OLD = "*We were there eleven days. I have thought about it more than is useful.*"
NEW = "*We were there eleven days. I have not seen it anywhere since.*"
EDITS = [(OLD, NEW)]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)
    before = io.open(P, encoding="utf-8").read()
    if before.count(OLD) != 1:
        sys.stderr.write("REFUSED: span matched %d times (need 1).\n" % before.count(OLD))
        sys.exit(2)
    after = before.replace(OLD, NEW, 1)
    if norm(before.replace(OLD, "")) != norm(after.replace(NEW, "")):
        sys.stderr.write("REFUSED: prose changed outside the declared span.\n"); sys.exit(3)
    if OLD in after or NEW not in after:
        sys.stderr.write("REFUSED: the declared edit did not take.\n"); sys.exit(4)
    io.open(P, "w", encoding="utf-8").write(after)
    print("Oreve hedge closed: 1 of 1")
    print("occurrences of the hedge remaining: %d (want 0)" % after.count(OLD))


if __name__ == "__main__":
    main()
