# -*- coding: utf-8 -*-
"""
Edits A, B and C — the Founder move is the book, not the app.

Source: `drafts/APPROVED_founder_move_is_the_book_2026-08-01.md` on
`claude/edit-enrollment-page`. Ruled by Wendell 2026-08-01: *"we need to rewrite the
autobiography. The founder's move is writing the book."*

Three of the eleven bars-engine sites. Section 5's other eight are NOT here; see the
report. They depend on a replacement whose two open fields are still open.

**Every replacement fact was checked against the page rather than against the draft.**
The provenance table in the approved draft is correct at every row:

    the course, hundreds of people, the ones who did not finish
        ch9:340 -- "The course had less than a ten percent completion rate."
    chapters at the applause counter, thrown out
        ch1:119 -- "I wrote whole chapters of this book standing at it and had to
        throw them out, because you can hear it in the prose."
    live in more hands than mine
        ch9:157, verbatim -- "I wrote this down so the map would live in more hands
        than mine."

The middle one is worth recording because I nearly reported it as invented biography.
`SPEC_CH9_REWRITE_V1` section 12 records exactly that failure mode -- a form with N slots
generates N specifics -- so the claim deserved the check. It survived it: the sentence is
in ch1, in a parenthetical, in Wendell's own first person.

*operate it* becomes *repeat it* because a book is repeated rather than operated. Edit C
takes Wendell's line edit: the verb is **write**, and *"the specific problem you want to
solve for the people you want to help"* restores the quest's second half from `ch1:205`,
where a quest is a fight *and* the people it is for.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # ---- Edit A · the Founder-move claim -------------------------------------
    ("ch9.md",
     "Bars-engine is my Founder move. I built the thing I needed and couldn't find: an "
     "actual game system that lets people practice the WAVE, that makes the emotional "
     "alchemy mechanical, that gives the six Faces a practice context instead of just a "
     "conceptual one.",
     "This book is my Founder move. I built the thing I needed and couldn't find: a "
     "practice you could actually run, that makes the emotional alchemy mechanical, "
     "that gives the six Faces a context instead of a vocabulary."),

    # ---- Edit B · the five Player moves, re-anchored --------------------------
    ("ch9.md",
     "Bars-engine has cost me all five of these.",
     "This book has cost me all five of these."),

    ("ch9.md",
     "*Put it in front of one person*: it went in front of players before it was good, "
     "and the sessions that failed are the reason the current version works. *Take the "
     "note that costs you the design*: the token economy did not get adjusted, it got "
     "rebuilt, three times, because each time the note was structural. *Run it again "
     "with one thing changed*: every failed session became the next session with "
     "something named and different in it. *Hand someone the pen*: the goal is for "
     "bars-engine to outlive its founder, which means whoever runs it later gets to "
     "change it, not just operate it.",
     "*Put it in front of one person*: the course went in front of hundreds of people "
     "before it was good, and the ones who did not finish are the reason this exists. "
     "*Take the note that costs you the design*: a stack of chapters written at the "
     "applause counter did not get revised, they got thrown out. *Run it again with one "
     "thing changed*: every version that failed became the next one with something named "
     "and different in it. *Hand someone the pen*: the point is for this to live in more "
     "hands than mine, which means whoever runs it later gets to change it, not just "
     "repeat it."),

    # ---- Edit C · the teaching sentence --------------------------------------
    ("ch9.md",
     "You don't have to build bars-engine. You have to build your version of what "
     "bars-engine is for your specific problem. That's the Player's move.",
     "You don't have to write a whole book about it. You have to build your version of "
     "what this book is for the specific problem you want to solve for the people you "
     "want to help. That's the Player's move."),
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
