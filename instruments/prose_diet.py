# -*- coding: utf-8 -*-
"""
prose_diet.py — the three grammar moves, measured.

Named 2026-07-29 after they were caught by eye in the W7 rewrites: leaning on
"is", on "it" without a clear antecedent, and on articles fronting nominalized
verbs. All three are ways of sounding like a sentence without committing to one,
and all three are nearly invisible one line at a time.

Implements the diagnostics four editors converge on:

  Lanham, *Revising Prose* — the Paramedic Method. Box the be-verbs, circle the
  prepositions, then ask "who is kicking whom?" and put the doer in the subject.
  Be-verbs are where the action went missing.

  Williams, *Style: Lessons in Clarity and Grace* — subjects should name
  characters, verbs should name their actions. When the action hides in a noun,
  turn the noun back into a verb. Williams licenses nominalization in four
  cases, which is why this is a candidate finder and not a gate.

  Sword, *The Writer's Diet* — five categories, three of which are these:
  be-verbs, zombie nouns, and the waste words *it / this / that / there*. Her
  rule for the last: use "it" and "this" only when you can state exactly which
  noun each refers to.

  Vague-pronoun-reference doctrine — search the draft for it/this/which/that,
  draw an arrow to the antecedent, and rewrite anything with no arrow.

**Thresholds are this book's own baseline, not absolute standards.** The
manuscript is written; the job is to stop new prose drifting heavier than the
prose around it. A chapter at the book average scores 1.00.

    python3 instruments/prose_diet.py              # per chapter vs baseline
    python3 instruments/prose_diet.py -v           # quote the orphan "it" sites
    python3 instruments/prose_diet.py FILE         # score a draft file
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
BLOCK = re.compile(r"\n?\n<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n.*?\n<!-- /\1 -->\n", re.S)

BE     = re.compile(r"\b(is|are|was|were|be|been|being)\b", re.I)
COPULA = re.compile(r"^\W*[\w'][\w' ]{0,30}\s(is|are|was|were)\s", re.I)
WASTE  = re.compile(r"\b(it|this|that|there)\b", re.I)
# Sword's zombie nouns arrive wearing an article — that is what makes them
# findable. "the maintenance of", "a recognition that".
ZOMBIE = re.compile(r"\b(?:the|a|an)\s+\w+(?:tion|ment|ance|ence|ness|ity|ism|sion)\b", re.I)
# "It is/was" opening a sentence with no noun behind it: Lanham's expletive,
# Sword's waste word, and the classic missing antecedent, all at once.
EXPLETIVE = re.compile(r"(?:^|(?<=[.!?]\s))\s*(It|There)\s+(is|was|are|were)\b")

# Book baseline, measured 2026-07-29 on the stripped manuscript.
BASE = {"be": 50.3, "copula": 29.1, "waste": 56.3, "zombie": 11.1, "expletive": 2.4}


def sentences(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"^[#>|\-*\s]*$", " ", t, flags=re.M)
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) > 3]


def score(text):
    w = max(len(text.split()), 1)
    S = sentences(text)
    n = max(len(S), 1)
    return {
        "be":        len(BE.findall(text)) / w * 1000,
        "copula":    sum(1 for s in S if COPULA.search(s)) / n * 100,
        "waste":     len(WASTE.findall(text)) / w * 1000,
        "zombie":    len(ZOMBIE.findall(text)) / w * 1000,
        "expletive": sum(1 for s in S if EXPLETIVE.match(s)) / n * 100,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv
    if args:
        files = args
    else:
        files = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                       key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))

    keys = ["be", "copula", "waste", "zombie", "expletive"]
    print("ratio against the book's own baseline — 1.00 is average, >1.30 is heavy\n")
    print(f"{'file':<12}" + "".join(f"{k:>11}" for k in keys))
    print("-" * (12 + 11 * len(keys)))
    worst = []
    for f in files:
        t = BLOCK.sub("", io.open(f, encoding="utf-8").read())
        s = score(t)
        row = "".join(f"{s[k]/BASE[k]:>11.2f}" for k in keys)
        print(f"{os.path.basename(f):<12}{row}")
        for k in keys:
            if s[k] / BASE[k] > 1.30:
                worst.append((os.path.basename(f), k, s[k] / BASE[k]))

    if worst:
        print("\nheavy (>1.30):")
        for f, k, r in sorted(worst, key=lambda x: -x[2]):
            print(f"  {f} {k} {r:.2f}")

    if verbose:
        print("\n--- expletive / orphan openers: no noun behind the pronoun ---")
        for f in files:
            t = BLOCK.sub("", io.open(f, encoding="utf-8").read())
            for s in sentences(t):
                if EXPLETIVE.match(s):
                    print(f"  {os.path.basename(f)}: {s[:96]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
