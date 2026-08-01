# 6-Face GM — The three open questions on the ch3 beat

**Created:** 2026-08-01
**Subject:** the two-readings replacement beat for ch3, v10, and the three decisions still open on it
**Companion:** `TWO_READINGS_6FACE_RULING.md`, `D5_SWEEP_REVERIFICATION_2026-08-01.md`

---

## The evidence that reframes two of the three

ch3's body carries **16 first-person sentences**, and none of them is Wendell. They are **Maera Voss's casebook**, at ch3:167–173:

> Thirty-first session. Jaw, then the back of the neck. I recorded contempt in the man at the head of the table. Grief, four days old. I did not have that until the funeral.
>
> **I called it discipline.** The entry correcting that is dated later and reads: the numbness began the morning after the funeral, not the morning of the error. It was not protecting me from being wrong. It was protecting him from being read a second time by somebody who had got it wrong in front of witnesses…
>
> Present session. Jaw, at the word correctly. The reading came back and it is better than it was.

Three things follow immediately.

**The self-deprecation slot has a legitimate filler.** A casebook entry is authored fiction in an assigned head voice. It is not invented biography, so the canon rule that killed the last draft — *do not attribute generated prose to Wendell* — does not apply to it.

**That passage is already the numbness confession.** *"I called it discipline"* and *"the numbness began the morning after the funeral"* is precisely the admission the beat was reaching for, in the right voice, forty-three lines below where the beat would sit.

**It is also the four missing voice markers.** Numbered observation (*Thirty-first session*), recorded wrong reading (*the entry correcting that is dated later*), sensation nouns (*jaw, the back of the neck*), refusal to name. The markers the linter wants are not absent from ch3's design; they are concentrated in one passage.

**Layout:** exile ends ~124 → **[proposed beat]** → Section 2 Distortion (127) → Section 3 Concept (158) → casebook (167).

---

## Q1 · The self-deprecation slot

### 🌊 Shaman
Being told *the village is you* and *you did it* with nobody standing beside you is a cold read. But the warmth arrives at :167 and the reader gets there in two minutes. **The beat does not have to carry what the chapter already carries forty lines later.**
**Verdict: leave the slot empty.** The company is coming.

### ⚔️ Challenger
The real question is whether *"for reasons that were good at the time"* is doing the work or buying the author out of exposure. It softens without anyone paying. But **the alternative already exists and is stronger than anything a new line would be** — *I called it discipline* is a practitioner admitting she misfiled her own numbness as virtue. Writing a second, weaker confession forty lines above it competes with the good one.
**Verdict: empty.** Do not put a decoy in front of the real thing.

### 🏛 Regent
The standing rule holds absolutely: nothing goes in Wendell's first person that he did not write. That was never really a question, and the last draft violated it.
**What to preserve is the casebook's position.** :167 lands after the concept has been set up, so the confession explains something. Moved to :124 it would arrive before the reader knows what a reading *is*.
**Verdict: empty, and the rule stays a rule.**

### 🧠 Architect
Two confessions 43 lines apart in the same register is a duplication, not a rhythm. If the beat needs the reader to not feel judged, the cheapest structural fix is **a forward pointer**, not a second admission — and the beat already has one in *"Section 4 brings it back."*
**Verdict: empty.** Consider whether the pointer should name the casebook instead of Section 4.

### 🎭 Diplomat
The bridge is trust, and trust here is a question of sequencing rather than volume. A reader told *you did it* at :124 and given a practitioner's *I called it discipline* at :167 experiences the book as honest. A reader given two confessions experiences it as pleading.
**Verdict: empty.**

### 📖 Sage
The instinct that produced the fabricated anecdote was correct and the execution was wrong twice — invented biography, and invented in the wrong voice. **The book had already solved this problem and nobody looked.** That is the finding worth keeping: before writing a new register into a chapter, check what the chapter already does.
**Verdict: empty.**

**Q1 — unanimous: leave the slot empty. The confession exists, it is better, and it is 43 lines away.**

---

## Q2 · The somatic echo — chest / jaw / stomach at both :124 and :740

