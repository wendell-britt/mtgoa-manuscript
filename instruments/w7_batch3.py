# -*- coding: utf-8 -*-
"""
W7 batch 3 — ch8, ch5, ch6. 34 candidates, 31 edits, one pass.

Method per MANUSCRIPT_FILE_CANON: cut, essence, synthesize, voice. Register is
Wendell's for 32 of 34 sites, so move 4 is his genre — second person, testimony
before instruction, punchline last, admits the thing before teaching the fix.

Three candidates are deliberately not edited:
  ch8:81, ch8:144  known false positives, asserted in test_toolchain.py.
  ch5:201  "not emotion. It's not will. It's not even logic. It's loyalty" —
           ranking, licensed by RULE_COLLISIONS. "Not even" is the escalation
           marker; the negated items stay true and are ranked under loyalty.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_batch3.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
8: [
("""Inner work is not a delay tactic. It is the thing that keeps the response clean enough to still be usable tomorrow.""",
 """Inner work is what keeps the response clean enough to still be usable tomorrow. It looks like delay from outside, and from inside on a bad day."""),
("""That gap is not the end of the view. It's the beginning of the work.""",
 """That gap is where the work starts, which is easy to mistake for the view ending."""),
("""The wonder is not the field turning out to be bigger than it looked. It's the field being exactly what it is, and you being able to stay curious about that.""",
 """The wonder is the field being exactly what it is, and you staying curious about that anyway. Nothing has to turn out bigger than it looked."""),
("""The triumph is not the view from above. It's going down and coming back without feeling diminished by the trip.""",
 """The triumph is going down and coming back without feeling diminished by the trip. The view from above was the easy half."""),
("""The bliss is not the game continuing. It's the discovery that the aliveness was never the game's property — it was yours, and it travels.""",
 """The bliss is discovering that the aliveness was never the game's property. It was yours, it travels, and the game is allowed to end."""),
("""The sadness is not weakness. It's the cost of the gift.""",
 """The sadness is the cost of the gift, and it will feel like weakness every time."""),
("""The poignance is not the loss. It's the moment where the distance between what you see and where they are becomes the place love happens.""",
 """The poignance is the moment the distance between what you see and where they are becomes the place love happens. The loss is what carries you there."""),
("""The distortion is not that it registers the difference. The distortion is what it does with the reading.""",
 """Registering the difference is the gift working. The distortion is what it does with the reading."""),
("""That's not the view talking. That's attachment to the view.""",
 """That's attachment to the view, wearing the view's voice."""),
("""That's not the Returner. That's exhaustion calling itself wisdom.""",
 """That's exhaustion calling itself wisdom, and it does a passable impression of the Returner."""),
("""Letting go is not giving up. It's saying: *this game was mine for a time, and it isn't anymore, and that's allowed.*""",
 """Letting go says *this game was mine for a time, and it isn't anymore, and that's allowed.* Giving up never bothers to say anything."""),
("""Holding the meta is not standing outside it. It's holding the view and still doing the thing the view is for.""",
 """Holding the meta means keeping the view and still doing the thing the view is for. Standing outside is the cheaper version."""),
],
5: [
("""That's not disloyalty. That's the most loyal thing there is.""",
 """That's the most loyal thing there is, and it will be read as disloyalty."""),
("""The first move is not to change anything. The first move is to acknowledge what arrived""",
 """The first move is to acknowledge what arrived, before you change any of it"""),
("""Stewarding is not passivity. It is the cost of keeping something alive while you figure out what it needs.""",
 """Stewarding is the cost of keeping something alive while you figure out what it needs. It looks like doing nothing and costs more."""),
("""The goal is not to reach Entrust and be done. The goal is to move through the cycle more consciously, more fully, each time.""",
 """The goal is to move through the cycle more consciously, more fully, each time. Entrust is a station on it, not the end of the line."""),
("""That is not meddling. That is the only reason anything inherited ever improves.""",
 """That is the only reason anything inherited ever improves, and it will look like meddling to somebody."""),
("""The distortion is not that it repairs. The distortion is what it attaches the repair to.""",
 """The repair itself is sound. The distortion is what gets attached to it."""),
("""The Regent's superpower is not endurance and it is not loyalty. It is the ability to put what you received into a form the next person can receive""",
 """The Regent's superpower is putting what you received into a form the next person can receive — endurance and loyalty are the entry requirements"""),
("""The Regent's first move is not action. The Regent's first move is witnessing.""",
 """The Regent's first move is witnessing. Action is the second."""),
("""That is not holding it. That is standing in for it.""",
 """That is standing in for it. Holding it would have cost more."""),
],
6: [
("""The test is not whether they can operate it. The test is whether they can *change* it""",
 """Operating it is the low bar. The test is whether they can *change* it"""),
("""That is not decoration. It is the reason the modes are five rather than three""",
 """That is the reason the modes are five rather than three"""),
("""The Emotional Body is not a strategy. It is the thing all four strategies are strategies *about.*""",
 """The Emotional Body is the thing all four strategies are strategies *about.*"""),
("""It is not a role. It is the instrument the roles are arguing with.""",
 """It is the instrument the roles are arguing with. No wonder it never gets a seat."""),
("""That is not intuition as a soft skill. That is the first stage of the practice, running on time.""",
 """That is the first stage of the practice, running on time. Calling it intuition undersells it by a stage."""),
("""The distortion is not that it feels. The distortion is how fast it hands the feeling off.""",
 """The distortion is how fast it hands the feeling off. Feeling it was never the issue."""),
("""The table is not responding to the analysis. The table is responding to the charge in it.""",
 """The table is responding to the charge underneath the analysis."""),
("""Emotional Body is not being suppressed. It is being *employed.* It is building things.""",
 """The Emotional Body is being *employed.* It is building things."""),
("""So the Architect's superpower is not the map. The map is the artifact, and you already know how to make one. The superpower is knowing where the push goes""",
 """So the map is the artifact, and you already know how to make one. The Architect's superpower is knowing where the push goes"""),
("""Naming an unstated assumption is not a small thing. It's the move that turns a good designer into a great one.""",
 """Naming an unstated assumption is the move that turns a good designer into a great one."""),
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
