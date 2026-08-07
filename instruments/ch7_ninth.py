# -*- coding: utf-8 -*-
"""
ch7_ninth.py — the ninth field site, the one held back from the eight.

    was  said once, to the field rather than about it, and then the field takes
         its turn.
    now  said once, to the field rather than about it, and then the others take
         their turn.

Taking a turn is participating in an exchange, which is the same high-order act
as asking or answering, and the field is a low-order exterior phenomenon.
Invisible to the recall net, because `take` appears in no lemma list at any
grade -- this one was caught by reading the passage the speech sites sit in, and
then held back because it was not among the eight approved.

`the others` rather than the drafted `they`. The drafted version read "to the
field rather than about it, and then they take theirs", which puts `it` and
`they` in adjacent clauses pointing at the same referent -- the field as
addressee, then the people in it as actors. That wobble is the same
dangling-referent fault the earlier passes kept catching, and it is avoidable
here for nothing: `the others` is the same seven words as the original, names
people outright, and keeps the turn-taking image the sentence was built on.

The passage now runs clean end to end: you speak once, the others take their
turn, silence, and then whatever they do with it. Three sentences later the
`they` that this fix avoided arrives with a proper antecedent already standing.

    python3 instruments/ch7_ninth.py --dry
    python3 instruments/ch7_ninth.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
CH7 = "manuscript/ch7.md"

EDITS = [
    ("and then the field takes its turn.",
     "and then the others take their turn."),
]


def main():
    dry = "--dry" in sys.argv
    full = os.path.join(ROOT, CH7)
    text = io.open(full, encoding="utf-8").read()

    for before, _a in EDITS:
        n = text.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (n, before[:96]))

    for before, after in EDITS:
        text = text.replace(before, after, 1)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edit verified, nothing written." % len(EDITS))
        return 0
    io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %s, %d edit." % (CH7, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
