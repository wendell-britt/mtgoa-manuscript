# -*- coding: utf-8 -*-
"""ch7_thing.py — `thing` out of ch7. 24 body sites; 3 marginalia held.

Ruled by Wendell 2026-08-03: *"run all the remaining chapters."*

## Marginalia held, not cleared

`ch7:145` and `ch7:170` are in-world testimony inside `>` blocks — a different voice, and
the surface `gate.py` has excluded by convention since it was written. *"other people
failing to tell me things"* and *"the hardest thing they teach"* are a person talking, and
quoted speech is the one category with a real argument behind it. Flagged for a ruling
rather than swept.

## What ch7 supplies instead

The chapter is unusually well equipped for this, which is why 24 sites cost almost no
invention:

- **`sentence`** carries five of them. ch7 already runs *"somebody says the sentence they
  had decided in the parking lot not to say"* and *"one clear sentence naming what this
  field must hold."* *the true thing said* → *the true sentence said*, three times over,
  and the repetition is the chapter's own.
- **`term`** takes `ch7:671`. *"you have never said the one thing you will not trade"* →
  *"you have never named the one term you will not trade."* TERMS runs 100 in this chapter
  and this sentence is the definition of a walk-away term. The placeholder was standing
  where the chapter's second-densest word belonged.
- **Six sites are deletions**, where a colon or a predicate already names the referent:
  73, 315, 411, 549, 590, 777.

## One that fixes two defects

`ch7:757` — *"the single thing in the field nobody can relate to compassionately"* — carried
a `thing` and a container preposition, the second being R-B's rule from earlier today: a
field has no inside. It goes to *"the one subject nobody there can relate to
compassionately,"* which resolves both.

## A cross-chapter formula, handled the same way each time

`ch7:777` — *"One line, four things: what you will do, who it reaches, by when, and what it
costs you"* — is a template that recurs in ch5, ch6 and elsewhere as the artifact
definition. The colon names all four, so the count and the placeholder are both delay. It
goes to *"One line: …"* here and in every other chapter, so the formula stays identical
across the book.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch7.md"

E = [
    ("as the precious, chosen thing it is",
     "as the precious, chosen gift it is"),

    ("without requiring it to resolve into one thing",
     "without requiring it to resolve into one answer"),

    ("the true thing said in a way that ends the possibility of saying the next true thing",
     "the true sentence said in a way that ends the possibility of saying the next one"),

    ("and the thing I have not yet said is",
     "and what I have not yet said is"),

    ("One thing separates a great Translator from a mediocre one:",
     "One habit separates a great Translator from a mediocre one:"),

    ("Agreements are cold things.",
     "Agreements are cold."),

    # The site marginalia/review.py has been flagging as say-the-noun.
    ("They say the thing, the temperature drops, and the matter gets settled.",
     "They say the sentence nobody else will, the temperature drops, and the matter gets "
     "settled."),

    ("The Skeptic decides whether the thing you react to was ever real. The Fixer-Healer "
     "decides whether the thing in front of you merits giving yourself to.",
     "The Skeptic decides whether what you react to was ever real. The Fixer-Healer "
     "decides whether what is in front of you merits giving yourself to."),

    ("which means the thing you built the ledger to prevent is now the thing your standing "
     "requires",
     "which means what you built the ledger to prevent is now what your standing requires"),

    # "the case" is set two sentences up: "A case would be longer."
    ("It does not cover the other thing, and that is the point.",
     "It does not cover the case, and that is the point."),

    ("and the true thing said in a way that ends the conversation",
     "and the true sentence said in a way that ends the conversation"),

    ("The Victim developed does one thing nothing else in this chapter can do:",
     "The Victim developed does what nothing else in this chapter can do:"),

    ("the agent has said neither thing out loud",
     "the agent has said neither out loud"),

    # TERMS runs 100 in this chapter and this sentence defines a walk-away term.
    ("you have never said the one thing you will not trade",
     "you have never named the one term you will not trade"),

    ("because it requires saying things that are uncomfortable in a specific order",
     "because it requires uncomfortable sentences in a specific order"),

    ("Not your interpretation of what broke. The specific thing that was said or done.",
     "Not your interpretation of what broke. What was actually said or done."),

    ("the only thing that builds confidence in a relationship",
     "the only proof that builds confidence in a relationship"),

    ("everyone gets to say their thing",
     "everyone gets to speak"),

    ("you've said the hard true thing and nothing has broken",
     "you've said the hard true sentence and nothing has broken"),

    # Two defects: the placeholder, and R-B's container preposition.
    ("becomes the single thing in the field nobody can relate to compassionately",
     "becomes the one subject nobody there can relate to compassionately"),

    ("One line, four things: what you will do, who it reaches, by when, and what it costs "
     "you.",
     "One line: what you will do, who it reaches, by when, and what it costs you."),
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
    print("ch7.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
