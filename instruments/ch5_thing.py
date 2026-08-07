# -*- coding: utf-8 -*-
"""ch5_thing.py — `thing` out of ch5. All 46 body sites.

Wendell 2026-08-03: *"run all five and bring me one consolidated diff."*

## ch5's cluster, and why it is not ch3's

Fourteen sites use `the thing` for the institution being inherited — *"let the thing
evolve"*, *"the whole weight of the thing"*, *"the thing you walked away from"*, *"the thing
you were holding was you."*

It looks like a term of art and it is not. Unlike ch3's `the true thing`, **nothing here
depends on the referent staying unnamed.** The chapter is about inheritance and it already
owns the words: `structure`, `tradition`, `inheritance`, `role`. The placeholder was not
protecting anything; it was standing where the chapter's own vocabulary goes.

So `structure` takes 179, 191, 301 and 550, and each of those sentences becomes more
concrete rather than less.

## The pronoun cases, which are most of the rest

`ch5:183` carries three in one paragraph and all three take pronouns or a deletion, because
the subject has been established for two pages: *the whole weight of the thing rested on* →
*the whole weight rested on*; *the thing went with them* → *it went with them*.

## `ch5:295`, where the repetition was doing rhythm

*"I said things. Careful things, the kind you say to a group allergic to structure."* The
doubling is deliberate and a straight substitution kills it, so this one goes to verbs:
*"I spoke up. Carefully, the way you do with a group allergic to structure."*

## Consistent with the other chapters

`does one thing nothing else in this chapter can do` → `does what nothing else in this
chapter can do`, the same fix ch3:779, ch4:595 and ch7:590 took, so all four Faces keep one
sentence shape.

`One line, four things:` → `One line:`, the same as ch3:962, ch4:752 and ch7:777.

`whether the thing in front of you` → `whether what is in front of you`, the same as
ch4:534 and ch7:522, so the daemon jurisdictions read identically across chapters.

6 marginalia sites excluded by the usual convention.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch5.md"

E = [
    ("as *maintenance problems*, things to fix with better systems",
     "as *maintenance problems*, fixable with better systems"),

    ("The villagers did the thing the Regent taught them to do",
     "The villagers did what the Regent taught them to do"),

    ("They held the line on how things were done.",
     "They held the line on how everything was done."),

    ("was the same thing as \"what actually works.\"",
     "was the same as \"what actually works.\""),

    ("the village truly believed it was doing the right thing.",
     "the village truly believed it was doing right."),

    ("The village thought loyalty was the same thing as obedience. The village thought "
     "tradition was the same thing as wisdom.",
     "The village thought loyalty was the same as obedience. The village thought tradition "
     "was the same as wisdom."),

    ("You were going to let the thing evolve as the people evolved.",
     "You were going to let the structure evolve as the people evolved."),

    ("different ideas about what the thing was for",
     "different ideas about what it was for"),

    ("The whole weight of the thing rested on whoever was most energized",
     "The whole weight rested on whoever was most energized"),

    ("and when those people left, the thing went with them.",
     "and when those people left, it went with them."),

    ("The thing you walked away from was real.",
     "What you walked away from was real."),

    ("builds a thing bigger than any one person's presence in it, a thing that knows how "
     "to receive a new person",
     "builds a structure bigger than any one person's presence in it, one that knows how "
     "to receive a new person"),

    ("It makes the things you build last longer than you do.",
     "It makes what you build last longer than you do."),

    ("One thing makes the Regent's practice distinct:",
     "One belief makes the Regent's practice distinct:"),

    ("not a living thing that can serve the next person's moment",
     "not a living tradition that can serve the next person's moment"),

    # The doubling is rhythm; substitution kills it, so this goes to verbs.
    ("I said things. Careful things, the kind you say to a group allergic to structure.",
     "I spoke up. Carefully, the way you do with a group allergic to structure."),

    ("the one who wants to run things",
     "the one who wants to run everything"),

    ("arguing about the same things from different angles",
     "arguing about the same questions from different angles"),

    ("watching things dissolve for twenty years",
     "watching structures dissolve for twenty years"),

    ("It sounds like the thing that keeps people inside harmful institutions.",
     "It sounds like what keeps people inside harmful institutions."),

    ("That's the most loyal thing there is",
     "That is the most loyal act there is"),

    ("The Teacher passes the thing in a form the next person can actually receive.",
     "The Teacher passes it on in a form the next person can actually receive."),

    ("hold the form and you cannot lose the thing)",
     "hold the form and you cannot lose what is inside it)"),

    ("This includes things you would not have chosen. Family patterns.",
     "This includes what you would not have chosen. Family patterns."),

    ("and the cost is the thing that makes it separate:",
     "and the cost is what makes it separate:"),

    ("where it can be postponed indefinitely as a thing you are already doing",
     "where it can be postponed indefinitely as work you are already doing"),

    ("This part of how we do things stopped serving what it was built for.",
     "This part of how we work stopped serving what it was built for."),

    ("whether the thing in front of you is in good enough condition",
     "whether what is in front of you is in good enough condition"),

    ("everyone discovers that the thing you were holding was you.",
     "everyone discovers that what you were holding up was you."),

    ("and that the thing I would fail is not mine",
     "and that what I would fail is not mine"),

    ("you will spend your life tending things that stopped working before you arrived",
     "you will spend your life tending structures that stopped working before you arrived"),

    ("not a thing anyone can take over",
     "not a role anyone can take over"),

    ("The only thing that changed is what you gave it authority over.",
     "What changed is what you gave it authority over."),

    ("The Fixer-Healer developed does one thing nothing else in this chapter can do:",
     "The Fixer-Healer developed does what nothing else in this chapter can do:"),

    ("Make a list of three things in your current inheritance that you would fight to "
     "protect.",
     "Make a list of three practices in your current inheritance that you would fight to "
     "protect."),

    ("A thing you cannot name a breakage for is a preference wearing inheritance.",
     "Anything you cannot name a breakage for is a preference wearing inheritance."),

    ("Ask: what essential thing does this tradition try to do, and does the current form "
     "still do it?",
     "Ask: what is this tradition essentially trying to do, and does the current form "
     "still do it?"),

    ("The vow is that a thing you said was true stays true",
     "The vow is that what you said was true stays true"),

    ("and the choosing is the thing you handed him",
     "and the choosing is what you handed him"),

    ("Everything else on that list follows from a thing never having been taken on:",
     "Everything else on that list follows from one act never taken:"),

    ("One line, four things: what you will do, who it reaches, by when, and what it costs "
     "you. *Tend the Structure*",
     "One line: what you will do, who it reaches, by when, and what it costs you. *Tend "
     "the Structure*"),

    ("A system that makes the right thing the easy thing for the people inside it.",
     "A system that makes the right move the easy one for the people inside it."),
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
    print("ch5.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
