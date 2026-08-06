# SPEC — The inchoative copula, and the two holes it came out of

**Found by Wendell 2026-08-02**, reading a ch2 replacement paragraph that had just passed
`gate` clean and scored `copula 0.46`:

> *"What does 'go careful' mean? In which way are we now using the go, went construction as
> a way to be passive in a way that seems active?"*

Both halves of that question are findings. The first is a banned word routed around. The
second is a counter the book has never had.

DL-34, DL-35, DL-36 in `specs/DECISION_LOG.md`.

---

## 1 · What the construction is

`go / goes / going / went / gone` + adjective is **inchoative**: it means *become*.
`goes cold` unpacks to `is cold now`. There is no motion and no object, so it wears the
shape of an intransitive action verb and the eye reads it as something happening.

Nothing happens. A state gets reported. And when the subject is inanimate, nobody caused
the state — which makes it the same defect as *the hum arrives* and *it shows up*, in a
costume that reads as active. That is why it survived an agency audit of the same
paragraph six hours earlier: I classified `ch2:11` and `ch2:13` as bare-`It` subjects and
relative clauses and did not see the third thing they share.

**Legal with a subject that can act.** `ch2:358` — *"A charge rises that you can't name,
and you go cold"* — is a person's body freezing, and the involuntariness is the whole
point of the sentence. The defect is an inanimate subject: a meeting does not go anywhere.

## 2 · Why no counter could see it

`BE` and `COPULA` match `is|are|was|were|be|been|being` and nothing else. Measured on two
files of otherwise identical sentences:

```
                                                     be     copula
"The meeting goes cold. The table goes careful."   0.00       0.00
"The meeting is cold.  The table is careful."      4.97       3.44
```

**So driving `copula` down actively rewards moving copulas into `go`.**

This is the third counter added to `prose_diet.py` because tightening an earlier one
pushed the defect somewhere nothing was looking — `waste` → `empty` on 2026-07-31, and now
`copula` → `inchoative`. **Assume there is a fourth.** The pattern is worth naming: a
counter creates a gradient, and prose flows down it into whatever is unmeasured.

## 3 · The measurement

Baseline **measured, not typed**, per this file's own standing lesson: **0.30 defect sites
per thousand words**, 31 sites in 101,821 words.

| ch | per 1k | ratio | ch | per 1k | ratio |
|---|---|---|---|---|---|
| **ch2** | **1.07** | **3.56** | ch6 | 0.28 | 0.95 |
| ch1 | 0.40 | 1.34 | ch5 | 0.10 | 0.34 |
| ch3 | 0.38 | 1.25 | ch7 | 0.08 | 0.25 |
| ch4 | 0.35 | 1.16 | ch9 | 0.08 | 0.27 |
| ch8 | 0.29 | 0.98 | | | |

**Ch2 runs 3.5x the book and 13x ch9.** The chapter the defect was found in is the chapter
that has it worst, which is the same result the agency audit reached by hand.

It is a **low-frequency** counter — a tenth the rate of `passive`, the next sparsest — so
the ratio is noise on anything short and **the `-v` site list is the output.** Two hits in
a 300-word draft reads as 22x and means nothing.

## 4 · The scan — 34 sites, every one of them

```
python3 instruments/prose_diet.py -v | sed -n '/--- inchoative/,$p'
```

`DEFECT` = the subject cannot act. `ok` = a person or a personified Face, which is legal.
`LAUNDER` = a banned word's synonym sitting in the slot.

### Read first — the six LAUNDER and near-LAUNDER sites

| site | text | note |
|---|---|---|
| `ch8:81` | *the way a table **goes still** when someone says a thing* | DEFECT + LAUNDER. **The same metonym and the same evasion as the sentence that started this.** Wendell's line, and it wants his ruling before mine gets fixed |
| `ch9:632` | *The person **goes still**, says nothing* | ok + LAUNDER. Human subject, so legal by the counter; still the construction |
| `ch7:551` | *Something in you **goes still** and attentive* | ok + LAUNDER. Classifier read the subject as *you*; the true head is *something in you*, a part of a person. Legal, recorded |

### The ch2 cluster — 8 sites in one chapter

