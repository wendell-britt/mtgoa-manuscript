# -*- coding: utf-8 -*-
"""Ch2 school-as-teaching-device passages. Approved by Wendell 2026-08-01.

Two inserts, both in his own frame voice, per the split he ruled: Section 5 carries why
the device exists, Section 10 carries how to read it. See SPEC_CH2_FRAME_2026-08-01.md.

Ch2 carries no marginalia since that spec, so this runs directly on the file with no
strip/apply cycle around it.
"""
import io, os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir,
                 'manuscript', 'ch2.md')
t = io.open(p, encoding='utf-8').read()
E = []

# Section 5 — the argument for a somewhere, sitting between "a game teaches differently"
# and the navigation line that closes the pedagogy run.
E.append(("""Chapter 1 put the joystick in your hands. This chapter teaches you how to walk the book.""",
"""A game also needs a somewhere. You do not make a move in the abstract. You make it in a place, against people who want something, under rules that hold still long enough for you to test them. So I set the six chapters ahead in one: a school that does not exist, on a ship, where six people teach six different ways of helping and argue with each other about the rest.

The school is somewhere to stand while you practice, and that is the whole of its job. Nobody will quiz you on the plot. A teacher who has to answer for what her method costs will tell you more than a framework that answers to nobody, and the only route I found to letting you argue with a Face was to give it a mouth that argues back.

Chapter 1 put the joystick in your hands. This chapter teaches you how to walk the book."""))

# Section 10 — how to read the apparatus, placed after the two routes so the reader takes
# it through the door with them. The reveal in ch8 is deliberately not set up here:
# MARGIN_ARC rule 2 says nothing may pay for it in advance.
E.append(("""Either way, the Forest is ahead and your hands are on the joystick. The only move left is through.""",
"""Turn the page and a letter is waiting, from the Headmaster of that school. After it, six chapters, and each opens with a treatise by the person who runs one of the six schools: their method, in their voice, carrying their bias and their quarrel with the other five. It runs as ordinary text until you reach a signature at the close of its third section. That is where a submitted document signs itself. Everything past that signature is me.

The boxed inserts belong to the school as well: an admissions page saying who they take and what it costs, students and citizens on the record about what the teaching did to them, and a margin in a hand that never signs.

Read those pages the way you would read a teacher you have not made up your mind about. Six people each solved one part of this and cannot agree on the rest, and I would rather hand you the argument than the summary.

Either way, the Forest is ahead and your hands are on the joystick. The only move left is through."""))

for i, (a, b) in enumerate(E, 1):
    n = t.count(a)
    if n == 0:
        raise SystemExit('MISS #%d: %r' % (i, a[:90]))
    if n > 1:
        raise SystemExit('DUPE %d #%d: %r' % (n, i, a[:90]))
    t = t.replace(a, b, 1)
io.open(p, 'w', encoding='utf-8').write(t)
print('applied %d' % len(E))
