# marginalia/ — the Calrunia frame

Every chapter from 2 onward is a document written by a named character, annotated
in the margin by somebody else. `HANDOFF.md` is the authoritative brief: the
frame, the locked decisions, the do-not list, and what remains unbuilt.

**The marginalia is live in `manuscript/ch2.md` – `ch9.md`.** 44 marginalia
blocks, 8 epigraph-byline blocks, 1 postcard. All wrapped in HTML comments —
`<!-- MARGINALIA -->`, `<!-- EPIGRAPH-BYLINE -->`, `<!-- POSTCARD -->` — so they
stay greppable, strippable, and safe to hand a typesetter. Chapter 1 carries none.

## Rebuilding

```
python3 marginalia/compile.py --check    # resolve every anchor, write nothing
python3 marginalia/compile.py --apply    # write marginalia into manuscript/
python3 marginalia/compile.py --strip    # remove it again
python3 marginalia/compile.py --verify   # prove apply+strip == original body text
```

Edit a note in `insertions.py`, `--strip`, then `--apply`. An anchor that misses
or matches twice is reported and that chapter is left untouched; the run never
half-writes.

## How this differs from the handoff package

The handoff shipped eight pre-compiled chapters and said to diff and merge them.
Do not. They were compiled from the `/mnt/project` docs, and two problems came
with that:

- **Their ch2 was one revision behind the working file.** Merging it would have
  deleted a seven-line passage that is in canon — the *"By the end of this
  chapter, you should know"* list closing Section 10.
- **They carry a STATUS header** (`STATUS: CURRENT MANUSCRIPT — Chapter N…`)
  that is project-doc metadata, not book content, and whose instruction to
  "write your edits back to this same path" is now false. Canon is this repo.

`compile.py` here reads `manuscript/ch{N}.md` instead, so it cannot drift from
canon. Verified: every one of the 53 blocks is byte-identical to the handoff's
output, and body text round-trips byte-identical on all eight chapters.

## Open, from the handoff

The school is unnamed, which blocks the half-title and the enrollment page. The
25 move stopping conditions are the largest remaining task. The body-text pass
D1–D4 has not started. See `HANDOFF.md` for the ordered pick-up list.

## Voice-gate status

**The gate applies to the margin as well as the body — ruled 2026-07-29 — and the
marginalia passes it clean.** Every counter reads 0. Check with:

```
python3 instruments/gate.py        # body and marginalia scored separately
python3 instruments/gate.py -v     # quote every hit with context
```

Getting there took 19 edits, all in `insertions.py`: 18 uses of *room* and one
of *quietly*, plus the single sentence opening with *But*. Two of the
replacements are worth knowing about, because they set house usage:

- *"what the room felt like"* became **"what the field felt like"** in both
  places it appeared. *Field* is the Body's own word, set up by Maera's question
  in the Ch3 byline, and the sentences that follow already call it a *reading*.
- *"reads a room"* became **"reads a company"**, and *company* now carries that
  sense wherever the margin means the people rather than the space.

Where the ban cost nothing, the noun just got more specific — *hall*, *space*,
*conversation*, *on a map*. Note that plural *rooms* passes the gate: `\broom\b`
does not match it, so the Ch7 note keeps *"stayed in rooms that had already
chosen harm."*

The negation rule is separate and was not touched: `specs/RULE_COLLISIONS.md`
deliberately revises it into licensed *ranking* negation versus banned *denying*
negation, and that supersedes the flat ban for this work.
