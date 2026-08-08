# -*- coding: utf-8 -*-
"""Humor-distribution scanner — conformance against the Humor Grid.

Written 2026-07-31. `marginalia/specs/HUMOR_GRID.md` is a fully-ruled comedy
architecture: three archetypes at three scales, a per-chapter policy Wendell
decided on 2026-07-28, and **twenty drafted jokes, one per cell**. None of the
2026-07-31 editorial passes assessed it, and the reason turned out to be that
there was almost nothing to assess: of the twenty specimens, exactly one reached
the manuscript.

The grid's own engine, quoted because it is what this instrument looks for:

    Clown       — me   — a process running unattended in *me*
    Jerk        — you  — a process running unattended in *you*
    Cult Leader — us   — a process running unattended in *us*

    What is funny in every case is one thing: something executing its script with
    total commitment in a situation that stopped calling for it.

So the archetype is a **grammatical person**, which is findable. Whether a given
passage is funny is not, and this instrument does not try.

**Read the limitation before quoting the table.** These patterns were derived
from the grid's own twenty specimens, so the scanner is good at answering *did
the drafted jokes land* and poor at answering *is this book funny*. It will miss
humor the book invented for itself — `ch4:115`, the I-statements satire that sits
in `specs/VOICE_ANCHOR.md`, was missed on a case-sensitivity bug and would have
been missed anyway had it been phrased differently. A zero in this table means
"no grid-shaped joke here", never "nothing funny here". The reliable number is
the specimen count, which needs no regex: **1 of 20**.

The falsifiable policy rulings this checks:

    ch7  Jerk = NONE      the withdrawal is the move; the absence is the payoff
    ch9  no butt at all   play / fondness / handoff instead
    ch4-ch6 Jerk = heavy  the spring the ch7 withdrawal releases
    ch8  Jerk points at the AUTHOR, delivered by the narrator
    ch3  Jerk light, or routed to Clown (Magenta-proximity risk)
    ch5  Jerk held visibly to process-not-person (Amber-contempt risk)

    python3 instruments/humor.py          # distribution by chapter
    python3 instruments/humor.py -v       # with specimen lines
"""
import io
import re
import sys
import glob

VERBOSE = '-v' in sys.argv

# Comic positioning, by person. Each pattern marks a place the book has set up
# the grid's engine — a script running past its situation — at that scale.
ARCHETYPE = {
    'clown': [
        r"\bI (rehearsed|caught myself|told myself|spent (forty|twenty|three|two)\b)",
        r"\bI (killed|built|ran|wrote) .{0,40}\band called it\b",
        r"\bwhich is the part that makes it so hard to stop\b",
        r"\bI have never once\b|\bI did it the entire time\b",
        r"\bI know that (counter|machine|move) from the inside\b|\bI know that counter\b",
        # PLACED 2026-08-07. The grid's specimens are drafts; what lands in the body
        # is adapted, so a pattern list keyed only to the drafts reports 0 forever
        # however many jokes ship. Each entry below is a joke actually in the
        # manuscript, added when it landed.
        r"\bI built a spreadsheet to track my moods\b",
    ],
    'jerk': [
        r"\b(He|She) (isn't|is not|has been|answers|says she's|says he's)\b.{0,60}"
        r"(exactly|every question|for \w+ years|holding)",
        r"\bYou'?ve found the flaw\b|\bthat stopped being \w+ and turned into\b",
        r"\bHis (brother|sister|team) (is fine|has a job)\b",
        r"\basked what his leading indicator was\b",
    ],
    'cult': [
        r"\bThe (committee|charter|onboarding|retreat|policy|process) (exists|says|had|has)\b",
        r"\bIt has never\b.{0,50}\band\b.{0,40}\b(unanimously|renewed|approved)\b",
        r"\bby the third day\b|\bwe had invented a way to\b",
        r"\bthe workshops teach the scripts\b",
        r"\bread the burnout survey and added a wellness hour\b",
    ],
}

