# -*- coding: utf-8 -*-
"""
agency_w2.py — the W-2 conversion, book-wide.

Wendell ruled W-2 on 2026-08-02: **a narrow license, navigation only.**

  LICENSED   the book / chapter taking mechanical or directional verbs for
             structural navigation -- covers, returns to, points to, put,
             handed in the sequencing sense. "Chapter 1 put the joystick in
             your hands" stands.

  ILLEGAL    perception, intention, speech and social-causal on the book or
             chapter -- asks, teaches, needs, wants, names, proposes, says.

The conversion target is NOT automatic, and this is the part of the ruling that
does the real work. Two-thirds of these land on **you**, not **I**:

  -> you   where the sentence is about what the reader gained. "This book has
           been teaching you" makes the book the agent and the reader the
           seat. In a book whose thesis is that the reader holds the joystick,
           the true subject is the reader.
  -> I     where the sentence is about a choice the author made -- credits,
           editorial decisions, direct questions.

    python3 instruments/agency_w2.py --dry
    python3 instruments/agency_w2.py
"""
import io, os, sys, collections

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

# (file, target, before, after)
EDITS = [
    # ---------------------------------------------------------------- -> you
    ("manuscript/ch9.md", "you",
     "The book has been preparing you for this.",
     "You have been preparing for this."),

    ("manuscript/ch9.md", "you",
     "This book has been teaching you what to do in those moments.",
     "You have been learning what to do in those moments."),

    ("manuscript/ch9.md", "you",
     "That's what this book has been teaching you. Not what to do.",
     "That's what you have been learning. Not what to do."),

    ("manuscript/ch9.md", "you",
     "they map the territory this book has been walking you into.",
     "they map the territory you have been walking into."),

    ("manuscript/ch8.md", "you",
     "the checking feels like exactly the discipline this chapter has been teaching.",
     "the checking feels like exactly the discipline you have been building."),

    ("manuscript/ch6.md", "you",
     "Everything this chapter teaches runs on Observe.",
     "Everything you learn here runs on Observe."),

    ("manuscript/ch5.md", "you",
     "Everything this chapter teaches runs on receiving something before you have finished evaluating it.",
     "Everything in this cycle runs on receiving something before you have finished evaluating it."),

    ("manuscript/ch5.md", "you",
     "This section teaches the Regent's cycle:",
     "Here is the Regent's cycle:"),

    # "Chapter 1 put the joystick in your hands" is LICENSED navigation and stays.
    ("manuscript/ch2.md", "you",
     "Chapter 1 put the joystick in your hands. This chapter teaches you how to walk the book.",
     "Chapter 1 put the joystick in your hands. Here you learn how to walk the book."),

    ("manuscript/ch2.md", "you",
     "It is how the book teaches recognition.",
     "It is how you come to recognise them."),

    ("appendices/APPENDIX_C_KEY_TERMS.md", "you",
     "The book teaches allyship through working with the Faces",
     "You learn allyship by working with the Faces"),

    # ---------------------------------------------------------------- -> I
    ("manuscript/ch2.md", "I",
     "That's the pivot this chapter needs from you.",
     "That's the pivot I need from you."),

    ("manuscript/ch2.md", "I",
     "This chapter asks whether you will stop treating your own somatic intelligence",
     "I am asking whether you will stop treating your own somatic intelligence"),

    ("appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", "I",
     "The book asks you to do things with your emotions",
     "I ask you to do things with your emotions"),

    ("appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", "I",
     "Use them when the framework asks for something your state won't let you reach yet.",
     "Use them when I ask for something your state won't let you reach yet."),

    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md", "I",
     "each of the six capacities the book names.",
     "each of the six capacities I name."),

    ("appendices/APPENDIX_F_POLARITY_MAP.md", "I",
     "The book names four because four chapters needed them;",
     "I name four because four chapters needed them;"),

    ("appendices/ON_THE_SHOULDERS_OF.md", "I",
     "That's the invisible scaffolding under how this book teaches",
     "That's the invisible scaffolding under how I teach"),

    ("appendices/ON_THE_SHOULDERS_OF.md", "I",
     "is the reason this book asks you to play rather than to improve.",
     "is the reason I ask you to play rather than to improve."),

    # ------------------------------------------------- licensed, but re-verbed
    # "the back of the book says where to start" is navigation doing its job,
    # but `says` is a speech verb. `points you to` is directional, which the
    # ruling licenses, and the sentence keeps its whole function.
    ("manuscript/ch3.md", "nav",
     "the back of the book says where to start.",
     "the back of the book points you to where to start."),
]


def main():
    dry = "--dry" in sys.argv
    loaded, plans = {}, []

    for path, target, before, after in EDITS:
        full = os.path.join(ROOT, path)
        if full not in loaded:
            loaded[full] = io.open(full, encoding="utf-8").read()

    # Verify every anchor against the ORIGINAL text before mutating anything.
    for path, target, before, after in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\n"
                     "Nothing written." % (path, n, before[:88]))
        plans.append((full, path, target, before, after))

    tally = collections.Counter()
    for full, path, target, before, after in plans:
        loaded[full] = loaded[full].replace(before, after, 1)
        tally[target] += 1
        print("\n%s  [-> %s]" % (path, target))
        print("  --  %s" % before)
        print("  ++  %s" % after)

    print("\ntargets: " + ", ".join("%s %d" % (k, v) for k, v in tally.most_common()))

    if dry:
        print("--dry: %d edits verified, nothing written." % len(plans))
        return 0

    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("wrote %d files, %d edits." % (len(loaded), len(plans)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
