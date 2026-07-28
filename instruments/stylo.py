# -*- coding: utf-8 -*-
import io,re,sys,math
VOW=re.compile(r'[aeiouy]+')
def syll(w):
    w=w.lower().strip(".,;:!?()\"'’—")
    if not w: return 0
    n=len(VOW.findall(w))
    if w.endswith('e') and n>1: n-=1
    return max(1,n)
ABBR=r'(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<!\bSt)(?<!\bvs)(?<!\be\.g)(?<!\bi\.e)(?<!\bPh\.D)'
def sents(t):
    t=re.sub(r'\s+',' ',t)
    parts=re.split(ABBR+r'(?<=[.!?])["”’\')]?\s+(?=[A-Z“"\'(])',t)
    return [p.strip() for p in parts if len(p.strip().split())>=2]
HEDGE=re.compile(r'\b(actually|really|just|sort of|kind of|somewhat|maybe|perhaps|probably|quite|very|rather|basically|essentially|simply)\b',re.I)
COP=re.compile(r"\b(is|are|was|were|am|be|been|being)\b|'s\b|’s\b",re.I)
SUBORD=re.compile(r'^(When|While|Because|Although|Though|If|Since|As|After|Before|Unless|Until|Whether|Once|Where|Whereas|Given|Having|Being)\b')
def measure(name,text):
    S=sents(text)
    W=text.split()
    n=len(W); ns=len(S)
    ls=[len(s.split()) for s in S]
    ls_s=sorted(ls)
    mean=sum(ls)/float(ns); med=ls_s[ns//2]
    sd=math.sqrt(sum((x-mean)**2 for x in ls)/float(ns))
    bins=[(1,6),(7,10),(11,14),(15,19),(20,26),(27,35),(36,999)]
    dist=[100.0*sum(1 for x in ls if a<=x<=b)/ns for a,b in bins]
    burst=sum(abs(ls[i+1]-ls[i]) for i in range(ns-1))/float(ns-1)
    per1k=lambda c: 1000.0*c/n
    syl=sum(syll(w) for w in W)
    fre=206.835-1.015*(n/float(ns))-84.6*(syl/float(n))
    fk=0.39*(n/float(ns))+11.8*(syl/float(n))-15.59
    r={'name':name,'words':n,'sents':ns,'mean':mean,'median':med,'sd':sd,
       'dist':dist,'burst':burst,
       'commas_per_sent':text.count(',')/float(ns),
       'semicolon_1k':per1k(text.count(';')),
       'colon_1k':per1k(text.count(':')),
       'emdash_1k':per1k(text.count(u'—')),
       'you_1k':per1k(len(re.findall(r'\b(you|your|yours|yourself)\b',text,re.I))),
       'i_1k':per1k(len(re.findall(r"\b(I|I'm|I’m|me|my|mine|myself)\b",text))),
       'we_1k':per1k(len(re.findall(r'\b(we|our|us|ours)\b',text,re.I))),
       'q_1k':per1k(sum(1 for s in S if s.rstrip().endswith('?'))),
       'contr_1k':per1k(len(re.findall(r"\w[’']\w",text))),
       'hedge_1k':per1k(len(HEDGE.findall(text))),
       'copula_1k':per1k(len(COP.findall(text))),
       'subord_pct':100.0*sum(1 for s in S if SUBORD.match(s))/ns,
       'and_but_pct':100.0*sum(1 for s in S if re.match(r'(And|But|So|Or|Yet)\b',s))/ns,
       'fre':fre,'fk':fk}
    return r
def dewrap(lines,thresh=58):
    paras=[];cur=[]
    for l in lines:
        s=l.rstrip()
        if not s.strip():
            if cur: paras.append(' '.join(cur));cur=[]
            continue
        cur.append(s.strip())
        if len(s.strip())<thresh and re.search(r'[.!?][\)"”’\']?$',s.strip()):
            paras.append(' '.join(cur));cur=[]
    if cur: paras.append(' '.join(cur))
    return [p for p in paras if len(p.split())>=8]
