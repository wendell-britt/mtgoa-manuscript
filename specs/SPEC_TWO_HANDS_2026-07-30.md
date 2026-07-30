# SPEC — Separating the treatises from Wendell, and why five of six Heads read flat

**2026-07-30. Wendell: "we still don't have an answer for how to separate the fictional
treatises and the backhalf work that's in my voice and i'd say that the voices of the
different faces are still a bit flat. We've got freedom to get a little whimsical with it
because it is in such a fantasy setting and every chapter ends with grounded if not
slightly humorous prose that connects to the readers real life."**

The two problems are one problem. The Heads read flat **because** they are typographically
indistinguishable from the author, so any whimsy would land as the author being whimsical.
Marking the seam is what buys the voices their range.

---

## 1 · There are three first persons in the book and only one is marked

| whose *I* | how the reader can tell | example |
|---|---|---|
| **The annotator** | set as marginalia, in a blockquote, in a hand | *"I killed an idea once in the first ten seconds and called it discernment."* |
| **A Head** | **nothing** | *"I was told that at nineteen, by people who meant well, and I believed them for another thirty years."* (ch4, Ash) |
| **Wendell** | **nothing** | *"These five channels did not start with me… I have used it hard… What follows is my remix, not the system it came from."* (ch3:384) |

The marginalia frame already solved one of the three. The other two share the same roman
body text with no signal, which means the reader meets a man who cites *wu xing* and
classical Chinese medicine three pages after being told the chapter is *"the first
treatise, submitted by Maera Voss, Keeper of First Signals."*

**And the byline overclaims.** `the second treatise, submitted by Corin Ash` frames the
**whole chapter** as Ash's, including Section 4's exercises, Section 6's Moves, and a
Section 7 recap that points forward to the next chapter of a book Ash cannot know exists.

## 2 · The seam already exists, exactly where Wendell put it

He said *"the backhalf work that's in my voice."* Two independent things agree:

- `HEAD_REGISTERS.md`: the Head's register shows *"in three places and nowhere else…
  inside Sections 1–3."*
- Every chapter's back half is unmistakably the author's: Section 4's exercises, Section
  5's daemon, Section 6's Moves and quests, Section 7's recap and forward pointer.

So the architecture is already **Head in the front half, Wendell in the back half**, and
it is already doing the thing Wendell described about endings: *the Head opens mythic, the
author lands the plane.* Nothing needs restructuring. The seam is simply unmarked.

**Measured, all six treatise chapters:** Section 3 ends with *"For the full process and
additional pairs, see Appendix F"* (or equivalent), then `---`, then Section 4 opens cold.
**Zero of six carry any change-of-hand signal.**

### The fix has to be apparatus, not voice

**Rejected 2026-07-30.** The first draft of this section proposed a hand-off line in
Wendell's voice: *"Cross submitted the above and declined to write an exercise… He is
right, and I have a book to finish, so the rest of this chapter is mine."*

Wendell: *"we cannot do this because the back half is me talking about allyship as wendell
britt NOT as Baldwin."*

He is right, and the failure is bigger than a register mismatch. **That line makes him a
character in the fiction** — a man who receives submissions from Corin Ash, adjudicates
them (*"He is right"*), and manages a workload alongside him. The moment the author speaks
*to* or *about* the Head inside the book's body, the membrane the seam exists to mark is
the thing the marker breaks. And the back half is not a persona at all. It is Wendell
Britt on allyship, which is the one voice in the book that must not be costumed.

**So nothing may cross the membrane. The marker cannot be anybody's voice.**

It has to be **apparatus** — running heads, labels, signatures, rules. Apparatus belongs
to the book rather than to a person, so it can point at the fiction without anyone
stepping into it, and it can point at the author without putting him in a scene.

### The move: sign the treatise where it ends

The byline already exists. It is currently at the **top** of each chapter, closing the
epigraph block:

> *the second treatise, submitted by Corin Ash, Master of the Clean No,*
> *Head of the School of the Line*

