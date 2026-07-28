# -*- coding: utf-8 -*-
import io, re
exec(open('specimens.py').read().split("random.seed")[0])
rows = []
for k, v in hits.items():
    for loc, s in v:
        if loc.startswith('ch2:'): rows.append((int(loc.split(':')[1]), k, s))
rows.sort()
paras = dict(prose_paras('ch2'))
for ln, k, s in rows:
    print('### %s  L%d' % (k, ln))
    print('LINE: %s' % s)
    ctx = paras.get(ln, '')
    if ctx.strip() != s.strip():
        print('PARA: %s' % ctx[:700])
    print()
print('TOTAL %d' % len(rows))
