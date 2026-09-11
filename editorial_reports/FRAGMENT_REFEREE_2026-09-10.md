# One fragment counter

**Ratified 2026-09-10** as step 2 of the instrument reconciliation (revised ruling after the hostile
review; the original cast was seed 7243). Its terms: core `fragment.py` becomes the one fragment
counter; its false positives are fixed in core first, reading the sites gained and lost; the index
leaves the scan through the manifest's `exclude:`; the gate's counter retires and its boxed and
anchor notes move to the ledger. **Your ban stands. Only the counter changes.**

Branch `editorial/trailing-and-onto-proof-2026-09-10`, on top of `7ae7dec`.

---

## Result

Measured with editorial-core **v32** installed over a clean copy of this commit, every site
counted (repeats included, ledger set aside for the comparison).

| | before (`7ae7dec`, core v31) | after |
|---|---|---|
| **fragment** | 251 | **54**: 16 ledgered (your ruling), 38 unresolved |
| trailing_and · telling · polysyndeton · slop_shapes · light_verb | 88 · 198 · 15 · 47 · 51 | unchanged at every location |
| Flirtcraft, AI Psychologist (all six scanners) | | **unchanged**: v32 moves nothing in either book |

One slop_shapes site moved from `headmasters_letter.md:3` to `:4`. It is the same sentence: the
`<!-- LETTER -->` comment on line 3 used to be joined into the paragraph below it.

## What the 197 removed sites were

Every site the change removed was listed. The 148 outside the index were read one by one and
sorted by cause, with nothing left over; the 49 index entries leave as a file, by the ruling. None
of them is a sentence.

| cause | sites | fixed in | examples |
|---|---|---|---|
| whole-line HTML comment | 61 | core `find_line` | `<!-- SECTION 3 -->`, `<!-- LETTER -->` |
| label in emphasis | 64 | core `fragment` | `**Alchemy 1 — Anxiety → Curiosity**`, `**The method:**`, the glossary's `*Ch 3 §4*` pointers, `**POLE A** ←——●——→ **POLE B**`, `**Wendell Britt**` |
| index entries | 49 | this manifest, `exclude:` | `**clearance** — Key Terms, **Ch 2 §7**, …` |
| `'s` after a pronoun | 17 | core `fragment` | *That's the price.*, *It's avoidance with better vocabulary.* |
| verbs the tagger only calls nouns | 4 | core `fragment` | *Your chest tightens.*, *None of them installs by repetition.* |
| phrasal imperative | 1 | core `fragment` | *Hand over the pen.* |
| provenance the build strips | 1 | core `find_line` + this `build_book.nonprinting` | *De-somatized per the no-somatic-prescription directive.* |

**The provenance fix is wider than fragment.** Seven appendices open with `**Status:**`,
`**Authority:**` and `**Location in book:**` lines that `build_book.strip_provenance` removes before
typesetting. Every core instrument scanned those 19 lines as prose. `build_book.py` now answers the
core's `nonprinting(lines)` with the same rule `strip_provenance` applies, checked line for line
against it: 19 lines, 0 mismatches. On this branch the fix removed one fragment and no other hit.

**My first label rule was wrong, and reading the removed sites caught it.** It tested only a run's
first and last characters. A glossary entry opens on a bold term and closes on an italic pointer,
so three real fragments inside entries disappeared (*The Protector's last resort.*, *Carolyn
Elliott's term.*, and the Channels entry). A label now also has no sentence boundary inside it, and
all three are counted again.

## The gate's counter, retired

It came from the product voice kit on 2026-09-01. Its finite-verb test counted any word of four
letters or more ending in -s or -ed as a verb. That let `this`, `days`, `words` and `exchanges`
clear real fragments: *Four words each, no explanation.*, *Three exchanges at minimum.* (six
sites), *Not this one, not yet, not from me.* It read 0 on the prose where `fragment.py` reads 251.
The core selftest now has a case for exactly that hole.

Its notes, one by one:

- **28 boxed notes**, all covering fragment hits and nothing else. The 16 boxed fragments core v32
  finds are now ledger notes in `editorial_exceptions.yaml`, **ledgered (your ruling)** under the
  boxed-records ruling, with that ruling's text as the reason. `BOXED_NOTES` is empty, and the
  mechanism stays for any other counter's hit inside a box.
- **Voice anchor 3** (*At framing a boundary as a preference rather than a line.*). `fragment.py`
  does not flag it: *framing* is a verb in the book's lexicon. No entry needed.
- **Ten form lines of Devon's sample sheet** (Appendix H). The sheet is a blockquote, and the core
  never scans a blockquote as prose. No entries needed.

`test_toolchain.py`'s six probes of the retired counter are replaced by one check that the gate
carries no fragment counter.

## The 38 unresolved fragments

These are real: sentences with no verb. They go to the zero pass with the other four instruments,
where each is rewritten or ledgered. Grouped for that pass:

- **Three exchanges at minimum.**, six times, one per chapter's practice section (ch3–ch8).
- **Colon lead-ins to a list**, six: *Two concrete examples:*, *The Skeptic's five:*, *The
  Fixer/Healer's:*, *The Emotional Body's five:*, *The structure:*, *The Victim's:*.
- **Label-and-value lines ending in a full stop**, three: *Formula: …*, *Total: 1-2 hours.*,
  *Source: Igniting Joy (Wendell Britt).*
- **Glossary definitions**, three (listed above).
- **Appendix H's checkbox row** (`○ Shaman · ○ Challenger · …`). The zero pass has to answer
  whether a row of options on a form counts as prose. Nothing in this step decided it.
- **The rest**, nineteen, eighteen in the chapters and *Thirteen lines.* in Appendix H: *Years of
  them.*, *Your actual ones.*, *Small ones first. Then larger ones.*, *Endless revisions. Infinite
  drafts.*, *(Yes, already.* and others.

`(Yes, already.` at ch1:60 was documented in `fragment.py` as a splitter false positive. Read in
context (*"(Yes, already. You just walked in and I'm handing you homework. Stay with me.)"*) it is
a whole verbless sentence, and the docstring now says so.

## Corrections to earlier reports

**`--keys` lists a repeated sentence once, at its first location.** A per-location comparison built
on it cannot see a repeated sentence turning up somewhere new. Step 1's comparison was built that
way. It was re-run on every site with `allsites.py` (in `editorial-core/replay/`): still **zero
locations rose** on any of the six scanners between `55edd24` and `7ae7dec`. The step-1 report is
corrected to say how it was measured.

## Not done here, and why

- **The branch's own book board has no fragment check until step 3.** `review.py` runs
  `fragment.py` on drafts but not book-wide, and the book-wide check was the gate's counter. Step 3
  installs core v32 and hand-merges `review.py`, which must wire `fragment` as a target.
- **MTGOA's gate still prints no `EDITORIAL` line**, so the zero check cannot read it. Step 3.
- **The voice kit's copy of the retired counter** (`export/voice-kit/tools/voice_lint.py`) has the
  same -s/-ed hole, and the product repos run it. Flagged as its own task.
- **Core v32 is not committed.** It lives in `editorial-core/` in The Library, with its
  `releases.yaml` entry and a selftest of 25/25. It is committed after the PR, as ruled.
