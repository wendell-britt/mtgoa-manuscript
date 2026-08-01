# -*- coding: utf-8 -*-
"""
The four appendix sites the remove-app inventory missed. DL-20 blocker one.

`SPEC_REMOVE_APP_V1` §2 inventoried three jobs and named Appendix B ×3. Running
`shipcheck.py -v` after the ruling-5 pass surfaced four more that no draft or spec listed,
three of them the framing sentences whose routing tails ruling 5 had already cut. Cutting
a tail and leaving the sentence that explains the tail is a half-finished sweep, and it is
exactly what the inventory's site count could not catch.

  APPENDIX_B:17   "you open the app and capture what moved" -> "you capture what moved"
  APPENDIX_B:189  "routes to the app for capture" -> "ends in a capture", which is
                  ruling 5's own phrasing
  APPENDIX_F:77   "Open bars-engine → Polarity Map." cut. The capture instruction around
                  it is complete without a destination.

**The glossary entry is a different kind and gets a different fix.** `APPENDIX_C:16`
defined bars-engine as *"The app that implements the MTGOA practice: BAR captures ...
route to oracle card unlocks and track the player's domain distribution over time."* Every
clause after the colon is a feature of software that is not shipping. But the term itself
still appears eleven times in ch9, where five of those are Wendell's Founder-move worked
example and the ruling on them is his. So the entry stays and stops promising features:
it now says what the book actually shows.

**If ch9's bars-engine goes, this entry goes with it.** Recorded here so the dependency is
not rediscovered later.

Measured, 130 words to 105. Every counter under the line before and after; the small rises
in waste, zombie and empty are the shorter denominator, not new defects.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APX = os.path.join(HERE, os.pardir, "appendices")

E = [
    ("APPENDIX_B_QUESTS_CAMPAIGNS.md",
     "Every quest ends the same way: you open the app and capture what moved.",
     "Every quest ends the same way: you capture what moved."),

    ("APPENDIX_B_QUESTS_CAMPAIGNS.md",
     "*Every quest and campaign routes to the app for capture.",
     "*Every quest and campaign ends in a capture."),

    ("APPENDIX_F_POLARITY_MAP.md",
     " Open bars-engine → Polarity Map.",
     ""),

    ("APPENDIX_C_KEY_TERMS.md",
     "**Bars-engine** — The app that implements the MTGOA practice: BAR captures "
     "(behavior, affect, what's clearer) route to oracle card unlocks and track the "
     "player's domain distribution over time.",
     "**Bars-engine** — The game system Wendell built from this practice. Chapter 9 "
     "uses it as the worked example of a Founder move."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(APX, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:56]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(APX, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
