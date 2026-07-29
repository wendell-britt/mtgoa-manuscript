# -*- coding: utf-8 -*-
"""
W8 batch C — the remaining 17 denying negations, ch1–ch6 and ch8–ch9.

Same method as batch B. Two shapes recur and get different treatment:

  · Padding. The denied half repeats what the sentence before already said, so
    it comes out and nothing replaces it. ("The inner work is not separate from
    the game." "It is not clarity — it is hiding," where the previous sentence
    already said people mistake it for clarity.)
  · Load-bearing. The reader really would guess the wrong answer, so the wrong
    guess gets its own sentence with a verb in it, then the claim stands alone.
    ("Timidity would look the same from outside." "Neutrality is the easy guess.")

Two negative listings — ch4's *not the willingness to fight, and not certainty*
and ch5's *not emotion, not will, not even logic* — become positive claims. The
ch5 one turns three denials into a real statement about the other three Faces,
which the chapter wanted anyway.

Not touched: ch7:399, the italic shadow-speech, and its twins in ch4 and ch6.

    python3 instruments/w8_batch_c.py
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
"ch1.md": [
("So a game is not a trick for making serious work go down easier. It is the only structure that generates the energy to keep doing serious work for a lifetime instead of one burnout cycle.",
 "Calling a game a trick for making serious work go down easier gets it backwards. A game is the only structure that generates the energy to keep doing serious work for a lifetime instead of one burnout cycle."),
("Write down the version of your face you fall into on empty. It is not your enemy; it is your tell.",
 "Write down the version of your face you fall into on empty. Treat it as your tell rather than your enemy."),
],
"ch2.md": [
("The problem is not that you wanted to be good. The problem is that trying to seem good takes the whole body.",
 "Wanting to be good was never the problem. Trying to seem good takes the whole body."),
("Recognition is not completion. It is where the move begins.",
 "Recognition is where the move begins, and beginning is all it is."),
("Saying it out loud is not a technique. It's how that part comes home: it finds out it's allowed to speak.",
 "Saying it out loud is how that part comes home. It finds out it's allowed to speak."),
],
"ch3.md": [
("These are not problems. They are *signals.*",
 "You have been calling these problems. They are *signals.*"),
("The six beliefs are not stray bad thoughts about yourself; they are the specific tool the Controller uses to keep your Shaman move from ever getting made.",
 "The six beliefs read like stray bad thoughts about yourself. They are the specific tool the Controller uses to keep your Shaman move from ever getting made."),
],
"ch4.md": [
("The Reckoning is not a threat. It is a consequence stated plainly. A natural result made visible.",
 "The Reckoning states a consequence plainly. A natural result made visible. A threat has to manufacture the consequence; the Reckoning only reports it."),
("Triumph here is not winning the exchange — it is the specific satisfaction of *I can act*, which Fire wants and almost never gets.",
 "Triumph here is the specific satisfaction of *I can act*, which Fire wants and almost never gets. Winning the exchange has nothing to do with it."),
("That is not timidity. That is what makes your no expensive.",
 "Timidity would look the same from outside. That is what makes your no expensive."),
("The Challenger's superpower is not the willingness to fight, and not certainty. It is the willingness to be unwelcome on a charge you have checked and chosen to trust — clarity without cruelty, held steady long enough to say one sentence and stay for what follows.",
 "The Challenger's superpower is the willingness to be unwelcome on a charge you have checked and chosen to trust — clarity without cruelty, held steady long enough to say one sentence and stay for what follows. Fighting comes easy by comparison, and so does certainty."),
("Most people mistake the three-paragraph explanation for clarity. It is not clarity — it is *hiding.*",
 "Most people mistake the three-paragraph explanation for clarity. The explanation is *hiding.*"),
],
"ch5.md": [
("The native material at the Regent's altitude is not emotion. It's not will. It's not even logic. It's **loyalty**",
 "The Shaman works in emotion, the Challenger in will, the Architect in logic. The native material at the Regent's altitude is **loyalty**"),
],
"ch6.md": [
("Both poles are real goods. That is not a hedge; it is the condition that makes the shadow workable.",
 "Both poles are real goods. That condition is what makes the shadow workable."),
],
"ch8.md": [
("These three are not obviously wrong. The Sage in distortion is doing versions of useful things",
 "Each of these three looks defensible. The Sage in distortion is doing versions of useful things"),
("The five moves are not a sequence. They're a toolkit.",
 "The five moves are a toolkit."),
],
"ch9.md": [
("**The five moves are not the practice. They are the map of the practice.**",
 "**The five moves are the map. The practice is the walking.**"),
],
}


def main():
    staged, bad = [], []
    for name, pairs in EDITS.items():
        p = os.path.join(MS, name)
        t = io.open(p, encoding="utf-8").read()
        for a, b in pairs:
            n = t.count(a)
            if n != 1:
                bad.append((name, n, a[:64]))
            else:
                t = t.replace(a, b, 1)
        staged.append((p, t))
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for name, n, a in bad:
            print("  %s  %d matches: %r" % (name, n, a))
        return 1
    for p, t in staged:
        io.open(p, "w", encoding="utf-8").write(t)
    print("applied %d edits across %d files" % (sum(len(v) for v in EDITS.values()), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
