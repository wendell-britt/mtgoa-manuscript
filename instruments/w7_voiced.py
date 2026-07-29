# -*- coding: utf-8 -*-
"""
W7 voiced pass — vary the synthesis line to each Head's genre.

The synthesis pass collapsed the polarities into one sentence each, and produced
its own formula: 9 of 12 were copula "[NOUN] is [NOUN-phrase]", with two exact
twin pairs sitting adjacent in the same chapter — Force/Restraint in ch4,
Care/Impact in ch7. Those are the two places a reader meets them back to back.
The skill's robotic-rhythm rule names it, and several also read as appended
aphorisms (its fake-profound-kicker rule).

Each line now takes the shape of the Head whose treatise it sits in, per
SEVEN_VOICES. This is the last pass in the sequence and the one that pays twice:
the sentences stop rhyming with each other and start doing W3's genre-marker
work.

  Voss   sensation before concept, ends without conclusion
  Ash    second-person imperative, states a cost, nothing softens
  Quill  formal periodic, cites prior keepers, written versus kept
  Vale   *in practice*, stated tolerance, closes like a door
  Cross  two positions before one, names what each party protects
  Orr    cites another school, disagrees courteously, holds the contradiction

    python3 marginalia/compile.py --strip
    python3 instruments/w7_voiced.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
# VOSS — body first, then the concept, and no conclusion offered
3: [(""" Function is where the feeling arrives in somebody other than you.""",
     """ You felt it in your chest. Function is whether anybody else ever did.""")],

# ASH — imperatives and a stated cost; three lines, three shapes
4: [(""" Fighting is what meaning it looks like from outside.""",
     """ From outside it will look like fighting. Ignore that."""),
    ("""Will is what anger becomes when you keep it past the heat.""",
     """Keep the anger past the heat. What is left is will."""),
    (""" Force is what aggression becomes when you agree to be the one who pays for it.""",
     """ Agree to be the one who pays for the crossing and the aggression becomes force."""),
    (""" Restraint is the same silence as cowardice, chosen.""",
     """ You will look like a coward. The difference is that you could have spoken.""")],

# QUILL — periodic, formal, and one citation of prior keepers
5: [(""" The gift is loyalty turned to face the people who have not arrived yet.""",
     """ The gift is loyalty as it is kept for those who have not yet arrived."""),
    (""" Holding two live poles feels like weakness from the inside.""",
     """ It is recorded here because from the inside it reads as weakness, and keepers before you have filed it under that name.""")],

# VALE — the verbal tic, and a specification that closes like a door
6: [(""" This is the cruelty that arrives sounding like rigour.""",
     """ In practice it is cruelty, specified as rigour.""")],

# CROSS — both protections named, which is his native form rather than a default
7: [(""" Care is sentiment that shows up to do maintenance.""",
     """ Sentiment protects how the connection feels; care protects whether it still works."""),
    (""" Impact is brutality that knows what it is buying.""",
     """ Brutality spends the relationship without pricing it. Impact names the price first and spends it anyway.""")],

# ORR — cites another school, disagrees courteously, deflects from himself
8: [(""" It gains its altitude by going in.""",
     """ Corin would call going inward a retreat, and he would be right about the movement and wrong about where it ends.""")],

# the student, no profile — keep it plain
9: [(""" Every line of it is something you have been, and that is what makes it something you can build with.""",
     """ Every line of it is something you have already been. That is what makes it usable.""")],
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
    print("voiced %d" % sum(n for *_, n in plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
