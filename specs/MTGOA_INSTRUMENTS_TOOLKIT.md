> **STATUS: CURRENT — the measurement toolkit.** Written 2026-07-28.
> These instruments live only in an ephemeral session container. This doc is the durable copy.
> If you are picking this project up cold: paste an instrument into a file and run it against `ch1.md`–`ch9.md`.
> Companion doc: `claude/MANUSCRIPT_FILE_CANON.md` — which files are the book.

---

# MTGOA — Editorial Instruments

Every claim made about this manuscript should come from one of these, run against the actual chapter files. Planning documents have been wrong and have burned days. **Measure, do not recall.**

A standing rule that governs all of them: *never trust a detector's output without inspecting specimen lines first.* Two known contaminations in `imports.py` — `\bRed` with `re.I` matches "reducing"/"redemption" (n=35, all false) and `\bchi` matches "children"/"chip" (n=6, all false).

---

## THE REVIEWER GATE
Run this on every piece of new prose **before** it goes in front of Wendell. Non-negotiable.

```python
import re, io
t = io.open('FILE.md', encoding='utf-8').read()
print('andbut', len(re.findall(r'(^|[.?!]["”\'’]? |\*|\*\*|— |; )(And|But) ', t, re.M)),
      'banned',  len(re.findall(r'\broom\b|\bquiet(ly)?\b|\bgenuinely\b', t, re.I)),
      'emdash',  len(re.findall(r'[a-zA-Z0-9,]—[a-zA-Z0-9]', t)),
      'A0',      len(re.findall(r'you (were|was) (taught|told|raised|trained)|somewhere along the way|the village taught you', t, re.I)),
      'stacks',  len(re.findall(r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b', t)))
```

Every counter must read 0. Notes:

- `genuine` is **not** banned. Only `genuinely`.
- For HTML, strip `<style>` blocks first, then tags, then restore `&nbsp; &mdash; &ldquo; &rdquo;`, and gate the result.
- **Known gap:** the A0 regex misses belief-assertions of the form *"You Just Stopped Believing It Could Be"*. Read the prose too.
- **True-positive caveat:** the `stacks` regex fires on legitimate *quotations* of the defect inside editorial documents. Inspect matches before "fixing" anything.

---

## THE SAFE-EDIT PATTERN
Every manuscript edit goes through this shape. The write happens at the **end**, so a MISS or a DUPE aborts and writes nothing. Never `Edit` a chapter file directly on an anchor you have not counted first.

`spec_edit.py`

