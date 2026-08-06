# -*- coding: utf-8 -*-
"""ch8_thing.py — `thing` out of ch8. 41 of 44 body sites.

Wendell 2026-08-03: *"run all five and bring me one consolidated diff."*

## The chapter's own title was sitting under five of them

ch8 is *"Seeing the Whole Board Without Leaving the Table."* Five sites were writing `the
whole thing` and `above things` where **`the board`** and **`the table`** belong:

    the one who saw the whole thing and still set the table  -> saw the whole board
    The Sage sees the whole thing.                           -> sees the whole board
    going up, seeing the whole thing                         -> seeing the whole board
    you've been above things too long                        -> above the table too long
    when things move from the power game toward harmony      -> when the table moves

Same shape as `fuel` in ch1:113 and `the beautiful words` in ch3:742 — the answer was in the
chapter's own heading, five times over.

`ch8:745` is the best of them. *"draws the line and holds the field and builds the thing and
stays"* is a roll-call of the other Faces, and the third slot had a placeholder where the
Architect's word goes: **line** (ch4), **field** (ch7), **structure** (ch6).

## Three held

`ch8:246` — *"good design makes the right thing easy"* — belongs to the ch6 subtitle cluster
held for a ruling.

`ch8:769` and `ch8:779` — *"*This is my thing* is not Fire, Water, Metal, Earth, or Wood"* —
quoted self-talk that the chapter is diagnosing. The book is exhibiting a bad habit, and
the habit is the phrase. Flagged with the marginalia question.

2 marginalia sites excluded by the usual convention.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch8.md"

E = [
    ("when someone says a thing nobody knows how to answer",
     "when someone says something nobody knows how to answer"),

    ("The wise thing to do is to be inside the game, seeing clearly",
     "Wisdom is being inside the game, seeing clearly"),

    ("the one who saw the whole thing and still set the table",
     "the one who saw the whole board and still set the table"),

    ("The choice came down to one thing: keep showing up",
     "The choice came down to this: keep showing up"),

    ("amounts to the same thing as exile",
     "amounts to the same as exile"),

    ("Offer it to yourself as a thing to check rather than a thing I already know about "
     "you.",
     "Offer it to yourself as a question to check rather than a verdict I already hold "
     "about you."),

    ("After the Sage stopped naming things, the villagers kept playing games.",
     "After the Sage stopped naming the games, the villagers kept playing them."),

    ("doing versions of useful things (mediating pain, solving problems, designing systems)",
     "doing versions of useful work (mediating pain, solving problems, designing systems)"),

    ("The Sage sees the whole thing.",
     "The Sage sees the whole board."),

    ("sits a third thing that nobody here has found a way to write down",
     "sits a third document that nobody here has found a way to write down"),

    ("will keep saying accurate things in a register nobody present can receive",
     "will keep saying accurate sentences in a register nobody present can receive"),

    ("check the one thing that gives it away",
     "check what gives it away"),

    ("the way things look smaller from inside than they did from above",
     "the way everything looks smaller from inside than it did from above"),

    ("becomes a thing you do for an audience",
     "becomes a performance for an audience"),

    ("going up, seeing the whole thing, and immediately needing to come back",
     "going up, seeing the whole board, and immediately needing to come back"),

    ("You notice when things move from the power game back toward harmony",
     "You notice when the table moves from the power game back toward harmony"),

    ("The Fixer-Healer decides whether the thing in front of you holds up well enough",
     "The Fixer-Healer decides whether what is in front of you holds up well enough"),

    ("It sounds like the most self-aware thing in the vicinity.",
     "It sounds like the most self-aware voice in the vicinity."),

    ("and the thing that needs fixing is always upstream of the thing that needed doing",
     "and what needs fixing is always upstream of what needed doing"),

    ("One more thing always waits to be worked through",
     "One more wound always waits to be worked through"),

    ("is, in shadow, the least coachable thing in the book",
     "is, in shadow, the least coachable Face in the book"),

    ("looks like the most rigorous thing available",
     "looks like the most rigorous move available"),

    ("The Damaged Self developed does one thing nothing else in this chapter can do:",
     "The Damaged Self developed does what nothing else in this chapter can do:"),

    ("Put them together and you get the thing the last chapter of a book about allyship "
     "actually needs:",
     "Put them together and you get what the last chapter of a book about allyship "
     "actually needs:"),

    ("because you've been above things too long",
     "because you've been above the table too long"),

    ("and things have moved to harmony",
     "and the table has moved to harmony"),

    ("Let me come back to where things are simpler.",
     "Let me come back to where it is simpler."),

    ("the person who never misses the thing everyone else misses",
     "the person who never misses what everyone else misses"),

    ("keeping the view and still doing the thing the view is for",
     "keeping the view and still doing what the view is for"),

    # A roll-call of the other Faces: line (ch4), field (ch7), structure (ch6).
    ("draws the line and holds the field and builds the thing and stays",
     "draws the line and holds the field and builds the structure and stays"),

    ("a fifty per cent chance of the thing that killed his father at sixty",
     "a fifty per cent chance of what killed his father at sixty"),

    ("witnessing a game from inside it is the one thing the whole-board view makes harder",
     "witnessing a game from inside it is what the whole-board view makes harder"),

    ("the way you notice things: the suspect way",
     "the way you notice everything: the suspect way"),

    ("which never amounts to the same thing.",
     "which never amounts to the same."),

    ("One line, four things: what you will do, who it reaches, by when, and what it costs "
     "you. *Leave the Gam",
     "One line: what you will do, who it reaches, by when, and what it costs you. *Leave "
     "the Gam"),

    ("the game underneath the game, the thing everyone can feel and nobody says",
     "the game underneath the game, what everyone can feel and nobody says"),

    ("*You saw the thing, and you named it and stayed",
     "*You saw it, and you named it and stayed"),

    ("Four things carry forward.",
     "Four capacities carry forward."),

    ("it's the most generous thing available at this altitude",
     "it's the most generous move available at this altitude"),
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
    print("ch8.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
