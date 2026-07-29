# -*- coding: utf-8 -*-
"""
W9 — ch7 em-dash pass, batch A (Sections 1-3 and the first two channels).

Every anchor spans the dash and is short on purpose: the shorter the anchor, the
less prose the script has to reproduce exactly, and the fewer ways an anchor can
be silently wrong.

The decision behind each one, per SPEC_EMDASH_AND_DENSITY §1.4:

  full stop   two independent clauses. The commonest right answer, and the one
              the drafting model was avoiding, because a period commits.
  comma       a modifier, a list, or an aside.
  colon       the tail names or defines what came before.
  parentheses a true aside that would drown in commas.

Deliberately NOT all colons. Fifty colons would be the same tic in a new
costume, which is the W7 lesson.

    python3 instruments/w9_ch7_a.py --dry
    python3 instruments/w9_ch7_a.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch7.md")

EDITS = [
# --- Section 1: the two openings -------------------------------------------
("reads as devotion — except it isn't", "reads as devotion, except it isn't"),
("has lost something — but cannot name the loss", "has lost something but cannot name the loss"),
("He has also — once, in a hard moment — surfaced", "He has also, once in a hard moment, surfaced"),
("because he had now chosen it — not scarce in the way of withholding",
 "because he had now chosen it, not scarce in the way of withholding"),
("integrative negotiation — surfacing what each party protects, naming stakes and sacrifices honestly, and closing toward terms",
 "integrative negotiation. It surfaces what each party protects, names stakes and sacrifices honestly, and closes toward terms"),
("what the agreement actually requires — and so nobody treats",
 "what the agreement actually requires, so nobody treats"),

# --- Section 1: the five stages ---------------------------------------------
("do not form a checklist — they run as a journey in sequence.",
 "run as a journey in sequence rather than a checklist."),
("another camp can hear — not betraying either side, but finding the common ground of meaning.",
 "another camp can hear, betraying neither side and finding the common ground of meaning."),
("even when the field is charged — not the four seconds of Stand",
 "even when the field is charged, not the four seconds of Stand"),
("the pretense that they did not occur — cleaning the wound",
 "the pretense that they did not occur: cleaning the wound"),
("generosity without closure — and generosity without closure stops being a gift",
 "generosity without closure, and generosity without closure stops being a gift"),

# --- Section 2: the altitude and the channels -------------------------------
("altitude of human development — pluralistic, relational, oriented toward inclusion.",
 "altitude of human development: pluralistic, relational, oriented toward inclusion."),
("multiple valid perspectives simultaneously — can be a partisan and still make space, can stand for something and still listen, can name",
 "multiple valid perspectives simultaneously. They can be a partisan and still make space, can stand for something and still listen, can name"),
("Not softening, not betraying — bridging the gap between ways of being in the world.",
 "Bridging the gap between ways of being in the world, without softening it and without betraying it."),
("Not solving — holding.", "Holding rather than solving."),
("must hold for everyone — and closing so the field moves.",
 "must hold for everyone, and closing so the field moves."),
("Each mode's full arc — the dissatisfaction it carries and the alchemy that transmutes it — is worked through",
 "Each mode's full arc, the dissatisfaction it carries and the alchemy that transmutes it, is worked through"),

# --- Section 2: the term ----------------------------------------------------
("the word holds real — people do this — and it explains why",
 "the word holds real (people do this), and it explains why"),
("for your staying to remain real — offered as information, once,",
 "for your staying to remain real, offered as information, once,"),
("The reader stays — pleasant, reliable, and slowly becoming furniture — and calls",
 "The reader stays (pleasant, reliable, and slowly becoming furniture) and calls"),

# --- Section 3: Care and Impact ---------------------------------------------
("protecting the connection itself — the trust, the willingness",
 "protecting the connection itself: the trust, the willingness"),
("the world outside the relationship — what moves, what stops, who is materially better off",
 "the world outside the relationship. What moves, what stops, who is materially better off"),
("into a conversation that needed this one — the true thing said in a way",
 "into a conversation that needed this one: the true thing said in a way"),
("The Care end has a vocabulary — holding, tending, centering, making space — and the Impact end",
 "The Care end has a vocabulary (holding, tending, centering, making space) and the Impact end"),

# --- Section 4: Bridge-Builder ----------------------------------------------
("the Diplomat's entry point — the channel through which contact happens",
 "the Diplomat's entry point: the channel through which contact happens"),
("every relational field as a transaction — what can I get, what do I need",
 "every relational field as a transaction. What can I get, what do I need"),
("always connecting, always bridging — and who cannot stop.",
 "always connecting, always bridging, and who cannot stop."),
("Bridge-Builder is **anxiety** — the low hum of", "Bridge-Builder is **anxiety**: the low hum of"),
("**stage-fright** — the fear of being seen without a script.",
 "**stage-fright**, the fear of being seen without a script."),
("always making contact — never actually arriving,", "always making contact, never arriving,"),
("from output to internal state — not eliminating the bridge, but ensuring something real builds it.",
 "from output to internal state, so that something real builds the bridge instead of the bridge being abandoned."),

# --- Section 4: Translator --------------------------------------------------
("most cognitively demanding channel — the work of taking meaning from one camp",
 "most cognitively demanding channel: the work of taking meaning from one camp"),
("a kind of relational deafness — not literally unable to hear, but incapable of truly receiving meaning",
 "a kind of relational deafness. Not literally unable to hear, but incapable of receiving meaning"),
("Translator has no position — the perfect channel, and therefore useless,",
 "Translator has no position: the perfect channel, and therefore useless,"),
("**intellectual superiority** — the subtle, seductive belief",
 "**intellectual superiority**, the subtle, seductive belief"),
("collapse into something more useful — the willingness to be changed by what you hear.",
 "collapse into something more useful: the willingness to be changed by what you hear."),
("a false neutrality that serves no one — least of all the field.",
 "a false neutrality that serves no one, least of all the field."),
]


def main():
    dry = "--dry" in sys.argv
    t = io.open(P, encoding="utf-8").read()
    bad = []
    for a, b in EDITS:
        n = t.count(a)
        if n != 1:
            bad.append((n, a[:70]))
        else:
            if dry:
                print("\n-  …%s…\n+  …%s…" % (a, b))
            t = t.replace(a, b, 1)
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for n, a in bad:
            print("  %d matches: %r" % (n, a))
        return 1
    if not dry:
        io.open(P, "w", encoding="utf-8").write(t)
    print("\n%s %d edits" % ("would apply" if dry else "applied", len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
