# light_verb: the proof session's DL-97 folded into the shared core

**Ratified 2026-09-11**, commit A of three in step 3 (install the toolkit). Before the toolkit can
be installed, the divergent instruments have to be reconciled or the install silently regresses the
board. This is the first: light_verb.

The branch ran the proof session's DL-97 light_verb; the shared core (v32) had none of it. A plain
install would revert DL-97 and move the count. So **DL-97's detection mechanism goes into core, and
its vocabulary — which is this book's — goes into the manifest.** One instrument now serves every
book.

## What is mechanism (→ core) and what is vocabulary (→ manifest)

| DL-97 change | kind | lands in |
|---|---|---|
| TRADE tier: an abstraction that buys/sells/spends, requiring an abstract object | universal shape | core, always on |
| `min_words` floor lowered from `> 3` to `> 1` | universal | core |
| the book's own abstractions (*feeling, charge, reading, vigilance*, …37) | this book's nouns | manifest `abstractions:` |
| BORROWED tier machinery (a wrong-domain verb on a feeling) | universal shape | core, empty by default |
| the borrowed vocabulary (*metabolize*) and its DL-102 ruling | this book's | manifest `light_verb_borrowed:` / `…_ruled_in:` |

Core reads all three lists through new `profile` accessors. A project that declares none runs the
generic detector unchanged. Core keeps its own improvements the branch fork had dropped: the
abbreviation-guarded sentence splitter and paragraph reflow.

## Measured

Zero-target accounting counts **DELEXICAL** only; DEAD and (the transaction sub-shape of) TRADE are
surfaced, never graded. So the number that gates is DELEXICAL.

| project | DELEXICAL before (core v32, no DL-97) | after (core + DL-97) | BORROWED |
|---|---|---|---|
| **MTGOA** | 51 | **52** | 0 |
| Flirtcraft | 1 | 1 | 0 |
| AI Psychologist | 5 | 5 | 0 |

**MTGOA moves by exactly one, and it is a real hidden hit.** The `min_words` floor was hiding
three-word sentences; the one it uncovers here is *"You're performing translation."* (perform + a
nominalization — a buried verb). That is DL-97 doing its job, not a regression.

**The siblings do not move.** With no `abstractions:` key they run the generic detector, and the
`min_words` floor adds no DELEXICAL hit to either. `BORROWED` is empty (no vocabulary declared), so
it fires on nothing. Their surfaced DEAD backlog may gain a couple of short-sentence candidates,
which never gates.

**BORROWED is 0 for MTGOA by ruling.** *metabolize* is declared as the tier's vocabulary and then
ruled in (DL-102), so the tier records that the question was asked and fires on nothing.

## This commit

The branch side of the port: `editorial.yaml` gains `abstractions:`, `light_verb_borrowed:` and
`light_verb_borrowed_ruled_in:`. It is inert until the toolkit install (commit C) replaces the
branch's forked light_verb with the ported core; the manifest is staged ahead of it so the install
is a clean drop-in with no count surprise. The core-side port (light_verb.py, profile.py) lands
with the editorial-core v32 commit, after the PR.

The branch's own board is unchanged by the manifest: `manifest` clean, gate/claims/round-trip/
toolchain pass, coherence fails only the known `drift` check that the zero-target manifest retires
at commit C.
