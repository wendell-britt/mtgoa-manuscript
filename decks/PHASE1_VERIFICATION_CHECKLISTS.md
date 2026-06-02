# Phase 1 — Verification Checklists
## *Per Deliverable Type*

---

## How to Use These Checklists

Run the relevant checklist BEFORE showing the output to Wendell. Check items are **non-negotiable gates** — the output does not go to review until every checkbox is passed. This is not optional. The cost of a broken preview is higher than the cost of taking 2 extra minutes to verify.

---

## Zo Space Page Layout (Primary Mode: Preview)

**Trigger:** Any edit or build of `/ally-deck/preview`, `/ally-deck`, or any card page.

| # | Check | Verify |
|---|---|---|
| 1 | `aspect-ratio: 7 / 5` in code | `grep -n "aspect-ratio" <file>` — must be 7/5, NOT 1/1, NOT 3/2 |
| 2 | 12px border in code | `grep -n "12px\|border-width" <file>` |
| 3 | Image zone present | Visual: `<img src="/images/..."` or placeholder div visible |
| 4 | All three text zones present | Recognition + Move + Bridge all in DOM |
| 5 | Text is readable against background | No black-on-dark, no white-on-white |
| 6 | Suit color correct | Check hex value matches spec for this suit |
| 7 | Route builds clean | `get_space_errors` returns zero errors |
| 8 | Live URL loads | Preview at wendellbritt.zo.space/ally-deck/preview |

**If any checkbox fails: STOP. Fix before showing.**

---

## Image Asset Upload

**Trigger:** Any `update_space_asset` call.

| # | Check | Verify |
|---|---|---|
| 1 | Source file exists | `ls /home/workspace/Images/<filename>` |
| 2 | File is non-zero | `wc -c <file>` returns non-zero |
| 3 | Asset path confirmed | `grep "asset_path" <call>` matches expected `/images/...` |
| 4 | Asset listed after upload | `list_space_assets` shows the asset |
| 5 | Image renders on page | View the live page, image visible |

**If any checkbox fails: STOP. Re-upload before proceeding.**

---

## Card Data / Content Changes

**Trigger:** Any edit to card text, card order, or card metadata.

| # | Check | Verify |
|---|---|---|
| 1 | Source file saved to obsidian | File exists in vault, `wc -c` non-zero |
| 2 | Zo route data updated | `get_space_route` shows updated content |
| 3 | No text truncation | No `...` mid-sentence in live output |
| 4 | Recognition + Move + Bridge all present | All three components visible in preview |
| 5 | Card count correct | `grep -c "rank:" <file>` returns expected count per suit |

**If any checkbox fails: STOP. Fix before showing.**

---

## New Route Creation

**Trigger:** Any `write_space_route` call.

| # | Check | Verify |
|---|---|---|
| 1 | Route path confirmed | `/ally-deck/xxx` — correct slug |
| 2 | Code compiles | `get_space_errors` returns zero errors |
| 3 | Live URL loads | Navigate to the URL |
| 4 | Route visible in route list | `list_space_routes` shows the path |
| 5 | Route code saved to obsidian | File in `ZOSPACE_ROUTES/` with `wc -c` non-zero |

**If any checkbox fails: STOP. Fix before showing.**

---

## Design Decisions (Preview-Layout Related)

**Trigger:** Any design decision that was not explicitly confirmed by Wendell.

| # | Check | Verify |
|---|---|---|
| 1 | Decision documented | Written to relevant spec file or noted in obsidian |
| 2 | 3 alternatives considered | At least 2 other options were named and dismissed |
| 3 | Intent stated explicitly | "I'm choosing X because Y — correct?" sent to chat |
| 4 | If unsure: draft mode | Flagged as DRAFT, not shown as final |
| 5 | If wrong: admit without performance | "You're right — I was building what I thought you wanted, not what you asked for" |

**If checkbox 1-3 fail: document before showing. If checkbox 4-5 apply: admit before showing.**

---

## When the User Asks to Review

Before saying "live" or "done" or "here's the preview":

| # | Check | Verify |
|---|---|---|
| 1 | All applicable checkboxes passed above | Run the relevant checklist |
| 2 | Known issues flagged | "Here are the things I still need to verify" — not silent |
| 3 | No false confidence | Say "here's what I built" not "here's what you wanted" |
| 4 | Image check | If images are involved, image must be visible on live page |

**If any checkbox fails: do not say "live." Fix first.**

---

## The Checklist Keeper

Before closing any turn where I built something:

```
Checklist run: [YES / NO]
- [x] aspect-ratio: 7/5
- [x] route builds clean
- [x] image visible
- [x] text all present
- [ ] [any failures flagged here]
```

If I don't write this, the output is not verified.

---

## Spec Status

**Phase 1 active.** These checklists are the gate before review. They do not prevent creativity — they prevent the 7-mistake pattern.
