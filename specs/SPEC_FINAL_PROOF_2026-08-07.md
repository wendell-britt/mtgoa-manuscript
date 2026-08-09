# The final proof — spec for the last pass before the book goes out

**2026-08-07. Wendell:** *"another final line and copy edit pass on the book… This is the
final proof before we send it out so we want to make sure we're doing deep reads of each
chapter."*

---

## 1 · What this pass is, and what it is not

The trade splits the work three ways and the distinctions are load-bearing here, because
**this repo has spent months doing one of the three and almost none of the other two.**

| | what it touches | this repo's coverage |
|---|---|---|
| **Line edit** | flow, voice, word choice, rhythm | **saturated.** `prose_diet` (8 counters), `gate`, `marginalia/review.py`, `preempt`, `agency`, `empty_head`, `ranking`, `punchup`, `humor`, `assumed` |
| **Copyedit** | spelling, grammar, punctuation, **consistency**, style-sheet conformance | **almost none** |
| **Proofread** | mechanical and formatting errors on the typeset proof | **none, and it cannot run yet** — it needs the PDF, not the markdown |

**The gap is the copyedit layer**, and the reason is structural rather than negligent: every
instrument in `instruments/` was built to answer *is this voice right*. None was built to
answer *is this the same word we used last time*.

**Proofreading proper is a separate, later job.** *"Proofreading is a meticulous quality
check done on the final, typeset version — often called the proof — not on your manuscript
in a Word document"*, and it verifies page counts, page breaks, running heads and asset
placement. That runs on `build/*.pdf` after this pass lands, and it is not in this spec.

---

## 2 · The finding that justifies the pass

**Four defects surfaced in the first ten minutes of diagnosis, and every one had shipped
past every existing check.**

**A · The book is American and carries British spellings.** Measured: `-ize` 108 against
`-ise` 3 · `honor` 26 / `honour` 0 · `behavior` 22 / **`behaviour` 3**. Seven sites total.
**One of them I wrote into `ch4:370` today** — *Apologising* — and it passed `gate`, all
eight diet counters, the voice linter, `dupes` and `shipcheck` on the way in. Fixed in this
commit; the other six need a ruling, because four sit inside `>` marginalia blocks written
by other hands and British spelling there may be voice rather than error.

**B · Two shipping appendices are never pointed at from the body.** Referenced from
`manuscript/`: A, C, E, F, G, H. **Missing: B and D.** Appendix B is the quests-and-campaigns
workbook — the part the reader is meant to actually run — and Appendix D is the emotional
alchemy practices. Both print. Neither has an on-ramp.

**C · No number policy exists.** `three` runs 77 against numerals in 14 places. Not
necessarily wrong — Chicago spells out under 100 in running prose and uses numerals in
technical contexts — but nothing has ever ruled it, so nothing is consistent by intent.

**D · Stale cross-references are a live failure mode, demonstrated today.** `index_build.py`
still pointed *bliss*, *poignance* and *triumph* at `Ch 7 §2` after ch7's EA table moved to
Section 4, and it would have dropped the `Say the Unsaid Charge` entry entirely on the next
rebuild had the pattern not been updated by hand.

---

## 3 · What the pass produces first: a style sheet

**The book does not have one, and a final proof without one is just opinion applied twice.**
The trade is unanimous on this: a style sheet is *"the book's memory"* — a manuscript-specific
record of every editorial decision, shared with the designer and the proofreader so everyone
applies the same conventions through production.

`specs/STYLE_SHEET.md`, written before any chapter is read, carrying:

1. **Spelling** — US, and the seven `-ise`/`-our` sites ruled individually.
2. **Numbers** — spelled out or numeral, and where the rule flips.
3. **Hyphenation** — a word list. This book compounds constantly: *load-bearing*, *first-tier*,
   *non-renewable*, *body-read*, *self-account*.
4. **Capitalisation of the book's own canon** — the six Faces, the eight daemons, the five
   channels, the four domains, the WAVE stages, the named moves. `ch3` already has a rule here
   (lowercase when telling you to do it, capitalised when naming it) and it is recorded in
   `gate.py`'s comments rather than anywhere a copyeditor would look.
