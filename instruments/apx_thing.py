# -*- coding: utf-8 -*-
"""apx_thing.py — `thing` out of the appendices and the front/back matter. 28 sites.

Ruled by Wendell 2026-08-03: *"sweep the marginalia and promote thing to the gate."*

## These surfaced because the gate is wider than the sweep was

Every pass today ran on `manuscript/ch?.md`. `gate.py` reads four surfaces — body,
marginalia, appendices, matter — and the last two were added on 2026-07-29 with a note
that until then *"~10,000 words of shipping prose had never been held to the standing
list."* Promoting `thing` to the banned counter is what made that visible: the body went
to zero and the gate still failed on 28.

**Nothing here is a new defect.** It is prose that was never in scope for the sweep,
which is its own small finding: a sweep scoped to `manuscript/` and a gate scoped to
everything printed will disagree by exactly the appendices every time.

`gate.py` already excludes the backups, the decision records and the review artifacts via
`SHIPPING_APPENDICES`, so all 28 are printed pages.

## Where the answer was already on the page, again

- `APPENDIX_B` — *"say the true thing about where things actually stand"* carried two in
  one clause and goes to *"say what is actually true"*, which is shorter than either.
- `APPENDIX_F` — *"you tear out load-bearing things to feel clean"* → **load-bearing
  parts**. `part` came off the empty list this morning precisely because it is contentful
  here, and this is the sentence that proves it: a load-bearing part is a real object.
- `headmasters_letter` — *"the third week of a first term is still the best thing in my
  year"* → **the best week in my year**. The noun was the subject of the sentence.

## One left as speech

`APPENDIX_C_FIVE_CHANNELS` — *"It ended because we want different things"* is a person
talking themselves through a breakup in a worked Show example. It still moves, to *"we want
different lives"*, because the appendix is a printed practice rather than a transcript and
the plainer noun is truer to what a breakup is about.

Anchors are exact and unique per file. A missed or duplicated anchor aborts with nothing
written.
"""
import io, os, sys

EDITS = [
    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md", [
        ("the working group formed to study the thing that needed to happen last week",
         "the working group formed to study what needed to happen last week"),
        ("which moves things that an individual acting alone cannot",
         "which moves what an individual acting alone cannot"),
        ("When the invisible thing needs a name before anyone can organize around it.",
         "When what is invisible needs a name before anyone can organize around it."),
        ("rather than as the thing that makes the move possible",
         "rather than as what makes the move possible"),
        ("Names the thing everyone present is organized around not saying.",
         "Names what everyone present is organized around not saying."),
        ("can say the thing that is true at every level",
         "can say what is true at every level"),
        ("the direct surgical move on the specific broken thing",
         "the direct surgical move on the specific breakage"),
    ]),
    ("appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md", [
        ("You design the whole thing in your head and never say the load-bearing part",
         "You design all of it in your head and never say the load-bearing part"),
        # Two in one clause; the replacement is shorter than either.
        ("say the true thing about where things actually stand",
         "say what is actually true"),
        ("allyship as another thing to be good at, another way to win",
         "allyship as another skill to be good at, another way to win"),
        ("- **Week 3 — Build one thing.** Make a single condition durable",
         "- **Week 3 — Build.** Make a single condition durable"),
        ("One clean intervention on the thing within your scope.",
         "One clean intervention within your scope."),
    ]),
    ("appendices/APPENDIX_C_FIVE_CHANNELS.md", [
        ("It ended because we want different things.",
         "It ended because we want different lives."),
    ]),
    ("appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", [
        ("I ask you to do things with your emotions that are hard to do when the charge is "
         "already running",
         "I ask you to handle your emotions in ways that are hard when the charge is "
         "already running"),
    ]),
    ("appendices/APPENDIX_F_POLARITY_MAP.md", [
        ("when you are torn between two things that both seem right",
         "when you are torn between two positions that both seem right"),
        ("Both things you could actually *do* in ten minutes",
         "Both actions you could actually *do* in ten minutes"),
        ("the thing you've been protecting starts to curdle",
         "what you've been protecting starts to curdle"),
        # `part` came off the empty list this morning; this is the sentence proving it.
        ("you tear out load-bearing things to feel clean",
         "you tear out load-bearing parts to feel clean"),
        ("the space stays warm and the true thing never gets said",
         "the space stays warm and nothing true gets said"),
    ]),
    ("front_matter/authors_note.md", [
        ("The same thing has happened to helping.",
         "The same has happened to helping."),
        ("how to do all of it without making things worse",
         "how to do all of it without making it worse"),
        ("his name for it is the most useful thing I can hand you before chapter one",
         "his name for it is the most useful idea I can hand you before chapter one"),
        ("and it is the thing I most want you to take from this page",
         "and it is what I most want you to take from this page"),
        ("that is the first thing this book takes off the table",
         "that is the first claim this book takes off the table"),
        ("A thing you cannot look at directly becomes visible",
         "What you cannot look at directly becomes visible"),
    ]),
    ("front_matter/headmasters_letter.md", [
        ("which is what most students come for and is not a small thing",
         "which is what most students come for, and it is not nothing"),
        ("the third week of a first term is still the best thing in",
         "the third week of a first term is still the best week in"),
    ]),
]


def main():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
    for rel, edits in EDITS:
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            p = os.path.join(root, rel.replace("front_matter/", "back_matter/"))
        t = io.open(p, encoding="utf-8").read()
        for i, (a, _b) in enumerate(edits, 1):
            n = t.count(a)
            if n != 1:
                sys.exit("%s E%d matched %d times: %r" % (rel, i, n, a[:60]))
    n = 0
    for rel, edits in EDITS:
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            p = os.path.join(root, rel.replace("front_matter/", "back_matter/"))
        t = io.open(p, encoding="utf-8").read()
        for a, b in edits:
            t = t.replace(a, b)
        io.open(p, "w", encoding="utf-8").write(t)
        n += len(edits)
    print("%d edits applied across %d files" % (n, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
