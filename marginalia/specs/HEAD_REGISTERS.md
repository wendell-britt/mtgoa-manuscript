# 14 — Head Registers

**2026-07-29. Sits under `SEVEN_VOICES.md`. Ruled by Wendell.**

`SEVEN_VOICES` gives each Head a **genre** (how the sentences are built) and a
**flavor** (who is building them and what it cost). This document supplies the
layer underneath both: **what each Head is doing with feeling while they teach.**

**The principle: the Heads run the alchemy, they never name it.** Chapter 3
teaches the channels explicitly. The treatises must not. A Head who explains her
own emotional move has broken the frame — she becomes a demonstration rather
than a person. The reader should finish Corin's chapter having *felt* anger
resolve into something worth having, without a sentence anywhere telling her
that is what happened.

This is the Shklovsky rule the marginalia already runs on, applied to register:
**describe before naming**, and here, never name at all.

---

## The register table

Every move below is canon from Chapter 3's channel table and its completion
lines — nothing invented. *Fear completes into wonder. Sadness completes into
poignance. Anger completes into triumph. Joy completes into bliss. Neutrality
completes into peace.*

| Head | Face | Dissatisfaction (from) | Channel | Move | Satisfaction (to) |
|---|---|---|---|---|---|
| **Corin Ash** | Challenger | frustration, bitterness | Fire / Anger | Transcend | **Triumph** |
| **Maera Voss** | Shaman | sadness | Water / Sadness | Transcend | **Poignance** |
| **Sera Quill** | Regent | worry **and** sadness | Metal **+** Water | Transcend ×2, compound | **Triumph and Poignance** |
| **Irix Vale** | Architect | anxiety, fear | Metal / Fear | Transcend | **Wonder** |
| **Elian Cross** | Diplomat | worry, anxiety | Metal → Water | Translate | **Poignance** |
| **Thalen Orr** | Sage | frustration | Fire → Wood | Translate | **Joy** |

Three of the six run a **Transcend** — the channel completes into its own
satisfaction. Two run a **Translate** — the charge crosses channels, which is
the harder move and should read as harder. Quill runs both at once, which is why
hers is the most complex register in the book and why the Regent chapter can
afford to be the slowest.

Two notes on the crossings:

- **Orr's Fire → Wood is *Igniting Joy* in miniature** — anger's fire into
  creative passion, and the solvent is humour. He is the only Head who is funny
  on purpose. That is a structural fact about his register, not a personality
  garnish.
- **Cross's Metal → Water is the Diplomat's whole thesis.** Worry about what a
  relationship can hold, refused as anxiety, arrives instead as poignance —
  which is what makes his unthanked staying legible rather than sad.

### What the register is *for*

**Each Head offers his students the satisfaction he is still reaching for.**
Corin is bitter and hands out triumph. Voss carries loss and gives back the ache
that reaches toward someone. That gap — between what the Head holds and what the
Head can give — is the engine. Close it and the character goes flat.

---

## How it surfaces in prose

Per Head, the register shows in three places and nowhere else. Roughly **60–120
words per chapter**, inside Sections 1–3, layered onto the `SEVEN_VOICES`
markers rather than added beside them.

| Head | Dissatisfaction shows as | Satisfaction shows as |
|---|---|---|
| **Ash** | a specific contempt, an unexplained cost, an interlocutor still being argued with | what the drill *earns*: the moment a boundary holds and the student is not sorry |
| **Voss** | the wrong reading she recorded; the thing she knew years before she said it | the reach — loss named all the way through, then someone else's loss carried without collapse |
| **Quill** | a clause that was kept and cost something; a practice she watched lapse | the inheritance passing intact **and** named — both, which is the compound |
| **Vale** | the tolerance he states because he has seen it exceeded; the system that ate someone | delight in the mechanism; the door-closing sentence that is pleased with itself |
| **Cross** | the case he lost; the eleven years unthanked | the field still holding after; both parties' protections named without a verdict |
| **Orr** | the deflection; the sentence that turns toward himself and stops | the joke that lands *because* it is true, and the warmth underneath it |

### The three rules

