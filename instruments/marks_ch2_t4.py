# -*- coding: utf-8 -*-
"""marks_ch2_t4 -- proof marks, ch2 pp.46-50 (the chapter file's last marks), every entry
changed (2026-09-09). The pp.51-54 marks live in front_matter/headmasters_letter.md and the
ch3 HANDBOOK block and are handled in their own tranche.

Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
    python3 instruments/marks_ch2_t4.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch2.md")

EDITS = [
# p.46
("A decision you kept circling without landing.",
 "A decision you kept circling and never made."),
# p.47
("Naming it is already half of taking the joystick back, because a daemon you can name is one you're no longer merged with.",
 "Naming it is already half of taking the joystick back."),
("The cost is your reason to take the joystick back, and saying it plainly takes the shine off the autopilot.",
 "The cost is your reason to take the joystick back."),
("and say it to someone where it isn't already safe to, in a live moment, not a debrief afterward.",
 "in a live moment where it is not already safe, not in a debrief afterward."),
("neither a confession nor a processing session, and placed where it costs something:",
 "neither a confession nor a processing session, placed where it costs something:"),
# p.48
("That's the whole action. One read, said out loud,",
 "One read, said out loud,"),
("So it reads, and reads, and never gets to speak.",
 "So it keeps reading and never gets to speak."),
("The read becomes a move, and the part that reads comes a little further home.",
 "The read becomes a move."),
# p.49
("Six guides know that terrain, and one of their questions may already have landed.",
 "Six guides know that terrain."),
(" All four are real allyship.",
 ""),
("Those two lines are the same mechanism seen from two directions, and most of the rest of this book works on the seam between them.",
 "Those two lines are the same mechanism seen from two directions."),
("from the Headmaster of that school.",
 "from the Headmaster."),
("After it, six chapters, and each opens with a treatise by the",
 "After it, six chapters, each opening with a treatise by the"),
# p.50
("about what the teaching did to them, and a margin in a hand that never signs.",
 "about what the teaching did to them. The margin is a hand that never signs."),
("Six people each solved one part of this and cannot agree on the rest, and I would rather hand you the argument than the summary.",
 "Six people each solved one part of this and cannot agree on the rest. You are getting the argument, not the summary."),
]

def main():
    t = io.open(P, encoding="utf-8").read()
    for old, new in EDITS:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("EDIT matched %d times (need 1): %r\n" % (c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2 tranche 4: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
