# -*- coding: utf-8 -*-
"""
W9, finished: ch2's 34 prose em-dashes.

SPEC_EMDASH_AND_DENSITY 1.6 called ch2 *"done at 5.2 and the reference, not a
target."* That was true when the target was a rate. It is not true now that the
finish line is the one ch3 and ch7 were taken to, so ch2 goes to zero with the rest.

**ch2 is the book's most colon-dense chapter at 16.6/1k**, against a book average
of 12.4 and 2.9 in the control text. So the conversions here steer to comma and
parenthesis wherever the sentence allows it, and the colon is spent only where the
left-hand side is a genuine list or a naming. Six colons in thirty-four.

  6 colon  ·  12 comma  ·  14 parenthesis (seven pairs)  ·  2 full stop
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # -- comma ------------------------------------------------------------------
    ("Just the feeling — the one that shows up late at night",
     "Just the feeling, the one that shows up late at night"),

    ("hit a moment when the map turns out to be wrong — not about the destination, "
     "about where they had to start.",
     "hit a moment when the map turns out to be wrong, not about the destination, "
     "about where they had to start."),

    ("The feedback — when it comes — comes fast",
     "The feedback, when it comes, comes fast"),

    ("the read gets set aside for the consensus — not for lack of capacity, but "
     "because body-knowing",
     "the read gets set aside for the consensus, not for lack of capacity, but "
     "because body-knowing"),

    ("to keep my feelings below the waterline — away from other people's awareness, "
     "and often away from my own.",
     "to keep my feelings below the waterline, away from other people's awareness, "
     "and often away from my own."),

    ("The Protector is the hull of the ship — the body itself, holding its shape, "
     "keeping the water out, taking the hit when a hit comes.",
     "The Protector is the hull of the ship, the body itself, holding its shape, "
     "keeping the water out, taking the hit when a hit comes."),

    ("because it only works by making the other person part of you — and the person "
     "you are allying with is not you.",
     "because it only works by making the other person part of you, and the person "
     "you are allying with is not you."),

    ("it lets you name one line — \"I'm open to challenge; I'm not available for "
     "personal attacks\" — and stay in the conversation.",
     "it lets you name one line, \"I'm open to challenge; I'm not available for "
     "personal attacks,\" and stay in the conversation."),

    ("say one body-read out loud to another person — and say it to someone where it "
     "isn't already safe to",
     "say one body-read out loud to another person, and say it to someone where it "
     "isn't already safe to"),

    ("Run it right after the next hard moment — not at the end of the week, not when "
     "you have time, right after",
     "Run it right after the next hard moment, not at the end of the week, not when "
     "you have time, right after"),

    ("what changed in me, others, or the situation — and what will I run next time?",
     "what changed in me, others, or the situation, and what will I run next time?"),

    ("The Shaman trains emotional signal-reading and regulation — the base layer the "
     "other faces depend on, and the reason to start there.",
     "The Shaman trains emotional signal-reading and regulation, the base layer the "
     "other faces depend on, and the reason to start there."),

    # -- parentheses: a true aside carrying its own internal commas ---------------
    ("They were not okay — disturbed, shaken, holding something they didn't know how "
     "to hold — and they delivered it to me, gift-wrapped as concern.",
     "They were not okay (disturbed, shaken, holding something they didn't know how "
     "to hold), and they delivered it to me, gift-wrapped as concern."),

    ("The instant something reads as a threat — a shift in tone, a move for power — "
     "the Protector has already braced to meet it, faster than thought.",
     "The instant something reads as a threat (a shift in tone, a move for power), "
     "the Protector has already braced to meet it, faster than thought."),

    ("the Protector goes back to its real job — protecting you when you actually need "
     "it — and stops running every hard conversation",
     "the Protector goes back to its real job (protecting you when you actually need "
     "it) and stops running every hard conversation"),

    ("the charge you feel has channels — fear, anger, sadness, joy, neutrality — and "
     "each one is information, not noise.",
     "the charge you feel has channels (fear, anger, sadness, joy, neutrality), and "
     "each one is information, not noise."),

    ("The practice format in this book — naming where you are now, finding where you "
     "want to be, and building the path between them — comes from Gerard Egan's",
     "The practice format in this book (naming where you are now, finding where you "
     "want to be, and building the path between them) comes from Gerard Egan's"),

    ("The part of you that reads a group — the one that clocks when a meeting has gone "
     "cold before anyone speaks — has been living in exile.",
     "The part of you that reads a group (the one that clocks when a meeting has gone "
     "cold before anyone speaks) has been living in exile."),

    ("A sensation I couldn't name, small enough that I almost dismissed it — just a "
     "low friction, persistent, the way a stone in your shoe is not agony but is also "
     "not nothing.",
     "A sensation I couldn't name, small enough that I almost dismissed it (just a "
     "low friction, persistent, the way a stone in your shoe is not agony but is also "
     "not nothing)."),

    # -- colon: the left side is a list, or the tail names it ---------------------
    ("The ones who don't push through instead of going through — they override the "
     "sensation",
     "The ones who don't push through instead of going through: they override the "
     "sensation"),

    ("My phone started filling up — white friends, mostly, checking in, asking if I "
     "was okay.",
     "My phone started filling up: white friends, mostly, checking in, asking if I "
     "was okay."),

    ("The difference shows up in a single moment — say someone challenges you in a "
     "meeting.",
     "The difference shows up in a single moment: say someone challenges you in a "
     "meeting."),

    ("Chest, throat, jaw, belly — somewhere in there sits a sensation that hasn't "
     "resolved.",
     "Chest, throat, jaw, belly: somewhere in there sits a sensation that hasn't "
     "resolved."),

    ("the work in this book unfolds in four directions — gathering resources, skillful "
     "organizing, taking direct action, and raising awareness.",
     "the work in this book unfolds in four directions: gathering resources, skillful "
     "organizing, taking direct action, and raising awareness."),

    # -- full stop: two independent sentences ------------------------------------
    ("The daemon work doesn't ask you to fix the Shadow — it asks you to find out what "
     "it has been protecting.",
     "The daemon work doesn't ask you to fix the Shadow. It asks you to find out what "
     "it has been protecting."),

    # Spoken line. The dash was doing the job a full stop does in speech, and both
    # halves are things a person actually says.
    ("*\"Something just shifted in my chest — give me a second.\"*",
     "*\"Something just shifted in my chest. Give me a second.\"*"),
]


def main():
    p = os.path.join(MS, "ch2.md")
    t = io.open(p, encoding="utf-8").read()
    bad = []
    for i, (old, new) in enumerate(E, 1):
        n = t.count(old)
        if n != 1:
            bad.append("#%d matched %d times: %r" % (i, n, old[:64]))
            continue
        t = t.replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        io.open(p, "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