5. **Punctuation** — serial comma, ellipses, quotation marks inside or outside, and the
   em-dash budget which already exists and only ratchets down.
6. **Italics** — what gets them: quoted self-talk, move names, book titles, emphasis.
7. **Names** — every person in every Example, spelled once and checked everywhere.
8. **Cross-reference format** — *Chapter 7* vs *Ch 7* vs *ch7*, and appendix letters.

---

## 4 · The deep read — nine chapters, one at a time

**Mechanical checks run first and are not the pass.** They clear the noise so the read is a
read: `review.py` all steps, plus the four new diagnostics below. Then the chapter gets read
end to end, on paper or in the typeset PDF rather than in the editor, because **the eye that
wrote a sentence cannot proof it in the same window.**

**Per chapter, in this order:**

| | check | how |
|---|---|---|
| 1 | `review.py` clean | existing |
| 2 | spelling variants against the style sheet | new, `copyedit.py` |
| 3 | hyphenation split (*load bearing* vs *load-bearing*) | new, `copyedit.py` |
| 4 | number treatment | new, `copyedit.py` |
| 5 | canon capitalisation | new, `copyedit.py` |
| 6 | every cross-reference resolved — chapter numbers, appendix letters, section numbers, *see* pointers | new, `xref.py` |
| 7 | every name spelled consistently | new, `copyedit.py` |
| 8 | **the deep read** | a human, end to end, once, without stopping to fix |
| 9 | the fixes from the read, applied as a batch with the diff shown first | existing discipline |

**Step 8 is the pass.** Steps 1–7 exist so that step 8 is not spent catching things a regex
could have caught. **Nothing in steps 1–7 substitutes for it**, and the day's evidence is
that the highest-value findings all came from a person reading: *"Not x but y is sneaking
in"*, *"the faces ARE altitudes"*, *"this should've already been ruled on and changed."*

---

## 5 · Two instruments this pass needs and does not have

**`copyedit.py`** — consistency, not quality. Spelling variants, hyphenation splits, number
treatment, canon capitalisation, name spellings. Reports; never gates. Its whole job is *did
we do this the same way last time*, which no existing instrument asks.

**`xref.py`** — every pointer resolves. *Chapter N* exists and says what the sentence claims,
*Appendix X* exists and ships, *Section N* exists after today's ch7 renumber, and the index
and glossary match the body. **This one has already caught something once**, by hand, and
should not have to be run by hand again.

---

## 6 · What this pass explicitly does not do

- **No restructuring, no new argument, no new material.** *"The time for rewrites,
  restructuring, and clarifying your message has long passed."* Anything larger than a
  sentence gets logged, not fixed.
- **No voice work.** That is line editing and it is done. If a diet counter goes heavy
  because of a copyedit fix, the fix stands and the counter gets a note.
- **No page-proof checks.** Page counts, breaks, running heads and widow/orphan control run
  on the built PDF, after this.

---

## 7 · Order

1. Write `specs/STYLE_SHEET.md` and get every open ruling in §2 decided.
2. Build `copyedit.py` and `xref.py`; run both book-wide; fix what is unambiguous.
3. **Deep-read ch1 through ch9 in order**, one chapter per sitting, fixes batched per chapter.
4. Re-run `review.py` and `shipcheck` after each chapter lands.
5. Build the PDF and run the true proofread against it.

**Sources consulted:** [NY Book Editors](https://nybookeditors.com/2016/05/whats-the-difference-between-copyediting-and-proofreading/) · [Reedsy](https://reedsy.com/blog/copy-editing-vs-proofreading/) · [Grammarly](https://www.grammarly.com/blog/writing-process/whats-the-difference-between-copy-editing-and-proofreading/) · [BubbleCow](https://bubblecow.com/blog/book-editing/copy-editing/copy-editing-vs-proofreading-key-differences-explained/) · [ebookpbook on style sheets](https://www.ebookpbook.com/2026/05/25/editorial-style-sheet-book-editing/) · [An American Editor](https://americaneditor.wordpress.com/2015/01/19/thinking-fiction-the-style-sheets-part-i-general-style/) · [DIY MFA copyediting checklist](https://diymfa.com/writing/copyediting-checklist/)
