# -*- coding: utf-8 -*-
"""marks_ch3_t6 -- proof marks, ch3 pp.54-59 (two marginalia blocks and the body through
the Voss sessions), every entry changed (2026-09-09).

Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
The p.56 "We were there eleven days." was logged [?] (low-confidence read) and is left alone.
    python3 instruments/marks_ch3_t6.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# p.54 marginalia (Maera)
("She\n> stopped in her fourth year here and has described the time since as the first she could hear\n> anything at all.",
 "She\n> stopped in her fourth year here. She describes the time since as the first she could hear\n> anything at all."),
# p.55 marginalia (Oreve)
("We put in once at Oreve, which is a port and a poor one — the moorings were rotten and the\n> harbourmaster kept his ledgers in his head and got them wrong.",
 "We put in once at Oreve, a poor port. The moorings were rotten, and the\n> harbourmaster kept his ledgers in his head, where they were wrong."),
# p.55 body
("Inside it. One of them. The Shaman served",
 "The Shaman served"),
("Doing something required making a decision, and decisions, the Challenger said, couldn't wait for everyone to process their feelings.",
 "Doing something required making a decision. Decisions, the Challenger said, couldn't wait for everyone to process their feelings."),
# p.56
("The Shaman wasn't banished with words. It was slower than that. It was the Shaman",
 "The Shaman wasn't banished with words. It was the Shaman"),
("They also got colder.",
 "Colder, too."),
("**The Shaman means: somebody said the unsaid charge, and it landed.**",
 "**The Shaman means: somebody said the unsaid charge to the person it was about.**"),
# p.57
("call you cold. Neither scores you wrong. They score you in another dictionary.",
 "call you cold. Each is scoring you in a different dictionary."),
# p.58
("The villagers did all of this on purpose. Because the Challenger was right:",
 "The villagers did this deliberately, because the Challenger was right:"),
("So the villagers made a choice: efficiency over wisdom.",
 "They chose efficiency over wisdom."),
("They called the pattern efficiency, and the pattern starved them.",
 "They called the pattern efficiency. The pattern starved them."),
# p.59 -- the Voss sessions
("I recorded contempt in the man at the head of the table. Grief, four days old. I did not have that until the funeral.",
 "I wrote down contempt in the man at the head of the table. Grief, four days old. I did not feel the grief until the funeral."),
("Three years of nothing, entered in my own hand, four hundred times.",
 "Three years of nothing, in my own handwriting, four hundred entries."),
("by somebody who had got it wrong in front of witnesses, and the only instrument it could reach was mine.",
 "by somebody who had got it wrong in front of witnesses. The only instrument it could reach was mine."),
("The reading came back and it is better than it was.",
 "The reading came back better than it was."),
(" That part is real, and it matters.",
 ""),
("That is the Shaman's practice with a governor on it, one installed by instructions that meant to teach you not to harm people and accidentally taught you to distrust your own read.",
 "The Shaman's practice is running under a governor, installed by instructions that meant to teach you not to harm people and taught you instead to distrust what your body had read."),
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
    print("ch3 tranche 6: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
