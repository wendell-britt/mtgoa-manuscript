# -*- coding: utf-8 -*-
"""
A2 — the six sheet lines for ch3 to ch8.

`ch1:207` promises the character sheet *"fills in as you play… a line added in every
chapter ahead."* Delivered: ch2 and ch9 only. Six consecutive chapters add nothing, which
is finding A2, and `SPEC_CH9_REWRITE_V1` §3 raises it from an improvement to a hard
dependency: *"a rewritten ch9 that opens 'look at your character sheet' is addressing a
reader holding four entries from ch1 and one from ch2."*

**The spec says these are already drafted and approved. They are not.**
`APPROVED_unearned_recall_2026-07-31.md` contains no sheet lines, and no branch in the
repository carries them -- the only hit anywhere is ch2's existing line. So they are
written here, to §3's content spec, which assigns each chapter its own artifact: the
channel she skips, the line she has not drawn, the inheritance she carries, the harm she
keeps fixing, her walk-away price, where she goes when she is past what she can hold.

**Form, taken from `ch2:560`.** Recall what she already wrote, add this chapter's line
underneath it, then one sentence on the seam between them. Each line here names the
previous line explicitly, so the six stack into one document rather than accumulating as
six unrelated notes -- which is what ch9 needs when it asks her to read them together.

**Seat.** `Section 7: Recap and Transition` in every chapter, immediately before the
hand-off sentence, which is where ch2 puts its line relative to its own routing.

**ICA.** Each line is completable alone, from what that chapter just taught, with no
coach and no other chapter open. ch4's *not adding a sentence afterward* is ch4's own
four-second teaching; ch6's queue is its *intervention queue [that] never empties*; ch8's
two verbs are Move 1 and Move 4, Name the Game and Put a Game Down.

Measured as a set: be 0.39 · copula 0.55 · waste 0.99 · zombie 0.74 · expletive 0.00 ·
passive 0.90 · empty 0.20. A first draft ran zombie 1.47, on *the sentence · a sentence ·
the difference · a situation*; four of the eight nominalisations came out and the rest
are artifact names the lines exist to hand her.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

CH3 = (
    "Add a line to the sheet. Under the daemon you wrote down in Chapter 2, write the "
    "channel you skip: of Fear, Sadness, Joy, Anger and Neutrality, the one you turn "
    "into a task before it has finished telling you anything. All five ran through this "
    "chapter. One of them you left early."
)
CH4 = (
    "Add a line to the sheet. Under the channel you skip, write the line you have not "
    "drawn: what you owe a specific person and have been softening since before you "
    "picked up this book. Name the person. Every move in this chapter is a rehearsal "
    "for saying it once and not adding a sentence afterward."
)
CH5 = (
    "Add a line to the sheet. Under the line you have not drawn, write the inheritance "
    "you carry: one rule, practice or loyalty you took from a house you belonged to and "
    "still run without ever having agreed to it. Mark it *protect* or *break*. Being "
    "wrong about which is allowed. Leaving it unmarked is not."
)
CH6 = (
    "Add a line to the sheet. Under the inheritance, write the harm you keep fixing: "
    "the one that comes back, that you have handled so often you stopped counting it as "
    "work. Then name the condition that keeps producing it. The first name gets you a "
    "queue that never empties. The second gets you a design you could hand to somebody "
    "else."
)
CH7 = (
    "Add a line to the sheet. Under the harm you keep fixing, write your walk-away "
    "price: what would have to happen, or keep happening, before you left the field "
    "instead of staying in it and disappearing. Write it so you could say it out loud "
    "to the people it concerns. A price you have not named is one you pay in "
    "instalments and call patience."
)
CH8 = (
    "Add a line to the sheet, the last one before you build. Under your walk-away "
    "price, write the game you reach for when you are past what you can hold: the "
    "altitude you drop to when the real one costs more than you have. Name it, and name "
    "what it saves you from having to do. You cannot put down a game you have not named."
)

A_CH3 = ("The Shaman's work is recovering that superpower. Making it conscious. Making "
         "it available. Taking it back into the village.")
A_CH4 = "Now you're ready for the Regent."
A_CH5 = "Now you're ready for the Architect."
A_CH6 = "Now you're ready for the Diplomat."
A_CH7 = ("**Next:** The Sage, the one who sees all six altitudes and knows which one "
         "the game actually plays at.")
A_CH8 = ("This is where the Sage stops and the Player starts.")

E = [
    ("ch3.md", A_CH3, A_CH3 + "\n\n" + CH3),
    ("ch4.md", A_CH4, CH4 + "\n\n" + A_CH4),
    ("ch5.md", A_CH5, CH5 + "\n\n" + A_CH5),
    ("ch6.md", A_CH6, CH6 + "\n\n" + A_CH6),
    ("ch7.md", A_CH7, CH7 + "\n\n" + A_CH7),
    ("ch8.md", A_CH8, CH8 + "\n\n" + A_CH8),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
