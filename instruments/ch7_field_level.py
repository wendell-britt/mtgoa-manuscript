# -*- coding: utf-8 -*-
"""
ch7_field_level.py — the eight field sites where a low-order thing does a
high-order act.

Wendell's rule, 2026-08-03:

    "People in the field can learn how the field responds, but learns is a
     higher order word and the field is a lower order entity. It's a UR low
     level phenomenon, and a LR quantum experience."

The field sits in AQAL's right-hand quadrants -- exterior, observable, the
interobjective space between bodies -- and low within them. Learning, allowing,
asking and answering are left-hand capacities: they need interiority. Putting
one on the field is a LEVEL confusion, not a missing mechanism, which is why
"it has no brain" was never quite the right objection.

THE REPAIR IS NEVER DELETION. The verb gets returned to whoever holds it. In
every one of these eight the owner was already in the sentence or one clause
away, which is the tell that the defect is grammatical rather than conceptual --
the chapter knows who is acting and the syntax lost them.

Six force verbs stay licensed on the field and are untouched here: carry, move,
push, fill, run, turn. A field carries and pushes the way a magnet pulls.

    python3 instruments/ch7_field_level.py --dry
    python3 instruments/ch7_field_level.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
CH7 = "manuscript/ch7.md"

EDITS = [
    # ---- perception ---------------------------------------------------------
    # The people stop noticing, not the field. And they are the ones being
    # taken advantage of, so the sentence lands harder with them in it.
    ("that the field learns to take for granted.",
     "that everyone in the field learns to take for granted."),

    # ---- intention ----------------------------------------------------------
    # Two faults in one clause. `allows` is permission, which needs a will; and
    # `enter` contradicts SPEC_FIELD_OF_BODIES outright -- a field has no
    # inside, it is what sits between the bodies making it. This clause survived
    # the R-B pass that was written to remove exactly the second fault.
    ("and the field allows a new presence to enter.",
     "and the people there let someone new in."),

    # The next clause already supplies the owner: "a person who does not send an
    # invoice is a person nobody has to pay." `nobody` was the sentence's own
    # logic arriving one clause late.
    ("and the field will let you, because a person who does not send an invoice",
     "and nobody there will stop you, because a person who does not send an invoice"),

    # ---- speech -------------------------------------------------------------
    # NOT INCLUDED, and it should be. Four clauses before the `asks` site below:
    #
    #   "said once, to the field rather than about it, and then the field takes
    #    its turn."
    #
    # Taking a turn is participating in an exchange, which is the same
    # high-order act as asking. It is invisible to the net (`take` is in no
    # lemma list) and it was flagged in conversation but was not among the eight
    # Wendell approved, so it is not applied here. The fix is ready:
    #   -> "and then they take theirs."
    # Leaving it means one paragraph carries both the repaired and unrepaired
    # form of the same defect, which is the local inconsistency the village
    # passes were careful about. One word closes it.

    ("One sentence covers what the field actually asks.",
     "One sentence covers what they actually need to hear."),

    ("and you let the field answer.",
     "and you let them answer."),

    # `take for granted` is a stance, and a stance needs somebody holding it.
    # Invisible to the recall net -- `take` is in no lemma list at any grade --
    # and caught by reading the passage the speech sites sit in.
    ("attendance is what a field takes for granted.",
     "attendance is what everyone in a field takes for granted."),

    # ---- accommodation ------------------------------------------------------
    # The mildest two: `makes space` is idiom. But under the rule it is still a
    # low-order thing performing an accommodating act, and both rewrite shorter.
    ("everyone gets to feel heard, the field makes space for the full range of "
     "perspectives present.",
     "everyone gets to feel heard, every perspective present gets space."),

    ("because closing feels like conflict and the field can always make space for "
     "one more round.",
     "because closing feels like conflict and there is always space for one more round."),
]


def main():
    dry = "--dry" in sys.argv
    full = os.path.join(ROOT, CH7)
    text = io.open(full, encoding="utf-8").read()

    for before, _a in EDITS:
        n = text.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (n, before[:96]))

    for before, after in EDITS:
        text = text.replace(before, after, 1)
        print("  --  %s" % before[:104])
        print("  ++  %s" % after[:104])

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %s, %d edits." % (CH7, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
