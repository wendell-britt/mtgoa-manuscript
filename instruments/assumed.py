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
HIST_ALLOW = re.compile(r'^\s*\*\*(One|Two|Three|Four|Five|Six)\.\*\*|\bIf you (learned|grew|were)\b'
                        r'|^\s*\*\*Example')

# ---------------------------------------------------------------- asserted experience
#
# ADDED 2026-08-01, batch nine. Wendell, on a draft line of mine reading *"You've
# been on the paying end of this"*:
#
#   "This sentence structure needs to get banned. We don't know they've been on the
#   paying end of this. We can invite them to imagine and it solves all of these
#   assertions. But these types of assertions have become a blocker for the book."
#
# HISTORY above catches the *narrated past* — a specific unnamed event asserted as
# the reader's history. This catches the wider form: any declarative about what the
# reader has done, felt, seen or become, stated as fact. It is the pattern behind
# five read-through notes filed across four separate batches (N12 *You are a Game
# Master*, N15 *You have done this before*, N17 *You graduated from it years ago*,
# and the ch1 opener note about assumed secret competence), which is why it is
# tracked as one thing here rather than five.
#
# The repair Wendell named is structural, not lexical: **invite instead of assert.**
# So INVITE below counts the licensed form, and the report prints the ratio. That
# ratio is the number the readiness spec tracks — a chapter is not fixed by deleting
# assertions, it is fixed by converting them.
EXPERIENCE = [
    ('youve-been-on',  r"You(?:'ve| have) been (?:on|at|in|through|the)\b"),
    ('youve-done',     r"You(?:'ve| have) (?:done|seen|felt|watched|had|met|played|lived|"
                       r"survived|sat|stood|walked|caught|noticed|carried|paid|earned|"
                       r"spent|tried|been)\b"),
    ('you-past',       r"\bYou (?:did|felt|saw|watched|walked|caught|sat|stood|graduated|"
                       r"outgrew|left|quit|chose|decided|set|named|drew|held)\b"),
    ('you-know-feel',  r"\byou know (?:the feeling|what that feels like|"
                       r"how (?:that|this) (?:feels|goes|lands))"),
    ('that-was-yours', r"\bThat was the \w+ you\b|\bthat is the \w+ you have\b"),
]

# The licensed alternative. Not a defect — the thing an assertion converts into.
INVITE = re.compile(
    r"\bImagine\b|\bPicture\b|\bSay you(?:'re| are| have)?\b|\bSuppose\b"
    r"|\bIf you(?:'ve| have) ever\b|\bMaybe you\b|\bPerhaps you\b"
    r"|\bThink of a time\b|\bIf any of (?:this|that)\b|\bIf that\b")

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
    hits, invites = [], {}
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
                for name, pat in EXPERIENCE:
                    for m in re.finditer(pat, s):
                        hits.append((ch, n, 'EXP:' + name, m.group(0), s))
            invites[ch] = invites.get(ch, 0) + len(INVITE.findall(s))
    return hits, invites


def main():
    hits, invites = scan()
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
    # The conversion ratio. Wendell's repair is to invite rather than assert, so the
    # number that matters is not how many assertions a chapter has but how it splits.
    print('%-5s %8s %8s %8s   %s' % ('ch', 'assert', 'EXP', 'invite', 'assert per invite'))
    for ch in sorted(bych):
        n_all = len(bych[ch])
        n_exp = sum(1 for _, name, _, _ in bych[ch] if name.startswith('EXP:'))
        inv = invites.get(ch, 0)
        ratio = ('%.1f' % (float(n_all) / inv)) if inv else 'no invitations'
        print('ch%-3d %8d %8d %8d   %s' % (ch, n_all, n_exp, inv, ratio))
    print()
    print('Every hit is a CANDIDATE. The instrument cannot tell earned recall from')
    print('unearned recall — it finds every place the book makes the claim. Rule each')
    print('one against whether the book has actually taught the thing by that line.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
