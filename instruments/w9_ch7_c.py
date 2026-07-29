# -*- coding: utf-8 -*-
"""
W9 — ch7 em-dash pass, batch C (Sections 5-7, the moves and the recap).

One family here gets a deliberate pattern rather than a mix, because the pattern
carries meaning: the four `Working vs. performed` pairs. In each, the working
half takes a colon (the gloss defines what working looks like) and the performed
half takes a full stop (the gloss is a separate, damning sentence). Same mark,
same job, four times — that is parallelism, not a tic.

Three denials come out with their dashes, because the dash was the only thing
holding them up: *is not relativism — this is*, *is not inclusion — it is*, and
*is not connection — it is*.

Left alone: the `[[TESTIMONY SLOT — WENDELL` marker at L359. That is an
editorial note to the author, not prose, and it leaves with the slot.

    python3 instruments/w9_ch7_c.py --dry
    python3 instruments/w9_ch7_c.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch7.md")

EDITS = [
("possible, and closing — heard *and* something moves.",
 "possible, and closing so that everyone is heard *and* something moves."),
("the capacity to close — to surface what everyone is protecting,",
 "the capacity to close: to surface what everyone is protecting,"),
("becomes — structurally, not intentionally, and this is the part that is hard to look at — a claimant against the same fund.",
 "becomes, structurally and not intentionally, a claimant against the same fund. That is the part that is hard to look at."),
("for you to have caused harm — and a part of you that cannot afford a finding",
 "for you to have caused harm, and a part of you that cannot afford a finding"),
("the number says this is impossible — look at what I have absorbed,",
 "the number says this is impossible: look at what I have absorbed,"),
("to the field rather than about it — and then the field takes its turn.",
 "to the field rather than about it, and then the field takes its turn."),
("what surfaces is not a defence — a defence you would catch.",
 "what surfaces is not a defence. A defence you would catch."),
("here is what it cost you* — with your own column left closed,",
 "here is what it cost you*, with your own column left closed,"),
("Care without impact is attendance — warm, reliable, and doing nothing.",
 "Care without impact is attendance: warm, reliable, and doing nothing."),
("being converted into cost — whether anything anyone says",
 "being converted into cost, whether anything anyone says"),
("the sequence, not the verdict — that is why the app keeps count.",
 "the sequence, not the verdict. That is why the app keeps count."),
("manage one or the other — they either lose track of the cost",
 "manage one or the other. They either lose track of the cost"),
("closed with is not connection — it is attendance, and attendance",
 "closed with is attendance, and attendance"),
("make you a Diplomat in practice — the ones that show up",
 "make you a Diplomat in practice, the ones that show up"),
("a fight about recognition — about whose reality gets to count.",
 "a fight about recognition, about whose reality gets to count."),
("it might be about something else — about whether this team sees your concerns as real.",
 "it might be about something else: whether this team sees your concerns as real."),
("It makes an offering — you say *here is what I think is happening",
 "It makes an offering. You say *here is what I think is happening"),
("playing at the wrong level — arguing about content", "playing at the wrong level, arguing about content"),
("a quality of clearing — the conversation gets simpler", "a quality of clearing: the conversation gets simpler"),
("a quality of positioning — you're naming the field", "a quality of positioning. You're naming the field"),
("Summarizing is compression — you take the essence", "Summarizing is compression: you take the essence"),
("Translating is conversion — you take the meaning", "Translating is conversion: you take the meaning"),
("questioning our authority\"* — and respond defensively", "questioning our authority\"*, and respond defensively"),
("what [Camp A] is actually saying — not a challenge to their authority,",
 "what [Camp A] is actually saying, not a challenge to their authority,"),
("you're not translating — you're performing translation.",
 "you're not translating. You're performing translation."),
("a quality of lightness — meaning flows between frameworks", "a quality of lightness: meaning flows between frameworks"),
("a quality of cleverness — you're showing how smart you are", "a quality of cleverness. You're showing how smart you are"),
("*Prerequisite: Moves 1 and 2 — you cannot close on a field",
 "*Prerequisite: Moves 1 and 2. You cannot close on a field"),
("Bridge, translate, hold, repair — and then this.", "Bridge, translate, hold, repair, and then this."),
("in this partnership except one thing — if we get to a place",
 "in this partnership except one thing. If we get to a place"),
("an offering of information — here is what this field must hold for my staying to remain real — and then the field gets to respond.",
 "an offering of information: here is what this field must hold for my staying to remain real. Then the field gets to respond."),
("where you actually stand — whether you've been trading impact away for the comfort of caring — go back to",
 "where you stand, whether you've been trading impact away for the comfort of caring, go back to"),
("reach to fill the silence — you've said the thing,", "reach to fill the silence. You've said the thing,"),
("*Prerequisite: some real trust has been built — this move requires a history*",
 "*Prerequisite: some real trust has been built. This move requires a history*"),
("When trust breaks — and it will — the Diplomat has a specific structure",
 "When trust breaks, and it will, the Diplomat has a specific structure"),
("the instinct is to leave — to give them space,", "the instinct is to leave: to give them space,"),
("does not undo the break — it proves that the relationship can survive the break, the only thing that actually builds confidence",
 "does not undo the break. It proves that the relationship can survive the break, the only thing that builds confidence"),
("a quality of ground underneath — the floor was always there", "a quality of ground underneath: the floor was always there"),
("a quality of urgency — you want the discomfort to end", "a quality of urgency. You want the discomfort to end"),
("Say so — clearly, without apology, and without pretending your refusal is neutral when it is actually a position.",
 "Say so, clearly, without apology, and without pretending your refusal is neutral when it is a position."),
("as equally valid — where *making space* becomes", "as equally valid, where *making space* becomes"),
("This is not relativism — this is the basic work of the Diplomat's altitude,",
 "Relativism is the easy misreading. This is the basic work of the Diplomat's altitude,"),
("as if they were equally valid is not inclusion — it is a failure of discernment",
 "as if they were equally valid is a failure of discernment"),
("closer to what you consider true — without invalidating the people",
 "closer to what you consider true, without invalidating the people"),
("If the answer is no — if you've done the work of understanding the other position and it still doesn't hold — then Refuse",
 "If the answer is no, if you've done the work of understanding the other position and it still doesn't hold, then Refuse"),
("a quality of clarity — you've said the hard true thing", "a quality of clarity: you've said the hard true thing"),
("a quality of certainty — you're more interested in being right", "a quality of certainty. You're more interested in being right"),
("capacity for all five at once — naming the field while translating",
 "capacity for all five at once: naming the field while translating"),
("daemon exists to prevent — receiving what something costs somebody else",
 "daemon exists to prevent: receiving what something costs somebody else"),
("the hundred and twenty — though not from a single row.",
 "the hundred and twenty, though not from a single row."),
("**What This Costs the Teller** — Open Up, Raise Awareness, Diplomat.",
 "**What This Costs the Teller**: Open Up, Raise Awareness, Diplomat."),
("dynamic that was actually live — not the content, the standing.",
 "dynamic that was live, not the content but the standing."),
("will cost you the belonging — occasionally true, and not a reason.",
 "will cost you the belonging. Occasionally true, and not a reason."),
("each party protects and close — not as a threat, not as manipulation,",
 "each party protects and close, not as a threat, not as manipulation,"),
("- The Victim — the part that keeps an exact ledger — and what it is for",
 "- The Victim, the part that keeps an exact ledger, and what it is for"),
("Connector — connection that has survived being told the truth",
 "Connector, connection that has survived being told the truth"),
("tools are not enough — when one camp is playing a power game and the other is playing a harmony game and the conflict is actually altitudinal — who names that?**",
 "tools are not enough, when one camp is playing a power game and the other is playing a harmony game and the conflict is altitudinal, who names that?**"),
("**Next:** The Sage — the one who sees all six altitudes",
 "**Next:** The Sage, the one who sees all six altitudes"),
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
