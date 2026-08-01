# -*- coding: utf-8 -*-
"""ch3: the 3-2-1 full teaching. Step 1 of SPEC_321_PER_CHAPTER_2026-08-01 section 9.

Approved by Wendell 2026-08-01 ("Apply this. This is it").

Replaces the block that named 3-2-1 and deferred the practice to Chapter 4 -- the
deferral the spec was written to close. The new block is the small version: it leans on
Appendix E for the full process and worked examples rather than restating them, per
Wendell's ruling that the chapter carries "a small version of that, which is in the
appendix."

Also lands three corrections he made while reading:

  - the step is BE IT, not OWN IT. Appendix E's body already taught "Don't report about
    it -- *be* it" under a label that said Own It.
  - the magic words "There is a part of me that" open the THIRD-person phase. They are a
    statement about a part, so the part cannot speak them.
  - no prescribed somatics. The old line told the reader what tightened their jaw, inside
    the chapter that teaches them to locate their own charge.

Anchored on the whole block, which occurs once. Aborts on a miss or a duplicate.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, os.pardir, 'manuscript', 'ch3.md')
t = io.open(p, encoding='utf-8').read()

OLD = """### The 3-2-1 Practice — Finding the Shadow Before It Finds You

Before you can alchemize, you need to see what you're working with.

The WAVE-Spiral works with charge you're already feeling in your body: fear in the meeting, sadness after a rupture, anger that arrived on schedule. A lot of the charge that drains allyship doesn't arrive that way. It arrives dressed as someone else. The colleague who makes your jaw tighten. The movement leader whose certainty feels like a personal attack. The person who has become, in your inner world, a cartoon.

That charge is projection. Projection is shadow work waiting to happen.

The 3-2-1 shadow method brings what you projected outward back into the system, where you can work with it. This book applies it as follows.

The **3-2-1 practice** metabolizes it in three vantage points: observe the charged figure in third person (3), talk with it in second person (2), own it as yours in first person (1). The energy you spent on them returns to your system, available for the WAVE-Spiral.

When the charge is in a **person**, a figure who makes your jaw tighten, start with 3-2-1. You'll practice it fully in Chapter 4. Do WAVE first when the trigger arrives as a *feeling already in your body*. Many hard moments need both.

| Stuck because… | Tool |
|----------------|------|
| Charge is in a *person* | 3-2-1 (Chapter 4) |
| Stuck between two *rights* | Polarity Map (Chapter 4 → Chapter 7) |
| Charge is in *body* now | WAVE-Spiral |

*Full process and source (Ken Wilber, Integral Life Practice): Appendix E: The 3-2-1 Shadow Process. First practice: Chapter 4.*"""

NEW = io.open(os.path.join(HERE, os.pardir, 'drafts',
                           'APPROVED_ch3_321_teaching_2026-08-01.md'),
              encoding='utf-8').read().rstrip('\n')

n = t.count(OLD)
if n == 0:
    raise SystemExit('MISS: the ch3 3-2-1 block did not match')
if n > 1:
    raise SystemExit('DUPE %d: anchor is not unique' % n)
io.open(p, 'w', encoding='utf-8').write(t.replace(OLD, NEW, 1))
print('applied 1')
