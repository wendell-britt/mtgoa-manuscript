# -*- coding: utf-8 -*-
import os as _os
MS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _os.pardir, 'manuscript') + _os.sep
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
    # The Spiral colours were CUT by Wendell 2026-07-31 (log row A4) -- a five-term
    # developmental scale used at six sites and defined nowhere, with the six Faces
    # taking the work. They were cut from the manuscript and left in this list, so the
    # ledger reported four NEVER DEFINED rows for terms that appear ZERO times in the
    # book. Measured 2026-08-05: Amber 0, Orange 0, Green 0, Teal 0.
    #
    # Same defect as the retired Key Terms glossary and `The Game So Far` -- a name for
    # something that does not exist, carried in a list because a row in a list reads
    # exactly like a row for something real. Removed rather than commented, since a
    # commented row is the next version of the same mistake.
    #     ('Amber', ...), ('Orange', ...), ('Green', ...), ('Teal', ...)
]

# Terms whose debt is DESIGN, not oversight. A gap between first use and first
# definition normally means a reader met jargon with no translation. For these it means
# the book is withholding on purpose, and "fixing" it breaks the structure.
#
# Wendell 2026-08-05: the six Faces sit at six different altitudes, and the reader walks
# that developmental sequence WITHOUT being told it is developmental. The reveal is held
# to ch8 -- "*Which altitude is this?* is a vertical question, and its answer-set is the
# six roles the schools teach... a fact about their development and not a fact about
# their worth" -- and the withholding is aimed at Green's hierarchy allergy: a reader
# told in Chapter 3 that she occupies a level rejects the ladder before she has walked
# it. The usage curve is the design, visible in the counts: 0, 0, 4, 6, 2, 7, 14, 30, 3.
#
# This entry exists because I glossed `altitude` at ch3:241 on this date (DL-72),
# cleared the "debt", and broke the reveal. The instrument cannot tell a withheld term
# from an undefined one, so the ruling has to live where the instrument reads it.
WITHHELD = {
    'altitude': 'Held to ch8 by design (DL-73). The six Faces ARE the six altitudes and '
                'the reader is not told until the Sage. Do not gloss it earlier.',
}

LINES = {}
for c in range(1, 10):
    LINES[c] = io.open(MS+'ch%d.md' % c, encoding='utf-8').read().split('\n')

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
    # Gloss INSIDE the bold span: "**Direct Action — the true thing said to the face**".
    # The rule above only sees a dash AFTER the closing asterisks, which is why A5 was
    # reported and then withdrawn on 2026-07-31 -- the four domains are all defined this
    # way and all four read as NEVER DEFINED for months.
    if re.search(r'\*\*[^*]{0,30}?' + term_rx + r'[^*]{0,4}[—:-]\s*[^*]{3,60}\*\*', s):
        return 'bold-gloss'
    # Appositive: "the Vulnerable Child, the player who should have been holding it" and
    # "Direct Action, the true thing said to a face". A term followed by a comma and a
    # noun phrase is the commonest way this book defines something in running prose, and
    # it was the one shape `is_def` could not see. DL-29 named it after it cost two
    # withdrawn findings; a third (`Vulnerable Child`, again) turned up 2026-08-05.
    # The colon is not decoration -- it is the discriminator. Every true appositive
    # definition in this book announces itself: "That conversion has a name: Emotional
    # Alchemy, the engine under the whole book"; "the youngest part of you still waits:
    # the Vulnerable Child, the player who should have been holding it"; "one of the
    # four: Direct Action, the true thing said to a face."
    #
    # Without the colon the rule matched a fronted adverbial and manufactured a
    # definition -- ch6:242, "At the Architect's altitude, the native material is not
    # emotion", which defines nothing. That is the worse failure direction: a missing
    # definition gets reported, a fabricated one is silent.
    if re.search(r'[:;]\s+(?:the\s+)?' + term_rx + r',\s+(?:the|a|an|your|his|her|its|one|what)\b[^.!?]{4,70}', s):
        return 'appositive'
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
    if name in WITHHELD:
        debt = 'WITHHELD BY DESIGN'
    elif fu and (fd is None):
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
