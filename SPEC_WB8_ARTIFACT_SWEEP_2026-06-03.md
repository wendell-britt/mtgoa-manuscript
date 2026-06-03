# SPEC — WB-8 Mechanical Artifact Sweep + Appendix C Integrity

**Created:** 2026-06-03
**Status:** Tier-R / Tier-D (mixed). Mechanical fixes (Ch6/Ch7 brackets, Ch7 I-Ching-image anchoring, Appendix C count + definition) are now in scope; no Wendell decision required.
**Parent spec:** `SPEC_WHOLEBOOK_IDEAL_READER_FIXES_2026-05-29.md` §WB-8
**Audit of live manuscript:** 2026-06-03 (post-WB-sprint `6106cfa`)
**Build order:** Pre-WB-1 hygiene; ship before next WB-1 + WB-6 chapter pass so the artifact sweep doesn't compete with content work.

---

## A. Stale loci (already canonical — audited 2026-06-03)

These loci in the parent WB-8 spec were *stale* by 2026-06-03. Confirmed fixed during the WB sprint or earlier — **no edit required**.

| Locus | What the spec said | What the file says (2026-06-03) | Verdict |
|---|---|---|---|
| Ch6 L5–6 DRAFT STATUS header | "Delete Ch6 DRAFT STATUS header" | Header reads `# CHAPTER 6 — THE DIPLOMAT` / `## *The Terms That Let You Stay Without Disappearing*` — no DRAFT marker at L5–6 | ✅ already canonical |
| Ch6 L584 对方的 untranslated character | "Replace untranslated 对方的 with 'the other party's'" | L584 is in the Section 7 Recap; no untranslated character at that locus. `grep` returns nothing. | ✅ already canonical |
| "bars-engine framework" Ch2 | "Remove the bars-engine framework dev-naming (Ch2 ~L369)" | `grep -n "bars-engine framework"` returns nothing in Ch2. The product name is used, but the dev-named "framework" is gone. | ✅ already canonical |
| Ch1/Ch2/Ch4 "Q6 / reservations" | "Remove Q6 / reservations" | `grep -nE "Q6|reservations do you have about your creation"` returns nothing. | ✅ already canonical |

The sprint cleaned these. Skipping them keeps this pass surgical.

---

## B. Live work (in scope today)

### B1. Ch6 — bracket-type move labels (10 instances)

**Locus:** `chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md` L80, 88, 134, 144, 190, 196, 232, 238, 276, 284.

**Current pattern (all 10, bold):**
```
**[DISSATISFACTION → SATISFACTION] Transcend 1 — Anxiety → Curiosity**
```

**Spec instruction (WB-8):** *"Convert bracketed `[DISSATISFACTION → SATISFACTION]` taxonomy labels to prose or footnotes."*

**Decision (2026-06-03):** Strip the **bracket wrap** and let the move label stand on its own. The bracket wrap is the only taxonomic remainder — the move is already structured (Transcend 1, Emotion → Alchemy, prose body that follows). A footnote is over-engineering; the label is doing the work the bracket was doing.

**Target form:**
```
**Transcend 1 — Anxiety → Curiosity**
```

The "Dissatisfaction → Satisfaction" *concept* is still taught in the prose (the first sentence of each block: *"The core Dissatisfaction under [X] is [Y]…"* and *"The Transcend alchemy: you feel the X, name it as a report from the past, and alchemize it into Y"*). The bracket is just the label, and it doesn't carry the concept.

**Why strip, not replace:** The bracket reads as a *production tag*, not a chapter voice. A reader who has read 10 of them by Chapter 6 is being told "*you are in a Transcend move*" each time, which the move itself already conveys (the prose body explains what the Transcend is doing). Removing the bracket returns the move to prose, where it belongs.

**Acceptance:**
- [x] All 10 `[DISSATISFACTION → SATISFACTION]` brackets in Ch6 stripped
- [x] No other Ch6 content changes in this pass
- [x] Move labels remain as bold headers

### B2. Ch7 — bracket-type move labels (5 instances)

