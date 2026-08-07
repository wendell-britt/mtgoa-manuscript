# -*- coding: utf-8 -*-
"""ch6_thing.py — `thing` out of ch6, and a revert of my own ch5 error.

Wendell 2026-08-03: *"run all five and bring me one consolidated diff."*

## The error this script fixes first

ch6's chapter subtitle is **`*The System That Makes the Right Thing the Easy Thing*`**, and
`ch5:715` ends the Regent chapter by naming it: *"A system that makes the right thing the
easy thing for the people inside it. That is the Architect's work."* That is a handoff
line, pointing forward to the next chapter by quoting its title.

`ch5_thing.py` changed it to *"makes the right move the easy one"* and broke the echo. **The
revert is the first edit here.** Same failure as `the beautiful warmth`: I edited a phrase
without checking what else in the book was holding onto it.

## The formula, held for a ruling

`the right thing / the easy thing` is the Architect's thesis, and it runs as a set:

    ch6:2    the chapter subtitle
    ch6:197  "how do I redesign the system so the right thing becomes the thing that
             actually gets done?"
    ch6:634  "the best systems make the right thing the easy thing"
    ch5:715  the handoff line quoting the subtitle
    ch6:165  "Doing the right thing in the wrong system is a specific kind of expensive"
    ch6:475  "the Architect wins when the right thing happens without them having to be
             there"

Eight instances. Under the option-b ruling a title survives, and here the title is quoted
three times in prose and once from the previous chapter, so sweeping the prose and keeping
the heading would leave the same split ch3 has — except this one spans two chapters.

**Not decided here.** It is a chapter subtitle and a thesis, which is Wendell's call, and it
is the last held cluster in the book.

## The rest of ch6

38 sites, ordinary. `design` takes 407, `move` takes both halves of 401, and `ch6:421`
turned out to name its own referent in apposition — *"Someone says the thing in the meeting,
the sentence that writes a whole group of people out of the plan"* → *"Someone says the
sentence in the meeting that writes a whole group of people out of the plan."*

`ch6:634`'s first instance is swept even though the formula is held: *"what the Architect
hands forward is the thing the Diplomat does not have yet:"* is a colon naming its own
referent, and it is not part of the title.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

EDITS = [
    # THE REVERT. ch5:715 quotes ch6's subtitle; my own ch5 pass broke it.
    ("manuscript/ch5.md", [
        ("A system that makes the right move the easy one for the people inside it.",
         "A system that makes the right thing the easy thing for the people inside it."),
    ]),
    ("manuscript/ch6.md", [
        ("looked at the chaos of how things got done",
         "looked at the chaos of how work got done"),

        ("The choice came down to one thing: Become invisible and useful,",
         "The choice came down to this: Become invisible and useful,"),

        ("The village still built things. Still created roles and processes",
         "The village still built. Still created roles and processes"),

        ("while continuing to do the same thing that had always produced the same failure",
         "while continuing to do what had always produced the same failure"),

        ("The village does one thing with structural design once the Architect leaves: it "
         "transforms it into",
         "Once the Architect leaves, the village transforms structural design into"),

        ("Started to say things like *we don't need to overthink this*",
         "Started saying *we don't need to overthink this*"),

        ("starve itself of the one thing it needed most:",
         "starve itself of what it needed most:"),

        ("and a living thing into a KPI",
         "and a living relationship into a KPI"),

        ("the discipline is the only thing that keeps a relational field",
         "the discipline is what keeps a relational field"),

        ("and that was the wrong thing. Not who failed it.",
         "and that was the problem. Not who failed it."),

        ("Good people do harmful things because the system they're inside",
         "Good people do harm because the system they're inside"),

        ("does the other thing, and the fact that they can is not a rounding error",
         "chooses otherwise, and the fact that they can is not a rounding error"),

        ("the mental models that explain why things are the way they are",
         "the mental models that explain why systems are the way they are"),

        ("rather than a thing waiting behind you",
         "rather than an ambush waiting behind you"),

        ("The thing you were only imagining now exists somewhere other than in you.",
         "What you were only imagining now exists somewhere other than in you."),

        ("and so never letting the thing go",
         "and so never letting it go"),

        ("nobody has named the thing underneath it:",
         "nobody has named what is underneath it:"),

        ("The Fixer decides whether the thing in front of you holds up well enough",
         "The Fixer decides whether what is in front of you holds up well enough"),

        ("The Emotional Body is the thing all four strategies are strategies *about.*",
         "The Emotional Body is what all four strategies are strategies *about.*"),

        ("The responsible thing to do with a feeling about injustice, obviously, is not to "
         "sit there having it. The responsible thing is to convert it",
         "The responsible move with a feeling about injustice, obviously, is not to sit "
         "there having it. The responsible move is to convert it"),

        ("staying in the feeling is the one thing the conversion exists to prevent",
         "staying in the feeling is what the conversion exists to prevent"),

        ("nobody ever really built it for the thing it got pointed at",
         "nobody ever really built it for what it got pointed at"),

        ("I answer by making the thing more defensible",
         "I answer by making the design more defensible"),

        ("It is building things.",
         "It is building."),

        # The apposition already names it.
        ("Someone says the thing in the meeting, the sentence that writes a whole group of "
         "people out of the plan.",
         "Someone says the sentence in the meeting that writes a whole group of people out "
         "of the plan."),

        ("The only thing that changed is what you gave it authority over.",
         "What changed is what you gave it authority over."),

        ("What was the last thing it converted?",
         "What did it convert last?"),

        ("The Emotional Body developed does one thing nothing else in this chapter can do:",
         "The Emotional Body developed does what nothing else in this chapter can do:"),

        ("building the thing so the next person can run it without you",
         "building it so the next person can run it without you"),

        ("the designer can move on to the next thing",
         "the designer can move on"),

        ("wrote down the one thing you were assuming they already knew",
         "wrote down what you were assuming they already knew"),

        ("Show Up is the thing you build,",
         "Show Up is what you build,"),

        ("The thing that needed feeling now has a process attached to it",
         "What needed feeling now has a process attached to it"),

        ("One line, four things: what you will do, who it reaches, by when, and what it "
         "costs you. *Build the Ladder",
         "One line: what you will do, who it reaches, by when, and what it costs you. "
         "*Build the Ladder"),

        ("with the three things I never wrote down",
         "with the three details I never wrote down"),

        ("the dread is usually that the thing will be built worse without you",
         "the dread is usually that it will be built worse without you"),

        # Not part of the title; a colon naming its own referent.
        ("What the Architect hands forward is the thing the Diplomat does not have yet:",
         "What the Architect hands forward is what the Diplomat does not have yet:"),
    ]),
]


def main():
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for i, (a, _b) in enumerate(edits, 1):
            n = t.count(a)
            if n != 1:
                sys.exit("%s E%d anchor matched %d times, expected 1: %r"
                         % (path, i, n, a[:60]))
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for a, b in edits:
            t = t.replace(a, b)
        io.open(path, "w", encoding="utf-8").write(t)
        print("%s — %d edit(s) applied" % (path, len(edits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
