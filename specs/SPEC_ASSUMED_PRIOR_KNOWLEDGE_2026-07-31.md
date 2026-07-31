# SPEC — Unearned recall: the book claims the reader already knows things

**Branch:** `claude/edit-assumed-prior-knowledge`. One editorial concern, per the
Lean OS git cadence and DL-18.

**2026-07-31.** The chapter pass found the same defect in eight of nine chapters
and reported it as fifteen separate flags. It is one habit, and naming it as one
is what makes it cheap to fix.

---

## 1 · The defect

**The prose reaches for the authority of having-already-taught before the
teaching has landed.** It runs at three scales:

| Scale | Example | Finding |
|---|---|---|
| **Word** | *"the auditor"* used as a known term 34 lines before it is defined (`ch4`) | chapter flags |
| **Move** | a do-it-now teaching Move 2, 130 lines before Move 2 (`ch6`) | chapter flags |
| **Book** | *"you already know all five"* — the WAVE-Spiral, asserted in ch3 after being promised in ch1 and missed in ch2 | **A6** |

**Why it is the highest-leverage item in the pass.** Jordan's documented drop-off
trigger is *jargon without translation*. Unearned recall is worse than jargon: it
tells her the failure to follow is hers. It is also the one defect that attacks
the book's central promise directly — *you do not have to learn everyone, you
learn one process* — because the process is the thing most often asserted rather
than delivered.

**What it is not.** Legitimate recall is the book working. *"In Chapter 1 you
wrote down the myth that runs you hardest"* (`ch2:560`) is earned, precise, and
does exactly what a spiral curriculum should. **The fix is never to strip
back-references.** It is to make each one true.

## 2 · The measured inventory

`instruments/assumed.py`, written for this pass. It attacks the defect from the
opposite side to `termdebt.py`: rather than asking *where is this term defined* —
a question whose detector has a known blind spot that already produced one
withdrawn finding — it finds **the assertion of prior knowledge itself**, which
is a small and reliable pattern.

```
python3 instruments/assumed.py          # 90 assertions, 9 chapters
python3 instruments/assumed.py -v       # with context
```

**90 candidate assertions.** Distribution:

| ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|
| 15 | 3 | 12 | 14 | 13 | 5 | 8 | 8 | 12 |

**Every hit is a candidate, not a finding.** The instrument cannot tell earned
recall from unearned recall — that is a human ruling, and most of the 90 will be
legitimate. What it can do is guarantee no site is missed, which nine readers
working chapter by chapter did not.

## 3 · Tier 1 — machine-verified, ruled, ready

One subclass is checkable without judgment: a claim about **what a named chapter
did**. Nine exist. Each was checked against the chapter it names.

| Site | Claim | Check | Verdict |
|---|---|---|---|
| `ch3:487` | "Chapter 1 taught you to read the meter" | *meter* in ch1 = **0** | **FALSE** |
| `ch4:325` | "Chapter 1 taught you to read the meter" | same | **FALSE** |
| `ch5:396` | "Chapter 1 taught you to read the meter" | same | **FALSE** |
| `ch2:276` | "Chapter 1 put the joystick in your hands" | *joystick* in ch1 = **0** | **FALSE** |
| `ch3:433` | "Chapter 1 put my own fluency on the table" | *fluency* in ch1 = 4 | true |
| `ch3:501` | "the fuel economy Chapter 1 handed to the Shaman" | token/fuel/tank in ch1 = 13 | true |
| `ch4:325` | "Chapter 3 taught you… the living field" | *living field* in ch3 = 1 | **thin — see below** |
| `ch5:396` | "Chapter 3 taught you… the living field" | same | **thin** |
| `ch9:682` | "Chapter 1 told you this would happen" | *autopilot* in ch1 = 1 | true (but see A2) |

**Two distinct fixes close four sites.**

**Fix 1 — the escalator ladder (`ch3:487`, `ch4:325`, `ch5:396`).** The same
sentence appears verbatim at three sites, building a cumulative ladder: ch3 adds
the living field, ch4 adds the fire question, ch5 adds the stewardship question.
The ladder is good structure built on a false first rung. Chapter 1 teaches this
idea thoroughly — the Token System, non-renewable and renewable tokens, the tank,
*"do you walk away with more fuel in the tank or less"* — and never once calls it
a meter. **The fix is one noun, applied three times.** Use ch1's own vocabulary.

Second rung, worth ruling at the same time: *living field* appears **once** in
ch3, and that once is inside the escalator sentence itself. So ch4 and ch5 credit
ch3 with teaching a concept ch3 named in passing, in the same construction. Either
seat the concept in ch3 or soften the two downstream claims.