1. **Never name the channel, the feeling-word, or the move.** No Head writes
   *anger*, *triumph*, *poignance*, *wonder*, or *alchemy* about himself. Ch3
   owns that vocabulary. The Heads own the experience.
2. **The satisfaction is offered, not achieved.** A Head who has completed his
   own move has nothing left to teach. Corin hands his students a triumph he
   has not fully had.
3. **The dissatisfaction arrives as biography, the satisfaction as
   instruction.** This is the load-bearing asymmetry: what he feels shows up as
   something that happened to him; what he offers shows up as what he tells you
   to do.

---

## The biography rule

Rule 3 requires biography, and biography is where a frame like this usually
goes wrong. It grows.

- **One fact per Head, reused.** Corin's is a span of years he was wrong.
  Cross's is eleven years unthanked (already in canon). One fact, referenced
  more than once, is a character. Three facts is a backstory, and
  `PRODUCTION_PLAN`'s do-not-build list already bans that.
- **State the cost, never explain it.** *"I believed them for ⟦SPAN⟧"* is a
  register. *"I believed them for ⟦SPAN⟧ because my father…"* is a novel.
- **First person for the cost, third person for the Face.** The Head keeps
  saying *the Challenger* — it is the role his school teaches, not his name for
  himself. The **I** appears only where the cost does. This resolves the 138
  third-person self-references in Sections 1–3 without touching any of them:
  the stance problem is fixed by adding the *I*, not by converting the *he*.

### Placeholders — Wendell fills these

`SEVEN_VOICES`'s worked sample invented *nineteen* and *six years* to
demonstrate shape. They are not canon and are not adopted here. Each Head needs
one fact, from Wendell:

| Token | Head | What it is |
|---|---|---|
| `⟦ASH-AGE⟧` | Corin Ash | how old he was when he was told the clean no was aggression |
| `⟦ASH-SPAN⟧` | Corin Ash | how long he believed it |
| `⟦VOSS-SPAN⟧` | Maera Voss | how long she knew the thing before she said it |
| `⟦QUILL-CLAUSE⟧` | Sera Quill | the clause she kept that cost her |
| `⟦VALE-SYSTEM⟧` | Irix Vale | the system whose specification ate someone |
| `⟦ORR-DEFLECTION⟧` | Thalen Orr | the question he will not answer about himself |

Cross's is already canon at eleven years. **Nothing ships with a token in it** —
`instruments/gate.py` should fail on `⟦` before print.

---

## Checking it

`review.py --mode voice` tests genre markers and cannot see register. Two
manual checks per chapter, until there is an instrument:

1. **The name test.** Grep Sections 1–3 for *anger, triumph, poignance, wonder,
   bliss, alchemy* in the Head's own mouth. Any hit breaks rule 1.

   **Baseline, measured 2026-07-29** — rule 1 is nearly satisfied already, which
   means this is a light pass and not a rewrite:

   | Ch | Head | Hits | |
   |---|---|---|---|
   | 3 | Voss | 10 × *alchemy* | **exempt** — ch3 is where the vocabulary is taught |
   | 4 | Ash | 0 | clean |
   | 5 | Quill | 0 | clean |
   | 6 | Vale | 0 | clean |
   | 7 | Cross | 2 × *alchemize / alchemical* | **fix** — both are the move-type label vocabulary leaking into Elian's mouth |
   | 8 | Orr | 1 × *alchemize* | **fix** — same leak |

   Ch7 also carries *"**Dissatisfaction moves** alchemize a negative charge into
   a positive one"*, which is Chapter 3's taxonomy stated outright in the
   Diplomat's treatise. That is the clearest single rule-1 break in the book.
2. **The offer test.** Read the last 200 words of Section 3. Does it hand the
   student something the Head does not appear to have? If it hands over
   something he plainly already has, the register has collapsed into
   competence.

---

## Sequencing

Lands **with** W3's genre-marker pass, not after it — the same ~150 words carry
both, and touching these paragraphs twice risks the voice. W6's five sentences
are the first site in each chapter where the register can show, so W6 and this
document are drafted together.

Open: the six placeholder facts, and whether Ch2's Caretaker (Bram Tull) and
Ch9's unnamed student get registers at all. Tull has no Face and no school,
which argues no; the postcard suggests he has one anyway.
