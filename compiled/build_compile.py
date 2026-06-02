#!/usr/bin/env python3
"""
Build the Tier-R-only compiled review manuscript.

Per SPEC_COMPILED_MANUSCRIPT_REVIEW_2026-05-29.md:
- Derived surface. Never writes back to canonical files.
- Applies ONLY Tier-R edits (mechanical / locked line swaps), wrapped in [[EDIT R]] markers.
- Drops Tier-U gaps as [[EDITORIAL NOTE — UNRESOLVED]] inline at chapter level.
- Tier-D drafts are EXCLUDED from this build (folded in later as written).
- Appendices A-E represented (A,C prose; B,D,E placeholders w/ design summaries).
- Emits provenance header, tier legend, TOC, and a closing Pending-Edit Ledger.

Regenerate: python3 build_compile.py
"""
import os, re, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
APPX = os.path.join(ROOT, "appendices")
BUILD_DATE = datetime.date.today().isoformat()
SRC_COMMIT = "1881622"

CHAPTERS = [
    ("Chapter 0 — The Infinite Arcade",        "chapters/ch0-infinite-arcade/CHAPTER0_DRAFT.md"),
    ("Chapter 1 — The Forest (Shaman Threshold)", "chapters/ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md"),
    ("Chapter 2 — The Shaman",                  "chapters/ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md"),
    ("Chapter 3 — The Challenger",              "chapters/ch3-CHALLENGER/CHAPTER3_CHALLENGER_FULL_DRAFT.md"),
    ("Chapter 4 — The Regent",                  "chapters/ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md"),
    ("Chapter 5 — The Architect",               "chapters/ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md"),
    ("Chapter 6 — The Diplomat",                "chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md"),
    ("Chapter 7 — The Sage",                    "chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md"),
    ("Chapter 8 — The Player",                  "chapters/ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md"),
]

# --- Tier-R edits: (file_key, find, replace, edit_id, desc) ---------------
# Each find MUST match exactly once or the build fails loud.
TIER_R = {
    "chapters/ch0-infinite-arcade/CHAPTER0_DRAFT.md": [
        (
            "You can tell yourself you were doing your best. That is true. It is also not enough.",
            "You can tell yourself you were doing your best. That is true. [[EDIT R: Ch0 P1-1 — drop \"not enough\" (inner-critic catchphrase)]]It is also not where the game is played.[[/EDIT]]",
            "Ch0-P1-1a", 'Ch0 line ~323: "not enough" -> "not where the game is played"'
        ),
        (
            "those were your calls. You made them. You will make more. Now you have to make them on purpose.",
            "[[EDIT R: Ch0 P1-1 — forward-tense the indictment (open an action, not indict the past)]]those are your calls. You're making them now, and you'll make more. The only question is whether you make them on purpose.[[/EDIT]]",
            "Ch0-P1-1b", "Ch0 line ~281: past-tense indictment -> forward-tense"
        ),
        (
            "(Some players in the Arcade earn a special currency — Vibeulons — when they complete quests or finish practices. We'll talk about those later. For now, the ticket is simpler: what are you spending, and what are you actually earning back?)",
            "[[EDIT R: Ch0 P2-2 — cut \"Vibeulons\" (coined product-word punctures register / reads as upsell)]](For now, the ticket is simpler: what are you spending, and what are you actually earning back?)[[/EDIT]]",
            "Ch0-P2-2", "Ch0 line ~167: remove Vibeulons parenthetical"
        ),
    ],
}