```python
# -*- coding: utf-8 -*-
import io
p='SPEC_REPETITION_AND_CUTS.md'
t=io.open(p,encoding='utf-8').read()
E=[]
E.append(("""**Housekeeping:** the source-analysis stub in the project credits""",
"""### 5.6 The fourth corpus — *Igniting Joy*

The three-book comparison was missing the only control that could settle a voice question: a book you already wrote. *Igniting Joy: Transforming Anger's Fire into Creative Passion via Humor* went through the same instrument as the other three. The sample is 4,779 words of continuous prose recovered from the extraction — front matter and the first two chapters — which is small, and every distortion the extraction introduced pushes the measured sentence length **down**, so the sample understates rather than overstates the gap.

| | MTGOA | Igniting Joy | Elliott | Chou |
|---|---|---|---|---|
| Mean sentence length | 13.4 | 17.9 | 23.7 | 22.5 |
| Median | 11 | 17 | 19 | 19 |
| Sentences ≤ 6 words | **27.5%** | **4.9%** | 12.4% | 12.8% |
| Commas per sentence | 0.53 | 1.21 | 1.41 | 1.62 |
| Subordinate-clause openers | 4.1% | 12.0% | 9.0% | 9.3% |
| Copula per 1k | 62.8 | 29.3 | 40.9 | 41.1 |
| Colon per 1k | 10.7 | 2.9 | 4.8 | 8.8 |
| Em-dash per 1k | 13.0 | 9.0 | 4.2 | 0.0 |
| we / our / us per 1k | 1.7 | 19.0 | 12.3 | 4.1 |
| I / me / my per 1k | 11.6 | 2.5 | 34.0 | 22.7 |
| Sentences opening And / But / So | 1.0% | 5.2% | 10.1% | 5.3% |
| Flesch reading ease | 73.7 | 50.7 | 54.9 | 53.8 |
| Grade level | 6.3 | 10.6 | 11.5 | 11.3 |

*Igniting Joy* lands beside Elliott and Chou on length, subordination and grade, and tighter than either on copula density and hedging. MTGOA sits outside all three on the short end. The distributions are close to inverted: your previous book puts 56.5% of its sentences in the 15-to-26-word band and 4.9% at six words or fewer; MTGOA puts 24.5% in that band and 27.5% at six or fewer.

Two further readings that are measurements, not recommendations. First, person: *we / our / us* runs at 19.0 per thousand in *Igniting Joy* and 1.7 in MTGOA, while *I / me / my* runs 2.5 against 11.6 — the books are built on opposite grammatical persons. Second, *Igniting Joy* opens 5.2% of its sentences with *And*, *But* or *So*, which the current voice rules put at effectively zero. That is a conflict between the rules and the control text, and it is your call, not mine; I am recording it rather than arguing either side of it.

**What the register repair returns in words.** Twelve real adjacent pairs, rewritten to the connective pattern the control text uses, measured: 182 words in, 161 out, mean **−1.75 per site**. The detector finds **464** pairs of that shape book-wide, of which 67 are true restatements. The whole narrow pool is therefore worth about **810 words**. A wider pass reaching into the 1,961 sentences of six words or fewer might reach 1,500 to 2,000. The register repair is a voice move that returns some words, not a word-count move.

**Housekeeping:** the source-analysis stub in the project credits"""))
E.append(("""The pattern in both mistakes is the same:""",
"""The third one you caught yourself. I wrote that the short declarative register *is* your voice, and it is not — it is the register this manuscript drifted into, and I was the one holding the pen for most of that drift. It is the second time in this project I have handed you prose I generated and described it back to you as something you built. The And/But taxonomy was the first. Calling it yours converts a defect into an asset and quietly protects it from the pass that should be removing it. The control text settles the question at 4.9% against 27.5%.

The pattern in all three mistakes is the same:"""))
E.append(("""and I carried it forward without testing the instrument. The Three Keep-Tests apply to my own findings, not only to your sentences.""",
"""and I carried it forward without testing the instrument. The Three Keep-Tests apply to my own findings, not only to your sentences. And the corollary the third one adds: when a feature of the prose needs defending, check whose hand put it there before defending it."""))
for i,(a,b) in enumerate(E,1):
    n=t.count(a)
    if n==0: raise SystemExit('MISS #%d: %r'%(i,a[:90]))
    if n>1: raise SystemExit('DUPE %d #%d: %r'%(n,i,a[:90]))
    t=t.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(t)
print('applied %d'%len(E))
```

---

## THE DUPLICATE SCANNER
Run on all new prose before insertion. A sentence has already been shipped in five separate chapters once. Do not let it happen twice.

`dupes.py`

```python
import re, collections, glob
for f in sorted(glob.glob('/home/claude/ch[2-9].md')):
    t=open(f).read()
    s=[x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if len(x.strip())>45]
    c=collections.Counter(s)
    d=[(n,x) for x,n in c.items() if n>1]
    if d:
        print(f)
        for n,x in d: print('  ',n,x[:110])
```

---

## PRACTICE-SURFACE DETECTOR
Counts reader-facing practice devices per chapter. Current baseline as of 2026-07-28 is in `claude/MANUSCRIPT_FILE_CANON.md`. `reflection prompts` reads 0 across all nine chapters — that convention is retired, not orphaned.

`practice.py`

