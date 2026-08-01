# APPROVED — the unearned-recall fix, ready to apply

**Ruled by Wendell 2026-07-31: R1 B · R2 A · R3 A · R4 A**, plus the label cut
approved after he called *"the X question"* clunky. Spec:
`specs/SPEC_ASSUMED_PRIOR_KNOWLEDGE_2026-07-31.md`.

**Not yet applied.** `claude/mtgoa-manuscript-changes-swmp78` still holds
unmerged chapter work (DL-18). Everything below is anchored on **quoted text
rather than line numbers**, so it survives whatever drift that branch lands.

**Review pass, final draft:** gate clean · **be 0.00 · copula 0.00 · waste 0.54 ·
zombie 0.37 · expletive 0.00 · passive 0.00**. Every counter under the 1.30 line,
and better than every earlier draft on all six.

---

## 1 · Three replacements — exact anchors

### ch3 — R1 (fuel) + R2 (living field defined at first use)

**OLD**
```
Chapter 1 taught you to read the meter: what a move costs you. The Shaman adds the next layer: what that spending does to the living field.
```
**NEW**
```
Chapter 1 taught you to read your own fuel: what a move costs you. The Shaman adds the next layer: what that spending does to the living field — to the people around you, and what it leaves them carrying.
```

### ch4 — R1 (fuel) + label cut

**OLD**
```
Chapter 1 taught you to read the meter: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Challenger adds the fire question:
```
**NEW**
```
Chapter 1 taught you to read your own fuel: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Challenger adds:
```

### ch5 — R1 (fuel) + label cut

**OLD**
```
Chapter 1 taught you to read the meter: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Regent adds the stewardship question:
```
**NEW**
```
Chapter 1 taught you to read your own fuel: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Regent adds:
```

## 2 · Two replacements in ch9 — R4, the altar cut

### ch9 — the three pillars

**OLD**
```
The six Faces are your toolkit. The WAVE is your process. The altar — the practice of returning — is your anchor.
```
**NEW**
```
The six Faces are your toolkit. The WAVE is your process. The practice of returning is your anchor.
```

### ch9 — the asserted recall

**OLD**
```
You know that the altar is not optional — that coming back makes the work real. That the return to the village, carrying what you found, is the whole point.
```
**NEW**
```
You know that the return is not optional — that coming back makes the work real. That carrying what you found back to the village is the whole point.
```

## 3 · Three new sections — R3

Seated to mirror ch4 and ch5, which put the Ecology immediately after the stage
sequence. ch6 and ch7 diverge structurally, so those two placements are a
judgment call and should be eyeballed on application.

### ch6 · insert AFTER this line

> `The Architect's flow cycle: Observe → Model → Design → Deploy → Observe (new state), and out through Hand Off.`

```markdown
### The Design Ecology

Chapter 1 taught you to read your own fuel: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Architect adds:

Did this change the condition, or did it clear the incident?

The Architect does not need you to count what you shipped. The Architect needs you to tell the truth about whether the next person walks into the same wall.
```

### ch7 · insert BEFORE the section that follows Channel 5

Anchor: the heading after `### Channel 5 — Integrative Negotiator` completes —
`### *The Ledger That Became a Standing*`.

```markdown
### The Presence Ecology

Chapter 1 taught you to read your own fuel: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Diplomat adds:

Did staying cost something you agreed to spend, or something you never named?

The Diplomat does not need you to tally what you gave. The Diplomat needs you to tell the truth about whether you set the price or somebody set it for you.
```

### ch8 · insert BEFORE this heading

> `### *The Walk Back: Coming Down Without Losing What You Found*`

```markdown
### The Sight Ecology

Chapter 1 taught you to read your own fuel: what a move costs you. Chapter 3 taught you to ask what a move does to the living field. The Sage adds:

Did the whole view send you back down into the game, or did it hand you somewhere to stand outside it?

The Sage does not need you to rank the games. The Sage needs you to tell the truth about whether seeing more made you easier to reach or harder.
```

## 4 · Fix 2 — the joystick, ruled 2026-07-31

**Wendell's call, and it is the better one.** The original plan patched `ch2` in
two places. He ruled the opposite direction: change ch1 to say *joystick*, which
makes `ch2:276`'s claim true without editing ch2 at all.

The asymmetry that justifies it: **`the controls` appears nowhere but ch1** — a
one-chapter synonym — while **`joystick` appears 32 times across ch2–ch8** and
carries the whole daemon system. The synonym had seniority only by page order.

It also introduces the term better than any gloss would have: joystick now first
appears in a sentence that hands it to the reader.

### ch1 — replacement 1

**OLD**
```
This is where you pick up the controls.
```
**NEW**
```
This is where you pick up the joystick.
```

