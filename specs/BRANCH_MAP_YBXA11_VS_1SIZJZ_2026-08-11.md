# Two final proofs, forked from the same commit

**Opened 2026-08-11**, after *"this is the 3rd time we've tried and remove those production
tags and they keep coming back"* turned out to have an answer bigger than the tags: **the final
proof was run twice, on two branches, and neither knows about the other.**

| | `claude/book-pdf-epub-production-ybxa11` | `claude/mtgoa-final-proof-1sizjz` |
|---|---|---|
| commits since fork | **12** | **41** |
| last commit | 2026-08-11 | 2026-08-10 |
| words vs fork | **+584** | **−5,498** |
| pages claimed | — | **404 → 398 → 382pp, trade + workbook + EPUB, board green** |

**Both forked from `62128b8`** — the merge of PR #15, *Prep the final proof*, 2026-08-08. Neither
is a subset of the other and neither is stale.

---

## 1 · Only on this branch (ybxa11) — 11 files

**Everything here is either the `WAVE` rename or a document.**

| file | | what |
|---|---|---|
| `appendices/APPENDIX_C_FIVE_CHANNELS.md` | 7+/7− | rename |
| `appendices/APPENDIX_E_321_SHADOW_PROCESS.md` | 6+/6− | rename, plus the four-vs-five movements repair |
| `back_matter/glossary.md` | 9+/3− | `WAVE-Spiral` retires; `Five-Move Form` and `WAVE` get entries |
| `back_matter/index.md` | 3+/1− | rename |
| `instruments/index_build.py` | 19+/6− | the one-regex-two-practices split, and `WAVE` made case-sensitive |
| `instruments/glossary_check.py` | 3+/3− | rename |
| `marginalia/insertions.py` | 1+/1− | anchor repaired after a heading rename |
| `specs/SPEC_WAVE_RENAME_2026-08-07.md` | +130 | doc |
| `specs/AMENDMENT_FORM_METAPHOR_2026-08-11.md` | +215 | doc |
| `specs/DEEP_READ_BRIEF_2026-08-11.md` | +205 | doc |
| `specs/DEEP_READ_FINDINGS_2026-08-11.md` | +281 | doc |

## 2 · Only on 1sizjz — 25 files

**Almost none of it is replayable. It is hand-ruled cuts, judgment calls, instruments and a
built book.**

**Manuscript, untouched here:**

| | | |
|---|---|---|
| `manuscript/ch7.md` | 99+/112− | **the 23 production tags stripped**, the `Section 3`/`Section 4` pointer fixed, the EA table rows resolved, 1,326 words cut |
| `manuscript/ch8.md` | 35+/69− | 987 words cut |
| `manuscript/ch5.md` | 19+/25− | 63 words cut |

**Instruments we do not have:**

| | | |
|---|---|---|
| `instruments/gate.py` | +21 | **the `prodtag` hard fail** — the only version of the tag fix that survives a merge |
| `instruments/proofread.py` | +278 | the true proofread, which this branch has as an unstarted task |
| `instruments/build_pdf_ebook.py` | +346 | |
| `instruments/build_sample.py` | +228 | |
| `instruments/copyedit.py` | +23 | **`rigour` and `programme` added to `BRITISH`** |
| `instruments/book/devices.lua`, `mtgoa.typ`, `build_book.py` | +37 | stranded pseudo-headings made sticky |

**`AGENTS.md` +44/−1** — **the tag template at line 92 replaced.** This is where the tags
regenerate from, and this branch still ships it.

**Specs and artifacts:** `LOG_FINAL_PROOF_2026-08-09.md` (+1,311) · `CUTS_ARCHIVE_2026-08-09.md`
(+393) · `SPEC_TIER2_SURGERY` · `PROPOSAL_CUTS` · `HANDOFF_ANNOUNCE_2026-08-10` ·
`front_matter/cover.png` · a seven-file `export/voice-kit/` including a 239-line `voice_lint.py`.

## 3 · Touched by both — 7 files, the whole conflict surface

| file | ybxa11 | 1sizjz |
|---|---|---|
| `manuscript/ch3.md` | 41+/33− | **37+/107−** |
| `manuscript/ch9.md` | 17+/15− | **32+/74−** |
| `manuscript/ch4.md` | 2+/2− | 31+/59− |
| `specs/STYLE_SHEET.md` | 25+/8− | 103+/12− |
| `manuscript/ch1.md` | 1+/1− | 6+/6− |
| `manuscript/ch2.md` | 2+/0− | 5+/5− |
| `manuscript/ch6.md` | 1+/1− | 7+/7− |

**ch3 and ch9 are the real collision** and the reason is dated, not textual — see §4.

**One task was done twice.** Both branches wrote Appendix B and D on-ramps.

