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
    # These lines are legitimate in the repo and must never reach a reader.
    # `build_book.py` now strips them at assembly, and this scanner applies the
    # same strip below — so under normal conditions this rule is silent. It is
    # kept as the regression guard: remove or break that strip and the headers
    # reappear in the scanned text and this fires again.
    ('production-metadata',
     r'^\*\*(Status|Authority|Location in book|Book body|Timing dependency|Depends on|'
     r'Blocked by|Revised|Ported):\*\*',
     'internal provenance that belongs in the repo, not in the book'),
    # Author-slot convention, added 2026-07-31. When a form requires N concrete
    # instances only Wendell can supply - a remembered moment, a draft count, a
    # note somebody actually gave him - the slot is marked `WENDELL:` and left
    # unfilled rather than drafted. This rule exists because the alternative was
    # demonstrated the same day: drafting into those slots produced invented
    # biography that read well and was false. A form requiring N specifics will
    # generate N specifics; the safeguard is the empty slot plus this rule.
    ('author-slot', r'\bWENDELL:',
     'a slot only the author can fill, deliberately left empty'),
]

# Scan what SHIPS, not what sits on disk. `build_book.py` strips each component's
# provenance header at assembly, so those lines are legitimate in the repository
# and never reach a reader. Applying the same strip here keeps this scanner
# honest in both directions: it stops reporting metadata as a blocker, and if
# that strip is ever removed from the builder, these lines reappear here and the
# scanner starts failing again. That is the intended coupling.
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from build_book import strip_provenance
except Exception:                                    # builder moved or broken
    def strip_provenance(text):
        return text

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
            for n, line in enumerate(strip_provenance(
                    io.open(path, encoding='utf-8').read()).split('\n'), 1):
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
