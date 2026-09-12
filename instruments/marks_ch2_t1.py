# -*- coding: utf-8 -*-
"""marks_ch2_t1 -- proof marks, ch2 pp.25-29, every entry changed (2026-09-09).

Wendell: "I highlighted everything that felt wrong ... anything marked up isn't deliberate
craft. It must be changed." Worklist: specs/PROOF_MARKS_CH2_CH3_2026-09-09.md. Rule applied:
hand the reader the material, remove the handling -- the appended interpretation, the verdict
stamp, the signpost, the hedge; a concrete verb where a nothing-word stood.

Every edit is (old, new) on the marked text, asserted to match exactly once.
    python3 instruments/marks_ch2_t1.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch2.md")

EDITS = [
# p.25
("says what has been sitting there for months and everybody at the table starts picking their words.",
 "says what has been sitting there for months. Everybody at the table starts picking their words."),
("end up arguing about a word,",
 "end up arguing over vocabulary,"),
("You say the sentence you rehearsed and your friend agrees with you and never brings it up again.",
 "You say the sentence you rehearsed. Your friend agrees with you and never brings it up again."),
# p.26
("It arrives before the words do, and no action item takes it out.",
 "It arrives before the words do."),
("anywhere other people can see what you did and adjust their read on you.",
 "anywhere other people can see what you did and revise what they think of you."),
("so the village is a reasonable place to have put all the tools. Allyship put all of them there.",
 "so allyship put all of its tools there."),
("or has become something the response cannot reach, and the person who responded has nothing left.",
 "or has become something the response cannot reach. The person who responded has nothing left."),
("or the read you set aside,",
 "or the signal you set aside,"),
("I was trained in shamanism, and I did not want to learn it.",
 "I was trained in shamanism. I did not want to learn it."),
("I stayed because her chops were impeccable. That was the whole reason, and it held.",
 "I stayed because her chops were impeccable."),
("in dance and in writing and in this.",
 "in dance, in writing, and on this page."),
# p.27
("or said the sentence they cannot take back,",
 "or said what they cannot take back,"),
("You know which time was yours. You know the feeling that came with it.",
 "You know the feeling that came with yours."),
(" It protected you when you needed protecting. It made sense once.",
 ""),
("Hold these three words, because the whole book turns on them. The **Shadow**",
 "The **Shadow**"),
("One word each: Shadow, distortion, cost. They are not the same, and the work is to tell them apart.",
 "Shadow, distortion, cost. The work is telling them apart."),
(" That is a different project entirely, and it produces different results.",
 ""),
("capacities that most training never reaches, and most training does not say so. The curriculum opens where the work becomes visible, which is a long way past where it starts.",
 "capacities that most training never reaches. The curriculum opens where the work becomes visible, a long way past where it starts."),
("The onboarding has a section on psychological safety. It is a form. You sign it.",
 "The onboarding has a section on psychological safety, a form you sign."),
("that allyship is mainly about what you do in public. The deeper truth is this:",
 "that allyship is mainly about what you do in public."),
# p.28
("This theory is incomplete rather than wrong. The old allyship produced real wins: doors that opened, conversations that happened, power that shifted in small amounts, temporarily, in specific places.",
 "The old allyship produced real wins: a door that opened, a conversation that happened, power that shifted a little, for a while, in one place."),
(" Both are true.",
 ""),
# "for a while," is on the voice linter's VAGUE list (say the noun); the first rewrite used
# it. Replaced with a span the reader can picture.
("power that shifted a little, for a while, in one place.",
 "power that shifted a little, in one place, for one season."),
# cutting "This theory is incomplete rather than wrong." left "It also produced" pointing at
# the list; the voice linter flagged it (say the noun). Name the subject.
("It also produced a generation of exhausted practitioners",
 "The old allyship also produced a generation of exhausted practitioners"),
("The trainers behind the old allyship never asked about that.",
 "The trainers behind the old allyship never asked what shape your body was in."),
("The walking went in the wrong direction, and no one had mentioned a different starting point.",
 "The walking went in the wrong direction. No one had mentioned a different starting point."),
("Some of what gets called burnout is that cost still being carried. It sits closer to sadness than to fatigue: the sadness",
 "Some of what gets called burnout is that cost still being carried: the sadness"),
# p.29
("The terms were set wrong from the beginning, and no one failed.",
 "The terms were set wrong from the beginning. No one failed."),
("That sadness is information. It tells you what mattered.",
 "That sadness tells you what mattered."),
("Something has shifted. Everyone is on edge, so a hard conversation could be around any corner, and vigilance that once made sense now runs as background noise.",
 "Everyone is on edge, so a hard conversation could be around any corner. Vigilance that once made sense now runs as background noise."),
("You cannot draw a boundary you have not felt.",
 "You cannot draw a boundary you have never felt in your own body."),
("unless you know what you're made of.",
 "unless you know what runs you under pressure."),
("I do not know whether a mind really holds eight separate voices, and neither does anybody selling you a model of one.",
 "I do not know whether a mind really holds eight separate voices."),
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
    print("ch2 tranche 1: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
