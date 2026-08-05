# -*- coding: utf-8 -*-
"""ch4_r8.py — the mechanical half of ch4's fable. 20 sites.

Ruled by Wendell 2026-08-02: "take your half", after he took the four breaks.

Pairs marked plainly are lifted verbatim from `R8_TEST_CH4.md`. Pairs marked `[VAR]` are
hand-built, because the site is one of the ellipsis-joined multi-instance rows the test
quotes in summary, and because R8's own pre-flight check 4 fires on them: **more than two
in a paragraph and variation is mandatory, not taste.**

`ch4:117` is the densest spot in the book — five `the village` inside roughly sixty words,
in a sentence whose repetition is doing rhetorical work (*Not because the village didn't
feel them — the village felt every one of them*). A straight suffix pass would have put
five `the villagers` in that span. Noun once, then pronouns: the figure survives, the tic
does not.

`ch4:167` is worth noting for the opposite reason. Its second half already reads *"cannot
draw **their** own without apologizing"* — the prose was already unstable on number before
anything was edited, exactly as `ch8:87` was. The plural regularises a defect that was
sitting there uncorrected rather than introducing one.

**A density figure this script does NOT act on.** After these edits ch4's fable carries
roughly twenty plural subjects across 110 lines. That is the same repetition rate the
singular had — R8 changes the number, not the count — so no tic was introduced. Whether
110 lines want that many identical subjects at all is a rhythm judgement about prose that
was already written that way, and it belongs to Wendell, not to this pass. `R8_TEST_CH8`
ruled variation mandatory for ch8 on volume; `R8_TEST_CH4` did not make the same ruling
here, and this script follows each chapter's own test rather than generalising one.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch4.md"

E = [
    # line 70
    ('The village built rituals around this.',
     'The villagers built rituals around this.'),
    # line 78
    ('The village chose the Regent.',
     'The villagers chose the Regent.'),
    # line 90
    ('That the village had confused *organized power* with *actual power* and could not tell the difference.',
     'That the villagers had confused *organized power* with *actual power* and could not tell the difference.'),
    # line 92
    ('The village never meant for that to happen. It never said "go." It just stopped asking. Which, it turns out, is the same thing as exile.',
     'The villagers never meant for that to happen. They never said "go." They just stopped asking. Which, it turns out, is the same thing as exile.'),
    # line 99
    ("Here's what happened after the Challenger left: the village didn't stop needing to draw lines.",
     "Here's what happened after the Challenger left: the villagers didn't stop needing to draw lines."),
    # line 101
    ('It just forgot how to do it without apologizing.',
     'They just forgot how to do it without apologizing.'),
    # line 103
    ('the village learned to *process* these moments instead of *respond* to them.',
     'the villagers learned to *process* these moments instead of *respond* to them.'),
    # line 111
    ('The village started mistaking politeness for peace. Started confusing *everyone being comfortable* with *everyone being safe.*',
     'The villagers started mistaking politeness for peace. Started confusing *everyone being comfortable* with *everyone being safe.*'),
    # line 113
    ('Without the Challenger, the village developed a sophisticated language for everything except the clean no.',
     'Without the Challenger, the villagers developed a sophisticated language for everything except the clean no.'),
    # line 115b (village, anchor's aphorism)
    ('The village learned to make its nos sound like yeses because yeses cost less.',
     'The villagers learned to make their nos sound like yeses because yeses cost less.'),
    # line 119
    ('Without the Challenger, the village also lost something else: the willingness to *be* unwelcome.',
     'Without the Challenger, the villagers also lost something else: the willingness to *be* unwelcome.'),
    # line 123
    ('The village does this with the clean no once the Challenger has gone: it transforms it into *performative diplomacy.*',
     'The villagers do this with the clean no once the Challenger has gone: they transform it into *performative diplomacy.*'),
    # line 136
    ('The village hears the clean no as aggression: the angry one, the difficult one, the one who makes things worse before they get better, someone who says no because they want to win.',
     'The villagers hear the clean no as aggression: the angry one, the difficult one, the one who makes things worse before they get better, someone who says no because they want to win.'),
    # line 140
    ('Because the village has gotten very sophisticated about this. The village has learned to make its nos sound like preferences, its lines sound like suggestions, its non-negotiables sound like flexible guidelines.',
     'Because the villagers have gotten very sophisticated about this. The villagers have learned to make their nos sound like preferences, their lines sound like suggestions, their non-negotiables sound like flexible guidelines.'),
    # line 175
    ('The village, without the Challenger, has forgotten the difference.',
     'The villagers, without the Challenger, have forgotten the difference.'),
    # line 117 [VAR]
    ("So the village started letting things slide. Small violations first. Then larger ones. Not because the village didn't feel them (the village felt every one of them) but because the village had lost the Challenger's gift",
     "So the villagers started letting things slide. Small violations first. Then larger ones. Not because they didn't feel them (they felt every one of them) but because they had lost the Challenger's gift"),
    # line 117b [VAR]
    ('The village, without the Challenger, could no longer hold those two things together.',
     'They could no longer hold those two things together without the Challenger.'),
    # line 125 [VAR]
    ('The village did all of this with good intentions.',
     'The villagers did all of this with good intentions.'),
    # line 125b [VAR]
    ('Because saying no cost something and the village had decided, without ever announcing it, to stop paying.',
     'Because saying no cost something and they had decided, without ever announcing it, to stop paying.'),
    # line 167 [VAR]
    ('The village without the Challenger cannot do this. The village can feel the violation but cannot name it cleanly.',
     'The villagers without the Challenger cannot do this. They can feel the violation but cannot name it cleanly.'),
    # line 90b [VAR] — a second instance in the same sentence the test itemised only once.
    ('The Challenger understood what the village did not:',
     'The Challenger understood what the villagers did not:'),
    # line 121 [VAR] — HOLDS WITH TOUCH. The simile needs singular-to-singular parity:
    # pluralising only the subject compares many people to one organism. "a body" ->
    # "bodies" is also a syllable wash, 25 -> 25.
    ('The village became afraid of conflict the way a body becomes afraid of a low-grade fever',
     'The villagers became afraid of conflict the way bodies become afraid of a low-grade fever'),
    ('became something the village treated as a symptom of its own inadequacy rather than a capacity it needed to develop',
     'became something they treated as a symptom of their own inadequacy rather than a capacity they needed to develop'),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch4.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
