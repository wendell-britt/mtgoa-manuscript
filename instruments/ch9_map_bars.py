# -*- coding: utf-8 -*-
"""
ch9:300 — the one bars-engine site inside The Map.

The handoff scopes eight sites as "inside Section 5, replaced wholesale." Measured,
seven of the eight sit in *The Walk* (`ch9:324`-513), which is the memoir the rewrite
replaces. This one sits in *The Map* (`ch9:232`-323), which is reader-facing teaching
that no ruling touches: **What the Map Doesn't Show You**, on the difference between the
terrain and the weather. The section survives whatever happens to The Walk, so its one
product reference cannot wait on that rewrite.

It is also the cheapest kind of fix. The passage runs three parallel *The moment when*
sentences and only the first names the product, so the reference leaves by deletion and
the parallel closes over the gap. Removal, not invention -- the same principle that took
the bars-engine entry out of ch9's offer list this morning. DL-20 requires it either way.

What goes with it is the clause *"something opens in them that you didn't know was
closed,"* which is a good beat. The two survivors carry the same idea: a player naming a
feeling they could not name, and the build working while the builder feels nothing. The
passage loses a sentence and not a point.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch9.md",
     " The moment when someone plays bars-engine and something opens in them that you "
     "didn't know was closed.",
     ""),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
