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

The marginalia has **not** been through the banned-word gate in
`specs/MANUSCRIPT_FILE_CANON.md`. It uses *room* 19 times and *quietly* once,
both banned in body prose. Nothing in `specs/` here addresses that list, so this
looks unconsidered rather than decided — but the margin is a different register
in a different character's voice, so whether the ban reaches it is Wendell's
call. Nothing has been changed either way.

The negation rule is different: `specs/RULE_COLLISIONS.md` deliberately revises
it into licensed *ranking* negation versus banned *denying* negation, and that
supersedes the flat ban for this work.
