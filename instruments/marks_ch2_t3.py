# -*- coding: utf-8 -*-
"""marks_ch2_t3 -- proof marks, ch2 pp.34-45, every entry changed (2026-09-09).

Same rule and contract as marks_ch2_t1.py. Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md.
    python3 instruments/marks_ch2_t3.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch2.md")

EDITS = [
# p.34
("Trained that way, you perform. You do not learn to be playful.",
 "Trained that way, you perform instead of play."),
# p.35
("The school is somewhere to stand while you practice, and that is the whole of its job.",
 "The school is somewhere to stand while you practice."),
("than a framework that answers to nobody, and the only route I found to letting you argue with a Face was to give it a mouth that argues back.",
 "than a framework that answers to nobody. The only way to let you argue with a Face was to give it a mouth that argues back."),
("Recognition is where the move begins, and beginning is all it is.",
 "Recognition is where the move begins."),
("It is the same part throughout; what changes is who's holding the joystick.",
 "The same part wears all three names; only the hand on the joystick changes."),
# p.36
("the Protector does not wait for you, and it should not.",
 "the Protector does not wait for you."),
("You answer armored, and the other person meets the armor before they reach you.",
 "You answer armored. The other person meets the armor before they reach you."),
("gets the result their own way, and you catch yourself docking points for how they did it instead of registering that they did it at all.",
 "gets the result their own way. You catch yourself docking points for how they did it instead of registering that they did it at all."),
# p.37
("and you're already three solutions deep, and they walk away having lost their own say in it.",
 "and you're already three solutions deep. They walk away having lost their own say in it."),
("the feeling runs clean and becomes information you can use.",
 "the feeling completes and becomes information you can use."),
("someone says something and it lands hard.",
 "someone says something and it hits you in the chest."),
("an unprocessed feeling spills out of you, and the person you came to support ends up taking care of you.",
 "an unprocessed feeling spills out of you. The person you came to support ends up taking care of you."),
# p.38
("It knows danger before you could prove it to anyone, because a hull that waits for proof is already taking on water.",
 "It knows danger before you could prove it to anyone."),
("That speed has kept you alive, and you want to keep it.",
 "That speed has kept you alive."),
("In the next chapter you learn to read the fear channel it runs on, which is where steering it starts.",
 "The next chapter teaches you to read the fear channel it runs on."),
("A hull that treats every century as the dangerous one never misses a threat,",
 "A hull that braces for a predator in every meeting never misses a threat,"),
("Vigilance runs at a higher price and buys aim: this tone, this move for power, this person, now.",
 "Vigilance costs more because it aims: this tone, this move for power, this person, now."),
# p.39
("braced against something that has not happened, and the person across from you meets the hull before they meet you.",
 "braced against something that has not happened. The person across from you meets the hull before they meet you."),
("It trades contact for control, and the trade feels like safety.",
 "Control replaces contact. From inside, that feels like safety."),
("The body knows one shortcut around this, worth naming because it looks like love:",
 "The body knows one shortcut, the one that looks like love:"),
("A mother does this with a child, and it is real.",
 "A mother does this with a child."),
("because it only works by making the other person part of you, and the person you are allying with is not you.",
 "because it only works by making the other person part of you. The person you are allying with is not you."),
("You do not fight the Protector, and you do not shove past it. You thank it,",
 "You do not fight the Protector or shove past it. You thank it,"),
("That exchange has a name and a form. Chapter 3 gives you both, and every chapter after it runs the same shape.",
 "Chapter 3 gives that exchange a name and a form."),
# p.40
("It only comes first; any of the seven can end up holding the joystick.",
 "The Protector only comes first; any of the seven can end up holding the joystick."),
("The care underneath is real; the missing piece is you on the joystick,",
 "The missing piece is you on the joystick,"),
("You are the player at the center of the Forest, and reaching that center and taking the joystick are the same motion.",
 "You are the player at the center of the Forest. Reaching that center and taking the joystick are one motion."),
# p.41
("A superpower is not a Face, and no chapter owns one.",
 "A superpower is not a Face. No chapter owns one."),
# p.42
(" The two come back to back on purpose.",
 ""),
# p.43
("The old hermetic rule is *as within, so without*, and here it is mechanical.",
 "The old hermetic rule, *as within, so without*, is mechanical here."),
("standing in front of every person you will ever try to help, and they do not know you.",
 "standing in front of every person you will ever try to help. They do not know you."),
("help a coworker named Imani with something real:",
 "help a coworker named Imani with a real problem:"),
("That trust is hers, and it comes out of the whole of her.",
 "The trust is hers, given by the whole of her."),
("Every skilled helper you have ever met already knows this, and most of them never say so out loud.",
 "Every skilled helper you have ever met already knows this."),
("*there is a standard here, and yours is not it.*",
 "*there is a standard here. Yours is not it.*"),
# p.44
("so you either meet hers or you help her move it, and both of those are allyship.",
 "so you either meet hers or you help her move it."),
("You see what she does, and you supply the rest, and what you supply comes out of you.",
 "You see what she does and supply the rest. What you supply comes out of you."),
("That is projection, and it is the trickiest move in shadow work:",
 "That is projection, the trickiest move in shadow work:"),
("You get past it or you do not, and how far it lets you in decides which of the other six you ever get near. That distance is your **clearance**, and it is the only currency on this side of the door.",
 "You get past it or you do not. How far it lets you in decides which of the other six you ever get near. That distance is your **clearance**."),
("Playing above your clearance is a major error, and your character has nothing to do with it. It usually has an author, and the author is your Controller:",
 "Playing above your clearance is a major error. Your character has nothing to do with it; your Controller does:"),
# p.45
("or a bar pointing somewhere she was not going, and either one is more than she can metabolize today.",
 "or a bar pointing somewhere she was not going. Either one is more than she can take on today."),
("People do it every day, and once in a while it is the only move left.",
 "People do it every day. Once in a while it is the only move left."),
("From the middle those two look the same, and most people will punish both.",
 "From the middle those two look the same."),
("Two Protectors meet constantly, and everybody calls that a conflict.",
 "Two Protectors meet constantly. Everybody calls that a conflict."),
("hers has a braced body across the table to check against, and both do their jobs perfectly while nothing gets through in either direction.",
 "hers has a braced body across the table to check against. Both do their jobs perfectly while nothing gets through in either direction."),
("Not knowing this costs you, and it costs you the same way every time.",
 "Not knowing this costs you the same way every time."),
("Imani's Protector fires, and the door closes an inch.",
 "Imani's Protector fires. The door closes an inch."),
("That is burnout, and every step of it is you playing hard.",
 "That is what burns people out, one hard-played round at a time."),
("Real help sits open at whatever clearance you already hold, and a small move at a narrow door still lands.",
 "Real help sits open at whatever clearance you already hold. A small move at a narrow door still counts."),
("A daemon stands at Imani's door, a person stands behind it, and you have one move you can make today.",
 "A daemon stands at Imani's door with a person behind it. You have one move today."),
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
    print("ch2 tranche 3: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
