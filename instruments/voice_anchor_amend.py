# -*- coding: utf-8 -*-
"""
voice_anchor_amend.py — the four amendments to specs/VOICE_ANCHOR.md.

Approved by Wendell 2026-08-02, drafted in console first. The agency audit found
that the anchor names the effect each passage protects and never the mechanism
that produces it, so anyone matching an anchor copies the mechanism along with
the effect — and at anchor 3 the mechanism is reified agency.

House pattern: exact anchors, writes nothing if any anchor misses or duplicates.

    python3 instruments/voice_anchor_amend.py --dry
    python3 instruments/voice_anchor_amend.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
TARGET = os.path.join(ROOT, "specs", "VOICE_ANCHOR.md")

EDITS = [
    # ---- 1. Delivers via, anchor 1
    ("""**Protects:** the willingness to end a heavy paragraph on something small and dry
rather than something profound. *Less fun* is two words after a sixty-word
sentence, and no measurement instrument can see the rhythm it makes.""",
     """**Protects:** the willingness to end a heavy paragraph on something small and dry
rather than something profound. *Less fun* is two words after a sixty-word
sentence, and no measurement instrument can see the rhythm it makes.

**Delivers via:** first person. *I* holds every verb in the passage — gave, saw,
was holding, ended up doing. The turn lands on the author, and nothing abstract
is asked to carry it."""),

    # ---- 2. Delivers via, anchor 2
    ("""**Protects:** naming your own bad prose inside good prose, in an aside, without
breaking stride. The admission is parenthetical *and* the sharpest sentence in
the paragraph.""",
     """**Protects:** naming your own bad prose inside good prose, in an aside, without
breaking stride. The admission is parenthetical *and* the sharpest sentence in
the paragraph.

**Delivers via:** the author's chair. *I wrote whole chapters of this book
standing at it.* The indictment has a person in it, which is what makes it cost
something."""),

    # ---- 3. anchor 3: the warning, and the completed targeting rule
    ("""**Protects: the humor.** This is the Humor Grid's **Jerk** archetype working on
the page — mocking the process that took someone's joystick, never the person.
It is in this set deliberately: **an anchor with no comedy in it will let the
Voice Guardian approve a book that has stopped being funny**, because nothing in
its comparison set would show that anything was lost.""",
     """**Protects: the humor.** This is the Humor Grid's **Jerk** archetype working on
the page — mocking the process that took someone's joystick, never the person.
It is in this set deliberately: **an anchor with no comedy in it will let the
Voice Guardian approve a book that has stopped being funny**, because nothing in
its comparison set would show that anything was lost.

**Delivers via: ⚠️ collective-as-mind — and that mechanism is NOT protected.**
*The village learned* · *the workshops teach* · *the workshops promise.* The joke
is protected. The grammar carrying it is not. Anchor 4 is the same archetype
delivered clean, and it is funnier, because the agent is specific.

**The targeting rule, completed (amended 2026-08-02).** Mock the process that
took someone's joystick, never the person — **and seat the mockery on a subject
that can hold the verb.** The original rule forbids the only obvious subject and
names no replacement, so the process arrives in the subject slot by default.
That is not a stylistic accident; it is the mechanism that produced 131 agency
sites in a manuscript with four linters and a green gate. Licensed carriers, in
order of preference:

1. **a named part** — *The Fixer is happy to take him.* Funniest, most specific.
2. **the author's chair** — *I wrote whole chapters standing at it.*
3. **the persons, plural** — the villagers, the trainers, the people in the room.
4. **a machine, mechanical verbs only** — *the structure pays out nothing for optics.*

**Known limit.** Pluralizing does not rescue this passage on its own. *The
workshops* is already plural and is not a population, so the sentence carrying
the actual joke is untouched by a number change and needs a different move."""),

    # ---- 4. Delivers via, anchor 4
    ("""**Protects:** named interior parts treated as people, and a close that judges
without softening. *Laundered into a work order* is the register's high-water
mark for a verb.""",
     """**Protects:** named interior parts treated as people, and a close that judges
without softening. *Laundered into a work order* is the register's high-water
mark for a verb.

**Delivers via:** a named part. *The Fixer is happy to take him* — a licensed
interior agent with its mechanism in canon, not an abstraction borrowing a mind.
**This anchor is the model for anchor 3.** Both mock a process; this one seats
the mockery on something that can hold the verb, and it is the better joke for
it."""),

    # ---- 5. Delivers via, anchor 5
    ("""**Protects:** a seven-word sentence that inverts what the reader had assumed for
a whole section. Compression as an argument.""",
     """**Protects:** a seven-word sentence that inverts what the reader had assumed for
a whole section. Compression as an argument.

**Delivers via:** no agent claimed. *The view* and *the triumph* are named
without being asked to act. Compression works here because nothing in the
sentence has to be traced."""),

    # ---- 6. the counter-anchor
    ("""---

## What the set shows, read together""",
     """---

## Counter-anchor · `ch7:138` — the passage that passes every check and still fails

**Added 2026-08-02.** The set's own logic runs both ways: an anchor set with no
comedy in it lets the Guardian approve a book that has stopped being funny, and
an anchor set with no failure in it lets the Guardian approve prose that has
stopped being **traceable**. This is the negative space.

> …offered as information, once, to **a field that is then free to answer**.

*(As it stood before 2026-08-02. Now: "to the people who are then free to answer.")*

**Fails on:** who holds the verb. Specific, rhythmic, authoritative, warm,
naturally-syntaxed — it scores well on all five of the Guardian's original
criteria, and it is Chapter 7 defining its own key term in a sentence where the
field answers. It passed every instrument and every gate in this project until
the agency audit read it by hand.

**Why it is here:** because nothing else in the comparison set shows the
Guardian what this failure looks like, and this failure is invisible to rhythm.
Three of the ten known breaks in the village repair are syllable-neutral. **The
read-aloud pass cannot catch them.** An anchor set that only demonstrates
liveness will keep approving untraceable prose forever.

---

## What the set shows, read together"""),

    # ---- 7. the Guardian rubric
    ("""For each original/revision pair, rule **ACCEPT · RESTORE ORIGINAL · REVISE
MINIMALLY**, and assess specificity, rhythm, authority, emotional temperature and
natural syntax in one sentence.""",
     """For each original/revision pair, rule **ACCEPT · RESTORE ORIGINAL · REVISE
MINIMALLY**, and assess specificity, rhythm, authority, emotional temperature,
natural syntax, **and who holds the verb** in one sentence."""),
]


def main():
    dry = "--dry" in sys.argv
    t = io.open(TARGET, encoding="utf-8").read()

    for before, after in EDITS:
        n = t.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\n"
                     "Nothing written." % (n, before.splitlines()[0][:78]))

    for before, after in EDITS:
        t = t.replace(before, after, 1)

    if dry:
        print("--dry: %d amendments verified, nothing written." % len(EDITS))
        return 0

    io.open(TARGET, "w", encoding="utf-8").write(t)
    print("wrote specs/VOICE_ANCHOR.md — %d amendments." % len(EDITS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