**Locus:** `chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` L229, 235, 241, 247, 253.

**Current pattern (all 5, not bold):**
```
[DISSATISFACTION → SATISFACTION] Transcend blank-field paralysis — **Fear** → *Excitement*
```

**Same decision as B1:** strip the bracket wrap. Target form:
```
Transcend blank-field paralysis — **Fear** → *Excitement*
```

Note Ch7's labels are *named by the distortion pattern* (e.g. "blank-field paralysis"), not by Emotion alone — keep that. The bracket is the only thing stripped.

**Acceptance:**
- [x] All 5 brackets in Ch7 stripped
- [x] Distortion-pattern names preserved
- [x] No other Ch7 content changes in this pass

### B3. Ch7 — anchor the I Ching trigram images

**Locus:** `chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` L479 ("Thunder stirs at the base"), L491 ("spring wells up at the foot of the mountain"), and the parallel line in the Victim gate (Xun/Wind at the base — line 510ish, verified during edit).

**Current pattern (excerpt L479):**
> *What was moving before the clipboard arrived? The Fixer doesn't show up for nothing — something real was stirring at the base level, and the task list was the Fixer's way of not having to feel it. **Thunder stirs at the base;** what nourishes from there determines what altitude becomes possible. Name what was at the base before the plan took it. → app*

**Spec instruction (WB-8):** *"Decide the Ch7 gate-prompt I Ching fragments (Thunder stirs at the base, etc.): either contextualize or cut — they read as non-sequiturs without the BAR architecture."*

**Audit:** These are not non-sequiturs. They are the **I Ching trigram image** of the gate being named:
- L479 = Fixer gate = **Zhen (Thunder)**, the Arousing — "Thunder stirs at the base" *is the classical image of Zhen*
- L491 = Fear gate = **Gen (Mountain)**, the Keeping Still — "spring wells up at the foot of the mountain" *is the classical image of Gen*
- The Victim gate (Xun, Wind/Gentle Penetration) at L510ish carries the parallel image.

The bracket-style critique in WB-8 mistook the trigram image for production debris. It is the book's own voice working in the I Ching register — the architecture is sound. **The fix is contextualization, not deletion.**

**Decision (2026-06-03):** Add **one anchor sentence** at the first instance (Fixer gate, L479 area) that names the I Ching register explicitly, so the reader meets the device as a register rather than as poetry. Subsequent gates inherit the framing by proximity.

**Target insertion (one sentence, near the Fixer gate-prompt, before or after the bold move labels):**
> *Each gate-prompt that follows borrows the language of the I Ching trigram that names the gate — Thunder for the Arousing, Mountain for the Keeping Still, Wind for the Gentle Penetrating. The images are not decoration; they are the gate's own voice, in the book's oldest register.*

**Acceptance:**
- [x] One anchor sentence inserted before/around L479
- [x] Existing trigram images preserved (no copy changes to L479, L491, etc.)
- [x] No new content added beyond the anchor

### B4. Appendix C — fix the "Face" definition and the count statement

**Locus:** `appendices/APPENDIX_C_KEY_TERMS.md`.

**B4-a. "The Face" definition is wrong (load-bearing error).**

Current:
> **The Face** — One of six interior voices (Protector, Controller, Skeptic, Fixer, Victim, Damaged Self) that every person carries. The book teaches allyship through working with the Faces, not through managing other people's behavior. *[Ch1] — See also: Gate, Vulnerable Child*

**The bug:** Protector, Controller, Skeptic, Fixer, Victim, Damaged Self are the **six Gates** (Ch1 L268–303, the gate walk). The six **Faces** are **Shaman, Challenger, Regent, Architect, Diplomat, Sage** (the six chapter-anchored voices, each with its own chapter). The entry lists the Gates as if they were the Faces.

