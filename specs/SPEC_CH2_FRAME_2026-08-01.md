# SPEC — Ch2 leaves the fiction. The game opens at the Headmaster's letter.

**Ruled by Wendell 2026-08-01**, reading ch2: *"we're having an issue between what is the
treatise content and what's me wendell teaching people. I don't think the cuts are as clean as
we thought."* Then: *"let's remove Bram from the chapter entirely. Especially since after 3 is
when the GAME begins properly with the letter from the headmaster. If we can keep the letter
from the headmaster boxed in just like the content in the other chapters it will signal to the
reader that this is alternative content."*

Applied the same day. Branch `claude/treatise-wendell-content-boundaries-78sq54`.

---

## 1 · The defect: ch2 was claimed twice and reconciled never

Four documents, two incompatible readings, and nothing that resolved them:

| Document | ch2 is |
|---|---|
| `SPEC_DL19_AUTHOR_COLLISION:33` | *"ch1, ch2 and ch9 are **Wendell's frame** and are out of scope."* |
| `SPEC_DL19_AUTHOR_COLLISION:73` | *"Wendell's real biography has exactly one legal home: the frame — ch1, ch2, ch9."* |
| `marginalia/HANDOFF.md:21` | *"**Bram Tull**, Caretaker, **writes Ch2**."* |
| `marginalia/new_prose/BYLINES.md:29` | *"**Not a treatise** — the Caretaker is staff, not a Head."* |

So ch2 was the designated home for the author's real biography **and** a document set down by a
fictional caretaker.

**The mechanical half.** `SPEC_TWO_HANDS` moved every treatise byline from the chapter head to
the close of Section 3, on the reasoning that a top-of-chapter byline *"overclaims… frames the
**whole chapter** as Ash's."* That landed six for six — ch3:246, ch4:227, ch5:294, ch6:229,
ch7:210, ch8:285. **Ch2 was not in the set, because it is not a treatise, so its byline stayed
at the top.** Ch2 therefore held the last top-of-chapter byline in the book, in the exact
configuration the spec condemned, over the chapter whose contents are most unmistakably the
author's.

The byline note made the claim explicit rather than implicit: *"He agreed to **set this down**…
I want you to know what **these pages** cost."*

## 2 · The measurement — ch2 had never been swept

`instruments/seam_sweep.py` hardcodes `CHAPTERS = [3, 4, 5, 6, 7, 8]`. Running its own three
tiers over ch2's body, marginalia stripped:

| | ch3–ch8 combined | **ch2** |
|---|---|---|
| BOOK — cannot know it is inside a book | 2 | **28** |
| AUTHOR — the author's life and work | 37 *(mostly legitimate Head biography in handbooks)* | **13** |
| CREDIT — real-world attribution | 0 | **2** |

Fourteen times the BOOK-tier count of all six cleaned treatises put together. The load-bearing
sites:

- **Section 4, 420 words of autobiography** under Bram's signature — George Floyd, May 2020, the
  phone filling up, *"I was the only Black person most of them knew."*
- **`ch2:241` is the only place in the manuscript body where the book names itself** — *"The
  first version of Mastering the Game of Allyship was written from that anger."* `seam_sweep`'s
  T2 pattern catches `Igniting Joy` and not this title, so the instrument under-reports even the
  chapter it does not scan.
- **Three real-world credits** a caretaker was signing for: Carolyn Elliott (`:73`), Robin Rice
  (`:294`), Gerard Egan (`:451`). Two are already in the T3 pattern.
- **Navigation Bram cannot perform** — *"For the full game taxonomy and mechanics, see Chapter
  1"* (`:151`), *"Before Chapter 3 teaches full emotional alchemy"* (`:405`), *"Appendix A holds
  the full map"* (`:558`).
- **Two unowned first persons** in otherwise second-person prose: `:268` *"let me tell you how
  this game teaches"*, `:370` *"**I** walk into a conversation already armored."*

**These 43 sites are not fixed. They are made legal.** With no fictional author claiming the
chapter, every one of them is Wendell Britt writing his own frame, which DL-19 already ruled is
where they belong.

## 3 · What was removed

Ch2 now carries no in-world apparatus at all and sits with ch1.

| Removed | Was |
|---|---|
| `FRONT[2]` | two epigraph testimonials + `set down by Bram Tull, Caretaker, who was asked eleven times` |
| `BYLINE_NOTE[2]` | *"Bram is not faculty…"* |
| `NOTES[2]` | five annotator margin notes |
| `compile.py` `CHAPTERS` | `[2,…,9]` → `[3,…,9]` |

Frame blocks book-wide: **54 → 47**. Ch2 body text is unchanged by this move; only the frame
came off.

### Two downstream dependencies, both checked

**Bram survives where he pays off.** He signs his own note at `ch8:584` (*"I leave food where he
will walk into it. He thinks the galley is badly organised"*) and receives the last page of the
book at `ch9:695` (*"The galley here is badly organised. Nobody is fixing it"*). That pair is
self-contained and never depended on ch2. `MARGIN_ARC:158` already had him signing in ch8.

**The one piece of canon the ch2 notes carried alone.** `CH2_CARETAKER.md:93` warns that *"which
is not a recommendation"* is *"the single most load-bearing clause in the chapter"* and that
without it *"the Ch9 invitation loses its only setup."* That content survives two pages later in
the Headmaster's letter, in the mouth it belongs to: *"Take all six and you will be useful in
most situations… Take one of them to the bottom and you become the person somebody travels a
long way to find, which is rarer and is not better. Nobody here will tell you which you are
for."*

## 4 · The letter is boxed

`front_matter/headmasters_letter.md` sits between ch2 and ch3 in the `build_book.py` spine. Its
body is now wrapped in a `> ` blockquote inside `<!-- LETTER -->` markers, matching how every
other in-world insert renders. `# A Letter to the Reader` stays outside the box, because
`build_book.title_of()` reads the first heading for the contents page.

The file is deliberately outside the `manuscript/ch*.md` glob, so `compile.py` never touches it
and the boxing is hand-maintained. `gate.py` reads it on the **matter** surface and still
passes; `build_book.py` still reports it at 722 words.

## 5 · Verification

```
python3 marginalia/compile.py --verify     # body text round-trips byte-identical, ch3-ch9
python3 instruments/gate.py                # GATE PASS, all four surfaces, every counter 0
python3 instruments/build_book.py          # Chapter 2 7,149 · Letter 722 · 47 frame blocks
grep -c "Bram\|Tull" manuscript/ch2.md     # 0
grep -c "Bram" manuscript/ch8.md manuscript/ch9.md   # 2, 1
```

## 6 · Open

`instruments/seam_sweep.py` still reads `CHAPTERS = [3..8]`. That is now correct rather than
accidental — ch2 has no seam because it has no fictional author — but the reason should be
recorded in the docstring so the next reader does not re-derive it.