If the treatise is Sections 1–3, that signature is in the wrong place. **A submitted
document is signed at the end of itself.** Move it to the close of Section 3 and the
treatise becomes bounded the way a real document is bounded: it opens, it runs, it is
signed, and then the book resumes in the author's own voice without commenting on it.

What stays at the top: the two testimonial voices — the student and the citizen — which
are *about* the Head rather than *by* the Head, so they work as an epigraph and always did.
Nothing is lost from the chapter opening, because `# CHAPTER 4: THE CHALLENGER` already
names the Face and the student's attribution already names the school.

**Cost: zero new words.** It relocates text that is already written, and it uses the one
convention that needs no narrator.

Optional second layer, for the typesetter rather than the manuscript: a running head
reading `FROM THE SECOND TREATISE` across Sections 1–3 that drops away at Section 4. Pure
apparatus, no voice, and it makes the seam visible on every spread rather than once. Print
only — ebook running heads are unreliable, so the signature carries it alone in the digital
edition.

### The convention gets explained once, in front matter

`front_matter/copyright.md` already carries **"A note on what this book is not"** — Wendell
Britt, real voice, speaking about his own book from outside it. That is the precedent and
the correct slot. One short note there, in the same register: six chapters open with a
treatise written in the voice of the Head who teaches that school, the practice sections
are the author's own, and the signature marks the turn.

Said once in apparatus, the reader carries the convention through all six chapters and no
line in the body ever has to reach across.

### One honest complication

**`ch3:384` is Wendell's, and it sits inside Section 3** — the *wu xing* sourcing note,
which is the most clearly authorial paragraph in the front half of any chapter. Under the
signature convention it stops being a judgment call and becomes a defect: Voss cannot cite
classical Chinese medicine or say *"what follows is my remix"* above her own signature. **It
moves below the seam.** It stays inside ch3, so `copyright.md`'s existing pointer — *"Chapter
3 says what the remix changed"* — survives the move untouched.

The same sweep has to catch every other authorial sentence sitting above a signature. That
is a measurement rather than a judgment, and it is the one piece of work this convention
creates: **six chapters, Sections 1–3, find every sentence only Wendell could have
written.**

## 3 · Why the voices are flat: the register pass never shipped for five of six Heads

`HEAD_REGISTERS.md` specifies 60–120 words of register per chapter and lists six
placeholder facts Wendell must supply. **Four are still absent from the manuscript
entirely:**

| token | Head | in manuscript |
|---|---|---|
| `⟦ASH-AGE⟧` / `⟦ASH-SPAN⟧` | Corin Ash | **filled 2026-07-30** — nineteen, another thirty years |
| `⟦VOSS-SPAN⟧` | Maera Voss | **0 occurrences** |
| `⟦QUILL-CLAUSE⟧` | Sera Quill | **0 occurrences** |
| `⟦VALE-SYSTEM⟧` | Irix Vale | **0 occurrences** |
| `⟦ORR-DEFLECTION⟧` | Thalen Orr | **0 occurrences** |

Zero occurrences means the token was never inserted, so **the paragraph that would carry
the register was never written.** Ash is the only Head who got one. The flatness is an
unshipped pass, not a craft ceiling.

### First-person density in Sections 1–3, where the spec says the cost must arrive

| ch | Head | words | first-person | per 1k |
|---|---|---|---|---|
| 3 | Voss | 3,094 | 38 | 12.3 |
| **4** | **Ash** | 2,368 | 20 | **8.4** |
| 5 | Quill | 2,981 | 21 | 7.0 |
| 8 | Orr | 4,128 | 19 | 4.6 |
| 6 | Vale | 2,673 | 10 | 3.7 |
| **7** | **Cross** | 1,168 | **0** | **0.0** |

Three readings:

- **ch4 at 8.4 is the only figure that is actually a Head.** Ash got the pass; that is what
  a landed register measures.
