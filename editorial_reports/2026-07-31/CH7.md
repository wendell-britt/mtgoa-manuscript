# CHAPTER 7 — THE DIPLOMAT · chapter-level diagnosis

**2026-07-31.** Role 2 of the Lean Editorial OS, run against `manuscript/ch7.md`
as it sits on disk, **marginalia frame in place** — all line numbers below are
frame-included and will not match the Architect's stripped-file numbers.
Diagnosis only; no prose was changed, no instrument that mutates a file was run.

**Summary.** Chapter 7 does the job it was given. Jordan arrives saying *I
accommodate, then resent* and the chapter meets that sentence head-on and by
name at ch7:397–403 (**Resentful Peace → Honest Terms**), which is the single
best-aimed passage in the chapter. The myth architecture also works: the myth is
planted (ch7:120), collected by the daemon (ch7:463), and cashed at the close
(ch7:703) with a replacement sentence a person can carry — that three-beat run is
the reference implementation and it earns the name. The damage is elsewhere and
it is concentrated in one place: **the chapter's own apparatus does not agree
with itself.** A summary table promises five alchemical arcs and Section 4
delivers two of them; the recap claims a practice the chapter never ran; the word
*channel* means two different things eighty pages apart; and one paragraph is an
unfilled note to the author, in brackets, addressed to Wendell by name, sitting
in shipped prose. Ten separately named practice structures across Sections 4 and
6 is also the mechanical form of the documented drop-off risk — the five channels
do read as more things to do, because they arrive with five more structures
underneath them.

**Flag count.** Structure **7** · Continuity and claims **4** (3 ERROR, 1 ERROR
with a print-blocker attached) · Line-level **6**. Total 17.

---

## VERDICT 1 — the "zero do-it-now headings" question

**Verdict: the Architect's count is correct and the inference from it is wrong.
Chapter 7 hands Jordan more to do right now than most chapters in the book. Do
not act on this finding.**

The detector is `instruments/practice.py:11`, which matches **markdown headings
only**, against a closed title list:

```
('do-it-now heading', re.compile(r'^#{2,4}\s*(Try It Now|The One Rep|The Last Rep|Halfway|Your First BAR|Run the|Name One|In Practice|Before You)', re.I))
```

Run across canon it returns ch1:1, ch2:2, ch3:1, ch4:1, ch5:2, ch6:1, **ch7:0**,
ch8:1, ch9:1. So ch7 is genuinely the only chapter with no *heading* from that
list. What ch7 has instead, under other conventions:

- **ch7:157 (body)** — "**Try this now.**" followed by a four-step numbered
  exercise (ch7:159–173) with an axis to draw and a fill-in sentence. This is the
  *same instrument* ch4:175, ch4:440 and ch5:220 carry — those three are bold
  runners, not headings, and the detector misses all of them too. ch7 is not the
  outlier; the detector's title list is.
- **ch7:479, ch7:588, ch7:684 (body)** — three italic capture prompts ending
  `→ app`, one per major section. ch2 and ch3 carry three each; ch8 carries three.
  ch7 is at parity.
- **ch7:672 (body)** — "Run it once, on something real. Bring the last time
  someone told you about your impact." A full five-move run with a per-move
  instruction, timed at ninety seconds.
- **ch7:586, ch7:634 (body)** — "**Before you name them, ask:**" and "**Before you
  refuse false equivalence, ask:**", each a go/no-go self-check attached to a move.
- **ch7:565–566 (margin)** — "*say it to yourself in one sentence before you go
  in. Not to decide anything. Only to find out which half you are in.*" A
  performable instruction, but delivered in the annotator's voice rather than the
  body's, so it is not the chapter making the ask.

**What is actually true and worth keeping:** ch7's do-it-now material is
unheaded, so it is invisible to the table of contents, to a skimmer, and to every
instrument that reads structure. Jordan skims theory and stops for a named move
with a practice — she can only stop at what she can see stopping at. That is a
typographic finding for the print pass, not a missing-practice finding. **Logged
as resolved; the underlying complaint is that ch4's and ch5's bold runners have
the same problem and no one has ruled on the convention.**

---

## VERDICT 2 — the bracket-placeholder question

