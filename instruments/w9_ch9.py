# -*- coding: utf-8 -*-
"""
W9, finished: ch9's 139 prose em-dashes. The last of the seven.

ch9 carries more repeated families than any other chapter, and per 095a1ed's method
each takes one ruling rather than one per sibling:

  the WAVE gloss lists   `Wake up — notice what happened.` and its siblings, twice
                         over -- once for failure, once for activation -- take a colon.
  the five Move recaps   `*Cut the field* — it is not about allyship in general` and
                         siblings take a colon.

ch9 is the book's least colon-dense chapter at 7.5/1k against an average of 12.4, and
its choppiest at 30.6% <=6-word sentences against 25.7. So the colon carries most of
this chapter and the full stop is spent nowhere, which is the opposite of the
allocation ch1 needed and the reason the ruling is per chapter rather than per book.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# The two WAVE families, generated so a sibling cannot drift from its siblings.
FAILURE = ["Wake up — notice what happened.",
           "Open up — let the failure land at full strength before you start explaining it.",
           "Clean up — name what didn't work.",
           "Grow up — ask what the failure is actually telling you.",
           "Show up — do the next version.",
           "Come back — notice what shifted."]
ACTIVATION = ["Wake up — notice what's happening inside you when your mother calls",
              "Open up — stay with it before you do anything with it.",
              "Clean up — name the channel and let it run to completion.",
              "Grow up — ask what this moment asks you to become.",
              "Show up — act from that place, not from the reactive place",
              "Come back — notice what happened, what shifted, what you learned."]

E = [(s, s.replace(" — ", ": ", 1)) for s in FAILURE + ACTIVATION]

E += [
    # -- the five Move recaps, one ruling ---------------------------------------
    ("*Cut the field* — it is not about allyship in general",
     "*Cut the field*: it is not about allyship in general"),
    ("*Put it in front of one person* — it went in front of players before it was good",
     "*Put it in front of one person*: it went in front of players before it was good"),
    ("*Take the note that costs you the design* — the token economy did not get adjusted",
     "*Take the note that costs you the design*: the token economy did not get adjusted"),
    ("*Run it again with one thing changed* — every failed session became the next "
     "session",
     "*Run it again with one thing changed*: every failed session became the next "
     "session"),
    ("*Hand someone the pen* — the goal is for bars-engine to outlive its founder",
     "*Hand someone the pen*: the goal is for bars-engine to outlive its founder"),

    # -- parentheses -------------------------------------------------------------
    ("The fear will run the entire scenario — the failure, the criticism, the public "
     "collapse — before I've taken a single real action.",
     "The fear will run the entire scenario (the failure, the criticism, the public "
     "collapse) before I've taken a single real action."),
    ("Maybe it was a public issue — the election, the pandemic, the ongoing "
     "catastrophe — where you felt morally obligated to act",
     "Maybe it was a public issue (the election, the pandemic, the ongoing "
     "catastrophe) where you felt morally obligated to act"),
    ("Everything I build — this book, bars-engine, the next thing — walks me further "
     "into that specific problem.",
     "Everything I build (this book, bars-engine, the next thing) walks me further "
     "into that specific problem."),
    ("a game that actually taught the WAVE, that made the emotional alchemy something "
     "you could practice instead of just understand — and I had enough of the six Faces",
     "a game that actually taught the WAVE, that made the emotional alchemy something "
     "you could practice instead of just understand), and I had enough of the six Faces"),
    ("I had a felt sense of what was missing — a game that actually taught the WAVE",
     "I had a felt sense of what was missing (a game that actually taught the WAVE"),
    ("Here's what I've noticed about my own mistake with this: I spent months with the "
     "sequence in front of me — reviewing, discerning, designing, building, passing on "
     "— without actually doing any of it.",
     "Here's what I've noticed about my own mistake with this: I spent months with the "
     "sequence in front of me (reviewing, discerning, designing, building, passing on) "
     "without actually doing any of it."),
    ("It wasn't until I actually started something — before I felt ready, before the "
     "design was complete — that the practice became real.",
     "It wasn't until I actually started something (before I felt ready, before the "
     "design was complete) that the practice became real."),
    ("If what you want is the method itself — to run these six Faces for other people, "
     "not just for the thing you're building — that is the succession",
     "If what you want is the method itself (to run these six Faces for other people, "
     "not just for the thing you're building) that is the succession"),
    ("If you want the method itself — to run it for other people, not just for the "
     "thing you're building — that's the succession",
     "If you want the method itself (to run it for other people, not just for the "
     "thing you're building) that's the succession"),

    # -- colon -------------------------------------------------------------------
    ("To show that the Faces weren't just a map for understanding — they were a "
     "toolkit for building.",
     "To show that the Faces weren't just a map for understanding: they were a "
     "toolkit for building."),
    ("That you don't *become* one of them — you *move through* all of them",
     "That you don't *become* one of them: you *move through* all of them"),
    ("These aren't concepts to understand — they're moves to make.",
     "These aren't concepts to understand: they're moves to make."),
    ("They don't run in sequence the way the WAVE's stages do — they loop.",
     "They don't run in sequence the way the WAVE's stages do: they loop."),
    ("The five modes work as roles, not personalities — you move through them as you "
     "design your practice.",
     "The five modes work as roles, not personalities: you move through them as you "
     "design your practice."),
    ("The Designer builds a working system — one you can actually use",
     "The Designer builds a working system: one you can actually use"),
    ("The Founder creates the thing that didn't exist before — the specific allyship "
     "practice",
     "The Founder creates the thing that didn't exist before: the specific allyship "
     "practice"),
    ("I built the thing I needed and couldn't find — an actual game system",
     "I built the thing I needed and couldn't find: an actual game system"),
    ("The Elder's move hands down an inheritance — not building something new",
     "The Elder's move hands down an inheritance: not building something new"),
    ("You have been handed twenty cards six times in this book — the Shaman's twenty",
     "You have been handed twenty cards six times in this book: the Shaman's twenty"),
    ("Running it for a group becomes possible after that — a session, a team, a family",
     "Running it for a group becomes possible after that: a session, a team, a family"),
    ("The Outlaw disrupts — not for the sake of it, but because every tradition",
     "The Outlaw disrupts: not for the sake of it, but because every tradition"),
    ("The deck runs underneath all five of them — whichever mode runs",
     "The deck runs underneath all five of them: whichever mode runs"),
    ("Build your personal practice — the specific blend of all six that is uniquely "
     "yours.",
     "Build your personal practice: the specific blend of all six that is uniquely "
     "yours."),
    ("You might start at Review — doing the honest inventory",
     "You might start at Review: doing the honest inventory"),
    ("You might start at Discern — you know which problem you keep trying to solve",
     "You might start at Discern: you know which problem you keep trying to solve"),
    ("You might start at Pass On — you're already doing the work",
     "You might start at Pass On: you're already doing the work"),
    ("You make the thing so it can meet a person — a reader, a player, a colleague, "
     "your kid.",
     "You make the thing so it can meet a person: a reader, a player, a colleague, "
     "your kid."),
    ("The Player in distortion builds in the other direction — inward, in circles",
     "The Player in distortion builds in the other direction: inward, in circles"),
    ("The kind that comes from performing allyship — saying the right things",
     "The kind that comes from performing allyship: saying the right things"),
    ("You now know that the work happens in the Forest — finding what was abandoned",
     "You now know that the work happens in the Forest: finding what was abandoned"),
    ("Then I did what the culture taught me to do — I looked outward for the solution.",
     "Then I did what the culture taught me to do: I looked outward for the solution."),
    ("You know how the Shaman feels what's true — how to name the feeling",
     "You know how the Shaman feels what's true: how to name the feeling"),
    ("You know how the Challenger draws the line — how to hold a position",
     "You know how the Challenger draws the line: how to hold a position"),
    ("You know how the Regent builds what lasts — how to ask *what am I protecting",
     "You know how the Regent builds what lasts: how to ask *what am I protecting"),
    ("You know how the Architect designs for the next person — how to make the right "
     "thing easy",
     "You know how the Architect designs for the next person: how to make the right "
     "thing easy"),
    ("You know how the Diplomat holds the field across difference — how to make space",
     "You know how the Diplomat holds the field across difference: how to make space"),
    ("You know how the Sage sees the whole game and plays their part — how to know "
     "which game",
     "You know how the Sage sees the whole game and plays their part: how to know "
     "which game"),
    ("You know that the five emotional channels do more than name things — they map "
     "the territory",
     "You know that the five emotional channels do more than name things: they map "
     "the territory"),
    ("Real failure — the kind where someone looks at what you built",
     "Real failure: the kind where someone looks at what you built"),
    ("I'd done this work informally for years — coaching people through the emotional "
     "labor",
     "I'd done this work informally for years: coaching people through the emotional "
     "labor"),
    ("Every version of bars-engine was the walk — not a step toward it.",
     "Every version of bars-engine was the walk, not a step toward it."),
    ("Something in a life, a job, a family, a community — some specific gap",
     "Something in a life, a job, a family, a community: some specific gap"),
    ("Bars-engine is the village's common ground — the playground where players arrive",
     "Bars-engine is the village's common ground: the playground where players arrive"),
    ("Some of you remain in the middle of the walk — still in the confusion",
     "Some of you remain in the middle of the walk: still in the confusion"),
    ("The Player treats failure as the WAVE — wake up to what actually happened",
     "The Player treats failure as the WAVE: wake up to what actually happened"),
    ("bars-engine works as more than a solo project — a structure already alive",
     "bars-engine works as more than a solo project: a structure already alive"),
    ("You bring your specific gift — the thing this book helped you name",
     "You bring your specific gift: the thing this book helped you name"),
    ("One of them is live in you right now — the Face that showed up most",
     "One of them is live in you right now: the Face that showed up most"),
    ("These five moves do something else — they name what you do when another person",
     "These five moves do something else: they name what you do when another person"),
    ("An unspecified ask gets you encouragement — the least useful thing a human being "
     "can hand you.",
     "An unspecified ask gets you encouragement: the least useful thing a human being "
     "can hand you."),
    ("Naming it first is what lets the group know what it is choosing to give up — the "
     "difference between a reform and an amputation.",
     "Naming it first is what lets the group know what it is choosing to give up: the "
     "difference between a reform and an amputation."),
    ("A hundred and twenty cards — Wake Up, Open Up, Clean Up, Grow Up, Show Up",
     "A hundred and twenty cards: Wake Up, Open Up, Clean Up, Grow Up, Show Up"),
    ("Now go build yours — the village is waiting.",
     "Now go build yours: the village is waiting."),
    ("The actual you, standing where the performed you and the performed ally used to "
     "stand — the one who has done the inner work",
     "The actual you, standing where the performed you and the performed ally used to "
     "stand: the one who has done the inner work"),
    ("What's the thing in your life that keeps showing up — the one you keep trying to "
     "fix",
     "What's the thing in your life that keeps showing up: the one you keep trying to "
     "fix"),
    ("One, rather than an audience or a group — one person who will actually respond",
     "One, rather than an audience or a group: one person who will actually respond"),
    ("Three people have failed at this role and every one of them experienced it as a "
     "personal failure — the signature of a design problem",
     "Three people have failed at this role and every one of them experienced it as a "
     "personal failure: the signature of a design problem"),
    ("you are the only person both sides will still talk to — the Connector's actual "
     "job.",
     "you are the only person both sides will still talk to: the Connector's actual "
     "job."),
    ("Receiving the piece of feedback that cannot be absorbed without rebuilding "
     "something you already made — and rebuilding it.",
     "Receiving the piece of feedback that cannot be absorbed without rebuilding "
     "something you already made, and rebuilding it."),

    ("keeps the Player from becoming the distortion — from collecting the Faces as "
     "credentials",
     "keeps the Player from becoming the distortion: from collecting the Faces as "
     "credentials"),
    ("being careful about every word — and finding that none of it works.",
     "being careful about every word, and finding that none of it works."),

    # -- comma -------------------------------------------------------------------
    ("It crept in slowly, the way most distortions do — not as a lie, but as an "
     "understandable mistake.",
     "It crept in slowly, the way most distortions do, not as a lie, but as an "
     "understandable mistake."),
    ("Anyone who wasn't one of those — who didn't naturally feel-first, or draw-lines, "
     "or build-systems — wasn't doing it right.",
     "Anyone who wasn't one of those, who didn't naturally feel-first, or draw-lines, "
     "or build-systems, wasn't doing it right."),
    ("could diagnose which game a group had fallen into — but when it came time to play",
     "could diagnose which game a group had fallen into, but when it came time to play"),
    ("The real Player walks through all six Faces and then — decides.",
     "The real Player walks through all six Faces and then decides."),
    ("The village needed the six Faces as a teaching instrument — and now the teaching "
     "instrument passes to you.",
     "The village needed the six Faces as a teaching instrument, and now the teaching "
     "instrument passes to you."),
    ("This one names what you do when you're activated — when your mother calls",
     "This one names what you do when you're activated, when your mother calls"),
    ("Like any moves, they require practice — the doing kind, repeated",
     "Like any moves, they require practice, the doing kind, repeated"),
    ("You might find that you naturally move to Challenger when things get hard — and "
     "that the Challenger's game suits you best",
     "You might find that you naturally move to Challenger when things get hard, and "
     "that the Challenger's game suits you best"),
    ("Or you might find that you live in the Architect's head — and that your gift lies",
     "Or you might find that you live in the Architect's head, and that your gift lies"),
    ("You might find that the Sage's whole-board view feels like yours — and that your "
     "shadow uses the panoramic view",
     "You might find that the Sage's whole-board view feels like yours, and that your "
     "shadow uses the panoramic view"),
    ("That felt like home — relational, careful, good at holding the field.",
     "That felt like home, relational, careful, good at holding the field."),
    ("I performed the Diplomat to avoid the discomfort of the Challenger's game — the "
     "discomfort of saying no",
     "I performed the Diplomat to avoid the discomfort of the Challenger's game, the "
     "discomfort of saying no"),
    ("Not as an abstraction — as a concrete plan.",
     "Not as an abstraction, as a concrete plan."),
    ("because that Face's territory makes them uncomfortable — not because it has "
     "nothing to do with them.",
     "because that Face's territory makes them uncomfortable, not because it has "
     "nothing to do with them."),
    ("and nobody else has built it — you build it yourself or it stays missing.",
     "and nobody else has built it, you build it yourself or it stays missing."),
    ("If that describes you — if you have a specific thing you want to build and you "
     "know it has to be you — the fastest path I know",
     "If that describes you, if you have a specific thing you want to build and you "
     "know it has to be you, the fastest path I know"),
    ("It won't stay true — I wrote this down so the map would live in more hands than "
     "mine.",
     "It won't stay true, I wrote this down so the map would live in more hands than "
     "mine."),
    ("One tell separates real building from the kind that's secretly avoidance — and "
     "it has nothing to do with how productive you feel.",
     "One tell separates real building from the kind that's secretly avoidance, and "
     "it has nothing to do with how productive you feel."),
    ("Now the question — what comes next?", "Now the question, what comes next?"),
    ("You may have located the problem outward — that the gap between the world and "
     "what it should be",
     "You may have located the problem outward, that the gap between the world and "
     "what it should be"),
    ("You know that the return is not optional — that coming back makes the work real.",
     "You know that the return is not optional, that coming back makes the work real."),
    ("The moment when the thing you built does exactly what you designed it to do and "
     "you feel nothing — because you're already thinking about the next version.",
     "The moment when the thing you built does exactly what you designed it to do and "
     "you feel nothing, because you're already thinking about the next version."),
    ("I want you to know it — so that when the walking takes longer than you thought",
     "I want you to know it, so that when the walking takes longer than you thought"),
    ("The performed ally burns out — because performing exhausts you",
     "The performed ally burns out, because performing exhausts you"),
    ("You don't arrive and then act — you act from somewhere on the path",
     "You don't arrive and then act, you act from somewhere on the path"),
    ("Got feedback mid-course that it wasn't fun — which meant I had to build a section",
     "Got feedback mid-course that it wasn't fun, which meant I had to build a section"),
    ("I hadn't known I was depressed — I'm someone who can keep moving even when I'm "
     "sad.",
     "I hadn't known I was depressed, I'm someone who can keep moving even when I'm "
     "sad."),
    ("I found myself sad but also relieved — the relief coming from ending a fight",
     "I found myself sad but also relieved, the relief coming from ending a fight"),
    ("They allied with the guilt, the shame, the avoidance — and alchemized them",
     "They allied with the guilt, the shame, the avoidance, and alchemized them"),
    ("or create the allies I'd wanted to create — and found that I'd learned something "
     "true",
     "or create the allies I'd wanted to create, and found that I'd learned something "
     "true"),
    ("You'll be afraid when you realize the thing you built has a shadow you didn't "
     "anticipate — that the tool you made",
     "You'll be afraid when you realize the thing you built has a shadow you didn't "
     "anticipate, that the tool you made"),
    ("Use the rehearsal as data — the fear shows me what I care about",
     "Use the rehearsal as data, the fear shows me what I care about"),
    ("I wake up to what's actually happening in a chapter — not the version I wanted",
     "I wake up to what's actually happening in a chapter, not the version I wanted"),
    ("I open up to it before I start repairing it — the chapter stays as broken as it is",
     "I open up to it before I start repairing it, the chapter stays as broken as it is"),
    ("who have done the therapy and read the books and know all the vocabulary — and "
     "who still don't have a practice.",
     "who have done the therapy and read the books and know all the vocabulary, and "
     "who still don't have a practice."),
    ("When the problem becomes specific enough — when you've mapped it enough times "
     "that you can name it in a sentence — the Founder move will become obvious.",
     "When the problem becomes specific enough, when you've mapped it enough times "
     "that you can name it in a sentence, the Founder move will become obvious."),
    ("Or you might be someone still in the confusion — and the honest answer says "
     "exactly that.",
     "Or you might be someone still in the confusion, and the honest answer says "
     "exactly that."),
    ("I'm a helper, a teacher, a parent, a friend — not a founder.*",
     "I'm a helper, a teacher, a parent, a friend, not a founder.*"),
    ("you decide to create something that didn't exist before you — whether it's "
     "a conversation",
     "you decide to create something that didn't exist before you, whether it's "
     "a conversation"),
    ("the problem you're carrying deserves solving — and start making something toward "
     "it.",
     "the problem you're carrying deserves solving, and start making something toward "
     "it."),
    ("find that the village wasn't ready for it — that what you built as liberation",
     "find that the village wasn't ready for it, that what you built as liberation"),
    ("It needs your willingness to go first — not because you have all the answers",
     "It needs your willingness to go first, not because you have all the answers"),
    ("The question comes down to where you fit in — and that's something you'll only "
     "discover",
     "The question comes down to where you fit in, and that's something you'll only "
     "discover"),
    ("Earlier in this chapter the tell was direction — is the work moving toward "
     "contact",
     "Earlier in this chapter the tell was direction, is the work moving toward "
     "contact"),
    ("Say what you want from them before you show it — *tell me where you got confused*",
     "Say what you want from them before you show it, *tell me where you got confused*"),
    ("which feels like courage and functions like avoidance — a total rebuild resets "
     "the clock",
     "which feels like courage and functions like avoidance, a total rebuild resets "
     "the clock"),
    ("The Architect designs a system that runs without them — that is handoff",
     "The Architect designs a system that runs without them, that is handoff"),
    ("puts it somewhere another person can change it — the only transaction that turns "
     "a design into a practice.",
     "puts it somewhere another person can change it, the only transaction that turns "
     "a design into a practice."),
    ("The Player shows the village what it looks like to walk all six Faces and come "
     "out the other side — not above the village",
     "The Player shows the village what it looks like to walk all six Faces and come "
     "out the other side, not above the village"),
    ("The Player shows that mastery is not about *being* one Face — it's about "
     "*playing* all six",
     "The Player shows that mastery is not about *being* one Face, it's about "
     "*playing* all six"),
    ("then **Switch Games Deliberately** — the same argument in a different setting",
     "then **Switch Games Deliberately**, the same argument in a different setting"),
]


def main():
    p = os.path.join(MS, "ch9.md")
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
