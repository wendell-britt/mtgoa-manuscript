# -*- coding: utf-8 -*-
"""marks_ch2_t2 -- proof marks, ch2 pp.30-33, every entry changed (2026-09-09).

Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
    python3 instruments/marks_ch2_t2.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch2.md")

EDITS = [
# p.30 -- the refrain's second use and the signpost
("The world is not fine. The people trying to fix it keep running into the same problem: themselves. This chapter is the threshold map.",
 "The people trying to fix the world keep running into the same problem: themselves."),
# p.31
("Trying to seem right costs energy. Trying to seem good costs more. Run both at once and most of the attention goes to how you are landing.",
 "Trying to seem right, and then trying to seem good on top of it, spends most of your attention on how you are coming across."),
("That vigilance costs you presence, and if you cannot be present with them you cannot ally with them.",
 "That vigilance spends the presence the person in front of you needed."),
("That gap, between the people in front of you and how much of you is there to meet them, is the edge of the Forest.",
 "The Forest begins in the gap between the person in front of you and how much of you shows up to meet them."),
("Read the book, adjusted the language, listened harder after that.",
 "Read the book, swapped out the words you had been corrected on, listened harder after that."),
("Maybe, somewhere in all of it, you started holding still by default.",
 "Somewhere in all of it, you started holding still by default."),
("No one reports back. You cannot tell",
 "You cannot tell"),
("All that effort has been sitting on top of one question.\n\n",
 ""),
("or to seem like the kind of person who would? Ask it without flinching.",
 "or to seem like the kind of person who would?"),
("Your body was never appropriating anything. It is yours.",
 "Reading your own body was never appropriation."),
("Wanting to be good was never the problem. Performing it costs a great deal, and punishing yourself for falling short of the performance costs a great deal more. Run both and you are funding two expensive processes, neither of which does anything for the person in front of you.",
 "Performing goodness is expensive. Punishing yourself for falling short of the performance is more expensive still. Neither bill buys anything for the person in front of you."),
# p.32
("so you can do the real work there and nowhere else.",
 "so you can do the real work there."),
("I was glad they called. Something in the reaching out mattered.",
 "I was glad they called."),
# p.33
("Something else came with it. A sensation",
 "The calls carried a second load. A sensation"),
("This produces a permanent low-grade charge that the people around you never suspect.",
 "This produces a permanent low-grade charge, invisible to the people around you."),
("and they delivered it to me, gift-wrapped as concern.",
 "and they handed it to me as concern."),
("What the anger produced first was not the book; Chapter 9 tells that part.",
 "What the anger produced first was not the book."),
]

def main():
    t = io.open(P, encoding="utf-8").read()
    for old, new in EDITS:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("EDIT matched %d times (need 1): %r\n" % (c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2 tranche 2: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
