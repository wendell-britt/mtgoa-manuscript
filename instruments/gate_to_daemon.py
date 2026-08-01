# -*- coding: utf-8 -*-
"""
Retire *gate* as a name for a daemon. Ruled by Wendell 2026-08-01.

**The measurement that settles it.** Across the nine chapters, *daemon* appears 45 times
in eight of them and *gate* appears three times, all in ch9. ch2 -- which teaches the
roster and which `MANUSCRIPT_FILE_CANON.md:109` says "keeps theirs" -- uses *daemon* 26
times and *gate* zero. The vocabulary migrated across the whole manuscript and never
reached ch9 or the appendices, which is why the reader meets the word last, in the
closing exercise, attached to nothing she was taught.

Canon line 109 is stale prose describing a state that no longer exists on the page. It is
corrected here rather than left to contradict the book.

**33 of the 37 shipping occurrences are straight substitutions.** Appendix B labels every
quest *Gate: Emotional Body* and every campaign *Gates: Protector + Controller*, and
those rows are daemons by name. Appendix A's affinity table is keyed on daemons through
all eight rows. `ON_THE_SHOULDERS_OF` is the daemon-lineage section, headed *The Shadow
Work and the Gates*, crediting Genpo Roshi and Carolyn Elliott for the work the rest of
the book calls daemons.

**Four are not substitutions, and they are the analysis.**

    ch9:288   "Fear, anger, sadness, joy, neutrality: each one a gate you can walk
              through" -- the five channels, not daemons. Swapping in *daemon* would
              install a new error where an old one was removed. Becomes *a door*.

    ON_THE_SHOULDERS_OF:62  "once you're at a gate" -- you arrive at a gate; you do not
              arrive at a daemon. Becomes "once you're with a daemon".

    APPENDIX_E:92  "walk the gates" -- the retired gate-walk exercise as a verb phrase,
              not a noun. Becomes "meet the daemons", which is ch2:556's own construction:
              "The Forest is where those daemons are met and befriended."

    ch9:296   "where the gates stand" and "the same gate ... still on duty" read as
              terrain, but *on duty* is a guard, which is what a daemon is. These take
              the substitution cleanly and are listed here only because they looked like
              metaphor at first pass.

The hand-set replacements run before the sweep so the sweep cannot reach them.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# Run first: sites where a blind noun swap produces the wrong sentence.
EXACT = [
    ("manuscript/ch9.md",
     "each one a gate you can walk through instead of a threat to manage.",
     "each one a door you can walk through instead of a threat to manage."),

    ("appendices/ON_THE_SHOULDERS_OF.md",
     "The approach you take once you're at a gate comes from",
     "The approach you take once you're with a daemon comes from"),

    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
     "find the shadow, alchemize the charge, walk the gates, show up in the field.",
     "find the shadow, alchemize the charge, meet the daemons, show up in the field."),

    ("specs/MANUSCRIPT_FILE_CANON.md",
     "The gate walk is removed from Chapters 4 through 8. Chapters 2 and 9 keep theirs.",
     "The daemon walk is removed from Chapters 4 through 8. Chapters 2 and 9 keep "
     "theirs. The word is **daemon** on every surface: *gate* was retired 2026-08-01, "
     "when it was measured at three occurrences in ch9 against 45 for *daemon* across "
     "eight chapters."),
]

# Then the sweep, over the files that carry the remaining 33.
SWEEP = [
    "manuscript/ch9.md",
    "appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md",
    "appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
    "appendices/ON_THE_SHOULDERS_OF.md",
    "appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
]
SUB = [(re.compile(r"\bGates\b"), "Daemons"), (re.compile(r"\bGate\b"), "Daemon"),
       (re.compile(r"\bgates\b"), "daemons"), (re.compile(r"\bgate\b"), "daemon")]


def main():
    dry = "--dry" in sys.argv
    files, bad, swept = {}, [], 0

    for path, old, new in EXACT:
        files.setdefault(path, io.open(os.path.join(ROOT, path), encoding="utf-8").read())
        n = files[path].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (path, n, old[:56]))
            continue
        files[path] = files[path].replace(old, new, 1)

    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1

    for path in SWEEP:
        files.setdefault(path, io.open(os.path.join(ROOT, path), encoding="utf-8").read())
        for pat, rep in SUB:
            files[path], k = pat.subn(rep, files[path])
            swept += k

    if not dry:
        for path, t in files.items():
            io.open(os.path.join(ROOT, path), "w", encoding="utf-8").write(t)
    print("%d hand-set + %d swept %s"
          % (len(EXACT), swept, "checked" if dry else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
