# -*- coding: utf-8 -*-
"""
agency_ch3.py — R8 pass on Chapter 3, the pilot batch.

Wendell authorised the full village repair into print scope, 2026-08-02.
ch3 goes first: highest hold rate in the book (20 of 23), the audit's clean
control, and three sites where R8 preserves a closing beat the ledger's existing
R1 proposal drops.

R8 pre-flight (instruments/agency_registry.yaml) applied per site. Three sites
route AWAY from R8:

  L119  reflexive — "never saw itself" encodes systemic blindness with no
        vantage point. The plural is grammatical and asserts a weaker claim.
  L267  coextensive — villagers cannot train everyone, because they are
        everyone. Compression + named trainers.
  L501  duration — a village persists a thousand years; villagers do not.
        Found while drafting; not in the stress test's break list.

L90 is HELD as keep-candidate, not fixed. Pluralizing "never meant for that to
happen" risks converting a diffuse-drift claim into an individually-exculpatory
one, and C3 reserves that ruling.

Place-uses are left alone throughout: "lived in the village" (54), "the feeling
in the village" (56), "back into the village" (914) are the settlement, not the
population — R8 pre-flight check 3.

Density: within-paragraph continuations use pronouns, per the mandatory
variation rule. The four-paragraph "still experienced fear/anger/sadness/joy"
anaphora is preserved as structure, not flattened.

    python3 instruments/agency_ch3.py --dry
    python3 instruments/agency_ch3.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
TARGET = os.path.join(ROOT, "manuscript", "ch3.md")

# (line-ish, op, before, after)
EDITS = [
    (58, "R8", "The village trusted this once. It built rituals around it.",
              "The villagers trusted this once. They built rituals around it."),

    (66, "R8", "There was a problem. The village had to act.",
              "There was a problem. The villagers had to act."),

    (68, "R8", "The village needed someone who could draw a line in the sand.",
              "The villagers needed someone who could draw a line in the sand."),

    (70, "R8", "The cost landed somewhere the village never thought to look.",
              "The cost landed somewhere the villagers never thought to look."),

    (82, "R8", "When the village started following the Challenger's lead,",
              "When the villagers started following the Challenger's lead,"),

    (97, "R8", "the village didn't stop feeling.",
              "the villagers didn't stop feeling."),

    # fear — four subjects in one paragraph; pronoun continuation after the first
    (101, "R8", "The village still experienced fear.",
               "The villagers still experienced fear."),
    (101, "R8", "The village learned to not-feel the fear, which meant the village also missed "
                "the intelligence fear kept trying to deliver. The village became brittle.",
                "They learned to not-feel the fear, which meant they also missed "
                "the intelligence fear kept trying to deliver. They became brittle."),

    # anger
    (103, "R8", "The village still experienced anger.",
               "The villagers still experienced anger."),
    (103, "R8", "The village learned to redirect anger *outward*",
               "They learned to redirect anger *outward*"),
    (103, "R8", "It forgot that anger could also point inward,",
               "They forgot that anger could also point inward,"),

    # sadness
    (105, "R8", "The village still experienced sadness.",
               "The villagers still experienced sadness."),
    (105, "R8", "The village learned to skip over sadness,",
               "They learned to skip over sadness,"),
    (105, "R8", "It forgot how to let sadness teach. So it kept hitting the same losses over "
                "and over, unable to actually grieve what it had lost.",
                "They forgot how to let sadness teach. So they kept hitting the same losses over "
                "and over, unable to actually grieve what they had lost."),

    # joy
    (107, "R8", "The village still experienced joy.",
               "The villagers still experienced joy."),
    (107, "R8", "the village learned to celebrate *doing the work*",
               "the villagers learned to celebrate *doing the work*"),
    (107, "R8", "The village forgot that joy was also information,",
               "They forgot that joy was also information,"),

    (109, "R8", "Without the Shaman, the village became very busy managing emotions",
               "Without the Shaman, the villagers became very busy managing emotions"),

    (111, "R8", "The village did all of this on purpose.",
               "The villagers did all of this on purpose."),

    (113, "R8", "So the village made a choice: efficiency over wisdom.",
               "So the villagers made a choice: efficiency over wisdom."),

    (115, "R8", "The village solved some problems. It moved some mountains. It changed some systems,",
               "The villagers solved some problems. They moved some mountains. They changed some systems,"),

    (117, "R8", "This is what the village does with emotional alchemy when the Shaman is gone: "
                "it transforms it into *performance management.*",
                "This is what the villagers do with emotional alchemy when the Shaman is gone: "
                "they transform it into *performance management.*"),

    # ---- BREAK 1: reflexive. R8 would assert a weaker claim.
    (119, "R6", "The village never saw itself doing this. It called the pattern efficiency, "
                "and the pattern starved it.",
                "No one in the village saw it happening. They called the pattern efficiency, "
                "and the pattern starved them."),

    (128, "R8", "The village shrinks alchemy into processing:",
               "The villagers shrink alchemy into processing:"),

    (180, "R8", "That is what the village lost when the Shaman left.",
               "That is what the villagers lost when the Shaman left."),

    # ---- BREAK 2: coextensive. Villagers cannot train everyone; they are everyone.
    (267, "R1", "The village trains everyone to turn feeling down. It hands you a dial in "
                "childhood and teaches one direction: lower it.",
                "The people who raised you hand you a dial in childhood and teach one "
                "direction: lower it."),

    (310, "R8", "the Shaman's practice and the village's distortion: the village tries to "
                "speed past this stage.",
                "the Shaman's practice and its distortion: the villagers try to "
                "speed past this stage."),

    (493, "R8", "Without the Shaman, the village manages emotions instead of learning from them.",
               "Without the Shaman, the villagers manage emotions instead of learning from them."),

    # ---- BREAK 3: duration. A village lasts a thousand years; villagers do not.
    (501, "R6", "The village took a thousand years to forget this.",
                "Forgetting this took a thousand years."),
]


def main():
    dry = "--dry" in sys.argv
    t = io.open(TARGET, encoding="utf-8").read()

    for ln, op, before, after in EDITS:
        n = t.count(before)
        if n != 1:
            sys.exit("ABORT: L%s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (ln, n, before[:90]))

    for ln, op, before, after in EDITS:
        t = t.replace(before, after, 1)
        print("\nL%-4s %s" % (ln, op))
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0

    io.open(TARGET, "w", encoding="utf-8").write(t)
    print("\nwrote manuscript/ch3.md — %d edits." % len(EDITS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
