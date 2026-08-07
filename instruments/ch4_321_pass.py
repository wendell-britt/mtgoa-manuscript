# -*- coding: utf-8 -*-
"""ch4: the 3-2-1 pass. Step 2 of SPEC_321_PER_CHAPTER_2026-08-01 section 9.

Approved by Wendell 2026-08-01.

ch4 is the one chapter that gets shorter: its teaching load moved to ch3, so the block
drops from 640 words to 356. What stays is what ch4 alone was carrying -- the figure
wearing somebody's face, and the guardrail that owning your split is not a verdict on
their innocence, which matters more here than anywhere because the target is a real
person.

Per Wendell 2026-08-01, ch4 must deliver on ch3 rather than repeat it: "the specific move
on how to take the charge to people, especially for whom we have negative feelings." One
new line makes that explicit, and the practice hands the reader from their own deficit to
the face they have put on its opposite.

Four defects fixed while relocating:

  ch4:477  "what they do that tightens your jaw"    -> asks where the charge sits
  ch4:488  "Don't polite the dialogue"              -> cut; polite is not a verb and it
                                                       judged the reader preemptively
  ch4:494  "STEP 1: OWN IT"                         -> BE IT
  ch4:501  "Capture what landed. /shadow/321"       -> the book's BAR line

The last was the only app deep-link left in the manuscript body. shipcheck reports app
routing clear because it scans for `bars-engine` rather than for paths, so this sat under
the instrument.

Bounded by its own heading and its closing line, both unique. Aborts on a miss or a dupe.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, os.pardir, 'manuscript', 'ch4.md')
t = io.open(p, encoding='utf-8').read()

START = "### 3-2-1 — Reclaim the Line You Projected"
END = "Back to the chapter. You didn't become the villain. You recovered the capacity you split off."

for anchor in (START, END):
    n = t.count(anchor)
    if n != 1:
        raise SystemExit('%s %d: %r' % ('MISS' if n == 0 else 'DUPE', n, anchor[:60]))

i = t.index(START)
j = t.index(END) + len(END)

NEW = io.open(os.path.join(HERE, os.pardir, 'drafts',
                           'APPROVED_ch4_321_pass_2026-08-01.md'),
              encoding='utf-8').read().rstrip('\n')

io.open(p, 'w', encoding='utf-8').write(t[:i] + NEW + t[j:])
print('applied 1')
