# -*- coding: utf-8 -*-
"""cut_cards_ch3 -- take the phantom deck out of ch3 (2026-09-09). Companion to
cut_cards_ch4_9.py; see its docstring for the ruling. ch3 is where the deck was introduced,
so its section carries the "operation" and "a hundred and twenty" apparatus the others only
refer back to. The Alchemist's category is order item 5 and is not touched here.

Every edit is (old, new), asserted to match exactly once.
    python3 instruments/cut_cards_ch3.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# the Tell logs to a card that does not exist
("So the answer goes on the card in writing, where a later you can read it back.",
 "So the answer goes in your log in writing, where a later you can read it back."),
# heading + the deck's introduction
("""## Your Twenty Cards

The Shaman is a Face. In the deck it is also an *operation* every move can run, which means you are not holding an archetype. You are holding twenty specific cards.

Here is where they come from. The deck runs five basic moves, and you already know all five, because they are the Five-Move Form: Wake Up, Open Up, Clean Up, Grow Up, Show Up. Cross those against the four domains where allyship stops being interior and goes external (gathering resources, raising awareness, direct action, skillful organizing), and five times four gives twenty. Twenty cards per operation, a hundred and twenty in the deck. These twenty are the Shaman's.

*Your twenty live in the deck rather than on this page: five basic moves against four domains, one card per crossing. You do not have to learn them. You have to find yours, and you already know the five moves that get you there.*

The five moves are this chapter, in order. Every stage you practiced is one of them. Clean Up holds the five channels, which is why all four of those cards begin with the same verb: *name.* Pick a domain instead and you are choosing where the move lands. The five are the sequence; the four domains are the arena.""",
 """## The Shaman Is a Move You Run

The Shaman is a Face, but it is also a move you can run, which means you are not holding an archetype. You are holding a practice: the Five-Move Form, Wake Up, Open Up, Clean Up, Grow Up, Show Up. This chapter was the five, in order, and every stage you worked is one of them."""),
# the daemon section: keep the question the deck framing carried
("""### Drawing Against the Shadow

Draw from your twenty rather than the hundred and twenty. Which twenty is easy. Which of the five rows is the real question, and a tempting wrong answer waits: that a shadow lives at one move and the other four are clean.""",
 """### Where the Daemon Bites

Which of the five moves your daemon corrupts is the real question, and a tempting wrong answer waits: that a shadow lives at one move and the other four are clean."""),
("exactly what makes the five worth having, because each of those failures has cards sitting beside it.",
 "exactly what makes the five worth having: each move shows you the same rule from a different side."),
# the guided pass: one pass of the Form, no card coordinate, no domain crossing
("""Take **What Seeing Costs**: Open Up, Raise Awareness, Shaman. Its question is the one the Controller exists to route around: *what am I actually feeling?* The card does not want the feeling the situation warrants, or the one a person at your level of understanding ought to have. It wants what is here.

Run it once, on something real. Bring a time""",
 """Run it once, on something real. Take the move called **What Seeing Costs**, the Shaman's version of Open Up, whose question is the one the Controller exists to route around: *what am I actually feeling?* It does not want the feeling the situation warrants, or the one a person at your level of understanding ought to have. It wants what is here.

Bring a time"""),
("Show Up: pick one of the four domains and say where this goes.",
 "Show Up: say it, out loud, to the person it concerns."),
("Five moves, one card, about ninety seconds. That is a full pass of the Form with an instrument in your hand.",
 "Five moves, one pass, about ninety seconds. That is the whole Form with an instrument in your hand."),
# the quest
("""### From Card to Quest

A card that ends in a notebook is a card you read. A card that ends in a quest is a card you played, and the difference is a person.""",
 """### From Read to Quest

A reading that ends in a notebook is a reading you had. A reading that ends in a quest is one you played, and the difference is a person."""),
("Quests come from the Show Up cards, and every one of them ends in an artifact, and an artifact is something another person can encounter.",
 "A quest comes out of Show Up, the move that takes the reading into the world, and every one of them ends in an artifact, which is something another person can encounter."),
("*Draw one card from your twenty. Run the five moves on a live situation.",
 "*Run the five moves on a live situation."),
]

def main():
    t = io.open(P, encoding="utf-8").read()
    for old, new in EDITS:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("EDIT matched %d times (need 1): %r\n" % (c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch3 card cut: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
