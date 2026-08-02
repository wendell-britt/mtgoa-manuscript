# -*- coding: utf-8 -*-
"""
ch9_village.py — R8 across chapter 9's village set.

R8 is the population reading: `the village` (Grade 6 pattern, which licenses
only residue verbs) becomes `the villagers` (Grade 1 persons, which licenses
everything). It is not a suffix pass. A village cannot teach, forget, need or
resist; a population of real people can do all four, and the pattern is what
their doing leaves behind.

R8_TEST_CH9.md censused 27 village-subject-plus-verb constructions here, which
is five more than any prior ledger listed. This converts 21, leaves 3 to
Wendell, and leaves 3 alone on grounds the census itself establishes.

------------------------------------------------------------------ the refrain

Lines 43, 49 and 51 open the Distortion fable as a three-beat refrain: the
village taught, the village heard and thought, the village forgot. The census
recommended dropping the definite article at 43 -- `Villagers taught` rather
than `The villagers taught` -- because the article makes the plural read as one
bloc delivering one bloc-teaching, which is the same hive-mind the op exists to
remove, just in cheaper grammatical clothes. The bare plural reads distributive:
some villagers, over time, each teaching a version of the same drift. Which is
what the section says three paragraphs later -- "It crept in slowly."

That reasoning applies to all three beats, not only the one the census tested,
and a refrain half in bare plural and half in definite plural is not a refrain.
All three drop the article. Everywhere else in the chapter `the villagers`
keeps its article, because nowhere else is the collective being credited with a
single unanimous act of mind.

------------------------------------------------------- what R8 does not touch

Line 25's "further out than the village extended" stays exactly as written. The
census filed it as R8's one outright break, and it is -- "the villagers
extended" claims the people themselves stretched out, which is nonsense -- but
the reason it breaks is that `extended` predicates a settlement's territorial
reach rather than an action its residents took. It is village-as-place. So it
was never an agency finding, and it needs no op at all, only to be left alone.
Place-sense and people-sense sit together fine in one sentence: the villagers
taught them everything, and the village only reached so far.

The possessive uses -- "your specific village" at 61, 83, 139, 149 -- are the
reader's own community, not the fable's, and stay singular. Locatives (242,
286, and 442's "meet the village") take no verb and are outside the op.

-------------------------------------------------------------- multi-reference

The census's sharpest warning: R8 cannot be applied clause-by-clause when
several village-references share a sentence, or the sentence ends up internally
inconsistent -- singular village as what the Player is not above, plural
villagers as who follows the path. Three sentences here carry more than one
reference and are converted whole: 320, 442 and 614.

Two of them had a pre-existing number-agreement fault that R8 fixes on the way
past. Line 442 already read "the village wasn't ready for it, that what you
built as liberation THEY experienced as threat", and line 616 already read "gives
the village permission ... to design THEIR own practice". Both were reaching for
the population reading before the op existed.

-------------------------------------------------------------- held for Wendell

Three sites, all in the last two screens, all flagged by the census as
keep-candidates it explicitly declined to rule:

  610  "### *What the Player Gives the Village*"   section heading
  672  "## The Village Is Already Playing"          section heading
  690  "Now go build yours: the village is waiting." the book's last sentence

These trade on `the Village` as a singular mythic counterpart to `the Player`.
The chapter is titled THE PLAYER and the book's central pairing throughout is
one personified role against one personified collective. The plural is not
wrong at any of the three -- it is arguably truer -- but it is a different last
beat, not a cleaner version of the same one, and VOICE_ANCHOR.md is explicit
that the closing move is the register. Section headings and the book's last
sentence are both already on Wendell's board.

Converting 610 leaves its own heading singular over a body that is now plural.
That inconsistency is real and is the cost of holding, recorded here rather
than resolved.

    python3 instruments/ch9_village.py --dry
    python3 instruments/ch9_village.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
CH9 = "manuscript/ch9.md"

EDITS = [
    # ---- Section 1: The Exile -----------------------------------------------
    (CH9, "The village had made no mistake",
          "The villagers had made no mistake"),
    (CH9, "they had learned everything the village could teach them",
          "they had learned everything the villagers could teach them"),
    # 29 — bare plural here too, and for the same reason as the refrain: a single
    # verbatim line attributed to `the villagers` reads as a chorus delivering a
    # rehearsed question. Without the article it reads as the same question
    # rising separately from many people over months, which is what happened.
    (CH9, "When the village asked *what now?*",
          "When villagers asked *what now?*"),
    (CH9, "a critique of what the village kept getting wrong",
          "a critique of what the villagers kept getting wrong"),
    (CH9, "The village was glad to see it. The village needed someone to go first.",
          "The villagers were glad to see it. The villagers needed someone to go first."),

    # ---- Section 2: The Distortion — the three-beat refrain ------------------
    (CH9, "The village taught that the six Faces named a destination.",
          "Villagers taught that the six Faces named a destination."),
    (CH9, "The village heard the six Faces and thought:",
          "Villagers heard the six Faces and thought:"),
    (CH9, "The village forgot that the Faces were a map, not a menu.",
          "Villagers forgot that the Faces were a map, not a menu."),
    (CH9, "playing any game the village needs played",
          "playing any game the villagers need played"),

    # ---- body ----------------------------------------------------------------
    (CH9, "The village needed the six Faces as a teaching instrument",
          "The villagers needed the six Faces as a teaching instrument"),
    (CH9, "returning with something the village actually needs.",
          "returning with something the villagers actually need."),
    (CH9, "the village says *we don't want this.*",
          "the villagers say *we don't want this.*"),
    (CH9, "You now know that the village needs you.",
          "You now know that the villagers need you."),
    (CH9, "The village needs actual allies more than it needs performed ones.",
          "The villagers need actual allies more than they need performed ones."),
    (CH9, "when the village doesn't receive what you built",
          "when the villagers don't receive what you built"),

    # 442 — two references, plus the they/village agreement fault R8 resolves.
    (CH9, "find that the village wasn't ready for it, that what you built as liberation they experienced as threat",
          "find that the villagers weren't ready for it, that what you built as liberation they experienced as threat"),
    (CH9, "The village often resists the new game until it doesn't",
          "The villagers often resist the new game until they don't"),

    (CH9, "The village doesn't need your perfection. It needs your willingness to go first",
          "The villagers don't need your perfection. They need your willingness to go first"),

    # 614 — three references in one sentence. Pronouns carry the second and
    # third rather than repeating the noun twice more.
    (CH9, "The Player shows the village what it looks like to walk all six Faces and come out "
          "the other side, not above the village, not separate from it, but further along a "
          "path the village can follow.",
          "The Player shows the villagers what it looks like to walk all six Faces and come out "
          "the other side, not above them, not separate from them, but further along a "
          "path they can follow."),
    (CH9, "The Player gives the village permission.",
          "The Player gives the villagers permission."),
    (CH9, "to play any game the village needs played",
          "to play any game the villagers need played"),
]


def main():
    dry = "--dry" in sys.argv
    full = os.path.join(ROOT, CH9)
    text = io.open(full, encoding="utf-8").read()

    for _p, before, _a in EDITS:
        n = text.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (n, before[:96]))

    for _p, before, after in EDITS:
        text = text.replace(before, after, 1)
        print("  --  %s" % before[:104])
        print("  ++  %s" % after[:104])

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %s, %d edits." % (CH9, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
