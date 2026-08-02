# -*- coding: utf-8 -*-
"""
agency_batch1.py — the five ruling-independent fixes from the agency audit.

Wendell authorised these on 2026-08-02, with before/after shown in the console.
Every one depends on no open ruling: two are repairs to the ch2 §6 roster (a
canon violation the agency audit found by accident), one is a B6 breach that is
banned verbatim and forever, one is the duty-of-care disclaimer, and one is the
single highest-value repair the audit found.

House pattern per instruments/spec_edit.py: exact anchors, and the script writes
NOTHING if any anchor is missed or matches more than once.

    python3 instruments/agency_batch1.py --dry
    python3 instruments/agency_batch1.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

# (file, before, after, why)
EDITS = [
    ("manuscript/ch1.md",
     "tells you which of these are yours and hands each one back with the page "
     "that takes it apart. It scores how you actually behave, and it will not tell "
     "you which kind of ally you are",
     "marks which of these are yours and hands each one back with the page "
     "that takes it apart. It scores how you actually behave, and it has no score "
     "for which kind of ally you are",
     "B6. A Grade 4 machine taking a perception verb, twice, banned verbatim and "
     "forever. The correct handling was already in the adjacent clause -- 'It "
     "scores how you actually behave' -- so both repairs are R2 mechanize, and the "
     "second is the Token/Ticket move exactly: no score for, rather than will not "
     "tell you."),

    ("manuscript/ch2.md",
     "It trades contact for control and calls the trade safety.",
     "It trades contact for control, and the trade feels like safety.",
     "ch2 section 6 roster: the embodied three act somatically, not verbally. "
     "'Calls' is a naming verb on the Protector, two sections after the chapter "
     "establishes the rule. 'Feels like' is somatic and keeps safety in the last "
     "position, which the anchor's closing-move rule requires."),

    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
     "Protector names the conditions a group needs to function;",
     "Protector guards the conditions a group needs to function;",
     "Same roster violation, same daemon, different surface and different hand. "
     "'Guards' is somatic and sits inside the list's own verb register -- locates, "
     "restores, routes, takes, absorbs, carries."),

    ("front_matter/copyright.md",
     "surface material that wants a trained person in the chair with you.",
     "surface material heavy enough that you want a trained person in the chair with you.",
     "A Grade 0 subject taking the registry's highest-severity intention lemma, "
     "inside the duty-of-care disclaimer. The one site in this audit where the "
     "abstraction standing in for a person costs a reader something real, because "
     "the sentence exists to tell someone in trouble that a person should be "
     "present. The want moves to the reader, who is Grade 1, and the image -- in "
     "the chair with you -- is untouched."),

    ("manuscript/ch7.md",
     "offered as information, once, to a field that is then free to answer.",
     "offered as information, once, to the people who are then free to answer.",
     "The highest-value single repair in the book: ch7's own definition of its own "
     "key term, written so that the field answers. The field is now Grade 6 with "
     "its mechanism traced to ch7:359, which licenses movement and mechanism but "
     "not cognition -- a space contingent on the people in it cannot answer. R6, "
     "relocation to participants. Turn survives, +1 syllable, meaning improves."),
]


def main():
    dry = "--dry" in sys.argv
    loaded, plans = {}, []

    for path, before, after, why in EDITS:
        full = os.path.join(ROOT, path)
        if full not in loaded:
            loaded[full] = io.open(full, encoding="utf-8").read()
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\n"
                     "Nothing written." % (path, n, before[:80]))
        plans.append((full, path, before, after, why))

    for full, path, before, after, why in plans:
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s" % path)
        print("  why : %s" % why)
        print("  --  : %s" % before)
        print("  ++  : %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(plans))
        return 0

    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(plans)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