# Wendell's ruled per-chapter policy. None = the absence is the design.
# ch1 is deliberately absent from the grid — it covers ch2-ch9. Reported as
# unpoliced rather than skipped, because ch1 carries the anchor's funniest
# material and a later edition may want it under policy.
POLICY = {
    1: {'clown': '-', 'jerk': '-', 'cult': '-'},
    2: {'clown': 'yes', 'jerk': 'yes',    'cult': 'yes'},
    3: {'clown': 'yes', 'jerk': 'light',  'cult': 'yes'},
    4: {'clown': 'yes', 'jerk': 'heavy',  'cult': 'yes'},
    5: {'clown': 'yes', 'jerk': 'heavy',  'cult': 'yes'},
    6: {'clown': 'yes', 'jerk': 'heavy',  'cult': 'yes'},
    7: {'clown': 'yes', 'jerk': 'NONE',   'cult': 'yes'},
    8: {'clown': 'yes', 'jerk': 'author', 'cult': 'yes'},
    9: {'clown': 'none', 'jerk': 'none',  'cult': 'none'},
}


def body_of(path):
    raw = io.open(path, encoding='utf-8').read()
    out, inblk = [], False
    for n, line in enumerate(raw.split('\n'), 1):
        if '<!--' in line:
            inblk = True
        margin = inblk or line.startswith('>')
        out.append((n, line, margin))
        if '-->' in line:
            inblk = False
    return out


def scan():
    hits = {}
    for path in sorted(glob.glob('manuscript/ch*.md'),
                       key=lambda p: int(re.search(r'ch(\d+)', p).group(1))):
        ch = int(re.search(r'ch(\d+)', path).group(1))
        hits[ch] = {'clown': [], 'jerk': [], 'cult': []}
        for n, line, margin in body_of(path):
            s = line.strip().lstrip('> ').strip()
            if not s or s.startswith('#'):
                continue
            for arch, pats in ARCHETYPE.items():
                for p in pats:
                    m = re.search(p, s, re.I)
                    if m:
                        hits[ch][arch].append((n, 'margin' if margin else 'body', s[:120]))
                        break
    return hits


def main():
    hits = scan()
    print('=== HUMOR DISTRIBUTION vs the ruled policy ===')
    print('%-5s %-22s %-22s %s' % ('ch', 'Clown (me)', 'Jerk (you)', 'Cult Leader (us)'))
    print('-' * 88)
    flags = []
    for ch in sorted(hits):
        row = []
        for arch in ('clown', 'jerk', 'cult'):
            n = len(hits[ch][arch])
            want = POLICY[ch][arch]
            mark = ''
            if want == 'NONE' and n:
                mark = '  <-- POLICY SAYS NONE'
                flags.append('ch%d %s: policy NONE, found %d' % (ch, arch, n))
            elif want in ('yes', 'heavy') and n == 0:
                mark = '  <-- policy wants %s' % want
                flags.append('ch%d %s: policy %s, found 0' % (ch, arch, want))
            elif want == 'none' and n:
                mark = '  <-- ch9 has no butt'
                flags.append('ch%d %s: ch9 policy is no butt, found %d' % (ch, arch, n))
            row.append('%d (%s)%s' % (n, want, mark))
        print('ch%-3d %-22s %-22s %s' % (ch, row[0], row[1], row[2]))
        if VERBOSE:
            for arch in ('clown', 'jerk', 'cult'):
                for n, surf, s in hits[ch][arch]:
                    print('        %-5s %-6s %d  %s' % (arch, surf, n, s))
    print('-' * 88)
    print('\nPOLICY DEVIATIONS: %d' % len(flags))
    for f in flags:
        print('  ' + f)
    print('\nPositioning, not punchlines. Whether a hit is funny is a human ruling;')
    print('this reports where the book is set up to be, against what Wendell ruled.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
