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

---

## What this closes

| | |
|---|---|
| **4 of 9** machine-verified false back-references — every *"Chapter 1 taught you to read the meter"* site plus the ch3 living-field gloss that made two downstream claims true | R1, R2 |
| The abandoned escalator ladder, now running ch3 → ch8 | R3 |
| A term asserted as known that the book never contained | R4 |
| The book's most-used metaphor, arriving unintroduced and mis-credited | Fix 2 |
| A coined-label formula that measured as the draft's largest defect | the cut |

**Not closed by this file, and still open in the spec:** A6's three edits, and Tier 3 — the ~77
unadjudicated candidates from `instruments/assumed.py`.

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
