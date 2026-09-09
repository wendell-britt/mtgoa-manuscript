# -*- coding: utf-8 -*-
"""marks_ch3_t7 -- proof marks, ch3 body pp.60-65, every entry changed (2026-09-09).
The marginalia marks on these pages (p.61 Polarity aside, p.65 Maera aside) are in
marks_ch3_t8.py because they wrap. The p.62 treatise SIGNATURE mark is left for a ruling:
it is structural attribution, and the fix is framing the treatise's entry, not its text.

Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
    python3 instruments/marks_ch3_t7.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# p.60
("the default answer whenever the read turns inconvenient.",
 "the default answer whenever the reading is inconvenient."),
("You have been calling these problems. They are *signals.*",
 "They are *signals*, whatever you have been calling them."),
# p.61
("When you do this with joy, which feels like the easy one and is not (",
 "When you do this with joy, the one that only looks easy ("),
("when you *land* in joy instead of using it for fuel",
 "when you *stay* in joy instead of using it for fuel"),
("This is emotional alchemy. Other practices manage emotions. Other practices optimize them. This one is the education by emotions.",
 "Other practices manage emotions or optimize them. Emotional alchemy is being educated by them."),
("Everything above is one pole.",
 "That was one pole."),
("that turn costly the moment they come apart.",
 "that start costing you the moment they come apart."),
("because the School of the Body stands on it, and you get the other end once you can hold the first.",
 "because the School of the Body stands on it. The other end comes once you can hold the first."),
("the feeling that gives you the read versus the function that makes the read matter to somebody else.",
 "the feeling that gives you the reading versus the function that makes it matter to somebody else."),
# p.62
("The sentence said to the face it concerns. The decision that went differently because somebody said it. The water that moved.",
 "A sentence said to the face it concerns; a decision that changed because somebody said it; water that moved."),
("between a read that stays in you and a read that lands *in the world*,",
 "between a reading that stays in you and one that reaches *the world*,"),
("You felt it in your chest. Function is whether anybody else ever did.",
 "You felt it in your chest; Function asks whether anybody else ever did."),
("Feeling without Function is the more expensive failure, because it looks like depth.",
 "Feeling without Function costs more, because it looks like depth."),
("Here is what is specific to this reader, and its shape is a squeeze rather than a lean.",
 "What is specific to this reader is shaped like a squeeze rather than a lean."),
("trusted privately and acted on alone, comes with warnings:",
 "trusted privately and acted on alone, carries warnings:"),
("Function has warnings of its own, and this altitude issues them loudest:",
 "Function's own warnings are the ones this altitude shouts loudest:"),
# p.63 -- the sourcing paragraph
("Other people built some of what this chapter hands you, and their names belong with the tools.",
 "Other people built some of what this chapter hands you. Their names belong with the tools."),
("comes from Eugene Gendlin's *Focusing*, and the phrase names the body's knowing that arrives before language does, which is what this chapter teaches you to read.",
 "comes from Eugene Gendlin's *Focusing*: the body's knowing that arrives before language, which this chapter teaches you to read."),
("A feeling carries energy that has to finish moving, and it jams when you cut it off.",
 "A feeling carries energy that has to finish moving; cut it off and it jams."),
("He studies that jam where it is severe, in trauma, which calls for a trained person in the chair with you.",
 "He studies that jam where it is severe, in trauma, with a trained person in the chair."),
("a bad afternoon rather than a wound, and the stretch from one to the other is mine to answer for.",
 "a bad afternoon rather than a wound. The stretch from one to the other is mine to answer for."),
("The Polarity Map is Barry Johnson's, and so is the distinction it rests on.",
 "The Polarity Map and the distinction it rests on are Barry Johnson's."),
("The five channels are borrowed too, and I say from where when they arrive a few pages on.",
 "The five channels are borrowed too; I name their source when they arrive a few pages on."),
("The Shaman's native material is *emotion*, and what you can use runs narrower than mood and faster than temperament: the charge that arrives in one particular second, about one particular person, and goes somewhere when you spend it.",
 "The Shaman's native material is *emotion*, narrower than mood and faster than temperament: the charge that arrives in one particular second, about one particular person, and moves when you spend it."),
("all problems are relational problems. Take it further. All problems are emotional problems.",
 "all problems are relational problems. Every one of them is also an emotional problem."),
("Solve for the emotion and you can move to service, which you thought you were doing all along.",
 "Solve for the emotion and service becomes possible."),
("The tightening in your chest when someone gets upset is your discomfort, not theirs.",
 "The tightening in your chest when someone gets upset belongs to you, not to them."),
# p.64
("They get efficiency. They needed presence.",
 "They get efficiency where they needed presence."),
("The game removes the option of solving.",
 "The game takes solving off the table."),
("What they say next is the real one, not the complaint, not the position, the feeling underneath it. Fear dressed as criticism. Sadness wearing the costume of an argument.",
 "What they say next is the feeling underneath the complaint or the position: fear dressed as criticism, sadness wearing the costume of an argument."),
("Most allyship has the same problem those calls had.",
 "Most allyship has the same problem that phone call had."),
("A real partnership has two people more real at the end than at the start.",
 "A real partnership leaves both people more themselves than when they started."),
("*Form* is the martial artist's word, and it is the exact one.",
 "*Form* is the martial artist's exact word."),
("You learn it in pieces and you never finish it.",
 "You learn it in pieces and never finish."),
("The beginner runs the form and the master runs the form, and what separates them lives inside the same five moves.",
 "The beginner and the master run the same form; what separates them lives inside the same five moves."),
# p.65
("(The converting happens very fast. You have converted your whole life. The pause is the practice.)",
 "(The converting happens very fast; you have been doing it your whole life. The pause is the practice.)"),
("run the length of the encounter, and you keep noticing the feeling the whole way through.",
 "run the length of the encounter, with you noticing the feeling the whole way through."),
("hand you a dial in childhood and teach one direction: lower it.",
 "hand you a dial in childhood and teach you one direction, down."),
("slips past before it registers, and we call that setting *calm*.",
 "slips past before it registers. That setting gets called *calm*."),
("The Shaman works by sensitivity, and an instrument kept behind glass reads nothing.",
 "The Shaman works by sensitivity; an instrument kept behind glass reads nothing."),
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
    print("ch3 tranche 7: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