```python
# -*- coding: utf-8 -*-
# Task 36: PRACTICE-EXAMPLE INVENTORY.
# What is Jordan actually handed to practice ON, and does every chapter hand her one?
import io, re, collections

L = {c: io.open('/home/claude/ch%d.md' % c, encoding='utf-8').read().split('\n') for c in range(1, 10)}

PAT = [
 ('do-it-now heading',  re.compile(r'^#{2,4}\s*(Try It Now|The One Rep|The Last Rep|Halfway|Your First BAR|Run the|Name One|In Practice|Before You)', re.I)),
 ('in-the-Village',     re.compile(r'in the Village', re.I)),
 ('quest block',        re.compile(r'^#{2,4}\s*From Card to Quest', re.I)),
 ('twenty cards',       re.compile(r'^#{2,4}\s*Your Twenty Cards', re.I)),
 ('shadow draw',        re.compile(r'^#{2,4}\s*Drawing Against the Shadow', re.I)),
 ('reflection prompts', re.compile(r'^#{2,4}\s*Reflection Prompts', re.I)),
 ('winning-when test',  re.compile(r"You're winning when|You are winning when", re.I)),
 ('BAR capture',        re.compile(r'capture it as a BAR|two minutes to capture', re.I)),
 ('polarity encounter', re.compile(r'^#{2,4}\s*Polarity Encounter', re.I)),
 ('scenario label',     re.compile(r'\*\*(Example|Scenario)\b|In practice:', re.I)),
]

print('=== PRACTICE SURFACE BY CHAPTER (counts) ===')
print('%-22s %s' % ('device', '  '.join('ch%d' % c for c in range(1, 10))))
grid = {}
for name, R in PAT:
    row = []
    for c in range(1, 10):
        n = sum(1 for l in L[c] if R.search(l))
        row.append(n); grid[(name, c)] = n
    print('%-22s %s' % (name, '  '.join('%3d' % n for n in row)))

print()
print('=== EVERY DO-IT-NOW / IN-THE-VILLAGE HEADING, IN READING ORDER ===')
HD = re.compile(r'^#{2,4}\s*(.*)')
for c in range(1, 10):
    for i, l in enumerate(L[c], 1):
        m = HD.match(l)
        if not m: continue
        t = m.group(1).strip()
        if re.search(r'Try It Now|One Rep|Halfway|Run the|Name One|In Practice|First BAR|Village|Before You|Put the Book', t, re.I):
            print('  ch%d:%-5d %s' % (c, i, t))

print()
print('=== THE TRANSFER TEST: is Jordan ever given a situation and asked to CHOOSE a face/move? ===')
CHOOSE = re.compile(r'which (face|move|game|card) (would|do) you|which one (does|do) (this|the) (moment|situation)'
                    r'|pick the (face|move|card)|choose the (face|move|card)|what would you (play|draw|reach for)'
                    r'|which face does this|which (face|move) the moment needs'
                    r'|write down .{0,40}which (face|move)', re.I)
hits = 0
for c in range(1, 10):
    for i, l in enumerate(L[c], 1):
        if CHOOSE.search(l):
            hits += 1; print('  ch%d:%-5d %s' % (c, i, l.strip()[:190]))
if not hits: print('  NONE FOUND across all nine chapters.')

print()
print('=== QUEST: how is the reader\'s own quest carried forward? ===')
Q = re.compile(r'\bquest\b', re.I)
for c in range(1, 10):
    ns = [(i, l.strip()) for i, l in enumerate(L[c], 1) if Q.search(l)]
    print('  ch%-2d  n=%d  %s' % (c, len(ns), ', '.join('%d' % i for i, _ in ns[:14])))
```

---

## CHAIN CHECK (claim → example → script)
Finds moves that assert without demonstrating. Validated output: worked 22 · script-no-scene 9 · **BARE CLAIM 4** (ch5:410, ch5:422, ch8:493, ch8:533).

Note: the manuscript scripts speech in **italics**, not quotes — the `ITAL` regex is what finds dialogue, not a quote-mark search. `chain.py` (v1) is retired; this is the validated instrument.

`chain2.py`

```python
# -*- coding: utf-8 -*-
# Task 34/35 v2: TEACH -> PERFORM -> APPLY, with the manuscript's ACTUAL conventions.
# Corrections from v1: sections accumulate to the next H2 (not the next H3);
# scripted speech is *italic*, not quoted; explicit **Example:** / In practice: labels count.
import io, re, collections

L = {c: io.open('/home/claude/ch%d.md' % c, encoding='utf-8').read().split('\n') for c in range(1, 10)}
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
```

---

## STYLOMETRY
Exports `syll`, `sents`, `measure`, `dewrap`. The comparison table against *Igniting Joy*, Carolyn Elliott, and Yu-kai Chou lives in `claude/SPEC_REGISTER_REMEDIATION_2026-07-28.md`.

`stylo.py`

```python
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
```

---

## EARNED SNAP / REGISTER RUNNER
*Earned snap* = a ≤7-word sentence whose left neighbour is ≥15 words. MTGOA 7.3% · Igniting Joy 18.4% · Existential Kink 18.6%. By chapter: ch1 17.8 · ch2 5.8 · ch3 12.2 · ch4 5.9 · ch5 8.4 · ch6 6.9 · ch7 6.9 · ch8 6.0 · ch9 2.6.

Housekeeping: point this at `ij_prose.txt`, not the older extracts.

`runstylo.py`

