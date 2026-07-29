# -*- coding: utf-8 -*-
"""
Register test — ch8 Section 2, one pass.

Timed experiment against the claim that a register rewrite "cannot happen by
August 1", which was asserted without measurement. Section picked for being
representative rather than easy: 1,140 words at 2.19x Igniting Joy, against a
book average of 2.13x and a ch8 average of 2.38x.

Method is Lanham throughout: find the be-verb, ask who is kicking whom, put the
doer in the subject. Deliberate figures are left alone — the "who sees
everything / who can name every game" fragment cadence, the three-beat "which
means" anaphora, "The design was elegant. The horse was not thirsty", and the
Architect/distortion parallel are all doing rhetorical work and none of them is
drift.

    python3 marginalia/compile.py --strip
    python3 instruments/reg_ch8_s2.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch8.md")

EDITS = [
# throat-clearing opener + colon reveal, both on the skill's list
("""Here's what happened after the Sage stopped naming things: the village didn't stop playing games.

It just stopped knowing which ones it was playing.""",
 """After the Sage stopped naming things, the village kept playing games.

It stopped knowing which ones."""),

# "The capacity ... was gone" — nominalization propped up by a be-verb
("""The capacity to name which game the village was stuck in was gone, and without it, every game started to feel like every other game.""",
 """Nobody could name which game the village had got stuck in, and every game began to feel like every other game."""),

# "This is what the village does without the Sage:" — copula frame + colon
("""This is what the village does without the Sage: it plays all the games at once, confused about which one it is in.""",
 """Without the Sage, the village plays every game at once and loses track of which one it occupies."""),

# "This is what happens when" — the frame carries no action
("""This is what happens when the village keeps the Sage's vocabulary without the Sage's practice.""",
 """The village kept the Sage's vocabulary and dropped the practice."""),

# "The trap is specific:" — copula plus colon reveal
("""The trap is specific: seeing becomes a way to avoid being in the game.""",
 """The trap works one way. Seeing becomes a way to avoid being in the game."""),

# "What never gets named is that" — a frame with the verb buried in it
("""What never gets named is that the competition is real and somebody is losing.""",
 """Nobody names the obvious. The competition runs for real, and somebody loses it."""),

# gerund subject + "means" doing the work a verb should do
("""Selecting for the most wounded as the most credible means the people who have done the work of metabolizing their pain become less visible.""",
 """When the most wounded reads as the most credible, the people who have metabolized their pain go quiet."""),

# passive inside the test line; the test convention itself stays
("""The test: where pain is being performed, does the Sage notice who isn't speaking?""",
 """The test: where pain gets performed, does the Sage notice who isn't speaking?"""),

# "This is the distortion's particular cruelty:" — copula + colon
("""This is the distortion's particular cruelty: solving the wrong problem with the right intentions.""",
 """Here the distortion turns cruel. It solves the wrong problem with the right intentions."""),

# two copulas in one sentence, and the second one only repeats the first
("""The gap between helpful and present is enormous, and it is the gap the distortion lives in.""",
 """The gap between helpful and present runs wide, and the distortion lives in it."""),

# "it is confused" + "the answer is simple:" — two frames, one colon
("""Then it is confused about why the design didn't work, when the answer is simple: the horse wasn't thirsty.""",
 """Then it wonders why the design didn't work. The horse wasn't thirsty."""),

# "What's actually happening is" — frame; and "The cost is the same:" — copula + colon
("""What's actually happening is subtler than misdesign. The Sage is projecting their own vantage onto people who aren't standing there. The cost is the same: the system fails because the people inside it don't behave the way the system requires.""",
 """The failure runs subtler than misdesign. The Sage projects their own vantage onto people who aren't standing there. The cost lands the same way. The system fails because the people inside it don't behave the way the system requires."""),

# "What's missing is" — frame
("""What's missing is the first move: *which game is this, actually?*""",
 """One move is missing, and it comes first: *which game is this, actually?*"""),

# "is what happens when" again
("""The Sage in distortion is what happens when you get good at the vocabulary without doing the practice — when you learn to name the games without learning to put them down.""",
 """The Sage in distortion appears when you get good at the vocabulary without doing the practice — when you learn to name the games without learning to put them down."""),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, b) in enumerate(EDITS, 1):
        n = t.count(a)
        if n != 1:
            print("ABORT #%d: %d matches for %r" % (i, n, a[:64]))
            return 1
        t = t.replace(a, b, 1)
    io.open(P, "w", encoding="utf-8").write(t)
    print("applied %d edits" % len(EDITS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
