# -*- coding: utf-8 -*-
"""
W9 — ch3 em-dash pass, batch B (Sections 3-5, the channels through the council).

Five parallel families run through this stretch, one per emotion. Each family
gets ONE mark applied to all five arms, because that is what makes it a figure
instead of a habit:

  If it's fear — what threat...            -> colon      (question follows a label)
  If fear showed you what matters — ...    -> comma      (clause continues)
  You understood what matters — now ...    -> full stop  (two instructions)
  What it restores is exploration — ...    -> colon      (the gloss defines it)
  1. **Name the charge** — the specific... -> colon       (inline label)

Parentheses take the load where a comma pair would leave four commas fighting in
one sentence: the Controller's whistle, the referee's rulebook, the council
woman's fear. Six of those, and no more, because parentheses are their own tic
past that.

    python3 instruments/w9_ch3_b.py --dry
    python3 instruments/w9_ch3_b.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# the five diagnostic questions
("If it's fear — what threat", "If it's fear: what threat"),
("If it's anger — what obstacle", "If it's anger: what obstacle"),
("If it's sadness — what do I care about", "If it's sadness: what do I care about"),
("If it's joy — what's aligned", "If it's joy: what's aligned"),
("If it's neutrality — what perspective", "If it's neutrality: what perspective"),
# the five integrations
("If fear showed you what matters — your system integrates", "If fear showed you what matters, your system integrates"),
("If anger showed you a boundary — your system integrates", "If anger showed you a boundary, your system integrates"),
("If sadness showed you what mattered — your system integrates", "If sadness showed you what mattered, your system integrates"),
("If joy showed you what's aligned — your system integrates", "If joy showed you what's aligned, your system integrates"),
("If neutrality showed you perspective — your system integrates", "If neutrality showed you perspective, your system integrates"),
# the five hand-offs
("You understood what matters — now show up", "You understood what matters. Now show up"),
("You understood your boundary — now hold it.", "You understood your boundary. Now hold it."),
("You understood what was real — now honor it.", "You understood what was real. Now honor it."),
("You understood what's aligned — now move toward it.", "You understood what's aligned. Now move toward it."),
("You understood the larger perspective — now lead from that clarity.",
 "You understood the larger perspective. Now lead from that clarity."),
# the five restorations
("What it restores is exploration — you can move toward", "What it restores is exploration: you can move toward"),
("What it restores is connection — sadness felt all the way through", "What it restores is connection: sadness felt all the way through"),
("What it restores is agency — *I can act.*", "What it restores is agency: *I can act.*"),
("What it restores is participation — you can be in this", "What it restores is participation: you can be in this"),
("What it restores is rest — *I can rest.*", "What it restores is rest: *I can rest.*"),
# the four polarity steps
("1. **Name the charge** — the specific scene", "1. **Name the charge:** the specific scene"),
("2. **Name the two poles** — behaviors you could do", "2. **Name the two poles:** behaviors you could do"),
("3. **Mark your position** — which pole", "3. **Mark your position:** which pole"),
("4. **Design one integrated action** — one move that contains", "4. **Design one integrated action:** one move that contains"),
# appendix titles
("Appendix — The Five Channels in Practice.*", "Appendix: The Five Channels in Practice.*"),
("Appendix — 3-2-1 Shadow Process.", "Appendix: 3-2-1 Shadow Process."),
("Appendix — Polarity Map.", "Appendix: Polarity Map."),
# the rest, in order
("its own sometimes, given enough time — but the game does not wait",
 "its own sometimes, given enough time, but the game does not wait"),
("is a restored capability — something you can do", "is a restored capability: something you can do"),
("it opens into poignance — the ache that reaches for someone.",
 "it opens into poignance, the ache that reaches for someone."),
("I do not mean triumph over anyone — I mean the plain solidity",
 "I do not mean triumph over anyone. I mean the plain solidity"),
("it completes into bliss — being in the thing instead of watching",
 "it completes into bliss, being in the thing instead of watching"),
("it completes into peace — the stillness that can hold two true things",
 "it completes into peace, the stillness that can hold two true things"),
("spending non-renewable fuel — guilt, obligation, optics, inherited debt — and calling the spending virtue.",
 "spending non-renewable fuel (guilt, obligation, optics, inherited debt) and calling the spending virtue."),
("was one of two kinds of token — the fixed supply that empties you",
 "was one of two kinds of token, the fixed supply that empties you"),
("mastery lies in knowing — in real-time — which WAVE-Spiral stage",
 "mastery lies in knowing, in real time, which WAVE-Spiral stage"),
("shifts in your nervous system — not relief yet, but *recognition*.",
 "shifts in your nervous system, not relief yet, but *recognition*."),
("practice is how you remember — in five stages, as many times",
 "practice is how you remember, in five stages, as many times"),
("already feeling in your body — fear in the meeting, sadness after a rupture,",
 "already feeling in your body: fear in the meeting, sadness after a rupture,"),
("them returns to your system — available for the WAVE-Spiral.",
 "them returns to your system, available for the WAVE-Spiral."),
("is in a **person** — a figure who makes your jaw tighten — start with 3-2-1.",
 "is in a **person**, a figure who makes your jaw tighten, start with 3-2-1."),
("to pick the right side — and the picking exhausts you.",
 "to pick the right side, and the picking exhausts you."),
("The dot is a diagnostic — not a verdict.", "The dot is a diagnostic, not a verdict."),
("It sets the standard — what's good, what's bad, what you're allowed to do about it — and then it holds the line",
 "It sets the standard (what's good, what's bad, what you're allowed to do about it) and then holds the line"),
("it is not automatic — it is a part of you doing a job.",
 "it is not automatic. It is a part of you doing a job."),
("my own anger out of order — a good facilitator does not get angry — so the anger went",
 "my own anger out of order (a good facilitator does not get angry), so the anger went"),
("before the feeling has finished arriving — *that's not fair, you don't get to be angry, other people have it worse* — and calls the play",
 "before the feeling has finished arriving (*that's not fair, you don't get to be angry, other people have it worse*) and calls the play"),
("until the conditions are perfect — the exact right words,",
 "until the conditions are perfect: the exact right words,"),
("Wake, Open, Clean, Grow, Show — every stage assumes", "Wake, Open, Clean, Grow, Show: every stage assumes"),
("handing it the right rulebook — your rules, the ones you would choose",
 "handing it the right rulebook, your rules, the ones you would choose"),
("goes back to its real work — keeping your integrity when it costs you,",
 "goes back to its real work: keeping your integrity when it costs you,"),
("inadmissible before you can speak — *probably just my stuff* — and you go along",
 "inadmissible before you can speak (*probably just my stuff*), and you go along"),
("you say the one true sentence — *\"Something here doesn't sit right with me. Can we slow down?\"* — even while your nerve",
 "you say the one true sentence, *\"Something here doesn't sit right with me. Can we slow down?\"*, even while your nerve"),
("Who are you to say this — you're not ready, you don't belong,",
 "Who are you to say this: you're not ready, you don't belong,"),
("you have already accepted the court — now you are litigating",
 "you have already accepted the court. Now you are litigating"),
("*there it is, \"not ready\" — noted.", "*there it is, \"not ready.\" Noted."),
("The first half was Feeling — the charge sensed cleanly. This half is Function — the read becoming a move",
 "The first half was Feeling: the charge sensed cleanly. This half is Function: the read becoming a move"),
("take the move where it counts — out of the forest,", "take the move where it counts, out of the forest,"),
("the lower fields — three families' fields — began to fail.",
 "the lower fields, three families' fields, began to fail."),
("who caught it every time — the way the circle warmed", "who caught it every time, the way the circle warmed"),
("the fear be all the way there — she was going to be disliked, and she was going to say it anyway — and she turned to the one",
 "the fear be all the way there (she was going to be disliked, and she was going to say it anyway) and turned to the one"),
("the council had to answer it — not her feeling, the fact",
 "the council had to answer it, not her feeling, the fact"),
("said to the face that could change it — which the correct words, for all their beauty, never were.",
 "said to the face that could change it. The correct words, for all their beauty, never were."),
("saying the true one — the thing a part of you has already felt, that everyone already half-knows — to the face it concerns,",
 "saying the true one, the thing a part of you has already felt, that everyone already half-knows, to the face it concerns,"),
("the Controller called a foul — the fear, the \"not ready,\" the \"not good enough\" — and burns it for fuel",
 "the Controller called a foul (the fear, the \"not ready,\" the \"not good enough\") and burns it for fuel"),
("That is the Shaman's whole practice — the sensing, the WAVE, the Controller pried off the joystick — aimed at one outcome:",
 "That is the Shaman's whole practice. The sensing, the WAVE, the Controller pried off the joystick, all aimed at one outcome:"),
("move needs both at once — the read let all the way in,", "move needs both at once: the read let all the way in,"),
("The verdict fired — *you don't have the standing* — and it fired against a rule",
 "The verdict fired (*you don't have the standing*), and it fired against a rule"),
]


def main():
    dry = "--dry" in sys.argv
    t = io.open(P, encoding="utf-8").read()
    bad = []
    for a, b in EDITS:
        n = t.count(a)
        if n != 1:
            bad.append((n, a[:70]))
        else:
            t = t.replace(a, b, 1)
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for n, a in bad:
            print("  %d matches: %r" % (n, a))
        return 1
    if not dry:
        io.open(P, "w", encoding="utf-8").write(t)
    print("%s %d edits" % ("would apply" if dry else "applied", len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
