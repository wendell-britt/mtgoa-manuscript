# -*- coding: utf-8 -*-
"""
W9, finished: ch1's 58 prose em-dashes.

The pass 095a1ed ran on ch7 and ch3 and stopped. Wendell, 2026-07-31: *"it's weird
to start it and not finish it."* This is chapter one of the remaining seven.

Method is 095a1ed's, per SPEC_EMDASH_AND_DENSITY 1.4: every dash is asked what
decision it avoided, and the decision is made. Where a family of parallel sentences
shares a shape, the family takes ONE ruling, because that is what separates a figure
from a habit -- here that is the three `Where is it Chance / Skill / Passion` questions,
which all take a comma.

Counts for this chapter: 19 colon, 17 comma, 20 parenthesis (ten pairs), 2 full stop.

**Only two full stops in 58.** That is deliberate and it is the whole risk control.
1.4 warns that converting dashes to periods raises the <=6-word share, which is this
book's existing register defect. The tail of a single-tail dash in ch1 is almost never
an independent clause -- it is an appositive naming what came before -- so the honest
conversion is a colon or a comma, and the period is reserved for the two places where
two real sentences were being held together by a hyphen.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # -- the tail names what came before. Colon. --------------------------------
    ("This is me showing up — late, imperfect, and in the game.",
     "This is me showing up: late, imperfect, and in the game."),

    ("The part that runs on default did — inherited reflexes, old wounds, the face "
     "you reach for without checking whether it fits.",
     "The part that runs on default did: inherited reflexes, old wounds, the face "
     "you reach for without checking whether it fits."),

    ("you've been trying to pay down a debt you inherited — to restore something, to "
     "be the one whose effort finally offsets the damage.",
     "you've been trying to pay down a debt you inherited: to restore something, to "
     "be the one whose effort finally offsets the damage."),

    ("(Yu-kai Chou spent a decade mapping exactly this — why some fuel keeps a player "
     "in the game and some burns them out of it.)",
     "(Yu-kai Chou spent a decade mapping exactly this: why some fuel keeps a player "
     "in the game and some burns them out of it.)"),

    ("call it by its real name — engaging.",
     "call it by its real name: engaging."),

    ("Yu-kai Chou spent a decade mapping what actually keeps a human being playing — "
     "what pulls people back to some things for years and drives them out of others "
     "for good.",
     "Yu-kai Chou spent a decade mapping what actually keeps a human being playing: "
     "what pulls people back to some things for years and drives them out of others "
     "for good."),

    ("Some part of me was getting off on it — the martyrdom, the being-behind, the "
     "noble suffering of the ally who cares too much to finish.",
     "Some part of me was getting off on it: the martyrdom, the being-behind, the "
     "noble suffering of the ally who cares too much to finish."),

    ("A game turns it into the thing standing right beside it — wonder, the same "
     "charge, now pointed at the door instead of away from it.",
     "A game turns it into the thing standing right beside it: wonder, the same "
     "charge, now pointed at the door instead of away from it."),

    ("Everything ahead is built to strengthen your hand in all three — to keep you "
     "present for the breaks when they come",
     "Everything ahead is built to strengthen your hand in all three: to keep you "
     "present for the breaks when they come"),

    ("the week before she files — timing you never touched, three floors up, deciding "
     "everything.",
     "the week before she files: timing you never touched, three floors up, deciding "
     "everything."),

    ("That is why Chance pays the biggest of the three — jackpot money, the wins that "
     "reshape things.",
     "That is why Chance pays the biggest of the three: jackpot money, the wins that "
     "reshape things."),

    ("The payout is honest and proportional — you get back about what your skill "
     "earns, no jackpot, no leverage, a steady wage for competence.",
     "The payout is honest and proportional: you get back about what your skill "
     "earns, no jackpot, no leverage, a steady wage for competence."),

    ("Neither one survives on discipline alone — what keeps you at the machine through "
     "the dry spells is that some part of this you would do for love.",
     "Neither one survives on discipline alone: what keeps you at the machine through "
     "the dry spells is that some part of this you would do for love."),

    ("Each of them plays all three games you just met — a jackpot they chase, a "
     "signature skill, a reason they keep coming back.",
     "Each of them plays all three games you just met: a jackpot they chase, a "
     "signature skill, a reason they keep coming back."),

    ("turns into the thing you overplay — the Diplomat who keeps the peace until "
     "nothing gets decided, the Challenger who scorches the people he came to protect.",
     "turns into the thing you overplay: the Diplomat who keeps the peace until "
     "nothing gets decided, the Challenger who scorches the people he came to protect."),

    ("The app holds it better — it keeps the sheet somewhere you will actually find it",
     "The app holds it better: it keeps the sheet somewhere you will actually find it"),

    # Two independent clauses, and the full stop is refused on purpose. `You can't
    # fail me.` is four words and `You can only fail yourself.` is five; splitting
    # them would add two sentences to the <=6-word bucket in a single stroke.
    ("You can't fail me — you can only fail yourself.",
     "You can't fail me: you can only fail yourself."),

    ("Writing is not the issue — putting the thought, the feeling, the experience on a "
     "page is halfway to something.",
     "Writing is not the issue: putting the thought, the feeling, the experience on a "
     "page is halfway to something."),

    ("Captured charge — one moment of your own play, caught while the heat is still on "
     "it, carried where you can reach it instead of filed where you cannot.",
     "Captured charge: one moment of your own play, caught while the heat is still on "
     "it, carried where you can reach it instead of filed where you cannot."),

    # -- a modifier, an aside, or a second clause joined by a conjunction. Comma. --
    ("You have been running your own allyship campaign for years — whether you named "
     "it or not.",
     "You have been running your own allyship campaign for years, whether you named "
     "it or not."),

    ("this one has no final payment — no moment when someone hands you a receipt.",
     "this one has no final payment, no moment when someone hands you a receipt."),

    ("You are burned out from trying to retire a debt designed never to clear — and "
     "some part of you has started to wonder whether the game itself is the problem.",
     "You are burned out from trying to retire a debt designed never to clear, and "
     "some part of you has started to wonder whether the game itself is the problem."),

    ("Allyship looks like the honorable place to bring those questions — and springs "
     "the trap.",
     "Allyship looks like the honorable place to bring those questions, and springs "
     "the trap."),

    ("the part of your allyship you least want to see — and enjoy it.",
     "the part of your allyship you least want to see, and enjoy it."),

    ("Some part of you is delighted by the very thing you complain about — and as long "
     "as that delight stays in the dark, it owns you.",
     "Some part of you is delighted by the very thing you complain about, and as long "
     "as that delight stays in the dark, it owns you."),

    ("You were in the game, the only move Chance rewards — and the jackpot you are "
     "still there for is real.",
     "You were in the game, the only move Chance rewards, and the jackpot you are "
     "still there for is real."),

    # The family. Three parallel questions, one ruling, per the 095a1ed method.
    ("Where is it Chance — moving on its own clock, asking only that you stay in the "
     "game?",
     "Where is it Chance, moving on its own clock, asking only that you stay in the "
     "game?"),
    ("Where is it Skill — waiting for you to get better, and to carry that better to "
     "people who want it?",
     "Where is it Skill, waiting for you to get better, and to carry that better to "
     "people who want it?"),
    ("Where is it Passion — the part you would keep playing after every reasonable "
     "person told you to stop?",
     "Where is it Passion, the part you would keep playing after every reasonable "
     "person told you to stop?"),

    ("You have a home face — one you reach for without deciding to, one that feels "
     "like plain decency rather than a strategy.",
     "You have a home face, one you reach for without deciding to, one that feels "
     "like plain decency rather than a strategy."),

    # Inside an already-parenthesised sentence, so the pair takes commas rather than
    # a second set of brackets.
    ("that is one face's shadow — the Diplomat's — worn so long it stopped looking "
     "like a choice.",
     "that is one face's shadow, the Diplomat's, worn so long it stopped looking "
     "like a choice."),

    ("The reason to widen your range is the person in front of you — the one who "
     "needed a move you did not have.",
     "The reason to widen your range is the person in front of you, the one who "
     "needed a move you did not have."),

    ("This is your character sheet — a few lines, filled in for who you are right now.",
     "This is your character sheet, a few lines filled in for who you are right now."),

    ("The one you already play — the one you just recognized as yours.",
     "The one you already play, the one you just recognized as yours."),

    ("Write down the one that runs you hardest — the rule you have been playing by "
     "without ever agreeing to it.",
     "Write down the one that runs you hardest, the rule you have been playing by "
     "without ever agreeing to it."),

    # -- a true aside with its own internal commas. Parentheses. ------------------
    ("It wasn't until I gave myself permission to actually be mad — at myself, about "
     "the delay, about the gap between who I said I was and what I was doing — that I "
     "saw what was happening.",
     "It wasn't until I gave myself permission to actually be mad (at myself, about "
     "the delay, about the gap between who I said I was and what I was doing) that I "
     "saw what was happening."),

    ("You've been doing the evolved version — the relational, emotionally literate, "
     "I've-done-my-work version — long enough to know that more trying isn't the answer.",
     "You've been doing the evolved version (the relational, emotionally literate, "
     "I've-done-my-work version) long enough to know that more trying isn't the answer."),

    ("Most allyship is built as a chore — a duty, a debt, a weight good people carry — "
     "and it runs on the fuel we already named",
     "Most allyship is built as a chore (a duty, a debt, a weight good people carry), "
     "and it runs on the fuel we already named"),

    ("say so, and — this is the whole move — enjoy it on purpose instead of by accident.",
     "say so, and (this is the whole move) enjoy it on purpose instead of by accident."),

    ("It has chance and skill inside it — every Game of Passion does — but the payout "
     "is not why you are at the machine.",
     "It has chance and skill inside it (every Game of Passion does), but the payout "
     "is not why you are at the machine."),

    ("You care about everyone — you would say so, and mean it — and you run all of "
     "that care through one face",
     "You care about everyone (you would say so, and mean it), and you run all of "
     "that care through one face"),

    ("needs a Challenger — one clean, costly line — and all you have is the Diplomat",
     "needs a Challenger (one clean, costly line), and all you have is the Diplomat"),

    ("Every serious game keeps an oath — the scout's, the athlete's, the doctor's — "
     "and you say the words out loud",
     "Every serious game keeps an oath (the scout's, the athlete's, the doctor's), "
     "and you say the words out loud"),

    ("I have also sat on the other side of a book that hit me — more times than I can "
     "count — and I know what comes next",
     "I have also sat on the other side of a book that hit me (more times than I can "
     "count), and I know what comes next"),

    ("when something hit me — the kind of hit you know you will lose by morning — I "
     "wrote it on a card.",
     "when something hit me (the kind of hit you know you will lose by morning), I "
     "wrote it on a card."),

    # -- two genuinely independent sentences. Full stop. --------------------------
    # Both halves run long enough that the split does not feed the <=6-word bucket.
    ("Not to the people I was trying to serve — to myself, to the people closest to "
     "me, to the work itself.",
     "Not to the people I was trying to serve. To myself, to the people closest to "
     "me, to the work itself."),

    ("If that landed as an accusation, notice the flinch — that's the shadow guarding "
     "its stash.",
     "If that landed as an accusation, notice the flinch. That's the shadow guarding "
     "its stash."),
]


def main():
    p = os.path.join(MS, "ch1.md")
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
