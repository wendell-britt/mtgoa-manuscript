# -*- coding: utf-8 -*-
"""
W2 — the 25 stopping conditions, plus ch7's five rewritten to match.

Form states the act and defers the outcome positively. The earlier
"the test is not [outcome]. The test is [act]" form prescribed by EXERCISE_AUDIT,
GAME_LOOP_GAP_ANALYSIS and the handoff is the denying-negation shape the house
rule bans — see W7. Ch7's five were built on it and are replaced here, which
also settles R6: three of them were outcome-based against their own prescription.

Insertion lands after each move block's last substantive line, before any
trailing rule. Chapters differ: ch3/4/6/9 close each move with `---`, ch5 does
not, so the separator is not used as the anchor.

    python3 marginalia/compile.py --strip
    python3 instruments/w2_edits.py --check     # show placement, write nothing
    python3 instruments/w2_edits.py
    python3 marginalia/compile.py --apply
"""
import io, os, re, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

TESTS = {
3: {
1:"**The test:** You noticed where it landed in your body before you had a sentence explaining it. Accuracy is a separate question and a later one. If you can name the place and not the reason, you caught it in time.",
2:"**The test:** You said it out loud, in the moment, where someone could disagree with it. Agreement is theirs to give or withhold. A channel named only to yourself belongs to Section 4.",
3:"**The test:** What you said was the read you actually had, and you said it while it was still live. What the conversation did afterward belongs to the conversation. A true thing said an hour late is a different move.",
4:"**The test:** What left your mouth was the size of the real need rather than the size you were confident would be granted. A no to the real ask beats a yes to the shrunken one, so score the ask.",
5:"**The test:** It left you inside the window you set — said, asked, acted on, or deliberately let go. Whether it changed anything is a separate question. A read still under review on Friday was banked.",
},
4: {
1:"**The test:** The thing is now named, stated plainly, in the moment, with no solution attached. What the group does with it next is the group's. The naming is the whole move.",
2:"**The test:** The line left your mouth without an essay, a justification, or an apology attached. Count the words afterward: more than you needed means you were explaining, whatever they did in response.",
3:"**The test:** It stayed a no — unexplained, unsoftened, still a no by the end of the sentence. Acceptance is theirs. Your part finished when the word did.",
4:"**The test:** The content stayed hard while the delivery stayed clean. Softening the content to keep the delivery kind is a different move, and you will know which one you did.",
5:"**The test:** You were still there when the discomfort passed, having neither softened, clarified, nor apologized for what you had already said. How long it took is a separate question.",
},
5: {
1:"**The test:** You named what arrived before you changed any of it. Finding something worth keeping is a bonus, not the bar. If the first change is already made, you skipped the move.",
2:"**The test:** You can say what would break if it were removed. Agreement from anyone else is a separate question. A thing you cannot name a breakage for is a preference wearing inheritance.",
3:"**The test:** You named what the tradition was trying to do before you changed how it does it, and you told people which of the two you were changing. Results arrive on their own schedule.",
4:"**The test:** You kept it on the day it would have cost you nothing to drop it and nobody would have known either way. Being noticed is a separate question, and usually the answer is no.",
5:"**The test:** What you handed over was context rather than anxiety. Context lets them decide; anxiety tells them what you need the outcome to look like. Their version will differ from yours, which is the point.",
},
6: {
1:"**The test:** You named one place and pushed there, instead of pushing everywhere at once with the same force. Cascades are slow and often invisible. One named point is the move.",
2:"**The test:** You got it stated — moved from something everyone treats as given to something on the table that can be examined. Whether it turns out to be false is a separate question.",
3:"**The test:** You asked who runs this after me before you shipped, and wrote down the one thing you were assuming they already knew. The system's survival is next year's evidence.",
4:"**The test:** It reached a real person while it was still embarrassing to show. A version you shipped once you were comfortable with it arrived late, however well that version performed.",
5:"**The test:** You changed it without filing the previous version as a mistake. It got you here, and saying so out loud is part of the move. Quality of the new design is a separate question.",
},
9: {
1:"**The test:** A stranger can repeat your sentence back to you without adding anything. Picking the right problem is a separate question. If they have to ask which part you mean, the field is still wide.",
2:"**The test:** You showed it at the point you would rather have kept working on it alone, to one person who could answer you. Their verdict is theirs. The showing is yours.",
3:"**The test:** You rebuilt, having first asked what would follow if the note were true instead of disqualifying the person who gave it. Whether the rebuild is better is a separate question.",
4:"**The test:** You named the one variable before you ran it and changed nothing else. Two changes at once tell you nothing about either, however the second run went.",
5:"**The test:** You said, in advance and in specifics, what they were allowed to change. *Make it your own* is a compliment; a handoff names the boundary. What they do inside it is theirs.",
},
}

