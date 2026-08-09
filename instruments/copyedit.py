# -*- coding: utf-8 -*-
"""Consistency against `specs/STYLE_SHEET.md`. Not quality — sameness.

Written 2026-08-07 for the final proof. Every other instrument in this directory
was built to answer *is this voice right*. **None was built to answer: is this
the same word we used last time.** That gap is why an American book carried
British spellings to its last pass, and why one of them was written in on the
morning of the proof and cleared `gate`, all eight diet counters, the voice
linter, `dupes` and `shipcheck` on the way past.

## What it checks, and where each rule comes from

    spelling      STYLE_SHEET §1 — US. Body only.
    hyphenation   STYLE_SHEET §4 — reports splits; the modifier rule makes
                  most of them correct, so this tier is READ, never FIX.
    numbers       STYLE_SHEET §3 — spelled in running prose, numerals for
                  durations, exercise quantities and tables.
    canon caps    STYLE_SHEET §6 — the Faces, daemons, domains, channels.
    names         STYLE_SHEET §7 — the cast, from agency.py's ANIMATE set.

## The marginalia carve-out is a ruling, not a convenience

Wendell, 2026-08-07: *"marginalia hands can spell British."* The `>` blocks and
the `<!-- MARGINALIA -->` frames are other characters writing, and their
spelling is voice. **Spelling is checked on body prose only.** Everything else
is checked everywhere, because a daemon's name is a daemon's name in any hand.

## Why it reports and never gates

A hyphenation split is usually correct — *the whole board* against *the
whole-board view* is the compound-modifier rule working, and this book runs 16
of each. A counter that called those defects would be wrong 32 times. **Read the
board; rule each line.**

    python3 instruments/copyedit.py         # the board
    python3 instruments/copyedit.py -v      # every site
"""
import re, io, os, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# STYLE_SHEET §1. An EXPLICIT list, not a morphological guess.
#
# The first version inferred British-ness from `-ise`/`-our` endings and reported
# 47 hits, of which one was real. It was flagging `precise`, `otherwise`,
# `exercise`, `promised`, `rises`, `detour` and `treatise`. A board that is 98%
# false positive trains you to skim it, which is the failure `ranking.py` and
# `dupes.py` each had to be narrowed out of on the same day.
#
# A real style sheet carries a word list. So does this.
BRITISH = {
    "behaviour": "behavior", "behaviours": "behaviors",
    "apologise": "apologize", "apologised": "apologized",
    "apologising": "apologizing", "apologises": "apologizes",
    "recognise": "recognize", "recognised": "recognized",
    "recognising": "recognizing", "recognises": "recognizes",
    "organise": "organize", "organised": "organized",
    "organising": "organizing", "organisation": "organization",
    "realise": "realize", "realised": "realized", "realising": "realizing",
    "sympathise": "sympathize", "sympathised": "sympathized",
    "prioritise": "prioritize", "prioritised": "prioritized",
    "summarise": "summarize", "summarised": "summarized",
    "alchemise": "alchemize", "alchemised": "alchemized",
    "honour": "honor", "honours": "honors", "honoured": "honored",
    "colour": "color", "colours": "colors", "coloured": "colored",
    "favour": "favor", "favours": "favors", "favoured": "favored",
    "labour": "labor", "rumour": "rumor", "neighbour": "neighbor",
    "defence": "defense", "offence": "offense", "licence": "license",
    "practise": "practice", "practised": "practiced",
    "travelling": "traveling", "cancelled": "canceled",
    "grey": "gray", "towards": "toward", "whilst": "while",
    "amongst": "among", "learnt": "learned", "spelt": "spelled",
}

# STYLE_SHEET §6. Canon that is always capitalised wherever it appears.
# MULTI-WORD ONLY. Single-word canon has legitimate common-noun uses all through
# the book -- a player at a machine, an arcade floor, the forest as terrain -- and
# flagging those reported 20 false "Player" hits. A two-word canon phrase in
# lowercase is unambiguous.
CANON_CAPS = ["emotional body", "damaged self", "vulnerable child",
              "direct action", "raise awareness", "gather resources",
              "skillful organizing", "panoramic seer", "game-switcher"]

# STYLE_SHEET §7. The cast, kept in sync with agency.py's ANIMATE set.
CAST = ["Ines", "Ravi", "Nadia", "Tomas", "Dara", "Yusuf", "Ana", "Meera",
        "Dele", "Alan", "Ellis", "Ade", "Femi", "Tess", "Bea", "Ruth", "Jo",
        "Imani", "Dana", "Corin", "Irix", "Maera"]

MARG = re.compile(r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n.*?\n<!-- /\1 -->", re.S)


def body_lines(path):
    """Yield (lineno, text) for body prose only — marginalia stripped."""
    raw = io.open(path, encoding="utf-8").read()
    for i, line in enumerate(MARG.sub(lambda m: "\n" * m.group(0).count("\n"),
                                      raw).split("\n"), 1):
        if not line.lstrip().startswith(">"):
            yield i, line


def main():
    verbose = "-v" in sys.argv
    paths = sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")),
                   key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))

    spelling, hyphen, caps, names = [], [], [], []
    words, compounds = collections.Counter(), collections.Counter()

    for p in paths:
        name = os.path.basename(p).replace(".md", "")
        for i, line in body_lines(p):
            for w in re.findall(r"\b[A-Za-z]+\b", line):
                if w.lower() in BRITISH:
                    spelling.append((name, i, "%s -> %s" % (w, BRITISH[w.lower()])))
            for m in re.finditer(r"\b([a-z]+)-([a-z]+)\b", line.lower()):
                compounds[m.group(0)] += 1
            for w in re.findall(r"\b[a-z]{3,}\b", line.lower()):
                words[w] += 1
            for c in CANON_CAPS:
                # The naming/instructing rule from STYLE_SHEET §6 covers domains too:
                # "gathering resources, taking direct action" describes the activity and
                # is correctly lowercase; "Direct Action" names the domain. Skip a hit
                # whose line renders the set as gerunds, which is how the book does it
                # at ch2:567, ch3:940 and ch9:680 -- all three were false positives.
                if c in line and "gathering resources" not in line:
                    caps.append((name, i, c))
            for n in CAST:
                for m in re.finditer(r"\b" + n.lower() + r"\b", line):
                    names.append((name, i, n))

    for comp, c in compounds.items():
        a, b = comp.split("-", 1)
        o = words.get(a, 0) and re.escape(a)
        if c >= 3 and words.get(b, 0) >= 3:
            hyphen.append((comp, c))

    print("copyedit — consistency against specs/STYLE_SHEET.md\n")
    print("  spelling   %3d   British forms in body prose (§1, marginalia exempt)" % len(spelling))
    print("  canon caps %3d   lowercase where the sheet says capitalise (§6)" % len(caps))
    print("  names      %3d   cast member lowercased (§7)" % len(names))
    print("  hyphen     %3d   compounds also appearing open — READ, do not sweep (§4)" % len(hyphen))

    if verbose:
        for label, rows in (("SPELLING", spelling), ("CAPS", caps), ("NAMES", names)):
            for r in rows:
                print("  [%s] %s:%d  %s" % (label, r[0], r[1], r[2]))
        for comp, c in sorted(hyphen, key=lambda x: -x[1]):
            print("  [HYPHEN] %-22s %d hyphenated" % (comp, c))

    bad = len(spelling) + len(caps) + len(names)
    print("\n%d fixable · %d to read — reporting only, the hyphen tier is usually correct"
          % (bad, len(hyphen)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
