# SPEC -- WB-1 + WB-8 Reapply Pass (after parallel Codex session)

**Created:** 2026-06-04
**Status:** REAPPLIED -- committed, awaits Wendell review and Obsidian promotion.
**Trigger:** Codex session ran in parallel 2026-06-04 (commits `b8a4ad1`, `9ce47cb`, `b39f60d`, `c837f1a`, `b28ee00`, `4ce37e0`) and clobbered the line-level WB-1 / WB-8 work I had committed on 2026-06-03 (`80859db`, `7f14a96`).
**Scope:** Steps 1, 2, 3, 4, 6, 7 of the original reapply plan. Step 5 (Appendix C integrity) was scoped out and queued for Wendell's adjudication per his 2026-06-04 instruction.

---

## A. What Codex did that affected our work

| Codex commit | What it touched | What it clobbered |
|---|---|---|
| `b8a4ad1` Ch3+Ch4+Ch6 promote | Ch3, Ch4, Ch6 | Ch3 First Move removed; Ch6 brackets re-added (23) |
| `9ce47cb` Ch7+Ch8 promote | Ch7, Ch8 | Ch7 brackets re-added (5) + I Ching anchor removed; Ch8 First Move upgrade removed |
| `b39f60d` Ch5 promote | Ch5 | (no WB-1/WB-8 work) |
| `c837f1a` Ch2 | Ch2 | (no WB-1/WB-8 work) |
| `b28ee00` Appendix C | Appendix C | The Face def, both WAVE entries, Distortion def all reverted |
| `4ce37e0` Laloux footnotes | Ch0, Ch2 | (no WB-1/WB-8 work) |

Codex's structural rewrites (energy-ecology vocabulary, Five Modes of Sight in Ch7, altitude-language submerge) were kept. The line-level edits we made were *not* preserved because they fell below the line-resolution of Codex's full-chapter rewrites.

## B. What was reapplied

1. **Ch1 WB-1 First Move upgrade** (two-readings reframe + author-shadow disclosure, ~1188 chars). Inserted between "The body that did the reading was yours the whole time" and the BAR prompt. ✅
2. **Ch3 WB-1 First Move** (full section, 16 lines, "30-second protocol promoted to chapter spine"). Inserted between Section 6 close and Section 7 open. ✅
3. **Ch8 WB-1 First Move upgrade** (2022 chars appended after "That's where the walk begins" and before Section 7). ✅
4. **Ch6 WB-8 bracket strip** (23 labels stripped: 10 Alchemy N + 2 Translate N + 2 Control N + 4 Translate sub-titles + 5 Control sub-titles). All 23 brackets replaced with clean `**Alchemy N -- X -> Y**` or `**Translate -- From X to Y**` headers. ✅
5. **Ch7 WB-8 bracket strip** (5 inline labels stripped). The "**Fear** -> *Excitement*" emotion/alchemy suffix preserved per WB-10/EA standard. ✅

## C. What was NOT reapplied (per Wendell's instruction)

- **Appendix C integrity** (Step 5) -- queued. Codex reverted all three of our fixes (The Face def, both WAVE orderings, Distortion def). Reapplying without adjudication risks re-introducing a conflict with Codex's vocabulary choices. Awaiting Wendell.

## D. Open question on Ch7 (separate from reapply scope)

Codex's restructure of Ch7 removed the 8-gate walk and replaced it with 5 "Alchemy Moves" (See, Switch, Serve, Release, Return). This means the **Ch7 First Move draft** I wrote (name altitude, stay in room) is still *applicable* -- the content is independent of the 8-gate structure -- but the I Ching anchor I added in WB-8 is now orphaned (no gate-walk to anchor to). Decision needed: (a) keep the I Ching anchor in a different form, (b) drop it, (c) extend it as a trigram-image note in the new Alchemy Move structure.

## E. Commit

Single commit for the whole reapply pass. See `git log --oneline -3`.

## F. Coordination rule (logged to AGENTS.md learn)

When two agents work in parallel on the same manuscript without a coordination protocol, line-level edits below the chapter-rewrite threshold are lost. Future parallel work must:
1. One agent claims a chapter at the chapter-rewrite grain (full chapter file)
2. Other agent works at the line-edit grain only after claiming specific lines
3. Pre-rewrite snapshot: capture file SHA256 before and after each chapter-level commit
4. Reconciliation pass after both complete: diff the parallel commits and re-apply any lost line-edits

This is the lesson; the implementation is the AAR.
