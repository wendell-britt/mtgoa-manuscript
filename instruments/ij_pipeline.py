# -*- coding: utf-8 -*-
# Igniting Joy: PDF -> ij_pages.json
#  - line-level reflow (keeps inline bold runs in place: they are separate blocks
#    but share a y with the body line, so (y,x) ordering re-seats them)
#  - column-aware page ordering for the 3 genuinely two-column pages
#  - Type3/ToUnicode ligature repair: fi renders as 'y', fl renders as 'z'
import fitz, io, re, json, itertools, collections
from wordfreq import zipf_frequency as Z

SRC = '/root/.claude/uploads/248d6205-9839-527b-b2a8-f162951173fa/39730757-Igniting_Joy_Transforming_Angers_Fire_Into_Joy_Via_Humor.pdf'
SPLIT = 315.0

d = fitz.open(SRC)
pages = []
twocol = []
for pno in range(d.page_count):
    lines = []
    for b in d[pno].get_text('dict', sort=False)['blocks']:
        if b.get('type', 0) != 0:
            continue
        for ln in b['lines']:
            spans = sorted(ln['spans'], key=lambda s: s['bbox'][0])
            txt = ''.join(s['text'] for s in spans)
            if not txt.strip():
                continue
            sizes = [s['size'] for s in spans if s['text'].strip()]
            fonts = set(s['font'] for s in spans if s['text'].strip())
            bold = all(('Bold' in f or 'bold' in f or 'Black' in f) for f in fonts) if fonts else False
            lines.append({'y': round(ln['bbox'][1], 1), 'x': round(ln['bbox'][0], 1),
                          'size': round(max(sizes), 1) if sizes else 0,
                          'bold': bold, 't': txt})
    left = [l for l in lines if l['x'] < SPLIT]
    orphanR = [l for l in lines if l['x'] >= SPLIT
               and not any(abs(l['y'] - m['y']) <= 3 for m in left)]
    if len(orphanR) >= 5:
        twocol.append(pno + 1)
        lines.sort(key=lambda l: (0 if l['x'] < SPLIT else 1, l['y'], l['x']))
    else:
        lines.sort(key=lambda l: (l['y'], l['x']))
    pages.append(lines)

# ---- ligature repair ----
changed = collections.Counter()
left_un = collections.Counter()


def cands(tok):
    idx = [i for i, ch in enumerate(tok) if ch in 'yz']
    out = []
    for r in range(1, len(idx) + 1):
        for combo in itertools.combinations(idx, r):
            s = list(tok)
            for i in sorted(combo, reverse=True):
                s[i:i + 1] = list('fi' if tok[i] == 'y' else 'fl')
            out.append(''.join(s))
    return out


def fix_token(tok):
    core = tok.strip("“”\"'’‘(),.;:!?—-")
    if not core or not re.search(r'[yz]', core):
        return tok
    low = core.lower()
    if Z(low, 'en') >= 1.5:
        return tok
    best = None
    bz = 1.5
    for c in cands(low):
        z = Z(c, 'en')
        if z > bz:
            bz = z
            best = c
    if not best:
        left_un[low] += 1
        return tok
    if core[0].isupper():
        best = best[0].upper() + best[1:]
    changed[low + ' -> ' + best] += 1
    return tok.replace(core, best, 1)


for pg in pages:
    for ln in pg:
        ln['t'] = ' '.join(fix_token(t) for t in ln['t'].split(' '))

json.dump(pages, io.open('ij_pages.json', 'w', encoding='utf-8'))
print('two-column pages:', twocol)
print('repaired token types:', len(changed), 'instances:', sum(changed.values()))
print('unrepaired non-words containing y/z:', sum(left_un.values()),
      dict(left_un.most_common(20)))
