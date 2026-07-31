# -*- coding: utf-8 -*-
"""Assumed-prior-knowledge scanner.

Written 2026-07-31. The 2026-07-31 chapter pass found the same defect in eight of
nine chapters and nobody had named it as one thing: **the prose claims the reader
already knows something before the book has taught it.** It runs at three scales —
a term used before its definition, a move referred to as familiar before it is
taught, and the book's central loop asserted as known one chapter before it
arrives (finding A6).

`termdebt.py` covers part of this and has a known blind spot (its bold-gloss rule
cannot match a gloss that sits inside the bold span, which is the book's most
common definition form — that mistake produced a withdrawn finding). This
instrument attacks the defect from the other side: rather than asking *where is
this term defined*, it finds **the assertion of prior knowledge itself**, which is
a smaller and much more reliable pattern to match.

    python3 instruments/assumed.py             # every site, by chapter
    python3 instruments/assumed.py -v          # with surrounding context
    python3 instruments/assumed.py --terms     # cross-check against first use

Findings are candidates. Every one is adjudicated by a human: some assertions of
familiarity are legitimate, because the reader genuinely was taught the thing.
The instrument cannot tell earned recall from unearned recall. It can tell you
every place the book makes the claim, which is the part a person cannot do by
reading.
"""
import io
import re
import sys
import glob
import os

VERBOSE = '-v' in sys.argv
TERMS_MODE = '--terms' in sys.argv

# The assertion patterns. Each one is the prose saying "you have this already".
CLAIMS = [
    ('already-know',   r'\byou already know\b|\byou know\b(?!\s+(what|how|why|that|when|where|the difference))'),
    ('already-have',   r'\byou already have\b|\byou now have\b|\byou have\b\s+(the|your)\s+\w+\s+(already|by now)'),
    ('you-met',        r'\byou (met|have met|已)\b|\byou have already\b|\bwe have already\b'),
    ('by-now',         r'\bby now\b|\bat this point you\b'),
    ('as-you-saw',     r'\bas you (saw|learned|read|practiced|ran)\b|\byou (saw|learned) (this|that|it) in\b'),
    ('recall',         r'\bremember (the|when|that|your)\b|\bthink back to\b|\byou will recall\b'),
    ('back-ref-ch',    r'\bChapter \d+ (taught|gave|showed|told|put|left|handed)\b'),
    ('the-one-you',    r'\bthe (one|move|face|card|channel) you (just|already)\b'),
    ('you-have-been',  r'\byou have been (running|playing|doing|practicing)\b'),
]

# Narrated history: the prose asserts a specific unnamed event in the reader's
# past as fact. Canon's standing rule bans it; `gate.py`'s A0 regex is far too
# narrow to find it, matching only "you were taught/told/raised/trained",
# "somewhere along the way" and "the village taught you". Added 2026-07-31 after
# Tier 3 turned up ch5:200 and ch5:458, neither of which the gate can see.
#
# Two false-positive classes are excluded below, both found by reading:
#   * transfer-drill scenarios ("**Six.** You have been making the same argument
#     in the same meeting for two years") — a hypothetical she practises on
#   * conditional framing ("If you learned to over-prepare because mistakes were
#     punished") — the correct way to write this, and common in ch2
HISTORY = [
    ('youve-been',    r"You(?:'ve| have) been [a-z]+ing\b"),
    ('since-the-time', r"since the (?:last )?time (?:you|somebody|someone)\b"),
    ('the-first-time', r"[Tt]he first time you\b"),
    ('you-stopped',   r"\byou stopped [a-z]+ing\b"),
    ('you-learned',   r"\byou learned (?:to|that|this)\b"),
    ('back-when',     r"\bback when you\b"),
    ('you-spent',     r"[Yy]ou (?:have )?spent (?:years|a decade|your)\b"),
]
HIST_ALLOW = re.compile(r'^\s*\*\*(One|Two|Three|Four|Five|Six)\.\*\*|\bIf you (learned|grew|were)\b')

# Definite constructions pointing at an antecedent that may not exist: "This is
# the X's gift" presumes X was introduced.
DEFINITE = re.compile(r'\bThis is the ([A-Z][a-z]+(?: [A-Z][a-z]+)?)\'s\b')

MARG = re.compile(r'<!--.*?-->', re.S)


def body_of(path):
    """Return (line_number, text) for body lines only, margin stripped."""
    raw = io.open(path, encoding='utf-8').read()
    out = []
    inblk = False
    for n, line in enumerate(raw.split('\n'), 1):
        if '<!-- MARGINALIA' in line or '<!--' in line:
            inblk = True
        if not inblk and not line.startswith('>'):
            out.append((n, line))
        if '-->' in line:
            inblk = False
    return out


def scan():
    hits = []
    for path in sorted(glob.glob('manuscript/ch*.md'),
                       key=lambda p: int(re.search(r'ch(\d+)', p).group(1))):
        ch = int(re.search(r'ch(\d+)', path).group(1))
        for n, line in body_of(path):
            s = line.strip()
            if not s or s.startswith('#') or s.startswith('|'):
                continue
            for name, pat in CLAIMS:
                for m in re.finditer(pat, s, re.I):
                    hits.append((ch, n, name, m.group(0), s))
            for m in DEFINITE.finditer(s):
                hits.append((ch, n, 'definite-ref', m.group(0), s))
            if not HIST_ALLOW.search(s):
                for name, pat in HISTORY:
                    for m in re.finditer(pat, s):
                        hits.append((ch, n, 'HISTORY:' + name, m.group(0), s))
    return hits


def main():
    hits = scan()
    bych = {}
    for ch, n, name, match, ctx in hits:
        bych.setdefault(ch, []).append((n, name, match, ctx))

    print('=== ASSERTIONS OF PRIOR KNOWLEDGE, BY CHAPTER ===')
    print('%-5s %6s  %-14s %s' % ('ch', 'line', 'pattern', 'match'))
    print('-' * 92)
    for ch in sorted(bych):
        for n, name, match, ctx in bych[ch]:
            print('ch%-3d %6d  %-14s %s' % (ch, n, name, match[:44]))
            if VERBOSE:
                print('        %s' % ctx[:170])
    print('-' * 92)
    print('TOTAL %d assertions across %d chapters' % (len(hits), len(bych)))
    print()
    print('%-5s %s' % ('ch', 'count'))
    for ch in sorted(bych):
        print('ch%-3d %d' % (ch, len(bych[ch])))
    print()
    print('Every hit is a CANDIDATE. The instrument cannot tell earned recall from')
    print('unearned recall — it finds every place the book makes the claim. Rule each')
    print('one against whether the book has actually taught the thing by that line.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
