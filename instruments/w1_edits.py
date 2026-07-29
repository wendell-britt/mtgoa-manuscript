# -*- coding: utf-8 -*-
"""
W1 of specs/SPEC_FINISHING_PASS_2026-07-29.md — clear the body's hard-gate hits
and the adjudicated denying negations. Also carries D1 from the work order,
because it sits in the same paragraph as the ch6 negation.

Follows the spec_edit.py contract: every anchor must match exactly once or the
run aborts having written nothing.

Run against a STRIPPED manuscript:
    python3 marginalia/compile.py --strip
    python3 instruments/w1_edits.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
 3: [
  # gate/stack — Wendell, card apparatus. State the card's want directly.
  ("""*what am I actually feeling?* Not what the situation warrants. Not what a person at your level of understanding ought to feel. What is here.""",
   """*what am I actually feeling?* The card does not want the feeling the situation warrants, or the one a person at your level of understanding ought to have. It wants what is here."""),
 ],
 6: [
  # D1 (template opener, ch6 the only inheritor) + the negation, one paragraph.
  # Irix Vale: state the specification rather than circling it.
  ("""Let's be clear about what we mean when we say *structural design.*

It's not organizational design. That's the village version — the org chart, the RACI matrix, the role description, the meeting cadence.""",
   """The village version of *structural design* is organizational design — the org chart, the RACI matrix, the role description, the meeting cadence."""),
  # gate/stack — ranking kept, expressed by subordination instead of a stack.
  ("""**Every system produces the outcomes it's designed to produce.** Not the outcomes the founders intended. Not the outcomes the mission statement describes. The outcomes the incentive structure actually rewards.""",
   """**Every system produces the outcomes it's designed to produce** — the outcomes the incentive structure actually rewards, which are rarely the ones the founders intended or the ones the mission statement describes."""),
  # banned word, card name. Sole occurrence; no downstream dependency in repo.
  ("""The Capacity in the Room""", """The Capacity in the Group"""),
 ],
 7: [
  # gate/stack — Elian Cross, negotiation casebook. Formal, states the positive.
  ("""Not a demand. Not a condition of continued affection. A fact about the arrangement, delivered while there is still time for anyone to do something with it.""",
   """It is a fact about the arrangement rather than a demand or a condition of continued affection, and it is delivered while there is still time for anyone to do something with it."""),
 ],
 8: [
  # gate/stack — Wendell, Section 4 practice register. Imperative fits the step.
  ("""Not as diagnosis. Not as verdict. As offering.""",
   """Say it as an offering rather than as a diagnosis or a verdict."""),
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
                print("ABORT ch%d edit #%d: %d matches for %r" % (ch, i, n, a[:70]))
                return 1
            t = t.replace(a, b, 1)
        plan.append((p, t, len(reps)))

    for p, t, n in plan:
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%s: %d edit(s)" % (os.path.basename(p)[2:-3], n))
    print("applied %d edits across %d chapters" % (sum(n for _, _, n in plan), len(plan)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
