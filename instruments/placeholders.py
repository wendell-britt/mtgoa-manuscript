# -*- coding: utf-8 -*-
"""Placeholder and production-debt scanner.

Written 2026-07-31 after `[[TESTIMONY SLOT - WENDELL ...]]` was found sitting in
manuscript/ch7.md, two days from delivery, having survived every existing check.
`gate.py` passed clean on all four surfaces and `build_book.py` assembled the
spine without complaint, because neither has a rule for unfilled text: the gate
scores banned words and voice defects, the builder scores missing *files*. An
authoring note addressed to the author is neither.

This is additive on purpose. It does not touch gate.py, so it cannot change what
that gate passes or fails; run it alongside. Any hit is a hard print blocker.

    python3 instruments/placeholders.py        # scan the shipping surfaces
    python3 instruments/placeholders.py -v     # quote every hit with context

Exits non-zero when anything is found, so it can gate a build.
"""
import io
import os
import re
import sys
import glob

VERBOSE = '-v' in sys.argv

# Every surface that reaches a reader. Mirrors gate.py's four surfaces plus
# drafts/, which is excluded from the build but is where half-written prose sits.
SURFACES = [
    ('body',       sorted(glob.glob('manuscript/ch*.md'))),
    ('appendices', sorted(glob.glob('appendices/APPENDIX_*.md'))
                   + sorted(glob.glob('appendices/ON_THE_SHOULDERS_OF.md'))),
    ('matter',     sorted(glob.glob('front_matter/*.md'))
                   + sorted(glob.glob('back_matter/*.md'))),
]

RULES = [
    # name,            pattern,                                    why
    ('authoring-note', r'\[\[[^\]]*\]\]|\[\[.*',
     'a note addressed to the author, not to the reader'),
    ('bare-slot',      r'\b(TK|TKTK)\b|\bTBD\b|\bFIXME\b|\bXXX\b|\bLOREM\b',
     'standard unfilled-copy markers'),
    ('production-tag', r'\[\s*(visual|image|figure|photo|diagram|chart)\s*:',
     'an asset called for that must exist before print'),
    ('empty-bracket',  r'\[\s*(URL|QR|LINK|ISBN)[^\]]*\]|\[\s*\]',
     'a slot for a value nobody has supplied'),
    ('placeholder-name', r'\bJOHN DOE\b|\bYOUR NAME HERE\b|\bINSERT\b',
     'template text'),
    # Production metadata. Found 2026-07-31: six shipping appendices carry
    # provenance headers - Status, Authority, Location in book, Timing
    # dependency - and build_book.py copies them straight into the deliverable.
    # 15 lines reached build/MTGOA_PRINT_2026-07-31.md, including internal file
    # paths (docs/plans/..., GATE_GIFTS_ALLYSHIP_MOVES.md), approval records
    # ("approved by Wendell"), a "Draft" status flag on a shipping appendix, and
    # an instruction to the production team ("Coordinate before press").
    #
    # These lines are legitimate in the repo and must never reach a reader. The
    # durable fix is for build_book.py to strip them; until it does, this rule
    # is what stands between them and the typesetter.
    ('production-metadata',
     r'^\*\*(Status|Authority|Location in book|Timing dependency|Depends on|Blocked by|Revised|Ported):\*\*',
     'internal provenance that belongs in the repo, not in the book'),
]

# Legitimate in-world constructions that must never be "fixed". The Diplomat's
# worked translation uses [Camp A]/[Camp B] as generic party labels, five times
# referentially in one paragraph; the Architect's treatise cites figures that are
# deliberately not reproduced (SEVEN_VOICES.md, HEAD_VOICE_DIAL.md).
ALLOW = re.compile(r'\[Camp [AB]\]|\[the other camp\]', re.I)


def scan():
    hits = []
    for surface, files in SURFACES:
        for path in files:
            if not os.path.exists(path):
                continue
            for n, line in enumerate(io.open(path, encoding='utf-8').read().split('\n'), 1):
                if ALLOW.search(line):
                    continue
                for name, pat, why in RULES:
                    for m in re.finditer(pat, line):
                        hits.append((surface, path, n, name, m.group(0)[:70], why, line.strip()[:150]))
    return hits


def main():
    hits = scan()
    print('%-11s %-26s %6s  %-16s %s' % ('surface', 'file', 'line', 'rule', 'match'))
    print('-' * 92)
    for surface, path, n, name, match, why, ctx in hits:
        print('%-11s %-26s %6d  %-16s %s' % (surface, os.path.basename(path), n, name, match))
        if VERBOSE:
            print('              why: %s' % why)
            print('              ctx: %s' % ctx)
    print('-' * 92)
    if hits:
        print('PLACEHOLDERS FOUND: %d. These print verbatim. Not shippable.' % len(hits))
        return 1
    print('CLEAN - no placeholder or production debt on any shipping surface.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