- **ch3's 12.3 is misleading.** It is largely Wendell — the sourcing note and the council
  narration — not Voss. Voss's own register is thinner than Ash's, not thicker.
- **ch7 is at literal zero, and Cross is the one Head whose fact is already canon**
  (*eleven years unthanked*, per `HEAD_REGISTERS`). The flattest voice in the book has the
  readiest material. Start there.

`ch8` also matters out of proportion: `HEAD_REGISTERS` says Orr's Fire → Wood crossing
makes him **"the only Head who is funny on purpose. That is a structural fact about his
register, not a personality garnish."** He is currently running at 4.6, half of Ash.

## 4 · The whimsy is already licensed, and it is not licensed everywhere

`SEVEN_VOICES` is not a restrained document. It anchors the Heads to **Baba Yaga,
McGonagall, Susan Calvin, Arthur Aguefort, Last Jedi Luke, Iroh, Picard, Worf, Colonel
Tigh** — and Voss's flavor is one word: **witchy.** *"Withholds on purpose; the refusal is
the teaching; not safe; transactional."* Nothing on the page is currently that strange.

**Where whimsy goes:** genre and manner. How the Head builds a sentence, what they refuse
to explain, what they find funny, what they are pleased with.

**Where it must not go**, per rules already ruled:

1. `HEAD_REGISTERS` rule 1 — **no Head ever names the channel, the feeling-word, or the
   move.** ch7 and ch8 already break this (`alchemize`, `alchemical`, and ch7's *"**Dissatisfaction moves** alchemize a negative charge into a positive one"*, called out as the clearest single break in the book). Whimsy must not add breaks.
2. The **biography rule** — one fact per Head, reused; state the cost, never explain it.
   *"I believed them for thirty years"* is a register. *"…because my father"* is a novel,
   and `PRODUCTION_PLAN`'s do-not-build list already bans it.
3. **First person only where the cost is.** The Face stays third person, because it is the
   role the school teaches rather than the Head's name for themselves.

So the whimsy budget is spent on **manner, not backstory** — which is also the cheap
direction, because manner costs sentences and backstory costs pages.

### Worked sample, ch7 · Elian Cross

Picard and Troi. Metal → Water. The cost is canon and the channel is never named:

> *The Bridge sets one examination and I have never written another. You are given a table
> with two parties at it and asked what each can afford to lose. Most candidates answer for
> the stronger party first, and do not notice that they have.*
>
> *I sat eleven years at a table where the terms I wrote held and nobody said so. They are
> still holding. I have stopped expecting the sentence and I have not stopped wanting it,
> and both of those are a condition of the work rather than a complaint about it.*

Ninety-one words. Cost in first person, Face in third, no channel named, the satisfaction
offered rather than achieved (*they are still holding* is what he hands the student; the
unthanked years are what he keeps).

## 5 · What this needs from Wendell

1. **The four facts** — `VOSS-SPAN`, `QUILL-CLAUSE`, `VALE-SYSTEM`, `ORR-DEFLECTION`. One
   line each, same shape as the two he filled for Ash today. These block five of six
   register paragraphs and therefore block the flatness fix.
2. **Sign-off on the signature move** — byline relocated from the chapter head to the
   close of Section 3, so the treatise is signed where it ends and no voice crosses the
   membrane.
3. **Sign-off on the front-matter note**, one paragraph beside *"A note on what this book
   is not."*
4. **Whether the print edition also gets the running head** across Sections 1–3.

Cross needs none of these and can be drafted now, since his fact is canon and his chapter
is the flattest in the book.

## 6 · How this gets checked

```
grep -rc "⟦" manuscript/                      # 0 — gate already enforces
grep -rn "alchemiz\|alchemical" manuscript/ch7.md manuscript/ch8.md   # 3 rule-1 breaks today
grep -c "submitted by" manuscript/ch4.md   # 1 — must sit below Section 3, not above Section 1
python3 -c "…"   # first-person per 1k in S1-S3; ch7 must leave 0.0
```
