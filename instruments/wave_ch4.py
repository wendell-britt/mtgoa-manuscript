# -*- coding: utf-8 -*-
"""
Restructure ch4's Section 6 onto the five WAVE stages, the way wave_ch3.py did ch3.

Target layout (specs/SPEC_WAVE_REALIGNMENT_2026-07-29.md §10, with one departure
recorded below):

  1 Wake  · Name the Unnameable        KEEP (was M1) + Example
  2 Open  · Take the Full Charge       NEW
  3 Clean · Confront Without Cruelty   RECAST (was M4) + Example
  4 Grow  · Find What You Keep Defending   NEW, approved 2026-07-29
  5 Show  · Draw the Line              KEEP (was M2) + Example

  RETIRE: Refuse Cleanly, Stay Past the Discomfort

**Departure from the spec, and why.** §10 had *Stay Past the Discomfort* keeping the
Open Up slot. Two things went wrong with that on the page:

  · Sequence. Its Situation beat opens "You've drawn the line," and Draw the Line is
    Move 5. A reader running the five in order hits the aftermath of a move two
    slots before the move.
  · Duplication. ch4:272 already teaches this as **Stage 4: Stand** — "You stay with
    what you said while the silence does its work" — and ch4:280 fixes its length at
    four seconds. The Move was the Stand stage under a second name, which is the
    exact bloat the ergonomics cuts exist to remove.

So Open Up gets a new Move instead. Its subject is Stage 1's own unpracticed claim
("The Challenger does not suppress it. The Challenger receives it") and the failure
the chapter already names at Stage 2 ("They feel the charge and act immediately").
That costs one more new Move than the spec budgeted and returns two duplicates.

ch3 gets one line fixed while we are here: its Section 6 framing still said "None of
them is a stage of the spiral wearing a new name," which the retagged headings now
contradict outright.

    python3 instruments/wave_ch4.py --dry
    python3 instruments/wave_ch4.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

MOVES = """### Move 1 · Wake Up — Name the Unnameable

**The Situation:** Someone says or does something. Everyone can feel it. Nobody names it.

**What it is:** You name it.

*We're not addressing the thing that just happened. I'd like to.*

The naming does the work. Most situations have a specific thing, a violation or a dismissal or a boundary crossed, that everyone has noticed and nobody has stated. You state it. You don't need a solution. You just need the thing to exist as a named reality.

**Why it matters:** Unnamed things feel larger than named things. Naming it reduces it. It demonstrates, for everyone watching, that the line exists.

In practice: Next time you're in a meeting and something happens that you can feel everyone noticing and nobody stating, that is your cue. State it. Plainly. *"That comment about X wasn't accurate. I want to note that before we move on."*

**Example:** A senior colleague says a contractor "isn't going to be here long enough to matter," and the contractor is on the call. Six people go quiet and the agenda moves on. What you say, forty seconds later, is *we skipped past something. Priya is on this call and that was about her.* No fix attached and no request. The cost of not saying it lands on her rather than on you. She works the next three weeks knowing the room heard it and let it stand. You don't know whether she wanted it named, and that is a real risk you are taking on her behalf. The alternative was six people agreeing by saying nothing, and she would have had to read that too.

**The test:** The thing is now named, stated plainly, in the moment, with no solution attached. What the group does with it next is the group's. The naming is the whole move.

---

### Move 2 · Open Up — Take the Full Charge

**The Situation:** The fire has arrived and you have not said anything yet. Two exits are open. You can spend it now, on the first sentence available, or you can talk it down to a size that would not embarrass you.

**What it is:** You take neither exit. You let the charge stay at the strength it arrived at, unspent, long enough to read what it is pointing at.

**Why it matters:** Aim runs on the charge at full size. Talk it down and you aim the smaller thing, which draws the line a mild irritation would draw, and that is a preference in a firmer voice. Spend it on arrival and you never aim at all, because the first sentence available is aimed at whoever is nearest and the fire is not reliably about them. Holding it unspent is uncomfortable in a specific way. The pressure does not arrive feeling like pressure. It feels like urgency, and urgency is the most convincing wrong reason to say something.

In practice: when the charge lands, start a clock instead of a sentence. Thirty seconds, and you may think about anything except what you are going to say. Where it sits in your body. How big it is. What it is pointing at. If the size drops while you are watching it, you did the talking down, and the reading you now have is a reading of the smaller thing.

