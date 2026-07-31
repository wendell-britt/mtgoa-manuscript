# Editorial pass 2026-07-31 — whole book, then chapter by chapter

Diagnosis only. **No prose was changed.** The marginalia frame round-trips
byte-identical and `gate.py` passes on all four surfaces, before and after.

**Line numbers everywhere in this directory are on-disk numbers** — the file with
the frame applied, what you see when you open it. The Architect scan was
originally written against stripped-file numbers and has been remapped by
searching the quoted text; ch1 carries no frame and was never affected.

| Report | Flags |
|---|---|
| `ARCHITECT_WHOLE_BOOK.md` | 6 structural (A1–A6) + A7 permissions |
| `CH1.md` | 16 — structure 3 · continuity 7 · line 6 |
| `CH2.md` | 19 — structure 5 · continuity 8 · line 6 |
| `CH3.md` | 19 — structure 6 · continuity 7 · line 6 |
| `CH4.md` | 18 — structure 5 · continuity 7 · line 6 |
| `CH5.md` | 16 — structure 4 · continuity 6 · line 6 |
| `CH6.md` | 19 — structure 6 · continuity 7 (1 withdrawn) · line 6 |
| `CH7.md` | 17 — structure 7 · continuity 4 · line 6 |
| `CH8.md` | 21 — structure 6 · continuity 9 · line 6 |
| `CH9.md` | 21 — structure 3 + drill 4 · continuity 8 · line 6 |

---

## P0 — would print tomorrow

**`ch7:467` carries an authoring note addressed to Wendell.**

> `[[TESTIMONY SLOT — WENDELL. This is where Ch5 puts Mr. Inadequate and Ch3
> puts the harm passage. Needed: one time the ledger opened while somebody was
> telling you the truth about your impact, and what you said instead of hearing
> it. Not the lesson. The beat. ~150-200 words in your voice.]]`

It is the only `[[` in the manuscript. Verified present in the built deliverable
at `build/MTGOA_PRINT_2026-07-31.md:4250`. Two more placeholders print with it:
`ch1:179` `*[visual: the six Game Masters]*`, an asset that exists in neither
`figures/` nor `visuals/`; and `ch1:267` `**[ URL / QR ]**`, which is the book's
only call to action and the terminus of two of ch1's four practices.

**Why nothing caught this.** `gate.py` scores banned words and voice defects.
`build_book.py` scores missing *files*. An unfilled slot inside a present file is
neither, so the gate reads clean at 0 across four surfaces with an authoring note
sitting in the prose. **`instruments/placeholders.py` was written today to close
that gap** — additive, does not modify `gate.py`, exits non-zero on any hit, and
allowlists the two legitimate in-world bracket constructions (the Diplomat's
`[Camp A]`/`[Camp B]` party labels and Irix Vale's unreproduced figures).

```
python3 instruments/placeholders.py      # currently: 3 hits, exit 1
```

---

## The one pattern under most of the rest

**Conventions that start and stop.** The book repeatedly opens a device, runs it
for a stretch, and drops it without closing it. Each instance is small; the
aggregate is the reader losing her grip on what the book is doing.

| Convention | Runs | Stops |
|---|---|---|
| Three Games — Chance/Skill/Passion | ch1 only | never used again (A1) |
| Character-sheet line | ch1 → ch2 → ch9 | six silent chapters (A2) |
| "Chapter 1 taught you to read the meter" ladder | ch3, ch4, ch5 | stops at ch6 |
| "You're winning when" test | ch3 (4×) | nowhere else |
| Polarity Encounter → Appendix F pointer | ch3–ch7 | ch8 alone lacks it |
| Myth teardown + bolded replacement belief | ch4, ch6, ch7, ch8 | ch5 recap has neither |

The *meter* ladder is worth its own note: `Chapter 1 taught you to read the
meter` appears verbatim at `ch3:451`, `ch4:293` and `ch5:324`, and **`meter` has
zero occurrences in ch1**, which teaches the Token System and the tank. Three
sites credit ch1 with vocabulary it never used, so the fix is one decision
applied three times.

---

## A6 — the spine, and the largest finding of the pass

Promoted into the Architect report after ch1, ch2 and ch3 converged on it
independently; re-verified directly. **It outranks A1–A5.**

Chapter 1 stakes the book on one repeatable process — *"you do not have to learn
everyone. You learn one process"* (`ch1:60`) — and says *"the loop you meet in
the next chapter"* (`ch1:191`). Chapter 2 delivers a different five (Spot /
Thank / Name the cost / Take the joystick / Log the tape), which return zero hits
in ch1 and ch3–ch9. The loop that actually runs the Face chapters is the
WAVE-Spiral, defined at `ch3:244`. Its five stage names read **0 in ch1 and 0 in
ch2**. Then `ch3:824` tells the reader *"you already know all five."*

No content is missing — ch2's moves are real and ch3 teaches the Spiral properly.
Three edits close it: repoint `ch1:191`, name ch2's five as what they are, cut
the false prior knowledge at `ch3:824`.

---

## Retired-scaffolding survivals — the gate walk and the Vulnerable Child

Canon records the eight-gate walk removed from ch4–ch8 and the Vulnerable Child
gone with it, leaving ch2's roster at seven. Four survivals remain:

- `ch8:191` — *"This is the Vulnerable Child's gift"*, a definite construction
  pointing at an introduction that no longer exists
- `ch9:492`, `ch9:508` — an eight-gate scan naming the Vulnerable Child, inside
  a reader instruction
