# -*- coding: utf-8 -*-
"""
ch5 and ch7 passive: fix the ones with a hidden doer, and name the rest as register.

Both chapters were classified once already, and the classification holds. What the counter
is measuring in them is subject matter, not carelessness:

  ch5  the Regent's material is inheritance, and inheritance vocabulary has no active
       form. `what was passed`, `was handed down`, `be received`, `be inherited`,
       `be carried`. The agent is a person who is gone, which is the chapter's thesis.
  ch7  the Diplomat's material is what happens to you inside a relational field.
       `be told`, `being seen`, `be rejected`, `been harmed`, `being converted`.

Some are load-bearing on purpose. `Ruptures that were repaired before anyone saw them`
withholds its agent because invisibility is the point. `Nothing has been received` is the
Victim's own account. `Therefore what I do next is covered` is the ledger talking, and
naming who covers it would break the sentence.

**Three sites have a doer standing in the same sentence.** Those are the defects, and they
are fixed here. The residual is measured afterwards and reported rather than tuned away,
because a register is Wendell's to rule and nobody else's.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # ch5 — the village is named inside the same sentence, as the subject of the clause
    # immediately after the colon. It did the exiling.
    ("ch5.md",
     "The Architect was exiled for a specific reason: the village mistook *seeing the "
     "system* for *not loving the people inside it.*",
     "The village exiled the Architect for a specific reason: it mistook *seeing the "
     "system* for *not loving the people inside it.*"),

    # ch5 — three sentences earlier the Challenger is named four times as the one doing
    # all of this. The two passives drop the actor mid-paragraph.
    ("ch5.md",
     "Problems that had festered for years were finally named. Long-standing violations "
     "were finally stopped.",
     "The Challenger named problems that had festered for years, and stopped violations "
     "the village had lived with for as long."),

    # ch7 — the sentence already has a subject doing the learning; the demonstrating is
    # done by the three things listed, so they can do it.
    ("ch7.md",
     "who has learned that love is demonstrated through honest stake-surfacing, timely "
     "closure, and the willingness to let the field decide what it can actually hold, "
     "rather than through infinite presence.",
     "who has learned that honest stake-surfacing, timely closure, and the willingness "
     "to let the field decide what it can actually hold demonstrate love better than "
     "infinite presence does."),
    # ch7 — Section 4 is named in the sentence and is the thing doing the working-through.
    ("ch7.md",
     "Each mode's full arc, the dissatisfaction it carries and the alchemy that "
     "transmutes it, is worked through in the five channel deep-dives in Section 4.",
     "Section 4 works each mode's full arc through in its five channel deep-dives, the "
     "dissatisfaction it carries and the alchemy that transmutes it."),
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