### ch1 — replacement 2

**OLD**
```
You just put your hands on the controls.
```
**NEW**
```
You just put your hands on the joystick.
```

**Ruled kept, not changed:** ch1's second control image — *"you take the seat"*
(`ch1:16`) and the Reader's Oath *"I take the seat, and from here every move is
chosen"* (`ch1:221`). Different picture, no collision: you sit down at the
machine, then you pick up the joystick. The Oath is ceremonial language written
to be said aloud and is not touched.

**Measurement note.** The two edited sentences score `be 1.24 · copula 1.72 ·
waste 1.11` — **identical before and after**, because the copula belongs to the
existing sentence and only the final noun changes. On a 14-word sample the
ratios are noise, which is what `.claude/skills/mtgoa-review` warns about below
~300 words. Recorded so nobody re-opens it as a heavy-prose finding.

## 5 · A6 — the spine. Ruled 2026-07-31, and it is ONE edit, not three

**The finding was right and its scope was wrong.** A6 was logged as three edits.
Measured against current master, two of the three are not defects at all — both
were artifacts of the ch1 mis-pointer:

- **ch2 never claims to be the loop.** It says *"Here's an opening game, five
  moves you can run the next time a daemon grabs the joystick."* That is accurate
  labelling. The defect was ch1 pointing at it.
- **ch3's recall is earned.** The WAVE-Spiral is defined at `ch3:278`; *"you
  already know all five"* sits at `ch3:860` — **582 lines later in the same
  chapter.** She was taught them.

### The real defect: *the loop* is not this book's name for anything

Every use of *loop* in the manuscript, measured:

| Site | Refers to |
|---|---|
| `ch2:172` | a rumination loop — a pathology |
| `ch6:269`, `271` | the Architect's four-stage loop |
| `ch8:438`, `446` | the five modes as a commitment loop |
| `ch9:103`, `196`, `604` | the five modes looping |

**None is the WAVE**, and `ch9:103` rules against it directly: *"They don't run in
sequence the way the WAVE's stages do — they loop."* Calling the WAVE *the loop*
in ch1 contradicts ch9.

What actually runs every Face chapter is the **WAVE** — 10 to 18 stage-name uses
in each of ch3–ch8, no exceptions.

So the referent was never missing. **The name was never adopted.** Pointing the
sentence at ch2 was wrong; re-pointing it at the Headmaster's Letter in `069bcbd`
was wrong the same way. Both moved a pointer instead of correcting a noun.

**Priority, per the Lean OS ladder:** question 1 — *does this threaten the book's
central promise?* Yes. The promise is *you learn one process*, and this is that
sentence at first mention. First yes beats everything below it.

### ch1 — replacement

**OLD**
```
You already have the process that runs every one of these faces: the loop, which the Headmaster sets out in the letter standing at the door of the six schools.
```
**NEW**
```
One process runs every one of these faces: the WAVE, which the Shaman hands you in Chapter 3 and every school after that one uses.
```

The rest of the paragraph needs *the loop* → *the WAVE* in its second sentence:

**OLD**
```
Each Game Master takes a chapter to teach you their game, and the loop is how you play it.
```
**NEW**
```
Each Game Master takes a chapter to teach you their game, and the WAVE is how you play it.
```

Three things in one edit: names the spine with the book's own word, points at
where it is taught, and drops *"You already have"* — itself unearned recall, in
the sentence this branch exists to fix.

**`069bcbd` stands.** The Headmaster's Letter is good and belongs at the door.
It simply is not where the WAVE lives, so only the claim about it changes.

Gate clean · be 0.31 · copula 0.00 · waste 0.55 · zombie 1.03 · expletive 0.00 ·
passive 0.00.

## 6 · Narrated reader-history — 2 sites, both ch5

**Tier 3 yield, and the number matters.** `assumed.py`'s history rules flag 18
sites. Read individually, **14 are legitimate or false positives** — ch1's *"You
have been running your own allyship campaign for years — whether you named it or
not"* is the book's stated premise and hedges itself; `ch4:492` sits inside a
quoted script the reader might say; `ch9:660` is Wendell about himself;
`ch7:622` is already conditional. Two more are borderline and left alone
(`ch4:134`, `ch8:612`).

**Two are real, and both are in ch5.** Converting them measured *better*, not
merely safer: **be 0.62 → 0.34, waste 1.67 → 0.90**, gate clean, history hits
2 → 0.

The fix pattern is the book's own, from `ch2:401`: state the mechanism generally
or conditionally, and let the reader recognise herself in it. Never assert the
biography.

### ch5 — replacement 1

**OLD**
```
You already have a version of what "tradition" means. You've been carrying it since the last time someone used it against you.
```
**NEW**
```
You already have a version of what "tradition" means. Most people got theirs the last time somebody used the word against them.
```