> **1sizjz `04a4c58`**, the terse italic pointer, matching `ch3:463`'s existing convention:
> *"Eight quests, one for each chapter of the walk, and four campaigns you can run with other
> people: Appendix B: Quests & Campaigns."*
>
> **ybxa11 `0ddda3f`**, body prose that argues for opening it now: *"Quest 1 belongs to this
> chapter and takes a week… a quest you save for after the last page becomes homework."*

**1sizjz's is the safer one**, because ybxa11's *homework* argument collides head-on with
Appendix B's own opening line (*"What follows isn't homework and it isn't a recap"*), which is
`DEEP_READ_FINDINGS` §2c.

## 4 · The decisive fact: 1sizjz predates the whole `WAVE` rename

**Measured, both sides:**

| | ch3 | ch4 | ch6 | ch9 |
|---|---|---|---|---|
| **1sizjz** `WAVE-Spiral` | **15** | 1 | 1 | 0 |
| **1sizjz** `WAVE` | 17 | 2 | 1 | 12 |
| **1sizjz** `Five-Move Form` | **0** | 0 | 0 | 0 |
| **ybxa11** `WAVE-Spiral` | 0 | 0 | 0 | 0 |
| **ybxa11** `Five-Move Form` | 13 | 1 | 1 | 3 |

1sizjz also still carries the pre-normalisation headings — `#### Stage 1: Wake`, `Stage 3:
Clean` — and has no martial-arts passage anywhere.

**So merging 1sizjz into this branch naively puts `WAVE-Spiral` back into ch3 fifteen times.**
That is the identical failure mode as the production tags, one level up: **a merge taking the
wrong side of a file whose other side was already fixed.** `485d004` did exactly this to ch7 on
2026-08-07 — one parent at 0 tags, one at 23, resolved to 23.

**Thirteen of 1sizjz's changed lines in ch3 and ch9 contain `WAVE`**, so this cannot be resolved
by taking one side per file. It needs the rename re-derived on top of the cut text.

## 5 · The two deep reads cross-validate, and they are complementary

Both branches ran a deep read, three days apart, neither able to see the other.

| | ybxa11 (nine readers, findings only) | 1sizjz (`a300987` + `37dec18`, 24 fixes applied) |
|---|---|---|
| ch7's 23 production tags | found | **fixed** |
| ch7:705 stale `Section 3` pointer | found | **fixed** |
| `rigour`, `programme` | found | **fixed, and added to `copyedit.py`** |
| `per cent` (`ch8:764`) | **found** | missed |
| `ch8:272` *at Red* | **found** | missed |
| `ch4:651` *forty seconds later* | **found** | missed |
| `the spiral` ×5 | **found** | missed |
| `APPENDIX_B` wrong daemons ×5 | **found** | missed |
| `APPENDIX_F` four pairs for six chapters | **found** | missed |
| glossary: no `Architect`, no `Controller` | **found** | missed |

**Two independent reads found `rigour` and `programme` at the same two sites.** That is the
strongest confirmation available that both passes were real reads.

**Neither read is redundant.** 1sizjz applied 24 fixes and shipped a build; ybxa11 produced ~30
blocking findings that 1sizjz's pass did not reach, none of them applied yet.

## 6 · Which direction the merge goes

**1sizjz is the base. ybxa11 replays onto it.** The asymmetry is not about which branch is
better — it is about which work can be redone.

**1sizjz's work is largely irreplayable:** 5,498 words of hand-ruled cuts across six chapters,
a 24-fix deep read, a page-count campaign protocoled to 382pp, four new instruments, a cover
and a built EPUB. Redoing any of it means re-making judgment calls that were already made once
with the reasoning archived in `CUTS_ARCHIVE` and `LOG_FINAL_PROOF`.

**ybxa11's work is largely replayable:** the `WAVE` rename is a deterministic sweep with a
documented site list in `SPEC_WAVE_RENAME`; the martial-arts frame is three new passages that
apply cleanly to cut text; the four spec documents are pure additions that cannot conflict.

**The one thing that must not be replayed mechanically** is the rename's site list. 1sizjz's
cuts removed five of ch9's seventeen `WAVE` sites, so the sites must be re-derived against the
cut text rather than replayed from the commits.

**Three items on this branch need re-deciding rather than replaying**, all from
`DEEP_READ_FINDINGS` §2 and all authored 2026-08-11:

1. **`ch3:286`** contradicts `ch3:300`. 1sizjz's ch3 has neither passage and its own cuts pass
   over that section.
2. **`ch9:388`** contradicts `ch8:904`. 1sizjz cut ch9 by 1,168 words including, per `a669032`,
   *"two coaching offers"* — **which is `DEEP_READ_FINDINGS` §4 R7 already ruled and applied.**
   The ch9 close must be rewritten against the cut text, not ported.
3. **The Appendix B on-ramp** — take 1sizjz's version, per §3.
