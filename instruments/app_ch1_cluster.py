# -*- coding: utf-8 -*-
"""
ch1's app cluster, drafted against the Myths Read ruling. DL-20 blocker one.

Wendell 2026-07-31: *"take the app out for v1 and let v2 carry the integration; the URL
masteringallyship.com exists now; the Myths Read and the superpower quiz can be live by
ship, so those stay."*

Six sites, and the ruling sorts them into three kinds.

**Two are the Myths Read and stay, re-pointed.** `ch1:83` is the Myths Read at first
mention, described but never named, which is why it did not read as one: *"a short,
unflattering diagnostic that tells you which of these are yours."* It takes the URL.
`ch1:205` names it and refers back, so it does not repeat the address.

**One is the tracking promise and goes, per B1's ruling: nothing replaces it.** `ch1:211`
claimed the app *"holds it better ... dates every version, and shows you how your face,
your shadow, and your myths move across a year of play."* The promise comes out; the
practice underneath it survives as something she can do alone, which is the ICA standard
in `SPEC_WORKBOOK_SCOPE.md:53`. Dating the versions is an instruction, not a feature.

**Three are false claims about where things live.** `ch1:249`'s *"The cards live in the
app now, so you are not carrying a paper deck in your coat"* is not merely unshippable,
it contradicts the chapter's own origin story twenty lines earlier, where Wendell carries
blank poker cards. `ch1:257` routes the first BAR into the app. `ch1:269` sells thirty
days in it.

**`[ URL / QR ]` stays.** Wendell deferred it pending links and it is not to be
allowlisted, so ch1:269 keeps the deck offer and the placeholder and loses only the trial.

Measured against the six originals, which is the discipline this pass keeps proving it
needs. The draft is better on five counters and the original was **over the line on two**:

    waste      1.31 -> 0.95      expletive  2.78 -> 0.00
    zombie     0.18 -> 0.00      empty      0.78 -> 0.63
    copula     0.46 -> 0.34      be         0.43 -> 0.62

One orphan opener was caught in my own draft before it landed: *"It is the first card in
your deck"* measured expletive 4.17 where the original's *"where it becomes"* had avoided
it. Naming the noun fixed it.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("(The app runs a short, unflattering diagnostic that tells you which of these are "
     "yours",
     "(A short, unflattering diagnostic at masteringallyship.com tells you which of "
     "these are yours"),

    ("(The app's Myths Read sorts your real top few",
     "(The Myths Read sorts your real top few"),

    ("Pen and paper hold this fine. The app holds it better: it keeps the sheet "
     "somewhere you will actually find it, dates every version, and shows you how your "
     "face, your shadow, and your myths move across a year of play, the change you "
     "cannot see from inside a single week. It is the same app that keeps your BARs, "
     "and your book comes with thirty days in it.",
     "Pen and paper hold this. Date every version, and across a year of play you can "
     "watch your face, your shadow and your myths move, which is the change you cannot "
     "see from inside a single week."),

    ("The cards live in the app now, so you are not carrying a paper deck in your coat. "
     "Every BAR becomes a card",
     "Every BAR becomes a card"),

    ("Then keep it on you. Put it in the app, where it becomes the first card in your "
     "deck and stays in reach for the rest of the book.",
     "Then keep it on you. That card is the first in your deck, and it stays in reach "
     "for the rest of the book."),

    ("Your book comes with thirty days in the app, where the BAR you just wrote becomes "
     "the first card in your deck and your captures stay in reach as you read. Activate "
     "it, and find the hundred-and-twenty-card deck for when you want the moves in your "
     "hands, at **[ URL / QR ]**.",
     "Find the hundred-and-twenty-card deck, for when you want the moves in your hands, "
     "at **[ URL / QR ]**."),
]


def main():
    p = os.path.join(MS, "ch1.md")
    t = io.open(p, encoding="utf-8").read()
    bad = []
    for i, (old, new) in enumerate(E, 1):
        n = t.count(old)
        if n != 1:
            bad.append("#%d matched %d times: %r" % (i, n, old[:56]))
            continue
        t = t.replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        io.open(p, "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
