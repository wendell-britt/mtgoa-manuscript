# -*- coding: utf-8 -*-
"""
w2_taught.py — the four W-2 escapees that teach.

W-2 was ruled 2026-08-02 and reported closed at 22 sites. Three more turned up
in ch9 during the thesis-contradiction pass. These are the last four, and they
are all one shape: a chapter or a book teaching.

W-2's ruling is explicit that this is the illegal half. The book and chapter may
take mechanical and directional verbs for structural navigation -- covers,
returns to, points to, put, handed, left -- and may NOT take perception,
intention, speech or social-causal verbs. `teach` is social-causal, severity 4.

The conversion follows W-2's own precedent rather than being invented here. Its
largest group went to `you`, on the reasoning that "This book has been teaching
you what to do" makes the book the agent and the reader the seat, when the true
subject is the reader:

    This book has been teaching you what to do in those moments.
    -> You have been learning what to do in those moments.

Tenses are kept as found. ch3:701 has `taught you`, simple past, so it takes
`you learned`; ch4:544 has `has taught you`, present perfect, so it takes `you
have learned`. The originals were already inconsistent with each other and that
is not this pass's business to tidy -- they sit in different chapters and each
matches its own surrounding tense.

ch3:701 and ch4:544 are the same device in two chapters: "Everything [the first
half of] this chapter (has) taught you runs on [X]." Both convert the same way,
so the parallel survives.

The six navigation sites in this block -- `put`, `leaves` x2, `gave` x3 -- are
NOT touched. They are what W-2 licensed, and they kept flagging only because the
ruling had lived as prose in `open_rulings` where no instrument could read it.
Now encoded as an entity_partial on Grade 0.

    python3 instruments/w2_taught.py --dry
    python3 instruments/w2_taught.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ("manuscript/ch3.md",
     "The chapter has taught you to feel each channel all the way through.",
     "You have learned to feel each channel all the way through."),

    ("manuscript/ch3.md",
     "Everything the first half of this chapter taught you runs on a feeling being allowed "
     "onto the field.",
     "Everything you learned in the first half of this chapter runs on a feeling being allowed "
     "onto the field."),

    ("manuscript/ch4.md",
     "Everything this chapter has taught you runs on a charge you trust enough to aim.",
     "Everything you have learned in this chapter runs on a charge you trust enough to aim."),

    # "you already have the framework" rather than "you already learned it" --
    # the next sentence is "These are the reps", so what matters is that the
    # reader HOLDS the thing, not how they came by it.
    ("appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md",
     "it isn't a recap — the book already taught the framework.",
     "it isn't a recap — you already have the framework."),
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
        print("  --  %s" % before[:100])
        print("  ++  %s" % after[:100])

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
