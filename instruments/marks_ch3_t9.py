# -*- coding: utf-8 -*-
"""marks_ch3_t9 -- proof marks, ch3 pp.66-75 (Open Up through the Polarity Map), every entry
changed (2026-09-09). Same rule and contract as marks_ch2_t1.py.
    python3 instruments/marks_ch3_t9.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# p.66
("Carolyn Elliott named this the existential kink, and I will not pretend I stand outside it: I have felt",
 "Carolyn Elliott named this the existential kink. I have felt"),
("where the work can reach it, and the skill that moves it is coming.",
 "where the work can reach it."),
("would feel this, which is a smaller claim than deciding the feeling is correct.",
 "would feel this, without ruling on whether the feeling is correct."),
("the meaning comes later, and this chapter builds a whole practice for finding it.",
 "the meaning comes later."),
# p.67
("**What it means:** Correct distortion. Clarify what",
 "**What it means:** Clarify what"),
("letting it show you, and it usually takes a few seconds to a few minutes.",
 "letting it show you, over a few seconds or a few minutes."),
("This is the first difference between the Shaman's practice and its distortion: the villagers try to speed past this stage.",
 "The villagers try to speed past this stage."),
# p.68
("The Grow stage is the integration, the moment when the feeling stops being something that happened *to* you",
 "In the Grow stage the feeling stops being something that happened *to* you"),
("Here the shift happens: from dissatisfaction",
 "The shift runs from dissatisfaction"),
("Your old patterns offer one available starting point. What you think you should do offers another.",
 "Your old patterns offer one starting point; the shoulds offer another."),
# p.69
("in the ten seconds you have to decide something, and I moved correspondences around to make that job work.",
 "in the ten seconds you have to decide something. I moved correspondences around to make that job work."),
("keeps other people outside them, and running a borrowed vocabulary past you unmarked is the same move with the credit taken off.",
 "keeps other people outside them. Running a borrowed vocabulary past you unmarked is the same move with the credit taken off."),
# p.70
("> *Triage is the part of this chapter you will actually use, and it is in an appendix.",
 "> *The part of this chapter you will actually use, triage, is in an appendix."),
("Each channel has a completed state, and you get there by making a move.",
 "Each channel has a completed state, reached by making a move."),
("You play a move, and the move carries the stuck charge into a restored capability:",
 "You play a move that carries the stuck charge into a restored capability:"),
("These five states are the renewable fuel Chapter 1 pointed you here to make, and you make them by moving.",
 "These five states are the renewable fuel Chapter 1 pointed you here to make. Moving makes them."),
# p.71
("The move is to name what you lost, all the way, before you reach for the lesson.",
 "The move is to name what you lost, every part of it, before you reach for the lesson."),
("when you set the limit and do not spend the next hour apologizing for it.",
 "when you set the limit without spending the next hour apologizing for it."),
("The move here is the hard one: stop, and actually be here for the good part.",
 "The move is to stop and be here for the good part."),
("These are the five renewable tokens, and you reach every one of them the same way:",
 "These are the five renewable tokens. Every one of them is reached the same way:"),
# p.72
("The Five-Move Form does not make every move easy. It was never going to.",
 "The Five-Move Form does not make every move easy."),
("A pause. A clean question. One honest sentence instead of the whole speech.",
 "A pause, a clean question, one honest sentence instead of the whole speech."),
("Staying in the conversation may cost you.",
 "Staying in the conversation is one."),
("They keep spending non-renewable fuel and calling the spending virtue.",
 "They keep spending non-renewable fuel and call it virtue."),
("empties you as you spend it, and the renewable kind hands back more than you spent.",
 "empties you as you spend it; the renewable kind gives back more than you spent."),
# p.73 -- the superpower aside
("I named grief and it was rage, and I was corrected at some volume in front of eleven\n> people.*",
 "I named grief and it was rage. Eleven people corrected me, at some volume.*"),
("the company opened regardless, because\n> what mattered was that somebody was willing to be wrong out loud about something real.",
 "the company opened regardless: somebody had been\n> willing to be wrong out loud about a real charge."),
("It will be a smaller and more specific disaster,\n> and you will survive it.*",
 "It will be a smaller and more specific disaster.*"),
("You practice this until it becomes your nervous system's operating system. Learning it once buys you nothing.",
 "You practice this until it becomes your nervous system's operating system."),
("The Five-Move Form is not just a thinking exercise. Your body should know you're doing it.",
 "The Five-Move Form runs in the body, not just the head."),
# p.74
("That charge is projection. Projection is shadow work waiting to happen.",
 "That charge is projection: shadow work waiting to happen."),
("brings the charge back to where you can spend it,",
 "brings the charge back into your own hands,"),
("Solo, written or spoken, fifteen to twenty-five minutes.",
 "Do it alone, written or spoken, in fifteen to twenty-five minutes."),
# p.75
("This is deep work on live material, and the material has weight.",
 "This is deep work on live material. Live material has weight."),
("the practice is doing its job, and getting help is your next move rather than a failure.",
 "the practice is doing its job. Getting help is the next move, not a failure."),
("You keep trying to pick the right side, and the picking exhausts you.",
 "You keep trying to pick the right side. The picking exhausts you."),
("That is not a problem. Problems have solutions. This is a **polarity**:",
 "That is a **polarity**, not a problem with a solution:"),
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
    print("ch3 tranche 9: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
