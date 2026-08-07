# Agency Traceability Audit — distribution report and pattern synthesis

**Spec:** `SPEC_AGENCY_TRACEABILITY_AUDIT_20260802`
**Pass:** analysis only. No prose file was edited. Every rewrite in every ledger is a proposal.
**Method:** ten agents, one rubric, nine chapters plus the appendix/matter surface, with
`instruments/agency_grep.py` running underneath as a recall net.
**Date:** 2026-08-02

---

## The headline

The spec's §2.4 hypothesis is **false**, and the thing that replaces it is better.

The bet was that the defect clusters in legacy pre-gauntlet prose and is sparse in
rebuilt chapters — *"a small job wearing a big plan."* It is not in the legacy prose.
It is in **one recurring narrative device, present in seven surfaces, including the
most-revised chapters in the book.**

The village fable. In ch3 it carries 11 of 12 Tier 3 sites. In ch4, 24 of 26 Grade 6
violations, inside 110 lines, while the other 80% of the chapter is clean. It recurs in
ch5, ch7, ch8, ch9 and the Key Terms glossary. It is the single largest pattern in the
audit and **it is not in the Registry at all.**

And `specs/VOICE_ANCHOR.md` already protects it.

---

## AC-2 — distribution

Body text only; marginalia frame stripped. Tier 3 = perception/intention on an
unlicensed subject, or social-causal on Grade 6/7.

| surface | T3 | T2 | T1 | dominant op | characteristic failure |
|---|---:|---:|---:|---|---|
| ch1 Infinite Arcade | 6 | 8 | 1 | R1 ×5 | abstraction in expository asides; people named freely in testimony |
| ch2 Forest | 11 | 5 | 0 | R1 ×8 | personifies the training it is diagnosing |
| ch3 Shaman | 12 | 2 | 0 | R1 ×10 | **village origin myth** (11 of 12); rest of chapter clean |
| ch4 Challenger | 22 | 3 | 1 | R1 ×14 | **village fable, L66–175** (24 of 26 G6); §4–7 clean |
| ch5 Regent | 9 | 7 | — | R1 ×9 | **village-and-Faces fable**; plus the office taking the officeholder's agency |
| ch6 Architect | 9 | 7 | 6 | **R2 ×12** | document-speech idiom; paragraph-joint compression |
| ch7 Diplomat | 10 | 6 | 2 | R1 ×15 | **"the field"** knows/decides/trusts, in the explanatory register |
| ch8 Sage | 30 | 1 | 4 | R1 ×23 | **village parable legislates**; liturgical lookalikes |
| ch9 Player | 16 | 7 | 10 | R4 ×6 | **village origin fable**; thesis-contradiction sites |
| appendices + matter | 6 | 9 | 1 | R1 ×5 | the book standing in for the author |
| **total** | **131** | **55** | **25** | **R1 ×96** | |

**R-op distribution book-wide:** R1 96 · R2 22 · R6 14 · R4 11 · R3 8 · R5 0.

**Flags:** W-1-PENDING 10 · W-2-PENDING 57 · AMBIGUOUS-REFERENT 34 sites ·
HANDBOOK-REGISTER 5 · CHARACTER-VOICE 2 · REGISTRY-GAP ~29 unlogged (ch9 alone).

**Legacy baseline (recall net only, not agent-adjudicated):** `MTGOA_TEAL_080525.md`
300 candidate rows, 26.76/10k. Manuscript chapters run 16.90–32.14/10k. The legacy doc
is **not** an outlier.

---

## The five patterns

### 1. The village — seven surfaces, and the audit's whole centre of gravity

ch3 · ch4 · ch5 · ch7 · ch8 · ch9 · Appendix C Key Terms.

The village learns, forgets, sees, means, needs, notices, hears, wants, prefers,
legislates, trains, teaches. In ch3 it hits the registry's own worked example verbatim:

> *"The village trains everyone to turn feeling down. It hands you a dial in childhood
> and teaches one direction: lower it."* — ch3:316

In ch8 it legislates:

> *"The village had made a rule: if you can see the pattern of the game, you must stop
> playing."* — ch8:89

Two agents (ch8, ch9) **refused to grade it** and tagged `REGISTRY-GAP` instead, because
"the village" appears nowhere in `agency_registry.yaml`. That is the correct refusal
under C2 — and it means the true site count inside the fables is **higher than any
ledger here reports.** ch9 alone left ~23 instances unlogged.

**The device is protected by existing canon.** `specs/VOICE_ANCHOR.md` §3 quotes ch4:115
as a protected anchor. The quoted passage ends:

