# -*- coding: utf-8 -*-
"""
W9 — ch3 em-dash pass, batch A (Sections 1-2, the village history and the WAVE).

ch3 is the heaviest chapter in the book at 15.3/1k and it earns that in one
specific way: a five-fold anaphora, *When you do this with fear / anger /
sadness / joy*, where every arm is built as dash-clause-dash. Converting all
five to comma pairs keeps the figure and removes the crutch. The figure was
never the dashes.

Four dashes here are **unspaced** and the gate never saw them, because its
emdash counter reads `[a-zA-Z0-9,]—[a-zA-Z0-9]` and these sit against a quote
mark, a bracket, or an asterisk: `realized—*not trusted anymore*`, `real risk
lives"—fear became`, `what matters"—anger became`, `this chapter)—when you`.
All four go.

    python3 instruments/w9_ch3_a.py --dry
    python3 instruments/w9_ch3_a.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
("the Diplomat, the Sage — all of them run the same instrument",
 "the Diplomat, the Sage: all of them run the same instrument"),
("the village's oldest advisor — the one who knew how to read the feeling",
 "the village's oldest advisor: the one who knew how to read the feeling"),
("feel it fully, was information — not weakness.", "feel it fully, was information, not weakness."),
("It came on gradually — the way a house gets colder", "It came on gradually, the way a house gets colder"),
("following the Challenger's lead — valuing speed over discernment",
 "following the Challenger's lead, valuing speed over discernment"),
("comes from sitting with complexity — the Shaman became less necessary.",
 "comes from sitting with complexity, the Shaman became less necessary."),
("needed less and finally — one day the Shaman realized—*not trusted anymore.*",
 "needed less and finally, one day, the Shaman realized: *not trusted anymore.*"),
("\"fear is your compass — it's showing you where the real risk lives\"—fear became just a noise.",
 "\"fear is your compass, it's showing you where the real risk lives,\" fear became noise."),
("\"anger is a boundary signal — it's telling you what matters\"—anger became dangerous.",
 "\"anger is a boundary signal, it's telling you what matters,\" anger became dangerous."),
("\"sadness is how we honor what mattered\"—sadness became shameful.",
 "\"sadness is how we honor what mattered,\" sadness became shameful."),
("the manic performance of joy — the \"yay team, we're doing good\" energy that masks exhaustion — the village learned",
 "the manic performance of joy (the \"yay team, we're doing good\" energy that masks exhaustion), the village learned"),
("that joy was also information — a signal that something true was happening",
 "that joy was also information, a signal that something true was happening"),
("Because the Challenger was right—*something had to be done.*",
 "Because the Challenger was right: *something had to be done.*"),
("The emotion would arrive — theirs and mine — and my chest would do",
 "The emotion would arrive, theirs and mine, and my chest would do"),
("Then I'd be gone. Not literally — I stayed on the call,",
 "Then I'd be gone. Not literally. I stayed on the call,"),
("you can actually move to service — the thing I thought I was doing all along.",
 "you can move to service, the thing I thought I was doing all along."),
("when someone got upset — that was my discomfort, not theirs.",
 "when someone got upset was my discomfort, not theirs."),
("I eventually invented a game — Tough Conversations.", "I eventually invented a game, Tough Conversations."),
("said next was the real thing — not the complaint, not the position,",
 "said next was the real thing, not the complaint, not the position,"),
("their own emotional problem — the need to feel useful, effective,",
 "their own emotional problem: the need to feel useful, effective,"),
("something from the encounter — both parties more real at the end than they were at the start.",
 "something from the encounter, both parties more real at the end than at the start."),
("may already feel familiar — you have likely built some language",
 "may already feel familiar. You have likely built some language"),
("what the group never registers — not dangerous, not catastrophic,",
 "what the group never registers, not dangerous, not catastrophic,"),
("in a moment that isn't yours — then give the consensus",
 "in a moment that isn't yours, then give the consensus"),
("practice with a governor on it — one installed by instructions",
 "practice with a governor on it, one installed by instructions"),
("When you feel neutrality — that spacious, clear quality — you're receiving",
 "When you feel neutrality, that spacious, clear quality, you're receiving"),
("When you do this — when you actually make space for fear instead of overriding it — fear teaches you",
 "When you do this, when you make space for fear instead of overriding it, fear teaches you"),
("When you do this with anger — when you let yourself be angry instead of converting it into activism — anger teaches you",
 "When you do this with anger, when you let yourself be angry instead of converting it into activism, anger teaches you"),
("When you do this with sadness — when you actually grieve instead of rushing past it — sadness teaches you",
 "When you do this with sadness, when you grieve instead of rushing past it, sadness teaches you"),
("that you should just move on — sadness is the voice", "that you should move on. Sadness is the voice"),
("When you do this with joy — and most people skip this one,", "When you do this with joy, and most people skip this one,"),
("harder than anything in this chapter)—when you actually *land* in joy instead of using it for fuel — joy teaches you",
 "harder than anything in this chapter), when you *land* in joy instead of using it for fuel, joy teaches you"),
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
