# -*- coding: utf-8 -*-
"""marks_ch3_t10 -- proof marks, ch3 pp.76-85 (Draw the Axis, the Controller up close, the
parable, the Alchemist, the opening of the Game), every entry changed (2026-09-09).
Same rule and contract as marks_ch2_t1.py.

Held for rulings, not changed here: the p.81 "deposits one" fragment (logged [partial], text
not confidently located); the handwritten "Rework" on p.83 (What You Take Out of the Forest),
which asks for more than its marked lines; the Alchemist's category (item 5 of the order).
    python3 instruments/marks_ch3_t10.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# p.76
("The dot is a diagnostic, not a verdict. You are allowed to move.",
 "You are allowed to move."),
("The draw wants a read you already had, and specifically the most recent one that never left your body.",
 "The draw wants a reading you already had: the most recent one that never left your body."),
# p.77
("The second half of this chapter takes up the part of you that decides whether you may use any of it.",
 "The second half of this chapter meets the part of you that decides whether you may use any of it."),
("That part has a name, and you have met it before.",
 "You have met that part before."),
("The practice above works on its own, and it goes on working after you close the book.",
 "The practice above works on its own, after you close the book too."),
("I asked the universe for a sign, and then spent forty minutes deciding whether the sign met my criteria for a sign.\n\nThe retreat had a rule against giving advice. By the third day we had invented a way to give it that sounded like a question.\n\n",
 ""),
("That is integrity, and it is not automatic. It is a part of you doing a job.",
 "That is integrity: a part of you doing a job, not a trait you have."),
("A person with no referee has values the width of whatever is easy that day.",
 "A person with no referee holds values only as wide as that day's convenience."),
("does not trust a private read over the version the group has agreed to. That is a judge now, and it holds court in you.",
 "does not trust a private reading over the version the group has agreed to. That is a judge, holding court in you."),
# p.78
("the one part that could have spoken it clean.",
 "the one part that could have said it plainly."),
("on their own timeline, and you catch yourself docking points for how they did it",
 "on their own timeline. You catch yourself docking points for how they did it"),
("Its other move never blows a whistle at all, because the play never starts.",
 "Its other move never blows a whistle at all. The play never starts."),
("says nothing, and calls the silence rigor.",
 "says nothing and calls the silence rigor."),
("Sensitivity is the Shaman's instrument; this hand keeps it in its case. The cost lands twice:",
 "This hand keeps the Shaman's instrument, sensitivity, in its case. You pay twice:"),
("the ones you would choose on your clearest day.",
 "the ones you would choose with a clear head."),
# p.79
("It shows up in a single beat. Someone on your team",
 "One beat: someone on your team"),
("before you can speak (*probably just my stuff*), and you go along with the group.",
 "before you can speak (*probably just my stuff*). You go along with the group."),
("a read you talked yourself out of with",
 "a reading you talked yourself out of with"),
("The Controller does not block your read with a vague no. It blocks with a verdict about you, and it has six of them, the same six every time:",
 "The Controller does not block your reading with a vague no. It blocks with a verdict about you, one of the same six every time:"),
("The read never reaches the field because the referee who would call it has been ruled ineligible. That is the mechanism.",
 "The reading never reaches the field, because the referee who would call it has been ruled ineligible."),
("while the moment passes, and the judge already has every past ruling on file and infinite patience. It wins on points every time.",
 "while the moment passes. The judge has every past ruling on file, infinite patience, and a perfect record on points."),
("catch the belief in the act of disqualifying your read,",
 "catch the belief in the act of disqualifying your reading,"),
# p.80
("That move gets you through the moment. Something else has to go in",
 "Something else has to go in"),
("The flat inversion fails on the mechanics. *I am good enough* is another verdict",
 "The flat inversion, *I am good enough*, is another verdict"),
("argued on the judge's home ground, and you already know who wins there.",
 "argued on the judge's home ground, where the judge wins."),
("Six verdicts, six replacements. The middle column holds",
 "The middle column holds"),
("which leaves the judge nothing to convene over, and which also means none of them installs by repetition.",
 "which leaves the judge nothing to convene over. None of them installs by repetition."),
# p.81
("is the hinge of the whole chapter, and the chapter's real axis: Feeling and Function.",
 "is the hinge of the whole chapter, its real axis: Feeling and Function."),
("The first half was Feeling: the charge sensed cleanly.",
 "The first half was Feeling: the charge felt clearly."),
("The read does nothing for the person you came to help until it leaves your body",
 "The reading does nothing for the person you came to help until it leaves your body"),
# p.82
("She let the fear be all the way there (",
 "She let the fear stay ("),
("the one who broke the beautiful words.",
 "the one who had spoiled the beautiful words."),
("Then it sat in the circle, and no one could unsay it, and the council had to answer it,",
 "Then it sat in the circle. No one could unsay it, and the council had to answer it,"),
("It moved because one sentence was true and said to the face that could change it.",
 "It moved because one true sentence reached the face that could change it."),
("That is the myth this chapter breaks. Allyship is not saying the right words. The council had the right words, and the right words were the wall.",
 "Allyship is not saying the right words. The council had the right words. The right words were the wall."),
("That move trains the Alchemist. The Alchemist is the one who takes",
 "That move belongs to the Alchemist, the one who takes"),
# p.83
("the read let all the way in,",
 "the reading let all the way in,"),
("You cannot burn a charge you never let yourself have, and you will not spend one while the fear is still live unless some part of you enforces a rule you set on a clearer day. The woman at the council had both, and the rule won. That is a referee doing its job rather than a feeling that finally got loud enough.",
 "You cannot burn a charge you never let yourself have. You will not spend one while the fear is still live unless some part of you enforces a rule you set on a clearer day. The woman at the council had both. The rule won, which is a referee doing its job rather than a feeling that finally got loud enough."),
("You know what your Controller is for now. That is what you take out.",
 "What you take out is what your Controller is for."),
("Theirs is doing the same job in a Forest you cannot see into.",
 "Other people's Controllers do the same job in a Forest you cannot see into."),
("You earn clearance with a Controller by keeping their rule.",
 "Keeping their rule is how you earn clearance with it."),
# p.84
(" Now the table.",
 ""),
("Winning at the Shaman's altitude is smaller than you want it to be: one true sentence, said to a person who can hear it, while it is still live. That is the whole win.",
 "The whole win at the Shaman's altitude is one true sentence, said to a person who can hear it, while it is still live."),
("One sentence counts: the one that left your body, entered the situation, and changed what was possible inside it.",
 "What counts is the sentence that left your body, entered the situation, and changed what was possible inside it."),
("said to the one face that could act on them.",
 "said to the face that could act on them."),
("It is a second layer built on top of the first, and by the time you are working with it, you are no longer reading the situation.",
 "It is a second layer built on top of the first. By the time you are working with it, you are no longer reading the situation."),
("In practice: the marker arrives in the body, because the body registers before the account exists. Heat in the chest, a drop in the stomach, the jaw.",
 "In practice: the marker arrives in the body, which registers before the account exists: heat in the chest, a drop in the stomach, the jaw."),
# p.85
("Accuracy is a separate question and a later one.",
 "Accuracy is a separate, later question."),
("You cannot affect what you cannot feel, and the dial in your hand only ever moved one direction.",
 "You cannot affect what you cannot feel. The dial in your hand only ever moved one direction."),
("That part steers better in the dark, and the low setting is the dark.",
 "That part steers better in the dark. The low setting is the dark."),
("In practice: the marker is the urge to sit up straight",
 "In practice: the sign is the urge to sit up straight"),
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
    print("ch3 tranche 10: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
