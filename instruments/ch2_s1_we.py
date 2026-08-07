# -*- coding: utf-8 -*-
"""ch2_s1_we.py — the unearned `we` out of ch2 Section 1's back half.

Ruled by Wendell 2026-08-02: "clean up the remaining we in Section 1", after the front
half went third person and left a visible seam. His original finding, 2026-08-02: *"We've
also created this we that feels a bit unearned."*

Six sites carried 13 tokens. **Five are edited here and one is deliberately left**, because
`ch2:39` is inside the approved testimony — *"Most of what **we** were calling shamanism was
presence, and **we** read the research next to the practice"* — where the `we` is Wendell
and his teacher, two named people who were in the same building. That one is earned, and
it is the contrast that makes the other five read as unearned.

The rule the five broke: a claim about the field's method has no business arriving as a
confession, because the `we` quietly recruits the reader into a group she never joined and
buys agreement she has not given. `SPEC_EDITORIAL_OS_INTEGRATION` §4 lists *moralizing
without self-deprecation* under what would betray this voice, and a first-person plural is
how moralizing gets in wearing company clothes.

One thing gained on the way: `ch2:57` had *"capacities we were never taught to build… we
weren't told the work starts"* — the exact shape of `gate.py`'s A0 counter
(`you (were|was) (taught|told)`), which fires on the second person and not the first. Going
third person means the sentence has to say who is not building and who is not telling, and
the replacement names the curriculum instead of an absent teacher.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = [
    ("Here's why: we're trying to navigate terrain we haven't mapped. We're trying to be "
     "allies in a world that demands capacities we were never taught to build. We don't "
     "build them because we weren't told the work starts somewhere deeper than "
     "performative showing up.",

     "The terrain here has no map. Allyship asks for capacities no training builds, and no "
     "training admits it. The curriculum opens where the work becomes visible, which is a "
     "long way past where it starts."),

    ("The world is not fine. The way we've been trying to fix it is not fine either.",
     "The world is not fine. The method for fixing it is not fine either."),

    ("Every time we hit the wall, we have a choice: turn back, or go through.",
     "Everybody who hits that wall gets the same choice: turn back, or go through."),

    ("This is the failure mode we're building a way out of.",
     "That is the failure mode you are here to get out of."),

    ("Here's what we know now:",
     "So here is the rule:"),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
