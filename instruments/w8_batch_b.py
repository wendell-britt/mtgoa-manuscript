# -*- coding: utf-8 -*-
"""
W8 batch B — the denying negations in ch7, which carries 14 of the book's 31.

Method is the one locked in W7: cut → essence → synthesize → voice. Where the
denied half was doing real work (a reader really will hear "ultimatum", really
will guess "neutrality"), the fix concedes the wrong guess in its own sentence
and then states the thing, instead of staging X-is-not-A-it-is-B.

Left standing on purpose: the italic shadow-speech at line 399 (*This is not the
moment. They are not ready to hear it.*) — that is the distortion talking, and
the same figure runs in ch4 and ch6. Also *you are not anxious despite your
holding — you are anxious because you hold something that matters*, where the
despite/because turn is the point rather than a formula.

    python3 instruments/w8_batch_b.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch7.md")

# (anchor, replacement, expected_count)
EDITS = [
("This is not naive optimism — it is a discipline of extending the same hypothesis to the present that you extend to strangers on the street.",
 "Call it optimism if you want. The discipline extends to the present the same hypothesis you already extend to strangers on the street.", 1),

("The Diplomat without Translator is not a bridge-builder — they are two ends of a wire that never actually connected.",
 "The Diplomat without Translator is two ends of a wire that never connected.", 1),

("I am a partisan who can also really hear. That is not a contradiction — it is the definition of a Translator.",
 "I am a partisan who can also really hear. That combination defines the Translator.", 1),

("The anxiety is not wrong — it is reading the field accurately.",
 "The anxiety reads the field accurately.", 1),

("Anxiety is not a signal to leave — it is a signal to lean in more deliberately.",
 "Anxiety signals you to lean in more deliberately.", 1),

("Not because you have to — because you have decided.",
 "You decided on it; nothing obliged you.", 1),

("*I don't leave when it gets hard. That is not a rule — it is a practice.*",
 "*I don't leave when it gets hard. I practice that rather than declare it.*", 1),

("Resentful peace is not peace — it is deferred conflict wearing a polite face.",
 "Resentful peace is deferred conflict wearing a polite face.", 1),

("The distortion is not that it keeps the ledger. The distortion is what it does with the balance.",
 "The distortion arrives in what it does with the balance.", 1),

("The inner work is not separate from the game. The inner work is what makes the game real.",
 "The inner work is what makes the game real.", 1),

("This is not a game of winning. The Diplomat's game is not about victory — it is about creating the conditions where connection remains possible,",
 "The Diplomat's game creates the conditions where connection remains possible,", 1),

("Close with Honest Terms is not an ultimatum. It is the single clear sentence that names what this field must hold for your staying to remain real — said once, and then left alone for the field to answer.",
 "Close with Honest Terms is one clear sentence naming what this field must hold for your staying to remain real, said once and then left alone for the field to answer. The leaving-alone separates it from an ultimatum.", 1),

("The moves are not a sequence. They are a way of being with people.",
 "The moves add up to a way of being with people.", 1),

("The Diplomat's gift is not neutrality — it is the capacity to be a partisan who can still hold the field.",
 "Neutrality is the easy guess. The Diplomat's gift is the capacity to be a partisan who can still hold the field.", 1),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    bad = []
    for a, b, want in EDITS:
        n = t.count(a)
        if n != want:
            bad.append((n, want, a[:64]))
        else:
            t = t.replace(a, b)
    if bad:
        print("ABORT — anchor counts wrong, nothing written:")
        for n, want, a in bad:
            print("  %d matches (want %d): %r" % (n, want, a))
        return 1
    io.open(P, "w", encoding="utf-8").write(t)
    print("applied %d edits to ch7" % len(EDITS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
