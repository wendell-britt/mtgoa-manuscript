# -*- coding: utf-8 -*-
"""
Register pass — the rest of ch8, one batch.

Throughput measurement. Section 2 took two passes for 1,145 words. This tests
whether the rest of a chapter can go in one batch instead of section by section.

Left alone deliberately: quoted questions (*Which game is this?* is a horizontal
question), the book's thesis line (Mastery is knowing which game you're playing),
the "The tell is" diagnostic convention, and the W7 definitions. A copula that
defines a term is licensed and there are many in this chapter.

    python3 marginalia/compile.py --strip
    python3 instruments/reg_ch8_rest.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch8.md")

EDITS = [
("""The Sage's gift is the seeing; the next move is the building, and that one was always going to be yours.""",
 """The Sage gives you the seeing. The building comes next, and that one was always going to be yours."""),
("""The first reading: you have the Sage's gift, and what you've been living is the Sage's exile.""",
 """Read it first as this: you have the Sage's gift, and you have been living the Sage's exile."""),
("""That's occasionally true and it is not a reason.""",
 """That happens, and it still doesn't count as a reason."""),
("""You stay present without being useful in the particular way you are capable of being useful.""",
 """You stay present without offering the particular usefulness you happen to be capable of."""),
("""There is always one more thing to work through before you're clean enough to be useful.""",
 """One more thing always waits to be worked through before you're clean enough to be useful."""),
("""The tell that a quest is alive is not enthusiasm.""",
 """A live quest does not announce itself through enthusiasm."""),
("""Here's what the village didn't know:""",
 """The village did not know this:"""),
("""Here's how it runs as a lived minute.""",
 """Run it as a lived minute."""),
("""Here's the thing nobody says about panoramic vision:""",
 """Panoramic vision is lonely, and nobody says so:"""),
("""Here's the collapse.""",
 """The collapse runs like this."""),
("""There is a large difference between the two.""",
 """The two differ enormously."""),
("""What's being described here is something else.""",
 """This describes something else."""),
("""The seeing becomes a way to be seen being wise.""",
 """Seeing turns into a way of being seen to be wise."""),
("""This is presence — because the staying is the work.""",
 """That is presence, because staying does the work."""),
("""It's answered by watching what people are actually doing rather than what they're saying.""",
 """Watch what people actually do rather than what they say, and it answers itself."""),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    applied = 0
    missing = []
    for a, b in EDITS:
        n = t.count(a)
        if n == 1:
            t = t.replace(a, b, 1); applied += 1
        else:
            missing.append((n, a[:56]))
    if missing:
        print("SKIPPED (anchor not unique):")
        for n, a in missing:
            print("  %d matches: %r" % (n, a))
    io.open(P, "w", encoding="utf-8").write(t)
    print("applied %d of %d" % (applied, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
