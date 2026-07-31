# -*- coding: utf-8 -*-
"""Punch-up finder — Part 2 of the Revision Instrument, mechanised.

`marginalia/specs/REVISION_INSTRUMENT.md` is the generative half of the humor
system: fourteen named colors, and six diagnostic checks that *select* one. The
spec is explicit that the diagnosis is not decoration — it picks the color.

This runs the mechanical checks against the body text and returns the paragraphs
where the instrument's own table says a color is available. It answers **where
is the book flat and which dial is indicated**, which is the question a hostile
read asks.

The six checks, from the spec:

    1  Who is in it?              named person acting, or nobody
    2  Which color is running?    name it, or write NONE
    3  Demonstrate or describe?   is something happening, or being explained
    4  Abstraction nouns in subject position — count them
    5  Sentence lengths — flag three consecutive over 25
    6  Negations — is the negated thing still true at the end?

Checks 2 and 6 need judgment and are left to a human; 1, 3, 4 and 5 are
mechanical and are what this reports. The spec's own routing table then names
the dial:

    nobody present, about a system or institution  ->  Cult Leader, Symmetry
    nobody present, about the author's own failure ->  Testimony, Clown
    correct but inert, no music                    ->  Conceit, Reversed, Deadpan
    stacked concepts, lecture creep                ->  Ladder / +NAVAL

**What this cannot do.** It cannot tell whether a paragraph is already funny, and
a flat paragraph is not automatically a defect — exposition has to happen
somewhere. Every hit is a candidate for a human to rule on, exactly as the spec
requires: three revisions, one color each, each with a COST line.

    python3 instruments/punchup.py            # ranked opportunities
    python3 instruments/punchup.py -n 25      # how many to show
    python3 instruments/punchup.py --ch 5     # one chapter
"""
import io
import re
import sys
import glob

N = 20
if '-n' in sys.argv:
    N = int(sys.argv[sys.argv.index('-n') + 1])
ONLY = None
if '--ch' in sys.argv:
    ONLY = int(sys.argv[sys.argv.index('--ch') + 1])

# check 1 — somebody present and acting
NAMED = re.compile(
    r'\b(Meera|Bea|Marcus|Jordan|Corin|Maera|Sera|Irix|Elian|Thalen|Wendell)\b'
    r'|\b(a|the|your|his|her|my) (coworker|colleague|friend|manager|sibling|partner|'
    r'brother|sister|neighbour|neighbor|client|student|teammate)\b'
    r'|\b(somebody|someone|he|she|they) (said|asked|told|answered|walked|sat|called)\b')
FIRST = re.compile(r'\bI\b|\bmy\b|\bme\b')

# check 3 — a scene happening, rather than a concept being explained
SCENE = re.compile(r'\b(said|asked|walked|sat|handed|looked|answered|arrived|'
                   r'in the meeting|at the table|on the call|that afternoon|last week)\b')

# check 4 — abstraction in the subject slot
ABSTRACT = re.compile(
    r'^(The|A|An) ('
    r'\w*(tion|ment|ness|ity|ance|ence|ism|ship|hood)|'
    r'practice|process|question|difference|problem|answer|point|work|move|thing'
    r')\b', re.I)

# institution vocabulary — routes a flat paragraph to Cult Leader rather than Clown
INSTITUTION = re.compile(
    r'\b(committee|policy|process|onboarding|charter|org|organisation|organization|'
    r'team|workshop|training|meeting|system|institution|board|leadership|HR)\b', re.I)


def paras(path):
    """Body paragraphs only. Margin, headings, tables and lists excluded."""
    raw = io.open(path, encoding='utf-8').read()
    out, buf, start, inblk = [], [], 1, False
    for n, line in enumerate(raw.split('\n'), 1):
        if '<!--' in line:
            inblk = True
        s = line.strip()
        skip = (inblk or s.startswith('>') or s.startswith('#') or
                s.startswith('|') or s.startswith('-') or s.startswith('*') or
                re.match(r'^\d+\.', s))
        if '-->' in line:
            inblk = False
            buf, start = [], n + 1
            continue
        if not s or skip:
            if buf:
                out.append((start, ' '.join(buf)))
                buf = []
            start = n + 1
            continue
        if not buf:
            start = n
        buf.append(s)
    if buf:
        out.append((start, ' '.join(buf)))
    return [(n, p) for n, p in out if len(p.split()) >= 45]


def sents(p):
    return [x for x in re.split(r'(?<=[.!?])\s+', p) if x.strip()]


def assess(p):
    S = sents(p)
    L = [len(x.split()) for x in S]
    nobody = not (NAMED.search(p) or FIRST.search(p))
    describing = not SCENE.search(p)
    abstract = sum(1 for x in S if ABSTRACT.match(x.strip()))
    longrun = any(L[i] > 25 and L[i+1] > 25 and L[i+2] > 25 for i in range(len(L) - 2))
    score = (2 if nobody else 0) + (1 if describing else 0) + abstract + (2 if longrun else 0)
    if nobody and INSTITUTION.search(p):
        dial = '+CULT LEADER / Symmetry'
    elif nobody:
        dial = 'Testimony / +CLOWN'
    elif longrun:
        dial = 'Ladder / +NAVAL'
    else:
        dial = 'Conceit / Reversed / Deadpan'
    return score, nobody, describing, abstract, longrun, dial


def main():
    rows = []
    for path in sorted(glob.glob('manuscript/ch*.md'),
                       key=lambda q: int(re.search(r'ch(\d+)', q).group(1))):
        ch = int(re.search(r'ch(\d+)', path).group(1))
        if ONLY and ch != ONLY:
            continue
        for n, p in paras(path):
            sc, nob, des, ab, lr, dial = assess(p)
            if sc >= 4:
                rows.append((sc, ch, n, nob, des, ab, lr, dial, p))
    rows.sort(key=lambda r: -r[0])
    print('=== PUNCH-UP OPPORTUNITIES — Revision Instrument Part 2 ===')
    print('%-4s %-6s %-5s %-6s %-5s %-4s %-5s %s'
          % ('sc', 'ch:line', 'nobody', 'descr', 'abst', 'long', '', 'indicated dial'))
    print('-' * 92)
    for sc, ch, n, nob, des, ab, lr, dial, p in rows[:N]:
        print('%-4d ch%-2d:%-4d %-6s %-6s %-5d %-5s %s'
              % (sc, ch, n, 'YES' if nob else '.', 'YES' if des else '.', ab,
                 'YES' if lr else '.', dial))
        print('      %s' % p[:150])
    print('-' * 92)
    print('%d paragraphs scored >=4 of a possible ~8.' % len(rows))
    by = {}
    for r in rows:
        by[r[1]] = by.get(r[1], 0) + 1
    print('by chapter: ' + '  '.join('ch%d:%d' % (c, by[c]) for c in sorted(by)))
    print('\nCandidates, not verdicts. A flat paragraph is not automatically a defect —')
    print('exposition has to happen somewhere. The spec asks for three revisions per')
    print('paragraph, one color each, every one carrying a COST line.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
