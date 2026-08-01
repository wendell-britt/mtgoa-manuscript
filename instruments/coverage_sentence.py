# -*- coding: utf-8 -*-
"""
The coverage sentence — what the mode-to-channel mapping is actually FOR.

"Five modes, five channels, no overlap" stayed cut. It is true, and being true is an
author's reason. Asked what Jordan does with it, the honest answer is nothing: ch4 said
the quiet part out loud, that the tidiness "explains why the modes number five rather
than three", which answers a question Wendell had rather than one she has.

**The reader value in the bijection is coverage, and that is a different sentence.**
Every channel has a mode, so whatever state she turns up in, a move here is built for it.
Which means the entry fee she thinks she owes is not owed. Jordan's standing belief is
that she has to be regulated before she can act, and each Face carries its own version of
that belief:

    ch4  I have to be in the right mood to confront
    ch5  I have to feel loyal to steward what I was handed
    ch6  I have to be dispassionate to think structurally
    ch7  I have to be calm to hold a field
    ch8  I have to be detached to see clearly

Each sentence answers the one its chapter provokes, and each is shaped differently on
purpose. The first draft opened four of five with "You do not have to be", which measured
be 1.71 and is the robotic-rhythm pattern: a formula, not five sentences. The second draft
tripped the `empty` counter added an hour earlier at 2.36, on "something" twice and
"nothing" once. Both caught before Wendell saw them.

At 122 words the ratios are weak evidence. The two catches above were the real review.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# (chapter, anchor to append after, the sentence)
E = [
    ("ch4.md",
     "Each mode names a different signal in the body asking to be spent a different way.",
     "Whatever you are carrying when the moment comes, one of these five will spend it. "
     "Confrontation makes no demand on your mood at the door."),

    ("ch5.md",
     "The Metal channel's discernment becomes the foundation for everything else the "
     "Regent builds.",
     "Fury at what you inherited does not disqualify you. One of these five carries the "
     "inheritance forward on exactly that fire."),

    ("ch6.md",
     "The logic is what the Architect does with the signal. The signal is what tells "
     "the Architect there is anything to do.",
     "A failing system will leave you feeling one of the five, and a mode here runs on "
     "each of them. The Strategist wants your anger in particular."),

    ("ch7.md",
     "Each mode's full arc, the dissatisfaction it carries and the alchemy that "
     "transmutes it, is worked through in the five channel deep-dives in Section 4.",
     "Calm is not the entry fee. Whatever you feel as you sit down, one of these five "
     "works with that feeling rather than around it."),

    ("ch8.md",
     "The Sage's practice runs the full spectrum, and that makes this the last Face "
     "before the Player: the emotional range has nowhere left to hide.",
     "You will feel the game from inside it, and one of these five sees from exactly "
     "there. No other vantage was ever on offer."),
]


def main():
    files, bad = {}, []
    for name, anchor, sentence in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(anchor)
        if n != 1:
            bad.append("%s: anchor matched %d times — %r" % (name, n, anchor[:60]))
            continue
        files[name] = files[name].replace(anchor, anchor + " " + sentence, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d sentence(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