### ch5 — replacement 2

**OLD**
```
You grew up in a family with a specific pattern — around money, around conflict, around who speaks and who stays silent. You inherited it. You have been living it, either repeating it or raging against it, for your entire adult life.
```
**NEW**
```
Every family runs a pattern — around money, around conflict, around who speaks and who stays silent. Whatever yours was, you inherited it, and most of adult life goes into either repeating it or raging against it.
```

**Why this class matters beyond two sentences.** Canon bans narrating the
reader's unnamed history as fact, and `gate.py`'s A0 rule matches four fixed
phrases — it caught neither of these. The rule was effectively unenforced.
`assumed.py` now enforces it.

## 7 · P0 placeholders — ruled 2026-07-31

Two of three closed. The third is deferred by Wendell and **remains a print
blocker**.

### ch7 — cut the testimony slot

**Ruled: cut.** The slot asked for 150–200 words of Wendell's own memory. Writing
it was not available — inventing a personal memory and attributing it to the
author is fabrication, not drafting.

**Cost, recorded honestly:** ch7 carries **6** first-person beats against ch3's
**17**, so it was already the thinnest chapter for testimony, and Wendell's
register is testimony-before-instruction. Cutting makes it thinner. The seam
still works — diagnosis runs straight into the instruction.

**OLD** — remove this block *and the blank line beneath it*:
```
[[TESTIMONY SLOT — WENDELL. This is where Ch5 puts Mr. Inadequate and Ch3 puts the harm passage.
Needed: one time the ledger opened while somebody was telling you the truth about your impact,
and what you said instead of hearing it. Not the lesson. The beat. ~150-200 words in your voice.]]
```
**NEW** — nothing.

**Care needed on the newlines.** Removing the block plus the blank line *above*
it merges two paragraphs. The correct cut is the block plus the blank line
*below* it. Verified: the seam keeps its paragraph break.

Resulting seam:
> …The Face whose whole chapter is about repair is, in shadow, structurally the
> worst in the book at receiving it.
>
> You do not fire the Victim. Fire the part of you that counts and you will spend
> the rest of your life absorbing costs you cannot name…

### ch1 — cut the visual marker

The sentence already names all six Faces with a gloss each, so the marker was
redundant with prose doing the job.

**OLD**
```
 *[visual: the six Game Masters]*
```
**NEW** — nothing. (Note the leading space, so the sentence ends on its full stop.)

Gate clean. The `passive` counter reads heavy on this line **before and after**
(2.96 → 3.10) — it belongs to the existing sentence, and the ratio moved only
because the sample lost five words.

### ch1 — the app CTA: DEFERRED, still blocking

**`**[ URL / QR ]**` stays in the manuscript.** Wendell is still setting the
links up. This is not closed and must not be read as closed:

> `ch1:269` — "Activate it, and find the hundred-and-twenty-card deck for when
> you want the moves in your hands, at **[ URL / QR ]**."

It is the book's only call to action, for an app referenced six times and never
named, and two of ch1's four practices route through it.
`instruments/placeholders.py` will keep reporting **1 hit and exiting non-zero**
until the URL lands. That is the intended behaviour — do not allowlist it.

---

## What this closes

| | |
|---|---|
| **4 of 9** machine-verified false back-references — every *"Chapter 1 taught you to read the meter"* site plus the ch3 living-field gloss that made two downstream claims true | R1, R2 |
| The abandoned escalator ladder, now running ch3 → ch8 | R3 |
| A term asserted as known that the book never contained | R4 |
| The book's most-used metaphor, arriving unintroduced and mis-credited | Fix 2 |
| A coined-label formula that measured as the draft's largest defect | the cut |
| **The book's central promise, misnamed at first mention** — *the loop* was never this book's word for the WAVE | **A6** |
| Two invented biographies, and a canon rule the gate could not enforce | Tier 3 |
| An authoring note addressed to Wendell, and a missing-asset marker, both printing | P0 — 2 of 3 |

**Not closed by this file, and still open in the spec:** Tier 3 — the ~77
unadjudicated candidates from `instruments/assumed.py`. A6 is closed here, at one
edit rather than three.

## Applying it

Every edit above goes through `instruments/spec_edit.py`, which aborts and writes
nothing on a missed or duplicated anchor. Then, per `.claude/skills/mtgoa-review`:

```bash
python3 instruments/dupes.py                 # before insertion
python3 instruments/gate.py                  # must pass, four surfaces
python3 marginalia/compile.py --verify       # body byte-identical
python3 instruments/review.py                # book-wide, six steps ok
python3 instruments/placeholders.py          # P0 still open, expect 3
```

One commit per editorial question, per the Lean OS git cadence.