**Example:** Your manager reassigns the project you built to somebody hired last month, and says so in a channel with forty people in it. The charge is at an eight. Two sentences arrive in the first three seconds and both are aimed at the new hire, who has done nothing. Thirty seconds of saying neither one, and the size holds, and what it points at moves: not the reassignment, which is a manager's call to make, but the forty people, and that you learned it the same way they did. That one is drawable. *I need to hear this kind of thing before the channel does.* Spending the eight in those first three seconds costs you the new hire for a year and leaves the line undrawn, because the sentence you would have said was about the wrong person.

**The test:** Thirty seconds passed, you said nothing, and the charge is the size it was. If it shrank, that is information about what you do with fire rather than a failed attempt. If you spent it, you will know, because the sentence was about a person instead of about a line.

---

### Move 3 · Clean Up — Confront Without Cruelty

**The Situation:** You have to say something hard to someone, and you have twenty minutes before you say it.

**What it is:** Name which channel you are carrying before you open your mouth. Fire or Water. A line was crossed, or something was lost. You are going to say the hard thing either way, and which one you are actually carrying decides what comes out.

**Why it matters:** Cruelty in a confrontation is rarely a decision. It is a mismatch. Anger delivered as anger lands hard and lands clean, because Fire is asking for agency and agency is something the other person can hand over. Hurt delivered as anger lands as an attack, and nothing they do can satisfy it, because Water wanted to be met and you asked to win instead. So they defend, you escalate, and afterward you cannot say what you were actually after. Naming the channel first does not soften the content. It aims it.

In practice: before the conversation, finish one of two sentences out loud. *A line was crossed and I want it to stop.* Or: *something was lost and I want you to know what it cost.* Say the truer one in the room, whichever it is. If it is the second, it is the harder sentence to get out of your mouth and the only one that can be answered.

**Example:** A colleague cut off a junior teammate twice in one review and you let both go. Walking to the conversation, the sentence that wants out is *you talk over people and it's arrogant.* Fire: a line was crossed, stop crossing it. Checked against the other sentence it does not hold up, because what is actually true is *Dara has not volunteered an idea since that meeting, I think you cost us her, and I mind.* Water. Say the second one and name the cost in the currency the room runs on, which is one person's ideas out of a pipeline that has six people in it. Your colleague does not defend, because a defence answers an accusation and Water made a report. Delivered as Fire, the same twenty minutes end with your colleague explaining the review process and Dara still saying nothing.

**The test:** You named the channel before you spoke, and the sentence in the room matched the one you named. The content did not get softer once the channel was named, which is how you know you used the naming to aim and not as an exit.

---

### Move 4 · Grow Up — Find What You Keep Defending

**The Situation:** You have drawn a few lines by now, and swallowed more than you drew. You have judged each one on its own.

**What it is:** Put the last five side by side. The ones you drew and the ones you let go. Find the thing all five have in common.

**Why it matters:** One line tells you almost nothing about yourself. You cannot tell from a single instance whether you met the thing in front of you or an old thing wearing today's clothes, and that question is what the whole chapter turns on. Five instances answer it, because lines cluster and the cluster has a subject. Somebody who draws every line around being talked over is protecting something different from somebody who draws every line around other people's workload. While the subject stays unnamed you draw when the trigger arrives. Named, you choose.

In practice: list five moments from the last month where a line was available. Four words each, no explanation. Then read the five together and say what they are all about.

**Example:** *Manager rewrote my summary. Colleague took the client call. Teammate presented my slide. Nobody credited the doc. My name came off the deck.* Separately, five ordinary irritations, four of which you let go. Together, they have one subject: attribution, the record of who did the thing. Knowing that changes the next month twice over. It tells you which fights are yours, and it tells you the four you swallowed were all the same fight.

**The test:** You can name the subject in one noun, and it surprises you a little. A subject you already knew is the story you tell about yourself rather than the pattern underneath it. If five moments give you five subjects, collect more moments instead of reaching for a tidier answer.

---

### Move 5 · Show Up — Draw the Line

**The Situation:** Someone is about to cross a line, or has just crossed one, or keeps crossing one.

**What it is:** State the line. State it without essay, without justification, without apology.

*I want to be direct: I'm not able to support this approach.*

*I won't be part of discussions that exclude X community.*

*This is where I need the line to be.*

**Why it matters:** Most people bury their lines in qualifiers. *"I don't know if this is the right time but I just wanted to maybe suggest that it might be worth considering..."* The line, buried in qualifiers, is not actually a line. The Challenger states the line cleanly, so clean it stands on its own.

In practice: When you feel yourself reaching for a qualifier, stop. Take the qualifier out. State the line. Hold it for one second longer than is comfortable. That's usually all it takes.