Three distinct bracket conventions run in this one chapter, and they need three
different answers.

**(a) `[Camp A]` / `[Camp B]` at ch7:546 — INTENDED, keep, but they are
unmarked.**

> ch7:546 (body) — "The Diplomat translates: *"What I hear [Camp A] saying, in
> [Camp B]'s language, is this: the process choices you're making signal something
> about whether our work is valued."*"

These are generic role labels inside a model script, not unfinished text. Two
things establish it: the labels carry meaning (*Camp A*, *Camp B* are the two
parties the paragraph has just set up at ch7:544), and they are used
*referentially* four more times in the same paragraph — "Now [Camp B] can hear
what [Camp A] is actually saying" — which is behaviour no placeholder exhibits.
Unfinished text does not maintain internal consistency across five uses.

The genuine defect is that the chapter has already taught Jordan a *different*
fill-in convention 380 lines earlier, using underscores:

> ch7:169–170 (body) — "*"I protect __________ because it makes __________
> possible, and the thing I have not yet said is __________."*"

So a reader who has learned that a blank is `__________` meets a bracket and has
to decide, unaided, whether she is supposed to fill it. In the same chapter the
bracket also means *production tag* (ch7:202 `**[DISSATISFACTION → SATISFACTION]
Alchemy 1**`, 23 instances) and *note to the author* (ch7:467, below). **Verdict:
not unfinished, do not cut, but the ambiguity is real and it is caused by the
other two bracket uses, not by this one.**

**(b) `[[TESTIMONY SLOT — WENDELL. …]]` at ch7:467–469 — UNFINISHED. Hard print
blocker.** Raised as its own flag at **C3** below.

**(c) `[DISSATISFACTION → SATISFACTION]`, `[TRANSLATE]`, `[CONTROL]` — already
ruled, fix has not landed.** Not re-reported here as a new finding.
`specs/SPEC_BRACKET_TAGS_2026-07-29.md` documents the whole history: the mechanic
was deprecated 2026-06-03, the fix was applied to the retired `chapters/` tree,
`manuscript/` never received it, and the acceptance grep was scoped so it could
not catch that. The spec's own check is
`grep -c "\[DISSATISFACTION\|\[TRANSLATE\]\|\[CONTROL\]" manuscript/ch*.md # must be 0`;
**ch7 currently returns 23 and ch8 returns 5.** The `Neutral Channel` relabel was
ruled 6–0 in `specs/PANEL_NEUTRAL_CHANNEL_2026-07-29.md` and is likewise still
unapplied — ch7 carries 11 uses. Recorded so the ch7 pass is not read as clearing
them.

---

## A. CHAPTER STRUCTURE

### [S1] The EA table promises five alchemical arcs; Section 4 delivers two of them
- **Location:** ch7:71–79 (body), against ch7:252, ch7:279, ch7:317, ch7:323, ch7:355, ch7:361
- **Evidence:** "| **Translator** | Earth/Neutrality | Disagreement → Dialogue |" … "Each mode's full arc, the dissatisfaction it carries and the alchemy that transmutes it, is worked through in the five channel deep-dives in Section 4."
- **Reader problem:** ch7:79 is an explicit promise that every row of the table is worked through later. Three of five rows are not. Translator is promised *Disagreement → Dialogue* and Section 4 gives *Arrogant Distance → Generous Hearing* and *Translation Guilt → Legitimate Partiality*. Field-Holder is promised *Inclusion-performance → Genuine inclusion* and gets *Anxiety → Grounded Presence* and *Collapsed Calm → Active Containment*. Repairer is promised *Rupture → Repair (moral equivalence → discerned equivalence)* and gets *Betrayal Wound → Discerning Trust* and *Performance Forgiveness → Genuine Repair* — while the moral-equivalence material the row names is actually delivered under a different channel entirely, at ch7:429. Only Bridge-Builder and Integrative Negotiator pay out. Jordan's stated trigger is claims without practice; this is a table of claims with a stated pointer to a practice that is not there when she arrives.
- **Category:** structure
- **Disposition:** structural decision — either the table is rewritten from Section 4, or Section 4 is rewritten from the table; the two were authored from different drafts and only one can survive.
- **What would disprove this:** finding *disagreement → dialogue*, *inclusion-performance*, or *moral equivalence → discerned equivalence* worked as a named arc anywhere in ch7:194–437 under vocabulary I did not search.

