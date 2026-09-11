# The toolkit installed, the board flipped to zero

**Ratified 2026-09-11**, commit C of three in step 3. Commits A and B reconciled the diverged
instruments (light_verb DL-97 to core; gate/prose_diet exemptions and registers to the manifest).
This installs the shared core v32 toolkit on the branch and switches the manifest to the
zero-target regime, in one commit. **The drift failure clears because the manifest changed and the
installed coherence has no drift check — not because coherence was hand-edited.**

Branch `editorial/trailing-and-onto-proof-2026-09-10`, on top of commit B.

## What the install did

`editorial-core/sync_core.py --apply` brought the branch from core v28 (the proof line) to v32:
17 core modules updated, 7 added (`exceptions`, `ledger`, `polysyndeton`, `core_meta`,
`build_bands`, `corpus_clean`, `presupposed`). The branch had been missing the ledger reader, the
ledger writer and polysyndeton entirely. Project files are untouched: `build_book.py` (with its
`nonprinting` hook), `review.py`, `claims.py`, `claims.yaml`, `markpatterns.py`, `agency_grep.py`.

MTGOA now runs the **same** gate, prose_diet, light_verb and fragment as every other book. Its own
rulings live in the manifest: the gate exemptions, the prose_diet registers, the light_verb
abstractions, the boxed-record scoring.

## The manifest, flipped to zero

- `core_version: 32`, `core_home: ../editorial-core`.
- `targets:` (gate, telling, trailing_and, light_verb, fragment, polysyndeton, slop_shapes — all
  0) and `reporting:` (prose_diet, antecedent). This is what `coherence.check_zero` drives.
- `baselines:` kept as **reference only** — the comment that said "coherence re-measures and fails
  on drift" is now false and corrected. **Core v32 has no drift check;** `check_zero` replaced it.
- `polysyndeton` added to `pass:` (promoted from reporting on 2026-09-09).

## review.py and claims.yaml

- **review.py** wires a book-wide `polysyndeton` step (7m). Coherence's `pass-wire` and `orphan`
  checks require every manifest target to be run by the orchestration; without this they failed.
- **claims.yaml**: DL-97's carrier `feelings?|charge|readings?|alchemy` lived in light_verb.py;
  commit A moved those abstractions to the manifest, so the registry (correctly) flagged the
  carrier as moved. Re-pointed to its two new homes — the accessor that reads it
  (`profile.abstractions([])`) and the data itself (`editorial.yaml`). CLAIMS PASS.

## A regression the install would have introduced, caught and fixed in core

Core prose_diet's `BLOCK` still stripped HANDBOOK frames. The step-2 boxed-records work had made
the *branch's* prose_diet stop stripping them (so Quill's charter is scored), but that fix was
never in core — so installing core reverted it: the charter left the scored surface, prose_diet's
register anchor `**Clause four.**` matched 0 times, and the charter's over-ceiling **box note
vanished from the board**. Fixed in core the general way: `BLOCK` now strips every frame *except*
those the manifest's `scored_frames:` declares. HANDBOOK is scored for MTGOA, stripped for a
project that scores nothing. The charter block is back on the board (block 1 expletive 1.98 over
1.89), matching the proof line.

## Measured

**The whole board, per location, moved by exactly one site.** Against the step-2 end state (core
v32 before the reconciliation), every scanner is identical except light_verb, which gains
`ch7.md:676` *"You're performing translation."* — the one real hit DL-97's word-floor reveals.
Zero locations rose on any other scanner.

| instrument | zero-target count |
|---|---|
| gate | 0 unresolved (EDITORIAL line now emitted — the step-2 gap) |
| trailing_and | 0 unresolved, 88 ledgered |
| fragment | 38 unresolved, 16 ledgered |
| telling | 198 unresolved |
| light_verb | 52 unresolved |
| slop_shapes | 40 unresolved, 7 ledgered |
| polysyndeton | 7 unresolved, 8 ledgered |

Board checks: **gate, claims, round-trip, test_toolchain, voice (6 BLOCK / 128 WARN), prose_diet
(2 heavy — the charter box note) all as on the proof line.** Coherence: `manifest`, `wiring`,
`pass-wire`, `orphan`, `ledger`, `readable`, `gates`, `core`, `register`, `doc-figures` all pass;
`reference` n/a (no comp-title bands). The single hard failure is **`zero`**.

## The board fails `zero`, and that is the honest state

The zero check reports the real editorial debt: 198 telling, 52 light_verb, 40 slop, 38 fragment,
7 polysyndeton — 335 unresolved hits. **This is the debt that was always there.** The proof-line
instruments surfaced it as a "baseline" and never counted it to zero; now it is counted honestly.
Before this commit the board failed `drift` (a retired self-baseline); now it fails `zero` (real
unresolved hits). Resolving them — rewrite or ledger, one at a time — is the ongoing editorial
pass, out of scope for the instrument reconciliation. The instruments are now correct; the prose
work is visible and named.

## Not committed here

The core-side edits (the v32 instruments) live in `editorial-core/` in The Library and are
committed as one editorial-core v32 release **after the PR**, with the two siblings synced to v32
in the same change (ratified 2026-09-11). Nothing is pushed.
