# -*- coding: utf-8 -*-
import os as _os
MS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _os.pardir, 'manuscript') + _os.sep
import io,re,json
from stylo import measure,dewrap
U='/root/.claude/uploads/248d6205-9839-527b-b2a8-f162951173fa/'
def mtgoa():
    out=[]
    for c in range(1,10):
        L=io.open(MS+'ch%d.md'%c,encoding='utf-8').read().split('\n')
        for l in L:
            s=l.strip()
            if not s: continue
            if s.startswith('#') or s.startswith('|') or s.startswith('>') or s.startswith('---'): continue
            if re.match(r'^[-*+]\s',s) or re.match(r'^\d+\.\s',s): continue
            if s.startswith('!['): continue
            s=re.sub(r'\*\*|\*|`','',s)
            if len(s.split())<4: continue
            out.append(s)
    return '\n'.join(out)
def elliott():
    L=io.open(U+'4c230fab-CORPUS.txt',encoding='utf-8',errors='replace').read().split('\n')
    L=L[574:7146]
    L=[l for l in L if not re.match(r'^\s*(\d{1,3}|Existential Kink|Carolyn Elliott.*)\s*$',l)]
    return '\n'.join(dewrap(L))
def chou():
    L=io.open(U+'84dc34cc-CORPUS.txt',encoding='utf-8',errors='replace').read().split('\n')
    L=L[395:996]
    L=[l for l in L if not re.match(r'^\s*(\d{1,3})\s*$',l)]
    return '\n'.join(dewrap(L))
def ij(full=True):
    t=io.open('/home/claude/ij_clean.txt',encoding='utf-8').read()
    if full: return t
    ps=t.split('\n\n');keep=[]
    for p in ps:
        dmg=p.count(' thing')+sum(1 for s in re.split(r'(?<=[.!?])\s+',p) if s[:1].islower())
        if dmg<=1: keep.append(p)
    return '\n\n'.join(keep)
rows=[measure('MTGOA',mtgoa()),measure('Igniting Joy (Wendell, 2024)',ij(True)),
      measure('IJ clean-subset',ij(False)),
      measure('Existential Kink (Elliott)',elliott()),measure('10,000 Hours (Chou)',chou())]
json.dump(rows,io.open('stylo.json','w',encoding='utf-8'))
K=[('words','%d'),('sents','%d'),('mean','%.1f'),('median','%d'),('sd','%.1f'),('burst','%.1f'),
   ('commas_per_sent','%.2f'),('subord_pct','%.1f'),('copula_1k','%.1f'),('emdash_1k','%.1f'),
   ('semicolon_1k','%.1f'),('colon_1k','%.1f'),('you_1k','%.1f'),('i_1k','%.1f'),('we_1k','%.1f'),
   ('q_1k','%.1f'),('contr_1k','%.1f'),('hedge_1k','%.1f'),('and_but_pct','%.1f'),('fre','%.1f'),('fk','%.1f')]
hdr='%-18s'%'metric'+''.join('%-14s'%r['name'][:13] for r in rows);print(hdr)
for k,f in K:
    print('%-18s'%k+''.join('%-14s'%(f%r[k]) for r in rows))
print()
bins=['1-6','7-10','11-14','15-19','20-26','27-35','36+']
print('%-18s'%'len dist %'+''.join('%-14s'%r['name'][:13] for r in rows))
for i,b in enumerate(bins):
    print('%-18s'%b+''.join('%-14s'%('%.1f'%r['dist'][i]) for r in rows))
