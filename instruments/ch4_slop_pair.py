# -*- coding: utf-8 -*-
"""ch4: the two slop findings in the prose this branch relocated. Approved 2026-08-01.

Both predate the session and both came through the ch4 compression unread, which is my
miss -- I moved the block without running the slop pass over the sentences I was keeping.

1. Binary contrast. "The Challenger in distortion controls. The real Challenger protects."
   is a paired opposition staging a distinction rather than holding it. Synthesized into
   one sentence on the chapter's own axis, using the chapter's own noun: the fire is what
   ch4 calls the Challenger's charge from Section 1 onward.

2. Formatting slop, twice in four lines: bold sprinkled mid-sentence to carry a contrast
   the syntax should carry. "3-2-1 owns **your** split, not **their** innocence" and
   "fighting in **them** that's actually **in you.**" Restructured so position does the
   work; the second is absorbed by fix 1.

The colon in "stay real: 3-2-1 owns" goes with them -- it was a third reveal.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, os.pardir, 'manuscript', 'ch4.md')
t = io.open(p, encoding='utf-8').read()

OLD = """None of this lets real harm off the hook. It reclaims the energy you have spent on a cartoon. Real harm and real accountability stay real: 3-2-1 owns **your** split, not **their** innocence.

The Challenger in distortion controls. The real Challenger protects. 3-2-1 finds which one you're fighting in **them** that's actually **in you.**"""

NEW = """None of this lets real harm off the hook. It reclaims the energy you have spent on a cartoon. Real harm and real accountability stay real. What 3-2-1 owns is your split, and it makes no claim about their innocence.

The same fire controls or protects depending on where it is aimed, and 3-2-1 finds which one you are fighting in them that is actually in you."""

n = t.count(OLD)
if n != 1:
    raise SystemExit('%s %d' % ('MISS' if n == 0 else 'DUPE', n))
io.open(p, 'w', encoding='utf-8').write(t.replace(OLD, NEW, 1))
print('applied 1')
