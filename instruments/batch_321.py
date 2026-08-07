# -*- coding: utf-8 -*-
"""The remaining 3-2-1 blocks: ch7, ch8, the ch3/ch4 daemons, and ch2's plant.

Approved by Wendell 2026-08-01 after a review pass and /no-ai-slop over the batch.

Seven blocks. ch7 and ch8 get the pair they were missing; ch3 and ch4 get the daemon
passes they never had, since they were built before the daemon half of the design existed;
ch2 gets one sentence naming the shape it already demonstrates on the Protector.

Placement follows what ch4-ch6 settled. The figure pass sits late in Section 4, after the
chapter's ecology and before its closing move. The daemon pass closes the daemon
exposition, before the polarity subsection that follows it. ch3 has no such subsection, so
its daemon pass sits at the close of the daemon material instead.

Three slop findings were fixed in draft and are not in what lands here. ch7's opener had
drifted into ch6's shape -- both were about a word the reader uses for the figure -- and
the deficit-to-figure hinge had become four near-variants of one sentence across ch5-ch8.
Near-variation is worse than either repetition or freshness: it reads as carelessness
rather than convention. ch7 and ch8 now reach the figure by different constructions.

Anchors verified unique by literal count. Aborts on any miss or duplicate, and writes
nothing until every anchor in the batch has resolved.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

blocks = {}
raw = io.open(os.path.join(ROOT, 'drafts', 'APPROVED_batch_321_2026-08-01.md'),
              encoding='utf-8').read()
for chunk in raw.split('=== ')[1:]:
    key, body = chunk.split(' ===', 1)
    blocks[key.split('.')[0].strip()] = body.strip()

# (chapter, block key, anchor, mode)
#   before : insert the block above the anchor, followed by a rule
#   after  : append the block to the paragraph the anchor ends
JOBS = [
    (7, 'A', "## Section 5: The Victim, Up Close", 'before'),
    (7, 'B', "### Care and Impact: Why the Ledger Always Sounds Like Care", 'before'),
    (8, 'C', "### *The Walk Back: Coming Down Without Losing What You Found*", 'before'),
    (8, 'D', "### Which Game and Which Altitude: Why the Defect Story Always Sounds Like Humility", 'before'),
    (3, 'E', "### What You Take Out of the Forest", 'before'),
    (4, 'F', "### Force and Restraint: Why the Audit Is So Hard to Catch", 'before'),
    (2, 'G', "stops running every hard conversation as though your life were on the line.", 'after'),
]

# Resolve every anchor first; a batch that writes three files and then aborts is worse
# than one that writes none. Learned on the polarity pass, which aborted mid-run.
#
# The first version of this cached each file's TEXT alongside its anchor, and two jobs
# against the same file both captured the pre-write content -- so ch7's daemon pass
# overwrote its figure pass and ch8's did the same, silently, while the script reported
# all seven applied. Resolve anchors here; re-read at write time.
for ch, key, anchor, mode in JOBS:
    fp = os.path.join(ROOT, 'manuscript', 'ch%d.md' % ch)
    n = io.open(fp, encoding='utf-8').read().count(anchor)
    if n != 1:
        raise SystemExit('%s %d: ch%d %r' % ('MISS' if n == 0 else 'DUPE', n, ch, anchor[:60]))
    if key not in blocks:
        raise SystemExit('no block %s in the approved draft' % key)

for ch, key, anchor, mode in JOBS:
    fp = os.path.join(ROOT, 'manuscript', 'ch%d.md' % ch)
    t = io.open(fp, encoding='utf-8').read()
    block = blocks[key]
    if mode == 'before':
        t = t.replace(anchor, block + "\n\n---\n\n" + anchor, 1)
    else:
        t = t.replace(anchor, anchor + " " + block, 1)
    io.open(fp, 'w', encoding='utf-8').write(t)
    print('ch%-2d %s  %d words' % (ch, key, len(block.split())))
