# -*- coding: utf-8 -*-
"""
W9, finished: ch5's 85 prose em-dashes.

One family, per 095a1ed's method: the five `Inherit — Honor — Steward — Reform —
Entrust` glosses in the family-pattern paragraph take one ruling between them, a colon.

Two of these sites are sentences written earlier tonight, in the narrated-reader-history
commit. `Every family runs a pattern — around money...` came in with a dash and goes
out without one, which is the ratchet doing its job on the same day rather than a
month later.

  23 colon  ·  46 comma  ·  12 parenthesis (six pairs)  ·  4 full stop
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # -- the family: five stage glosses, one ruling ------------------------------
    ("The Regent asks you to: Inherit — *this is what came to me.* Honor — *this part "
     "of how I was raised gave me something real.* Steward — *I'm going to tend this "
     "consciously even while I'm still angry about it.* Reform — *I'm going to stop "
     "passing the wound forward, and name it as a change rather than leaving it to not "
     "happen on its own.* Entrust — *I'm going to hand something different to the "
     "people who come after me.*",
     "The Regent asks you to: Inherit: *this is what came to me.* Honor: *this part "
     "of how I was raised gave me something real.* Steward: *I'm going to tend this "
     "consciously even while I'm still angry about it.* Reform: *I'm going to stop "
     "passing the wound forward, and name it as a change rather than leaving it to not "
     "happen on its own.* Entrust: *I'm going to hand something different to the "
     "people who come after me.*"),

    # -- parentheses -------------------------------------------------------------
    ("The ones who stayed learned to perform compliance — to say the words, wear the "
     "role, go through the motions — while everything alive inside them drained out",
     "The ones who stayed learned to perform compliance (to say the words, wear the "
     "role, go through the motions) while everything alive inside them drained out"),
    ("Without the Regent there to tend them — to ask, every time: *does this still "
     "serve the people inside it?* — the structures started to calcify.",
     "Without the Regent there to tend them (to ask, every time: *does this still "
     "serve the people inside it?*) the structures started to calcify."),
    ("The practices you inherited from the work — the frameworks, the vocabulary, the "
     "rituals someone before you built with real stakes — some of them are still "
     "load-bearing.",
     "The practices you inherited from the work (the frameworks, the vocabulary, the "
     "rituals someone before you built with real stakes): some of them are still "
     "load-bearing."),
    ("Real loyalty sees the whole inheritance — the gift and the damage — and decides, "
     "with full knowledge, to carry it forward.",
     "Real loyalty sees the whole inheritance (the gift and the damage) and decides, "
     "with full knowledge, to carry it forward."),
    ("The Regent's superpower puts what you received into a form the next person can "
     "receive — endurance and loyalty are the entry requirements — the account of "
     "where this came from",
     "The Regent's superpower puts what you received into a form the next person can "
     "receive (endurance and loyalty are the entry requirements): the account of "
     "where this came from"),
    ("Five moves down — the WAVE-Spiral — four domains across.",
     "Five moves down (the WAVE-Spiral), four domains across."),

    # -- parenthetical pairs taking commas ---------------------------------------
    ("The traditions — the ones that used to carry the village's actual values — "
     "became cargo cults.",
     "The traditions, the ones that used to carry the village's actual values, "
     "became cargo cults."),
    ("The Regent's mistake — the distortion that exiled them — confused stewardship "
     "with preservation.",
     "The Regent's mistake, the distortion that exiled them, confused stewardship "
     "with preservation."),

    # -- colon -------------------------------------------------------------------
    ("The Challenger didn't need to — the lines were drawn",
     "The Challenger didn't need to: the lines were drawn"),
    ("The Regent gave them identity — \"this is who we are",
     "The Regent gave them identity: \"this is who we are"),
    ("The weekly council isn't a bureaucratic obligation — it's a gift from every person",
     "The weekly council isn't a bureaucratic obligation: it's a gift from every person"),
    ("The roles aren't cages — they're inheritance.",
     "The roles aren't cages: they're inheritance."),
    ("A tradition that can't change is a tradition that has died — it's just still "
     "moving because nobody noticed.",
     "A tradition that can't change is a tradition that has died: it's just still "
     "moving because nobody noticed."),
    ("Martial arts, church, academia — all of them Regent organizations",
     "Martial arts, church, academia: all of them Regent organizations"),
    ("Caring for what exists begins as a surrender — you did not choose this.",
     "Caring for what exists begins as a surrender: you did not choose this."),
    ("Some of what you received is load-bearing — remove it and the whole structure "
     "collapses.",
     "Some of what you received is load-bearing: remove it and the whole structure "
     "collapses."),
    ("Every family runs a pattern — around money, around conflict, around who speaks "
     "and who stays silent.",
     "Every family runs a pattern: around money, around conflict, around who speaks "
     "and who stays silent."),
    ("Pick one inheritance you've already located — a practice, a norm, a role, a "
     "tradition you've been carrying without deciding about.",
     "Pick one inheritance you've already located: a practice, a norm, a role, a "
     "tradition you've been carrying without deciding about."),
    ("The Fixer-Healer makes that feel like the highest form of loyalty — pour "
     "yourself into the gap",
     "The Fixer-Healer makes that feel like the highest form of loyalty: pour "
     "yourself into the gap"),
    ("He is not wrong — he accurately notes that I could fail",
     "He is not wrong: he accurately notes that I could fail"),
    ("All of it, in detail — that is the report I want",
     "All of it, in detail: that is the report I want"),
    ("so the deadline is not a breath — it is a count.",
     "so the deadline is not a breath: it is a count."),
    ("Someone asks you to take the role — chair the meeting, hold the practice, put "
     "your name on it.",
     "Someone asks you to take the role: chair the meeting, hold the practice, put "
     "your name on it."),
    ("Take **Can You Hold the Whole** — Open Up, Skillful Organizing, Regent.",
     "Take **Can You Hold the Whole**: Open Up, Skillful Organizing, Regent."),
    ("The Regent's version runs slower than the others — give it the length of a walk",
     "The Regent's version runs slower than the others: give it the length of a walk"),

    # -- comma -------------------------------------------------------------------
    ("The Regent started to believe that the structure *was* the village — that if you "
     "kept the walls intact",
     "The Regent started to believe that the structure *was* the village, that if you "
     "kept the walls intact"),
    ("The Regent saw these as *maintenance problems* — things to fix with better systems",
     "The Regent saw these as *maintenance problems*, things to fix with better systems"),
    ("the Regent was gone — not exiled exactly, but *retired.*",
     "the Regent was gone, not exiled exactly, but *retired.*"),
    ("the person who knew how to tend them — who could tell the difference",
     "the person who knew how to tend them, who could tell the difference"),
    ("meant it as a defense — as if \"how we've always done it\"",
     "meant it as a defense, as if \"how we've always done it\""),
    ("the comfortable mechanical repetition of its form — and then calls that "
     "faithfulness.",
     "the comfortable mechanical repetition of its form, and then calls that "
     "faithfulness."),
    ("protected what they'd built — at the expense of the people who came after.",
     "protected what they'd built, at the expense of the people who came after."),
    ("the way a fire goes out when you stop feeding it — a gradual loss of heat rather "
     "than a catastrophe.",
     "the way a fire goes out when you stop feeding it, a gradual loss of heat rather "
     "than a catastrophe."),
    ("most energized at any given moment — and when those people left",
     "most energized at any given moment, and when those people left"),
    ("The Regent's gift passes something down — builds a thing bigger than any one "
     "person's presence in it",
     "The Regent's gift passes something down, builds a thing bigger than any one "
     "person's presence in it"),
    ("That treats a practice as a *relic* — preserved because it is old",
     "That treats a practice as a *relic*, preserved because it is old"),
    ("learned something through costly experience — through failure, through sadness",
     "learned something through costly experience, through failure, through sadness"),
    ("staying loyal to the inheritance — not because it's perfect",
     "staying loyal to the inheritance, not because it's perfect"),
    ("before you had any say in the matter — and that you've been carrying ever since",
     "before you had any say in the matter, and that you've been carrying ever since"),
    ("at the Regent's altitude is **loyalty** — the felt sense of belonging",
     "at the Regent's altitude is **loyalty**, the felt sense of belonging"),
    ("The village conflated loyalty with compliance — and then wondered why",
     "The village conflated loyalty with compliance, and then wondered why"),
    ("The mode of receiving — including receiving the damage.",
     "The mode of receiving, including receiving the damage."),
    ("Passing it forward requires vitality — the aliveness of knowing that what you "
     "carry matters.",
     "Passing it forward requires vitality, the aliveness of knowing that what you "
     "carry matters."),
    ("requires the fire of conviction — the willingness to say *this part no longer "
     "serves*",
     "requires the fire of conviction, the willingness to say *this part no longer "
     "serves*"),
    ("whether you can let go without abandoning — whether you can pass the tradition "
     "forward without clinging to it.",
     "whether you can let go without abandoning, whether you can pass the tradition "
     "forward without clinging to it."),
    ("The team has a culture — one you would not have built.",
     "The team has a culture, one you would not have built."),
    ("*I'm going to prepare the next person — not a replica of me",
     "*I'm going to prepare the next person, not a replica of me"),
    ("so this won't resolve this week — but it can *start* this week",
     "so this won't resolve this week, but it can *start* this week"),
    ("From outside, those look identical — until you leave",
     "From outside, those look identical, until you leave"),
    ("The Fixer-Healer ends the cycle between those two steps — not by arguing that "
     "the inheritance is bad",
     "The Fixer-Healer ends the cycle between those two steps, not by arguing that "
     "the inheritance is bad"),
    ("names the person doing all of it — because the job is a shape a body makes",
     "names the person doing all of it, because the job is a shape a body makes"),
    ("Look at the sequence, not the verdict — the pattern shows nowhere else",
     "Look at the sequence, not the verdict, the pattern shows nowhere else"),
    ("Most people manage one or the other — loyal and blind, or clear-eyed and "
     "uncommitted.",
     "Most people manage one or the other, loyal and blind, or clear-eyed and "
     "uncommitted."),
    ("Now — what does it actually look like in a real situation?",
     "Now, what does it actually look like in a real situation?"),
    ("a new team, a new responsibility — before you make a single change",
     "a new team, a new responsibility, before you make a single change"),
    ("The Regent's second move is discrimination — naming what would collapse if you "
     "removed it",
     "The Regent's second move is discrimination, naming what would collapse if you "
     "removed it"),
    ("what essential thing does this tradition try to do — and does the current form "
     "still do it?",
     "what essential thing does this tradition try to do, and does the current form "
     "still do it?"),
    ("Draw from your twenty rather than the hundred and twenty — though not all from "
     "one move.",
     "Draw from your twenty rather than the hundred and twenty, though not all from "
     "one move."),
    ("to put the second question underneath it — hold it how, and for how long after "
     "you are gone.",
     "to put the second question underneath it, hold it how, and for how long after "
     "you are gone."),
    ("name the capability the structure lacks — the structure, not you.",
     "name the capability the structure lacks, the structure, not you."),
    ("The village needed someone who could hold both — the love of what was handed "
     "down and the willingness to reform it.",
     "The village needed someone who could hold both, the love of what was handed "
     "down and the willingness to reform it."),
    ("The Architect has the Regent's stewardship in their blood — because the "
     "Architect knows",
     "The Architect has the Regent's stewardship in their blood, because the "
     "Architect knows"),

    # -- the tail found on the second sweep of the chapter -----------------------
    ("I'm not waiting until I'm sure I'm worthy of it — I'm taking it on now",
     "I'm not waiting until I'm sure I'm worthy of it. I'm taking it on now"),
    ("I'm not throwing it out — I'm naming that it needs to change",
     "I'm not throwing it out. I'm naming that it needs to change"),
    ("(That's the Fixer's whole racket — one more cycle of reform before you commit.",
     "(That's the Fixer's whole racket: one more cycle of reform before you commit."),
    ("Something you inherited is broken — an organization with a founding story that "
     "stopped being true",
     "Something you inherited is broken: an organization with a founding story that "
     "stopped being true"),
    ("Somebody repaired every tradition still worth having — noticed it failing",
     "Somebody repaired every tradition still worth having, noticed it failing"),
    ("There has to be — no inheritance ever arrives in working condition",
     "There has to be. No inheritance ever arrives in working condition"),
    ("A personally-held inheritance offers them competence instead — unwritten, "
     "undelegated, and available only while its carrier is.",
     "A personally-held inheritance offers them competence instead, unwritten, "
     "undelegated, and available only while its carrier is."),
    ("Everything else on that list follows from a thing never having been taken on — "
     "the damage inventory",
     "Everything else on that list follows from a thing never having been taken on: "
     "the damage inventory"),

    # -- full stop ---------------------------------------------------------------
    ("Not walls to keep people out — walls to hold what the village had agreed to.",
     "Not walls to keep people out. Walls to hold what the village had agreed to."),
    ("Not because they're perfect — because removing them would break something real.",
     "Not because they're perfect. Because removing them would break something real."),
]


def main():
    p = os.path.join(MS, "ch5.md")
    t = io.open(p, encoding="utf-8").read()
    bad = []
    for i, (old, new) in enumerate(E, 1):
        n = t.count(old)
        if n != 1:
            bad.append("#%d matched %d times: %r" % (i, n, old[:64]))
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
