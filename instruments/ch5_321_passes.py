# -*- coding: utf-8 -*-
"""ch5: the figure pass and the daemon pass. Step 3 of SPEC_321_PER_CHAPTER section 9.

Approved by Wendell 2026-08-01.

Two corrections of his are carried here, and the second falsifies a load-bearing claim in
the spec.

1. "the form" was vague. The territory now names a concrete thing and the person the
   betrayal is against, which is ch5's own account of it: "You keep the forms because
   dropping them would feel like a betrayal of someone whose effort you still respect."

2. The daemon pass does NOT get Step 3 for free. Wendell: "The players need to describe
   the fixer/healer as it shows up for THEM not the generic one." SPEC section 2 claimed
   Section 5's portrait writes Step 3 and called that "the single fact that keeps the whole
   change inside a page budget." Wrong: the portrait describes the generic daemon, and
   reading a good description of a Fixer-Healer is not having faced your own. The portrait
   still earns its keep by telling the reader what to look for -- postponing versus
   substituting -- which is why Step 3 here is four questions instead of a paragraph of
   instruction. Daemon pass 96 -> 171 words; the spec is corrected in the same commit.

Placement. The figure pass sits before "Name One Inheritance Out Loud", so the inner work
precedes the village move, mirroring ch4 where 3-2-1 precedes "Name the Voice". The daemon
pass sits at the close of the portrait, before the Honor/Reform subsection, which is where
the daemon exposition actually ends.

Both anchors verified unique. Aborts on a miss or a duplicate.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
p = os.path.join(ROOT, 'manuscript', 'ch5.md')

draft = io.open(os.path.join(ROOT, 'drafts',
                             'APPROVED_ch5_321_passes_2026-08-01.md'),
                encoding='utf-8').read()
figure, daemon = [s.strip() for s in draft.split('===SPLIT===')]

t = io.open(p, encoding='utf-8').read()

E = [
    ("### Name One Inheritance Out Loud, in the Village", figure),
    ("### Honor and Reform: Why the Repair Always Sounds Like Reform", daemon),
]

for i, (anchor, block) in enumerate(E, 1):
    n = t.count(anchor)
    if n != 1:
        raise SystemExit('%s %d #%d: %r' % ('MISS' if n == 0 else 'DUPE', n, i, anchor))
    t = t.replace(anchor, block + "\n\n---\n\n" + anchor, 1)

io.open(p, 'w', encoding='utf-8').write(t)
print('applied %d' % len(E))
