# MANUSCRIPT FILE CANON — read this before editing any chapter

**Last synced: 2026-07-28. Book ships 2026-08-01.**

## Where the book actually is

The nine chapter docs below are the manuscript. Each one carries a STATUS header stamped with its sync date and word count. Edit these, and write edits back to the same path.

| Ch | Project doc | Words |
|---|---|---|
| 1 | `claude/CHAPTER1_DRAFT.md` | 7,527 |
| 2 | `claude/CHAPTER2_FULL_DRAFT.md` | 7,187 |
| 3 | `claude/CHAPTER3_SHAMAN_FULL_DRAFT.md` | 15,096 |
| 4 | `claude/CHAPTER4_CHALLENGER_FULL_DRAFT.md` | 11,093 |
| 5 | `claude/CHAPTER5_REGENT_FULL_DRAFT.md` | 8,820 |
| 6 | `claude/CHAPTER6_ARCHITECT_FULL_DRAFT.md` | 9,835 |
| 7 | `claude/CHAPTER7_DIPLOMAT_FULL_DRAFT_MASTER.md` | 12,818 |
| 8 | `claude/CHAPTER8_SAGE_FULL_DRAFT.md` | 13,292 |
| 9 | `claude/CHAPTER9_PLAYER_FULL_DRAFT.md` | 12,070 |

Book total: 97,738 words.

**There is no git repository.** The project is the only durable store. Working sessions pull these docs down to `ch1.md` through `ch9.md` in an ephemeral container and edit there, and those working files vanish when the session ends. **Any session that edits a chapter must sync it back to the project doc above before it finishes.** A chapter edited only in a session container is a chapter that was not edited.

The cheap way to sync, which never puts the chapter text into context:

```
project_write(path="claude/CHAPTER3_SHAMAN_FULL_DRAFT.md", local_path="ch3.md")
```

Do **not** `project_read` a full chapter doc unless the text genuinely has to be in context. It returns inline and costs tens of thousands of tokens.

## The rest of the durable set

- `claude/MTGOA_INSTRUMENTS_TOOLKIT.md` — the reviewer gate, the safe-edit pattern, the duplicate scanner, and the measurement instruments (practice surfaces, chain check, stylometry, term debt, negation stacks, repetition sweep, construction sites). Paste an instrument into a file and run it against `ch1.md`–`ch9.md`. Every claim about this manuscript should come from one of these, not from a planning document.
- `claude/visuals/` — the built HTML visuals: `CHAPTER_ENGINE`, `CH2_SEVEN_DAEMONS`, `CH3_PROCESS_SHAPE`, `STRUCTURAL_DELIVERY`, `REGISTER_REMEDIATION`, `STRUCTURE_COMPARISON`, `VOICE_COMPARISON`.
- The three open specs: `claude/SPEC_STRUCTURAL_DELIVERY_2026-07-28.md`, `claude/SPEC_REGISTER_REMEDIATION_2026-07-28.md`, `claude/SPEC_REPETITION_AND_CUTS_2026-07-28.md`. Each ends in a rulings section that is still awaiting Wendell.
- Unmerged working drafts, kept because their prose is not in any chapter: `claude/CH3_REBUILD_WORKING_DOC.md`, `claude/CH4_SECTION5_REBUILD.md`, `claude/CH2_LINE_LEDGER_65_SITES.md`, `claude/SOURCE_TEXT_COMPARISON_CHOU_ELLIOTT.md`.

## Docs that are stale and will mislead you

These describe the book as it was, not as it is. Do not plan from them without checking the claim against the chapter docs above.

- `EDITING_PLAN.md` — its ICA Journey Map uses obsolete 8-chapter numbering, off by one against the current nine.
- `CHAPTER_TEMPLATE_GUIDE.md`, `claude/DAEMON_CANON.md`, `claude/ArgumentMap.md`, `claude/MTGOA_OUTLINE.md`, `DAEMON_ARCHITECT_CONSISTENCY_CHECK_2026-07-15.md` — carry the retired 8-gate walk, the retired four-stage sequences, and the retired "jeppi" naming.
- `claude/MTGOA_CROSS_BOOK_SYNTHESIS_CH3_9.md`, `CHAPTER_COMPLETION_AUDIT.md`, `claude/CH8_PRINT_READINESS_PLAN.md`, `claude/SPEC_PRINT_SPRINT_2026-07-26.md` — superseded by later work.
- `SPEC_BOOK_TOOL_PLACEMENT.md` — its appendix lettering is desynced from current appendix naming.
- The source-analysis stubs credit "Bob Elliott" for *Existential Kink*. The author is **Carolyn Elliott, PhD**.

## Structural facts that are current

The gate walk is removed from Chapters 4 through 8. Chapters 2 and 9 keep theirs. Chapter 2's daemon roster carries seven, not eight — the Vulnerable Child left with the gate walk.

Every stage sequence is five beats. There are no four-stage models left in the book.

The Reflection Prompts convention is retired. It appears in zero chapters as of 2026-07-28.

Chapter 2's sections renumber 1 through 10. The old Section 9 (Reflection Prompts) was cut and Sections 10 and 11 moved up.

## Still missing from the book

Neither appendix exists as prose anywhere — not in the project, not on any disk. Both are hard print blockers.

- **Appendix — The Polarity Map** (~1,500 words). Closes open references at `ch3:623`, `ch4:148`, `ch5:188`, `ch6:151`, `ch7:121`.
- **Appendix — The 3-2-1 Shadow Process** (~1,500 words). Closes `ch3:456`, `ch3:593`, `ch4:374`. Carries the book's only Wilber credit.

Front matter, table of contents, and back matter are also unwritten.

## Standing editorial rules

Banned words: *room*, *quiet*, *quietly*, *genuinely*. (*Genuine* is not banned.) No sentence opens with *And* or *But*. The "Not X. Not Y." negation stack is banned. "Make room" becomes "make space." Never narrate the reader's unnamed history back to her as fact.

Do not attribute generated prose to Wendell as his established voice. Do not invent a frame and present it as a finding. When a voice rule is violated, write around it — do not argue for an exemption and do not build a taxonomy of acceptable variants.

Run this gate on any new prose before it goes in front of Wendell. Every counter must read 0.

```python
print('andbut',len(re.findall(r'(^|[.?!]["""\'’]? |\*|\*\*|— |; )(And|But) ',t,re.M)),
      'banned',len(re.findall(r'\broom\b|\bquiet(ly)?\b|\bgenuinely\b',t,re.I)),
      'emdash',len(re.findall(r'[a-zA-Z0-9,]—[a-zA-Z0-9]',t)),
      'A0',len(re.findall(r'you (were|was) (taught|told|raised|trained)|somewhere along the way|the village taught you',t,re.I)),
      'stacks',len(re.findall(r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b',t)))
```

Also check new prose for duplicate sentences against all nine chapters before inserting it. Sentences have been accidentally duplicated across five chapters before. The scanner is in `claude/MTGOA_INSTRUMENTS_TOOLKIT.md`.