# --- Tier-U editorial notes, keyed by file (emitted at chapter head) -------
TIER_U = {
    "__global__": [
        "Issue 2 — Wendell voice not yet applied to manuscript prose (infra built, no edits made).",
        "Issue 10 — Somatic poetics / Council of Joanne's / comedic calibration specs complete, awaiting Wendell session.",
        "Issue 11 — Shame-parasite ontology defined, not yet integrated into manuscript.",
    ],
    "chapters/ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md": [
        "Issue 3 — Ch1 oracle-card revision pass (Image text + appendix routing) deferred.",
    ],
    "chapters/ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md": [
        "Issue 3 — Ch2 oracle-card revision pass deferred.",
    ],
    "chapters/ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md": [
        "Issue 16 — Ch4 polarity encounter merge (architecture approved, implementation gated).",
    ],
    "chapters/ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md": [
        "Issue 5 — Eight-gates structure begins risking repetition from here through Ch7 (no design solution chosen).",
    ],
    "chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md": [
        "Issue 15 (Ch6) — Integrative Negotiator (Channel 5) voice pass deferred.",
        "Issue 16 — Ch6 Move 3 merge (architecture approved, implementation gated).",
    ],
    "chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md": [
        "Issue 12 — Ch7 confession (\"A Note Before the Exile\") voice pass pending (Tier-D; not in this build). NB: in-file flag not found 2026-05-29 — locus to confirm.",
        "Issue 5 — Eight-gates repetition most acute by this chapter.",
    ],
    "chapters/ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md": [
        "Issue 6 — Ch8 does not yet integrate the Six Faces.",
    ],
}

def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()

def wc(text):
    return len(re.findall(r"\S+", text))

def apply_tier_r(key, text, ledger):
    for find, repl, eid, desc in TIER_R.get(key, []):
        n = text.count(find)
        if n != 1:
            raise SystemExit(f"BUILD FAIL: edit {eid} matched {n} times in {key} (need exactly 1).\nText: {find[:80]}...")
        text = text.replace(find, repl, 1)
        ledger.append(("R", eid, key, desc))
    return text

def chapter_edits_summary(key):
    ids = [eid for (_, _, _, eid, _) in [(None,)*5]]  # placeholder
    applied = [e[2] for e in []]
    return [d for (_, _, _, d) in [(0,0,0,0)]]

out = []
ledger = []  # (tier, id, locus, desc)

# header
out.append("# MASTERING THE GAME OF ALLYSHIP — COMPILED REVIEW BUILD")
out.append("")
out.append(f"> **DERIVED SURFACE — NOT CANON.** Built from canonical chapter files. "
           f"Never write this file back to source. Canon lives in Obsidian under Wendell's approval.")
out.append(">")
out.append(f"> **Build date:** {BUILD_DATE}  |  **Source commit:** {SRC_COMMIT}  |  **Build tier:** Tier-R only")
out.append(">")
out.append("> **Tier legend:** "
           "`[[EDIT R: ...]] … [[/EDIT]]` = Ready edit applied (mechanical/locked). "
           "`[[EDITORIAL NOTE — UNRESOLVED]]` = Tier-U gap flagged in place. "
           "Tier-D (draftable) edits are **excluded** from this build and folded in later as drafted.")
out.append("")
out.append("---")
out.append("")

# global unresolved notes
out.append("## Whole-Book Unresolved Notes (apply across all chapters)")
out.append("")
for note in TIER_U["__global__"]:
    out.append(f"- `[[EDITORIAL NOTE — UNRESOLVED]]` {note}")
    ledger.append(("U", "global", "all chapters", note))
out.append("")
out.append("---")
out.append("")

# build chapters, collecting TOC data
toc = []
body = []
for title, key in CHAPTERS:
    raw = read(key)
    edited = apply_tier_r(key, raw, ledger)
    words = wc(raw)
    applied_ids = [eid for (find, repl, eid, desc) in TIER_R.get(key, [])]
    toc.append((title, words, applied_ids))
    body.append("")
    body.append("═══════════════════════════════════════════════════════════════")
    body.append(f"> _source: `{key}` | words: {words:,} | "
                f"edits applied: {', '.join(applied_ids) if applied_ids else 'none'}_")
    body.append("═══════════════════════════════════════════════════════════════")
    body.append("")
    # chapter-level unresolved notes
    for note in TIER_U.get(key, []):
        body.append(f"`[[EDITORIAL NOTE — UNRESOLVED]]` {note}")
        ledger.append(("U", key.split('/')[-1], title, note))
    if TIER_U.get(key):
        body.append("")
    body.append("───────────────────────────────────────────────────────────────")
    body.append("")
    body.append(edited.strip())
    body.append("")

# TOC
out.append("## Table of Contents")
out.append("")
total = 0
for title, words, ids in toc:
    total += words
    flag = f"  _(edits: {', '.join(ids)})_" if ids else ""
    out.append(f"- **{title}** — {words:,} words{flag}")
