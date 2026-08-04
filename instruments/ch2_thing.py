# -*- coding: utf-8 -*-
"""ch2_thing.py — `thing` out of ch2. All eleven sites, no exceptions.

Ruled by Wendell 2026-08-03: *"run all the remaining chapters."*

## The exception I predicted, and it did not survive

I flagged `ch2:254` in advance — *"When a sentence names the thing you have been circling
for years"* — on the theory that the **unnamed** referent is the content, which is the one
argument that worked for `Say the Thing Under the Thing`.

It fails immediately. *"When a sentence names what you have been circling for years"* keeps
the withholding exactly, because **the circling is the content**, not the noun. The
placeholder was carrying nothing the relative clause was not already carrying.

Worth recording as a method note: predicting an exception before writing the replacement is
how the 320-site idiom bucket happened. The test is the rewrite, every time.

## ch2:11 is mine

*"when somebody finally says the thing that has been sitting there for months"* is from the
opening written this session and approved on 2026-08-02, two days after Wendell banned the
phrasing. It is fixed here rather than left because I wrote it.

## Notes on three

`ch2:91` — *the last hard thing* names a crisis, and `crisis` is the word the sentence was
avoiding. Nothing is lost by saying it.

`ch2:258` carried two in one breath. The referent is set four lines up at `ch2:254` — *"When
a daemon lands, stop there"* — so `recognition` is the chapter's own idea, and the second
one goes to a verb: *do one thing with it* → *take one action on it*.

`ch2:324` and `ch2:53` are deletions of the third kind seen in ch1: a colon or a
predicate names the referent inside the same sentence, so the placeholder was delay.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = [
    # Mine, from this session's opening. See the docstring.
    ("when somebody finally says the thing that has been sitting there for months",
     "when somebody finally says what has been sitting there for months"),

    ("They are not the same thing, and the work is to tell them apart.",
     "They are not the same, and the work is to tell them apart."),

    ("Both of these things are true.",
     "Both are true."),

    ("Coalitions that held through the last hard thing are fraying",
     "Coalitions that held through the last crisis are fraying"),

    ("What pattern do the people in this group end up rewarding when things get uncertain?",
     "What pattern do the people in this group end up rewarding when nobody knows what "
     "happens next?"),

    # The predicted exception. It did not survive the rewrite.
    ("When a sentence names the thing you have been circling for years, stay with it.",
     "When a sentence names what you have been circling for years, stay with it."),

    ("Let the first true thing find you. Then do one thing with it.",
     "Let the first true recognition find you. Then take one action on it."),

    ("it does the last thing a hull can do: it takes the damage itself",
     "it does what a hull does last: it takes the damage itself"),

    ("it manages how things look",
     "it manages appearances"),

    ("You lunge for the one thing you can repair.",
     "You lunge for whatever you can repair."),
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
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