### 🌊 Shaman
The three markers are the chapter's physical vocabulary. Meeting them at :124 and again at Move 1 is how a body vocabulary gets learned — once cold, once in use.
**Verdict: plant.**

### ⚔️ Challenger
Move 1's line is *"Heat in the chest, a drop in the stomach, the jaw. When you notice one, do not ask what it means."* That is the operative instruction, and it lands harder if the reader has already met the three and done nothing with them.
**Verdict: plant** — but the beat must not instruct. If :124 tells her what to do with the markers, Move 1 has nothing left.

### 🏛 Regent
`dupes.py` will not catch this because the sentences differ. **Which means it needs recording**, or a future reader of a duplication report re-derives the question from scratch.
**Verdict: plant, and note it in the commit.**

### 🧠 Architect — dissent
Both instances use the same three. A plant that varies — throat, shoulders, breath at :124 — would widen the vocabulary *and* leave Move 1's triple intact. Same pedagogy, no overlap.
**Verdict: vary.** The plant argument does not require identical items.

### 🎭 Diplomat
Identical items are what makes the recognition work at Move 1. Varied ones read as a longer list, not a callback.
**Verdict: plant, identical.**

### 📖 Sage
ch3 is under its own sensation-noun target book-wide. Both options add sensation nouns; only the varied one adds *new* ones.
**Verdict: no strong preference — note that either improves the chapter's weakest measured axis.**

**Q2 — 4 for identical plant, 1 for varied (Architect), 1 abstain. Carried: plant, identical, recorded in the commit, and the beat must not instruct.**

---

## Q3 · Go / no-go on v10

Every Face reached the same two-part answer.

**Go on the content.** v10 is the first version that does the job stated: turns the fable inward, checks it behaviourally rather than by sensation, and does not tell Jordan what she feels. `gate clean`, seven diet counters in band, `voice BLOCK 0`, `body BLOCK 0`.

**One line does not survive Q1.** With the slot ruled empty, the beat currently ends:

> …Calling numbness peace is the mistake this chapter exists to interrupt.
>
> Section 4 brings it back.

**Challenger and Architect both flag `"the mistake this chapter exists to interrupt"`** as the beat explaining its own importance — importance puffery, and the one remaining line where the author stands above the material. Cut it and the paragraph ends on the concrete claim.

**Sage adds a placement note:** the beat asserts *the village is you* at :124, and `FACE_AUTHORS.md:115` records the six heads as *"a reconciliation job"* found on 2026-07-28 and not yet merged. **The beat is being written into a chapter whose voice spec is mid-migration.** Worth knowing; not worth blocking on.

---

## Summary

| Q | Ruling | Vote |
|---|---|---|
| **1 · self-deprecation slot** | **leave empty** — the casebook at :167 is the confession, and it is better | 6–0 |
| **2 · somatic echo** | **plant, identical**, recorded; the beat must not instruct | 4–1–1 |
| **3 · v10** | **go**, minus the self-importance clause | 6–0 |

---

## The resulting text

> Read that again with one change. The village is you. You stopped listening, gradually, without ever saying go.
>
> Check that against the record rather than against how you feel now. When did you last say what you sensed in a meeting before you had proof? If an answer arrives fast, the Shaman still gets consulted in there. If you have to go back years, you already know what happened, and it did not happen to you. You did it, for reasons that were good at the time.
>
> The signal did not stop arriving. Heat in the chest before a hard sentence, the jaw setting when somebody says *fine*, the drop in the stomach a beat before you know why. What stopped is the part that treats the signal as usable. Calling numbness peace is the mistake.
>
> Section 4 brings it back.

Requires a re-gate before it lands — the final clause changed.

---

## Open question for Wendell

**Should the beat point at the casebook rather than Section 4?** *"Section 4 brings it back"* points 400 lines ahead. The casebook at :167 is 43 lines ahead and is the chapter's own account of numbness misfiled as virtue. The Architect raised it and the panel did not resolve it, because it depends on whether :167 is meant to be a payoff the reader stumbles into or one the book routes her to.

---

*Ruling: adopt all three. Cut the self-importance clause, re-gate, then apply with the ch8 one-word fix.*
