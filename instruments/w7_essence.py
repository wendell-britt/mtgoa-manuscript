# -*- coding: utf-8 -*-
"""
W7 essence pass — restore what batch 1's mechanical cuts threw away.

Batch 1 cleared the denying negations by deleting the negated clause and keeping
the positive. That is correct as far as the rule goes and wrong as writing: each
negation was protecting its term against a specific caricature, and deleting it
removed both the beat and the distinction. "That is not anger. That is will."
became "That is will.", floating with nothing to push against.

The fix is not to restore the negation. It is to say the true thing the negation
was gesturing at — usually a contrast between two verbs, stated positively.
Sentiment *feels*; care *maintains*. Aggression spends *someone else*; force
spends *you*. Cowardice *cannot* spend; restraint *declines to*.

Ch4 lost a matched pair — fight/mean-it opening the passage, anger/will closing
it — so both ends are rebuilt.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_essence.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
# Voss — productivity counts output, function counts arrival
3: [("""Function is the difference between sensing a thing and the thing being sensed *in the world*, where the person you came for can get something out of it.""",
     """Function is the difference between sensing a thing and the thing being sensed *in the world*, where the person you came for can get something out of it. Productivity counts what you produced. Function counts what arrived.""")],

# Ash — the matched pair, both ends
4: [("""The Challenger's gift is the willingness to *mean it.*""",
     """The Challenger's gift is the willingness to *mean it.* Fighting is the cheap part."""),
    ("""That is will.""",
     """Anger arrives and leaves. What is still standing when it has gone is will."""),
    ("""Force is the willingness for a moment to be more expensive because you were in it.""",
     """Force is the willingness for a moment to be more expensive because you were in it. Aggression spends someone else. Force spends you."""),
    ("""because the line stops being information about the world and turns into weather.""",
     """because the line stops being information about the world and turns into weather. Cowardice cannot spend. Restraint declines to.""")],

# Quill — loyalty faces backward, the gift faces forward
5: [("""that can survive the loss of its founder.""",
     """that can survive the loss of its founder. Loyalty faces the people who came before. The gift faces the ones who come after."""),
    ("""That is the Regent's pair in active tension.""",
     """That is the Regent's pair in active tension. From the inside it feels like weakness, and the feeling is how you know both poles are still live.""")],

# Vale — cruelty announces itself; this does not
6: [("""which is the one account that never requires you to have been there as a person.""",
     """which is the one account that never requires you to have been there as a person. Cruelty would announce itself. This arrives sounding like rigour.""")],

# Cross — the Care/Impact pair, each against its caricature
7: [("""That decision is an accurate reading of a specific misuse.""",
     """That decision is an accurate reading of a specific misuse, which is why nobody has ever talked her out of it."""),
    ("""Care is the maintenance of the only medium through which anything relational travels.""",
     """Care is the maintenance of the only medium through which anything relational travels. Sentiment feels warmly about a connection; care is the upkeep."""),
    ("""Impact is the willingness for a relationship to be spent on something, rather than preserved as an end in itself.""",
     """Impact is the willingness for a relationship to be spent on something, rather than preserved as an end in itself. Brutality spends a relationship without noticing. Impact spends it on purpose.""")],

# Orr — the expectation he is deflecting
8: [("""The Sage's journey runs inward and then back.""",
     """The Sage's journey runs inward and then back. Everyone expects it to run up.""")],

# the student — résumé versus toolkit
9: [("""That's a design system.""",
     """That's a design system. It reads like a list of things you have been. It is a list of things you can build with.""")],
}


def main():
    plan = []
    for ch, reps in sorted(EDITS.items()):
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        for i, (a, b) in enumerate(reps, 1):
            n = t.count(a)
            if n != 1:
                print("ABORT ch%d #%d: %d matches for %r" % (ch, i, n, a[:66]))
                return 1
            t = t.replace(a, b, 1)
        plan.append((ch, p, t, len(reps)))

    for ch, p, t, n in plan:
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: %d" % (ch, n))
    print("restored %d beats" % sum(n for *_, n in plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
