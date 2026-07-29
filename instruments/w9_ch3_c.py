# -*- coding: utf-8 -*-
"""
W9 — ch3 em-dash pass, batch C (Sections 6-7, the five moves and the four domains).

The four `You're winning when:` markers are the tightest structure in the
chapter: read, then a dash-clause gloss naming the harder version, then the
delivery. All four take comma pairs so the shape survives, except *Skillful
Organizing*, where the gloss is itself a three-item list and a comma pair would
put five commas in one clause. That one takes parentheses.

One dash stays, converted rather than removed: `"What's really going on here
is—"` is a quotation cut off mid-phrase, which is the one job an em-dash does
that nothing else does. It becomes an ellipsis, the mark that actually means
*trailing off*, so the sentence keeps its meaning and the count still falls.

    python3 instruments/w9_ch3_c.py --dry
    python3 instruments/w9_ch3_c.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
("the spiral wearing a new name — the spiral gets you the read.",
 "the spiral wearing a new name. The spiral gets you the read."),
("The story comes next — who did what, what it says about them,",
 "The story comes next: who did what, what it says about them,"),
("your explanation of the situation — a document you wrote.",
 "your explanation of the situation, a document you wrote."),
("Everything downstream — the channel you name, the sentence you say, the domain you spend it in — is only as good as",
 "Everything downstream (the channel you name, the sentence you say, the domain you spend it in) is only as good as"),
("The story is already assembling — *they are undermining me,",
 "The story is already assembling: *they are undermining me,"),
("You say which channel runs — yours, or the field's — where other people can hear it.",
 "You say which channel runs, yours or the field's, where other people can hear it."),
("You say the read — what moves underneath the stated discussion — to the people it concerns,",
 "You say the read, what moves underneath the stated discussion, to the people it concerns,"),
("so that nobody can argue with you — and the case is where the read goes to die",
 "so that nobody can argue with you, and the case is where the read goes to die"),
("usually say what it requires — more time, a different person",
 "usually say what it requires: more time, a different person"),
("a documented need with a number on it — something a budget cycle",
 "a documented need with a number on it, something a budget cycle"),
("It gets spent — said, asked, acted on, put somewhere", "It gets spent: said, asked, acted on, put somewhere"),
("it will not get spent — it will get understood.", "it will not get spent. It will get understood."),
("inside the window you set — said, asked, acted on, or deliberately let go.",
 "inside the window you set: said, asked, acted on, or deliberately let go."),
("makes it public and useful — the only transaction this Face performs.",
 "makes it public and useful, the only transaction this Face performs."),
("showed one of the four — Direct Action, the true thing said to a face.",
 "showed one of the four: Direct Action, the true thing said to a face."),
("same safety runs alongside it — you do say something, but only the correct words, the ones no one can fault — and that is the awareness trap",
 "same safety runs alongside it. You do say something, but only the correct words, the ones no one can fault, and that is the awareness trap"),
("So here are all four — and before them, the three things that decide whether saying it helps or wounds. Not to study — pick where",
 "So here are all four, and before them the three things that decide whether saying it helps or wounds. Not to study: pick where"),
("helps the person or wounds them — and the same three moves decide it",
 "helps the person or wounds them, and the same three moves decide it"),
("the read tells you it landed — they get defensive, or shut down, or well up.",
 "the read tells you it landed: they get defensive, or shut down, or well up."),
("reaches to put a lid on it — theirs, this time: *no, no, I didn't mean it like that.*",
 "reaches to put a lid on it, theirs this time: *no, no, I didn't mean it like that.*"),
("\"What's really going on here is—\" is the judge", "\"What's really going on here is…\" is the judge"),
("Staying — present, not defending, not adding anything — lets the truth land",
 "Staying present, without defending and without adding anything, lets the truth land"),
("true thing you had been feeling — the unsaid charge, not the softened hint — to the face it concerns,",
 "true thing you had been feeling, the unsaid charge and not the softened hint, to the face it concerns,"),
("you said what was actually happening — the read under the approved language — to the real people",
 "you said what was actually happening, the read under the approved language, to the real people"),
("what a situation actually needs — the real ask, not the palatable one you were already sure would be granted — and you asked the person",
 "what a situation actually needs, the real ask and not the palatable one you were already sure would be granted, and you asked the person"),
("and no one will touch — the resentment, the power nobody names, the silence everyone is keeping — to the group,",
 "and no one will touch (the resentment, the power nobody names, the silence everyone is keeping) to the group,"),
("the Architect's design — not one of them is worth anything",
 "the Architect's design: not one of them is worth anything"),
("why one true sentence — said, not just felt — is the move everything else will stand on.",
 "why one true sentence, said and not only felt, is the move everything else will stand on."),
("That question is real — a Shaman who names the unsaid to be seen as the most perceptive person present has run the awareness trap with better production values — but it is the easiest thing",
 "That question is real. A Shaman who names the unsaid to be seen as the most perceptive person present has run the awareness trap with better production values. It is also the easiest thing"),
("- **Direct Action —** Did you say the true thing", "- **Direct Action.** Did you say the true thing"),
("- **Raise Awareness —** Did you name what is happening", "- **Raise Awareness.** Did you name what is happening"),
("- **Gather Resources —** Did you ask for what the situation needs", "- **Gather Resources.** Did you ask for what the situation needs"),
("- **Skillful Organizing —** Did you name the unsaid thing", "- **Skillful Organizing.** Did you name the unsaid thing"),
("also an *operation* — a thing every move can do — which means you are not holding",
 "also an *operation*, a thing every move can do, which means you are not holding"),
("interior and goes external — gathering resources, raising awareness, direct action, skillful organizing — and five times four",
 "interior and goes external (gathering resources, raising awareness, direct action, skillful organizing), and five times four"),
("begin with the same verb — *name.*", "begin with the same verb: *name.*"),
("come out, one per row — exactly what makes the grid worth having",
 "come out, one per row, exactly what makes the grid worth having"),
("an experience would show — which is Open Up.", "an experience would show, which is Open Up."),
("Take **What Seeing Costs** — Open Up, Raise Awareness, Shaman.",
 "Take **What Seeing Costs**: Open Up, Raise Awareness, Shaman."),
("Clean Up: name the channel — Fire, Water, Metal, Earth, Wood.",
 "Clean Up: name the channel, one of Fire, Water, Metal, Earth, Wood."),
("come from the Show Up row — every card in it ends in an artifact",
 "come from the Show Up row, and every card in it ends in an artifact"),
("any move you make in the world — there is pattern.**", "any move you make in the world, there is pattern.**"),
("to read that pattern — in yourself, in others, in the group.",
 "to read that pattern, in yourself, in others, in the group."),
("That is the Skeptic — the part that doubts your own knowing before anyone else can — and the next face begins there.",
 "That is the Skeptic, the part that doubts your own knowing before anyone else can, and the next face begins there."),
("about what's unacceptable — if you haven't read the emotional truth underneath — then the Challenger's line is performance.",
 "about what's unacceptable, if you haven't read the emotional truth underneath, then the Challenger's line is performance."),
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
