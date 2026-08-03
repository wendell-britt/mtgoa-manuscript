# -*- coding: utf-8 -*-
"""ch1_thing.py — `thing` out of ch1. Eighteen of nineteen sites.

Ruled by Wendell 2026-08-03, after the classification that cleared 320 of 405 sites as
idiom failed his test: *"until I see a number of examples of 'the thing' that are
grammatical we're actually preserving something bad and saying it's ok because we've done
it before."*

He was right about the method, and the error has a name it already had in this repo. The
sort was made against "is this normal English", measured on writing that already carries
the defect — the same failure as `prose_diet.py`'s `empty` counter, whose baseline comment
reads *"measured across manuscript/ch*.md"* in a file whose own doctrine is
`BASELINE IS EXTERNAL, DELIBERATELY`. Health defined by averaging the sick, in the
instrument and then again in the hand sort, inside an hour.

Fourteen sampled sites were then tested one at a time. Fourteen improved. **The default is
remove**, and the burden sits on each survivor.

## Held out of this script

`ch1:50a` — the first draft read *the coworker who says the outdated line*, and Wendell:
*"same issue with the definite article. What is the outdated line? And line of what. It's
introducing ambiguities."* Two defects, and the second is worse: `the line` is the
Challenger's boundary, **41 uses in ch4**, and spending it on a stale remark collides the
book's second-densest metaphor with a throwaway. Awaiting a ruling.

## The one survivor so far

`ch1:54` — *"you lose the things that told you who you were."* Ruled an exception by
Wendell. It survives on the rule rather than on precedent: the referent is supplied by the
sentence before it — *"The game hands you every bit of it"* — so the definite article has
a real antecedent, which is the first of the four legal cases. It is also deliberately
plural and unbounded, and naming three of them would shrink it.

## What the sites taught

`ch1:113` carried two in one line, and the sentence between them already said **fuel**.

`ch1:50b` is the only site where naming a noun made it worse: *the right words* collides
with *"The words make a very convincing receipt"* one sentence earlier. Wendell supplied
the fix himself — *"you said it correctly so surely you're helping"* — and it moves to an
adverb rather than a noun. His contraction is left as the file's majority form (`you are`
runs 35 to 12 in ch1); the ruled word is `correctly`.

Three sites were pure deletion: 93, 149 and 255 each name the referent within the same
sentence, so the blank was only delay.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch1.md"

E = [
    # --- deletions: the sentence already names it ---------------------------
    ("The definition guards one thing: the conditions where both of us can keep making "
     "real moves.",
     "The definition guards the conditions where both of us can keep making real moves."),

    ("A game turns it into the thing standing right beside it: wonder,",
     "A game turns it into what stands right beside it: wonder,"),

    ("Find that one thing and write it down.",
     "Find it and write it down."),

    # --- named, from vocabulary the book already owns -----------------------
    ("You said the right thing, so surely you are helping.",
     "You said it correctly, so surely you are helping."),

    ("to never once be the person who says the wrong thing",
     "to never once be the person who gets it wrong"),

    ("You are someone who can make more of the very thing the game runs on. What that fuel "
     "earns you back, once you start spending it well, is the next thing on the floor.",
     "You are someone who can make more of the fuel the game runs on. What it earns you "
     "back, once you start spending it well, is the next move on the floor."),

    ("You repaired the thing you would rather have avoided.",
     "You repaired the rupture you would rather have avoided."),

    ("Return to the thing you brought with you.",
     "Return to whatever you brought with you."),

    ("what pulls people back to some things for years and drives them out of others for "
     "good",
     "what pulls people back to one activity for years and drives them out of another for "
     "good"),

    ("Some part of you is delighted by the very thing you complain about",
     "Some part of you is delighted by exactly what you complain about"),

    ("the wins that reshape things",
     "the wins that reshape the board"),

    ("The **Shaman** feels the thing before anyone can name it.",
     "The **Shaman** feels what is happening before anyone can name it."),

    ("it stops being your strength and turns into the thing you overplay",
     "it stops being your strength and turns into the move you overplay"),

    ("because a thing said out loud is harder to take back",
     "because a sentence said out loud is harder to take back"),

    # --- the two that needed the page, not the line -------------------------
    # six lines up: "a map of the moments that had changed me"
    ("The thing that hit me was in my pocket",
     "The card that hit me was in my pocket"),

    ("it kept the thing that changed you where you could pick it up and play it again",
     "it kept the moment that changed you where you could pick it up and play it again"),
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
    print("ch1.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
