# -*- coding: utf-8 -*-
"""ch4_breaks.py — the four ch4 sites R8 cannot carry.

Ruled by Wendell 2026-08-02: "do 127, 68 and 84 too", after ch4:115 landed.

These are the sites `R8_TEST_CH4.md` marks BREAKS. R8 fails on them in two distinct ways
and each needs a real sentence, which is why they were reserved out of the mechanical pass.

## ch4:127 — the worst site in the chapter, and it carries the thesis

R8 gives *"the villagers taught their people"*: a population cannot teach a subset of
itself. The failure shape is possession/self-reference.

**The fix is one phrase.** *it taught its people* → **they taught each other**. A population
cannot teach its own members, and it can absolutely teach each other — which is also more
accurate about how a norm actually spreads. R6 transmission, achieved without rebuilding
the sentence, and the three-part *That… That…* figure hanging off the opening clause
survives untouched.

## ch4:68 — a site that was never a defect, where R8 would create one

`LEDGER_CH4.md` never flagged *"The village was full of people who could feel what was
wrong."* It is not a violation: *was full of* is a state, and the village there is the
container. R8 turns the container into its own contents — *"the villagers were full of
people"* — and the test's note is the one worth keeping:

> "a defect R8 *introduces* rather than repairs… reads smoothly aloud, which makes it
> dangerous."

**It is edited anyway, and not because it was broken.** The sentence two before it —
*"The village needed that"* — is a real site and takes the plural. Leaving 68b singular
two sentences later would give the fable two different narrators inside one paragraph, and
the whole reason ch4 is a hand pass rather than a batch is that the village is one
continuous character across 110 lines.

## ch4:84 — three collectives, none of them a population

*The councils*, *the rituals*, *the stories*. R8 has no number to change on any of them, so
it never arrives. All three route to R1: name who was doing it.

The people at the councils stopped asking; they started building the rituals around the
walls; the stories they told changed. Note the third keeps `changed` on `the stories` —
that is causal-bare, the registry's most forgivable class, and attaching *they told* puts
the mechanism on the page, which is what C1 asks for rather than a subject swap for its
own sake.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch4.md"

E = [
    # 68a is a clean R8 site; 68b is not a defect. Both move so the paragraph keeps one
    # narrator. See the docstring.
    ("The village needed that. The village was full of people who could feel what was "
     "wrong but couldn't say it out loud.",
     "The villagers needed that. Plenty of them could feel what was wrong but couldn't say "
     "it out loud."),

    ("The councils stopped asking first. The rituals started referencing the Regent's walls "
     "instead of the Challenger's lines. The stories changed from",
     "The people at the councils stopped asking first. They started building the rituals "
     "around the Regent's walls instead of the Challenger's lines. The stories they told "
     "changed from"),

    ("The village never realized it had traded the capacity to draw lines for the comfort "
     "of not having to. That every time it chose the facilitated conversation over the "
     "clean no, it taught its people that the clean no no longer belonged to them. That "
     "the Challenger's gift (the willingness to be unwelcome in service of what is true) "
     "was draining away, not just from the village, but from the village's *capacity to "
     "even recognize* when the moment called for it.",

     "The villagers never realized they had traded the capacity to draw lines for the "
     "comfort of not having to. That every time they chose the facilitated conversation "
     "over the clean no, they taught each other that the clean no no longer belonged to "
     "them. That the Challenger's gift (the willingness to be unwelcome in service of what "
     "is true) was draining away, not just from the village, but from their *capacity to "
     "even recognize* when the moment called for it."),
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
    print("ch4.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
