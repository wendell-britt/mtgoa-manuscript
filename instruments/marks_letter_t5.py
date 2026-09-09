# -*- coding: utf-8 -*-
"""marks_letter_t5 -- proof marks, pp.51-54: the Letter to the Reader and the School of the
Body admissions box, every entry changed (2026-09-09).

Both live in hard-wrapped blockquotes, so each old string matches across its "\n> " breaks.
Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
    python3 instruments/marks_letter_t5.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LETTER = os.path.join(HERE, os.pardir, "front_matter", "headmasters_letter.md")
CH3 = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

LETTER_EDITS = [
("I am glad this reached you, and I would rather you were not disappointed in us for the wrong\n> reasons.",
 "I am glad this reached you. I would rather you were not disappointed in us for the wrong\n> reasons."),
("particular when they need something, and it is rarely where you are standing.",
 "particular when they need something, rarely where you are standing."),
("Those are five different kinds\n> of trouble and help shaped for one of them does very little in another, which is the whole",
 "Those are five different kinds\n> of trouble. Help shaped for one of them does very little in another, which is the whole"),
("Two ways through, and I have watched both work.",
 "Two ways through."),
("which is what most students come for, and it is not nothing.",
 "which is what most students come for."),
("which\n> is rarer and is not better.",
 "which\n> is rarer."),
("Nobody here will tell you which you are for, and I have guessed\n> wrong in both directions.",
 "Nobody here will tell you which you are for."),
("The schools are in an order, and the order is there to protect the people you will be\n> practising on.",
 "The schools are in an order that protects the people you will be\n> practising on."),
("when the moment comes, and it will land on the nearest available person rather than the one who\n> needed it.",
 "when the moment comes, at the nearest available person rather than the one who\n> needed it."),
("You are taught one move, and the school will\n> decline to teach you a second",
 "You are taught one move. The school will\n> decline to teach you a second"),
("and then they are gone, and whoever they were helping is left\n> holding something half done.",
 "and then they are gone. Whoever they were helping is left\n> holding something half done."),
("in\n> front of the same faces, and none of the six has found a kinder way to teach anyone to read\n> anything accurately.",
 "in\n> front of the same faces. None of the six has found a kinder way to teach anyone to read\n> anything accurately."),
("your move is theirs, and we do not record it as your result.",
 "your move is theirs. We do not record it as your result."),
("starts being in it, and I\n> have never once been able to predict which week it will be for which person, which is most of\n> why I am still here.",
 "starts being in it, which is most of\n> why I am still here."),
]

HANDBOOK_EDITS = [
("I look for two qualities and will not take one without the other.",
 "I look for two qualities, together or not at all."),
("and noticed the holding in, and minded it afterward.",
 "and noticed the holding in enough to mind it afterward."),
("It sounds small to me as well, and I have watched what follows from\n> it:",
 "It sounds small to me as well. I have watched what follows from\n> it:"),
("I\n> keep my own errors in more detail than my successes and students find the ratio unsettling\n> for about a term.",
 "I\n> keep my own errors in more detail than my successes. Students find the ratio unsettling\n> for about a term."),
("Two responses are possible and\n> neither of them is mine.",
 "Two responses are possible, neither of them mine."),
(" I send more students to the\n> Pattern than I expected to.",
 ""),
]

def apply(path, edits, label):
    t = io.open(path, encoding="utf-8").read()
    for old, new in edits:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("%s: EDIT matched %d times (need 1): %r\n" % (label, c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(path, "w", encoding="utf-8").write(t)
    print("%s: %d edits applied" % (label, len(edits)))

if __name__ == "__main__":
    apply(LETTER, LETTER_EDITS, "letter")
    apply(CH3, HANDBOOK_EDITS, "ch3 handbook")
