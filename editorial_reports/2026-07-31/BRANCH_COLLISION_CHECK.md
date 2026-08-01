# Branch collision check — 2026-07-31

Run before applying any prose fix from this pass. The July precedent is the
reason: two branches ran book-wide passes over the same nine files and conflicted
across **91 hunks**, and `MANUSCRIPT_FILE_CANON.md` ruled the lesson —
*land apparatus and prose on separate branches, or sequence the sessions.*

## The state, measured

`origin/master` was **force-updated** during this session, from `00431e8` to
`625aaab`. That is now our merge-base and master's head simultaneously, so master
has not moved ahead of us: **0 commits on master that we do not have.**

| Branch | Commits ahead of master | `manuscript/` files | Active |
|---|---|---|---|
| **ours** — `claude/editorial-system-book-integration-umo641` | 7 | **0** | today |
| `claude/mtgoa-manuscript-changes-swmp78` | 26 | **8** | **today** |
| `claude/book-print-readiness-august-ar95mo` | 98 | 0 | — |
| `codex/book-eod-draft-2026-06-09` | 80 | 0 | — |
| `simplify-draft-2026-06-08` | 66 | 0 | — |
| `claude/mtgoa-marginalia-frame` | 54 | 0 | — |
| `claude/print-apparatus-off-master` · `say-the-noun-off-master` · `self-sabotage-ally-beliefs-a9lhzu` | 0 | 0 | merged |

**This branch touches no shipping surface.** 16 files, 3,749 insertions, **zero
deletions**, every file new — nothing in `manuscript/`, `appendices/`,
`front_matter/`, `back_matter/`, or `marginalia/`.

## The one live branch, and it is working today

`claude/mtgoa-manuscript-changes-swmp78` shares our merge-base (`625aaab`) and
committed five times today, editing `manuscript/ch1.md`–`ch8.md` — 328
insertions, 39 deletions — seating worked Examples in ch3–ch7 and running a
citation audit.

**File-level overlap with this branch: none.** Verified by set intersection.
Both merge into master cleanly:

```
git merge-tree $(git merge-base origin/master HEAD) origin/master HEAD     # 0 conflicts
git merge-tree $(git merge-base HEAD $SWMP78) HEAD $SWMP78                 # 0 conflicts
```

## What that branch has already fixed — do not duplicate

**A7 is closed there.** They found the same uncredited source independently and
wrote a fuller entry than a bare credit, naming the disagreement:

> `ON_THE_SHOULDERS_OF.md` — "**Ichiro Kishimi and Fumitake Koga's *The Courage
> to Be Disliked*** (Atria Books, 2018)… Chapter 3 quotes one line from it before
> departing from it… That is a change rather than a refinement and the change is
> mine, so the disagreement belongs on this page."

Their `specs/AUDIT_CITATIONS_2026-07-31.md` also found three things our pass did
not: **four Appendix G credits pointing at sources that appear nowhere in the
book**, two missing attributions on pages built on the thing being attributed,
and **three attributions sitting above ch8's seam, in a Head's mouth**, where
`SPEC_TWO_HANDS` says credit cannot go.

## What neither branch has fixed

**P0 survives on both.** The testimony slot is present on swmp78 at `ch7:501`
(it is `ch7:467` here — the line drift is theirs), and both ch1 placeholders are
intact there. Two independent sessions worked these files today and neither
caught it, which is the argument for `instruments/placeholders.py` rather than a
reading pass.

## Line numbers in this directory are against master, not swmp78

swmp78 adds 328 lines across ch1–ch8, so every citation in these reports drifts
against that branch. Example: the testimony slot is `ch7:467` here and `ch7:501`
there. **Re-anchor by searching the quoted text, never by applying an offset** —
the offset is not constant. Every flag in this pass carries its quotation for
exactly this reason.

## Where our planned fixes would land

| Fix | Target | Overlap with swmp78 |
|---|---|---|
| **A2** — six sheet lines | immediately before `## Section 7` in ch3–ch8 | **none.** Section 7 headings untouched on that branch; its last ch8 hunk ends at old line 527, Section 7 begins at 669 |
| **A4** — cut the colours | `ch8:183`, `213`, `223`, `297`, `307`, `327` | **one.** `ch8:213` is rewritten there — *"Wilber makes the structural point:"* → *"The structural point is that"*, moving the Wilber credit into a new attributions paragraph. The colour content is unchanged, the opening clause is not |

A4 also needs re-reading against that branch for a second reason: they **deleted
the Big Mind/Shamanic/Faces attribution paragraph** that sat directly below the
passage this report named as the golden-monkey replacement, and replaced it with
a longer attributions paragraph higher up.

## Ruling

**This branch stays apparatus-only.** No prose fix from this pass gets applied
here while swmp78 owns `manuscript/`. It merges into master today with zero
conflicts and zero risk, because it adds files rather than editing them.

The prose fixes go one of two ways, and both are sequencing rather than
parallelism:

1. **Merge this branch first** — it is pure addition — then apply A2/A4 on the
   branch that already owns the chapters, with these findings in hand. Preferred.
2. Hand the six drafted sheet lines and the A4 site list to swmp78 to apply.

What is not available is applying them here while that branch is live. That is
the 91-hunk shape, and the repo has already paid for it once.