### [S2] The recap claims a practice the chapter never ran
- **Location:** ch7:705 (body)
- **Evidence:** "The five stages form the chapter's spine, and you have now practiced all five: Bridge, Translate, Hold, Repair, Negotiate."
- **Reader problem:** The five *stages* are stated at ch7:43, restated at ch7:45, ch7:387 and ch7:572, and recapped here — the sequence is present and consistent, so the five-beat requirement is met. What is absent is any practice keyed to a stage. Section 4 practises the five **channels**; Section 6 practises the five **moves**; nothing in the chapter asks Jordan to do Bridge, then Translate, then Hold. She is told she has done a thing she has not been asked to do, in the recap, which is the position where she is most likely to conclude she missed something and that the missing thing was her fault.
- **Category:** structure
- **Disposition:** fix locally — the claim is one clause.
- **What would disprove this:** a stage-sequenced exercise anywhere in ch7 that walks Bridge→Translate→Hold→Repair→Negotiate as steps.

### [S3] The move the chapter says it was built toward is the one move missing its scaffold
- **Location:** ch7:558–588 (body), against ch7:516–556, ch7:592–638
- **Evidence:** ch7:572 — "It is the move the whole chapter has been building toward, and the one the Diplomat's altitude skips most reliably."
- **Reader problem:** Every other chapter runs `**Why it matters:**` five times out of five (ch3, ch4, ch6, ch8 all 5/5). ch7 runs it three times — Moves 1, 2 and 4 have it; **Move 3 and Move 5 do not**. Move 3 is also the only move in ch7 with no labelled `**Working vs. performed:**` (Moves 1, 2, 4, 5 all carry it); the material is present at ch7:584 but unlabelled, so it does not appear where Jordan's eye has been trained by four repetitions to look for it. The chapter's climax is the one place its own teaching template breaks.
- **Category:** structure
- **Disposition:** structural decision — restore the template on Moves 3 and 5, or drop `Why it matters` from all five and accept the divergence from ch3/ch4/ch6/ch8.
- **What would disprove this:** a ruling on record that ch5–ch8 deliberately run a lighter move template than ch3/ch4. ch5 runs `Why it matters` once and ch6 five times, so the convention is not stable book-wide and this may be a book-level question rather than a ch7 one.

### [S4] Section 2's forward promise is not paid off in the terms it was made
- **Location:** ch7:53 (body), against ch7:497–499
- **Evidence:** "The Diplomat's working capacity is honest multiplicity… That capacity supplies the raw material. What it is *for* arrives at the end of Section 5."
- **Reader problem:** This is an explicit deferral with a named address, so Jordan is entitled to arrive at the end of Section 5 and collect. What is there (ch7:497–499) is the payoff for the **Victim developed** and the Connector superpower — a good passage that never mentions honest multiplicity, never uses the word *capacity*, and does not close the loop it was sent to close. The setup and the payoff are both fine; they are not the same loop. Compounding it, *it* in "What it is *for*" has two live antecedents in the preceding sentence (the capacity, the raw material).
- **Category:** structure
- **Disposition:** structural decision — either point ch7:53 at what Section 5 actually ends on, or land the honest-multiplicity payoff there.
- **What would disprove this:** reading ch7:499's "connection that has survived being told the truth" as the intended cash-out of honest multiplicity; if that is the author's intent, the flag is a wording problem, not a structural one.

### [S5] Move 4 is used as a known thing 127 lines before it is taught
- **Location:** ch7:465 (body)
- **Evidence:** "Read that again against Section 4, because the Repairer is one of your five channels and **Move 4 is a structure for receiving rupture.**"
- **Reader problem:** Move 4 is defined at ch7:592, in Section 6. At ch7:465 Jordan is in Section 5 and has met no numbered moves at all. She is asked to hold a load-bearing inference — the reason the Victim is a catastrophe is that it disables Move 4 — against a referent she cannot check. The sentence also puts "Section 4" and "Move 4" eleven words apart with different referents, so the likeliest recovery she makes is the wrong one: that Move 4 is something in Section 4.
- **Category:** structure
- **Disposition:** fix locally — name the move rather than number it, or move the beat.
- **What would disprove this:** an earlier introduction of the numbered moves in ch7 that I missed; `grep -n "Move [0-9]"` finds none before ch7:465.

