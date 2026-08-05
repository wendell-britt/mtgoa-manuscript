# -*- coding: utf-8 -*-
"""ch2_s567_agency.py — the agency pass over ch2 Sections 5, 6 and 7.

Ruled by Wendell 2026-08-02: "now do sections 5 through 7", then "apply the sections 5
through 7 batch" after one correction.

**Every instrument reports these 3,639 words clean** — voice, gate and all eight diet
counters. That is the point of this pass: an abstraction doing a human verb is a defect no
counter in this repo can see, which is why Sections 1, 2 and 3 needed a reader to find it
and why this one did too.

Nine edits.

E3 is the one Wendell corrected, and the correction is the most useful thing in this file.
The original read *"the bracing fired exactly when it should."* The first draft promoted
the nominalization to *"your body braced exactly when it should"* — and got this back:
*"you can't narrate someone's somatic experience. What is actually being described here and
describe it. Don't make up how someone is feeling."*

Sensation is unfalsifiable and unshared, which is what makes it such an easy subject and
such a bad one. What was actually being described is the reflex outrunning the decision and
whether that timing is correct: a mechanism and a judgement, both of which the book asserts
in its own voice at `ch2:266` and `ch2:314`. The replacement carries the observable outcome,
the named mechanism, and the verdict, and invents nothing about anybody's chest.

Five things were left alone, and the reasons are worth keeping:

- `:240` *"That structure trains performance."* A training structure does train. Same class
  as `ch2:73`, *"The old allyship tells you what to do."*
- `:258` *"Let the first true thing find you."* The passivity is the argument.
- `:318` *"the tightening … just hums."* A deliberate callback to `:89`; cutting one breaks
  the pair.
- `:384`, `:411` — the part that waits, the sensation that sits. The book personifies parts
  and body-sensation on purpose.
- `:419` *"where the information lives."* Echoes Wendell's own `:411`, *"Where does it live?
  Chest, throat, jaw, belly."*

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = []

# E1 — a passive with no doer that also narrates the reader's history. Handed by whom.
E.append((
    "Most of the allyship training you've been handed works like school, compliance, or "
    "court.",
    "Most allyship training works like school, compliance, or court."))

# E2 — the zombie subject, and an "in place of" doing the work a verb should do.
E.append((
    "The work is to notice the first place you recognize yourself in the map, in place of "
    "memorizing the roster, mastering the Guides, or becoming the kind of person who can "
    "explain the whole system at dinner.",

    "Notice the first place you recognize yourself in the map. You are not here to "
    "memorize the roster, master the Guides, or become the kind of person who can explain "
    "the whole system at dinner."))

# E3 — see the docstring. The nominalization and the invented sensation both go.
E.append((
    "*In play:* a car swerves toward you and you're already moving before you've thought "
    "about it; the bracing fired exactly when it should.",

    "*In play:* a car swerves toward you and you are out of its path before you have "
    "decided anything. When the danger is real, the Protector does not wait for you, and "
    "it should not."))

# E4 — passive with no doer, in the definition of the reader's own superpower, which is
# the one sentence in the section where she is unambiguously the one who does it.
E.append((
    "once that capacity is made conscious, ethical, and usable in service of others.",
    "once you have made that capacity conscious, ethical, and usable in service of "
    "others."))

# E5, E6 — the most abstract prose in the chapter. "early conflict sensing and
# de-escalation in teams before harm escalates" is four nominalizations and no person.
E.append((
    "your integrated superpower can be early conflict sensing and de-escalation in teams "
    "before harm escalates.",
    "you can be the person who feels a conflict building and cools it while it is still "
    "small."))

E.append((
    "your integrated superpower can be rigorous planning that protects vulnerable people "
    "from preventable failure without slipping into control.",
    "you can be the person who plans so carefully that a preventable failure never reaches "
    "the people least able to absorb it."))

# E7 — the last first-person plural in the chapter outside the testimony. `let's` is
# `let us`, and Section 1 was swept for exactly this.
E.append((
    "Let's make it concrete. Watch what happens to the joystick.",
    "Now the walk itself. Watch what happens to the joystick."))

# E8, E9 — moves that become available on their own, and a move that gets cleaner on its
# own, in the two sentences whose whole subject is the reader taking the joystick back.
E.append((
    "with your hands back on the joystick, different moves become available:",
    "with your hands back on the joystick, you can make moves you could not reach before:"))

E.append((
    "The Forest is where you get back to the center. From there, your next move gets "
    "cleaner.",
    "The Forest is where you get back to the center. From there you play the next move "
    "cleanly."))


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