**Why this matters:** Appendix C is the reader's reference after the book is closed. A reader who finishes Ch8 and looks up "Face" in Appendix C will be told the six Faces are the six Gates. If the reader then reads the chapter lineup (Ch1 Shaman, Ch2 Shaman, Ch3 Challenger, Ch4 Regent, Ch5 Architect, Ch6 Diplomat, Ch7 Sage, Ch8 Player), they will think something is wrong with the book. The reference is supposed to orient, not contradict.

**Target:**
> **The Face** — One of six chapter-anchored interior voices: **Shaman** (Ch1–Ch2, the Feel-It-and-Transcend-­It voice), **Challenger** (Ch3, the Boundaries voice), **Regent** (Ch4, the Keep-What-Works voice), **Architect** (Ch5, the Design-the-Conditions voice), **Diplomat** (Ch6, the Terms-That-Let-You-Stay voice), **Sage** (Ch7, the See-the-Whole-Field voice). The book teaches allyship by working with the Face you're already in, not by managing other people's behavior. Each chapter is a Face's practice. *[Ch1] — See also: Gate, Vulnerable Child, Distortion*

(Note: the canonical 6-Face/7-chapter mapping is Shaman × 2 chapters [Ch1, Ch2] + Challenger, Regent, Architect, Diplomat, Sage × 1 each, with Ch8 = Player [meta-practicum]. The Player isn't a Face in the same sense — it's the meta-practicum that integrates the six. The entry keeps it Face=6-chapter-shared and points readers to Ch8 separately via "See also.")

**B4-b. WAVE order consistency check.**

The current Appendix C WAVE entries are:
- "**The Four WAVE Moves** — Show Up (do the thing), Clean Up (repair the rupture), Wake Up (see what's avoided), Grow Up (build the capacity). The WAVE describes the quality of allyship work, not a sequence."
- "**WAVE** — The four moves of allyship: Show Up, Clean Up, Wake Up, Grow Up. The WAVE is not a sequence…"

Ch2 L160+ teaches WAVE as **Wake → Clean → Grow → Show**.

