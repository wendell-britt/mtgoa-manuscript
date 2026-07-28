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
