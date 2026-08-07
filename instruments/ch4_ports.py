# -*- coding: utf-8 -*-
"""
ch4_ports.py — three fixes carried over from the parallel ch4 village pass.

Two sessions ran the village work at once. This branch and
claude/chapter-2-agency-abstraction-d8peid both did ch4, independently, from a
common base at the ch9 village commit. d8peid's version is the better one and
is now this branch's base. Three sites did not survive the merge in the better
state, and this ports them across.

d8peid wins on everything else in ch4, and two of those wins are worth naming so
nobody re-litigates them later:

  Pronouns. Where this branch wrote "Not because the villagers didn't feel them
  (the villagers felt every one of them) but because the villagers had lost the
  Challenger's gift", d8peid wrote "Not because they didn't feel them (they felt
  every one of them) but because they had lost". Three repetitions against one
  noun and two pronouns. Same at 125 and 167. R8 mechanically repeats the noun;
  a reader does not.

  ch4:115, the VOICE_ANCHOR site this branch held for Wendell. He ruled it
  (candidate A), and d8peid caught a trap this branch had not seen: ch4:115 sits
  in Section 2, ABOVE Corin Ash's signature, so per SPEC_TWO_HANDS it is
  treatise prose. "I have run those workshops" there is Ash claiming Wendell's
  biography, which is the DL-19 author collision. The shipped line uses Ash's
  own recorded credential instead -- "I believed those scripts for thirty
  years" -- which HEAD_FACTS already establishes, since Ash's whole authority
  rests on having been taken in rather than on having taught.

--------------------------------------------------------------------- the ports

1. ch4 — "The village still experienced violations."

   Missed by d8peid's pass. Every other clause in that paragraph converted, so
   this one sentence was left carrying the singular alone.

2. ch4:127 — the thesis sentence, and the census's flagship break.

   d8peid has "they taught each other that the clean no no longer belonged to
   them". That is still the population acting on itself, which is the exact
   coextensive-set break R8_TEST_CH4.md flagged: villagers cannot teach
   villagers-in-general as though the two were separate groups. "Each other"
   softens it but does not dissolve it.

   The census's own R6 does dissolve it, by making the relation temporal rather
   than reflexive: one generation to the next. It also lands at the same
   syllable count as the original, with the turn intact. Worth remembering that
   this break is metrically silent -- 16 syllables before and after, since
   it/they and its/their are all monosyllabic -- so it reads as clean aloud as
   it is broken on the page, and neither pass would have caught it by ear.

3. ch3 — "the village's solution to the Shaman problem".

   Not a ch4 site, but the last outstanding village possessive in ch3 and the
   only piece of this branch's ch3 remainder commit that d8peid lacks. Both
   censuses excluded it by design, since they counted subject+verb constructions
   and this is a bare possessive with no verb. Strictly not a registry
   violation, the grades governing verbs. But devising a solution is a mental
   act, and it was the last clause in that chapter still crediting the village
   rather than the population.

    python3 instruments/ch4_ports.py --dry
    python3 instruments/ch4_ports.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ("manuscript/ch4.md",
     "The village still experienced violations.",
     "The villagers still experienced violations."),

    ("manuscript/ch4.md",
     "over the clean no, they taught each other that the clean no no longer belonged to them.",
     "over the clean no, one generation taught the next that the clean no was not theirs."),

    ("manuscript/ch3.md",
     "The second is the village's solution to the Shaman problem:",
     "The second is the villagers' solution to the Shaman problem:"),
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
                     % (path, n, before[:88]))

    for path, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s" % path)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
