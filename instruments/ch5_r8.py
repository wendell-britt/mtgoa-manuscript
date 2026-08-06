# -*- coding: utf-8 -*-
"""ch5_r8.py — R8 across chapter 5's village fable. 17 sites.

Ruled by Wendell 2026-08-02: "batch ch5, ch7, ch8 and the glossary."

Every pair below is lifted verbatim from `editorial_reports/agency/R8_TEST_CH5.md`,
which stress-tested R8 against 25 ch5 sites with six agents instructed to break the
rule rather than confirm it. Only rows the test marked HOLDS or HOLDS WITH TOUCH are
here.

R8 — pluralize the collective. A fictional collective whose members are persons takes
a perception, intention, speech or social-causal verb; change the number and keep every
other word unless grammar forces it. The village is Grade 6 and cannot know, decide or
teach; the villagers are Grade 1 and can.

DELIBERATELY EXCLUDED, per the test's own verdicts:

  line 70 (ii)  BREAKS  "the village's boundaries" -> "the villagers' boundaries"
                swaps a community's shared norms for each person's private boundary,
                a concept the book treats separately. Syllable-neutral, so a
                read-aloud pass cannot catch it. Needs R1.
  line 171      BREAKS  "The village becomes a museum" — people do not become a
                museum. Collective-as-place.
  line 315,628  BREAKS  R8 not applicable; the office/role pattern, where converting
                a critique of a role into a critique of its holders is what the Jerk
                archetype forbids.
  line 165      SHOULD NOT CHANGE, flagged by the test and not ruled.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch5.md"

E = [
    # line 68
    ('For a time the village tried to run on fire alone.',
     'For a time the villagers tried to run on fire alone.'),
    # line 70 (i)
    ('The village felt, for the first time in a long time, *clear about what it stood for.*',
     'The villagers felt, for the first time in a long time, *clear about what they stood for.*'),
    # line 74
    ('After the Challenger left, the village realized it had a different problem: nobody knew how to *hold* the lines across time.',
     'After the Challenger left, the villagers realized they had a different problem: nobody knew how to *hold* the lines across time.'),
    # line 82
    ('The village loved the Regent.',
     'The villagers loved the Regent.'),
    # line 100 (i)
    ('The argument escalated. The village took sides.',
     'The argument escalated. The villagers took sides.'),
    # line 100 (ii)
    ('The village kept the walls. The village kept the traditions. The village kept the roles. What the village lost was the person who knew how to tend them, who could tell the difference between a tradition that still served and a tradition that had become a comfortable cage.',
     'The villagers kept the walls. The villagers kept the traditions. The villagers kept the roles. What the villagers lost was the person who knew how to tend them, who could tell the difference between a tradition that still served and a tradition that had become a comfortable cage.'),
    # line 102
    ('The Regent left because the village no longer knew the difference between protecting and imprisoning.',
     'The Regent left because the villagers no longer knew the difference between protecting and imprisoning.'),
    # line 104
    ('The village never meant for that to happen.',
     'The villagers never meant for that to happen.'),
    # line 153
    ('The village kept the walls. It kept the ceremonies. It kept the roles and the traditions and the weekly councils and the yearly renewals and all the structures the Regent had built.',
     'The villagers kept the walls. They kept the ceremonies. They kept the roles and the traditions and the weekly councils and the yearly renewals and all the structures the Regent had built.'),
    # line 155
    ('The village did the thing the Regent taught them to do, but the meaning underneath it had gone.',
     'The villagers did the thing the Regent taught them to do, but the meaning underneath it had gone.'),
    # line 157
    ("The village didn't realize this was happening. The village thought it was *being faithful.* The Regent had said: *guard the tradition.* So the village guarded it. They guarded it hard. They held the line on how things were done. They enforced the roles. They kept the walls high. They said: *this is how we've always done it* and meant it as a defense",
     "The villagers didn't realize this was happening. The villagers thought they were *being faithful.* The Regent had said: *guard the tradition.* So the villagers guarded it. They guarded it hard. They held the line on how things were done. They enforced the roles. They kept the walls high. They said: *this is how we've always done it* and meant it as a defense"),
    # line 161
    ("The village developed a specific, recognizable distortion: **obedience without understanding.** The village learned to follow the Regent's structures without knowing *why* the structures existed. They kept the form and lost the function. They said the words and missed the meaning. They performed the role and forgot the person.",
     "The villagers developed a specific, recognizable distortion: **obedience without understanding.** The villagers learned to follow the Regent's structures without knowing *why* the structures existed. They kept the form and lost the function. They said the words and missed the meaning. They performed the role and forgot the person."),
    # line 169
    ("The village does this with the Regent's gift once the Regent has gone: it turns protection into imprisonment. It turns inheritance into cargo cult. It turns the beautiful complexity of a living tradition into the comfortable mechanical repetition of its form, and then calls that faithfulness.",
     "The villagers do this with the Regent's gift once the Regent has gone: they turn protection into imprisonment. They turn inheritance into cargo cult. They turn the beautiful complexity of a living tradition into the comfortable mechanical repetition of its form, and then call that faithfulness."),
    # line 305
    ('The village never taught you this question: what did you inherit?',
     'The villagers never taught you this question: what did you inherit?'),
    # line 313
    ('The village conflated loyalty with compliance, and then wondered why the institutions it served became so brittle.',
     'The villagers conflated loyalty with compliance, and then wondered why the institutions they served became so brittle.'),
    # line 711
    ('The Regent did not leave the village because the village was wrong to need structure. The Regent left because the village could not tell the difference between loyalty and obedience, between a tradition worth protecting and a cage disguised as belonging. The village needed someone who could hold both, the love of what was handed down and the willingness to reform it.',
     'The Regent did not leave the village because the villagers were wrong to need structure. The Regent left because the villagers could not tell the difference between loyalty and obedience, between a tradition worth protecting and a cage disguised as belonging. The villagers needed someone who could hold both, the love of what was handed down and the willingness to reform it.'),
    # line 717
    ("The village exiled the Architect for a specific reason: it mistook *seeing the system* for *not loving the people inside it.* If you can analyze it, the village said, you don't really love it.",
     "The villagers exiled the Architect for a specific reason: they mistook *seeing the system* for *not loving the people inside it.* If you can analyze it, the villagers said, you don't really love it."),
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
    print("ch5.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
