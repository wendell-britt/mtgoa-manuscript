# Editorial shipping merge notes — 2026-08-07

## Chapter 6: merge-ready draft

Apply the uncommitted `manuscript/ch6.md` diff as one unit.

- Adds `### The Five Modes of Design` before the axis and EA table.
- Aligns Section 6 to the native Architect sequence:
  `Trace What Is Happening` → `Name the Unstated Assumption` →
  `Find the Leverage Point` → `Ship the Minimum` → `Design for Handoff`.
- Folds Refactor Kindly into the deployment/iteration paragraph after Ship the
  Minimum rather than retaining it as a competing fifth move.
- Focused checks: reader-run 0 candidates; `git diff --check` clean;
  `marginalia/review.py manuscript/ch6.md` has no new blockers (one pre-existing
  blocker remains elsewhere in the chapter).

## Chapter 7: merge-ready draft

Apply the uncommitted `manuscript/ch7.md` diff together with its marginalia
anchor updates. It:

- change the five local `Channel` headings to `Mode`;
- removes the Alchemy / Translate / Control taxonomy and all bracket tags;
- preserve Section 6 as the only game-move sequence;
- consolidate Bridge anxiety, Translator superiority, and Repairer
  forgiveness/closure material as approved in the review conversation.

Focused Chapter 7 review: reader-run 0 candidates; duplicate scan clean;
all marginalia anchors resolve. The two remaining review blockers predate this
Section 4 work.

## Already committed, cherry-pickable units

- `3f47aa9` — define Neutrality's dissatisfaction/satisfaction arc.
- `2523cd0` — distinguish Diplomat modes from channels.
- `2448745` — relabel Diplomat control practices.
- `c9ff167` — sequence the Chapter 7 game: Bridge → Translate → Hold → Repair → Negotiate.
- `dcd11ff` — make the Architect stage sequence explicit.

## Still to draft before final ship

- Chapter 2: rename or bridge `Five Moves for the Threshold` so it cannot be
  confused with the Five-Move Form.
- Chapter 9: repair remaining Form-language drift.
- Appendices C, E, and F: replace or scope unsupported somatic certainty in the
  worked scenarios.
- Back matter: write the missing Kickstarter backers page, or remove it from
  production requirements.

## Verification after merge

Run:

```bash
python3 instruments/reader_run_scan.py --spine
python3 instruments/dupes.py
python3 instruments/gate.py
python3 marginalia/compile.py --check
git diff --check
```

Then run the assembled-book build and inspect the rendered output.
