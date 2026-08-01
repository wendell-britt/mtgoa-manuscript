# -*- coding: utf-8 -*-
"""
The app removal's mechanical set: B2 six times, three practice-prompt tails, one draw
instruction. DL-20 blocker one.

**B2, six identical sites.** The section is *From Card to Quest* and the sentence teaches
read against played, "and the difference is a person." The app was where the reading
ended, so it needs a place a card can die that is not a quest. ch1 already names one:
*"a notebook you will almost never reopen, because reviewing a journal is real work and
no one has made that part work."* Using the book's own image for failed capture keeps the
contrast and costs no new vocabulary.

**Three practice-prompt tails.** They match the pattern the tag strip left standing in
thirty other prompts: *Two minutes to capture it as a BAR.* Each keeps its own tail.

**One draw instruction.** *"by hand or by letting the app deal it"* offered two ways to
draw; without an app there is one, so the clause goes rather than getting a substitute.

**Measured against the originals, which is the discipline this repo already recorded.**
88 words before and after, so nothing here is the shrinking-denominator artefact:

    copula  1.47 -> 0.98   better
    zombie  1.52 -> 1.52   unchanged, and already over the line in the original
    waste   1.21 -> 1.61   three real tokens added, one removed

The three are the `it` in "capture it as a BAR", which is the phrasing thirty other
prompts in this book already use. Deviating to save a pronoun would break consistency
with all of them, and the pronoun has a clear antecedent. Accepted, and recorded rather
than tuned.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

B2_OLD = "A card that ends in the app is a card you read."
B2_NEW = "A card that ends in a notebook is a card you read."

E = [(ch, B2_OLD, B2_NEW) for ch in
     ("ch3.md", "ch4.md", "ch5.md", "ch6.md", "ch7.md", "ch8.md")]

E += [
    ("ch4.md", "Two minutes in the app, while it's still warm.",
     "Two minutes to capture it as a BAR, while it's still warm."),
    ("ch5.md", "Two minutes in the app, while the weight of it is still on you.",
     "Two minutes to capture it as a BAR, while the weight of it is still on you."),
    ("ch6.md", "Two minutes in the app while it is still in your body.",
     "Two minutes to capture it as a BAR while it is still in your body."),
    ("ch3.md", "Draw one card from your twenty, by hand or by letting the app deal it.",
     "Draw one card from your twenty."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:56]))
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