```python
# -*- coding: utf-8 -*-
import io,re,json
from stylo import measure,dewrap
U='/root/.claude/uploads/248d6205-9839-527b-b2a8-f162951173fa/'
def mtgoa():
    out=[]
    for c in range(1,10):
        L=io.open('/home/claude/ch%d.md'%c,encoding='utf-8').read().split('\n')
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
```

---

## TERM-DEBT TRACKER
Finds terms used before they are defined. Surviving real debts: Amber/Orange/Green (ch8:161, never defined) · Vulnerable Child (ch8:169, never) · Teal (ch8:161 → ch8:269) · altitude (ch3:167 → ch6:235) · Player (ch8:252 → ch8:606) · joystick (ch2:224 → ch2:312) · Forest (ch1:260 → ch2:87) · superpower (ch1:206 → ch2:320).

`termdebt.py`

```python
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
```

---

## NEGATION-STACK FINDERS
The *"Not X. Not Y."* construction is a voice defect, ruled by Wendell directly. `stacks.py` is the shorter variant.

`notstack.py`

```python
import re, sys, glob

FILES = sorted(glob.glob('/home/claude/ch[1-9].md'))

# A negation fragment: a sentence that STARTS with Not/No/Never/Nor/Don't and
# has no finite verb-y independent-clause shape -- we detect by: begins with
# the negator and is short-ish and does not contain " is " / " was " etc.
NEG_START = re.compile(r'^(Not|No|Never|Nor|Neither|Don\'t|Doesn\'t|Nothing)\b')

def sentences(text):
    # strip markdown headers/table rows for signal, keep line numbers
    out = []
    for ln, line in enumerate(text.split('\n'), 1):
        if line.startswith('#') or line.startswith('|'):
            continue
        # split into sentences
        parts = re.split(r'(?<=[.!?])\s+', line)
        for p in parts:
            out.append((ln, p.strip()))
    return out

total = 0
for f in FILES:
    text = open(f).read()
    sents = sentences(text)
    hits = []
    prev = None
    for i, (ln, s) in enumerate(sents):
        clean = re.sub(r'[*_`]', '', s).strip()
        if NEG_START.match(clean):
            hits.append((ln, clean))
    if hits:
        print('='*70)
        print(f, len(hits))
        for ln, s in hits:
            print(f'  {ln}: {s[:150]}')
        total += len(hits)
print()
print('TOTAL', total)
```

---

`stacks.py`

```python
import re, glob
NEG = re.compile(r'^(Not|No|Never|Nor|Neither|Don\'t|Doesn\'t|Nothing)\b')
FILES = sorted(glob.glob('/home/claude/ch[1-9].md'))
grand=0
for f in FILES:
    lines = open(f).read().split('\n')
    runs=[]
    for ln,line in enumerate(lines,1):
        if line.startswith('#') or line.startswith('|'): continue
        parts=[p.strip() for p in re.split(r'(?<=[.!?])\s+', line)]
        run=[]
        for p in parts:
            c=re.sub(r'[*_`]','',p).strip()
            if NEG.match(c): run.append(c)
            else:
                if len(run)>=2: runs.append((ln,run))
                run=[]
        if len(run)>=2: runs.append((ln,run))
    if runs:
        print('='*70); print(f, len(runs),'stacks')
        for ln,r in runs:
            print(f'  L{ln}: '+' || '.join(x[:70] for x in r))
        grand+=len(runs)
print('\nTOTAL STACKS', grand)
```

---

## REPETITION SWEEP
Cross-chapter repeated-phrase finder. Feeds `claude/SPEC_REPETITION_AND_CUTS_2026-07-28.md`.

`repeat.py`

```python
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
```

---

## IGNITING JOY EXTRACTION PIPELINE
**The authoritative extractor.** `SPLIT=315.0`, `orphanR>=5`. Produces `ij_prose.txt` (342 paragraphs / 20,077 words of running prose) from the 121-page PDF.

**Do not use** the `0b3c63da-CORPUS.txt` .txt of this book — Wendell said it cannot be trusted. **Retired:** `ij_clean.txt`, `clean_ij.py`, `pdfx.py`, `ij_extract.py`.

`ij_pipeline.py`

```python
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
```

---
Assembles `igniting_joy.md`. Housekeeping: fold the heading-merge post-pass in here; there is residual `##` spillover.

`ij_build.py`

