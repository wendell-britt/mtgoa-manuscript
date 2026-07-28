# -*- coding: utf-8 -*-
import os as _os
MS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _os.pardir, 'manuscript') + _os.sep
# Task 34/35 v2: TEACH -> PERFORM -> APPLY, with the manuscript's ACTUAL conventions.
# Corrections from v1: sections accumulate to the next H2 (not the next H3);
# scripted speech is *italic*, not quoted; explicit **Example:** / In practice: labels count.
import io, re, collections

L = {c: io.open(MS+'ch%d.md' % c, encoding='utf-8').read().split('\n') for c in range(1, 10)}
H2 = re.compile(r'^##\s+(.*)'); H3 = re.compile(r'^###\s+(.*)')
MOVE = re.compile(r'^###\s+\**Move\s+(\d)\s*[:—-]\s*(.*)')

def wc(lines):
    return len(re.sub(r'[#*|`>]', ' ', ' '.join(lines)).split())

def sections(c):
    """Accumulate each '## Section N' to the NEXT '## ' heading."""
    out = {}; cur = None; buf = []
    for i, l in enumerate(L[c], 1):
        if H2.match(l) and not H3.match(l):
            if cur: out[cur] = (out[cur][0], wc(buf))
            m = re.match(r'^##\s+Section\s*(\d)', l)
            cur = int(m.group(1)) if m else None
            if cur: out[cur] = (i, 0)
            buf = []
        else:
            buf.append(l)
    if cur: out[cur] = (out[cur][0], wc(buf))
    return out

def h3blocks(c):
    out = []; cur = None
    for i, l in enumerate(L[c], 1):
        if H2.match(l) or H3.match(l):
            if cur: out.append(cur)
            cur = [i, re.sub(r'^#+\s*', '', l).strip(), []]
        elif cur is not None: cur[2].append(l)
    if cur: out.append(cur)
    return out

# --- the manuscript's real example conventions --------------------------------
EXLABEL = re.compile(r'\*\*(Example|In practice|Try it|Worked example|Scenario)\b|^\s*In practice:', re.I | re.M)
# italic run of >=6 words = a scripted line the reader can say
ITAL = re.compile(r'(?<!\*)\*([^*\n]{28,})\*(?!\*)')
def scripts(t):
    out = []
    for m in ITAL.finditer(t):
        s = m.group(1)
        if len(s.split()) < 6: continue
        if re.search(r'\b(I|you|we|my|your|this|that|it|he|she|they)\b', s, re.I): out.append(s)
    return out
SCENE = re.compile(r'\b(a (coworker|colleague|friend|team|manager|meeting|conversation)|'
                   r'your (friend|coworker|boss|sibling|partner|manager|team)|'
                   r'someone (says|tells|shares|asks|brings)|the meeting|a team stuck|'
                   r'three weeks|in the room|at the table|a campaign|a client)\b', re.I)

DO_NOW = re.compile(r'try it now|the one rep|put the book down|before you (read on|turn the page)|'
                    r'this week|thirty seconds|30-second|two minutes|next time you|right now', re.I)
IMPER = re.compile(r'^(Name|Ask|Say|Write|Pick|Choose|Run|Take|Put|Hold|Catch|Notice|Draw|Stop|Start|'
                   r'Do|Try|Go|Set|Look|Listen|Watch|Cut|Hand|Refuse|Repeat|Spend|Close|Open|Feel|Find|Log|Thank)\b')

print('=== CHAIN CHECK v2 ===')
print('%-4s %7s %8s %8s %8s %8s  %-6s %s' % ('ch','words','S1-2 why','S3 teach','S4 prac','S6 game','moves','deck'))
DATA = []
for c in range(1, 10):
    S = sections(c); txt = '\n'.join(L[c])
    why = sum(S[k][1] for k in (1, 2) if k in S)
    B = h3blocks(c)
    moves = []
    for i, t, body in B:
        m = MOVE.match('### ' + t)
        if not m: continue
        bt = '\n'.join(body)
        moves.append({'line': i, 'title': m.group(2).strip(' *'), 'words': len(bt.split()),
                      'label': len(EXLABEL.findall(bt)), 'script': len(scripts(bt)),
                      'scene': len(SCENE.findall(bt))})
    deck = ''.join(['T' if re.search(r'^##+\s*Your Twenty Cards', txt, re.M) else '.',
                    'S' if re.search(r'^###\s*Drawing Against the Shadow', txt, re.M) else '.',
                    'Q' if re.search(r'^###\s*From Card to Quest', txt, re.M) else '.'])
    perf = []
    for i, t, body in B:
        bt = ' '.join(body)
        if DO_NOW.search(t) or DO_NOW.search(bt[:1500]):
            n = sum(1 for l in body if IMPER.match(l.strip().lstrip('*_1234567890. ')))
            perf.append((i, t[:62], n))
    DATA.append((c, S, why, moves, deck, perf))
    f = lambda k: ('%dw' % S[k][1]) if k in S else '—'
    print('%-4d %7d %8s %8s %8s %8s  %-6d %s'
          % (c, wc(L[c]), '%dw' % why if why else '—', f(3), f(4), f(6), len(moves), deck))

print()
print('=== WORKED EXAMPLES PER MOVE ===')
print('%-11s %-44s %5s %6s %7s %6s  %s' % ('ref','move','words','label','scripts','scenes','VERDICT'))
tot = collections.Counter(); bare = []
for c, S, why, moves, deck, perf in DATA:
    for m in moves:
        if m['label'] or (m['script'] and m['scene']): v = 'worked'
        elif m['script']: v = 'script, no scene'
        elif m['scene']: v = 'scene, no script'
        else: v = 'BARE CLAIM'
        tot[v] += 1
        if v == 'BARE CLAIM': bare.append((c, m))
        print('ch%-2d:%-6d %-44s %5d %6d %7d %6d  %s'
              % (c, m['line'], m['title'][:44], m['words'], m['label'], m['script'], m['scene'], v))
print()
print('totals:', dict(tot))
print()
print('=== BARE CLAIMS (a move with no example Jordan can copy) ===')
for c, m in bare: print('  ch%d:%-5d %-46s %4dw' % (c, m['line'], m['title'], m['words']))
print()
print('=== EXAMPLE DENSITY BY CHAPTER ===')
for c, S, why, moves, deck, perf in DATA:
    if not moves: print('  ch%-2d  no moves' % c); continue
    lab = sum(m['label'] for m in moves); sc = sum(m['script'] for m in moves)
    print('  ch%-2d  moves=%d  labelled examples=%d  scripted lines=%d  bare=%d'
          % (c, len(moves), lab, sc, sum(1 for m in moves if not m['label'] and not m['script'] and not m['scene'])))
