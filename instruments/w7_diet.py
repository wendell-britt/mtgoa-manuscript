# -*- coding: utf-8 -*-
"""
Apply the three grammar moves to my own W7 rewrites.

prose_diet.py showed the ~1,300 words written across the W7 passes running 69%
heavier on be-verbs, 85% on copula-as-main-verb, 38% on "it" and 71% on
nominalizations than the book around them. This fixes the sites where the
diagnosis is real.

Selected by judgment, not by ratio. Per-sentence ratios are noise — one zombie
noun in an eight-word sentence reads as 11x — so the aggregate finding drove the
search and Lanham's and Sword's tests decided each site.

Sites left alone on purpose:
  "The danger is pretending costly moves are renewable."  Wendell's own
      phrasing; W7 only cut the half in front of it.
  "Sentiment protects how the connection feels..."  *Connection* is a defined
      term in this book, which is Williams' familiar-concept licence.
  "The Founder is the moment you stop consuming and start creating."  Defining
      a term, which is the licensed copula.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_diet.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
4: [
  # zombie: "the willingness" is the verb *mean* wearing a noun. Ash's line, and
  # a definition, so the copula stays; the nominalization goes.
  ("""The Challenger's gift is the willingness to *mean it.*""",
   """The Challenger's gift is meaning it."""),
  # copula + "the difference" as a zombie subject. Paramedic: the action is
  # *could have spoken*, so give it to the two people doing it.
  ("""You will look like a coward. The difference is that you could have spoken.""",
   """You will look like a coward. The coward could not have spoken. You could."""),
],
9: [
  # "An organization is" — copula fronting a nominalization. Give it a verb.
  ("""An organization is one thing that can come out of that, and usually doesn't.""",
   """Sometimes an organization comes out of that. Usually nothing does."""),
  # two "it"s in one clause, the second with no clean antecedent
  ("""That's the stage you're in, and it feels like failure from inside it.""",
   """That's the stage you're in, and from inside it feels like failure."""),
  # orphan "it": the antecedent sits a sentence back. Name the noun.
  ("""Every line of it is something you have already been. That is what makes it usable.""",
   """Every line of that list is something you have already been. That is what makes it usable."""),
],
5: [
  # "filed it under that name" — "it" and "that name" both point backwards past
  # a clause boundary. Quill can say the noun and keep her register.
  ("""reads as weakness, and keepers before you have filed it under that name.""",
   """reads as weakness, and keepers before you have filed the tension under that name."""),
],
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
    print("applied %d" % sum(n for *_, n in plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
