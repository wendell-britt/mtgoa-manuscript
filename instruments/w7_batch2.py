# -*- coding: utf-8 -*-
"""
W7 batch 2 — ch9 and ch3, run as a single four-move pass.

First batch to use the method recorded in MANUSCRIPT_FILE_CANON.md rather than
arriving at it: cut, essence, synthesize, voice, in one edit per site.

These sit in Wendell's register, not a Head's, so move 4 is his genre from
SEVEN_VOICES — direct second person, testimony before instruction, punchline
last, admits the thing before teaching the fix. Shape is varied deliberately:
a run of thirty identical synthesis lines is what the last pass had to undo.

Three sites take a bare cut, because the surviving positive is long enough to
carry its own weight and appending anything would pad it.

    python3 marginalia/compile.py --strip
    python3 instruments/w7_batch2.py
    python3 marginalia/compile.py --apply
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
9: [
("""The Elder is not about being the authority. The Elder is about making sure the work outlives you.""",
 """The Elder is about making sure the work outlives you. Authority is what that looks like to everyone else."""),
("""That's not a list of things you learned. That's a set of capacities you built.""",
 """Everything on that list started as something you learned and became something you can do."""),
("""The walk is not upward. The walk is forward.""",
 """The walk goes forward, at ground level, the whole way."""),
("""The iteration is not a deviation from the walk. The iteration is the walk.""",
 """The iteration is the walk. Every time it feels like a detour, that is what walking looks like."""),
("""The walk is not a straight line from plan to execution. The walk is iteration.""",
 """You will plan, then execute, then find the plan was a draft. That is the shape of it."""),
("""The rehearsal is not the thing. The mind rehearsing failure is not the same as doing the thing.""",
 """Rehearsing failure and doing the thing feel identical from inside your head. Only one of them produces information."""),
("""It is not work. The actual thing is simpler and scarier: put it in front of someone and see what happens.""",
 """The actual thing is simpler and scarier. Put it in front of someone and see what happens."""),
("""It's not a meditation exercise you do in the morning. It's how you walk through the world.""",
 """It's how you walk through the world. The morning version is practice for the rest of the day."""),
("""That's not a failure — that's the stage you're in.""",
 """That's the stage you're in, and it feels like failure from inside it."""),
("""The Founder is not about starting an organization. The Founder is about the moment you stop consuming and start creating.""",
 """The Founder is the moment you stop consuming and start creating. An organization is one thing that can come out of that, and usually doesn't."""),
("""That's not a failure of character. That's the Outlaw's cost.""",
 """That's the Outlaw's cost, and it arrives dressed as a failure of character."""),
("""That's not failure. That's the walk.""",
 """That's the walk. Nobody told you it would look like this."""),
("""You are not alone out there. The village is already there.""",
 """The village is already out there, and you are walking into it rather than founding it."""),
("""The second one is not less serious. The second one is the only one holding any information.""",
 """The second one sounds smaller and is the only one holding any information."""),
("""The practice is not the list. The practice is the loop.""",
 """The practice is the loop, and the list is only what the loop leaves behind."""),
("""The Player's gift is not an answer. The Player's gift is a path.""",
 """The Player's gift is a path. You wanted an answer; this is better and slower."""),
],
3: [
# bare cut — the surviving definition runs long and needs no coda
("""Spiral is not a single moment. It's a progression through five stages""",
 """Spiral is a progression through five stages"""),
("""Opening is not a demand to feel more and cope worse. It is the training to hold sensation on purpose""",
 """You will expect Opening to mean feeling more and coping worse. It is the training to hold sensation on purpose"""),
("""That completed state is not a nicer feeling. It is a restored capability — something you can do that you could not do while the feeling was stuck.""",
 """That completed state is a restored capability — something you can do that you could not do while the feeling was stuck. It may not feel nicer at all."""),
("""The danger is not cost. The danger is pretending costly moves are renewable.""",
 """The danger is pretending costly moves are renewable. Cost itself is fine, so long as you count it."""),
("""The Shaman's mastery is not in feeling feelings well. It's in knowing""",
 """The Shaman's mastery is in knowing"""),
("""This is not something you learn once. It's something you practice until it becomes your nervous system's operating system.""",
 """This is something you practice until it becomes your nervous system's operating system. Learning it once buys you nothing."""),
("""Some stuckness is not a person and not a feeling. It is a structure.""",
 """Some stuckness is a structure wearing the shape of a person or a feeling."""),
("""The work is not to eliminate one pole forever. The work is to hold both without letting either eat the other.""",
 """The work is to hold both poles without letting either eat the other. You will want to pick one. Picking one is how the pair breaks."""),
("""That is not a referee anymore. That is a judge, and it holds court in you.""",
 """That is a judge now, and it holds court in you."""),
("""It is not a foul. It is the game.*""",
 """It is in bounds.*"""),
("""The Shaman's move is not to win the case. It is to notice that a case is being held at all""",
 """The Shaman's move is to notice that a case is being held at all"""),
("""The trap is not ignorance. It is a large private collection of accurate reads""",
 """The trap is a large private collection of accurate reads"""),
("""Challenger's line is not grounded. It's performance.""",
 """Challenger's line is performance."""),
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
