# -*- coding: utf-8 -*-
"""ch6: the figure pass and the daemon pass. Step 4 of SPEC_321_PER_CHAPTER section 9.

Approved by Wendell 2026-08-01.

The figure comes from ch6's own polarity section rather than from invention: "Agency
language has warnings attached to it at this altitude ... Structure language has none."
So the person an Architect-reader is charged at is the one who names a human being out
loud, and the word that gets used on them is `simplistic`.

The daemon pass borrows two things from the portrait instead of restating them: the
conversion menu (proposal, risk register, retrospective) is the portrait's own list, and
the naming instruction points at the Collapse, where ch6 already demonstrates the move --
"Named, it is a part of me that is afraid. Unnamed, it is simply what I think about the
design." Step 3 is still the reader's own daemon, per the correction in section 2.

Two slop findings were caught in draft and are not in what lands here: the framing opened
"It is doing work for you, and this is where you take the work back", which was both an
expletive opener and a near-copy of ch5's framing, and the hinge "That part has an
opposite, and you have already given the opposite a face" was word-for-word ch5's. The
variance rule lets scaffolding repeat and does not let framing prose repeat; both had
drifted across that line.

Both anchors verified unique. Aborts on a miss or a duplicate.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
p = os.path.join(ROOT, 'manuscript', 'ch6.md')

draft = io.open(os.path.join(ROOT, 'drafts',
                             'APPROVED_ch6_321_passes_2026-08-01.md'),
                encoding='utf-8').read()
figure, daemon = [s.strip() for s in draft.split('===SPLIT===')]

t = io.open(p, encoding='utf-8').read()

E = [
    ("### Name One Unstated Assumption, in the Village", figure),
    ("### Structure and Agency: Why the Fix Always Sounds Like Systems Thinking", daemon),
]

for i, (anchor, block) in enumerate(E, 1):
    n = t.count(anchor)
    if n != 1:
        raise SystemExit('%s %d #%d: %r' % ('MISS' if n == 0 else 'DUPE', n, i, anchor))
    t = t.replace(anchor, block + "\n\n---\n\n" + anchor, 1)

io.open(p, 'w', encoding='utf-8').write(t)
print('applied %d' % len(E))
