# -*- coding: utf-8 -*-
"""ch8_r8.py — R8 across chapter 8, with the variation rotation the test makes mandatory.

Ruled by Wendell 2026-08-02: "batch ch5, ch7, ch8 and the glossary."

**Ch8 is the one that is not a batch, and the audit says so in its own words.**
`R8_TEST_CH8.md` scores a sentence-level break rate of **0 of 23** and then rules the
chapter needs variation anyway:

> "23 identical subject-nouns in one chapter reads as a tic regardless of which noun it is.
> R8 does not get an exemption from that discipline just because the noun it repeats is
> grammatically licensed. **A licensed tic is still a tic.** … That is an edit, not a suffix
> pass. It costs the same editorial attention R1 cost. The 'cheaper than R1' claim holds
> only if variation is optional. **It is not optional at this volume.**"

12 of the sites sit inside one 32-line, ~900-word fable — a new subject-noun roughly every
75 words for three pages — and seven more stack into 12 lines in Section 2. So every
replacement below is the test's own R8 wording **except** where density forced a variant,
and each of those is marked `[VAR]` with which of the four moves it uses.

The variation set, from the test: full noun on first mention in a run · pronoun continuation
once the antecedent is established · the passage's own concrete nouns (*everyone*, *the
people there*) · *no one* / *nobody* for negation.

Section 1 now runs: villagers · (noun removed) · villagers · they · everyone · villagers +
they · everyone · people there + they · no one + nobody. **No two `the villagers` in
adjacent sentences.**

DELIBERATELY EXCLUDED, per the test and the R8 pre-flight checks:

  line 162  `the village's version` — possessive. Pre-flight check 1 routes possessives to
            R6 or compression, never R8.
  line 164  SHOULD NOT CHANGE, flagged by the test and not ruled.
  lines 56, 136  section headings, outside the ledger's declared body-text scope.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch8.md"

E = [
    # --- Section 1, the fable -------------------------------------------------
    # 77 — first mention, sets the antecedent for the whole fable.
    ("The village noticed this.",
     "The villagers noticed this."),

    # 85 [VAR — noun removed]. The test's own note: "a candidate for the pronoun-
    # continuation variant instead: 'What landed instead was...' works equally well under
    # R8's plural and avoids stacking the noun twice this close together."
    ("The village heard: *I see this and I'm not on your side.*",
     "What landed instead was: *I see this and I'm not on your side.*"),

    ("The village had gotten used to wisdom as a form of leaving.",
     "The villagers had gotten used to wisdom as a form of leaving."),

    # 89 [VAR — pronoun continuation]. The verdict's flagship example is "The villagers had
    # made a rule"; it scans, but it would be the third `villagers` in three paragraphs.
    ("The village had made a rule: if you can see the pattern of the game, you must stop "
     "playing.",
     "They had made a rule: if you can see the pattern of the game, you must stop "
     "playing."),

    # 93 [VAR — swap-in noun].
    ("and the village reading that as contradiction",
     "and everyone reading that as contradiction"),

    # 95 — noun, then pronoun inside the same paragraph.
    ("The village did not know this: the Sage contradicted nothing.",
     "The villagers did not know this: the Sage contradicted nothing."),
    ("The village asked: *are you in the game or are you wise?*",
     "They asked: *are you in the game or are you wise?*"),

    # 97 [VAR — swap-in noun].
    ("The village wanted wisdom to look like departure.",
     "Everyone wanted wisdom to look like departure."),

    # 99 [VAR — swap-in noun, then pronoun].
    ("One day, the village made its preference official.",
     "One day, the people there made their preference official."),
    ("The village kept the caricature.",
     "They kept the caricature."),

    # 105 [VAR — negative quantifier]. The test: "'No one meant for that to happen' reads
    # cleaner than 'The villagers never meant for that to happen.'"
    ("The village never meant for that to happen. It never said *go.*",
     "No one meant for that to happen. Nobody said *go.*"),

    # --- Section 2, the seven-in-twelve-lines run -----------------------------
    ("After the Sage stopped naming things, the village kept playing games.",
     "After the Sage stopped naming things, the villagers kept playing games."),
    ("It stopped knowing which ones it was playing.",
     "They stopped knowing which ones they were playing."),

    ("Nobody could name which game the village had got stuck in",
     "Nobody could name which game the villagers had all got stuck in together"),

    # 158 [VAR — swap-in noun, then pronoun].
    ("The village mistook motion for progress. It treated arguments as evidence of "
     "commitment rather than evidence of stuckness.",
     "Everyone mistook motion for progress. They treated arguments as evidence of "
     "commitment rather than evidence of stuckness."),

    ("Without the Sage, the village plays every game at once and loses track of which one "
     "it occupies.",
     "Without the Sage, the villagers play every game at once and lose track of which one "
     "they occupy."),

    # --- Section 4 and the close ----------------------------------------------
    ("Because the village doesn't always recognize you when you return.",
     "Because the villagers don't always recognize you when you return."),
    # [VAR — pronoun continuation; second instance in the same paragraph.]
    ("The village, seeing from where it stands, may not manage to see what you saw.",
     "They, seeing from where they stand, may not manage to see what you saw."),

    ("The Sage who names it gets called difficult. The Sage who doesn't gets called wise. "
     "The village prefers the second one.",
     "The Sage who names it gets called difficult. The Sage who doesn't gets called wise. "
     "The villagers prefer the second one."),

    # 541 [VAR — pronoun; the move's own title is "Let them not understand", so the
    # antecedent is one clause away.]
    ("The village doesn't have to understand what you saw.",
     "They don't have to understand what you saw."),
    ("because the distortion can't stand the gap between what it sees and what the village "
     "receives",
     "because the distortion can't stand the gap between what it sees and what the "
     "villagers receive"),

    ("The village needs someone who can name which game it's in, and you can be that "
     "person, not from above, from with.",
     "The villagers need someone who can name which game they're in, and you can be that "
     "person, not from above, from with."),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    miss = [(i, a) for i, (a, _b) in enumerate(E, 1) if t.count(a) != 1]
    if miss:
        for i, a in miss:
            print("E%d matched %d times: %r" % (i, t.count(a), a[:78]))
        sys.exit("aborted, nothing written")
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch8.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
