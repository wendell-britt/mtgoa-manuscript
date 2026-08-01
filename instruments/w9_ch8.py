# -*- coding: utf-8 -*-
"""
W9, finished: ch8's 136 prose em-dashes.

**The plan recorded in the ch6 commit does not fit this chapter, and the data says
so.** That note said ch8 and ch9 would spend the full stop, because the <=6-word share
had slack book-wide. Per chapter it does not: ch8 sits at 28.7% and ch9 at 30.6%,
the two choppiest in the book against an average of 25.7. They are also the two
*least* colon-dense, at 10.8 and 7.5 against 12.4. So the marks invert here. The colon
is the one with room, and spending it also pulls the book's colon spread together
rather than further apart.

Two families take one ruling each, per 095a1ed's method:

  the five distortion labels  `**Panoramic Seer — *perspective as performance***`
                              and siblings take a colon. They are headings that the
                              bold-label rule misses because of the nested italics.
  the five channel tags       `*(Panoramic Seer — Metal/Fear)*` and siblings take a
                              comma. Same typography, and a colon inside a parenthetical
                              tag reads as a definition rather than a pairing.

  46 colon  ·  76 comma  ·  12 parenthesis (six pairs)  ·  2 full stop
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# The two families, generated so a sibling cannot drift from its siblings.
MODES = [("Panoramic Seer", "perspective as performance", "Metal/Fear"),
         ("Game-Switcher", "switching as inconsistency", "Fire/Anger"),
         ("Diagnostician", "naming as lecturing", "Earth/Neutrality"),
         ("Liberator", "putting down as giving up", "Wood/Joy"),
         ("Returner", "returning as retreating", "Water/Sadness")]

E = []
for name, gloss, chan in MODES:
    E.append(("**%s — *%s***" % (name, gloss), "**%s: *%s***" % (name, gloss)))
    E.append(("*(%s — %s)*" % (name, chan), "*(%s, %s)*" % (name, chan)))

E += [
    # -- parentheses -------------------------------------------------------------
    ("it's actually a harmony problem — everyone needs to feel heard first — that's "
     "why no amount of vision is fixing it.*",
     "it's actually a harmony problem (everyone needs to feel heard first), that's "
     "why no amount of vision is fixing it.*"),
    ("felt the gap between what people said and what they played — the game underneath "
     "the language, running the whole time — then you have the Sage's capacity.",
     "felt the gap between what people said and what they played (the game underneath "
     "the language, running the whole time) then you have the Sage's capacity."),
    ("reaches for the Architect's strategy game — *let me design you a system* — when "
     "the actual need is the Challenger's",
     "reaches for the Architect's strategy game (*let me design you a system*) when "
     "the actual need is the Challenger's"),
    ("Or reaches for the Diplomat's harmony game — *let me validate your experience* — "
     "when the actual need was the Sage's own",
     "Or reaches for the Diplomat's harmony game (*let me validate your experience*) "
     "when the actual need was the Sage's own"),
    ("because the game they're playing — seeing the whole board — feels like it puts "
     "them above the problem.",
     "because the game they're playing (seeing the whole board) feels like it puts "
     "them above the problem."),
    ("The Sage in distortion is doing versions of useful things — mediating pain, "
     "solving problems, designing systems — without the one diagnosis",
     "The Sage in distortion is doing versions of useful things (mediating pain, "
     "solving problems, designing systems) without the one diagnosis"),

    # -- colon -------------------------------------------------------------------
    ("The Sage could sit at a table and see all the games at once — could feel the "
     "Challenger's charge",
     "The Sage could sit at a table and see all the games at once: could feel the "
     "Challenger's charge"),
    ("The Sage's oldest wound: the capacity to see all the games without leaving any "
     "of them — and the village reading that as contradiction.",
     "The Sage's oldest wound: the capacity to see all the games without leaving any "
     "of them, and the village reading that as contradiction."),
    ("The second reading: you've spent enough time around the Sage's vocabulary — the "
     "games, which one the conflict actually turns on, who plays what — that the "
     "fluency itself",
     "The second reading: you've spent enough time around the Sage's vocabulary (the "
     "games, which one the conflict actually turns on, who plays what) that the "
     "fluency itself"),
    ("it's actually a boundary problem — that's why no amount of vision is fixing it.*",
     "it's actually a boundary problem: that's why no amount of vision is fixing it.*"),
    ("The guru on the mountain — not because the guru chose the mountain",
     "The guru on the mountain: not because the guru chose the mountain"),
    ("The distortion navigates these with perfect equanimity — able to see both sides",
     "The distortion navigates these with perfect equanimity: able to see both sides"),
    ("The real Sage sees all of it — including the hierarchy of pain — and names what "
     "they see.",
     "The real Sage sees all of it, including the hierarchy of pain, and names what "
     "they see."),
    ("The distortion designs for the rational actor — the version of the person who "
     "would respond correctly to the right incentive — without accounting",
     "The distortion designs for the rational actor (the version of the person who "
     "would respond correctly to the right incentive) without accounting"),
    ("The Sage in distortion appears when you get good at the vocabulary without doing "
     "the practice — when you learn to name the games without learning to put them down.",
     "The Sage in distortion appears when you get good at the vocabulary without doing "
     "the practice: when you learn to name the games without learning to put them down."),
    ("That's not a contradiction — it's the whole point.",
     "That's not a contradiction: it's the whole point."),
    ("the capacity to take in all the altitudes — Red, Amber, Orange, Green, Teal — "
     "and still choose to stand somewhere.",
     "the capacity to take in all the altitudes (Red, Amber, Orange, Green, Teal) "
     "and still choose to stand somewhere."),
    ("A meta-view of all of them — the capacity to see the whole system and choose "
     "where to stand inside it.",
     "A meta-view of all of them: the capacity to see the whole system and choose "
     "where to stand inside it."),
    ("The Sage gets this by staying — by seeing everything and then choosing",
     "The Sage gets this by staying: by seeing everything and then choosing"),
    ("True, because feeling is information — the body reports honestly on what it "
     "encounters.",
     "True, because feeling is information: the body reports honestly on what it "
     "encounters."),
    ("Stabilizing, because continuity is survival — what worked for the last generation",
     "Stabilizing, because continuity is survival: what worked for the last generation"),
    ("Incomplete, because holding is not resolving — the tension remains",
     "Incomplete, because holding is not resolving: the tension remains"),
    ("It asks what a person can currently hold — the size of the frame they operate "
     "from",
     "It asks what a person can currently hold: the size of the frame they operate "
     "from"),
    ("That's the whole difference — a question about where you're standing",
     "That's the whole difference: a question about where you're standing"),
    ("*The contraction is the body reporting honestly on what it takes in — and what "
     "it takes in is the gap",
     "*The contraction is the body reporting honestly on what it takes in, and what "
     "it takes in is the gap"),
    ("*The judgment is accurate, and it is also the trap — because the moment you "
     "stand above them",
     "*The judgment is accurate, and it is also the trap: because the moment you "
     "stand above them"),
    ("you feel the arrogance rise, you name it — *I am using the altitude to make "
     "distance instead of service* — and you let the judgment",
     "you feel the arrogance rise, you name it (*I am using the altitude to make "
     "distance instead of service*) and you let the judgment"),
    ("you notice the flatness, you name it — *I have gone unstaked, and unstaked "
     "naming reads as verdict* — and you let the numbness",
     "you notice the flatness, you name it (*I have gone unstaked, and unstaked "
     "naming reads as verdict*) and you let the numbness"),
    ("You've seen from Teal — the whole map, where everyone stands, why they're stuck, "
     "what altitude they're operating from — and now you have to come back",
     "You've seen from Teal (the whole map, where everyone stands, why they're stuck, "
     "what altitude they're operating from) and now you have to come back"),
    ("you feel the loss of altitude — the way things look smaller from inside than "
     "they did from above — and you let the sadness become tenderness.",
     "you feel the loss of altitude (the way things look smaller from inside than "
     "they did from above) and you let the sadness become tenderness."),
    ("People can feel that you're above it even when the naming lands correctly, and "
     "from above you can't serve — you can only report.",
     "People can feel that you're above it even when the naming lands correctly, and "
     "from above you can't serve: you can only report."),
    ("*I don't need this anymore — I'm past it.*",
     "*I don't need this anymore: I'm past it.*"),
    ("Call it a commitment loop rather than a developmental ladder — you don't climb "
     "it, you go around it.",
     "Call it a commitment loop rather than a developmental ladder: you don't climb "
     "it, you go around it."),
    ("Someone makes a strategy-game move — proposes a system, reaches for the process "
     "fix.",
     "Someone makes a strategy-game move: proposes a system, reaches for the process "
     "fix."),
    ("No — the problem is in the power game and we're dressing it as strategy.*",
     "No: the problem is in the power game and we're dressing it as strategy.*"),
    ("The work gets done by the capacity to be fully present with the client — without "
     "agenda, without rescue",
     "The work gets done by the capacity to be fully present with the client: without "
     "agenda, without rescue"),
    ("The Sage's is not measured in time at all — the last joke this Forest plays on you",
     "The Sage's is not measured in time at all: the last joke this Forest plays on you"),
    ("Something in you goes wide and attentive — the Panoramic Seer arriving on time",
     "Something in you goes wide and attentive: the Panoramic Seer arriving on time"),
    ("The Escape Artist half is the capacity to get out of a game — to put down a "
     "fight, a role, an identity that was load-bearing once",
     "The Escape Artist half is the capacity to get out of a game: to put down a "
     "fight, a role, an identity that was load-bearing once"),
    ("Not a game *about* something — the game of knowing which game you're in",
     "Not a game *about* something: the game of knowing which game you're in"),
    ("You've been playing strategy — systems, process, the search for the right lever.",
     "You've been playing strategy: systems, process, the search for the right lever."),
    ("Or you've been playing power — holding boundaries, staying clear about what you "
     "won't accept — and things have moved to harmony.",
     "Or you've been playing power (holding boundaries, staying clear about what you "
     "won't accept) and things have moved to harmony."),
    ("The Sage's most underrated move, coming back to a narrower game — staying with "
     "people in the game they can actually be in — without treating them as less",
     "The Sage's most underrated move, coming back to a narrower game (staying with "
     "people in the game they can actually be in) without treating them as less"),
    ("because coming down feels uncomfortable — the view from up there is so much "
     "clearer",
     "because coming down feels uncomfortable: the view from up there is so much "
     "clearer"),
    ("putting it down means sitting with the loss of that — not pretending it didn't "
     "matter",
     "putting it down means sitting with the loss of that: not pretending it didn't "
     "matter"),
    ("The real Sage is in it, has skin in it, draws the line and holds the field and "
     "builds the thing and stays — and knows which game they're doing it from.",
     "The real Sage is in it, has skin in it, draws the line and holds the field and "
     "builds the thing and stays, and knows which game they're doing it from."),
    ("Wake Up is the Panoramic Seer with an instrument in its hand — every card at "
     "that stage asks the same question",
     "Wake Up is the Panoramic Seer with an instrument in its hand: every card at "
     "that stage asks the same question"),
    ("The signal registers, and alongside it registers the fact that you noticed it "
     "the way you notice things — the suspect way.",
     "The signal registers, and alongside it registers the fact that you noticed it "
     "the way you notice things: the suspect way."),
    ("a defective instrument doesn't get upgrades, it gets fixed first — and the "
     "fixing has no completion condition.",
     "a defective instrument doesn't get upgrades, it gets fixed first, and the "
     "fixing has no completion condition."),
    ("Take **Who the Fight Makes You** — Grow Up, Direct Action, Sage.",
     "Take **Who the Fight Makes You**: Grow Up, Direct Action, Sage."),
    ("The card assumes the instrument works and asks what it's becoming — the "
     "assumption the daemon cannot make on its own.",
     "The card assumes the instrument works and asks what it's becoming: the "
     "assumption the daemon cannot make on its own."),
    ("Bring a fight you're carrying right now — an actual one, with people in it.",
     "Bring a fight you're carrying right now: an actual one, with people in it."),
    ("You see something true — the game underneath the game, the thing everyone can "
     "feel and nobody says — and instead of holding it",
     "You see something true (the game underneath the game, the thing everyone can "
     "feel and nobody says) and instead of holding it"),
    ("The gift is perspective with commitment — the capacity to see all the games",
     "The gift is perspective with commitment: the capacity to see all the games"),

    ("and you name it — *I don't want to give this up because giving it up means "
     "being someone who doesn't do this anymore.*",
     "and you name it: *I don't want to give this up because giving it up means "
     "being someone who doesn't do this anymore.*"),
    ("all running at once — isn't that something?*",
     "all running at once, isn't that something?*"),

    # -- comma -------------------------------------------------------------------
    ("It came on gradually — the way a table goes still",
     "It came on gradually, the way a table goes still"),
    ("still in relationship* — the village didn't know what to do with that.",
     "still in relationship*, the village didn't know what to do with that."),
    ("The actual Sage — the one who saw the whole thing and still set the table — "
     "stopped speaking.",
     "The actual Sage, the one who saw the whole thing and still set the table, "
     "stopped speaking."),
    ("Not the loud kind — not being asked to leave, not being told you were wrong.",
     "Not the loud kind, not being asked to leave, not being told you were wrong."),
    ("If something moved while you read — a recognition, a *yes* — the story located "
     "something real.",
     "If something moved while you read, a recognition, a *yes*, the story located "
     "something real."),
    ("nobody around you knew what to do with that capacity — not because the seeing "
     "itself had anything wrong with it.",
     "nobody around you knew what to do with that capacity, not because the seeing "
     "itself had anything wrong with it."),
    ("the distance you sometimes feel in your progressive spaces — why you can stand "
     "surrounded by people",
     "the distance you sometimes feel in your progressive spaces, why you can stand "
     "surrounded by people"),
    ("more certain everyone became that they were doing the work — when actually they "
     "were playing the same game",
     "more certain everyone became that they were doing the work, when actually they "
     "were playing the same game"),
    ("Not the real Sage — the village's version.",
     "Not the real Sage, the village's version."),
    ("The person most wounded gets the most airtime — not because their pain is more "
     "valid",
     "The person most wounded gets the most airtime, not because their pain is more "
     "valid"),
    ("The real Sage names which game the people are actually in and designs for that — "
     "not for the game they wish the people were in.",
     "The real Sage names which game the people are actually in and designs for that, "
     "not for the game they wish the people were in."),
    ("Not to hold above — to hold with.", "Not to hold above, to hold with."),
    ("The real Sage knows it happens from inside — not from a balcony above it.",
     "The real Sage knows it happens from inside, not from a balcony above it."),
    ("Not sadness about what people can't see — something colder.",
     "Not sadness about what people can't see, something colder."),
    ("Not pleasant — fun.", "Not pleasant, fun."),
    ("The pattern: speaking from the whole-board view to people inside the power game, "
     "in whole-board language, as though they could receive it — or knowing they can't",
     "The pattern: speaking from the whole-board view to people inside the power game, "
     "in whole-board language, as though they could receive it, or knowing they can't"),
    ("the first response comes back defensive — *you think you're better than us* — "
     "even when the naming lands exactly right.",
     "the first response comes back defensive, *you think you're better than us*, "
     "even when the naming lands exactly right."),
    ("the commitments put down before they taught what they had to teach — they don't "
     "disappear.",
     "the commitments put down before they taught what they had to teach, they don't "
     "disappear."),
    ("and immediately needing to come back — not because the moment asks for it",
     "and immediately needing to come back, not because the moment asks for it"),
    ("You notice when things move from the power game back toward harmony — someone "
     "names the boundary",
     "You notice when things move from the power game back toward harmony, someone "
     "names the boundary"),
    ("You've seen from a different vantage — not better, different.",
     "You've seen from a different vantage, not better, different."),
    ("Name what you saw — honestly, without performance.**",
     "Name what you saw, honestly, without performance.**"),
    ("You name it anyway — not because the naming will change anything",
     "You name it anyway, not because the naming will change anything"),
    ("Listen for which game they're in — and meet them there.**",
     "Listen for which game they're in, and meet them there.**"),
    ("unless naming it is itself the whole-board move — which it sometimes is, and "
     "usually isn't.",
     "unless naming it is itself the whole-board move, which it sometimes is, and "
     "usually isn't."),
    ("Stay embodied — especially when the view is clear.**",
     "Stay embodied, especially when the view is clear.**"),
    ("is worth more than the Sage who stays above — and only when the one who returns "
     "arrives fully present.",
     "is worth more than the Sage who stays above, and only when the one who returns "
     "arrives fully present."),
    ("Let them not understand — and let that be okay.**",
     "Let them not understand, and let that be okay.**"),
    ("It keeps you from expecting your own experience to be universal — the single "
     "most useful correction",
     "It keeps you from expecting your own experience to be universal, the single "
     "most useful correction"),
    ("returns an answer about what needs fixing in you — and the thing that needs "
     "fixing is always upstream",
     "returns an answer about what needs fixing in you, and the thing that needs "
     "fixing is always upstream"),
    ("the accumulation never becomes knowledge — it stays a prosthetic for a defect",
     "the accumulation never becomes knowledge, it stays a prosthetic for a defect"),
    ("Somebody offers you something — a correction, a piece of feedback, an opening — "
     "and it doesn't get received as input",
     "Somebody offers you something, a correction, a piece of feedback, an opening, "
     "and it doesn't get received as input"),
    ("you will spend your life assuming everyone sees what you see — its own "
     "catastrophe, and a louder one.",
     "you will spend your life assuming everyone sees what you see, its own "
     "catastrophe, and a louder one."),
    ("It argues about the instrument — and an argument about the instrument looks like",
     "It argues about the instrument, and an argument about the instrument looks like"),
    ("Doesn't matter — I'm not calibrated for it.",
     "Doesn't matter, I'm not calibrated for it."),
    ("Look at the sequence, not the verdict — that is why the app keeps count.",
     "Look at the sequence, not the verdict, that is why the app keeps count."),
    ("Sometimes — often — it's Return, because you've been above things too long",
     "Sometimes, often, it's Return, because you've been above things too long"),
    ("when to stay and when to leave — from choice rather than default.",
     "when to stay and when to leave, from choice rather than default."),
    ("isn't practicing the Game-Switcher — they're uncomfortable with commitment.",
     "isn't practicing the Game-Switcher, they're uncomfortable with commitment."),
    ("Not because it didn't matter — because it mattered and it's over.",
     "Not because it didn't matter, because it mattered and it's over."),
    ("If you can, and you put it down anyway — that's the practice.",
     "If you can, and you put it down anyway, that's the practice."),
    ("you can still choose to stand on the board — inside a game, with people playing "
     "a different one",
     "you can still choose to stand on the board, inside a game, with people playing "
     "a different one"),
    ("and still care — not despite knowing, because of it.",
     "and still care, not despite knowing, because of it."),
    ("Draw from your twenty rather than the hundred and twenty — though not all from "
     "one move.",
     "Draw from your twenty rather than the hundred and twenty, though not all from "
     "one move."),
    ("Fire, Water, Metal, Earth, Wood — one of them, not *my thing.*",
     "Fire, Water, Metal, Earth, Wood, one of them, not *my thing.*"),
    ("and you can be that person — not from above, from with.",
     "and you can be that person, not from above, from with."),
    ("That question was never the Sage's to answer — only to hand you.",
     "That question was never the Sage's to answer, only to hand you."),
    ("Not the Sage looking down from anywhere — the Player out ahead on the road",
     "Not the Sage looking down from anywhere, the Player out ahead on the road"),
]


def main():
    p = os.path.join(MS, "ch8.md")
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