- `ch8:458` — enumerates six daemons while calling the last *"seventh in line"*,
  dropping the Emotional Body, and places the Damaged Self *"one gate before the
  center"*
- `ch2:434`–`436` — the center of the Forest is *"the youngest part of you"* who
  says *"Please don't leave me here again"*, and *"the whole walk is reaching
  her"*. The name was removed; the shape is still load-bearing.

**Four-beat sequences against the five-beat rule:** `ch8:431` *"The practice has
four moves"* is the last four-move sequence in the manuscript. And `ch4:354`–`368`
hands Jordan a 30-second protocol with four beats — feel, aim, act, exit —
dropping **Stand**, which `ch4:277` has just argued is precisely the omission
that lets a reader *"execute every other stage correctly and still end up with
nothing drawn."* The chapter names the failure and then models it.

Running the other way: `ch9:284` reads *"You now know the WAVE. Wake up. Open up.
Clean up. Grow up. Show up. **Come back.**"* — six beats where canon has five,
and *the altar* (`ch9:286`), asserted as known, is defined nowhere in ch1–ch8.

---

## Chapter 9 does not close two of Chapter 1's three promises

The five Player moves and the transfer drill are the chapter's best work, and the
drill covers all six Faces with the wrong pull named in each. What fails is the
bookkeeping.

**The BAR deck.** `ch1:247` promises *"by the last chapter you hold a deck no one
else could have built."* Measured: `BAR` appears **0 times in ch9's 725 lines**,
against 8 in ch1 and 2–7 in every other chapter. Meanwhile `deck` is used nine
times in ch9 to mean the published 120-card product — `ch9:700`, *"Start with the
deck. It is the one that begins the moment you open the box."* The noun the
reader was told she would build has been reassigned to a thing she buys.

**The drill has no result she can pass.** Cluster four or more and *"you have
just watched your autopilot run"* (`ch9:682`); spread across six and *"choosing
between the Faces on a page is the easy version"* (`ch9:686`). The most likely
outcome — two or three clustering — gets no read, and the *move* half of the
two-part answer collected at `ch9:648` is never scored.

**The character sheet closes, partly** — and see A2 for why the sheet it turns
to is nearly empty.

---

## Where a chapter demonstrates less than it claims

- **ch6 §6** promises *"what does it actually look like in a real situation"*
  (`ch6:380`) and delivers five examples containing no person and no allyship — a
  dashboard, decision rights, an onboarding flow, three tools, a feature. The
  chapter's own replacement belief (`ch6:533`) is never demonstrated. This is
  Jordan's documented coldness risk landing exactly where predicted.
- **ch8 Move 5** (`ch8:603`, 308w) is the book's only move with neither an
  example nor a test, and the template degrades monotonically across Moves 3, 4
  and 5.
- **ch4:422** names *"the actual work of this chapter"* and attaches no move to
  it.
- **ch3:764** summarises five moves, two of which — *"Ask for the unreduced
  version"* and *"Spend the read inside the window"* — exist nowhere in the
  manuscript, and drops Open Up and Grow Up. `ch4:729` runs the same convention
  correctly.
- **ch7:71–79** promises each of five table rows is *"worked through in the five
  channel deep-dives in Section 4"*; three are not.

---

## Two corrected false positives, recorded so they stay corrected

1. **`ch6:113` "See figure four" is not an error.** Withdrawn from CH6. It is
   Irix Vale's ruled tic — `SEVEN_VOICES.md` lists *"references figures and
   diagrams that are not reproduced"*, and the surrounding passage carries his
   Refusal verbatim at `ch6:118`. The flag was reasonable, because the line is in
   body text rather than margin — but **Sections 1–3 body text is the Head's
   treatise, not Wendell's register**, so "not in the margin" does not mean "in
   the author's voice." This is the exact failure the Voice Guardian exists to
   prevent.
2. **ch4's hedge BLOCK is the linter over-reporting.** All four treatise hits are
   `\brather\b` catching the comparative *X rather than Y*, plus one *maybe*
   quoted inside village speech the treatise is mocking. Corin's treatise has
   zero genuine hedges. **The fix belongs in `marginalia/review.py`, not in ch4
   prose.**

Also cleared by instrument, so nobody re-runs them: ch2's section numbering is
1–10 with no gap and its roster is seven, counted consistently at six points;
`chain2.py`'s "ch1–ch4 no moves" was a parser artifact (ch3–ch9 each carry five);
ch5 has zero bare claims, contrary to an earlier instrument run; ch7 does hand
Jordan practice (a four-step *Try this now*, three app captures, a timed run, two
self-checks) — it is typographically invisible, not absent; Wilber, Elliott,
Chou, Egan, Laloux, Maslach and *wu xing* all check out.

---

## The one uncredited source

*The Courage to Be Disliked* is quoted at `ch3:228` — *"has a line: all problems
are relational problems"* — and returns **zero hits** in the copyright page's
Sources and permissions, in Appendix G, and in all back matter. It is the only
named outside source in the book with no credit anywhere. Logged as A7.

---

## Recommended order

**Tonight, if anything:** the P0 placeholders — `ch7:467` first, then ch1's two.
Then A7, which is a line on the copyright page.

**Cheap and high-value, in order:** A6's three edits (the spine). A5's appendix
pointer, which copies a form ch3 already uses three times. A4, a cut. The *meter*
ladder, one decision applied at three sites. A3, softening one phrase.

**Real decisions, not tonight:** A2 (narrow the promise, or seat six sheet
lines), ch3's split at `ch3:685`, ch9's BAR-deck closure, and the retired-
scaffolding survivals, which want one sweep rather than six patches.
