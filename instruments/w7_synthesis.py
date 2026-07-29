# -*- coding: utf-8 -*-
"""
W7 synthesis pass — collapse the contrast pairs into single sentences.

The essence pass replaced deleted negations with two-clause contrasts:
"Aggression spends someone else. Force spends you." Grammatically positive, but
still staging an opposition — the reader hears the negation the syntax is
avoiding.

The book already rules on this. Chapter 3: *two legitimate poles, your position
on the axis, one action containing both.* Every one of these sites sits on a
named pair — Feeling ↔ Function, Force ↔ Restraint, Care ↔ Impact, honor ↔
reform — so the sentence should hold the axis rather than pick a side of it.

The move is X-is-Y-transformed rather than X-not-Y or X-versus-Y:

    Will is what anger becomes when you keep it past the heat.
    Care is sentiment that shows up to do maintenance.
    Impact is brutality that knows what it is buying.
    Restraint is the same silence as cowardice, chosen.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_synthesis.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
# Feeling ↔ Function
3: [(""" Productivity counts what you produced. Function counts what arrived.""",
     """ Function is where the feeling arrives in somebody other than you.""")],

# Force ↔ Restraint, plus the fight/will frame that brackets the passage
4: [(""" Fighting is the cheap part.""",
     """ Fighting is what meaning it looks like from outside."""),
    ("""Anger arrives and leaves. What is still standing when it has gone is will.""",
     """Will is what anger becomes when you keep it past the heat."""),
    (""" Aggression spends someone else. Force spends you.""",
     """ Force is what aggression becomes when you agree to be the one who pays for it."""),
    (""" Cowardice cannot spend. Restraint declines to.""",
     """ Restraint is the same silence as cowardice, chosen.""")],

# honor ↔ reform
5: [(""" Loyalty faces the people who came before. The gift faces the ones who come after.""",
     """ The gift is loyalty turned to face the people who have not arrived yet."""),
    (""" From the inside it feels like weakness, and the feeling is how you know both poles are still live.""",
     """ From the inside the tension reads as weakness, which is what holding two live poles feels like.""")],

# structure ↔ agency
6: [(""" Cruelty would announce itself. This arrives sounding like rigour.""",
     """ This is the cruelty that arrives sounding like rigour.""")],

# Care ↔ Impact
7: [(""" Sentiment feels warmly about a connection; care is the upkeep.""",
     """ Care is sentiment that shows up to do maintenance."""),
    (""" Brutality spends a relationship without noticing. Impact spends it on purpose.""",
     """ Impact is brutality that knows what it is buying.""")],

# altitude ↔ return
8: [(""" Everyone expects it to run up.""",
     """ It gains its altitude by going in.""")],

# who you have been ↔ what you can build
9: [(""" It reads like a list of things you have been. It is a list of things you can build with.""",
     """ Every line of it is something you have been, and that is what makes it something you can build with.""")],
}


def main():
    plan = []
    for ch, reps in sorted(EDITS.items()):
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        for i, (a, b) in enumerate(reps, 1):
            n = t.count(a)
            if n != 1:
                print("ABORT ch%d #%d: %d matches for %r" % (ch, i, n, a[:64]))
                return 1
            t = t.replace(a, b, 1)
        plan.append((ch, p, t, len(reps)))

    for ch, p, t, n in plan:
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: %d" % (ch, n))
    print("synthesized %d" % sum(n for *_, n in plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