> *"The village learned to make its nos sound like yeses because yeses cost less."*

The same quotation carries *"The workshops teach the scripts."* The anchor's stated
protection is **the humor** — the Jerk archetype, mocking the process not the person —
and it is in the set deliberately, because *"an anchor with no comedy in it will let the
Voice Guardian approve a book that has stopped being funny."*

Whether that protection reaches the village construction itself, or only the joke it
carries, the anchor does not say.

**C2 gives the direction:** where the Registry and older canon conflict, **the older
canon wins and the Registry is amended.** VOICE_ANCHOR.md is older than a Registry
written this morning. On the constitution's own rule the device stands until Wendell
rules otherwise. Every village site, all six chapters, is held as keep-candidate.

There is also a genre argument nobody has made yet and somebody should: **a fable is a
form in which collective personification is native equipment.** The village thinking as
one is how fables have always worked. Four agents independently ledgered it as defect
because the rubric told them to. The rubric may be wrong at this one point.

### 2. Each chapter fails in its own dialect

The fan-out was designed to answer whether the defect is Face-linked. It is.

- **ch6 Architect** is the outlier, in the right direction. R2 ×12 against R1 ×2 — the
  inverse of every other chapter. Its failures are *document-speech* ("the report says,"
  "the org chart says") and *paragraph-joint compression*, where a mechanism stated one
  paragraph earlier is not restated at the sentence that needs it. Both are recoverable
  by mechanize, the house's no-risk move. The recall net rated ch6 the book's densest
  chapter; the agent's verdict is that the net **overstates by 2–3×** and 24 of 33
  systemic constructions clear on mechanism-on-page.
- **ch5 Regent** carries a register no other chapter has: the office taking the agency of
  the person holding it. *"New leadership wants to retire the quarterly all-hands"* (628).
  *"Real loyalty sees the whole inheritance… and decides"* (315).
- **ch7 Diplomat** runs its central conceit, "the field," as a mind ~40 times — including
  in **the chapter's own definition of its key term** (138: *"offered as information,
  once, to a field that is then free to answer"*).
- **ch8 Sage** carries the liturgical lookalike: *"The pattern shows fully and nothing in
  you moves about it"* (373) reads like protected Grade 3 liturgy, but the subject is the
  pattern, not a channel, so the protection does not reach it.

### 3. Apparatus hides a different person than chapters do

**Chapters hide the person who acted. Appendices hide the person who decided.**

22 of the surface's sites are the book/chapter/appendix standing in for Wendell, taking
verbs he performed: teaches, asks, names, quotes, proposes. Nine of the 22 are in
Appendix G — the bibliography, the one document whose every sentence records a choice he
made.

### 4. The embodied-three roster is broken in two places by two hands

ch2 §6 restricts Protector, Emotional Body and Damaged Self to **somatic** action, not
verbal. Broken at:

- ch2:302 — *"It trades contact for control and calls the trade safety."* (Protector, naming verb) — two sections after the chapter establishes the rule
- APPENDIX_A:159 — *"Protector names the conditions a group needs to function."* (same daemon, same violation, different surface)

This is a canon violation the agency audit found by accident. It is independent of every
W ruling.

### 5. B6 survives — in ch1, not ch9

ch9 is **clean**: grepped explicitly, zero machine-perceives constructions. The ban holds
where the arcade conceit runs hardest.

It fails in ch1:

> *"A short, unflattering diagnostic… **tells you** which of these are yours… it will not
> **tell you** which kind of ally you are"* — ch1:83

Grade 4 machine, perception verb, the construction banned verbatim and forever. The fix
is already in the sentence next door: *"It scores how you actually behave."*

---

## Three Registry gaps — C2 reserves these to Wendell

1. **`DAEMON_CANON.md` does not exist in this repo.** C2 makes it canon outranking the
   Registry and Grade 2 defers to it for each daemon's canonical job. Carried with a
   `MISSING FROM REPO` marker rather than dropped.
2. **`"the field"`** — ch7's central conceit, defined at ch7:359, ~40 agentive verbs, no
   grade-table entry. Agent adjudicated Grade-6-equivalent and flagged rather than adding.
3. **`"the village"`** — seven surfaces, the largest pattern in the audit, no entry. Two
   agents refused to grade it.

---

## The T0 rulings, now with evidence

### W-1 — do channels get intention verbs?

**10 sites book-wide. 6 of them in ch3.** The ch3 agent's Grade 3 census: ~15–18
liturgical (protected), ~12 directional, ~10 perception, 6 intention.