# ch7: replace in place. Three were outcome-based (R6), one carried the banned
# shape (W7), one was already act-based and is aligned to the common form.
CH7 = [
("""**The test:** You know you've done it when both sides say *yes, that's actually what this is about.* If they don't, you update and try again.""",
 """**The test:** You said what the field is actually about, in one sentence, in front of the people standing in it. Whether they accept the description is theirs to answer, and a correction is the move working rather than failing."""),
("""**The test:** You know you've done it when both camps say *yes, that's what we mean* — and neither camp says you got it wrong.""",
 """**The test:** You put each camp's position into language the other camp could hear, without softening either one to make the fit easier. Whether both sides accept your rendering is theirs to say."""),
("""**The test:** The test of honest terms is not whether they change their behavior when you name them. The test is whether the naming itself was honest. Did you name what you actually need from the agreement, or did you name a softer version because you were afraid to name the real one? If you named the real terms and nothing changed, that's not a failure. That's information.""",
 """**The test:** You named what you actually need from the agreement rather than a softer version, said it once, and left it alone for the field to answer. Their behavior may or may not change. If you named the real terms and nothing moved, that is information."""),
("""**The test:** You know repair is real when the other person can name the rupture back to you accurately without you needing to explain it, and can name your part without you needing to correct them. If they're still explaining it back to you as if it was entirely your fault, the repair hasn't landed yet. Go back to step one.""",
 """**The test:** You named what broke, named your part in it, named what you were not asking for, and stayed. Whether they can name it back to you accurately yet is a separate question, and often a later one. If it is still landing as entirely your fault, go back to step one."""),
("""**The test:** You know your refusal is honest when you can paraphrase the opposing position accurately enough that its strongest advocate would recognize it, and then say *here is why I still don't agree.*""",
 """**The test:** You paraphrased the opposing position accurately enough that its strongest advocate would recognize it, and then said *here is why I still don't agree.* Whether they grant the distinction is theirs."""),
]

HDR = re.compile(r'^### Move (\d+)\b')
STOP = re.compile(r'^(### Move |## )')


def place(lines, tests):
    """Return list of (insert_index, move_no). Insert after last substantive line."""
    out = []
    idx = [i for i, l in enumerate(lines) if HDR.match(l)]
    for i in idx:
        mv = int(HDR.match(lines[i]).group(1))
        if mv not in tests:
            continue
        j = i + 1
        while j < len(lines) and not STOP.match(lines[j]):
            j += 1
        # A move closes at its own first `---`. Past that, Move 5's block runs on
        # into section-level wrap-up (ch3's Tells, ch6's "the Architect's game",
        # ch9's sixty-second exercise), and the test must not attach to those.
        # ch5 has no rules between moves, so fall back to the block end.
        end = next((k for k in range(i + 1, j) if lines[k].strip() == '---'), j)
        last = None
        for k in range(end - 1, i, -1):
            s = lines[k].strip()
            if s and s != '---':
                last = k
                break
        if last is None:
            return None, "no body found for Move %d" % mv
        out.append((last, mv))
    return out, None


def main():
    check = "--check" in sys.argv
    total = 0

    for ch, tests in sorted(TESTS.items()):
        p = os.path.join(MS, "ch%d.md" % ch)
        lines = io.open(p, encoding="utf-8").read().split('\n')
        if '**The test:**' in '\n'.join(lines):
            print("ABORT ch%d: already has a test marker" % ch)
            return 1
        spots, err = place(lines, tests)
        if err:
            print("ABORT ch%d: %s" % (ch, err))
            return 1
        if len(spots) != 5:
            print("ABORT ch%d: found %d moves, expected 5" % (ch, len(spots)))
            return 1
        for at, mv in sorted(spots, reverse=True):
            if check:
                print("  ch%d M%d -> after: %s…" % (ch, mv, lines[at].strip()[:64]))
            else:
                lines.insert(at + 1, "")
                lines.insert(at + 2, tests[mv])
        if not check:
            io.open(p, "w", encoding="utf-8").write('\n'.join(lines))
        total += 5

    p7 = os.path.join(MS, "ch7.md")
    t7 = io.open(p7, encoding="utf-8").read()
    for i, (a, b) in enumerate(CH7, 1):
        n = t7.count(a)
        if n != 1:
            print("ABORT ch7 rewrite #%d: %d matches" % (i, n))
            return 1
        t7 = t7.replace(a, b, 1)
    if not check:
        io.open(p7, "w", encoding="utf-8").write(t7)
    total += 5

    print("%s %d stopping conditions (25 new, 5 rewritten in ch7)"
          % ("would place" if check else "placed", total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
