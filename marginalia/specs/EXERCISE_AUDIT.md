# Exercise and Quest Audit

**2026-07-28.** Three findings. One is a real book-wide gap, one is a defect I introduced, one is
unverifiable from this project.

---

## FINDING 1 — the Move template is inconsistent, and 25 moves have no stopping condition

Not seven chapters versus one. **A three-way split:**

| Chapters | Template | Stopping condition |
|---|---|---|
| **7, 8** | prerequisite → body → **The test:** → failure modes | **yes** |
| **3, 6, 9** | *What it is* → *Why it matters* → *In practice* → *Example* | **no** |
| **4, 5** | no consistent structure | **no** |

Ch7 and Ch8 carry `**The test:**` on every move. Ch3, Ch6 and Ch9 use a solid descriptive
template that teaches well and never tells her she is finished. Ch4 and Ch5 have neither.

**Why this matters beyond consistency.** The book's argument is that experience gets metabolised.
**A move with no completion signal cannot be metabolised** — she does it, and does not know whether
she did it. That is the awareness trap operating at the exercise layer, in a book that names the
awareness trap.

It is also the single most visible quality difference between chapters. Ch7's Move 3 has a
prerequisite, a script, a test, and three named failure modes. Ch6's Move 1 has an example and
stops.

**The fix, and it is bounded:** add one stopping condition to each of the 25 moves in Ch3, Ch4,
Ch5, Ch6, Ch9. **~40 words each, ~1,000 words total.** Use Ch7's phrasing so the book reads as one
template rather than three.

**Ch7's form, for reuse:**
> **The test:** The test of honest terms is not whether they change their behavior when you name
> them. The test is whether the naming itself was honest.

The shape is: *the test is not [the outcome you cannot control]. The test is [the thing you did].*
That form works for every move in the book and it is the reason Ch7's moves land.

---

## FINDING 2 — two of my three AMEND notes are defective, and one is a real problem

### Ch5 — **CUT AND REPLACE. This one softens the ask.**

The exercise says: *"Interior sorting is free. Saying it out loud, to the people who hold the
tradition with you, is where loyalty has a price."* And: *"Not in your journal. To their face."*

My note says: *"Do not name it out loud first. Name it to one person who was also there."*

**That is not an amendment. It undercuts the exercise's entire thesis** — the chapter says the cost
*is* the mechanism, and the margin offers a cheaper version. It is the Diplomat shadow installed
next to the exercise built to prevent it, and Jordan will take the cheaper option because the
margin has more authority than the body by Ch5.

**Replacement — raises the cost instead of lowering it:**

> *Pick the person who will be least gracious about it. You already know who that is, and you have
> been quietly choosing somebody else since you started this section.*
>
> *The gracious one will make you feel you have done it. Only the other one will tell you whether
> you have.*

### Ch7 — redundant. The body already has a prerequisite.

Move 3 already sends her back to the Care ↔ Impact axis before closing. My note adds a second
"do this first," which stacks two prerequisites on one move.

**Fix: lead with the finding, which is the part that was not duplicative.**

> *Half the time you will find you do not have a walk-away term at all, which is worth knowing
> before the conversation rather than during it. The other half you will find that you do, and
> that you have known it for months, which is worse and more useful.*
>
> *Either way — say it to yourself in one sentence before you go in. Not to decide anything. Only
> to find out which half you are in.*

### Ch3 — legitimate disagreement, wrongly framed as correction.

The body says the WAVE-Spiral *"can happen in ten seconds or ten hours."* My note says she will
not have five stages available. **Both are true** — Maera is describing what the practice becomes,
the margin is describing the first year. That is exactly what marginalia is for, but mine reads as
a correction of the treatise rather than a disagreement with it.

**Fix: concede the point, then scope the amendment.**

> *Maera says the spiral can run in ten seconds. She is right, and she has been practising for
> thirty years.*
>
> *For your first year, run two: notice, and say. The other three are what you do afterwards, on
> your own time, and they are where the training actually happens. She tells you five first
> because students who learn two never come back for the other three.*

---

## FINDING 3 — the card mapping cannot be verified from here

`Your Twenty Cards` appears in **6 chapters**. `APPENDIX_G_BELIEF_TO_SUPERPOWER_MAP.md` is **not in
this project** — only Appendix A and the Five Channels appendix are.

The daemon-alliance work added a canonical line per Head (*Maera stopped grading her readings*,
*Sera let three inheritances die*, and so on). **If Appendix G maps beliefs to superpowers per
Face, those six lines need to agree with it**, and I cannot check.

**Action:** open Appendix G from the repo and diff the six alliance sentences against it before
print. If they conflict, the canon document governs and the byline notes change.

---

## What does not need fixing

- **The exercises themselves are strong.** Ch5's inheritance exercise gives two exact sentences to
  say and names where they must be said. Ch7's Move 3 gives a full script. These are more concrete
  than most trade nonfiction manages.
- **The frame does not break any of them.** She performs them at home either way; Earth being a
  village the ship visits changes nothing about her Tuesday.
- **The Twenty Cards sections** need no structural change, pending the Appendix G check.

---

## Priority against four days

1. **Ch5 AMEND replacement** — a defect I introduced that actively undermines an exercise. Ten
   minutes.
2. **Ch7 and Ch3 AMEND rewrites** — quality, not defect. Ten minutes.
3. **Appendix G diff** — unknown size, possibly zero, must be looked at.
4. **25 stopping conditions** — ~1,000 words. **The largest remaining writing task in the book**
   and the only one that touches the body text meaningfully. If it does not fit before print, do
   Ch4 and Ch5 first, since they have no template at all.
