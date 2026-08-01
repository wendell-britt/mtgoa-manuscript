# -*- coding: utf-8 -*-
"""
pass2_apply.py — the Continuity and Claims findings, applied.

Wendell 2026-08-01, on `editorial_reports/2026-08-01/PASS2_CONTINUITY_AND_CLAIMS.md`:
"let's make the changes for these." CA-1 through CA-6.

CA-1 is not a new decision. Wendell ruled the altitude colours CUT on 2026-07-31 and the
ledger recorded it as ruled; the audit found the scale still on the page at six sites.
His ruling also set the replacement: *the six Faces are the taught answer-set.* Where a
colour was carrying meaning rather than decorating a sentence, the replacement uses a
set the chapter actually teaches — the four games at `ch8:260`, or the whole-board view.

CA-2 renames the Diplomat's five from *channels* to *modes*, which is what every other
Face chapter calls its five. **The EA channels keep the word**: Metal, Water, Wood, Fire
and Earth are *the five channels* on the copyright page, in Chapter 3 and in Appendix C,
and ch7's own uses of them — the Fire channel, the destination channel, the length of
one channel from the fear end of Metal — are left exactly as they are. Fourteen renames,
each one checked for which set it names.

Anchors are exact, every file is written once at the end, and a missed or duplicated
anchor aborts the run with nothing written.

    python3 instruments/pass2_apply.py --check
    python3 instruments/pass2_apply.py

Run `gate.py`, `termdebt.py`, `citation_audit.py` and `build_book.py` after.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# (flag, relative path, anchor, replacement)
EDITS = [
    # ================================================== CA-1 · the ruled cut, applied
    ("CA-1a", "manuscript/ch8.md",
     "the capacity to take in all the altitudes (Red, Amber, Orange, Green, Teal) and still choose to stand somewhere",
     "the capacity to take in all the altitudes and still choose to stand somewhere"),
    ("CA-1b", "manuscript/ch8.md",
     "*Which altitude is this?* is a vertical question. Red, Amber, Orange, Green, Teal. It asks what a person can currently hold",
     "*Which altitude is this?* is a vertical question, and its answer-set is the six Faces "
     "you have spent this book learning. It asks what a person can currently hold"),
    ("CA-1c", "manuscript/ch8.md",
     "The Teal view doesn't mean you've stopped being Red. It means you know when you're Red, "
     "you can choose to stay there deliberately, and you can come back.",
     "The widest view doesn't mean you have stopped being able to stand in a narrow one. It "
     "means you know when you are standing there, you can choose to stay deliberately, and "
     "you can come back."),
    ("CA-1d", "manuscript/ch8.md",
     "The *I am at Teal and you are at Green and this conversation is beneath my time* that fires",
     "The *I can see the whole board and you are playing one square of it and this "
     "conversation is beneath my time* that fires"),
    ("CA-1e", "manuscript/ch8.md",
     "*This is a Red dynamic. This is Green stuckness. This is an Orange problem wearing Teal vocabulary.*",
     "*This is a power game. This is harmony stuckness. This is a strategy problem wearing "
     "whole-board vocabulary.*"),
    ("CA-1f", "manuscript/ch8.md",
     "You've seen from Teal (the whole map, where everyone stands",
     "You've seen the whole map (where everyone stands"),

    # CA-1g · one colour survived the six anchors above and was caught by termdebt on the
    # re-run: "Green" at ch8:270, used once and defined nowhere.
    ("CA-1g", "manuscript/ch8.md",
     "You decide the group sits at Green, so you treat every conflict as a Green conflict,",
     "You decide the group sits at one altitude, so you treat every conflict as that kind "
     "of conflict,"),

    # ================================== CA-2 · the Diplomat's five are modes, not channels
    ("CA-2a", "manuscript/ch7.md",
     "The Diplomat operates through five channels:",
     "The Diplomat operates through five modes:"),
    ("CA-2b", "manuscript/ch7.md",
     "**Bridge-Builder.** The channel of initial entry.",
     "**Bridge-Builder.** The mode of initial entry."),
    ("CA-2c", "manuscript/ch7.md",
     "**Translator.** The channel of rendering meaning.",
     "**Translator.** The mode of rendering meaning."),
    ("CA-2d", "manuscript/ch7.md",
     "**Field-Holder.** The channel of maintained safety.",
     "**Field-Holder.** The mode of maintained safety."),
    ("CA-2e", "manuscript/ch7.md",
     "**Repairer.** The channel of healing ruptures.",
     "**Repairer.** The mode of healing ruptures."),
    ("CA-2f", "manuscript/ch7.md",
     "**Integrative Negotiator.** The channel of honest closing.",
     "**Integrative Negotiator.** The mode of honest closing."),
    ("CA-2g", "manuscript/ch7.md",
     "works each mode's full arc through in its five channel deep-dives",
     "works each mode's full arc through in its five deep-dives"),
    ("CA-2h", "manuscript/ch7.md",
     "the Diplomat's entry point: the channel through which contact happens",
     "the Diplomat's entry point: the mode through which contact happens"),
    ("CA-2i", "manuscript/ch7.md",
     "The Translator is the Diplomat's most cognitively demanding channel",
     "The Translator is the Diplomat's most cognitively demanding mode"),
    ("CA-2j", "manuscript/ch7.md",
     "The Translate layer forms the operational core of the channel",
     "The Translate layer forms the operational core of the mode"),
    ("CA-2k", "manuscript/ch7.md",
     "The Field-Holder demands more sheer presence than any other Diplomat channel",
     "The Field-Holder demands more sheer presence than any other Diplomat mode"),
    ("CA-2l", "manuscript/ch7.md",
     "The Repairer is the Diplomat's deepest channel",
     "The Repairer is the Diplomat's deepest mode"),
    ("CA-2m", "manuscript/ch7.md",
     "The Integrative Negotiator is the Diplomat's closing channel",
     "The Integrative Negotiator is the Diplomat's closing mode"),
    # ch6:492 reads "Wake Up is a mode detecting"; ch7 is the only chapter that swapped
    # the word here, which is the collision in one line.
    ("CA-2n", "manuscript/ch7.md",
     "Wake Up is a channel detecting who is in the field",
     "Wake Up is a mode detecting who is in the field"),
    ("CA-2o", "manuscript/ch7.md",
     "- The five channels: Bridge-Builder, Translator, Field-Holder, Repairer, Integrative Negotiator",
     "- The five modes: Bridge-Builder, Translator, Field-Holder, Repairer, Integrative Negotiator"),

    # Three further sites, found by re-reading every surviving "channel" in ch7 after the
    # first run. CA-2q takes "conduit" rather than "mode": the sentence is about the
    # Translator becoming a pipe, and the paragraph already uses the word two lines up.
    ("CA-2p", "manuscript/ch7.md",
     "This channel surfaces what each party protects",
     "This mode surfaces what each party protects"),
    ("CA-2q", "manuscript/ch7.md",
     "The distorted Translator has no position: the perfect channel, and therefore useless",
     "The distorted Translator has no position: the perfect conduit, and therefore useless"),
    ("CA-2r", "manuscript/ch7.md",
     "because the Repairer is one of your five channels and Move 4 is a structure",
     "because the Repairer is one of your five modes and Move 4 is a structure"),

    # ================================================ CA-3 and CA-4 · the chapter titles
    ("CA-4a", "manuscript/ch1.md",
     "# Chapter 1 — The Infinite Arcade",
     "# CHAPTER 1: THE INFINITE ARCADE"),
    ("CA-4b", "manuscript/ch7.md",
     "# CHAPTER 7 — THE DIPLOMAT",
     "# CHAPTER 7: THE DIPLOMAT"),
    ("CA-3", "manuscript/ch9.md",
     "# CHAPTER 9: CREATING YOUR OWN ALLYSHIP GAME",
     "# CHAPTER 9: THE PLAYER"),

    # ============================================================= CA-5 · the Gendlin credit
    ("CA-5", "front_matter/copyright.md",
     "The five emotional channels are a remix of **wu xing**",
     "*Felt sense*, used in Chapters 1, 3, 5, 8 and 9 and in Appendix A, is **Eugene\n"
     "Gendlin's**, from *Focusing*.\n\n"
     "The five emotional channels are a remix of **wu xing**"),

    # ==================================================== CA-6 · eight gates, seven daemons
    ("CA-6", "manuscript/ch9.md",
     "a gate scan. Eight gates, eight questions.",
     "a gate scan. Seven daemons and the child at the center: eight gates, eight questions."),
]


def main():
    check = "--check" in sys.argv
    files, problems = {}, []
    for flag, rel, anchor, _ in EDITS:
        if rel not in files:
            files[rel] = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()
        n = files[rel].count(anchor)
        if n != 1:
            problems.append("%s %s: anchor found %d times: %r" % (flag, rel, n, anchor[:64]))
    if problems:
        print("ABORT — nothing written")
        for p in problems:
            print("  " + p)
        return 1

    for flag, rel, anchor, new in EDITS:
        files[rel] = files[rel].replace(anchor, new, 1)

    for flag, rel, anchor, new in EDITS:
        print("%-6s %-26s %s" % (flag, os.path.basename(rel), anchor[:58]))
        print("%-6s %-26s -> %s" % ("", "", new.replace("\n", " ")[:58]))
    if check:
        print("\n--check: %d anchors verified, nothing written" % len(EDITS))
        return 0
    for rel, text in files.items():
        io.open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(text)
    print("\n%d edits applied across %d files" % (len(EDITS), len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
