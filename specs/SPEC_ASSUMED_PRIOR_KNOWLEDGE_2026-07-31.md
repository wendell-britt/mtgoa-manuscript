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

## 7 · Rulings needed

1. **The meter → what noun?** Chapter 1's own vocabulary is *the Token System*,
   *tokens*, *the tank*, *fuel*. Wendell's call which one the escalator should
   use, since it has to survive three repetitions and a cumulative ladder.
2. **The living field** — seat it properly in ch3, or soften ch4 and ch5.
3. **The ladder stops after ch5** — finish it through ch6–ch8, or end it
   deliberately at ch5.
4. **The altar** (`ch9`) — define it, or cut both uses.
