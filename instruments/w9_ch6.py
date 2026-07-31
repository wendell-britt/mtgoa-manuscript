# -*- coding: utf-8 -*-
"""
W9, finished: ch6's 94 prose em-dashes.

One site is not a joint and takes a different mark. `Let me show you —*` at line 89
ends the Architect's speech mid-sentence, cut off by the village walking away. That
is a trailing-off, not a joint between two clauses, and the mark for it is an
ellipsis. Converting it to a comma or a colon would have implied the sentence
finished, which is the one thing the scene needs it not to do.

  19 colon  ·  56 comma  ·  18 parenthesis (nine pairs)  ·  1 ellipsis
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("Let me show you —*", "Let me show you…*"),

    # -- parentheses -------------------------------------------------------------
    ("Because the village had exiled the Architect — had decided that structural "
     "clarity meant coldness, that systems thinking meant not loving the people inside "
     "the systems — the village lost the ability",
     "Because the village had exiled the Architect (had decided that structural "
     "clarity meant coldness, that systems thinking meant not loving the people inside "
     "the systems) the village lost the ability"),
    ("Then — here comes the part most people skip — *and now",
     "Then (here comes the part most people skip) *and now"),
    ("the most comfortable sentence in the discipline — *the system did it* — true",
     "the most comfortable sentence in the discipline (*the system did it*), true"),
    ("will iterate forever — each deployment producing new observations, each set of "
     "observations justifying another cycle — and nothing inside that loop",
     "will iterate forever (each deployment producing new observations, each set of "
     "observations justifying another cycle) and nothing inside that loop"),
    ("Neutrality detects coherence — whether the parts add up to a whole — and stuck "
     "Neutrality is flatness",
     "Neutrality detects coherence (whether the parts add up to a whole) and stuck "
     "Neutrality is flatness"),
    ("Joy detects vitality — what wants to exist and doesn't yet — and Joy stuck is "
     "the idea",
     "Joy detects vitality (what wants to exist and doesn't yet) and Joy stuck is "
     "the idea"),
    ("Pick a group you're actually in — a team, a committee, a coalition — where "
     "everyone keeps busy",
     "Pick a group you're actually in (a team, a committee, a coalition) where "
     "everyone keeps busy"),
    ("Before it has finished landing — before you could name the channel, before you "
     "could say where in your body it went — it has already become a design problem.",
     "Before it has finished landing (before you could name the channel, before you "
     "could say where in your body it went) it has already become a design problem."),
    ("land as enormous — three-quarter restructures aimed at a two-degree problem — "
     "and the Architect cannot understand",
     "land as enormous (three-quarter restructures aimed at a two-degree problem) "
     "and the Architect cannot understand"),
    ("Then you say the sentence back — the small, unarchitected, in-the-meeting "
     "sentence — and the restructure still gets built",
     "Then you say the sentence back (the small, unarchitected, in-the-meeting "
     "sentence) and the restructure still gets built"),

    # -- parenthetical pairs taking commas ---------------------------------------
    ("The village became very busy — very purposeful, very committed — and very unable",
     "The village became very busy, very purposeful, very committed, and very unable"),
    ("Into the performance of systemic thinking — the language without the practice — "
     "and that costs more",
     "Into the performance of systemic thinking, the language without the practice, "
     "and that costs more"),
    ("The previous designer in you — past you — needs to hear that they weren't wrong.",
     "The previous designer in you, past you, needs to hear that they weren't wrong."),
    ("Without the Architect to say *wait — before you build this, let me show you what "
     "it will actually produce* — the village built systems",
     "Without the Architect to say *wait, before you build this, let me show you what "
     "it will actually produce*, the village built systems"),

    # -- colon -------------------------------------------------------------------
    ("*we don't need another analysis — we need action.",
     "*we don't need another analysis: we need action."),
    ("We don't need to understand why we're stuck — we need to get un-stuck.",
     "We don't need to understand why we're stuck: we need to get un-stuck."),
    ("the people inside the systems become abstractions — inputs, outputs, leverage "
     "points.",
     "the people inside the systems become abstractions: inputs, outputs, leverage "
     "points."),
    ("**Every system produces the outcomes it's designed to produce** — the outcomes "
     "the incentive structure actually rewards",
     "**Every system produces the outcomes it's designed to produce**: the outcomes "
     "the incentive structure actually rewards"),
    ("the system has not broken — the system is working exactly as designed.",
     "the system has not broken: the system is working exactly as designed."),
    ("and rightly — *personal responsibility* has done a great deal of work",
     "and rightly: *personal responsibility* has done a great deal of work"),
    ("the native material is not emotion — it is *logic.*",
     "the native material is not emotion: it is *logic.*"),
    ("Then the Architect hands off — names who owns the format",
     "Then the Architect hands off: names who owns the format"),
    ("Somebody will hear it as criticism — that's the cost",
     "Somebody will hear it as criticism: that's the cost"),
    ("A feeling converted at that speed does not deliver its information — it delivers "
     "its energy",
     "A feeling converted at that speed does not deliver its information: it delivers "
     "its energy"),
    ("Observe is the first stage and the one everything else rests on — what is "
     "actually happening, traced to its source",
     "Observe is the first stage and the one everything else rests on: what is "
     "actually happening, traced to its source"),
    ("asked the person what they need — asking would require staying in the feeling",
     "asked the person what they need: asking would require staying in the feeling"),
    ("When it does not work, it will not be forgotten — it will be cited.",
     "When it does not work, it will not be forgotten: it will be cited."),
    ("All of it, raw, before it means anything — the channel, the place it landed, "
     "what it did.",
     "All of it, raw, before it means anything: the channel, the place it landed, "
     "what it did."),
    ("not a breath and it is not a cycle — it is a stage.",
     "not a breath and it is not a cycle: it is a stage."),
    ("The Emotional Body does not argue for coldness — you would notice coldness.",
     "The Emotional Body does not argue for coldness: you would notice coldness."),
    ("Take **Forge the Anger** — Clean Up, Direct Action, Architect.",
     "Take **Forge the Anger**: Clean Up, Direct Action, Architect."),
    ("before relationship, before loyalty, before strategy — there is structure.",
     "before relationship, before loyalty, before strategy: there is structure."),
    ("When goodwill is missing, someone has to go build it — hold the field",
     "When goodwill is missing, someone has to go build it: hold the field"),

    # -- comma -------------------------------------------------------------------
    ("The Architect drew the first map — looked at the chaos",
     "The Architect drew the first map, looked at the chaos"),
    ("*here is why this keeps breaking — and here is how to redesign it so it holds.*",
     "*here is why this keeps breaking, and here is how to redesign it so it holds.*"),
    ("The shift arrived gradually — the way a village running on good intentions",
     "The shift arrived gradually, the way a village running on good intentions"),
    ("The village had started working around the Architect — implementing half the "
     "design",
     "The village had started working around the Architect, implementing half the "
     "design"),
    ("we understand the systemic issues* — while continuing to do the same thing",
     "we understand the systemic issues*, while continuing to do the same thing"),
    ("*we don't need to overthink this* — another way of saying",
     "*we don't need to overthink this*, another way of saying"),
    ("Structural blame costs more than structural ignorance — because at least a "
     "question cures ignorance.",
     "Structural blame costs more than structural ignorance, because at least a "
     "question cures ignorance."),
    ("say *here is why this keeps breaking — and here is how to fix it.*",
     "say *here is why this keeps breaking, and here is how to fix it.*"),
    ("because the report says the process worked — and it did work, on the backs of "
     "whoever paid the difference.",
     "because the report says the process worked, and it did work, on the backs of "
     "whoever paid the difference."),
    ("the part of you that feels the system before it models it — those show what "
     "structural clarity looks like",
     "the part of you that feels the system before it models it, those show what "
     "structural clarity looks like"),
    ("the outcomes it produces — and redesigning the system so that the right outcome",
     "the outcomes it produces, and redesigning the system so that the right outcome"),
    ("Not the job description — the actual incentive.",
     "Not the job description, the actual incentive."),
    ("Change the system and you change the behavior — not by convincing the person to "
     "be better",
     "Change the system and you change the behavior, not by convincing the person to "
     "be better"),
    ("wonder why nobody listened — when the answer comes simple",
     "wonder why nobody listened, when the answer comes simple"),
    ("does the other thing — and the fact that they can is not a rounding error",
     "does the other thing, and the fact that they can is not a rounding error"),
    ("a structural account of every situation you were personally in — the one account "
     "that never requires you to have been there as a person.",
     "a structural account of every situation you were personally in, the one account "
     "that never requires you to have been there as a person."),
    ("What is actually happening — measured, traced to its source.",
     "What is actually happening, measured, traced to its source."),
    ("It is a map — useful for a specific territory, disposable when it outlives its "
     "usefulness.",
     "It is a map, useful for a specific territory, disposable when it outlives its "
     "usefulness."),
    ("The test is whether they can *change* it — whether you handed over a machine",
     "The test is whether they can *change* it, whether you handed over a machine"),
    ("dread is that channel stuck — the break you can see coming and cannot name",
     "dread is that channel stuck, the break you can see coming and cannot name"),
    ("Most systems fail here — not from missing the decay",
     "Most systems fail here, not from missing the decay"),
    ("emotional alchemy work together — not as two systems, but as one system seen "
     "from two altitudes.",
     "emotional alchemy work together, not as two systems, but as one system seen "
     "from two altitudes."),
    ("Structural clarity, kept in your head, costs nothing — and risks nothing.",
     "Structural clarity, kept in your head, costs nothing, and risks nothing."),
    ("do we maybe want to think about whether…?\"*) — as a flat observation",
     "do we maybe want to think about whether…?\"*), as a flat observation"),
    ("exactly what it was built to do — and it was built for a world we're not in "
     "anymore.*",
     "exactly what it was built to do, and it was built for a world we're not in "
     "anymore.*"),
    ("You get an Architect with no readings — someone modeling a system on the basis",
     "You get an Architect with no readings, someone modeling a system on the basis"),
    ("are feeling their way through it — and it does not fit, and they cannot say why",
     "are feeling their way through it, and it does not fit, and they cannot say why"),
    ("You feel it — a real, accurate, honest signal.",
     "You feel it, a real, accurate, honest signal."),
    ("Not to the Fixer — to the design itself.",
     "Not to the Fixer, to the design itself."),
    ("What stops is the narration — the running commentary that had been reading",
     "What stops is the narration, the running commentary that had been reading"),
    ("Someone says the thing in the meeting — the sentence that writes a whole group",
     "Someone says the thing in the meeting, the sentence that writes a whole group"),
    ("no single instance will look like an evasion — because no single instance is one.",
     "no single instance will look like an evasion, because no single instance is one."),
    ("Look at the sequence, not the verdict — that is the only place the pattern shows",
     "Look at the sequence, not the verdict, that is the only place the pattern shows"),
    ("What they lose is timing — the sense of *now.*",
     "What they lose is timing, the sense of *now.*"),
    ("knowing where the push goes and when to make it — and then, because you also know",
     "knowing where the push goes and when to make it, and then, because you also know"),
    ("Now — what does it actually look like in a real situation?",
     "Now, what does it actually look like in a real situation?"),
    ("Not unnecessary in a dismissive way — unnecessary in a generous way.",
     "Not unnecessary in a dismissive way, unnecessary in a generous way."),
    ("redesign interfaces — all at the same time, with the same amount of force.",
     "redesign interfaces, all at the same time, with the same amount of force."),
    ("You got it stated — moved from something everyone treats as given",
     "You got it stated, moved from something everyone treats as given"),
    ("Not the simplest version that looks good — the simplest version that tells you",
     "Not the simplest version that looks good, the simplest version that tells you"),
    ("Clean Up is the conversion — performed on purpose, in its own slot",
     "Clean Up is the conversion, performed on purpose, in its own slot"),
    ("Draw from your twenty rather than the hundred and twenty — though not all from "
     "one move.",
     "Draw from your twenty rather than the hundred and twenty, though not all from "
     "one move."),
    ("now choose, deliberately — does this get transcended, translated, or neutralized",
     "now choose, deliberately, does this get transcended, translated, or neutralized"),
    ("Five moves, one card, ninety seconds — six of which are the only ones",
     "Five moves, one card, ninety seconds, six of which are the only ones"),
    ("The Architect measures it by obsolescence — a system that still runs",
     "The Architect measures it by obsolescence, a system that still runs"),
    ("and the Emotional Body up close — the sensor that turns a feeling into a spec",
     "and the Emotional Body up close, the sensor that turns a feeling into a spec"),
]


def main():
    p = os.path.join(MS, "ch6.md")
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
