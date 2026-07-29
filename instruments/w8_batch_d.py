# -*- coding: utf-8 -*-
"""
W8 batch D — the comma-tail "which is" appositives.

The heaviest single finding here is a tic rather than a grammar fault: **"which
is the point"** closes five sentences across ch4 and ch5. Each replacement is
deliberately a different shape, so the fix does not install a new formula the
way the W7 synthesis pass did before the voiced pass caught it.

Left standing:

  · ch6's *Metal, which is fear / Water, which is sadness / Fire, which is
    anger* — three parallel definitional glosses. That is the figure, and
    breaking one of the three would break it.
  · ch8's *I run differently, which is why I can see this* — quoted speech.
  · the ch3 hit, which is a BAR-grid table row and not prose at all.

    python3 instruments/w8_batch_d.py
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
"ch4.md": [
("The contraction attempts to know in advance, which cannot be done, which is why the fear does not resolve by thinking harder.",
 "The contraction attempts to know in advance. Nothing can be known in advance, so no amount of thinking harder resolves the fear."),
("Exit fails differently from Stand, which is why the sequence keeps them apart.",
 "Exit fails differently from Stand, so the sequence keeps them apart."),
("It cannot answer the other one, which is the point.",
 "It cannot answer the other one. That limit is the point."),
("For a Challenger the dread usually arrives first, which is a good sign and a hard one.",
 "For a Challenger the dread usually arrives first. Good sign, hard one."),
("It is the most defensible myth in the book, which is exactly what makes it durable.",
 "It is the most defensible myth in the book, and its defensibility is what makes it durable."),
("Force ↔ Restraint is the axis all of it sits on, which is why the chapter gave you a polarity rather than a rule.",
 "Force ↔ Restraint is the axis all of it sits on, so the chapter gave you a polarity rather than a rule."),
],
"ch5.md": [
("No version of it costs nothing, which is precisely why it gets folded into the tending,",
 "No version of it costs nothing. That is precisely why it gets folded into the tending,"),
("and starting it costs something, which is the whole point.",
 "and starting it costs something. The cost is how you know it started."),
("The cost is generational, which is why it takes so long to surface.",
 "The cost is generational, so it takes a long time to surface."),
("It is not enough for the other one, which is the point.",
 "It is not enough for the other one, and it was never meant to be."),
("Their version will differ from yours, which is the point.",
 "Their version will differ from yours. Let it."),
("For a Regent the dread usually concerns becoming unnecessary, which is the point.",
 "For a Regent the dread usually concerns becoming unnecessary, and that is the dread to trust."),
],
"ch6.md": [
("notice what the Strategist runs on — Fire, which is anger, resolving to triumph.",
 "notice what the Strategist runs on: Fire, anger, resolving to triumph."),
],
}

PHRASES = {
    # no-ai-slop, banned phrases. Three in 97,000 words, so the list mostly
    # confirms the prose rather than correcting it.
    "ch1.md": [],
}


def main():
    staged, bad = [], []
    for name, pairs in EDITS.items():
        p = os.path.join(MS, name)
        t = io.open(p, encoding="utf-8").read()
        for a, b in pairs:
            n = t.count(a)
            if n != 1:
                bad.append((name, n, a[:64]))
            else:
                t = t.replace(a, b, 1)
        staged.append((p, t))
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for name, n, a in bad:
            print("  %s  %d matches: %r" % (name, n, a))
        return 1
    for p, t in staged:
        io.open(p, "w", encoding="utf-8").write(t)
    print("applied %d edits across %d files" % (sum(len(v) for v in EDITS.values()), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
