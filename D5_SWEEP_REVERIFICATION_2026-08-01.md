# D5 — Re-verifying the signed-off sweeps against what actually ships

**Created:** 2026-08-01
**Ordered by:** `specs/SPEC_BRACKET_TAGS_2026-07-29.md` §D5 — *"WB-8 was one artifact sweep that was verified in the wrong tree. Nothing has re-run it against `manuscript/`."*
**Scope of this pass:** WB-8 and `SPEC_WHOLEBOOK_IDEAL_READER_FIXES_2026-05-29.md`. Eleven extractable claims.

---

## Method — and the correction it needed

The obvious scope is *"re-run the checks against `manuscript/`."* That is still too narrow. WB-8's Appendix C items target a file that has since been retired from the book; they are neither passing nor failing, they describe something no reader will ever see.

**The correct scope is the ship manifest** — the 22 components `instruments/build_book.py` actually assembles. A claim about a file outside it cannot be a defect no matter what it says.

---

## Result

| spec | claim | verdict |
|---|---|---|
| WB-8 B1 | 10 brackets in the Diplomat stripped | **pass** — but only since 2026-08-01 |
| WB-8 B2 | 5 brackets in the Sage stripped | **pass** — fixed by someone, undated |
| WB-8 B3 | I Ching trigram register anchored in the Sage | **unverifiable** |
| WB-8 B4a | Appendix C "The Face" definition lists the six Faces | **moot** |
| WB-8 B4b | Appendix C WAVE entries disambiguate | **moot** (recorded as a pass by a faulty check — see below) |
| WB-8 B4c | Appendix C count reads "≤26 terms" | **moot** |
| WB-8 gate | no brackets anywhere that ships | **pass** |
| IR p98 | a "two readings" beat appears before any major framework | **FALSE — live defect** |
| IR p99 | it is framed as a reusable test | **FALSE — same defect** |
| IR p100 | the Sage retains a callback version | **pass** |

**One live defect. Two dead ends. Seven fine.**

---

## The live defect — a callback with no original

`SPEC_WHOLEBOOK_IDEAL_READER_FIXES_2026-05-29.md` signs off three linked claims. The third is true and the first two are not, which is the worst possible combination.

**What ships, at `manuscript/ch8.md:117`:**

> You just read a story about someone who sees clearly and gets exiled for it… **You know this test by now. You've taken it since the first page.** Take it again here, where it cuts sharpest.

**What the reader has actually taken:** nothing. The two-reading structure — *"Read it first as this… The second reading…"* — appears in the entire shipped book **only in ch8, lines 117–127**. Its first appearance is the sentence claiming she has been doing it for eight chapters.

The spec's own p98 locates the original in "Ch0, between Build Your Character + The Reader's Oath" — today's ch1. It is not there, under that phrasing or any other.

**Why this is worse than the dead cross-reference cleared out of ch7 today.** A dead pointer sends the reader somewhere useless. This one tells her something false *about herself* — that she possesses a skill and a history she was never given. A reader who believes the book concludes she was not paying attention.

**This is a claim error, the category currently topping the ship board at 16.**

### The fix is a choice, not a mechanic

- **A — write the original.** Add the two-readings beat to ch1 where the spec always said it went, before any framework is taught. Honours the design; costs new prose in the book's most load-bearing chapter.
- **B — rewrite the claim.** Change ch8:117 so it introduces the test rather than recalling it. Cheap, honest, and loses the payoff the spec was reaching for — the recognition arriving after eight chapters of practice.

**A is the better book and B is the safer edit.** Wendell's call.

---

## The two dead ends, and why neither is a defect

**B3 — the trigram anchor.** WB-8 asked for a sentence anchoring "existing trigram images" at "L479, L491" in the Sage chapter. Searched today: **zero** occurrences of *trigram*, *I Ching* or *hexagram* in `manuscript/`, and **zero** in the retired `chapters/` tree. The images the anchor was written to introduce have never existed in git. The item was signed off against content in neither tree — most likely an Obsidian-era draft that never migrated.

Nothing to fix. Recorded so nobody re-opens it.

**B4a/b/c — Appendix C.** All three target the Key Terms glossary. `build_book.py` does not reference `APPENDIX_C_KEY_TERMS.md`; Appendix C is now `APPENDIX_C_FIVE_CHANNELS.md`. The file still sits in `appendices/`, unshipped, alongside a backup of itself.

**A faulty check inside this audit, recorded because the point of D5 is that checks lie.** B4b was initially scored *pass* by testing `APPENDIX_C_FIVE_CHANNELS.md` for the string `WAVE-Somatic`. It is there, for unrelated reasons, in a different Appendix C than the one WB-8 was describing. A check pointed at the wrong file produced a green result — which is precisely the failure this audit exists to find, reproduced by the audit on its first pass.

---

## Four failure modes, not one

D5 was opened on the assumption of a single defect: *verified against the wrong tree*. There are four, and they need different guards.

| # | mode | instance | catchable by grep? |
|---|---|---|---|
| 1 | verified against a parallel tree | the brackets | yes, if scoped to the ship manifest |
| 2 | target retired after sign-off | Appendix C ×3 | only if the checker knows the manifest |
| 3 | claim about content that never existed | the trigram anchor | no — nothing to search for |
| 4 | **half the fix shipped** | two readings | **no** |

**Mode 4 is the dangerous one.** The callback landed and the original did not. Any check asking *"does the callback exist?"* returns green, and the green is what makes the book wrong. Only a check that verifies both halves of a relocation catches it — and no such check existed, because the sweep that performed the relocation is the same document that certified it.

---

## Recommendations

1. **Decide A or B on the two-readings defect.** It is a claim error in shipped prose.
2. **Point every future acceptance gate at the ship manifest**, never at a directory. `build_book.py` already holds the list; a gate that does not read it is guessing.
3. **A relocation claim must assert both ends.** *"Ch7 retains a callback"* is half a check. The other half — *"and ch1 still has the original"* — is the one that would have caught this in May.
4. **Continue D5.** This pass covered 2 sweeps and 11 claims. Still unaudited: `SESSION_WORK_INVENTORY_20260420.md` (10), `SPEC_6_SABOTAGING_BELIEFS.md` (2), `wb1_drafts/CH4_FIRST_MOVE.md` (7), and the `decks/` verification checklists (4). The `PHASE2A*` reports are database migrations and out of scope for the book.

---

*Audit complete for WB-8 and the whole-book ideal-reader fixes. One live defect found, awaiting a ruling. Two items closed as unfixable-and-harmless. The audit's own first pass reproduced the bug it was written to find.*
