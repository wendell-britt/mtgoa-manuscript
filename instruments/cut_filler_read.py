# -*- coding: utf-8 -*-
"""cut_filler_read -- DL-95. The filler uses of "the read" leave ch3.

Wendell, 2026-09-09: *"'their read' hate this use of read. It's overused and means very little"*,
then on the count: *"we should probably reevaluate this. We need a stronger word that doesn't get
so tired upon repetition"*, then the ruling: *"cut the filler reads only."*

**23 noun uses in one chapter, roughly one every 340 words.** No word survives that rate, which
is why the answer here is frequency rather than vocabulary -- a stronger word would tire on the
same page. The two loose uses outside ch3, *"their read of you as…"* meaning their opinion of
you, went with DL-94.

THE THREE JOBS IT WAS DOING, and only one of them earns the noun:

  - **the faculty** and **the defined term** -- *"your read catches what the group never
    registers"*, *"Function means what the read does once it leaves you"*, *"The read has four
    domains"*, the four handbook labels, the section heading. **Kept, 15 uses.** These define it,
    hand it off, or label it, and a technical term has to be repeated to stay technical.
  - **filler** -- where it means no more than *what you noticed* and the sentence can say so.
    **Cut, 8 occurrences in 7 spans.**

One of the eight was mine, put there an hour earlier: DL-92 replaced *one true sentence* with
*the read* at ch3:852, which is the chapter's closing line and already had *the read* forty words
above it. **The rule that catches this does not exist: nothing counts how often a word is asked
to carry a paragraph.**

    python3 instruments/cut_filler_read.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard

CLAIM = "DL-95"
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

EDITS = [
    # the Polarity Map instruction: the axis is where you sat, not where a noun deserved to sit
    ("Not where the read deserved to sit.",
     "Not where you wish you had sat."),
    # Move 4's receipt, seconds after you catch it
    ("plainly, in the seconds after the read.",
     "plainly, in the seconds after you catch it."),
    # Raise Awareness: the appositive was restating the clause it hung off. Now a phrase.
    ("you said what was actually happening, the read under the approved language,",
     "you said what was actually happening, under the approved language,"),
    # the chapter's closing line, and the one I broke on 2026-09-09
    ("and why the read, said and not only felt, is the move everything else will stand on.",
     "and why saying what you sensed, and not only feeling it, is the move everything else "
     "will stand on."),
    # the Tell
    ("the read spent on being seen as perceptive instead of on changing something.",
     "what you saw, spent on being seen as perceptive instead of on changing something."),
    # the placement questions
    ("Who can tell you no, redirect you, or correct the read?",
     "Who can tell you no, redirect you, or say you have it wrong?"),
    # two in two sentences, at the handoff to ch4
    ("One more voice waits on the other side of the read. The moment you take the read into the "
     "world",
     "One more voice waits after that. The moment you take what you saw into the world"),
]

NOUN = re.compile(r"\b(?:the|a|an|your|their|his|her|my|our|that|this|one|bad|good|accurate|"
                  r"clean|first|true|same|whole)\s+read\b", re.I)
TAIL = re.compile(r"\s+(?:it|this|that|the|a|an|him|her|them|us|me|you|my|your|his|their|our|"
                  r"through|about|into|on|in|to|for|and|or|as|with|from|back|over|up|out|aloud|"
                  r"again|[A-Z])\b")


def count(text):
    return sum(1 for m in NOUN.finditer(text) if not TAIL.match(text[m.end():]))


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)

    before = io.open(P, encoding="utf-8").read()
    after = before
    for old, new in EDITS:
        if after.count(old) != 1:
            sys.stderr.write("REFUSED: span matched %d times (need 1).\n  %s\n"
                             % (after.count(old), old[:70]))
            sys.exit(2)
        after = after.replace(old, new, 1)

    b, a = before, after
    for old, new in EDITS:
        b = b.replace(old, "", 1); a = a.replace(new, "", 1)
    if norm(b) != norm(a):
        sys.stderr.write("REFUSED: prose changed outside the declared spans.\n"); sys.exit(3)
    for old, new in EDITS:
        if old in after or new not in after:
            sys.stderr.write("REFUSED: a declared edit did not take.\n  %s\n" % old[:70])
            sys.exit(4)

    io.open(P, "w", encoding="utf-8").write(after)
    print("filler reads cut: %d span(s)" % len(EDITS))
    print("noun uses of 'read' in ch3: %d -> %d, all defining, handing off, or labelling"
          % (count(before), count(after)))
    print("  (this counter undercounts: its TAIL filter skips 'the read into…', so one of the"
          "\n   eight occurrences cut was never in the 23. 8 cut, 7 of them counted.)")


if __name__ == "__main__":
    main()
