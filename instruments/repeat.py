# -*- coding: utf-8 -*-
import re, io
CH=['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8','ch9']
CONCEPTS={
 'Forest':r'\bForest\b','Village':r'\bvillage\b','daemon':r'\bdaemons?\b',
 'joystick/controls':r'\bjoystick\b|\bthe controls\b','Shadow':r'\bShadow\b',
 'BAR':r'\bBAR\b','superpower':r'\bsuperpowers?\b','Faces':r'\bsix Faces\b|\bthe Faces\b|\bFace\b',
 'Guides':r'\bGuides?\b','WAVE':r'\bWAVE\b|Wake Up|Open Up|Clean Up|Grow Up|Show Up',
 'channels':r'\bchannels?\b','Polarity':r'\bPolarit(y|ies)\b','3-2-1':r'3-2-1',
 'tokens/tickets':r'\btokens?\b|\btickets?\b','domains':r'\bdomains?\b',
 'deck/cards':r'\bdecks?\b|\bcards?\b','quest':r'\bquests?\b',
 'Game Master':r'\bGame Master\b','exile':r'\bexiles?\b|\bexiled\b',
 'alchemy':r'\balchemy\b|\balchemi',
 'burnout/debt':r'\bburn(ed)? ?out\b|\bburnout\b|\bdebt\b',
 'the Game':r'\bthe game\b','Infinite Arcade':r'\barcade\b',
}
DEF=re.compile(r"(\bis\b|\bare\b|\bmeans\b|\bcalls?\b|\bcalled\b|refers to|Here'?s what|what .{0,20}actually is|\bis not\b|\bisn'?t\b)",re.I)
def paras(fn):
    out=[];buf=[];start=1
    for i,l in enumerate(io.open(fn,encoding='utf-8').read().split('\n'),1):
        s=l.strip()
        if not s:
            if buf: out.append((start,' '.join(buf))); buf=[]
            continue
        if not buf: start=i
        buf.append(s)
    if buf: out.append((start,' '.join(buf)))
    return out
P={c:paras(c+'.md') for c in CH}
print('%-18s %s'%('CONCEPT','definition-events per chapter (ch:line,line)'))
print('-'*100)
for name,pat in CONCEPTS.items():
    rx=re.compile(pat)
    ev={}
    for c in CH:
        hits=[]
        for ln,p in P[c]:
            if rx.search(p) and DEF.search(p) and len(p.split())>=12:
                hits.append(ln)
        if hits: ev[c]=hits
    tot=sum(len(v) for v in ev.values())
    chs=len(ev)
    if chs>=2:
        print('%-18s chs=%d evt=%-4d %s'%(name,chs,tot,'  '.join('%s:%s'%(c,','.join(map(str,v[:6]))) for c,v in ev.items())))
