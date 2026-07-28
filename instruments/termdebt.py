# -*- coding: utf-8 -*-
# Task 33: TERM-DEBT LEDGER.
# For every canonical term: first USE vs first DEFINITION, by ch:line.
# A use before a definition = "jargon without translation" = Jordan's #1 drop-off trigger.
import io, re, collections

TERMS = [
    # spine
    ('the Village',        r'\bVillage\b'),
    ('the Forest',         r'\bForest\b'),
    ('the joystick',       r'\bjoystick\b'),
    ('the Game',           r'\bthe Game\b'),
    ('Game Master',        r'\bGame Master\b'),
    ('altitude',           r'\baltitude\b'),
    ('the deck',           r'\ballyship deck\b|\bthe deck\b'),
    ('quest',              r'\bquest\b'),
    ('BAR',                r'\bBAR\b'),
    ('Polarity',           r'\bPolarit(y|ies)\b'),
    ('Emotional Alchemy',  r'\bEmotional Alchemy\b'),
    ('superpower',         r'\bsuperpower\b'),
    ('daemon',             r'\bdaemon\b'),
    ('shadow',             r'\bshadow\b'),
    ('3-2-1',              r'3-2-1'),
    ('Reader.s Oath',      r'Reader.s Oath'),
    ('Allyship Character', r'Allyship Character'),
    # faces
    ('Shaman', r'\bShaman\b'), ('Challenger', r'\bChallenger\b'), ('Regent', r'\bRegent\b'),
    ('Architect', r'\bArchitect\b'), ('Diplomat', r'\bDiplomat\b'), ('Sage', r'\bSage\b'),
    ('Player', r'\bPlayer\b'),
    # daemons
    ('Protector', r'\bProtector\b'), ('Controller', r'\bController\b'), ('Skeptic', r'\bSkeptic\b'),
    ('Fixer', r'\bFixer\b'), ('Emotional Body', r'\bEmotional Body\b'), ('Victim', r'\bVictim\b'),
    ('Damaged Self', r'\bDamaged Self\b'), ('Vulnerable Child', r'\bVulnerable Child\b'),
    # WAVE
    ('Wake Up', r'\bWake Up\b'), ('Open Up', r'\bOpen Up\b'), ('Clean Up', r'\bClean Up\b'),
    ('Grow Up', r'\bGrow Up\b'), ('Show Up', r'\bShow Up\b'),
    # EA channels + satisfied states
    ('Fire (channel)', r'\bFire\b'), ('Water (channel)', r'\bWater\b'), ('Metal (channel)', r'\bMetal\b'),
    ('Earth (channel)', r'\bEarth\b'), ('Wood (channel)', r'\bWood\b'),
    ('Triumph', r'\bTriumph\b'), ('Poignance', r'\bPoignance\b'), ('Wonder', r'\bWonder\b'),
    ('Peace', r'\bPeace\b'), ('Bliss', r'\bBliss\b'),
    # domains
    ('Gather Resources', r'Gather Resources'), ('Raise Awareness', r'Raise Awareness'),
    ('Direct Action', r'Direct Action'), ('Skillful Organizing', r'Skillful Organizing'),
    # spiral
    ('Amber', r'\bAmber\b'), ('Orange', r'\bOrange\b'), ('Green', r'\bGreen\b'), ('Teal', r'\bTeal\b'),
]

LINES = {}
for c in range(1, 10):
    LINES[c] = io.open('/home/claude/ch%d.md' % c, encoding='utf-8').read().split('\n')

def is_def(term_rx, line, nxt):
    """Definition event. nxt = the next 3 lines joined, for roster-entry detection."""
    s = line.strip()
    if not s: return False
    if s.startswith('#') and re.search(term_rx, s): return 'heading'
    if s.startswith('|') and re.search(term_rx, s) and s.count('|') >= 3: return 'table'
    # roster entry: a bold term standing alone, glossed by the lines beneath it
    if re.match(r'^\*\*[^*]{0,40}\*\*$', s) and re.search(term_rx, s):
        if re.search(r'\*\*(Job|As an ally|As a demon|What it does|Shadow)', nxt): return 'roster'
    # inline gloss inside a running sentence: "The **Regent** keeps what works and hands it on."
    if re.search(r'\*\*(The |the )?[^*]{0,30}?' + term_rx + r'[^*]{0,20}?\*\*\s+[a-z]', s): return 'inline'
    if re.search(r'\*\*[^*]{0,30}?' + term_rx + r'[^*]{0,30}?\*\*\s*[—:-]', s): return 'bold-gloss'
    if re.search(term_rx + r'[^.!?]{0,60}?\b(is|are)\b\s+(the|a|an|what|how|your|when|where)', s): return 'copula'
    if re.search(term_rx + r'[^.!?]{0,40}?\b(means|refers to|stands for|is called|we call)\b', s): return 'gloss'
    if re.search(r'\b(call|called|name|named|term)\b[^.!?]{0,30}?' + term_rx, s): return 'naming'
    return False

rows = []
for name, rx in TERMS:
    R = re.compile(rx)
    first_use = None; first_def = None; def_kind = None; n = 0
    per_ch = collections.Counter()
    for c in range(1, 10):
        for i, l in enumerate(LINES[c], 1):
            if not R.search(l): continue
            n += 1; per_ch[c] += 1
            if first_use is None: first_use = (c, i, l.strip())
            if first_def is None:
                k = is_def(rx, l, ' '.join(LINES[c][i:i+3]))
                if k: first_def = (c, i, l.strip()); def_kind = k
    rows.append((name, first_use, first_def, def_kind, n, per_ch))

def key(x):
    if x is None: return (99, 99999)
    return (x[0], x[1])

print('=== TERM-DEBT LEDGER: first USE vs first DEFINITION ===')
print('%-20s %-10s %-10s %-11s %6s  %s' % ('term', 'first use', 'first def', 'def kind', 'n', 'DEBT'))
debts = []
for name, fu, fd, dk, n, per in sorted(rows, key=lambda r: key(r[1])):
    u = 'ch%d:%d' % (fu[0], fu[1]) if fu else '—'
    d = 'ch%d:%d' % (fd[0], fd[1]) if fd else 'NEVER'
    debt = ''
    if fu and (fd is None):
        debt = 'NO DEFINITION'; debts.append((name, fu, fd, dk, 999999))
    elif fu and fd and key(fd) > key(fu):
        gap = 0
        if fd[0] == fu[0]: gap = fd[1] - fu[1]
        else: gap = 10000 * (fd[0] - fu[0])
        debt = 'used %s before defined' % ('%d lines' % gap if fd[0] == fu[0] else '%d chapter(s)' % (fd[0]-fu[0]))
        debts.append((name, fu, fd, dk, gap))
    print('%-20s %-10s %-10s %-11s %6d  %s' % (name, u, d, dk or '', n, debt))

print()
print('=== THE DEBTS, WORST FIRST ===')
for name, fu, fd, dk, gap in sorted(debts, key=lambda r: -r[4]):
    print('  %-20s first use ch%d:%d   %s' % (name, fu[0], fu[1], 'NEVER DEFINED' if fd is None else 'defined ch%d:%d (%s)' % (fd[0], fd[1], dk)))
    print('      USE : %s' % fu[2][:160])
    if fd: print('      DEF : %s' % fd[2][:160])