Note the ladder also **stops after ch5** — ch6, ch7 and ch8 do not continue it.
That is the abandoned-convention pattern from the summary, and it is a separate
ruling: finish the ladder or let it end deliberately.

**Fix 2 — the joystick (`ch2:276`).** Chapter 1's control metaphor is *the
controls* (`ch1:16`, *"you take the seat"*, `ch1:62`, *"this is where you pick up
the controls"*). Chapter 2 introduces *joystick* — and uses it at `274` and `276`
before introducing it at `294`, so the chapter's own central metaphor is used
twice, mis-credited to ch1, then introduced as new. **Two fixes in one site:
correct the attribution, and move the introduction above first use.**

## 4 · Tier 2 — the confirmed sites from the chapter pass

Evidence-backed, each with a quotation in `editorial_reports/2026-07-31/`.
Adjudicated already; these are findings, not candidates.

| Site | The assertion | The gap |
|---|---|---|
| `ch3:824` | "you already know all five" (the WAVE-Spiral) | **A6** — promised in ch1 for ch2, delivered here |
| `ch1` | *BAR* used as known | 34 lines before its definition |
| `ch2` | "You already have the Shaman's first move" | 285 lines early |
| `ch3` | "the awareness trap" as a known term | 119 lines early |
| `ch4` | "the auditor" as a known term | 34 lines early |
| `ch6` | do-it-now teaching Move 2 | 130 lines before Move 2 |
| `ch7` | Move 4 used as known | 127 lines early |
| `ch8:191` | "This is the Vulnerable Child's gift" | term retired from the book |
| `ch9` | "the altar", twice, as recall | **defined nowhere in ch1–ch8** |

`ch9`'s is the worst of these and the cheapest to rule: a term the reader is told
she knows, which the book never contains.

## 5 · Tier 3 — the remaining ~77, and how to rule them

Not yet adjudicated. The protocol, cheapest test first:

1. **Name the object.** What exactly is the reader said to know? If the sentence
   cannot be resolved to a specific term, move or moment, that is itself the
   finding.
2. **Find its teaching.** First substantive teaching, by `ch:line`. Not first
   *use* — first *teaching*.
3. **Compare.** Teaching before the assertion → **earned, leave alone.** After,
   or absent → **unearned.**
4. **Rule the repair, in this order of preference:**
   - **Cut the claim, keep the sentence.** *"You already know X, because it is Y"*
     → *"X is Y."* Costs nothing, loses nothing, and is right most of the time.
   - **Move the teaching earlier**, where it is short and the chapter allows.
   - **Move the assertion later.**
   - **Seat the teaching**, only where the object is absent from the book and load-
     bearing — `ch9`'s altar is the candidate.
5. **Never** repair by deleting a legitimate back-reference. Earned recall is the
   spiral curriculum doing its job.

**Stop rule.** When the remaining candidates are all earned recall, the pass is
done. Expect that to be most of the 77.

## 6 · Sequencing, and why no prose moves yet

**`claude/mtgoa-manuscript-changes-swmp78` is live.** It committed at 19:34,
after this session merged to master, and holds unmerged work in ch7, ch8 and ch9.
Every chapter in Tier 1 and Tier 2 is inside its working set.

DL-18 governs: *land apparatus and prose on separate branches, or sequence the
sessions.* So this branch carries **the instrument, the inventory and the plan**,
and no chapter edit, until that branch lands. All of section 3 and 4 is
diagnosis; none of it is blocked by waiting, and none of it will need redoing,
because every site here is anchored to **quoted text rather than a line number** —
the numbers drift with every commit that session makes.

**When the chapters are free, the order is:**

1. Fix 1, the escalator — one noun, three sites, mechanical, no judgment needed.
2. Fix 2, the joystick — attribution plus an introduction moved above first use.
3. A6's three edits — the spine, and the flagship instance of this defect.
4. `ch9`'s altar and the Tier 2 term sites.
5. Tier 3 adjudication, working down from the chapters with the most candidates
   (ch1 15, ch4 14, ch5 13).

Each through `instruments/spec_edit.py`, each gated, each one commit answering
one editorial question.

## 7 · Rulings needed — with options

Drafted 2026-07-31. Each option is written out so the choice is between
sentences rather than between abstractions. None is applied; all await Wendell.

### R1 · The meter becomes what?

`ch1:125` is the moment the escalator is pointing at: *"After you engage it, do
you walk away with more fuel in the tank or less? That answer is your real
score."* Chapter 1's nouns are **the Token System** (2), **the tank** (2),
**renewable / non-renewable tokens** (2), **your real score** (1).

| | Option | Cost |
|---|---|---|
| **A** | *"Chapter 1 taught you to read the tank: what a move costs you."* | 3 sites, one noun. Keeps the gauge image the ladder wants — a tank has a level you read |
| **B** | *"Chapter 1 taught you to read your own fuel: what a move costs you."* | 3 sites. Warmer, slightly less precise |
| **C** | *"Chapter 1 taught you what a move costs you."* — cut the metaphor | 3 sites. Zero risk, loses the *read the X* parallel the ladder is built on |
| **D** | **Reverse it — put *meter* into ch1** at `ch1:125`, so all three downstream claims become true | **1 site.** Cheapest by count, but it invents ch1 vocabulary to satisfy ch3–ch5, which is the tail wagging the dog |

**Recommend A.** *The tank* is already ch1's word, it survives three repetitions,
and *read the tank* keeps the ladder's parallel intact. D is tempting on cost and
worth considering only if the word *meter* is one you actively want.

### R2 · The living field

`ch3` names it **once**, inside the escalator sentence itself, though the chapter
teaches field-reading throughout — it is the Shaman's whole job.

| | Option | Cost |
|---|---|---|
| **A** | Seat the phrase once in ch3's teaching, before the escalator | 1 insertion in ch3. Makes both downstream claims true |
| **B** | Soften ch4 and ch5 to describe rather than cite: *"Chapter 3 taught you to ask what a move does to the people around it"* | 2 sites, no new prose |
| **C** | Leave it. The claim is technically true | 0 |

**Recommend A.** The concept is taught in full; only the label is thin, and one
sentence in ch3 converts a thin claim into an earned one for two later chapters.

### R3 · The ladder stops after ch5

ch6, ch7 and ch8 do not continue it. Each has a natural rung already written into
its own material — the design question, the price question, the game question.

| | Option | Cost |
|---|---|---|
| **A** | Finish it: three more escalator sentences at ch6, ch7, ch8 | 3 insertions, ~40 words each. Turns an abandoned device into the book's cumulative spine, and strengthens ch9's payoff |
| **B** | End it deliberately at ch5 with one closing beat, so it reads as complete | 1 insertion |
| **C** | Cut it from ch3, ch4, ch5 | 3 deletions. Loses a good device |

**Recommend A**, if any prose work happens after ship. The ladder is the spiral
curriculum working, and it is the single clearest answer to the unearned-recall
defect: recall that is built rung by rung cannot be unearned.

### R4 · The altar

Two uses, both in ch9, and the first glosses itself:

> `ch9:83` — "The six Faces are your toolkit. The WAVE is your process. **The
> altar — the practice of returning — is your anchor.**"
> `ch9:286` — "**You know that the altar is not optional** — that coming back
> makes the work real."

The problem is not the gloss. It is that `ch9:83` gives the altar **equal billing
with the Faces and the WAVE** — three pillars, two of which the book spent nine
chapters teaching — and `ch9:286` then asserts recall. ch8 teaches the concept
thoroughly as the **Returner** (`ch8:307`, `ch8:368`); it never calls it an altar.

| | Option | Cost |
|---|---|---|
| **A** | Cut the name, keep the concept: *"The practice of returning is your anchor"* / *"You know that the return is not optional"* | 2 sites, no new prose. Zero loss — the gloss already carries the meaning |
| **B** | Seat the name in ch8 beside the Returner, so both ch9 uses become earned | 1 insertion in ch8 + 2 sites left alone. Keeps a good image and earns the third pillar |
| **C** | Keep `ch9:83`'s gloss, soften only `ch9:286` | 1 site. Leaves the equal-billing problem |

**Recommend B if the altar is an image you want**, A if it is not. This is the
one ruling where the cheap fix and the good fix differ, because a third pillar
named at the close is worth having — provided the book taught it.

## 8 · Rulings needed

1. **The meter → what noun?** Chapter 1's own vocabulary is *the Token System*,
   *tokens*, *the tank*, *fuel*. Wendell's call which one the escalator should
   use, since it has to survive three repetitions and a cumulative ladder.
2. **The living field** — seat it properly in ch3, or soften ch4 and ch5.
3. **The ladder stops after ch5** — finish it through ch6–ch8, or end it
   deliberately at ch5.
4. **The altar** (`ch9`) — define it, or cut both uses.

---

## 9 · RULED by Wendell, 2026-07-31 — R1 B · R2 A · R3 A · R4 A

Drafts written, gated, and **awaiting approval before any chapter is touched**.
Prose lives in the console and the session scratchpad only, per AGENTS.md.

**Review pass run, per `.claude/skills/mtgoa-review`:** gate clean; diet
**be 0.25 · copula 0.53 · waste 0.45 · zombie 1.02 · expletive 0.00 · passive
0.00** — every counter under the 1.30 line. `/no-ai-slop` detect mode found four
real defects in draft 1, all fixed in draft 3: a person shift into first person
in the ch7 and ch8 questions, a two-referent pronoun stack in the ch8 question, a
mixed metaphor (*"the people standing inside the move"*), and a passive tail.

**One trade recorded, because it nearly shipped.** Draft 2 compressed the refrain
to avoid six verbatim repetitions and drove **zombie to 1.94** by adding five
*"the X question"* pairs. Repetition was traded for nominalization, which is the
worse defect and the one the reader cannot see. Draft 3 restores the full refrain
— which is ch4 and ch5's existing pattern regardless, so compressing it was a
voice change I had no ruling for.

### R3 is larger than it was priced

**ch6, ch7 and ch8 have no Ecology section at all.** Only ch3, ch4 and ch5 carry
one. So R3-A is three *new sections*, not three sentences — roughly 90 words each
including heading. Proposed placement, mirroring where ch4 and ch5 put theirs
(immediately after the stage sequence):

| Chapter | New heading | Seat between |
|---|---|---|
| ch6 | `### The Design Ecology` | after the flow cycle at `ch6:301`, before `Name One Unstated Assumption` at `ch6:309` |
| ch7 | `### The Presence Ecology` | after Channel 5 at `ch7:419`, before `The Ledger That Became a Standing` at `ch7:476` |
| ch8 | `### The Sight Ecology` | after the stage sequence at `ch8:436`, before `The Walk Back` at `ch8:460` |

ch8's slot mirrors ch4 and ch5 exactly. ch6 and ch7 diverge structurally and
their slots are a judgment call.

### Still open

The refrain reaches **six sites** under R3-A. It works as a mnemonic at two and
risks reading as boilerplate by the fifth. Draft 3 keeps it verbatim because that
is the established pattern; whether it survives six repetitions is Wendell's call
and the only piece of this set that is not settled.

### FINAL — approved 2026-07-31

Wendell: *"the X question — as a format is hitting as clunky."* The label is cut
at all five sites. **The measurement agreed with his ear**: *the fire question*,
*the design question* and their siblings are article-plus-nominalization, and
removing them moved the draft from **zombie 1.02 / be 0.25 / copula 0.53** to
**zombie 0.37 / be 0.00 / copula 0.00**. The clunky formula was the largest
measurable defect in the draft.

Recorded because it changes scope: *"the fire question"* (`ch4`) and *"the
stewardship question"* (`ch5`) are **shipped prose**, from commit `db3f534` — not
drafts. Cutting the label edits two existing sites as well as declining the
format at three new ones. Wendell approved that wider scope.

Also recorded: the label was not baseless. Fire is a canonical channel
(`ch3:444` — Fire · Anger · *the clarity of your limits*) and ch4 is titled *How
to Wield the Fire*. The label was grounded and still wrong, because it required a
decode for something the question underneath it already said in concrete words.
The two labels were also different kinds — *fire* elemental, *stewardship*
topical — which is likely what made the pattern read as a formula.

**Approved set, ready to apply:** `drafts/APPROVED_unearned_recall_2026-07-31.md`.
Every anchor verified unique; `spec_edit.py` would abort on any that were not.

---

## 10 · A6 re-measured, 2026-07-31 20:05 — site 1 moved rather than closed

**Site 1 was edited today by another session** (`069bcbd`, *"Seat the
Headmaster's Letter, and keep ch1's loop promise"*). The promise was preserved
and re-pointed:

> **was** — "the process that runs every one of these faces: **the loop you meet
> in the next chapter.**"
> **now** — "the process that runs every one of these faces: **the loop, which
> the Headmaster sets out in the letter standing at the door of the six
> schools.**"

**The letter does not set out the loop.** Measured: the five WAVE stage names
appear **0 times** in `front_matter/headmasters_letter.md` and **18 times** in
`manuscript/ch3.md`. *Loop* and *WAVE* also read 0 in the letter.

Read in full and judged fairly, the letter is strong prose and it does set out a
sequence — the shape of a term (*arrive carrying something · say what you are
taking on · be taught one move · make it outside, on a person, by a date · come
back and report*). That is a **pedagogy**, not the emotional-alchemy loop the
Face chapters run. ch1's own sentence settles which one it means: *"the process
that runs every one of these faces"* and *"the loop is how you play it."*

**So the defect relocated rather than closing**, and it is arguably tighter now:
the previous target (ch2) at least contained five moves, wrong ones. The letter
contains none.

**Two readings, and they need different fixes.** Either *the loop* still means
the WAVE — in which case ch1 points at the wrong document — or the term-shape has
been promoted to *the loop*, in which case **the book now has two loops** and ch3
defines the other one.

**Not drafted, deliberately.** That session is live (9 commits ahead, last at
20:03) and this is their active work. Drafting a competing fix is the 91-hunk
mistake in miniature. Sites 2 and 3 are untouched and unaffected by their work,
and remain as specified.