| site | text |
|---|---|
| `ch2:11` | *the meeting that **goes sideways*** — one of the original agency-audit sites |
| `ch2:13` | *A conversation that **goes wrong*** — likewise |
| `ch2:15` | *a conversation that's **going fine** on the surface* |
| `ch2:122` | *the 2am inventory of what **went wrong*** |
| `ch2:132` | *Picture a meeting that **goes cold*** — the Section 3 site already flagged as a follow-on |
| `ch2:132` | *the literacy gets built and the read **goes unused*** — same sentence pair, second hit |
| `ch2:181` | *for reasons that started early and **went deep*** — spatial metaphor, probably fine |
| `ch2:446` | *when a meeting has **gone cold** before anyone speaks* |
| `ch2:358` | *and you **go cold*** — **ok**, the Emotional Body freezing |

### The rest of the book

| site | text |
|---|---|
| `ch1:87` | *The scoreboard **went dark*** |
| `ch1:159` | *a hire is about to **go sideways*** |
| `ch1:167` | *an arcade whose owner is exhausted and **going under*** — genuinely ambiguous whether the arcade or the owner is going under, which is why it is a reader's call |
| `ch3:134` | *Fear of things **going wrong*** |
| `ch3:134` | *if something in the allyship **went sideways*** |
| `ch3:264` | *because something has **gone unfelt*** |
| `ch3:320` | *stand inside it without **going under*** |
| `ch3:750` | *The fire **went silent*** |
| `ch3:926` | *stops being interior and **goes external*** |
| `ch4:278` | *Compliance **gone numb** → Peace* — inside an EA table |
| `ch4:289` | *Earth **gone flat*** |
| `ch4:352` | *The fire **goes sideways*** |
| `ch4:546` | *where the crossing **went unremarked*** |
| `ch5:658` | *forty minutes on what **went wrong** in 2019* |
| `ch6:291` | *detects what could **go wrong*** |
| `ch6:370` | *know something has **gone wrong** under the third floor* |
| `ch6:391` | *When something **goes wrong**, which arrives first* |
| `ch7:645` | *nobody has explained what happens if it **goes wrong*** |
| `ch8:131` | *Distortion is the gift **turned sideways*** |
| `ch8:174` | *the people who have metabolized their pain **go unheard*** |
| `ch8:270` | *the violation sitting in the middle of the table **goes unnamed*** |
| `ch9:556` | *A gathering **falls flat*** |

**Nothing in this table has been edited.** The counter is a finder; the sites are Wendell's
to rule. `what went wrong` and `something goes wrong` are ordinary English and may all be
fine; `the meeting goes cold` and `a table goes still` are the ones worth reading twice.

## 5 · The other hole, which is not mechanisable

The sentence wanted **"the whole table goes quiet."** `quiet` is banned by `gate.py`.
`careful` went in instead — a word that does not collocate with *go*, and therefore carries
no fixed meaning — and the gate passed clean.

That is routing around a banned word instead of rebuilding the sentence, which is the thing
the ban exists to force. The gate can see the word; it cannot see that the word was replaced
with a hole. **If a banned word is the word the sentence wants, the sentence is wrong, not
the word** — the fix was to name what the people actually did (*everybody at the table
starts picking their words*), which is a different sentence, not a different adjective.

`INCH_LAUNDER` flags the six *quiet*-family synonyms in the one construction that hides
them. It is the nearest approximation available and it is not a solution; the rule now
lives in the skill, where a reader will meet it.

## 6 · Two more findings this work turned up

**`review.py`'s book-wide diet step could not fail.** `prose_diet.py` exits 0 whatever it
finds, so the generic loop marked the step `ok` and printed only the last line of the
`heavy:` block as if it were the summary. **`ch7 passive 1.44` had been on the page and
unreported since the counter landed on 2026-07-31.** The same failure the file's own
comment describes forty lines above, in the other half of the same file: `draft()` was
taught to parse the block and `book()` never was. Fixed; DL-35.

**The slop pass was being run on half of itself.** `/no-ai-slop` carries a pattern list and
an `eval.md` checklist. Auditing against the patterns finds bad sentences and cannot find
invented ones, which is how *"Six of you built the group to hold exactly this"* reached
Wendell reported clean. `eval.md` check 1 is the one that catches it. Fixed in the skill;
DL-36.

## 7 · Verification

```
python3 instruments/prose_diet.py             # 8 columns, inchoative last
python3 instruments/prose_diet.py -v          # 34 sites with subject and line number
python3 instruments/review.py                 # 2 diet LOOK 3 heavy — was "ok" and one line
python3 instruments/test_toolchain.py         # all cases pass
python3 instruments/gate.py                   # GATE PASS, four surfaces
python3 marginalia/compile.py --verify        # byte-identical
```

**No manuscript file is touched by this work.** `prose_diet.py`, `review.py`, the skill,
this spec and the decision log — apparatus only.
