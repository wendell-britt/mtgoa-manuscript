# -*- coding: utf-8 -*-
"""
The five duplicate pairs, re-run through the Jordan lens.

Wendell: *"re analyze these through the lens of 'is this going to make Jordan a better
ally?' we should cut anything that's not going to do that."*

The question stops being which copy reads better and becomes whether the second copy
changes what she does. That flips two of my five recommendations.

  1  ch6, the blueprint line at 415 and 579. 415 is the teaching and it is an
     instruction: ship on a day it can still matter, because late and correct is not
     generous. 579 restates it inside the transition. She already has the instruction, so
     the restatement changes nothing she does. **Cut the restatement at 579.**

  2  ch2, "and just hums" at 111 and 368. I called this working before and the lens
     agrees for a better reason than I gave. 111 names a symptom she can feel. 368 gives
     the mechanism under it, and the repeated phrase is the hook that connects the two.
     The second copy converts something she recognises into something she can work with.
     **Keep both. Not a defect.**

  3  ch2, "nearer the center" at 344 and 374. I recommended cutting 344 as the weaker
     copy. Under the lens both are forward-pointers, and a forward-pointer is book
     navigation rather than capability. 374 at least names the Damaged Self. 344's clause
     names nothing and asks her to remember a promise. **Cut the pointer at 344, keep the
     job description it is attached to.**

  4  ch9, the goal sentence at 51 and 636. I offered to vary it. The lens says leave it:
     it is the one sentence in the chapter that tells her what to aim at, and a chapter
     opening and closing on what to aim at is doing its job. **Keep both, unchanged.**

  5  ch9, the bars-engine passage at 400 and 470. Held for Wendell. See the report: the
     lens says something sharper than "cut the duplicate" and the call is his.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # ch6 — the recap restates an instruction the reader already has. The sentence before
    # it does the recap's actual work, so the restatement comes out whole.
    ("ch6.md",
     " A blueprint delivered eighteen months after the pressure released is not "
     "generous. It is only correct.",
     ""),

    # ch2 — the job description stays; the forward-pointer goes. ch2:374 makes the same
    # promise thirty lines later and names the daemon while doing it.
    ("ch2.md",
     "It's the Protector's last resort, and you'll meet it nearer the center.",
     "It's the Protector's last resort."),
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
