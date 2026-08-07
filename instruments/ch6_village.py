# -*- coding: utf-8 -*-
"""
ch6_village.py — R8 across chapter 6, the fable nobody censused.

Every other fable chapter got an R8 stress test before conversion: ch3, ch4,
ch5, ch7's glossary, ch8, ch9. There is no R8_TEST_CH6.md and there never was.
ch6 carried 37 village instances, 30 of them subjects -- more than ch4 -- and
was the last chapter still at zero villagers.

Converted without a fresh census because five chapters of censuses already
taught what to check for, and ch6 was read against all of it:

  COEXTENSIVE POPULATION (ch3's break): a village acting on a set that is
  itself. None here. The village always acts on the Architect, on systems, or
  on itself reflexively, never on "everyone".

  POSSESSION / SELF-REFERENCE (ch4's break): "it taught its people". None here.

  REFLEXIVES (ch3's subtler break): three -- "defend itself", "thought itself
  holistic", "thought itself practical". All three survive pluralisation, and
  none carries ch3:152's systemic-blindness claim, which was the thing that
  actually broke there. Many people each defending, each thinking themselves
  holistic, is the true reading and the plural states it.

  SCOPE-MISS (ch4's third shape): collective nouns that are not populations.
  None -- ch6 has no councils, rituals or workshops.

  AGREEMENT (the cost every census understated): line 124 is the present-tense
  formula, so does->do, transforms->transform, has->have. Line 169 needs
  reduces->reduce.

--------------------------------------------------------------------- the refrain

  The village never meant for that to happen. It never said go. It just
  stopped listening.

This sentence is a four-chapter refrain, and it was in three states at once:
converted in ch4 and ch5, held as a keep-candidate in ch3, untouched in ch6.
The keep argument was real -- the singular describes emergent, no-one-decided
drift, and the plural nudges a structural non-decision toward something more
individually exculpatory -- but two chapters had already answered it by
accident, and a refrain that says village twice and villagers twice reads as an
unfinished pass rather than a deliberate distinction.

Wendell 2026-08-03: convert the refrain. So ch3:123 moves here too, and all
four chapters now carry the plural.

------------------------------------------------------------------ anaphora

Line 116 runs four parallel "The village built X" clauses, which is the
paragraph's rhetorical engine. Repeating the full noun five times is heavier
than the original was, so the first stays a noun and the rest go to pronouns.
Anaphora on "They built" is still anaphora, and the device survives at the
original weight.

Held per DL-38: the headings at 62, 110 and 349. Left as found: the locative at
64, "the Architect lived in the village".

    python3 instruments/ch6_village.py --dry
    python3 instruments/ch6_village.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    # ---- ch3: the refrain, released from its hold -------------------------
    ("manuscript/ch3.md",
     "The village never meant for that to happen. It never said \"go.\" It just stopped listening.",
     "The villagers never meant for that to happen. They never said \"go.\" They just stopped listening."),

    # ---- ch6 Section 1: the exile ------------------------------------------
    ("manuscript/ch6.md",
     "The village listened, at first, because the maps worked.",
     "The villagers listened, at first, because the maps worked."),

    ("manuscript/ch6.md",
     "The village started to defend itself against the Architect's maps.",
     "The villagers started to defend themselves against the Architect's maps."),

    ("manuscript/ch6.md",
     "The village did not want to be shown. The village wanted to be heard.",
     "The villagers did not want to be shown. They wanted to be heard."),

    ("manuscript/ch6.md",
     "The village needed something the Architect didn't know how to give: presence.",
     "The villagers needed something the Architect didn't know how to give: presence."),

    ("manuscript/ch6.md",
     "the village had stopped asking for maps. The village had started working around the Architect",
     "the villagers had stopped asking for maps. They had started working around the Architect"),
    ("manuscript/ch6.md",
     "The village used the Architect for outputs and kept the Architect out of decisions.",
     "They used the Architect for outputs and kept the Architect out of decisions."),

    ("manuscript/ch6.md",
     "The village never meant for that to happen. It never said *go.* It just stopped listening to the design.",
     "The villagers never meant for that to happen. They never said *go.* They just stopped listening to the design."),

    # ---- ch6 Section 2: the distortion -------------------------------------
    ("manuscript/ch6.md",
     "After the Architect left, the village didn't stop needing systems.",
     "After the Architect left, the villagers didn't stop needing systems."),

    # the four-beat anaphora: noun once, then pronouns, so the device keeps its
    # original weight instead of gaining a syllable per beat
    ("manuscript/ch6.md",
     "The village still built things.",
     "The villagers still built things."),
    ("manuscript/ch6.md",
     "the village built systems that looked correct and failed anyway. The village built planning "
     "processes that produced plans nobody followed. The village built accountability structures "
     "that nobody trusted. The village built meeting formats that everyone hated attending. The "
     "village built all of this with sincere effort and no structural clarity.",
     "they built systems that looked correct and failed anyway. They built planning "
     "processes that produced plans nobody followed. They built accountability structures "
     "that nobody trusted. They built meeting formats that everyone hated attending. They "
     "built all of this with sincere effort and no structural clarity."),

    ("manuscript/ch6.md",
     "Because the village had exiled the Architect",
     "Because the villagers had exiled the Architect"),
    ("manuscript/ch6.md",
     "inside the systems) the village lost the ability",
     "inside the systems) they lost the ability"),

    ("manuscript/ch6.md",
     "The village started mistaking motion for progress.",
     "The villagers started mistaking motion for progress."),
    ("manuscript/ch6.md",
     "The village became very busy, very purposeful, very committed,",
     "They became very busy, very purposeful, very committed,"),

    ("manuscript/ch6.md",
     "The village also started doing something more damaging: it started using the Architect's own tools",
     "The villagers also started doing something more damaging: they started using the Architect's own tools"),
    ("manuscript/ch6.md",
     "The village learned to *describe* systems without *understanding* them.",
     "They learned to *describe* systems without *understanding* them."),
    ("manuscript/ch6.md",
     "The village learned to have the vocabulary of structural thinking without the practice.",
     "They learned to have the vocabulary of structural thinking without the practice."),
    ("manuscript/ch6.md",
     "The village could then dismiss structural insight with the vocabulary itself:",
     "They could then dismiss structural insight with the vocabulary itself:"),

    # present tense: three agreement changes in one sentence
    ("manuscript/ch6.md",
     "The village does one thing with structural design once the Architect leaves: it transforms it into",
     "The villagers do one thing with structural design once the Architect leaves: they transform it into"),
    ("manuscript/ch6.md",
     "because now the village has enough sophistication to dismiss genuine structural insight while "
     "believing it has already accounted for it.",
     "because now they have enough sophistication to dismiss genuine structural insight while "
     "believing they have already accounted for it."),

    ("manuscript/ch6.md",
     "The village did all of this without realizing it. It thought itself holistic. It thought itself "
     "comprehensive. What it actually did:",
     "The villagers did all of this without realizing it. They thought themselves holistic. They thought "
     "themselves comprehensive. What they actually did:"),

    ("manuscript/ch6.md",
     "the village learned to fear its own clarity.",
     "the villagers learned to fear their own clarity."),

    ("manuscript/ch6.md",
     "The village didn't realize any of this. It thought itself practical. What it actually did: starve "
     "itself of the one thing it needed most:",
     "The villagers didn't realize any of this. They thought themselves practical. What they actually did: "
     "starve themselves of the one thing they needed most:"),

    ("manuscript/ch6.md",
     "The village reduces structural design to its outputs:",
     "The villagers reduce structural design to its outputs:"),

    # ---- ch6 later sections ------------------------------------------------
    ("manuscript/ch6.md",
     "The village did not exile the Architect for being wrong. It exiled the Architect for arriving",
     "The villagers did not exile the Architect for being wrong. They exiled the Architect for arriving"),

    ("manuscript/ch6.md",
     "you are the Architect the village exiled:",
     "you are the Architect the villagers exiled:"),
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
        print("  --  %s" % before[:96])
        print("  ++  %s" % after[:96])

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
