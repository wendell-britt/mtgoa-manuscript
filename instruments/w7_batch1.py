# -*- coding: utf-8 -*-
"""
W7 batch 1 — the 25 denying negations in the treatise halves (Sections 1-3).

Each was tested against RULE_COLLISIONS: is the negated thing still true when
the sentence ends? Ranking survives, denying gets cut. 23 fail and are rewritten
here. Two survive and are deliberately untouched:

  ch2:136  "The problem is not that you wanted to be good."  -> RANKING. She did
           want to be good; that stays true and is ranked under the real problem.
           Same shape as Adams' cave ladder.
  ch8:81   "That much is not in question."  -> FALSE POSITIVE. Idiomatic, not a
           definitional negation. The detector cannot see the difference; a human
           has to.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_batch1.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
2: [("""This theory is not wrong. It's incomplete.""",
     """This theory is incomplete rather than wrong.""")],

3: [("""That is not the Shaman's practice. That is the Shaman's practice with a governor on it""",
     """That is the Shaman's practice with a governor on it"""),
    ("""Function is not productivity. It is the difference between sensing a thing""",
     """Function is the difference between sensing a thing""")],

4: [("""The Challenger's gift is not the willingness to fight. The Challenger's gift is the willingness to *mean it.*""",
     """The Challenger's gift is the willingness to *mean it.*"""),
    ("""That is not anger. That is will.""",
     """That is will."""),
    ("""Force is not aggression. It is the willingness for a moment""",
     """Force is the willingness for a moment"""),
    ("""Restraint is not cowardice. It is what keeps a no worth something""",
     """Restraint is what keeps a no worth something""")],

5: [("""The Regent's gift is not loyalty to the past. The Regent's gift is the ability to pass something down""",
     """The Regent's gift is the ability to pass something down"""),
    ("""That gift is not the same as conservatism. It is not the same as rigidity. It is not the same as "this is how we've always done it." """.rstrip(),
     """That gift is distinct from conservatism, from rigidity, and from "this is how we've always done it." """.rstrip()),
    ("""That is not weakness. That is the Regent's pair in active tension.""",
     """That is the Regent's pair in active tension.""")],

6: [("""Because allyship is not primarily a problem of individual behavior. It's a problem of system design.""",
     """Because allyship is a problem of system design before it is a problem of individual behavior."""),
    ("""So the drift is not toward cruelty. It is toward a structural account""",
     """So the drift runs toward a structural account""")],

7: [("""The Diplomat is not a cold person. The Diplomat is not a pushover who cannot hold the field. The Diplomat is the negotiator who has learned that love is not demonstrated through infinite presence — it is demonstrated through honest stake-surfacing, timely closure, and the willingness to let the field decide what it can actually hold.""",
     """The Diplomat is the negotiator who has learned that love is demonstrated through honest stake-surfacing, timely closure, and the willingness to let the field decide what it can actually hold, rather than through infinite presence."""),
    ("""It is not niceness. It is not conflict-avoidance dressed in the language of harmony. It is not the absence of judgment in the service of false peace. It is the altitude at which""",
     """Niceness, conflict-avoidance dressed in the language of harmony, and the absence of judgment in the service of false peace are all mistaken for it. It is the altitude at which"""),
    ("""That decision is not cowardice, and it is not a failure of nerve. It is an accurate reading of a specific misuse.""",
     """That decision is an accurate reading of a specific misuse."""),
    ("""Care is not sentiment. It is the maintenance of the only medium""",
     """Care is the maintenance of the only medium"""),
    ("""Impact is not brutality. It is the willingness for a relationship""",
     """Impact is the willingness for a relationship""")],

8: [("""The Sage in distortion is not stupid and is not malicious. It is doing versions of useful things""",
     """The Sage in distortion is doing versions of useful things"""),
    ("""The Sage's journey is not upward. It is inward and then back.""",
     """The Sage's journey runs inward and then back."""),
    ("""The failure is not choosing one. The failure is letting one answer the other's question.""",
     """You may choose one. The failure is letting one answer the other's question.""")],

9: [("""That the goal is not to arrive at Sage and stay there. The goal is to be able to play any game the village needs played, whatever the moment requires.""",
     """That the goal is to be able to play any game the village needs played, whatever the moment requires, rather than to arrive at Sage and stay there."""),
    ("""That's not a list of credentials. That's a design system.""",
     """That's a design system.""")],
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
    print("applied %d rewrites (2 sites deliberately kept — see docstring)"
          % sum(n for *_, n in plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
