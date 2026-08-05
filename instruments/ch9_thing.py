# -*- coding: utf-8 -*-
"""ch9_thing.py — `thing` out of ch9. 72 of 78 body sites.

Wendell 2026-08-03: *"run all five and bring me one consolidated diff."*

## Six held, and both clusters are already known

**The move name.** `### Move 4: Run It Again With One Thing Changed`, plus its two recaps
at `ch9:576` and `ch9:590` and the prose gloss at `ch9:552` that restates it in the same
words. Same ruling as `Say the Thing Under the Thing`.

**The Architect's formula.** `ch9:75` and `ch9:274` both say *"make the right thing easy"*,
which is the ch6 subtitle cluster held for Wendell.

## The repeated idiom

*"when things get hard"* runs six times — 121, 125, 141, 330, 396, 450 — always about
defaulting to a home game under pressure. All six take **when it gets hard**, which is
shorter and loses nothing, and keeping them uniform matters because the phrase is doing
callback work across the chapter.

## Where the chapter supplied the word

`work` takes 522 and 576 — *"Showing the unfinished thing to a single human being"* →
*"the unfinished work"* — and the two sentences are the same move stated twice, so they had
to move together.

`ch9:538` — *"the most expensive thing anyone can say to a builder"* → *"the most expensive
**sentence**"*, which is the book's word for a said thing in ch3 and ch7 both.

`ch9:250` — *"saying the right things, posting the right takes"* → *"saying the **right
words**"*, ch3's own phrase at five sites, and this sentence is describing exactly the
failure ch3 names.

## A heading swept rather than held

`ch9:324` — *"The Walk: Building the Thing That Didn't Exist Before"* — is descriptive rather
than a named move, and `ch9:147` and `ch9:207` run the same phrase in prose where it is
being swept. Holding the heading alone would produce the ch3 split for no gain.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch9.md"

E = [
    ("a different thing from having read about them",
     "not the same as having read about them"),

    # The six-instance idiom, kept uniform.
    ("you naturally move to Challenger when things get hard",
     "you naturally move to Challenger when it gets hard"),
    ("Then I actually mapped where I went when things got hard",
     "Then I actually mapped where I went when it got hard"),
    ("I naturally moved to Challenger when things got hard",
     "I naturally moved to Challenger when it got hard"),
    ("still defaulting to your home game when things get hard",
     "still defaulting to your home game when it gets hard"),
    ("Who still default to their home game when things get hard.",
     "Who still default to their home game when it gets hard."),
    ("You will still default to your home game when things get hard.",
     "You will still default to your home game when it gets hard."),

    ("The Founder creates the thing that didn't exist before:",
     "The Founder creates what didn't exist before:"),

    ("*This is the thing I'm building. This is the game I'm playing.*",
     "*This is what I'm building. This is the game I'm playing.*"),

    ("I built the thing I needed and couldn't find:",
     "I built what I needed and couldn't find:"),

    ("if you have a specific thing you want to build",
     "if you have something specific you want to build"),

    ("not just for the thing you're building) that's the succession",
     "not just for what you're building) that's the succession"),

    ("The Elder doesn't start new things. The Elder hands things forward.",
     "The Elder doesn't start anything new. The Elder hands forward what exists."),

    ("making sure the thing you built doesn't depend on you to survive",
     "making sure what you built doesn't depend on you to survive"),

    ("when a card names the thing you have been routing around",
     "when a card names what you have been routing around"),

    ("people who already know how to do the thing and have never been able to name it",
     "people who already know how to do the work and have never been able to name it"),

    ("You can't hand things forward without eventually having to break",
     "You can't hand anything forward without eventually having to break"),

    ("if you have a specific thing to build and you know you need support",
     "if you have something specific to build and you know you need support"),

    ("Create the thing that didn't exist before you.",
     "Create what didn't exist before you."),

    ("You make the thing so it can meet a person:",
     "You make it so it can meet a person:"),

    ("every redesign dodges the one thing the work actually needs:",
     "every redesign dodges what the work actually needs:"),

    ("Avoidance keeps the thing safe, and perfect, and unmet.",
     "Avoidance keeps it safe, and perfect, and unmet."),

    # ch3's own phrase, and this sentence describes ch3's failure exactly.
    ("saying the right things, posting the right takes",
     "saying the right words, posting the right takes"),

    ("the five emotional channels do more than name things:",
     "the five emotional channels do more than name feelings:"),

    ("where you present the thing you made with love and care",
     "where you present what you made with love and care"),

    ("The moment when the thing you built does exactly what you designed it to do",
     "The moment when what you built does exactly what you designed it to do"),

    ("having walked through the thing that hurt",
     "having walked through what hurt"),

    ("They might say the wrong thing and have to correct.",
     "They might get it wrong and have to correct."),

    ("### *The Walk: Building the Thing That Didn't Exist Before*",
     "### *The Walk: Building What Didn't Exist Before*"),

    ("That's the first thing nobody tells you.",
     "Nobody tells you that."),

    ("Turns out thirst and wanting to drink are different things.",
     "Turns out thirst and wanting to drink are not the same."),

    ("I'd built the whole thing out of what I found fun",
     "I'd built all of it out of what I found fun"),

    ("when someone critiques the thing you made",
     "when someone critiques what you made"),

    ("when you realize the thing you built has a shadow you didn't anticipate",
     "when you realize what you built has a shadow you didn't anticipate"),

    ("Rehearsing failure and doing the thing feel identical from inside your head.",
     "Rehearsing failure and doing it feel identical from inside your head."),

    ("whether you've done nothing or whether the thing has already failed. The rehearsal "
     "feels like work. The actual thing runs simpler and scarier.",
     "whether you've done nothing or whether it has already failed. The rehearsal feels "
     "like work. The actual attempt runs simpler and scarier."),

    ("where you kept doing the right thing and feeling nothing",
     "where you kept doing everything right and feeling nothing"),

    ("some specific thing you already do with your family",
     "something specific you already do with your family"),

    ("*I don't start things.",
     "*I don't start anything."),

    ("To look at the thing that keeps showing up in your life",
     "To look at what keeps showing up in your life"),

    ("I'm going to create the thing that should exist.*",
     "I'm going to create what should exist.*"),

    ("As an actual thing that happens, rather than as a lesson about resilience.",
     "As an actual event, rather than as a lesson about resilience."),

    ("Some things you build will fail.",
     "Some of what you build will fail."),

    ("The thing you built didn't solve the problem you thought it would solve.",
     "What you built didn't solve the problem you thought it would solve."),

    ("an obstacle, a gap, a thing that needs to be cleared",
     "an obstacle, a gap, something that needs to be cleared"),

    ("what's the thing that story is circling, the thing the Cauldron needs to transform?*",
     "what is that story circling, and what does the Cauldron need to transform?*"),

    ("What specific thing have you survived",
     "What specifically have you survived"),

    ("the thing that would keep you building even if nobody noticed?",
     "what would keep you building even if nobody noticed?"),

    ("one thing exists that did not exist before you",
     "something exists that did not exist before you"),

    ("The thing has to get made, get handed over, and come back changed.",
     "It has to get made, get handed over, and come back changed."),

    ("the thing you made lies on the table between you",
     "what you made lies on the table between you"),

    ("Reducing everything you could work on down to the one thing you are actually going "
     "to work on",
     "Reducing everything you could work on down to what you are actually going to work "
     "on"),

    ("one situation that keeps recurring, and one thing that keeps not happening",
     "one situation that keeps recurring, and one outcome that keeps not happening"),

    ("Showing the unfinished thing to a single human being",
     "Showing the unfinished work to a single human being"),

    ("you will not find out whether the thing works by looking at it harder",
     "you will not find out whether it works by looking at it harder"),

    ("the least useful thing a human being can hand you",
     "the least useful response a human being can hand you"),

    ("it is the most expensive thing anyone can say to a builder",
     "it is the most expensive sentence anyone can say to a builder"),

    ("The other is to throw the whole thing out and start over",
     "The other is to throw all of it out and start over"),

    ("Handing over the pen is how a thing survives being wrong",
     "Handing over the pen is how a design survives being wrong"),

    ("do not correct the first thing they do differently",
     "do not correct the first change they make"),

    ("Put the unfinished thing in front of somebody.",
     "Put the unfinished work in front of somebody."),

    ("*Cut the field.* Right now. What's the thing in your life that keeps showing up:",
     "*Cut the field.* Right now. What in your life keeps showing up:"),

    ("it is the one thing in here you cannot get from reading",
     "it is what you cannot get from reading"),

    ("write down two things before you go on:",
     "write down two answers before you go on:"),

    ("assembling the thing you are going to say when she stops",
     "assembling what you are going to say when she stops"),

    ("and the thing you are assembling really might be right",
     "and what you are assembling really might be right"),

    ("Two things exist on the other side of this book. They are not the same size, and "
     "they don't ask the same thing of you.",
     "Two paths exist on the other side of this book. They are not the same size, and they "
     "don't ask the same of you."),

    ("not just for the thing you're building) that is the succession",
     "not just for what you're building) that is the succession"),
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
    print("ch9.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
