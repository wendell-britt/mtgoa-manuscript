# -*- coding: utf-8 -*-
"""ch3_thing.py — `thing` out of ch3's ordinary sites. 31 of 72 body sites.

Ruled by Wendell 2026-08-03: *"run all the remaining chapters."*

## Why this is a partial sweep, and the part it does not touch

ch3 is the one chapter where `thing` is **load-bearing**, and the argument is not the idiom
plea that failed everywhere else.

Roughly forty of its sites belong to one construction — **`the true thing`**, with its
variants `the unsaid thing`, `the real thing`, and its pairing against `the right thing`.
It is not filler. It is the chapter's term of art, it names all four domains of Direct
Action, and it is the name of a canonical move:

    Move 5 · Show Up — Say the Thing Under the Thing
    the true thing said to a face · the true thing said out loud in place of the right
    thing · the honest need named and asked for · the unsaid thing put on the table

**The vagueness is the referent.** The chapter is about what a person has felt and not
said, and the whole teaching is that it stays unnamed until somebody says it. That is the
one defense that survived for `Say the Thing Under the Thing`, and here it extends over an
entire system rather than a title.

**That is a ruling about a term of art and the name of a move, not a copy-edit.** Held
whole for Wendell. Touching half of it would leave the chapter with two vocabularies for
one idea.

## What this script does sweep

The 31 ordinary sites, where `thing` is doing what it does everywhere else in the book.
`ch3:779` takes the same fix `ch7:590` took this morning — *does one thing nothing else can
do* → *does what nothing else can do* — so the two Faces keep the same sentence shape.
`ch3:962`'s *four things in it* takes the same fix as `ch7:777`, keeping the artifact
formula identical book-wide.

`ch3:235` needed a rebuild rather than a substitution: *"the difference between sensing a
thing and the thing sensed in the world"* goes to *"between a read that stays in you and a
read that lands in the world."* `read` is ch3's own densest term and the sentence is about
exactly that.

Six marginalia sites are excluded by the same convention as ch7.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch3.md"

E = [
    ("The choice came down to one thing: Stay and become invisible.",
     "The choice came down to this: Stay and become invisible."),

    ("Fear of things going wrong.",
     "Fear that the work would go wrong."),

    ("fear became noise. A thing to be managed, suppressed, medicated away.",
     "fear became noise. A symptom to be managed, suppressed, medicated away."),

    ("The practice comes down to one thing: Feel what's real.",
     "The practice comes down to this: Feel what's real."),

    ("the thing your body registered about a situation two beats before anyone said a word",
     "what your body registered about a situation two beats before anyone said a word"),

    ("Function is the difference between sensing a thing and the thing sensed *in the "
     "world*",
     "Function is the difference between a read that stays in you and a read that lands "
     "*in the world*"),

    ("unable to tell the table one thing it did not already know",
     "unable to tell the table anything it did not already know"),

    ("Nobody in the situation gains a thing from her knowing.",
     "Nobody in the situation gains anything from her knowing."),

    ("the whole language of getting things done",
     "the whole language of execution"),

    ("the other end sounds like the thing the altitude was built to leave behind",
     "the other end sounds like what the altitude was built to leave behind"),

    ("and the chest does a particular thing: a tightening, a pulling inward",
     "and the chest reacts in a specific way: a tightening, a pulling inward"),

    ("notice what you feel, the thing actually here in your body right now",
     "notice what you feel, what is actually here in your body right now"),

    ("put my own fluency on the table as a thing that gets me through doors",
     "put my own fluency on the table as an asset that gets me through doors"),

    ("each with the move that reaches it and the thing it hands you",
     "each with the move that reaches it and what it hands you"),

    ("you can move toward the hard thing instead of away from it",
     "you can move toward what is hard instead of away from it"),

    ("being in the thing instead of watching yourself do it",
     "being in it instead of watching yourself do it"),

    ("the stillness that can hold two true things at once without picking",
     "the stillness that can hold two truths at once without picking"),

    ("You are torn between two things that both seem true.",
     "You are torn between two positions that both seem true."),

    ("when you're stuck between two things that both seem necessary",
     "when you're stuck between two demands that both seem necessary"),

    ("Only one thing changed: whose rules it enforces.",
     "What changed is whose rules it enforces."),

    ("describes a thing you have watched happen rather than a phrase you are trying to "
     "talk yourself into",
     "describes an event you have watched happen rather than a phrase you are trying to "
     "talk yourself into"),

    # Same fix ch7:590 took, so the two Faces keep one sentence shape.
    ("The Controller developed does one thing nothing else in this chapter can do:",
     "The Controller developed does what nothing else in this chapter can do:"),

    ("It is a second thing built on top of the first",
     "It is a second layer built on top of the first"),

    # "moves" is the word the sentence three lines down already uses.
    ("and before them the three things that decide whether saying it helps or wounds",
     "and before them the three moves that decide whether saying it helps or wounds"),

    ("Watch the moment you shift from feeling the thing to pronouncing it.",
     "Watch the moment you shift from feeling it to pronouncing it."),

    ("Leaving strands the person with the hard thing you just handed them.",
     "Leaving strands the person with what you just handed them."),

    ("It is also the easiest thing in the world to lie to yourself about",
     "It is also the easiest lie to tell yourself"),

    ("answer the one thing the marker didn't ask:",
     "answer the question the marker didn't ask:"),

    ("it is also an *operation*, a thing every move can do",
     "it is also an *operation* every move can run"),

    # Same fix as ch7:777, keeping the artifact formula identical book-wide.
    ("Write yours in one line with four things in it: what you will do, who it reaches, by "
     "when, and what it costs you.",
     "Write yours in one line: what you will do, who it reaches, by when, and what it "
     "costs you."),

    ("and the one thing separating the referee from the judge: whose rulebook it enforces",
     "and what separates the referee from the judge: whose rulebook it enforces"),
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
    print("ch3.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
