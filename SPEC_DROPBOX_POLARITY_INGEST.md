# SPEC: Dropbox Polarity Ingestion
## Source: "worldbuilding with wendell" podcast folder

**Purpose:** Ingest and analyze the "worldbuilding with wendell" podcast episodes from Dropbox to understand how polarity mapping is used in Wendell's voice — before writing the Polarity Map tool placement spec.
**Why it matters:** SPEC_BOOK_TOOL_PLACEMENT.md flags Polarity Map as TBD. The strongest voice content for this tool is in these podcasts. We need the source material before we can decide where polarity mapping belongs in the book.
**Status:** BACKLOG — ready to run when Dropbox access is available
**Companion:** `SPEC_BOOK_TOOL_PLACEMENT.md`, `SPEC_MANUSCRIPT_INTEGRATION.md`

---

## Why This Is Needed

The Polarity Map tool is currently TBD in the tool placement spec because:

1. We don't know how Wendell uses it in teaching — only that it's "strongest in voice" in these podcasts
2. We don't know if it's taught as a standalone tool or woven into other practices
3. We don't know if it's a 5-minute tool or a 45-minute facilitation
4. We don't know if it's an ICA-reader tool or a coaching-level tool

Until we ingest and analyze these podcasts, we're speculating. The tool placement spec says "TBD — ingest before placing." This spec is that ingestion.

---

## Source Location

**Dropbox folder:** "worldbuilding with wendell" (or similar — exact folder name to be confirmed in Dropbox inventory)
**File types:** Podcast audio files (mp3/m4a/wav) + any show notes or transcripts
**Known context:** These are Wendell's own teaching episodes — the voice in these recordings is the authoritative source for how he teaches polarity mapping in live settings

---

## What to Extract

For each episode:

1. **The polarity pairs discussed** — what two-pole tensions does Wendell teach?
2. **The teaching arc** — how does he introduce, explain, and practice polarity mapping?
3. **Audience level** — is this ICA-reader level, coaching level, or practitioner level?
4. **Time requirement** — how long does a full polarity mapping exercise take?
5. **Practice structure** — does he use worksheets, verbal prompts, visual diagrams?
6. **Emotional charge** — what is the EA signature of polarity work (what channels does it operate on)?
7. **Integration points** — where does polarity mapping connect to other tools (WAVE, 3-2-1, BARs)?
8. **Wendell's exact language** — capture the phrases he uses to describe polarity to students

---

## Ingestion Protocol

1. **Download** all episodes from the "worldbuilding with wendell" folder via Dropbox
2. **Transcribe** each episode (use `transcribe_audio` for local files, or `save_webpage` if hosted)
3. **Analyze** each transcript using the gm-source-ritual framework (6-face Take/Leave/Map)
4. **Extract** the polarity teaching moments per episode
5. **Synthesize** into a single Polarity Map Voice Document

---

## Output Deliverables

### Deliverable 1: Episode Analysis (one per episode)
- File: `manuscripts/sources/worldbuilding-ww/{episode_slug}.md`
- Content: 6-face analysis of the episode, polarity-specific sections flagged

### Deliverable 2: Polarity Map Voice Document
- File: `manuscripts/sources/worldbuilding-ww/POLARITY_VOICE_DOC.md`
- Content: Synthesis of how Wendell teaches polarity mapping — his exact language, the pairs he uses, the practice structure, the EA signature, the integration points
- This becomes the canonical source for writing the Polarity Map section in the book

### Deliverable 3: Placement Recommendation
- File: `manuscripts/sources/worldbuilding-ww/PLACEMENT_RECOMMENDATION.md`
- Content: Based on time requirement, audience level, and practice structure — where does Polarity Map belong in the book architecture (Alpha/Beta/Gamma/Delta)?
- This feeds back into `SPEC_BOOK_TOOL_PLACEMENT.md` to resolve the TBD

---

## Research Questions to Answer

| Question | Why it matters |
|---------|---------------|
| What polarity pairs does Wendell teach most? | Determines which pairs go in the book |
| Does he teach polarity as a standalone tool or embedded in something else? | Determines if it needs Gamma appendix or can live fully in body |
| Is it a 5-minute self-guided exercise or a 45-minute facilitated process? | Determines Beta (in-book) vs Delta (workbook) |
| What EA channels does polarity work activate? | Determines integration with WAVE-Spiral |
| Does Wendell use diagrams, worksheets, or verbal prompts? | Determines format for in-book presentation |
| Is it for ICA readers or coaching clients? | Determines if it belongs in the front-end book at all |

---

## Spec Dependencies

| Spec | What this delivers |
|------|-------------------|
| `SPEC_BOOK_TOOL_PLACEMENT.md` | Resolves Polarity Map from TBD to Alpha/Beta/Gamma/Delta |
| `SPEC_MANUSCRIPT_INTEGRATION.md` | May add Polarity Map as new integration unit if not already present |
| `SPEC_WORKBOOK_SCOPE.md` | May add Polarity Map to Delta if placement requires workbook component |

---

**Spec status:** BACKLOG
**Created:** 2026-04-22
**Owner:** Wendell Britt
**Blocked by:** Dropbox access confirmation (folder name + file list)
**Unblocks:** `SPEC_BOOK_TOOL_PLACEMENT.md` (Polarity Map row), `SPEC_WORKBOOK_SCOPE.md`