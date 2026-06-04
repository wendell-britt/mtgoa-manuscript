# Ch4 WB-1 First Move — Apply Pending

**Status:** WAITING ON TOOLING.
**What this is:** Note only. No code generated. Apply from a fresh tooling context (Claude / Codex / future session with reliable `write_file`).

## What's needed

Apply the WB-1 First Move to `chapters/ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md`.

- **Current file:** 51,794 bytes, 7 sections, Section 6 ends ~L612, Section 7 opens L653.
- **Insert point:** between Section 6 close and Section 7 header.
- **Pattern:** same as the Ch1/Ch2/Ch3/Ch5/Ch6/Ch7/Ch8 First Move sections.

## Source content

- **Spec-style draft** (full): `wb1_drafts/CH4_FIRST_MOVE.md` (5,204 bytes)
- **Assembled prose draft** (this is the one to apply): see "Prose section" below

## Prose section to insert

```markdown

## THE FIRST MOVE -- Ch4

Before the recap, one conversation. Within seven days.

The Regent's game is chosen loyalty -- the inheritance you hold, and the reformation you've decided to make, and the willingness to name both out loud to the person whose standing is affected. The honest-terms conversation is the move. There is a relationship in your life -- a parent, a sibling, a co-founder, a long-time colleague, a partner in a project you didn't start -- where you have been carrying an inheritance. You know what you've decided to keep from how it was done. You know what you've decided to change. The person across from you doesn't know either, because you haven't said it. The inheritance is being run on autopilot -- the institution survives, the choice does not.

Pick the person. Pick one specific thing you are keeping and one specific thing you are doing differently. Then have the conversation, in person or on a call -- text doesn't count, because the inheritance is held in the room and the terms are heard in the voice. The sentence is short: *I want to tell you what I am keeping from how we did this, what I am doing differently, and ask whether that is okay with you.* Then listen. The conversation lasts twenty minutes, maybe less.

The test. **Reading one:** you named both sides and the person across from you heard it as a *choice*, and something in the relationship changed because the inheritance stopped being invisible. **Reading two:** you named both sides and the person across from you heard it as accusation, and the next morning the distance in the relationship was a relief. The distance is not the read. The relief is not the read. The read is whether the inheritance became *yours* in the room, or stayed a thing you were either keeping or leaving. Reading one is ownership. Reading two is a clean break disguised as a clean keep.

I drafted a long passage about chosen loyalty this year and then realized I had not said the terms out loud to the people I am actually inheriting from. I was writing the move instead of making it. The most Regent failure is editing the chapter about the inheritance instead of having the conversation. I am still having it.

*The person. What you said you were keeping. What you said you were doing differently. What they said back. The part where you noticed you were performing the reform instead of doing it. The surprise is usually in the part where the other person wanted something you had not named. -> app*

```

## Acceptance criteria

- [ ] The prose block above is inserted between Section 6 close and `## Section 7: Recap and Transition`
- [ ] The chapter is L2-verified after the write (`safe_write.py write <path> <content> L2`)
- [ ] File size delta: +1,343 chars (the prose body) plus 6 chars of leading/trailing whitespace handling
- [ ] Idempotency: before writing, confirm `## THE FIRST MOVE -- Ch4` is NOT already in the chapter (avoid double-insert)
- [ ] No regression on existing WB-12 de-obligate work in Section 6
- [ ] No regression on Codex's 2026-06-04 `fd05db3` WB-9 altitude submerge (Ch4 should already reflect that)

## Related: same task for Ch5, Ch6, Ch7

The Ch5, Ch6, Ch7 First Move drafts ARE full-prose drop-in (have `## THE FIRST MOVE -- Ch{N}` header). They were going to be applied via the same inserter script `/tmp/wb1_insert.py` (which has a known LLM-placeholder-path bug for Ch6/Ch7 — fix by replacing `ch6-...` and `CHAPTER6_...` with the real values below before running).

Real values for the CHAPTERS list:
- `ch5-ARCHITECT`, `CHAPTER5_ARCHITECT_FULL_DRAFT.md`, `CH5_FIRST_MOVE.md`
- `ch6-diplomat`, `CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md`, `CH6_FIRST_MOVE.md`
- `ch7-sage`, `CHAPTER7_SAGE_FULL_DRAFT.md`, `CH7_FIRST_MOVE.md`

**Note on Ch7:** the chapter's structure changed when Codex removed the 8-gate walk (commit `6341df6`). The First Move prose content is still applicable (independent of the 8-gate structure) but the **I Ching-image anchor** (added in WB-8 commit `7f14a96`) is now orphaned. **I Ching cross-book decision is needed before re-adding the anchor.** See `SPEC_COORDINATED_REAPPLY_2026-06-04.md` for the four open options (keep / drop / relocate / hybrid).