### [S6] The line designated to land viscerally is not in the chapter
- **Location:** ch7:497 (body) — nearest carrier; the phrase itself returns zero hits
- **Evidence:** ch7:497 — "it lets you know exactly what your presence costs and decline to bill for it."
- **Reader problem:** "the price of your presence" appears nowhere in ch7. The idea is everywhere — ch7:33 "she never told them what her presence cost", ch7:104 "what this field must hold for your staying to remain real", ch7:497 above — but it is never set as a standalone sentence Jordan could underline, quote, or carry out. Every instance is a subordinate clause inside a longer sentence, and the strongest one (ch7:33) is third-person parable about a woman in a village, not a sentence addressed to Jordan. A chapter with a designated visceral line and no quotable form of it hands its reader the argument and withholds the handle.
- **Category:** structure
- **Disposition:** structural decision — this is a placement question (which beat gets the naked sentence), not a rewording of any existing line.
- **What would disprove this:** a ruling that the chapter's carry-out line is meant to be ch7:703's "I can be told what I cost and stay in the conversation afterward" instead, which *is* set naked and bolded and does work as a handle.

### [S7] Section 4 answers "more things to do" with ten more things to do
- **Location:** ch7:301, 339, 377, 421, 431 (body); Section 6 throughout
- **Evidence:** ch7:377 — "**The structure of the Three-Part Repair:** You build a practice of repair that does not skip: (1) **Witness** … (2) **Impact** … (3) **Agreement** …"
- **Reader problem:** The documented drop-off risk for this chapter is that the five channels read as more things to do rather than relief. Counted: Section 4 hands Jordan **five named practice structures** (Interpreter's Discipline, Precedent of Presence, Three-Part Repair, Stake-Surfacing Close, Discernment Check), ten named alchemies, eleven Translate sub-moves and seven Control patterns; Section 6 then adds five moves, each with a prerequisite, a test and a working-versus-performed check. That is the risk realised in the table of contents, before a word of the prose is read. The chapter's relief argument — that naming a term is *less* work than absorbing cost indefinitely — is made well at ch7:399–401 and then buried under an inventory that models the opposite.
- **Category:** structure
- **Disposition:** structural decision — a triage line ("you need one of these; here is how to pick") would cost a paragraph, but which one is a doctrinal call. ch3:415 already routes this kind of load to an appendix with a triage rule, which is the precedent.
- **What would disprove this:** a reader test showing the deep-dives are read as reference material rather than as assignments. The chapter never tells Jordan she may skip them, which is what makes me read them as assignments.

---

## B. CONTINUITY AND CLAIMS

**Cross-reference sweep — every pointer in ch7 resolves. No ERRORs.** Checked and
clean: `Appendix F: The Polarity Map` (ch7:183 → `appendices/APPENDIX_F_POLARITY_MAP.md`
exists; the form matches ch4:202, ch5:245, ch6:202 exactly). `Chapter 3 (The
Shaman) has the full system` (ch7:190 ✓). `That is Chapter 4's game` (ch7:435 ✓
Challenger). `You met the Polarity Map at the School of the Body` (ch7:141 ✓ ch3).
`the fifth treatise` (ch7:176 ✓ — ch3 first … ch8 sixth, unbroken). `sixth in
line` (ch7:444 ✓ — ch2's roster is Protector, Controller, Skeptic, Fixer/Healer,
Emotional Body, Victim, Damaged Self; ch8:458 uses the identical roll-call and
also skips the Emotional Body, so ch7 is following the convention, not breaking
it). `fifth operation of six` (ch7:648 ✓). `the four seconds of Stand you learned
from the Challenger` (ch7:43 ✓ ch4:283, verbatim agreement including the "months"
contrast). `→ app` (ch7:479, 588, 684 ✓ — established ch1:249). **No surviving
gate walk, no four-stage sequence, no Reflection Prompts, no Vulnerable Child, no
Key Terms reference in ch7** — all five greps return zero. **Zero banned words.**

**Also checked and dismissed, so it is not rediscovered:** ch7:650–652's "the five
moves" meaning Wake Up/Open Up/Clean Up/Grow Up/Show Up while ch7:712 calls Name
the Field et al. "the five game moves" is a **book-wide** convention, identical in
ch3:826–828, ch4:680, ch5:535, ch6:488–492 and ch8:623–625. The bare
`### Move N: Title` heading form (no Wake Up binding) is likewise shared by ch5,
ch6, ch7 and ch8; only ch3 and ch4 bind. Neither is a ch7 finding.

### [C1] "Five channels" names two different things, and ch7 is the only chapter that redefines it
- **Location:** ch7:55, ch7:188, ch7:465, ch7:709 (body)
- **Evidence:** ch7:55 — "The Diplomat operates through five channels:" and ch7:709 — "The five channels: Bridge-Builder, Translator, Field-Holder, Repairer, Integrative Negotiator"
- **Reader problem:** *The five channels* is established book vocabulary for the EA channels — ch3:399 "Every feeling you experience falls into one of five channels", ch3:395 naming them Metal, Water, Wood, Fire, Earth, ch4:235 "the five EA channels", and an appendix titled *Appendix C: The Five Channels in Practice* that ch3:415 routes the reader to. Every other Face chapter keeps the two apart with the same sentence — ch4:245, ch6:253, ch8:280 all read "Five modes, five channels, no overlap", modes being the Face's own five. **ch7 alone calls its own five "channels", and then uses the original sense in the same chapter without warning**: ch7:429 "this is where **Refuse False Equivalence** lives inside the **Fire channel**", and the ch7:71 table's own column header calls the five "Mode". Jordan is asked to hold *channel* meaning two things within 380 lines, in the chapter where she is already carrying four separate five-item sets.
- **Category:** claim-error
- **Disposition:** structural decision — this is 30+ instances and a section title (ch7:188), and it interacts with the unapplied `Neutral Channel` ruling in `specs/PANEL_NEUTRAL_CHANNEL_2026-07-29.md`. Do not fix piecemeal.
- **What would disprove this:** a ruling on record that *channel* is deliberately polysemous at the Diplomat's altitude. Nothing in `specs/` says so, and ch4/ch6/ch8's shared sentence is evidence of the opposite intent.

### [C2] **FIXED 2026-08-01** ~~"The shortest in the book" is contradicted by the sentence in front of it~~ — the phrase does not appear anywhere in manuscript/.
- **Location:** ch7:674 (body)
- **Evidence:** "Five moves, one card, ninety seconds. **The Diplomat's version is the shortest in the book** and the one most likely to get interrupted by a balance."
- **Reader problem:** Four other chapters state the identical duration for the identical exercise: ch3:852 "about ninety seconds", ch4:704 "ninety seconds", ch6:514 "ninety seconds", ch8:647 "ninety seconds". Only ch5:559 differs, and it is explicitly *longer* ("give it the length of a walk rather than ninety seconds"). So ch7's version is tied with four chapters and shorter than one — it is not the shortest, and the number disproving the claim is nine words earlier in the same line. This is exactly the kind of small falsifiable boast that costs a sceptical reader her trust in the larger claims.
- **Category:** claim-error
- **Disposition:** fix locally.
- **What would disprove this:** ch9's five-move run being shorter and my having miscounted the field — ch9:622 is a sixty-second exercise but it is not the twenty-cards run, so it is not comparable.

### [C3] An unfilled note to the author is in shipped prose — print blocker
- **Location:** ch7:467–469 (body)
- **Evidence:** "[[TESTIMONY SLOT — WENDELL. This is where Ch5 puts Mr. Inadequate and Ch3 puts the harm passage. Needed: one time the ledger opened while somebody was telling you the truth about your impact, and what you said instead of hearing it. Not the lesson. The beat. ~150-200 words in your voice.]]"
- **Reader problem:** Two failures, and the second is worse than the first. **(1)** It is production scaffolding addressed to the author by name, in double brackets, in the middle of Section 5, and it will typeset. `grep "\[\[" manuscript/` returns this and nothing else — it is the only one in the book. **(2)** The hole it marks is real and load-bearing. Its own text names the two chapters that filled the equivalent slot, and both are filled: ch5:444 is Mr. Inadequate, in first person, and the ch3 harm passage is in place. So ch7 — the chapter running the myth architecture most thoroughly, and the chapter whose subject is *being told what you cost* — is the one chapter where the author does not go first and model being told what he cost. The self-deprecation Jordan needs to stay in the room is missing at the exact beat it was designed for.
- **Category:** claim-error (unfinished text)
- **Disposition:** structural decision — the marker is a five-second deletion; the 150–200 words it stands for cannot be written by anyone but Wendell, and deleting the marker without writing them silently converts a known hole into an unknown one.
- **What would disprove this:** the passage existing in `drafts/` and having failed to land. `drafts/appendix_channels.md` and the other listed drafts do not contain it.

### [C4] **FIXED 2026-08-01** ~~The EA table assigns Field-Holder a signal the chapter contradicts twice~~ — the Field-Holder's Alchemy 1 now reads Inclusion-Performance to Genuine Inclusion, matching the table's Wood/Joy row. The anxiety collision with the Bridge-Builder is gone, and the 'five modes, five channels, no overlap' sentence this finding measured against returns zero in ch4, ch6 and ch8 as well.
- **Location:** ch7:75 (body), against ch7:317 and ch7:319
- **Evidence:** ch7:75 — "| **Field-Holder** | Wood/Joy | Inclusion-performance → Genuine inclusion |" against ch7:317 — "**Alchemy 1 — Anxiety → Grounded Presence** … The Dissatisfaction here is **anxiety**."
- **Reader problem:** ch3 fixes anxiety to Metal/Fear and ch7:204 and ch7:220 both use it that way for the Bridge-Builder ("from Metal (fear/anxiety) to Wood (joy/interest)"). The table then labels Field-Holder Wood/Joy while Section 4 runs its primary alchemy on anxiety, which is Metal. The consequence is that ch7's table cannot make the claim ch4:245, ch6:253 and ch8:280 all make — "five modes, five channels, no overlap" — because Bridge-Builder and Field-Holder are running the same signal. ch7 is the only Face chapter that omits that sentence, which reads as the draft knowing the mapping did not close.
- **Category:** claim-error
- **Disposition:** structural decision — same edit as S1; the table and Section 4 disagree about Field-Holder's arc *and* its signal, and both come from the same divergence.
- **What would disprove this:** a doctrinal position that a mode's EA signal names its satisfied destination rather than its dissatisfied source, which would make Wood/Joy correct. ch4's table does not work that way (The Interrupt is Metal/Fear and its arc *ends* in Wonder), so the book's own precedent is against it.

---

## C. LINE-LEVEL CANDIDATES

All six **AWAIT STRUCTURAL RULING** — none should be touched before S1, S3, S7 and
C1 are decided, because three of them sit in passages those rulings may delete.

### [L1] Two sentences of the Field-Holder are printed twice, ten lines apart — AWAITS STRUCTURAL RULING
- **Location:** ch7:315 and ch7:325 (body)
- **Evidence:** ch7:315 — "They sit in the middle of chaos and perform peace, believing that their equanimity will regulate the field. This is collapse masquerading as calm." · ch7:325 — "The distorted Field-Holder sits in the middle of chaos and performs peace, believing that equanimity will regulate everyone else. This is collapse masquerading as calm."
- **Reader problem:** Near-verbatim duplication with one sentence identical in both. Jordan reads the second and cannot tell whether she lost her place, whether the repetition is deliberate emphasis, or whether the second instance is going to add something — so she re-reads the first, and the chapter has spent her attention on a printing accident.
- **Category:** line
- **Disposition:** fix locally
- **What would disprove this:** an intent to restate the distortion at the head of Alchemy 2. The gap is ten lines, which is too short for restatement to read as anything but an error.

### [L2] "You build a practice … that does not skip" is used twice as a formula — AWAITS STRUCTURAL RULING
- **Location:** ch7:377 and ch7:421 (body)
- **Evidence:** ch7:377 — "You build a practice of repair that does not skip: (1) **Witness:**…" · ch7:421 — "You build a practice that does not skip: (1) **Protect:**…"
- **Reader problem:** Two of the five named structures open with the same nine-word frame and the same numbered-triple shape, 44 lines apart. Read together they sound generated rather than authored, which is the specific texture that costs a reader her belief that a named practice was arrived at rather than filled in.
- **Category:** line
- **Disposition:** fix locally
- **What would disprove this:** the frame appearing as a deliberate refrain across all five structures — it does not; ch7:301, 339 and 431 each open differently.

### [L3] The Care/Impact failure states are restated with one word swapped — AWAITS STRUCTURAL RULING
- **Location:** ch7:151 and ch7:487 (body)
- **Evidence:** ch7:151 — "Care without impact is attendance: warm, **dependable**, and doing nothing." · ch7:487 — "Care without impact is attendance: warm, **reliable**, and doing nothing."
- **Reader problem:** ch7:485 announces the passage as a deliberate return ("You drew the Care ↔ Impact axis in Section 3"), so a quotation would be legitimate. The single swapped adjective is what breaks it: a quotation that is not quite a quotation reads as drift, not as callback, and the same paragraph re-states ch7:153's "fluent in one pole and suspicious of the other" too (ch7:487, "fluent in one of them and suspicious of the other").
- **Category:** line
- **Disposition:** fix locally — quote it exactly or recast it, but not both.
- **What would disprove this:** a house convention permitting inexact self-quotation. `specs/SPEC_REPETITION_AND_CUTS.md` governs this and should be checked before acting.

### [L4] Malformed possessive — AWAITS STRUCTURAL RULING
- **Location:** ch7:672 (body)
- **Evidence:** "stay there for one sentence' worth of time without answering"
- **Reader problem:** *one sentence' worth* is not a possessive form; it reads as a typo mid-instruction, at the one point in the passage where Jordan is being told exactly how long to hold still. A typesetting artifact inside a timing instruction undercuts the instruction.
- **Category:** line
- **Disposition:** fix locally
- **What would disprove this:** nothing; this is a straightforward error.

### [L5] "It is the altitude at which…" — the pronoun's nearest antecedent is the wrong one — AWAITS STRUCTURAL RULING
- **Location:** ch7:53 (body)
- **Evidence:** "Niceness, conflict-avoidance dressed in the language of harmony, and the absence of judgment in the service of false peace all get mistaken for it. It is the altitude at which a person can hold multiple valid perspectives simultaneously."
- **Reader problem:** The first *it* refers to the Diplomat's stance; the second *it* opens the next sentence and must refer to the same thing, but the nearest noun phrase is *false peace* and the whole preceding sentence is a list of things the stance is **not**. The correction beat that this passage exists to make lands on a pronoun the reader has to reverse-engineer, in the chapter's definitional paragraph.
- **Category:** line
- **Disposition:** fix locally
- **What would disprove this:** reading the pair as an intentional pivot, which would still require the reader to resolve *it* against a negated list.

### [L6] The reader's first meeting with the five stages runs a 60-word not/but sandwich — AWAITS STRUCTURAL RULING
- **Location:** ch7:43 (body)
- **Evidence:** "**Hold** is the maintenance of enough safety that difficult conversation remains possible even when the field is charged, not the four seconds of Stand you learned from the Challenger, where one person declines to take back one line, but the sustained containment of a whole field over the length of a hard conversation, sometimes over months."
- **Reader problem:** Four of the five stages get one clean sentence each; Hold gets a definition, then a cross-chapter negation with its own subordinate clause, then a *but* clause resuming the original definition. Jordan meets the chapter's spine here and has to hold "is X, not Y-with-a-relative-clause, but X-again" to get the third beat. The Challenger contrast is worth making and it is made a second time, cleanly and in its own place, at ch7:315.
- **Category:** line
- **Disposition:** fix locally — but see S2; if the stage sequence gets restructured, this line moves.
- **What would disprove this:** a decision that the Stand/Hold distinction must land at first mention rather than at ch7:315.