out.append(f"- **Appendix A** — Four Allyship Domains (prose)")
out.append(f"- **Appendix B** — Quests + Campaigns  `[NOT YET WRITTEN]`")
out.append(f"- **Appendix C** — Key Terms (prose)")
out.append(f"- **Appendix D** — EA Practices  `[DRAFT PENDING]`")
out.append(f"- **Appendix E** — Bibliography  `[NOT YET WRITTEN]`")
out.append("")
out.append(f"_Total chapter prose: ~{total:,} words._")
out.append("")

# splice body
out.extend(body)

# appendices
def appendix_block(title, path=None, placeholder=None):
    blk = []
    blk.append("")
    blk.append("═══════════════════════════════════════════════════════════════")
    if path:
        words = wc(read(path))
        blk.append(f"> _source: `appendices/{os.path.basename(path)}` | words: {words:,}_")
    else:
        blk.append(f"> _status: placeholder_")
    blk.append("═══════════════════════════════════════════════════════════════")
    blk.append("")
    if path:
        blk.append(read(path).strip())
    else:
        blk.append(placeholder.strip())
    blk.append("")
    return blk

out.append("")
out.append("# APPENDICES")
out.extend(appendix_block("Appendix A", path=os.path.join(APPX, "APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md")))
out.extend(appendix_block("Appendix B", placeholder=(
    "# Appendix B — Quests + Campaigns\n\n"
    "`[NOT YET WRITTEN — Issue 13]`\n\n"
    "**Planned content** (per `docs/plans/2026-05-21-appendix-design.md`): "
    "8 chapter quests (one per face chapter) + 4 domain campaigns "
    "(Gather Resources, Skillful Organizing, Direct Action, Raise Awareness). "
    "Routes reader from gate/mode identification into a concrete next action sequence."
)))
out.extend(appendix_block("Appendix C", path=os.path.join(APPX, "APPENDIX_C_KEY_TERMS.md")))
out.extend(appendix_block("Appendix D", placeholder=(
    "# Appendix D — EA Practices\n\n"
    "`[DRAFT PENDING — Issue 13]`\n\n"
    "**Planned content:** Happy Apples, Grounding, The Rose — three Emotional Anatomy practices "
    "drafted from the IJ source; needs Wendell review. (Draft to be located/folded in a later build.)"
)))
out.extend(appendix_block("Appendix E", placeholder=(
    "# Appendix E — Bibliography\n\n"
    "`[NOT YET WRITTEN — Issue 13]`\n\n"
    "**Planned content:** Full source list (Maslach, Gorski, Chou, Watts, Carse, Elliott, Jung, Wilber, "
    "Wilhelm/Baynes I Ching, et al.). Needs Wendell pass."
)))

# ledger
out.append("")
out.append("═══════════════════════════════════════════════════════════════")
out.append("# PENDING-EDIT LEDGER (audit)")
out.append("═══════════════════════════════════════════════════════════════")
out.append("")
out.append("| Tier | ID | Locus | Description |")
out.append("|---|---|---|---|")
for tier, eid, locus, desc in ledger:
    d = desc.replace("|", "\\|")
    out.append(f"| {tier} | {eid} | {locus} | {d} |")
out.append("")
out.append(f"**Tier-R edits applied:** {sum(1 for r in ledger if r[0]=='R')}  |  "
           f"**Tier-U notes flagged:** {sum(1 for r in ledger if r[0]=='U')}")
out.append("")
out.append("_Tier-D (draftable) edits are NOT in this build. See "
           "`SPEC_COMPILED_MANUSCRIPT_REVIEW_2026-05-29.md` §6 for the full inventory._")

result = "\n".join(out)
outpath = os.path.join(os.path.dirname(__file__), f"MTGOA_COMPILED_{BUILD_DATE}.md")
with open(outpath, "w", encoding="utf-8") as f:
    f.write(result)

print(f"WROTE {outpath}")
print(f"  total words in compile: {wc(result):,}")
print(f"  Tier-R edits applied:   {sum(1 for r in ledger if r[0]=='R')}")
print(f"  Tier-U notes flagged:   {sum(1 for r in ledger if r[0]=='U')}")
