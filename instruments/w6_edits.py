# -*- coding: utf-8 -*-
"""
W6 of specs/SPEC_FINISHING_PASS_2026-07-29.md — retire the "village version"
formula. Five sentences, one per Section 3, each carrying a distinct active verb
for how the village mis-reads that Face's lesson.

ch4 additionally carries Corin Ash's register per marginalia/specs/HEAD_REGISTERS.md:
dissatisfaction as biography, third person kept for the Face, first person only
on the cost. Its two biography facts are unfilled placeholders — see R9.
instruments/gate.py fails on any surviving token.

Run against a STRIPPED manuscript:
    python3 marginalia/compile.py --strip
    python3 instruments/w6_edits.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
 # Maera Voss — the village makes the practice smaller than it is.
 3: [("""It's not emotional processing. That's the village version — the neat, linear model where you *identify* the emotion, *understand* where it came from, *release* it, and then *move on.* That model treats emotions like a problem that has a solution. Once you solve it, it's gone. That's not emotional alchemy.""",
      """The village shrinks alchemy into processing: *identify* the emotion, *understand* where it came from, *release* it, and then *move on.* That model treats emotions like a problem that has a solution. Once you solve it, it's gone.""")],

 # Corin Ash — mishearing, which is the Challenger's predicament. Register: the
 # cost arrives in first person, the Face stays in third.
 4: [("""It's not aggression. That's the village version — the Challenger as the angry one, the difficult one, the one who makes things worse before they get better. The Challenger as someone who says no because they want to win. That version exists, and you've probably met them, and they are not what we're talking about here.""",
      """The village hears the clean no as aggression: the angry one, the difficult one, the one who makes things worse before they get better, someone who says no because they want to win. I was told that at ⟦ASH-AGE⟧, by people who meant well, and I believed them for ⟦ASH-SPAN⟧. The version they were describing does exist, and you've probably met them, and it is not what we're talking about here.""")],

 # Sera Quill — hoarding against transmission. "Keeps" is her own vocabulary:
 # SEVEN_VOICES has her distinguishing the practice as written from as kept.
 5: [("""It's not nostalgia. That's the village version — the version that says "we do it this way because we've always done it this way." That version treats tradition as a *relic* — something preserved because it's old, not because it works. That's not the Regent's practice. That's a cargo cult of the Regent's practice.""",
      """The village keeps tradition instead of passing it on: "we do it this way because we've always done it this way." That treats a practice as a *relic* — preserved because it is old, rather than because it works. It is a cargo cult of the Regent's practice.""")],

 # Irix Vale — mistaking artifacts for the work. Engineering register.
 6: [("""The village version of *structural design* is organizational design — the org chart, the RACI matrix, the role description, the meeting cadence. Those are outputs of structural thinking, not structural thinking itself. You can have all those things and still have a broken system.""",
      """The village reduces structural design to its outputs: the org chart, the RACI matrix, the role description, the meeting cadence. Those are what structural thinking produces, not structural thinking itself. You can have all of them and still have a broken system.""")],

 # Elian Cross — rigidity. An ultimatum is a term that has set.
 7: [("""The village version is the ultimatum.""",
      """The village hardens terms into ultimatums.""")],
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
        plan.append((ch, p, t, len(reps)))

    for ch, p, t, n in plan:
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: %d edit(s)" % (ch, n))
    print("applied %d edits across %d chapters" % (sum(n for *_, n in plan), len(plan)))
    print("NOTE: ch4 carries 2 unfilled placeholders (R9). gate.py will report them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