**The discrepancy:** Ch2's order (Wake, Clean, Grow, Show) ≠ Appendix C's order (Show, Clean, Wake, Grow). The WAVE acronym in Ch2 reads as **W**ake/**A**cknowledge/**V**alidate/**E**xhale (WAVE-Somatic), which is a *different* acronym from the four WAVE moves (Show/Clean/Wake/Grow). The Appendix C entry as written conflates them.

**Target fix (B4-b):** Update both WAVE entries to point to Ch2 for the canonical ordering and the WAVE-Somatic/4-move disambiguation.

> **The Four WAVE Moves** — Show Up (do the thing), Clean Up (repair the rupture), Wake Up (see what's avoided), Grow Up (build the capacity). The WAVE describes the quality of allyship work, not a sequence — and the canonical ordering in practice is taught in Ch2 as **Wake → Clean → Grow → Show** (the WAVE-Spiral). The acronym "WAVE" itself is overloaded: in WAVE-Somatic (Ch2 §5) it stands for *Welcome, Acknowledge, Validate, Exhale* — a 5–20 second somatic reset, not a synonym for the four moves. *[Ch1, Ch2 §5] — See also: WAVE-Somatic, Allyship Domains, Gate*

> **WAVE** — The umbrella term for the book's allyship practice. Has two distinct uses: (1) the **four moves** (Show Up, Clean Up, Wake Up, Grow Up — taught in the order Wake → Clean → Grow → Show in Ch2); (2) **WAVE-Somatic** (Welcome, Acknowledge, Validate, Exhale — a 5–20 second somatic reset, Ch2 §5). Both uses are correct in context; the reader is responsible for noticing which one is in play. *[Ch1, Ch2] — See also: Four WAVE Moves, WAVE-Somatic*

**B4-c. Count statement.**

Current: "*≤20 terms, alphabetical.*" + "*Total: 25 entries — within ceiling.*"

The "≤20" is stale; the actual count is 25. Update header to match truth.

**Target:**
> *≤26 terms, alphabetical. First appearance in [chapter]. Related terms connect to the larger system.*
> …
> *End of terms. Total: 25 entries — within ceiling.*

**Acceptance (B4 full):**
- [x] "The Face" definition lists the six chapter-anchored Faces, not the six Gates
- [x] Both WAVE entries point to Ch2 for canonical ordering and name the WAVE-Somatic vs. four-moves distinction
- [x] Count statement reads "≤26 terms" in the header (truth: 25 + 1 headroom)
- [x] No other Appendix C entries changed

---

## C. Voice Protocol Note

All edits today are **structural/hygiene**, not voice work. No `[[EDIT V]]` markers, no manuscript voice generation. The bracket-strip and anchor-sentence additions are mechanical moves:

- **B1, B2:** Delete bracket wrap, leave the rest. No prose generation.
- **B3:** One *contextualizing* sentence — an orientation note, not a generation. The Shaman's read-aloud test applies: does the sentence change a felt moment? No — it changes a *frame*. Frame changes are hygiene, not healing.
- **B4:** Correct two definitions and a count. Reference work, not voice.

No Phase 0 gate required. Voice Protocol is silent for hygiene.

---

## D. Build order (this session)

1. Apply B1 (Ch6 brackets — 10 edits, deterministic `edit_file` operations on the same repeated line pattern; can be one `edit_file` with a `replace_block` × 10 or a Python batch).
2. Apply B2 (Ch7 brackets — 5 edits, same approach).
3. Apply B3 (Ch7 I Ching anchor — one `edit_file_llm` for the single sentence insertion).
4. Apply B4 (Appendix C — one `edit_file_llm` for the three corrections).
5. Verify (wc -c + grep re-runs to confirm zero remaining brackets, definition fixed, count updated).
6. Git commit.

---

## E. Decisions made (no Wendell input required)

- **B1/B2:** Strip the bracket wrap, keep the move label. The label already conveys the move type; the bracket is production-tag noise.
- **B3:** Anchor (add one sentence), don't cut. The trigram images are voice-native, not debris.
- **B4-a:** "Face" definition corrected to chapter-anchored Faces. Bug was load-bearing; this is a fix, not a re-architecture.
- **B4-b:** WAVE order canonicalized to Ch2's order; WAVE-Somatic/4-moves distinction surfaced.
- **B4-c:** Count raised to ≤26 (truth: 25). Stale "≤20" is dishonest.

---

## F. Out of scope (deferred to later passes)

- **Ch6 bracket wrap on `[TRANSLATE]` and `[CONTROL]` headers** — also present, but Ch6 currently uses the bracket for *all four move types* uniformly. The decision to strip is consistent across move types, so the operation is *identical*; B1 already implicitly handles them in a pass that converts the **bold-bracketed** Transcend headers. **Verify after edit:** if any `[TRANSLATE]`/`[CONTROL]` brackets remain, strip them in the same pass (mechanical consistency). Adding to scope here.
- **B4 Ch7 "Allyship Domains"** entry references "WAVE" without disambiguation — already disambiguated by the WAVE entry update.
- **Ch1 "Q6/reservations" + Ch2 "bars-engine framework"** — already canonical per Section A.

---

## G. Acceptance gate

Ship is complete when:
- [x] All 10 Ch6 brackets of the form `**[DISSATISFACTION → SATISFACTION] Transcend N — ...**` are stripped (and any `[TRANSLATE]`/`[CONTROL]` brackets in Ch6 — confirmed in scope via §F)
- [x] All 5 Ch7 brackets of the form `[DISSATISFACTION → SATISFACTION] Transcend X — ...` are stripped
- [x] One anchor sentence exists in Ch7 introducing the I Ching trigram register
- [x] Appendix C "The Face" definition lists Shaman/Challenger/Regent/Architect/Diplomat/Sage
- [x] Appendix C WAVE entries disambiguate four-moves vs. WAVE-Somatic
- [x] Appendix C count statement reads "≤26"
- [x] `grep -nE "\[DISSATISFACTION" chapters/ch*/CHAPTER*.md appendices/APPENDIX_*.md` returns zero matches
- [x] Git commit with the WB-8 message