**The finding that should decide it:** the liturgical register **never once reaches for
an intention verb.** The signature device is disciplined. The W-1 leakage happens
entirely in the connective-tissue sentences around it. Whichever way you rule, the
protected passages are unaffected — which makes this the cheapest of the four rulings.

### W-2 — does the book get a discourse license?

**57 sites. 22 in the appendices, 11 in ch3, 0 in ch1.**

This is not a chapter problem. It is an **apparatus** problem, concentrated where the
book describes its own machinery — and ch3, the one chapter that opens by explaining its
own length and closes with a full recap. ch1, which is pure conceit and testimony, has
zero.

Ruling against the license means ~57 conversions to the author's chair, most of them in
reference apparatus where first person may not fit the register. The appendix agent
flagged that tension directly: R4 is right in a chapter and can be wrong in a glossary.

### W-3 — print scope cutoff

**Cannot be estimated until the village ruling lands.** If the device is protected,
Tier 3 drops from 131 to roughly 60 and the print job is small and surgical. If it is
not, ch3, ch4, ch5, ch8 and ch9 each need a fable rebuilt, and that is not a print-scope
job at all — it is edition two.

**The village ruling is therefore the gate on W-3, not the other way round.**

### W-4 — placement of the confrontation beat

Three candidates, ranked:

1. **ch3:744 — already written.** *"So the council said its words. It spoke of
   resilience… and it moved not one handful of earth."* The chapter stages institutional
   speech against one woman's individual sentence three paragraphs later. That is the
   beat's entire argument, on the page, by hand, in the control chapter. Held as
   keep-candidate, not ruled.
2. **ch4** — the fable ends on the banned verb *"taught"*; a textbook illustration, but it
   illustrates without naming.
3. **ch7 §3 (154–158)** — can host it, but the agent found **no** passage where a
   character reaches for systemic language specifically to dodge naming one person. The
   three closest analogs use silence or interpersonal softening. Building the beat here
   means scaffolding, *and* fixing ch7's own field personification first, or the beat
   lands in a chapter still performing the error it condemns.

---

## AC-5 is moot; here is what replaced it

The 60% precision gate governed the spaCy linter build. Agents-as-detector was ruled
instead, so there is no mode to gate. Measured recall-net precision, per agent:

| chapter | net T3 rows | real | noise | agent-found, net-missed |
|---|---:|---:|---:|---:|
| ch1 | 3 | 3 | 0 | — |
| ch3 | 11 | 5 | 6 | most findings |
| ch4 | 8 | 6 | 2 | 17 |
| ch6 | 35 raw | 12 | 23 | 4 |
| ch7 | 9 | 2 | 7 | most findings |
| ch8 | 21 | ~10 | 11 | the entire village bloc |
| ch9 | 27 | 21 | 5 | ~23 |

Net precision runs roughly 22–75% by document and its recall is worse than its precision:
**it has no entry for "the village" and therefore missed the largest pattern in the book
entirely.** It did its job — it caught regions, not defects — and it should be kept as a
regression check, not promoted.

**Cross-agent agreement was high.** No two agents graded a comparable construction
differently. The one systematic divergence is the village, and every agent that met it
either ledgered it consistently as Grade-6-equivalent or refused to grade it and said so.

---

## What I recommend

**Rule the village first.** It gates W-3, it decides roughly half the Tier 3 volume, and
it is a C3 somatic-gate call that no instrument and no agent may make. Read ch4:115 and
ch3:316 aloud, back to back, and the ruling will make itself.

**Fix ch1:83 regardless.** B6 is banned verbatim, the violation is in a shipping chapter,
and the correct construction is already in the adjacent sentence. It depends on no
ruling.

**Fix the copyright line regardless.** `front_matter/copyright.md` carries *"material
that wants a trained person in the chair with you"* — a Grade 0 subject taking the
highest-severity intention lemma, inside the duty-of-care disclaimer. Of every site in
this audit, that is where the abstraction standing in for a person costs the most,
because the sentence exists to tell a reader in trouble that a person should be present.

**Treat the embodied-three breaks as canon repair, not agency remediation.** ch2:302 and
APPENDIX_A:159 violate ch2 §6 directly and need no W ruling.

**Hold R1.** It fired 96 times. C5's guard against R1 drumbeating into scolding was
written as a theoretical risk; at this volume it is the audit's central execution problem.
Every agent varied its constructions and documented how, but no R1-heavy batch should
land without the AC-4 profile check — and if the village is protected, most of the 96
evaporates on their own.
