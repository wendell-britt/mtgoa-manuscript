# -*- coding: utf-8 -*-
"""
W9 — ch7 em-dash pass, batch B (Sections 4-6, Translator through Negotiator).

Two families recur here and each gets a deliberate mix rather than one mark:

  "The Dissatisfaction here is **X** — gloss"   five times
  "The Neutral Channel pattern here is **X** — gloss"   five times

Ten identical colons would be the W7 mistake in a new costume — a formula fixed
by installing another formula. So the ten split across colon, comma, and a full
stop that gives the gloss its own verb.

The inline numbered labels — (1) **Witness** — take a colon, unlike the
standalone label lines W9 converted to a full stop. A label mid-sentence cannot
take a period without ending the sentence around it.

    python3 instruments/w9_ch7_b.py --dry
    python3 instruments/w9_ch7_b.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch7.md")

EDITS = [
("is **intellectual superiority** — the behavioral pattern of using your fluency",
 "is **intellectual superiority**: the behavioral pattern of using your fluency"),
("the original speaker and ask — \"did I get this right?\"",
 "the original speaker and ask: \"did I get this right?\""),
("than any other Diplomat channel — the work of maintaining enough safety",
 "than any other Diplomat channel. The work is maintaining enough safety"),
("a kind of presence collapse — the moment something difficult actually happens, they either",
 "a kind of presence collapse. The moment something difficult happens, they either"),
("mistakes stillness for safety — they sit in the middle of chaos",
 "mistakes stillness for safety. They sit in the middle of chaos"),
("Real Field-Holding does not remove the charge — it contains it.",
 "Real Field-Holding contains the charge rather than removing it."),
("The Dissatisfaction here is **anxiety** — the Field-Holder's nervous system",
 "The Dissatisfaction here is **anxiety**. The Field-Holder's nervous system"),
("anxious despite your holding — you are anxious *because*",
 "anxious despite your holding. You are anxious *because*"),
("is **performative stillness** — the belief that good holding looks calm.",
 "is **performative stillness**, the belief that good holding looks calm."),
("an active, energetic practice — it requires as much charge as the field itself.",
 "an active, energetic practice. It requires as much charge as the field itself."),
("does not sit passive — it forms the active structure",
 "does not sit passive. It forms the active structure"),
("is **presence collapse** — the behavioral pattern of disappearing",
 "is **presence collapse**, the behavioral pattern of disappearing"),
("not to make it better — but to be the presence that makes it possible",
 "not to make it better. To be the presence that makes it possible"),
("the Diplomat's deepest channel — the work of healing ruptures",
 "the Diplomat's deepest channel: the work of healing ruptures"),
("a kind of relational brittleness — people who stay together but never recover",
 "a kind of relational brittleness. People stay together and never recover"),
("before it has been cleaned — they say *it's fine, let's move on, I forgive you* — and in fact",
 "before it has been cleaned. They say *it's fine, let's move on, I forgive you*, and in fact"),
("The Dissatisfaction here is **betrayal** — the specific pain",
 "The Dissatisfaction here is **betrayal**: the specific pain"),
("the reference point for real trust — not naive trust, not performance trust, but the kind of trust that has been tested and has survived.",
 "the reference point for real trust, not naive trust, not performance trust, but the kind that has been tested and survived."),
("does not disqualify you from repair — it qualifies you",
 "does not disqualify you from repair. It qualifies you"),
("is **performance forgiveness** — the rush to be done with the wound",
 "is **performance forgiveness**, the rush to be done with the wound"),
("I do not forgive to keep the peace — I repair to restore the relationship.",
 "I do not forgive to keep the peace. I repair to restore the relationship."),
("is **premature closure** — the behavioral pattern of rushing to close",
 "is **premature closure**: the behavioral pattern of rushing to close"),
("(1) **Witness** — the full accounting", "(1) **Witness:** the full accounting"),
("(2) **Impact** — the honest naming", "(2) **Impact:** the honest naming"),
("(3) **Agreement** — what each person commits", "(3) **Agreement:** what each person commits"),
("sit in a wound until it heals — not to minimize it,", "sit in a wound until it heals, not to minimize it,"),
("the Diplomat's closing channel — the Fire/Anger application",
 "the Diplomat's closing channel, the Fire/Anger application"),
("hold, repair — and then **negotiate**.", "hold, repair, and then **negotiate**."),
("because closing feels like conflict — who treats every hard question",
 "because closing feels like conflict, who treats every hard question"),
("is **endless process** — the Diplomat who has confused hearing with closing.",
 "is **endless process**, the Diplomat who has confused hearing with closing."),
("**ultimatum dressed as negotiation** — leverage where integration belonged.",
 "**ultimatum dressed as negotiation**: leverage where integration belonged."),
("has skipped the native work — surfacing interests, finding terms — and imported",
 "has skipped the native work (surfacing interests, finding terms) and imported"),
("is **resentful peace** — the accommodation that says yes",
 "is **resentful peace**, the accommodation that says yes"),
("for my staying to remain real — for everyone's staying to remain real.*",
 "for my staying to remain real, and for everyone's.*"),
("sits as heaviness — a pleasant surface with something dense underneath.",
 "sits as heaviness, a pleasant surface with something dense underneath."),
("feel like heat with ground — your chest engages,", "feel like heat with ground: your chest engages,"),
("is **positional stuckness** — camps locked on what they demand,",
 "is **positional stuckness**, camps locked on what they demand,"),
("the whole field can live with — including the terms that let you stay",
 "the whole field can live with, including the terms that let you stay"),
("is **endless process** — the behavioral habit of extending conversation",
 "is **endless process**, the behavioral habit of extending conversation"),
("for everyone to feel heard — as if hearing were the destination",
 "for everyone to feel heard, as if hearing were the destination"),
("(1) **Protect** — what is each party afraid of losing?", "(1) **Protect:** what is each party afraid of losing?"),
("(2) **Require** — what must the agreement hold", "(2) **Require:** what must the agreement hold"),
("(3) **Commit** — what are we agreeing to,", "(3) **Commit:** what are we agreeing to,"),
("is **false closure** — the agreement that sounds resolved but wasn't.",
 "is **false closure**, the agreement that sounds resolved but wasn't."),
("lives inside the Fire channel — not as a separate performance of righteousness,",
 "lives inside the Fire channel, not as a separate performance of righteousness,"),
("what each party actually needs — or on terms that pretend",
 "what each party actually needs, or on terms that pretend"),
("actually address those interests — or are we papering over a gap?*",
 "actually address those interests, or are we papering over a gap?*"),
("*When negotiation fails — when someone refuses to name stakes,",
 "*When negotiation fails, when someone refuses to name stakes,"),
("when the field cannot hold truth — the Challenger's clean no",
 "when the field cannot hold truth, the Challenger's clean no"),
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
            t = t.replace(a, b, 1)
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for n, a in bad:
            print("  %d matches: %r" % (n, a))
        return 1
    if not dry:
        io.open(P, "w", encoding="utf-8").write(t)
    print("%s %d edits" % ("would apply" if dry else "applied", len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
