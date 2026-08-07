# -*- coding: utf-8 -*-
"""ch4_thing.py — `thing` out of ch4. 38 of 39 body sites.

Wendell 2026-08-03: *"run all five and bring me one consolidated diff."*

Written under the rule his ch3 corrections produced: **pronoun with a real antecedent, or a
verb; a new noun last. If every site wants the same new noun, the sentence wanted a verb.
Indefinite article for an act, definite only when something named it. And look in the
surrounding paragraph before inventing a word** — three wrong guesses in ch1 and ch3 were
all cases where the passage had already supplied the answer.

## What ch4 supplied

`line` runs 151 in this chapter and `charge` is canon book-wide at 204. Between them they
take nine sites with nothing invented:

- `ch4:556` — *"Someone says the thing in the meeting"* → *"Someone crosses a line in the
  meeting."* The chapter is named for the line.
- `ch4:654`, `ch4:656` — *aim the smaller thing* → *aim the smaller charge*. Both sentences
  are about the size of a charge.
- The Skeptic's audit question at 536, 552 and 686 — *"is this the thing in front of me, or
  is this an old thing wearing today's clothes?"* → *"is this what is actually in front of
  me, or an old charge wearing today's clothes?"*

`ch4:117` and `ch4:303` and `ch4:636` are the ch1:113 shape again: the referent is named in
the very next sentence. *"letting things slide. Small violations first"* → *"letting
violations slide. Small ones first."* *"points at one specific thing. A line being crossed.
A commitment being violated."* → *"one specific event."*

## Held

`*Say the Thing*` at `ch4:752` is italicised as a card name, so it stays under the same
ruling that kept `Say the Thing Under the Thing`.

**Flagged, not fixed:** that card does not match this chapter. ch4's Show Up move is **Draw
the Line**, and the quest example under it is an apology for having been dismissive, which
is neither Say the Thing nor Draw the Line. ch3:962 runs the identical passage with its own
move name correctly. Wendell's call.

8 marginalia sites excluded by the usual convention.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch4.md"

E = [
    ("because they could say the thing that needed saying",
     "because they could say what needed saying"),

    ("were not the same thing as the Challenger's will",
     "were not the same as the Challenger's will"),

    ("is the same thing as exile",
     "is the same as exile"),

    # The next sentence names them.
    ("So the villagers started letting things slide. Small violations first. Then larger "
     "ones.",
     "So the villagers started letting violations slide. Small ones first. Then larger "
     "ones."),

    ("They could no longer hold those two things together without the Challenger.",
     "They could no longer hold both together without the Challenger."),

    ("the one who makes things worse before they get better",
     "the one who makes it worse before it gets better"),

    # The three sentences after it are the list.
    ("The charge points at one specific thing. A line being crossed.",
     "The charge points at one specific event. A line being crossed."),

    ("sudden explosions over small things",
     "sudden explosions over nothing"),

    ("the way people say things when they don't know who is listening",
     "the way people talk when they don't know who is listening"),

    ("The thing does not get said. A comment goes by.",
     "Nothing hard gets said. A comment goes by."),

    ("The swallower learns the thing that is least true of all:",
     "The swallower learns what is least true of all:"),

    ("whether the thing you reacted to was ever real",
     "whether what you reacted to was ever real"),

    ("*is this the thing in front of me, or is this an old thing wearing today's clothes?* "
     "Sometimes the honest answer names the old thing,",
     "*is this what is actually in front of me, or an old charge wearing today's clothes?* "
     "Sometimes the honest answer names the old charge,"),

    ("Tell me whether this is the thing in front of me or an old thing in its clothes",
     "Tell me whether this is what is in front of me or an old charge in its clothes"),

    # `line` runs 151 in this chapter.
    ("Someone says the thing in the meeting.",
     "Someone crosses a line in the meeting."),

    # Same fix as ch3:779 and ch7:590.
    ("The Skeptic developed does one thing for you that nothing else in this chapter can:",
     "The Skeptic developed does what nothing else in this chapter can:"),

    ("*We're not addressing the thing that just happened. I'd like to.*",
     "*We're not addressing what just happened. I'd like to.*"),

    ("Most situations have a specific thing, a violation or a dismissal or a boundary "
     "crossed,",
     "Most situations have a specific event, a violation or a dismissal or a boundary "
     "crossed,"),

    ("You just need the thing to exist as a named reality.",
     "You just need it to exist as a named reality."),

    ("**Why it matters:** Unnamed things feel larger than named things.",
     "**Why it matters:** What goes unnamed feels larger than what gets named."),

    ("**The test:** The thing is now named, stated plainly,",
     "**The test:** It is now named, stated plainly,"),

    ("you aim the smaller thing, so you draw the line a mild irritation would draw",
     "you aim the smaller charge, so you draw the line a mild irritation would draw"),

    ("the reading you now have is a reading of the smaller thing",
     "the reading you now have is a reading of the smaller charge"),

    ("You are going to say the hard thing either way",
     "You are going to speak either way"),

    ("Find the thing all five have in common.",
     "Find what all five have in common."),

    ("whether you met the thing in front of you or an old thing wearing today's clothes",
     "whether you met what was in front of you or an old charge wearing today's clothes"),

    ("the record of who did the thing",
     "the record of who did what"),

    ("Wake Up names four things you do not look at. Show Up names four things that happen "
     "in front of other people.",
     "Wake Up names four cards you do not look at. Show Up names four that happen in front "
     "of other people."),

    ("often the best thing said at the table",
     "often the best read at the table"),

    ("The Skeptic's remit is whether the thing was ever real",
     "The Skeptic's remit is whether it was ever real"),

    # Same fix as ch3:962 and ch7:777, keeping the artifact formula identical book-wide.
    ("One line, four things: what you will do, who it reaches, by when, and what it costs "
     "you. *Say the Thing*",
     "One line: what you will do, who it reaches, by when, and what it costs you. *Say the "
     "Thing*"),

    ("the version of myself that gets things right the first time",
     "the version of myself that gets it right the first time"),
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
    print("ch4.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
