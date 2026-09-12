# -*- coding: utf-8 -*-
"""rework_council_close -- DL-91. The two "the true one" sites in ch3's council parable.

Wendell, 2026-09-09, after I reported the site at the chapter's landing and said I would not
rewrite it without him: *"this is a dumb reason not to fix an obvious problem. weenie shit again.
Change it it doesn't make any sense out of context and I don't think it made sense IN context
either. stop inventing sacred cows to seem sophisticated."*

He is right on both counts. It is the same construction DL-87 removed from the section forty
lines below, and reporting it while leaving it standing is the deferral he has now named twice in
one day.

WHAT WAS BROKEN. `the true one` is a pro-form carrying nothing. Its nearest nouns are
*the beautiful words* and *the right words* -- plural, and the wrong thing besides. The referent
it wants, **one true sentence**, sits in the paragraph above and the paragraph below and never
inside the sentence that needs it. So the reader is told *you know which one I mean* about a noun
the sentence never gave her.

THE CENSUS, run before anything was written. `article.py` reports 11 PRO sites in ch3 and nine
are licensed: two are social roles the book is quoting, four have their noun in the same or
previous clause, two are supplied on the spot by *"two contents"*. **Only the two `the true one`
sites had none.**

THE THIRD SPAN was found while reading the second and is a different defect wearing the same
coat: *"The correct words, for all their beauty, never were"* leaves `were` with no predicate to
recover, because the clause behind it is *reached the face that could change it*. Declared here
rather than left standing, and separable -- it is EDITS[1] and can be backed out alone.

    python3 instruments/rework_council_close.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                     # FR-E1

CLAIM = "DL-91"

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

# 1 -- what she carried. The relative clause supplies the referent the pro-form never had, and
# it plants "sentence" so that "one true sentence" two paragraphs on has ground to stand on.
OLD_1 = ("So she said the beautiful words with everyone else and went home each time with the "
         "true one still sitting in her chest.")
NEW_1 = ("So she said the beautiful words with everyone else and went home each time with the "
         "sentence she had not said still sitting in her chest.")

# 2 -- the parable's close. `never were` had no predicate to recover.
OLD_2 = ("It moved because one true sentence reached the face that could change it. The correct "
         "words, for all their beauty, never were.")
NEW_2 = ("It moved because one true sentence reached the face that could change it. Three years "
         "of correct words never reached that face.")

# 3 -- the chapter's landing. The definite article goes; the noun the book already uses on both
# sides of this line arrives inside the sentence that needs it. `that everyone already half-knows`
# becomes `what`, so the two appositives are parallel under the colon.
OLD_3 = ("Allyship is saying the true one, what a part of you has already felt, that everyone "
         "already half-knows, to the face it concerns,")
NEW_3 = ("Allyship is saying one true sentence: what a part of you has already felt, what "
         "everyone already half-knows, to the face it concerns,")

EDITS = [(OLD_1, NEW_1), (OLD_2, NEW_2), (OLD_3, NEW_3)]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)                      # FR-E3

    before = io.open(P, encoding="utf-8").read()
    after = before
    for old, new in EDITS:
        if after.count(old) != 1:
            sys.stderr.write("REFUSED: a declared span matched %d times (need 1). Nothing "
                             "written.\n  %s\n" % (after.count(old), old[:70]))
            sys.exit(2)
        after = after.replace(old, new, 1)

    # Containment: strip every declared span from both sides and the remainder must be identical.
    b, a = before, after
    for old, new in EDITS:
        b = b.replace(old, "", 1)
        a = a.replace(new, "", 1)
    if norm(b) != norm(a):
        sys.stderr.write("REFUSED: prose changed outside the declared spans. Nothing written.\n")
        sys.exit(3)

    # Completeness: every declared edit took, and no old text survives.
    for old, new in EDITS:
        if old in after or new not in after:
            sys.stderr.write("REFUSED: a declared edit did not take. Nothing written.\n  %s\n"
                             % old[:70])
            sys.exit(4)

    io.open(P, "w", encoding="utf-8").write(after)
    print("council close reworked: %d declared span(s), %d words in, %d out"
          % (len(EDITS),
             sum(len(o.split()) for o, _ in EDITS),
             sum(len(n.split()) for _, n in EDITS)))


if __name__ == "__main__":
    main()
