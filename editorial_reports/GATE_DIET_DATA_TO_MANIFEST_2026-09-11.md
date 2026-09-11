# gate and prose_diet: the leak was data, not mechanism

**Ratified 2026-09-11**, commit B of three in step 3. The consensus ruling said to make
gate/prose_diet project-owned. Reading them changed the call: **core's gate and prose_diet are
already clean, portable, zero-target mechanism** — identical counters, the spine corpus, an
EDITORIAL line, ledger integration. What leaked into core was MTGOA's own *data*:

- `gate.py`: the `EXEMPT` (Laloux "rooms") and `CANON` (the "thing" theses) exemption lists;
- `prose_diet.py`: the `REGISTERS` dict — the headmasters-letter and ch5-charter ceilings.

Every other book ran core and carried those inertly. Worse for registers: `register_for` matches
by filename substring, so a book with its own `ch5.md` would have inherited MTGOA's charter
ceilings. So the fix keeps both instruments **shared** and moves the data to the manifest, which
is the reconciliation's own thesis (mechanism in core, rulings in project data) applied to gate.
MTGOA does not need a project-owned gate, and gets core's EDITORIAL line for free.

## The change

- **Core** (v32, uncommitted): `profile.gate_exceptions()` and `profile.registers()`. `gate.py`
  builds its exemptions from `gate_exceptions:`; `prose_diet.py` reads `REGISTERS` from
  `registers:`. Both empty by default — a project that declares neither runs the bare gate and the
  BASE register on every file.
- **This manifest**: MTGOA's 10 `gate_exceptions` (1 exempt, 9 canon) and 3 `registers`
  (headmasters letter, the ch5 charter block, the ch5 draft-file register), emitted verbatim from
  the exact literals that were in core.

gate.py and prose_diet.py stay **core-owned** (shared, synced). Nothing becomes project-owned.

## Measured

**MTGOA — the exemptions and registers reproduce the hardcoded behavior exactly.**

| | with manifest data | manifest data stripped (control) |
|---|---|---|
| gate | **PASS, 0 unresolved** | FAIL, 20 hits (the "thing"/"rooms" sites, now unexempted) |
| ch5 charter block ceiling | expletive **1.89** (the charter register) | BASE |
| headmasters `be` ceiling | **1.30** (the letter register) | BASE |

The control proves the data is read and applied: strip it and the 20 MTGOA-specific sites surface
and the charter loses its raised ceilings.

**The siblings shed the data with no count change.**

| | gate (unresolved / total) | prose_diet heavy |
|---|---|---|
| Flirtcraft before → after | 0 / 0 → **0 / 0** | 2 → **2** |
| AI Psychologist before → after | 13 / 15 → **13 / 15** | 3 → **3** |

Neither sibling's prose contains MTGOA's exemption phrases, so removing the exemptions from core
changes no gate count. Neither has a `ch5.md` or `headmasters_letter.md`, so `register_for` never
matched their files — the register move is provably inert for them. The leak is gone and nothing
moved.

## This commit

The branch side: `editorial.yaml` gains `gate_exceptions:` and `registers:`, staged ahead of the
install (commit C), which replaces MTGOA's old branch gate/prose_diet with core's clean shared
copies that read this data. The core side (profile.py, gate.py, prose_diet.py) lands with the
editorial-core v32 commit, after the PR. The branch's own board is unchanged by the manifest
additions.
