# -*- coding: utf-8 -*-
"""
The certification removal, and ch9's offer list reduced to what ships.

Source: `drafts/APPROVED_remove_certification_2026-08-01.md`, ruled 2026-08-01. Three
sites carry a credential the book cannot honour in v1. `back_matter/about_the_author.md`
carries a fourth and is not touched here: it was applied on `claude/edit-enrollment-page`
and belongs to that branch under DL-18.

**The draft's anchors were stale, again, and for the same reason as the app draft.** It
was written against master; this branch ran the W9 em-dash sweep, which converted the
joints at ch9:159 and ch9:700 from em-dashes to parentheses. The ruling is untouched and
the anchors below are re-derived from the current page. Two drafts in a row have now gone
stale this way, which is the cost of a sweep that touches every chapter and the reason
spec_edit.py aborts rather than fuzzy-matches.

**The offer list.** The ruling folds the certification cut into the app removal because
bars-engine is the list's middle entry, so the paragraph is edited once rather than twice.
Cutting the entry is removal, not invention: DL-20 requires it regardless, and the three
count words follow arithmetically from a list that is now two long. What is NOT done here
is drafting a replacement. The real offer stack is deck / Dojo / cohort / ninety minutes,
and it lives on an enrollment page that is still `drafts/DRAFT_enrollment_page_2026-08-01.md`
rather than `back_matter/enrollment.md`. ch9's job is to point at that page, and a pointer
cannot be written to a file that does not ship yet. Reported rather than improvised.

**The passive.** *"was written to make possible"* is a passive with a hidden doer in a
paragraph where the doer is the whole point: the sentence is about what Wendell wants
handed off. `I wrote this book to make possible` puts him back in it.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

BARS_ENTRY = (
    "**Bars-engine, and the non-profit that holds it.** The live game. Campaigns, "
    "quests, allyship programs, other players already mid-move. This is where the "
    "practice stops being something you do alone with a deck and starts having other "
    "people's outcomes attached to it. It was running before you finished this book. It "
    "does not need your admiration. It needs whatever you cut the field down to in "
    "Section 6.\n\n"
)

E = [
    # ---- the three ruled certification sites ---------------------------------
    ("ch9.md",
     "I am looking for people to carry this and eventually get certified to teach it.",
     "I am looking for people to carry this."),

    ("ch9.md",
     "deeply enough to run it for others, reach out about certification "
     "(wendell@masteringallyship.com).",
     "deeply enough to run it for others, say so (wendell@masteringallyship.com)."),

    ("ch9.md",
     "**The coaching, and the certification behind it.** The most expensive of the "
     "three, in every sense of the word.",
     "**The coaching.** The more expensive of the two, in every sense of the word."),

    # ---- the passive, same paragraph ------------------------------------------
    ("ch9.md",
     "that is the succession this whole book was written to make possible",
     "that is the succession I wrote this book to make possible"),

    # ---- DL-20 · the middle entry, and the count words that follow ------------
    ("ch9.md", BARS_ENTRY, ""),

    ("ch9.md",
     "Three things exist on the other side of this book.",
     "Two things exist on the other side of this book."),

    ("ch9.md",
     "It is the smallest of the three steps and the only one you can take this week.",
     "It is the smaller of the two steps and the only one you can take this week."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
