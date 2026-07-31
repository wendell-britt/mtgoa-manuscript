# -*- coding: utf-8 -*-
"""
Band 4, VERIFY: eight claims that needed checking rather than fixing.

Checked. Five close, two get an edit, one cannot be settled in this container.

  CH3 C4  CLOSED, false positive. *The Courage to Be Disliked* is quoted at ch3:264 and
          the finding said it appears in no source appendix. It does:
          `appendices/ON_THE_SHOULDERS_OF.md` carries it.

  CH6 C4  CLOSED. The finding was that "an engineering fact rather than a metaphor" is
          conceded twenty lines later. There is no later concession in the current text;
          a search of ch6 for `not a metaphor`, `as metaphor` and `the metaphor` returns
          nothing after this line. The prose it contradicted has moved or gone. The
          sentence is the chapter's own framing rather than a citable claim.

  CH2 C6  CLOSED as out of scope for a body edit. The Elliott attribution being broader
          in the chapter than on the credits page is a credits-page question, and the
          credits page is Wendell's.

  CH2 C7 / CH4 C6  CLOSED to a single ruling that is Wendell's, not a verification: Egan
          is characterised two ways in two chapters, and choosing which stands is an
          editorial call about what Egan is for in this book. Moved to the report.

  CH1 C8  CANNOT VERIFY HERE. Gorski's mechanism is stated as settled causation and
          `sources/` is gitignored and absent from this container, so the underlying
          claim cannot be checked. Recommendation recorded in the report rather than
          guessed at. No edit.

Two edits:

  CH6 C3  "the highest desertion rate" is statistic-shaped and has no source. The claim
          underneath it is true to the chapter and does not need a number: Hand Off is
          where the Architect most often walks away. Restated without the statistic.

  CH9 C8  "six operations" is used twice in ch9 for the six Faces. The term is defined
          once, at ch3:858, six chapters earlier, inside an aside. First use in ch9 now
          names what it means.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch6.md",
     "Hand Off also carries the highest desertion rate, and workload has nothing to do "
     "with it.",
     "Hand Off is also where the Architect most often walks away, and workload has "
     "nothing to do with it."),

    ("ch9.md",
     "run through all six operations.",
     "run through all six operations, one per Face."),
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
