# -*- coding: utf-8 -*-
"""
Two repairs to the gate-to-daemon sweep, both caused by the sweep itself.

**ch9:474.** The sweep hit "Eight gates" inside a sentence edited earlier tonight to read
"Eight gates, eight questions: the seven daemons, and then you." Substituting produced
"Eight daemons ... the seven daemons", which contradicts itself and says daemon three
times in nine words. The count word was doing the work the colon now does, so it goes.

**ch9:296.** Recorded as a clean substitution when the sweep was proposed, and it was not.
"The map shows you where the gates stand ... how long it takes to walk through them"
survives the swap in its first clause, because *still on duty* is a guard and a guard is
what a daemon is, but you do not walk *through* a daemon. *Befriend* is ch2:556's own
verb -- "The Forest is where those daemons are met and befriended" -- and it is the
required word rather than a convenient one: "get past them" would contradict ch2:296,
"you're not here to slay" them.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch9.md",
     "a daemon scan. Eight daemons, eight questions: the seven daemons, and then you.",
     "a daemon scan. Eight questions: the seven daemons, and then you."),

    ("ch9.md",
     "It does not show you how long it takes to walk through them. It does not show you "
     "what it feels like the third time you arrive at the same daemon and discover it "
     "was still on duty.",
     "It does not show you how long it takes to befriend them. It does not show you what "
     "it feels like to meet the same daemon the third time and discover it was still on "
     "duty."),
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
