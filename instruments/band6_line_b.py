# -*- coding: utf-8 -*-
"""
Band 6, LINE — second pass. Six more, ch1 and ch2.

  CH1 L1  "the payoff" had no findable antecedent. The paragraph above it ends on "the
          shadow guarding its stash", which is the thing being described, so the noun
          points at it now.
  CH1 L2  "never sees a point of it" is malformed inside a payout metaphor. The Arcade
          runs on tokens and payouts, so the word is penny.
  CH1 L4  "how to win and succeed" is a doublet where one word does the work.
  CH1 L5  Yu-kai Chou introduced twice with the same formula, "spent a decade mapping",
          thirty-two lines apart. The second keeps the research and drops the formula.
  CH1 L6  "quieter" is the banned-word family and the gate cannot see it. See below.
  CH2 L5  a broad "it" plus a redundant tail: "When you see it as pattern, the incidents
          don't look the same after that."

**An instrument gap, reported rather than closed.** `gate.py` bans `\\bquiet(ly)?\\b`,
which matches *quiet* and *quietly* and misses *quieter* and *quietest*. Two sites carry
the comparative: `ch1:48`, which is this finding, and `ch5:78` -- "The Regent arrived with
something quieter and harder to see" -- where the word is doing real comparative work and
may well be right.

Widening the pattern is a one-line change and would fail the gate on ch5:78 immediately.
That is a ruling, not a fix, so the pattern is left alone and the second site is left
alone with it.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch1.md",
     "Look at what the payoff really buys you.",
     "Look at what that stash really buys you."),

    ("ch1.md", "never sees a point of it.", "never sees a penny of it."),

    ("ch1.md",
     "even while you're still figuring out how to win and succeed.",
     "even while you're still figuring out how to win."),

    ("ch1.md",
     "Yu-kai Chou spent a decade mapping what actually keeps a human being playing:",
     "Chou's decade of mapping answers a second question:"),

    ("ch1.md",
     "whether the vocabulary we have built does the same quieter thing: a set of "
     "conditions to meet before the real help arrives.",
     "whether the vocabulary we have built does the same thing less visibly: a set of "
     "conditions to meet before the real help arrives."),

    ("ch2.md",
     "When you see it as pattern, the incidents don't look the same after that.",
     "When you see the pattern, the incidents stop looking the same."),
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