**Example:** A hiring panel is closing out a no on a candidate because she would not be a culture fit, and nobody has said what that means. The line: *I'm not able to support a no on culture fit unless somebody names the behaviour. Name it and I'll vote with you.* One sentence of line and one of offer, in front of five people who will remember which side you took. It costs you the next twenty minutes, which are now uncomfortable and were going to be efficient. The candidate gets a decision made on something a person can be wrong about out loud. The sentence does not argue that she should be hired. Drawing a line for somebody else means insisting on the standard rather than delivering the outcome, and confusing the two is how advocacy becomes speaking for a person who never asked you to.

**The test:** The line left your mouth without an essay, a justification, or an apology attached. Count the words afterward: more than you needed means you were explaining, whatever they did in response.
"""

START = "### Move 1: Name the Unnameable"
END = "\n\n---\n\n## Your Twenty Cards"

CH4_EDITS = [
    # The framing paragraph has to say what the five are now, because the headings do.
    ("The Challenger's game has five concrete moves. You can use them today.",
     "The Challenger's game has five concrete moves. They are the same five stages you "
     "ran with the Shaman, run at a table where the other person can answer back. You "
     "can use them today."),
    # The recap names the retired pair. Also two em-dashes out, since the budget only
    # ever ratchets down and this line was carrying a pair it did not need.
    ("The five game moves — Name the Unnameable, Draw the Line, Refuse Cleanly, "
     "Confront Without Cruelty, Stay Past the Discomfort — compress all of it into "
     "what a person actually does at a table.",
     "The five game moves (Name the Unnameable, Take the Full Charge, Confront Without "
     "Cruelty, Find What You Keep Defending, Draw the Line) compress all of it into "
     "what a person actually does at a table, in the order the spiral runs."),
    # Same trade in the Twenty Cards paragraph: a parenthetical that was set with dashes.
    ("Five basic moves down — the WAVE-Spiral, which you have been running since "
     "Chapter 3 — four domains across, twenty cards.",
     "Five basic moves down (the WAVE-Spiral, which you have been running since "
     "Chapter 3), four domains across, twenty cards."),
]

CH3_EDITS = [
    ("None of them is a stage of the spiral wearing a new name. The spiral gets you "
     "the read. These five are what the read costs.",
     "They run in the spiral's order, because the spiral is the order: you catch the "
     "signal, you let it up, you name the channel, you find what it grew, you spend "
     "it. Section 4 taught you to run that alone. These five are what it costs to run "
     "it where somebody is watching."),
]


def edit(name, t, edits):
    """Every anchor must match exactly once. Nothing reaches disk otherwise."""
    for i, (a, b) in enumerate(edits, 1):
        n = t.count(a)
        if n != 1:
            raise SystemExit("%s edit #%d matched %d times: %r" % (name, i, n, a[:70]))
        t = t.replace(a, b, 1)
    return t


def main():
    dry = "--dry" in sys.argv
    p4 = os.path.join(MS, "ch4.md")
    p3 = os.path.join(MS, "ch3.md")

    t4 = io.open(p4, encoding="utf-8").read()
    i = t4.find(START)
    j = t4.find(END, i)
    if i < 0 or j < 0:
        raise SystemExit("ch4: could not bracket the Moves block")
    old = t4[i:j]
    for title in ("Refuse Cleanly", "Stay Past the Discomfort", "Confront Without Cruelty"):
        if title not in old:
            raise SystemExit("ch4: %r is not inside the block being replaced" % title)
    if "<!-- MARGINALIA" in old or "<!-- POSTCARD" in old or "<!-- EPIGRAPH" in old:
        raise SystemExit("ch4: a frame block sits inside the Moves region; strip first")

    t4 = edit("ch4", t4[:i] + MOVES.rstrip("\n") + t4[j:], CH4_EDITS)
    t3 = edit("ch3", io.open(p3, encoding="utf-8").read(), CH3_EDITS)

    if dry:
        print("ch4: block %d chars -> %d, plus %d anchored edits, all matched once"
              % (len(old), len(MOVES), len(CH4_EDITS)))
        print("ch3: %d anchored edit matched once" % len(CH3_EDITS))
        return 0

    io.open(p4, "w", encoding="utf-8").write(t4)
    io.open(p3, "w", encoding="utf-8").write(t3)
    print("ch4: 5 Moves retagged to WAVE, 2 retired (Refuse Cleanly, Stay Past the "
          "Discomfort), 2 new (Take the Full Charge, Find What You Keep Defending)")
    print("ch4: %d chars out, %d in" % (len(old), len(MOVES)))
    print("ch3: Section 6 framing no longer contradicts the retagged headings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
