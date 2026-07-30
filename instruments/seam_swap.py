# -*- coding: utf-8 -*-
"""
Swap "this chapter" for "the School of the X" in the six treatises.

`instruments/seam_sweep.py` found 22 sentences in Sections 1-3 where a Head refers to
the chapter they are standing in. A Head cannot know they are in a book. Wendell ruled
2026-07-30 that the replacement is the School, in full form: *the School of the Body*,
not *the Body*.

The fix is additive rather than mechanical. A Head who says *"every move the School of
the Bridge teaches"* is doing worldbuilding in a sentence that previously did
bookkeeping, so the pass gains texture instead of sanding it off.

Fifteen swaps here. The other seven are held:

  · four copies of the Appendix F pointer, which have no in-world equivalent and move
    below the seam once the seam has a marked location. The signature placement is not
    signed off, so there is nowhere to move them to yet.
  · ch3:169, promoted to the margin, which is a marginalia edit rather than a body edit.
  · ch8:191, the Wilber attribution, held with the other new findings.

Every replacement was run through the `no-ai-slop` skill and its `eval.md`, not just the
noun swap. Five sentences changed by more than the noun; those are listed in the ruling
column below so Wendell can revert any one of them independently.

    python3 instruments/seam_swap.py --dry
    python3 instruments/seam_swap.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# (chapter, old, new, what the slop pass did beyond the noun swap)
SWAPS = [
    (3, "This chapter is asking for the trust.",
        "The School of the Body is asking for the trust.",
        "noun only"),

    (3, "it requires you to stop moving, harder than anything in this chapter",
        "it requires you to stop moving, harder than anything else the School of the Body teaches",
        "noun only"),

    (3, "Everything in this section argues for keeping it calibrated, and the argument holds: a read you never let yourself have is a read you can never act on.",
        "Everything the School of the Body teaches argues for keeping it calibrated. A read you never let yourself have is a read you can never act on.",
        "cut 'and the argument holds:' — filler plus a colon reveal. The claim lands harder unannounced."),

    (4, "You met the Polarity Map in Chapter 3.",
        "You met the Polarity Map at the School of the Body.",
        "noun only"),

    (5, "Here's what this chapter is not: a defense of the organizations that used tradition to protect power.",
        "The School of the Oath is not a defense of the organizations that used tradition to protect power.",
        "three patterns out at once: throat-clearing opener, colon reveal, negative listing. Claim unchanged."),

    (5, "You met the Polarity Map in Chapter 3.",
        "You met the Polarity Map at the School of the Body.",
        "noun only"),

    (6, "That case forms the spine of this section, and it holds.",
        "That case is the spine of the School of the Pattern, and it holds.",
        "'forms' to 'is' — the skill prefers the copula where it is clearer."),

    (6, "the most comfortable sentence in this book's neighborhood",
        "the most comfortable sentence in the discipline",
        "'this book's neighborhood' was both vague and authorial. A Head says 'the discipline'."),

    (6, "Here the pair gets specific for the reader this book addresses.",
        "The pair gets specific for the student the School of the Pattern attracts.",
        "dropped 'Here' (throat-clearing) and the ICA leak 'the reader this book addresses'."),

    (7, "that version forces this chapter to define the word before it can use it",
        "that version forces the School of the Bridge to define the word before it can use it",
        "noun only"),

    (7, "Which produces the sentence this chapter exists to disprove, the most protected sentence the ideal reader carries.",
        "Which produces the sentence the School of the Bridge exists to disprove, the most protected sentence a student arrives carrying.",
        "second ICA leak: 'the ideal reader' becomes 'a student'."),

    (7, "Every move in this chapter runs downstream of that myth.",
        "Every move the School of the Bridge teaches runs downstream of that myth.",
        "noun only"),

    (7, "This chapter replaces it with something a person can actually stand on: not *I have never caused harm*, but *I can be told what I cost and stay in the conversation afterward.*",
        "The School of the Bridge replaces it with something a person can stand on, which is not *I have never caused harm* but *I can be told what I cost and stay in the conversation afterward.*",
        "colon reveal out, empty 'actually' out. The not/but stays: the two quoted sentences are the teaching, so the contrast is the content rather than a flourish."),

    (7, "You met the Polarity Map in Chapter 3.",
        "You met the Polarity Map at the School of the Body.",
        "noun only"),

    (8, "This chapter takes up what happened next.",
        "The School of the Horizon takes up what happened next.",
        "noun only"),
]


def main():
    dry = "--dry" in sys.argv
    texts, plan = {}, []
    for n, old, new, note in SWAPS:
        if n not in texts:
            texts[n] = io.open(os.path.join(MS, "ch%d.md" % n), encoding="utf-8").read()
        c = texts[n].count(old)
        if c != 1:
            raise SystemExit("ch%d: %r matched %d times, expected 1" % (n, old[:60], c))
        texts[n] = texts[n].replace(old, new, 1)
        plan.append((n, old, new, note))

    if dry:
        for n, old, new, note in plan:
            print("ch%d\n  -  %s\n  +  %s\n  ~  %s\n" % (n, old[:150], new[:150], note))
        print("%d swaps, all anchors matched exactly once" % len(plan))
        return 0

    for n, t in texts.items():
        io.open(os.path.join(MS, "ch%d.md" % n), "w", encoding="utf-8").write(t)
    beyond = sum(1 for _, _, _, note in plan if note != "noun only")
    print("%d swaps applied across %d chapters; %d changed beyond the noun"
          % (len(plan), len(texts), beyond))
    return 0


if __name__ == "__main__":
    sys.exit(main())
