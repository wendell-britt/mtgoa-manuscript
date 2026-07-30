# MTGOA export — 2026-07-28

Snapshot of the working manuscript and toolchain out of the Claude session container.
Book ships 2026-08-01.

## manuscript/

The nine chapter files. This is the book. 97,013 words of body text.

Re-measured 2026-07-30, frame stripped, whitespace-split. The 97,738 total this
file carried was a true figure at `e662f84`, before the register fan-out. The
fan-out and the W8/W9 passes then cut 1,245 words and this file was never re-run.
`specs/SPEC_EMDASH_AND_DENSITY_2026-07-29.md` documents the decline.

| File | Words |
|---|---|
| ch1.md — The Infinite Arcade | 7,461 |
| ch2.md — The Forest | 7,193 |
| ch3.md — Shaman | 15,237 |
| ch4.md — Challenger | 11,042 |
| ch5.md — Regent | 8,859 |
| ch6.md — Architect | 9,771 |
| ch7.md — Diplomat | 12,307 |
| ch8.md — Sage | 13,086 |
| ch9.md — The Player | 12,057 |

**Not written, and both are hard print blockers:** Appendix — The Polarity Map
(closes open references at ch3:623, ch4:148, ch5:188, ch6:151, ch7:121) and
Appendix — The 3-2-1 Shadow Process (closes ch3:456, ch3:593, ch4:374, and
carries the book's only Wilber credit). Front matter, TOC, and back matter
are also unwritten.

## instruments/

Python measurement tools. `spec_edit.py` is the safe-edit pattern every
manuscript edit goes through — it aborts and writes nothing on a missed or
duplicated anchor. `dupes.py` is the cross-chapter duplicate scanner; run it
on new prose before insertion. The reviewer gate itself is documented in
`specs/MTGOA_INSTRUMENTS_TOOLKIT.md`.

Every number quoted about this manuscript should come out of these, run
against the chapter files. Planning documents have been wrong.

## specs/

`MANUSCRIPT_FILE_CANON.md` — which files are the book, which are stale.
The three open specs each end in a rulings section still awaiting Wendell.

## visuals/

Built HTML. Self-contained, no external assets.

## drafts/

Working prose not merged into any chapter. `appendix_channels.md` and
`ch9_transfer_drill.md` are finished pieces; the rest are partial.