```python
# -*- coding: utf-8 -*-
import json,io,re
pages=json.load(io.open('ij_pages.json',encoding='utf-8'))
OVR=[('zip the situation','flip the situation'),('frustration, zip','frustration, flip'),
     ('in order to yt into','in order to fit into'),('both feet zat on','both feet flat on'),
     ('pressyeld','Pressfield')]
BUL={'\x89':1,'\x8a':2,'\x8b':3,'\x8c':4,'\x8d':5,'\x8e':6,'\x8f':7}
out=[];prev=None
md=[]
for pno,pg in enumerate(pages,1):
    for ln in pg:
        t=ln['t']
        for a,b in OVR: t=t.replace(a,b)
        t=t.replace('\xa0',' ').replace('\xad','')
        m=re.match(r'^[\x89-\x8f]¯\x9d',t)
        bullet=bool(m)
        t=re.sub(r'[\x89-\x8f]¯\x9d','',t).replace('¯','').replace('\x9d','')
        t=re.sub(r'\s+',' ',t).strip()
        if not t: continue
        sz=ln['size']
        if sz<11: continue                       # running header / page number
        if abs(ln['y']-29.5)<2: continue          # top running header
        if re.match(r"^Igniting Joy: Transforming Anger's Fire",t): continue
        kind='title' if sz>=28 else ('head' if sz>=20 else 'body')
        out.append({'p':pno,'y':ln['y'],'x':ln['x'],'k':kind,'b':bullet,'t':t})
# assemble
blocks=[];cur=None
for i,l in enumerate(out):
    newpar = (cur is None or cur['k']!=l['k'] or l['b'] or
              (cur['p']==l['p'] and l['y']-cur['y']>22) or
              (cur['p']!=l['p'] and l['k']=='body' and cur['end_par']))
    if cur is not None and cur['k']==l['k'] and l['k']!='body' and cur['p']==l['p'] and l['y']-cur['y']<=40:
        newpar=False
    if newpar:
        if cur: blocks.append(cur)
        cur={'k':l['k'],'p':l['p'],'y':l['y'],'t':[l['t']],'b':l['b'],'end_par':False}
    else:
        cur['t'].append(l['t']); cur['y']=l['y']; cur['p']=l['p']
    cur['end_par']=bool(re.search(r'[.!?][”’")]?$',l['t'])) and len(l['t'])<60
if cur: blocks.append(cur)
md=[]
for b in blocks:
    t=re.sub(r'\s+',' ',' '.join(b['t'])).strip()
    if b['k']=='title': md.append('\n\n# '+t)
    elif b['k']=='head': md.append('\n\n## '+t)
    elif b['b']: md.append('- '+t)
    else: md.append(t)
doc='\n\n'.join(md)
doc=re.sub(r'\n{3,}','\n\n',doc)
io.open('igniting_joy.md','w',encoding='utf-8').write(doc)
w=len([x for x in doc.split() if not x.startswith('#')])
print('blocks',len(blocks),'words',w)
```

---

## CONSTRUCTION-SITE SCANNERS
The eight construction families (536 sites book-wide): A_beat · H_dashgloss (n=120) · F_isnotpair · D_democlose · E_notopen · C_interior · B_rhetq · G_hinge (n=20). Density: ch1 30 · ch2 21 · ch3 76 · ch4 77 · ch5 49 · ch6 62 · ch7 53 · ch8 89 · ch9 79.

**The three keep-tests.** Every site is *presumed cut*. It survives only by passing all three: **Function** · **Earned** · **Non-substitutable**. Dispositions: `KEEP` · `MERGE` · `REWRITE` · `CUT`. The burden of proof is on keeping, not on cutting — Wendell's ruling.

`ch2_sites.py`

```python
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
```

---

`sweep2.py`

```python
# -*- coding: utf-8 -*-
import io
path='/home/claude/ch9.md'
t=io.open(path,encoding='utf-8').read()
reps=[
("That's the only definition that matters. Not what you believe about allyship. Not what you intend to do when you're calm. What you do when you're activated",
 "That's the only definition that matters. What you believe about allyship is a separate question. What you intend to do when you're calm is a separate question. This one is what you do when you're activated"),
("Like any moves, they require practice. Not theory. Practice.",
 "Like any moves, they require practice — the doing kind, repeated, which is a different thing from having read about them."),
]
for a,b in reps:
    assert a in t and t.count(a)==1, a[:80]
    t=t.replace(a,b,1)
io.open(path,'w',encoding='utf-8').write(t)
print('ok')
```

---
