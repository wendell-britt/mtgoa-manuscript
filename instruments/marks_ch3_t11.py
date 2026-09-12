# -*- coding: utf-8 -*-
"""marks_ch3_t11 -- proof marks, ch3 pp.86-90 and pp.94-95 (Moves 3-5, Where You'll Spend the
Read, How to Say It, the domain markers, the Tell, the recap), every entry changed
(2026-09-09). The pp.91-94 marks are the card apparatus and are removed by the card cut
(order item 4), not reworked here. Same rule and contract as marks_ch2_t1.py.
    python3 instruments/marks_ch3_t11.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

RECAP_OLD = ("The chapter leaves you holding a practice whose parts fit together. Your body registers a situation before your mind has finished making sense of it, the entire reason the read is worth anything, since it arrives early, and early is the only window in which it can change what happens. Wake → Open → Clean → Grow → Show carries a charge from arrival to a move, and Clean is the stage almost everyone skips, because locating a feeling and letting it settle takes longer than converting it into something useful. The five channels (Metal/Fear, Water/Sadness, Wood/Joy, Fire/Anger, Earth/Neutrality) tell you which teaching a given charge carries, since fear at the edge of what matters to you and anger at a line getting crossed are different instruments asking for different moves. The energy ecology tells you afterward which moves replenished you, which sustained the field, and which spent capacity you were going to need next week. 3-2-1 is here by name and in practice (Face it, Talk to it, Be it), and it runs again in every chapter after this one, and the Polarity Map is here by name as well, drawn again in every chapter after this one: two legitimate poles, your position on the axis, one action containing both. Feeling ↔ Function is the axis this chapter itself sits on, the reason you got a polarity rather than a rule. The Controller up close is the referee that holds your integrity when holding it costs you, the judge that rules your read out of order before it can be spoken, the six beliefs it rules with, the six developmental beliefs that go in where a flat inversion only re-enters the court, and what separates the referee from the judge: whose rulebook it enforces. The read leaves your body across four domains, and how you carry it is the difference between a true sentence that helps and one that only lands: stay with the reaction, say it as your own, don't leave. The five game moves are all of it compressed into what a person actually does at a table: Catch It Before the Story, Turn the Dial Up, Name the Channel Out Loud, Say What You Can Do Now, Say the Unsaid Charge.")
RECAP_NEW = ("The chapter leaves you holding a practice whose parts fit together. Your body registers a situation before your mind has finished making sense of it, which is the only reason the reading is worth anything: it arrives early, in the one window where it can still change what happens. The Form carries a charge from arrival to a move. The five channels tell you which lesson a charge carries. The energy ecology tells you afterward what a move cost and what it gave back. The Controller decides whether the reading is allowed onto the field at all. The four domains are where the reading leaves your body, and the five game moves are what a person actually does with it at a table.")

P819_OLD = ("The read has four domains, and one cheap habit that is none of them. The cheap habit is the read you keep: you sense what moves, refine it, and never say it, your body never on the line. Reading under the surface is real skill, and it asks nothing of you, because no one ever has to watch you get it wrong. A louder version of the same safety runs alongside it. You do say something, but only the correct words, the ones no one can fault, and that is the awareness trap, the habit that swallowed the others because you can run it from the chair. Both keep it unsaid. The four domains are where it finally leaves: said to a face, said out loud instead of the correct version, named as a need and asked for, put on the table so a group can work. Each costs more than sensing, because each trades the safety of the accurate private read for the risk of getting it wrong out loud.")
P819_NEW = ("The read has four domains and two cheap habits that are neither. The first is the reading you keep: you sense what moves, refine it, never say it, your body never on the line. Reading under the surface is real skill. It asks nothing of you, because no one has to watch you get it wrong. The second is louder. You do say something, but only the correct words, the ones no one can fault. That is the awareness trap, the habit that swallowed the rest because you can run it from the chair. Both leave the reading unsaid. The four domains are where it finally goes: to a face; out loud instead of the correct version; named as a need and asked for; onto the table so a group can work. Each costs more than sensing. Each trades the safety of an accurate private reading for the risk of getting it wrong out loud.")

EDITS = [
# p.86
("You are saying what the field runs, which hands everybody",
 "You are reporting what the field is doing, which hands everybody"),
("The euphemisms exist to keep the channel deniable, and nobody can work a deniable channel, including you.",
 "The euphemisms exist to keep the channel deniable. Nobody can work a deniable channel, including you."),
("got told it was fine, and you can name two other times that happened to him and to nobody else.",
 "got told it was fine. You can name two other times that happened to him and to nobody else."),
("What you feel is fear, because saying it means saying something about this team out loud. That is Metal.",
 "What you feel is fear, Metal, because saying it means saying something about this team out loud."),
("and I would like to know why that landed differently.*",
 "and I would like to know why that was received differently.*"),
("**What it is:** After the read lands, name the capability it left behind.",
 "**What it is:** After the reading, name the capability it left behind."),
("A read you understand and then set down leaves you where you started",
 "A reading you understand and then set down leaves you where you started"),
("Anger that showed you a line becomes a line you are allowed to have.",
 "Anger that showed you a line becomes a line you may hold."),
# p.87
("You were right, and being right bought her nothing.",
 "You were right. Being right bought her nothing."),
("What she does with it is hers, including nothing.",
 "What she does with it, including nothing, is hers."),
("it has not landed yet.",
 "it has not taken yet."),
("This is the Shaman's steepest move, the one the entire chapter exists to make possible.",
 "The entire chapter exists to make this move possible."),
("Every conversation has a stated content and an actual one. The stated content is the agenda item, the disagreement, the plan. The actual one is what",
 "Every conversation carries two contents. The stated one is the agenda item, the disagreement, the plan. The actual one is what"),
("nobody stated it, and stating it draws a line.",
 "nobody stated it; stating it draws a line."),
("One of them creates a boundary. The other creates contact.",
 "One creates a boundary; the other creates contact."),
# p.88
("A read usually runs one clause long.",
 "A reading is usually one clause long."),
("What extends it: the case you build so that nobody can argue with you, and the case is where the read goes to die, because a case invites a rebuttal and a read invites a response.",
 "What extends it is the case you build so that nobody can argue with you. The case is where the reading goes to die: a case invites a rebuttal, a reading invites a response."),
("You reach for the category instead of the person, and that kills a read faster than any case:",
 "You reach for the category instead of the person, which kills a reading faster than any case:"),
("Name a system and nobody has to answer you.",
 "Name a system and nobody has to answer."),
("Two colleagues have restated the same scoping position four times.",
 "Two colleagues have repeated the same scoping position four times."),
("She did not come up through the graduate scheme and everyone else did, and the shorthand on the call belongs to the scheme.",
 "She did not come up through the graduate scheme and everyone else did. The shorthand on the call belongs to the scheme."),
("One sentence, and nothing about who is right.",
 "One sentence, with nothing in it about who is right."),
("You said the read you actually had, and you said it while it was still live.",
 "You said the reading you actually had, while it was still live."),
("That is the Shaman's game. Five moves. Catch it before the story rewrites it. Turn the dial up instead of down. Name the channel out loud. Say what you can do now. Say the unsaid charge.",
 "The Shaman's game is five moves: catch it before the story rewrites it, turn the dial up instead of down, name the channel out loud, say what you can do now, say the unsaid charge."),
("The parable showed one of the four: Direct Action, said to a face.",
 "The parable showed one of the four, Direct Action: said to a face."),
(P819_OLD, P819_NEW),
("So here are all four, and before them the three moves that decide whether saying it helps or wounds.",
 "Here are all four, after the three moves that decide whether saying it helps or wounds."),
("pick where you'll spend the read this week,",
 "pick where you'll say it this week,"),
("you never made the Shaman's move. You practiced it.",
 "you practiced the Shaman's move without making it."),
# p.89
("whether it helps the person or wounds them, and the same three moves decide it in every domain.",
 "whether it helps the person or wounds them. The same three moves decide it in every domain."),
("You say it and the read tells you it landed: they get defensive,",
 "You say it and the reaction comes: they get defensive,"),
("Let the reaction be there, and stay in it with them instead of smoothing it flat.",
 "Let the reaction be there. Stay in it with them instead of smoothing it flat."),
("\"What's really going on here is…\" is the judge handing down a verdict from above, something to defend against.",
 "\"What's really going on here is…\" comes down from the bench, a verdict to defend against."),
("\"This is what I feel is happening, and I could be wrong\" is the same read offered as your own,",
 "\"This is what I feel is happening\" is the same reading offered as your own,"),
("The riskiest second comes right after the words are out, when the fear grabs for the exit:",
 "Right after the words are out comes the riskiest second, when the fear grabs for the exit:"),
# p.90
("in a message you draft and never send, and it cost you the safety of being the one who never breaks the surface.",
 "in a message you draft and never send. It cost you the safety of being the one who never breaks the surface."),
("the real ask and not the palatable one you were already sure would be granted, and you asked the person who can grant it or refuse it.",
 "the real ask rather than the palatable one you were already sure would be granted. You asked the person who can grant it or refuse it."),
("not one of them is worth anything built on a bad read.",
 "none of them holds up on a bad reading."),
("The read comes first, and a read that never leaves the chair stalls the whole game.",
 "The reading comes first. A reading that never leaves the chair stalls the whole game."),
# p.91
("None of the four markers asked why you said it. That question is real. A Shaman",
 "None of the four markers asked why you said it. A Shaman"),
# p.94
("**before strategy, before structure, before any move you make in the world, there is pattern.**",
 "**before any move you make in the world, there is pattern.**"),
("the part that doubts your own knowing before anyone else can, and the next face begins there.",
 "the part that doubts your own knowing before anyone else can. The next face begins there."),
("then the Challenger's line is performance. It's strategy without root.",
 "then the Challenger's line is performance, strategy without root."),
# p.95
(RECAP_OLD, RECAP_NEW),
("Underneath every part of it is the Alchemist: the willingness to spend a charge while it is still live, instead of waiting for the conditions that never arrive.",
 "Underneath every part of it is the Alchemist, who spends a charge while it is still live instead of waiting for conditions that never arrive."),
("The system did not give you your superpower. Your specific survival shaped it,",
 "Your specific survival shaped your superpower,"),
("All five ran through this chapter. One of them you left early.",
 "One of the five you left early."),
]

def main():
    t = io.open(P, encoding="utf-8").read()
    for old, new in EDITS:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("EDIT matched %d times (need 1): %r\n" % (c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch3 tranche 11: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
