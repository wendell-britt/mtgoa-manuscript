# -*- coding: utf-8 -*-
"""
Seat the approved unearned-recall set — drafts/APPROVED_unearned_recall_2026-07-31.md.

Ruled by Wendell 2026-07-31: R1 B · R2 A · R3 A · R4 A, plus the label cut and Fix 2.
A6 was applied separately and is asserted here rather than re-applied.

Every edit is anchored on literal text. An anchor that matches zero times or more than
once aborts the whole run and writes nothing, because a partially seated ruling is worse
than an unseated one — the file would look edited and be wrong in a place nobody checked.

    python3 instruments/seat_approved_recall.py --dry     # report only
    python3 instruments/seat_approved_recall.py           # write
    python3 instruments/seat_approved_recall.py R3        # write one ruling only

Each edit carries the ruling it came from, so the set can be seated one editorial
question at a time -- the git cadence the approved file asks for.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# The recall clause, verbatim, so the three replacements below cannot drift apart.
FUEL = "Chapter 1 taught you to read your own fuel: what a move costs you."
FIELD = "Chapter 3 taught you to ask what a move does to the living field."


def ecology(title, question, body):
    return "### The %s Ecology\n\n%s %s The %s\n\n%s\n\n%s\n" % (
        title, FUEL, FIELD, body[0], question, body[1])


EDITS = [
    # -- 1 - three replacements. R1 fuel, R2 the living-field gloss, and the label cut.
    ("R1R2", "ch3.md",
     "Chapter 1 taught you to read the meter: what a move costs you. The Shaman adds "
     "the next layer: what that spending does to the living field.",
     FUEL + " The Shaman adds the next layer: what that spending does to the living "
     "field — to the people around you, and what it leaves them carrying."),

    ("R1cut", "ch4.md",
     "Chapter 1 taught you to read the meter: what a move costs you. Chapter 3 taught "
     "you to ask what a move does to the living field. The Challenger adds the fire "
     "question:",
     "%s %s The Challenger adds:" % (FUEL, FIELD)),

    ("R1cut", "ch5.md",
     "Chapter 1 taught you to read the meter: what a move costs you. Chapter 3 taught "
     "you to ask what a move does to the living field. The Regent adds the stewardship "
     "question:",
     "%s %s The Regent adds:" % (FUEL, FIELD)),

    # -- 2 - R4, the altar cut. The term is asserted as known and the book never contains it.
    ("R4", "ch9.md",
     "The six Faces are your toolkit. The WAVE is your process. The altar — the "
     "practice of returning — is your anchor.",
     "The six Faces are your toolkit. The WAVE is your process. The practice of "
     "returning is your anchor."),

    ("R4", "ch9.md",
     "You know that the altar is not optional — that coming back makes the work "
     "real. That the return to the village, carrying what you found, is the whole point.",
     "You know that the return is not optional — that coming back makes the work "
     "real. That carrying what you found back to the village is the whole point."),

    # -- 3 - R3, the escalator ladder, now running ch3 -> ch8.
    #
    # ch4 and ch5 seat the Ecology immediately after the Stage Sequence and before the
    # cycle section, separated by a rule. ch6 and ch7 have no Stage Sequence heading, so
    # the draft flagged both placements as judgment calls. Both are resolved to the same
    # rule: the Ecology closes the practice section, immediately before what follows it.
    #
    # ch6 - the draft said "insert AFTER the flow-cycle line." That line is followed by
    # the "In practice:" paragraph that elaborates it and then by the summation, so
    # inserting there would cut a paragraph off its own worked example. It goes after the
    # section closes instead.
    ("R3", "ch6.md",
     "That is the Architect's practice. Logic as a living instrument. Structure as "
     "generosity. The map that makes you unnecessary.\n\n---\n\n"
     "### Name One Unstated Assumption, in the Village",
     "That is the Architect's practice. Logic as a living instrument. Structure as "
     "generosity. The map that makes you unnecessary.\n\n---\n\n"
     + ecology("Design",
               "Did this change the condition, or did it clear the incident?",
               ("Architect adds:",
                "The Architect does not need you to count what you shipped. The Architect "
                "needs you to tell the truth about whether the next person walks into the "
                "same wall."))
     + "\n---\n\n### Name One Unstated Assumption, in the Village"),

    # ch7 - the draft said "insert BEFORE ### *The Ledger That Became a Standing*". That
    # heading is the subtitle of "## Section 5: The Victim, Up Close" one line above it,
    # so inserting there would land between a section heading and its own subtitle. It
    # goes before the Section 5 heading, closing Section 4.
    ("R3", "ch7.md",
     "It is more real.*\n\n---\n\n## Section 5: The Victim, Up Close",
     "It is more real.*\n\n---\n\n"
     + ecology("Presence",
               "Did staying cost something you agreed to spend, or something you never "
               "named?",
               ("Diplomat adds:",
                "The Diplomat does not need you to tally what you gave. The Diplomat needs "
                "you to tell the truth about whether you set the price or somebody set it "
                "for you."))
     + "\n---\n\n## Section 5: The Victim, Up Close"),

    # ch8 - the draft's placement stands. It follows the Stage Sequence exactly as ch4 and
    # ch5 do. ch8 uses no rule between these subsections, so none is added.
    ("R3", "ch8.md",
     "### *The Walk Back: Coming Down Without Losing What You Found*",
     ecology("Sight",
             "Did the whole view send you back down into the game, or did it hand you "
             "somewhere to stand outside it?",
             ("Sage adds:",
              "The Sage does not need you to rank the games. The Sage needs you to tell "
              "the truth about whether seeing more made you easier to reach or harder."))
     + "\n### *The Walk Back: Coming Down Without Losing What You Found*"),

    # -- 4 - Fix 2. `the controls` is a one-chapter synonym; `joystick` runs ch2 to ch8.
    ("Fix2", "ch1.md",
     "This is where you pick up the controls.",
     "This is where you pick up the joystick."),

    ("Fix2", "ch1.md",
     "You just put your hands on the controls.",
     "You just put your hands on the joystick."),

    # -- 6 - narrated reader-history. State the mechanism, let the reader recognise herself.
    ("Tier3", "ch5.md",
     "You already have a version of what \"tradition\" means. You've been carrying it "
     "since the last time someone used it against you.",
     "You already have a version of what \"tradition\" means. Most people got theirs the "
     "last time somebody used the word against them."),

    ("Tier3", "ch5.md",
     "You grew up in a family with a specific pattern — around money, around "
     "conflict, around who speaks and who stays silent. You inherited it. You have been "
     "living it, either repeating it or raging against it, for your entire adult life.",
     "Every family runs a pattern — around money, around conflict, around who speaks "
     "and who stays silent. Whatever yours was, you inherited it, and most of adult life "
     "goes into either repeating it or raging against it."),
]

# Section 5 of the approved file. Applied earlier; asserted, not re-applied, so that a
# revert of that commit surfaces here instead of passing silently.
A6 = [("ch1.md", "One process runs every one of these faces: the WAVE, which the Shaman "
                 "hands you in Chapter 3 and every school after that one uses."),
      ("ch1.md", "Each Game Master takes a chapter to teach you their game, and the WAVE "
                 "is how you play it.")]


def main():
    dry = "--dry" in sys.argv
    files, problems = {}, []

    for name, text in A6:
        t = io.open(os.path.join(MS, name), encoding="utf-8").read()
        if t.count(text) != 1:
            problems.append("A6 not seated in %s: %r found %d times"
                            % (name, text[:48], t.count(text)))

    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    for i, (ruling, name, old, new) in enumerate(EDITS, 1):
        if only and ruling not in only:
            continue
        if name not in files:
            files[name] = io.open(os.path.join(MS, name), encoding="utf-8").read()
        n = files[name].count(old)
        if n != 1:
            problems.append("#%d %s: anchor matched %d times, expected 1 — %r"
                            % (i, name, n, old[:60]))
            continue
        files[name] = files[name].replace(old, new, 1)
        print("  ok  #%-2d %-6s %-8s %s"
              % (i, ruling, name, old.split("\n")[0][:58]))

    if problems:
        print("\nABORTED, nothing written:")
        for p in problems:
            print("  " + p)
        return 1

    if dry:
        print("\ndry run — %d file(s), nothing written" % len(files))
        return 0

    for name, t in files.items():
        io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("\nwrote %d file(s)" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
