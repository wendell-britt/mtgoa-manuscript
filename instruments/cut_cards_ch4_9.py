# -*- coding: utf-8 -*-
"""cut_cards_ch4_9 -- take the phantom deck out of ch4-ch8, and turn ch9's capstone from the
deck to the six quests and the sheet (2026-09-09).

Wendell: "the 20 cards is full nonsense. There aren't cards." Then: "the 20 moves in each
chapter should probably leave the book entirely." The 6-GM panel (Round 1, Q5; Round 2)
ruled: the deck was a generator the author wrote with, not an artifact the reader holds; the
job it did -- one practiced move per Face -- is already done by the quest. Strip the product,
keep the practice.

Per Face chapter, the "Your Twenty Cards" section becomes "The [Face] Is a Move You Run":
the five-failures teaching stays (a daemon is a rule in force at every move), the guided
pass stays as one pass of the Form, the quest stays, and every card / deck / grid / draw /
operation / "twenty" reference goes. Nothing is crossed against the four domains any more.
ch9's four deck passages are rewritten around what the reader actually made.

Every edit is (old, new), asserted to match exactly once in its chapter.
    python3 instruments/cut_cards_ch4_9.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

QUEST_OLD = ("### From Card to Quest\n\nA card that ends in a notebook is a card you read. A card that ends in a quest is a card you played. Quests come out of the Show Up cards, because those cards end in artifacts and an artifact is something another person can encounter.")
QUEST_NEW = ("### From Read to Quest\n\nA reading that ends in a notebook is a reading you had. A reading that ends in a quest is one you played. Quests come out of Show Up, because that move ends in an artifact, and an artifact is something another person can encounter.")
DEAL_OLD = "### Drawing Against the Shadow\n\nDraw from your twenty rather than the hundred and twenty, though not all from one move. "
DEAL_NEW = "### Where the Daemon Bites\n\n"
LIVE_OLD = "*Your twenty live in the deck rather than on this page: five basic moves against four domains, one card per crossing. You do not have to learn them. You have to find yours, and you already know the five moves that get you there.*\n\n"

def intro(face):
    return ("## The %s Is a Move You Run\n\nThe %s is a Face, but it is also a move you can run, which means you are not holding an archetype. You are holding a practice: the Five-Move Form"
            % (face, face))

EDITS = {
4: [
 ("## Your Twenty Cards\n\nSame grid as the Shaman's, one operation over. Five basic moves down (the Five-Move Form, which you have been running since Chapter 3), four domains across, twenty cards. These are the Challenger's.",
  intro("Challenger") + ", which you have been running since Chapter 3."),
 (LIVE_OLD, ""),
 ("Notice what happens as you go down the five. Wake Up names four cards you do not look at. Show Up names four that happen in front of other people. That is the Challenger's arc compressed into twenty phrases: it starts at what you refuse to see and ends at something you did with witnesses. Pick a domain instead and you choose the arena. Down is the sequence, across is where it lands.",
  "Notice what happens as you go down the five. Wake Up names what you refuse to see. Show Up names what you do in front of other people. That is the Challenger's arc: it starts at what you refuse to see and ends at something you did with witnesses."),
 (DEAL_OLD, DEAL_NEW),
 ("The other four rows run that same ruling early or late.",
  "The other four moves run that same ruling early or late."),
 ("Take **The Story About the Truth**: Clean Up, Raise Awareness, Challenger.",
  "Take the move called **The Story About the Truth**, the Challenger's version of Clean Up."),
 ("This card points the same instrument", "This move points the same instrument"),
 ("Show Up: pick a domain and name the intervention.", "Show Up: name the intervention."),
 ("Five moves, one card, ninety seconds.", "Five moves, one pass, ninety seconds."),
 (QUEST_OLD, QUEST_NEW),
 ("*Draw one from your twenty. Run the five moves on something live.", "*Run the five moves on something live."),
],
5: [
 ("## Your Twenty Cards\n\nSame grid, one operation further along. The five movements of the Five-Move Form run down, four domains across. Twenty cards, and these are the Regent's.",
  intro("Regent") + "'s five movements."),
 ("*Your twenty live in the deck rather than on this page: the five movements of the Five-Move Form against four domains, one card per crossing. You do not have to learn them. You have to find yours, and you already know the movements that get you there.*\n\n", ""),
 ("The Regent's Show Up cards are the only ones in the deck built entirely out of verbs for keeping",
  "The Regent's Show Up is the only one built entirely out of verbs for keeping"),
 ("and it makes this operation the slowest of the six. Read down for the sequence, across for the arena.",
  "and it makes this the slowest practice of the six."),
 (DEAL_OLD, DEAL_NEW),
 ("Take **Can You Hold the Whole**: Open Up, Skillful Organizing, Regent.",
  "Take the move called **Can You Hold the Whole**, the Regent's version of Open Up."),
 ("The card exists to slow that answer down", "The move exists to slow that answer down"),
 ("One pass through the Form, one card.", "One pass through the Form."),
 (QUEST_OLD, QUEST_NEW),
 ("*Draw one from your twenty. Run the Form on something live.", "*Run the Form on something live."),
],
6: [
 ("## Your Twenty Cards\n\nThe grid again, fourth operation of six. Five moves down, four domains across, twenty cards. These are the Architect's.",
  intro("Architect") + "."),
 (LIVE_OLD, ""),
 (" Every card at Show Up starts with the same verb. Pick a domain instead and you are choosing the arena. Down is the sequence, across is where it lands.", ""),
 (DEAL_OLD, DEAL_NEW),
 ("The four rows around it are what", "The four moves around it are what"),
 ("Take **Forge the Anger**: Clean Up, Direct Action, Architect. Sit with how uncomfortable it is that the card asks you to choose at all.",
  "Take the move called **Forge the Anger**, the Architect's version of Clean Up. Sit with how uncomfortable it is that the move asks you to choose at all."),
 ("The card's job is to make that choice", "The move's job is to make that choice"),
 ("Show Up: pick a domain and size the intervention", "Show Up: size the intervention"),
 ("Five moves, one card, ninety seconds, six of which", "Five moves, one pass, ninety seconds, six of which"),
 (QUEST_OLD, QUEST_NEW),
 ("*Draw one from your twenty. Run the five moves on something live.", "*Run the five moves on something live."),
],
7: [
 ("## Your Twenty Cards\n\nThe grid again, fifth operation of six. Five moves down, four domains across, twenty cards. These are the Diplomat's.",
  intro("Diplomat") + "."),
 (LIVE_OLD, ""),
 (" Pick a domain instead and you are choosing the arena. Down is the sequence, across is where it lands.", ""),
 (DEAL_OLD, DEAL_NEW),
 ("The other four rows are that settlement", "The other four moves are that settlement"),
 ("Take **What This Costs the Teller**: Open Up, Raise Awareness, Diplomat.",
  "Take the move called **What This Costs the Teller**, the Diplomat's version of Open Up."),
 ("Five moves, one card, ninety seconds. The Diplomat's version", "Five moves, one pass, ninety seconds. The Diplomat's version"),
 (QUEST_OLD, QUEST_NEW),
 ("*Draw one from your twenty. Run the five moves on something live.", "*Run the five moves on something live."),
],
8: [
 ("## Your Twenty Cards\n\nThe grid again, sixth operation of six, the last one. Five moves down, four domains across, twenty cards. These are the Sage's.",
  intro("Sage") + "."),
 (LIVE_OLD, ""),
 ("Grow Up is the only move in the deck that asks what the playing does to the player, and Show Up is legacy, and every card there names what remains once you stop holding it. Pick a domain and you're choosing the arena instead. Down is the sequence. Across is where it lands.",
  "Grow Up is the only move in the Form that asks what the playing does to the player, and Show Up is legacy: what remains once you stop holding it."),
 (DEAL_OLD, DEAL_NEW),
 ("It bites hardest in the Grow Up cards.", "It bites hardest at Grow Up."),
 ("The other four rows show that settlement", "The other four moves show that settlement"),
 ("Take **Who the Fight Makes You**: Grow Up, Direct Action, Sage.",
  "Take the move called **Who the Fight Makes You**, the Sage's version of Grow Up."),
 ("The card assumes the instrument works", "The move assumes the instrument works"),
 ("Show Up: pick a domain and name what you'd leave behind", "Show Up: name what you'd leave behind"),
 ("Five moves, one card, ninety seconds. The Sage's version", "Five moves, one pass, ninety seconds. The Sage's version"),
 (QUEST_OLD, QUEST_NEW),
 ("*Draw one from your twenty. Run the five moves on something live.", "*Run the five moves on something live."),
],
9: [
 ("The deck starts earning its keep here. You have been handed twenty cards six times in this book: the Shaman's twenty, then the Challenger's, the Regent's, the Architect's, the Diplomat's, the Sage's. A hundred and twenty cards. Five moves crossed against four domains, six operations deep. Nobody built that as a reference table. It works as the practice surface, and every chapter has pointed at its own twenty.",
  "The quests start earning their keep here. You have made one in each of the six Face chapters: the Shaman's, then the Challenger's, the Regent's, the Architect's, the Diplomat's, the Sage's. Six commitments with a name and a date in them, and a sheet with a row from every chapter. Nobody built that as a reference table. It is the practice surface, and every chapter has pointed at its own row."),
 ("The Elder's use of the deck comes second. The first one belongs to you, alone, with nobody watching: draw against the face you have been performing and find out what you actually do when a card names what you have been routing around.",
  "The Elder's use of the practice comes second. The first one belongs to you, alone, with nobody watching: run the five moves against the face you have been performing and find out what you actually do when the reading names what you have been routing around."),
 ("because a deck you actually play will keep dealing you the card you did not want.",
  "because a practice you actually run will keep handing you the move you did not want."),
 ("The deck runs underneath all five of them: whichever mode runs, the practice stays the same hundred and twenty cards. The mode only changes what you do with what the draw turns up.",
  "The five moves run underneath all five of them: whichever mode runs, the practice stays the same. The mode only changes what you do with what the reading turns up."),
 ("The deck is what you run the session from. It works without you standing in the middle of it, once you know it well enough to get out of the way.",
  "The five moves are what you run the session from. They work without you standing in the middle of them, once you know them well enough to get out of the way."),
 ("It is the mode the deck is worst at prompting on its own, so you draw for it on purpose.",
  "It is the mode the practice is worst at prompting on its own, so you run it on purpose."),
 ("The deck outlasts any single trip through it.", "The practice outlasts any single trip through it."),
 ("**The deck.** A hundred and twenty cards: Wake Up, Open Up, Clean Up, Grow Up, Show Up, crossed against gathering resources, raising awareness, direct action, and skillful organizing, run through all six operations, one per Face. You have met every one of them twenty at a time. The private use comes first: draw against the face you have been performing and see what you do when the card names it. The public use comes after: run it for a group. It is the smaller of the two steps and the only one you can take this week. It costs you nothing except the willingness to sit with a card you would rather have shuffled back.",
  "**The practice.** Five moves, Wake Up, Open Up, Clean Up, Grow Up, Show Up, run through all six Faces and out into the four domains, with a quest at the end of each chapter and a sheet that now has a row from every one. The private use comes first: run the moves against the face you have been performing and see what you do when the reading names it. The public use comes after: run them for a group. It is the smaller of the two steps and the only one you can take this week. It costs you nothing except the willingness to sit with a reading you would rather have set aside."),
 ("Start with the deck. It is the one that begins the moment you open the box.",
  "Start with the practice. It begins the moment you close this book."),
],
}

def main():
    for ch, edits in EDITS.items():
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        for old, new in edits:
            c = t.count(old)
            if c != 1:
                sys.stderr.write("ch%d: EDIT matched %d times (need 1): %r\n" % (ch, c, old[:70]))
                sys.exit(2)
            t = t.replace(old, new)
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: %d edits applied" % (ch, len(edits)))

if __name__ == "__main__":
    main()
