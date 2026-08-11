# `WAVE` is two things, and both of them ship

**2026-08-07. Wendell:** *"the issue I'm running into is the use of 'the WAVE'… I think this
was supposed to be the 5 move flow and not the open up exercise."*

**He is right, and the collision is live in print right now.**

---

## 1 · The two meanings, both in the shipping book

| | | where it ships |
|---|---|---|
| **WAVE** | **W**elcome · **A**cknowledge · **V**alidate · **E**xhale — four breath actions, a short somatic practice for when charge is already in the body | `APPENDIX_C_FIVE_CHANNELS.md:15` |
| **the Five-Move Form** | Wake · Open · Clean · Grow · Show — five macro movements, the form that runs every Face's game section | `ch1`, `ch5`, five apparatus files |

**The repo's own specs state the split and nothing enforced it:**

> *"`WAVE` = four breath actions; Five-Move Form = five macro movements"*
> *"…`WAVE-Spiral` that means the Five-Move Form; keep 3-2-1's own lineage separate"*

**A reader who reads Appendix C and then Chapter 3 meets two different WAVEs.** Appendix C
gets it right; the chapters do not.

**Nothing caught it, and could not have.** `WAVE` is never expanded in the body, so its
letters are never checkable against what it names, and **no instrument asks whether a
concept has one name.** `xref.py` only asks whether pointers resolve.

## 2 · This is a rename somebody started and abandoned

**The book already uses both names, split cleanly by chapter. No chapter uses both.**

| ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|
| **Five-Move** ×1 | — | WAVE ×20 | WAVE ×2 | **Five-Move ×3** | WAVE ×1 | — | — | WAVE ×17 |

**ch1 makes the promise correctly** — *"One form runs through every Face: the Five-Move
Form."* **ch3 then delivers it as `WAVE-Spiral` eighteen times.** ch5 goes back to the right
term and uses it exactly as intended — *"the five movements of the Five-Move Form against
four domains, one card per crossing."* **ch9 says `the WAVE` seventeen times and
`WAVE-Spiral` zero**, so it is not even consistent with ch3's version of the wrong name.

**So the job is finishing a conversion, not making one.**

### Size, shipping surfaces only

| | |
|---|---|
| `WAVE` / `WAVE-Spiral` to convert | **53** |
| `Five-Move Form` already correct | **9** |

*(A further 9 sit in `APPENDIX_C_KEY_TERMS`, retired and not in `SHIPPING_APPENDICES`.)*

**Four chapters plus the glossary and the index.** ch3 carries 20, ch9 17, Appendix E 6,
Appendix C 3, ch4 2, ch6 1, and one each in Appendix D, Appendix F, the glossary and the
index.

**It is not mechanical.** ch3's twenty sit inside the practice section where the term is
load-bearing and hyphenated as `WAVE-Spiral`. ch9's seventeen are mostly running prose —
*"the WAVE runs through your parenting"* — which reads differently as *"the Five-Move Form
runs through your parenting."* **Those seventeen want rewriting, not replacing.**

## 3 · The breath practice comes back, and it is already written

**Wendell: the breath practice should come back into the book. Scanned — it is already
there**, in the shipping Appendix C, and the retired Key Terms carries a fuller definition:

> **WAVE** — A short somatic practice: Welcome, Acknowledge, Validate, Exhale. Use it when
> charge is already present in your body.

**So `WAVE` does not return to an empty seat.** It returns to a definition the book already
holds. What is missing is that **the four words appear as a set exactly twice in the whole
repo**, both in apparatus, and never in a chapter.

**Wendell: it is the Open Up practice.** That places it: `ch3` **Stage 2: Open Up**, which
currently teaches the dial — *"Turn the sensitivity up, and let what's there reach you"* —
and hands the reader no procedure for what to do once the charge is in the body.

**The nearest thing the book already says** is `ch3:956` — *"Open Up: stay there for the
length of an exhale without converting it into a response."* **That is Exhale, the fourth of
the four, arriving without the first three.**

**So the work is: teach WAVE as the four breath actions inside Stage 2, where it belongs.**
That gives Open Up the procedure it lacks and gives the name back its referent.

## 4 · The `Up` convention

**Measured, and it is not a split — it is a heading convention that contradicts the prose.**

| stage | `X Up` in prose | ch3 heading |
|---|---|---|
| Wake | **20** | `Stage 1: Wake` |
| Open | **27** | `Stage 2: Open Up` |
| Clean | **24** | `Stage 3: Clean` |
| Grow | **21** | `Stage 4: Grow` |
| Show | **27** | `Stage 5: Show` |

**The prose is unanimous: all five carry `Up`, 119 times.** Only ch3's five stage headings
drop it, and only for four of the five — `Stage 2: Open Up` keeps it, which is what makes the
set look deliberate when it is not.

**The glossary drops it for all five** — *"Wake, Open, Clean, Grow, Show"* — and is the third
form.

**Ruling wanted: `Wake Up · Open Up · Clean Up · Grow Up · Show Up` everywhere**, which
matches 119 sites of running prose and needs only ch3's four headings and the glossary line
to change. **This is the cheap one and it should go first**, because it is 5 edits against
53 and it removes the reading that started this — five stages that look like variants of
Open Up.

## 5 · Order of work

1. **Normalize `Up` across all five stages.** Five edits: four ch3 headings, one glossary
   line. No rewriting.
2. **Write the WAVE breath practice into `ch3` Stage 2**, from the definition Appendix C and
   Key Terms already carry. New prose, so it runs the full `mtgoa-review` pass.
3. **Convert the 53.** ch3 and ch4 and ch6 first, because those are the practice sections
   where the term is technical. **ch9's seventeen last and by hand**, because they are prose
   about a life rather than references to a form.
4. **Glossary and index.** `WAVE-Spiral` retires as an entry; `WAVE` gets the breath-practice
   entry it has in the retired Key Terms; `Five-Move Form` gets the entry the flow needs.
5. **Re-run `review.py`, `xref.py` and `dupes.py`** after each chapter.

## 6 · What this needs that no instrument provides

**A one-concept-one-name check.** Nothing in `instruments/` asks whether two names refer to
the same thing, which is exactly why a half-finished rename survived four chapters, an
appendix, a glossary and an index. **Worth building after the sweep**, seeded with the pairs
this rename establishes, so the next abandoned conversion is caught in one run rather than by
a reader.
