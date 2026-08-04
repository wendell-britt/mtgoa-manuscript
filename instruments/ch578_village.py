# -*- coding: utf-8 -*-
"""
ch578_village.py — the village stragglers in ch5, ch7 and ch8.

These three chapters were converted in an earlier pass (47 sites across ch5,
ch7, ch8 and the glossary) and these fifteen were left behind. Most of them were
invisible rather than skipped: the recall net reported 3 for the whole block
because the perception class had no `think` and no `believe`, and because
`think` -- once added -- still could not produce `thought`, which is the form
ch5:165 uses three times in a row.

Both gaps are now closed in the registry and the inflector. The net reports 6
where it reported 3; the rest of these carry verbs that are in no class at all
(`live with`, `keep`, `pause`, `treat`, and the copulas) and are converted here
for consistency inside their own paragraphs rather than because a counter found
them. A paragraph that says villagers three times and village twice reads as an
unfinished pass whatever the taxonomy thinks.

------------------------------------------------------------------- the anaphora

ch5:165 runs the same shape as ch6:116 did: a belief, then three parallel "The
village thought" clauses. Same treatment -- the noun carries the first beat and
pronouns carry the rest, so the device keeps its original weight instead of
gaining a syllable per beat.

  the village truly believed it was doing the right thing
  -> the villagers truly believed they were doing the right thing

Note `it was` -> `they were`: the belief's own complement had to move too, which
is the kind of downstream agreement these passes keep finding one clause late.

------------------------------------------------------------------ pre-existing

ch8:87 already read "the village didn't know what to do with that. It didn't
match the story THEY'D heard." Singular subject, plural pronoun, two clauses
apart. R8 removes an inconsistency here rather than introducing one -- the same
thing it did at ch4:167 and ch5:155.

    python3 instruments/ch578_village.py --dry
    python3 instruments/ch578_village.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    # ---- ch5 ---------------------------------------------------------------
    ("manuscript/ch5.md",
     "stopped violations the village had lived with for as long.",
     "stopped violations the villagers had lived with for as long."),

    ("manuscript/ch5.md",
     "Walls to hold what the village had agreed to.",
     "Walls to hold what the villagers had agreed to."),

    # The next three sentences of this paragraph already name people -- "the
    # people they were meant to serve", "the humans who filled them" -- so the
    # singular was the odd one out in its own paragraph.
    ("manuscript/ch5.md",
     "confuse *what the village had built* with *what the village actually was.*",
     "confuse *what the villagers had built* with *what the villagers actually were.*"),

    ("manuscript/ch5.md",
     "After the Regent left, the village didn't stop building.",
     "After the Regent left, the villagers didn't stop building."),

    # the belief, then the three-beat anaphora
    ("manuscript/ch5.md",
     "the village truly believed it was doing the right thing. The village thought loyalty "
     "was the same thing as obedience. The village thought tradition was the same thing as "
     "wisdom. The village thought: *if we just hold the line long enough, the meaning will "
     "come back.*",
     "the villagers truly believed they were doing the right thing. They thought loyalty "
     "was the same thing as obedience. They thought tradition was the same thing as "
     "wisdom. They thought: *if we just hold the line long enough, the meaning will "
     "come back.*"),

    ("manuscript/ch5.md",
     "The village keeps tradition instead of passing it on:",
     "The villagers keep tradition instead of passing it on:"),

    ("manuscript/ch5.md",
     "The village was wrong. The Architect's love is structural.",
     "The villagers were wrong. The Architect's love is structural."),

    # ---- ch7 ---------------------------------------------------------------
    # The vignette already has people in it -- "a woman in the village", "a man
    # operates differently" -- so the collective was the only abstraction left.
    ("manuscript/ch7.md",
     "In the weeks that followed, the village noticed something.",
     "In the weeks that followed, the villagers noticed something."),
    ("manuscript/ch7.md",
     "The village started treating his presence as something that could be lost.",
     "They started treating his presence as something that could be lost."),

    # ---- ch8 ---------------------------------------------------------------
    ("manuscript/ch8.md",
     "The village would pause.",
     "The villagers would pause."),

    ("manuscript/ch8.md",
     "the village didn't know what to do with that.",
     "the villagers didn't know what to do with that."),

    ("manuscript/ch8.md",
     "The village kept the Sage's vocabulary and dropped the practice. It learned to say",
     "The villagers kept the Sage's vocabulary and dropped the practice. They learned to say"),
    ("manuscript/ch8.md",
     "It learned to name the games other people were playing without noticing it was also "
     "playing one. It learned to *describe* perspective without *practicing* it.",
     "They learned to name the games other people were playing without noticing they were also "
     "playing one. They learned to *describe* perspective without *practicing* it."),
]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, n, before[:92]))

    for path, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("  --  %s" % before[:98])
        print("  ++  %s" % after[:98])

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
