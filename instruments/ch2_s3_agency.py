# -*- coding: utf-8 -*-
"""ch2_s3_agency.py — the agency pass over ch2 Section 3.

Ruled by Wendell 2026-08-02: "fix the agency problem in Section 3", then four corrections
to the first draft, all of which are in these replacements.

Eight edits. The defect throughout is the one he named on the ch2 opening: a subject that
cannot act. A loop that runs itself, a default that installs itself, a signal that leaves,
a question that waits, exhaustion that lives somewhere, work that happens on its own, and
a four-pair grid whose actors are *modes*, *moves* and *feedback* with the reader present
in one pair out of four.

His four corrections, and what each one fixed:

**E1 was wrong on content, not grammar.** The first draft only tidied the loop's syntax.
Wendell: *"I don't know what this ch2:138 is doing and what it's describing and why we
need to think of it as a loop. The vicious cycle is that they are spending so much energy
trying to seem right and seem good that they are blind to the opportunities in front of
them."* Rebuilt on that, and the rumination-loop framing is gone.

**E1 also carried the failure this whole session keeps producing.** The draft opened *"You
know the loop"* — `MANUSCRIPT_FILE_CANON:154` broken in four words. Wendell: *"They don't
know the loop. Whatever produces this assertion has got to go."* What produces it:
promoting an agentless abstraction needs a subject, and the nearest available subject is
always the reader. The replacement uses a conditional instead — *Run both at once and…* —
which asserts nothing about anybody's history.

**E5.** *"'leaves nothing over' is nonsense. Ungrammatical. Doesn't mean anything. Trying
to seem good takes so much energy that there's not enough energy available to actually
help people. pretending to be good, while punishing yourself for not, are two expensive
processes that get in the way of you showing up effectively."* Both processes now named.
E1 and E5 were saying the same thing after the rebuild, so they are split: **E1 is the cost
to perception** (you cannot see the openings), **E5 is the cost to capacity** (nothing left
for the person in front of you).

**E8.** *"In the Forest you play to understand deeper truths and increase your capacity in
a sustainable way"* — his line, in the grid.

The grid's third pair was already right, so the other three are made to match it rather
than the reverse. `optimizes for` and `data for development` were the only consultant-speak
in the chapter, and `play for` is the book's own frame.

Anchors are exact and unique, and the two-space line breaks inside the grid are preserved.
A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = []

# E1 — the vicious cycle, rebuilt on what Wendell said it is about.
E.append((
    "A familiar loop keeps running: the moment after a hard conversation spent rehearsing "
    "what you should have said, the 2am inventory of what went wrong, the same pattern "
    "surfacing in a different building, with different people, wearing different faces. "
    "That loop is the edge of the Forest.",

    "Trying to seem right costs energy. Trying to seem good costs more. Run both at once "
    "and most of the attention goes to how you are landing. Whoever you came to help gets "
    "what is left.\n"
    "\n"
    "Whatever the situation, part of you stays braced for the judgment. That vigilance "
    "costs you presence, and if you cannot be present with them you cannot ally with "
    "them.\n"
    "\n"
    "That gap, between the people in front of you and how much of you is there to meet "
    "them, is the edge of the Forest."))

# E2 — a default nobody installs.
E.append((
    "Maybe, somewhere in all of it, holding still became the default.",
    "Maybe, somewhere in all of it, you started holding still by default."))

# E3 — a signal that leaves on its own. "No one reports back" is a third party who really
# acts, which is one of the four legal subjects when an abstraction has to go.
E.append((
    "At some point the signal drops out. No clear way to tell if any of it is working, or "
    "even what working would look like.",

    "No one reports back. You cannot tell whether any of it is working, or what working "
    "would even look like."))

# E4 — a question that waits. prose_diet's AGENT detector has `question` in its noun list
# and does not have `waits` in its verb list, so this one was invisible to it as well.
E.append((
    "Underneath the effort waits a question worth sitting with:",
    "All that effort has been sitting on top of one question."))

# E5 — the two expensive processes, in Wendell's terms.
E.append((
    "Wanting to be good was never the problem. Trying to seem good takes the whole body. "
    "That leaves nothing over. The face you're holding in place and the face underneath it "
    "run at the same time, and the exhaustion actually lives in that split.",

    "Wanting to be good was never the problem. Performing it costs a great deal, and "
    "punishing yourself for falling short of the performance costs a great deal more. Run "
    "both and you are funding two expensive processes, neither of which does anything for "
    "the person in front of you."))

# E6 — work that happens by itself.
E.append((
    "No one in there needs you to seem good, and that makes it the only place where the "
    "real work can happen.",

    "No one in there needs you to seem good, so you can do the real work there and "
    "nowhere else."))

# E7 — the zombie subject.
E.append((
    "The work of the Forest is to meet those parts, not to silence them. To find out where "
    "they came from, what they were protecting, and whether they still belong to you.",

    "In the Forest you meet those parts instead of silencing them. You find out where they "
    "came from, what they were protecting, and whether they still belong to you."))

# E8 — the grid. Trailing two spaces are markdown line breaks and must survive.
E.append((
    "**Village mode** optimizes for appearance, speed, and immediate social safety.  \n"
    "**Forest mode** optimizes for truth, integration, and durable capacity.\n"
    "\n"
    "In the Village, the core move is impression management.  \n"
    "In the Forest, the core move is pattern recognition and repurposing.\n"
    "\n"
    "In the Village, you ask: *How do I look right now?*  \n"
    "In the Forest, you ask: *What keeps repeating in me, and what does it cost if I keep "
    "running it?*\n"
    "\n"
    "In the Village, feedback feels like threat to identity.  \n"
    "In the Forest, feedback becomes data for development.",

    "In the Village you play for appearance, speed, and getting through the next hour "
    "safely.  \n"
    "In the Forest you play to understand deeper truths and to build capacity you can "
    "sustain.\n"
    "\n"
    "In the Village you manage the impression.  \n"
    "In the Forest you catch the pattern and put it to work.\n"
    "\n"
    "In the Village you ask: *How do I look right now?*  \n"
    "In the Forest you ask: *What keeps repeating in me, and what does it cost if I keep "
    "running it?*\n"
    "\n"
    "In the Village you hear feedback as a threat to who you are.  \n"
    "In the Forest you hear it as information about what to build."))


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
