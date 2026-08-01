# -*- coding: utf-8 -*-
"""
W9, finished: ch4's 90 prose em-dashes.

Two families take one ruling each, per 095a1ed's method:

  the five modes    `1. **The Line** — A boundary stated.` and its four siblings
                    take the book's existing bold-label shape, `**The Line.** A
                    boundary stated.`, which ch5 already uses for Inherit/Honor/
                    Steward/Reform/Entrust.
  the 3-2-1 steps   `**1. STEP 3 — FACE IT (third person)**` and its two siblings
                    take a colon. These are labels rather than sentences, and the
                    dash in them is the same typography the heading rule exempts;
                    they are only in scope because the bold-label pattern in
                    emdash.py keys on an initial capital and these open with a digit.

The colon is rationed here. Converting every naming tail to one would have added
about forty colons to a chapter already at 12.8/1k, so wherever a cumulative comma
carried the sentence it took the comma instead.

  29 colon  ·  33 comma  ·  20 parenthesis (ten pairs)  ·  8 label/full stop
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # -- the two families --------------------------------------------------------
    ("1. **The Line** — A boundary stated.", "1. **The Line.** A boundary stated."),
    ("2. **The Interrupt** — Breaking a pattern mid-flight.",
     "2. **The Interrupt.** Breaking a pattern mid-flight."),
    ("3. **The Demand** — Insisting on something.",
     "3. **The Demand.** Insisting on something."),
    ("4. **The Refusal** — The clean no.", "4. **The Refusal.** The clean no."),
    ("5. **The Reckoning** — Naming the cost.",
     "5. **The Reckoning.** Naming the cost."),

    ("**1. STEP 3 — FACE IT (third person)**", "**1. STEP 3: FACE IT (third person)**"),
    ("**2. STEP 2 — TALK TO IT (second person)**",
     "**2. STEP 2: TALK TO IT (second person)**"),
    ("**3. STEP 1 — OWN IT (first person)**", "**3. STEP 1: OWN IT (first person)**"),

    # -- parentheses: a true aside with its own internal commas -------------------
    ("Not because the village didn't feel them — the village felt every one of them — "
     "but because",
     "Not because the village didn't feel them (the village felt every one of them) "
     "but because"),
    ("The Challenger's fire — the willingness to push back, to name, to stand — became "
     "something",
     "The Challenger's fire (the willingness to push back, to name, to stand) became "
     "something"),
    ("That the Challenger's gift — the willingness to be unwelcome in service of what "
     "is true — was draining away",
     "That the Challenger's gift (the willingness to be unwelcome in service of what "
     "is true) was draining away"),
    ("After the push — after you draw the line, make the demand, state the refusal — "
     "you rest.",
     "After the push (after you draw the line, make the demand, state the refusal), "
     "you rest."),
    ("Not to think clearly — that's the easy part — but to act.",
     "Not to think clearly (that's the easy part) but to act."),
    ("The five modes of confrontation — Line, Interrupt, Demand, Refusal, Reckoning — "
     "name the shape the fire arrives in",
     "The five modes of confrontation (Line, Interrupt, Demand, Refusal, Reckoning) "
     "name the shape the fire arrives in"),

    # -- parenthetical pairs that take commas, not brackets -----------------------
    ("without softening it — without the Challenger's willingness to be unwelcome in "
     "service of what was true — the village learned",
     "without softening it, without the Challenger's willingness to be unwelcome in "
     "service of what was true, the village learned"),
    ("The conclusion named a few pages back — that the clean no is what oppressors do "
     "— does not stay an idea.",
     "The conclusion named a few pages back, that the clean no is what oppressors do, "
     "does not stay an idea."),
    ("I say no because the line protects the work — and the people in it — from slow "
     "death by accommodation.",
     "I say no because the line protects the work, and the people in it, from slow "
     "death by accommodation."),

    # -- colon: the tail names, or the left side is a claim the tail unpacks ------
    ("Because the Regent was right — *power had to be organized.*",
     "Because the Regent was right: *power had to be organized.*"),
    ("The first is *the line itself* — what you will not do, will not accept, will not "
     "stand.",
     "The first is *the line itself*: what you will not do, will not accept, will not "
     "stand."),
    ("The second is *the delivery* — said plainly, without essay",
     "The second is *the delivery*: said plainly, without essay"),
    ("The third is *the cost* — what happens if someone crosses it.",
     "The third is *the cost*: what happens if someone crosses it."),
    ("Force without restraint is a hazard — every charge becomes a line",
     "Force without restraint is a hazard: every charge becomes a line"),
    ("Restraint has a vocabulary — discernment, deference, not centering yourself, "
     "waiting to be invited.",
     "Restraint has a vocabulary: discernment, deference, not centering yourself, "
     "waiting to be invited."),
    ("Not solo, not relational — pick a specific moment where a crossing happened",
     "Not solo, not relational: pick a specific moment where a crossing happened"),
    ("Not willpower, not determination — the raw energy of pushing back",
     "Not willpower, not determination: the raw energy of pushing back"),
    ("The Challenger uses them at a different altitude — not sensing inward but acting "
     "outward.",
     "The Challenger uses them at a different altitude: not sensing inward but acting "
     "outward."),
    ("That tidiness is no coincidence — it explains why the modes number five rather "
     "than three.",
     "That tidiness is no coincidence: it explains why the modes number five rather "
     "than three."),
    ("it does not wait for capitulation — the line does not need to win",
     "it does not wait for capitulation: the line does not need to win"),
    ("Not the hardest line you're avoiding — the next real one.",
     "Not the hardest line you're avoiding: the next real one."),
    ("This is the moment for the Reckoning. Not anger — *consequence.*",
     "This is the moment for the Reckoning. Not anger: *consequence.*"),
    ("Not a threat — a *foresight.*", "Not a threat: a *foresight.*"),
    ("The swallower learns the thing that is least true of all — that the standing to "
     "draw it was never theirs.",
     "The swallower learns the thing that is least true of all: that the standing to "
     "draw it was never theirs."),
    ("Real harm and real accountability stay real — 3-2-1 owns **your** split",
     "Real harm and real accountability stay real: 3-2-1 owns **your** split"),
    ("If the charge is trauma-level, pause — the appendix has the full process",
     "If the charge is trauma-level, pause: the appendix has the full process"),
    ("It is not the auditor — the auditor asks a question.",
     "It is not the auditor: the auditor asks a question."),
    ("and you would not want to — the memory is true.",
     "and you would not want to: the memory is true."),
    ("the auditor asks the single useful question — *is this the thing in front of me",
     "the auditor asks the single useful question: *is this the thing in front of me"),
    ("Charge, Aim, Act, Stand, Exit — the whole sequence assumes Stage 1 got "
     "permission to count.",
     "Charge, Aim, Act, Stand, Exit: the whole sequence assumes Stage 1 got "
     "permission to count."),
    ("or an old thing in its clothes — that question I want",
     "or an old thing in its clothes: that question I want"),
    ("Heat arrives in your chest — that is Charge, on time, doing its job.",
     "Heat arrives in your chest: that is Charge, on time, doing its job."),
    ("A Challenger who cannot restrain is a hazard — every charge becomes a line",
     "A Challenger who cannot restrain is a hazard: every charge becomes a line"),
    ("Take **The Story About the Truth** — Clean Up, Raise Awareness, Challenger.",
     "Take **The Story About the Truth**: Clean Up, Raise Awareness, Challenger."),
    ("The Regent does not draw the lines — the Regent builds what carries them forward.",
     "The Regent does not draw the lines: the Regent builds what carries them forward."),

    # -- comma: a modifier, a cumulative tail, or a clause joined by a conjunction -
    ("afraid of conflict the way a body becomes afraid of a low-grade fever — "
     "something to be suppressed rather than something to be read.",
     "afraid of conflict the way a body becomes afraid of a low-grade fever, "
     "something to be suppressed rather than something to be read."),
    ("The Challenger learned this the hard way — by watching boundaries dissolve",
     "The Challenger learned this the hard way, by watching boundaries dissolve"),
    ("**Force** means spending yourself on a crossing — saying the unwelcome sentence",
     "**Force** means spending yourself on a crossing, saying the unwelcome sentence"),
    ("Something in your body shows up — a heat in your chest, a clenching in your jaw",
     "Something in your body shows up, a heat in your chest, a clenching in your jaw"),
    ("Not the story — underneath the story.", "Not the story, underneath the story."),
    ("They feel the charge and act immediately — which leaves most confrontation "
     "messy, reactive, and apologetic.",
     "They feel the charge and act immediately, which leaves most confrontation "
     "messy, reactive, and apologetic."),
    ("a different animal entirely — sustained containment of a charged field",
     "a different animal entirely, sustained containment of a charged field"),
    ("Exit fails afterward — in the follow-up message, the hallway clarification",
     "Exit fails afterward, in the follow-up message, the hallway clarification"),
    ("The Refusal is the Demand turned inward — a line you draw against your own "
     "compliance.",
     "The Refusal is the Demand turned inward, a line you draw against your own "
     "compliance."),
    ("Then you repair — not apologize for, not soften, but *repair.*",
     "Then you repair, not apologize for, not soften, but *repair.*"),
    ("The Challenger lives in a rhythm — of fire, and rest, and repair, and fire again.",
     "The Challenger lives in a rhythm, of fire, and rest, and repair, and fire again."),
    ("into the Village this week — the meeting, the group chat, the dinner table",
     "into the Village this week, the meeting, the group chat, the dinner table"),
    ("Someone says something that crosses a line — not a catastrophic violation, but a "
     "real one.",
     "Someone says something that crosses a line, not a catastrophic violation, but a "
     "real one."),
    ("Let it arrive — the heat, the tightening.",
     "Let it arrive, the heat, the tightening."),
    ("Well-meaning people who had decided their perspective didn't belong in the "
     "conversation — keeping their mouths shut while the charge built.",
     "Well-meaning people who had decided their perspective didn't belong in the "
     "conversation, keeping their mouths shut while the charge built."),
    ("to find common ground — not to draw lines.*",
     "to find common ground, not to draw lines.*"),
    ("The Challenger developed uses no to protect — including, sometimes, to protect "
     "the person being told no.",
     "The Challenger developed uses no to protect, including, sometimes, to protect "
     "the person being told no."),
    ("Pick the figure you call \"oppressor energy\" — someone who draws lines, says no",
     "Pick the figure you call \"oppressor energy,\" someone who draws lines, says no"),
    ("This is the figure on the other side of the door — not the real person.",
     "This is the figure on the other side of the door, not the real person."),
    ("That's fuel returning — available for a clean line, not an explosion.",
     "That's fuel returning, available for a clean line, not an explosion."),
    ("Somewhere behind it sits a real occasion when pushing did cost something — a "
     "relationship that cooled, a table nobody invited you back to.",
     "Somewhere behind it sits a real occasion when pushing did cost something, a "
     "relationship that cooled, a table nobody invited you back to."),
    ("It lets you hold the fear without being the fear — the only condition under "
     "which you can aim.",
     "It lets you hold the fear without being the fear, the only condition under "
     "which you can aim."),
    ("The question changes shape without announcing that it has changed — from *is "
     "this real*",
     "The question changes shape without announcing that it has changed, from *is "
     "this real*"),
    ("the person who needed the line ends up somewhere nobody drew one — where the "
     "crossing went unremarked",
     "the person who needed the line ends up somewhere nobody drew one, where the "
     "crossing went unremarked"),
    ("closer to it than me* — and by the time the audit has finished",
     "closer to it than me*, and by the time the audit has finished"),
    ("Look at the sequence, not the verdict — the only place the pattern shows",
     "Look at the sequence, not the verdict, the only place the pattern shows"),
    ("Not to other people first — to yourself.",
     "Not to other people first, to yourself."),
    ("on a charge you have checked and chosen to trust — clarity without cruelty",
     "on a charge you have checked and chosen to trust, clarity without cruelty"),
    ("Now — what does it actually look like in a real situation?",
     "Now, what does it actually look like in a real situation?"),
    ("Draw from your twenty rather than the hundred and twenty — though not all from "
     "one move.",
     "Draw from your twenty rather than the hundred and twenty, though not all from "
     "one move."),
    ("write the story you believed as a flat sentence — *this is exaggerated",
     "write the story you believed as a flat sentence, *this is exaggerated"),
    ("has no standing until somebody ratifies it — and ratification does not arrive",
     "has no standing until somebody ratifies it, and ratification does not arrive"),
    ("the standing is the stage almost everyone collapses at — four seconds of not "
     "adding a sentence",
     "the standing is the stage almost everyone collapses at, four seconds of not "
     "adding a sentence"),
    ("Naming the voice puts a half step between you and the fear — the only condition "
     "under which aiming happens at all.",
     "Naming the voice puts a half step between you and the fear, the only condition "
     "under which aiming happens at all."),

    # -- full stop: two independent sentences ------------------------------------
    ("Not because allyship is about conflict — allyship means being present with "
     "people across power differentials.",
     "Not because allyship is about conflict. Allyship means being present with "
     "people across power differentials."),
    ("Not the idea of confrontation — the actual, specific, mechanical practice of it.",
     "Not the idea of confrontation. The actual, specific, mechanical practice of it."),
    ("*\"That framing isn't accurate — X community has specifically raised this "
     "concern and the data shows Y.\"*",
     "*\"That framing isn't accurate. X community has specifically raised this "
     "concern and the data shows Y.\"*"),
    ("Not who hurt you in history — the **figure** your nervous system built to hold "
     "everything you aren't allowed to be.",
     "Not who hurt you in history. The **figure** your nervous system built to hold "
     "everything you aren't allowed to be."),
]


def main():
    p = os.path.join(MS, "ch4.md")
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
