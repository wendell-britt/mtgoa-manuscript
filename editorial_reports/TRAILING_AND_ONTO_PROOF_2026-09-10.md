# The trailing_and pass, landed on the proof line

**Ratified 2026-09-10** as step 3 (cast seed 6117). The trailing_and pass is replayed onto the
reconciled proof line and whatever remains is taken to zero fresh. It runs with **Wendell's
ruling of the same day:** *"Boxed records should be scored, but those should be ledger notes
because they have to be edited separately."*

Branch `editorial/trailing-and-onto-proof-2026-09-10`, on top of `2ebf084` (the fragment-ban
reconciliation).

---

## Result, measured with editorial-core v31

Measured on clean copies of the two commits (`55edd24`, before the replay, and the commit that
added `scored_frames` below), with core v31 installed over each and the same manifest in both.
Every figure is a count of hits.

| | before this step (`55edd24`, no ledger) | after |
|---|---|---|
| **trailing_and** | 738 | 88: **0 unresolved**, 88 accepted, 0 stale |
| fragment | 252 | 251: all unresolved |
| telling | 215 | 198: all unresolved |
| polysyndeton | 23 | 15: 7 unresolved, 8 accepted |
| slop_shapes | 47 | 47: 40 unresolved, 7 accepted |
| light_verb | 52 | 51: all unresolved |
| gate · claims · round-trip · test_toolchain | pass | **pass** |
| voice linter | 6 BLOCK · 128 WARN | 6 BLOCK · 128 WARN (appendix voice 27 → 26) |

**Corrected 2026-09-10, after a hostile review.** The first version of this table was measured
in a scratch copy whose manifest carried `scored_frames`, a key this branch's manifest did not
have until the fix commit. It also mixed units: fragment (185 → 184) and telling (212 → 194)
were counted as distinct flagged sentences, and polysyndeton and slop_shapes as unresolved hits
with the final ledger applied. The table above re-measures the commits themselves, in hits.

**No hit rose at any line.** Each scanner's hits were compared per `file:line` between the two
clean copies, with the ledger set aside on the after side so that accepted hits count too:
zero locations rose on any of the six. All five voice anchors are byte-identical to the proof
line.

## Boxed records — the ruling applied

- **Every HANDBOOK box is restored byte-for-byte to the proof line (`af8a931`).** That undoes my
  step-2 repairs inside boxes, and also master's clean fragment-ban edits inside them: if boxes
  are edited separately, no sweep edits them. The admissions boxes read alike again
  (*"6. A word from the Head."* in each).
- **They are scored.** Core v29 adds a manifest key `scored_frames:`, and MTGOA's manifest lists
  HANDBOOK. `prose_diet.py` no longer strips the boxes either, so Quill's charter is measured
  again. *(The key missed the first commit of this step: without it the 22 boxed notes read as
  stale ledger entries under core. Added in the fix commit.)*
- **Their hits are ledger notes:** 22 trailing_and notes in `editorial_exceptions.yaml`, and 35
  gate hits covered by 28 entries in `gate.py`'s `BOXED_NOTES`. Each gate entry is keyed on the
  whole boxed line, so a note cannot spread to the same words elsewhere.
- **For the separate box edit, the notes in one place:**
  - the 22 trailing_and sites (Quill's charter, the admissions pages, the Heads' records);
  - the 35 fragments (*"Entry."*, *"None."*, *"A word from the Head."*, *"Clause one."*, and the
    session records);
  - **Quill's charter now reads over two of its own ceilings, ruled 2026-07-31**: expletive
    1.98 against 1.89, copula 1.47 against 1.30;
  - **the ch8 pull-quote pair** (box at L49, body at L227: *"That is a joke and it is also the
    timetable"*) should be edited together. The body copy was put back to match the box.

## How the replay worked

My trailing_and commit (`b89c60c`) was cherry-picked onto this branch with its instruments and
manifest held back. Its prose conflicts were resolved one sentence at a time, with the proof
line winning every collision. Three corrections followed:

- **Git over-drops adjacent edits.** It treats edits to adjacent sentences as a conflict, so a
  proof mark on one sentence discarded my edit to the next. Every sentence-level change was
  rebuilt from the full diff and re-applied wherever its original sentence still stood verbatim
  outside a box: **69 edits recovered.**
- **147 edits were genuinely superseded**, meaning the proof line rewrote the sentence first,
  mostly in the *land* sweep (DL-98/99) and in ch2/ch3's proof marks. Their new wording was
  rescanned, and the 69 open sites that turned up were rewritten fresh. Most keep the relation
  chosen before, fitted to your new word (*"a decision falls on…"*).
- **The *"which" tail* regression was mine.** The house voice linter flags `which` as the subject
  of a clause commenting on what came before (*"…, which is what makes it durable"*). My pass had
  added 64 of them, exchanging one flagged tic for another. All 64 are rewritten: the six
  *"Yours …, which is the one to work"* now read *"…: work that one"*, the quest examples read
  *"…, though it will cost me…"*, and the rest are full stops, appositives and colons. That count
  is now **91, below the 92 the book had before.**

## Defects found and fixed along the way

- **ch6, a not-X-but-Y shape from my earlier bare-*and* pass.** It is now *"Written as an
  accusation or not, the design is one."*
- **ch6, a denying negation exposed by a full stop** (voice BLOCK), rewritten.
- **Voice anchor 3 (ch4, *"using 'I' statements"*) had been edited by PR #21's fragment pass.**
  It is restored to Wendell's text under *"Do not polish these"* and its fragment is an anchor
  note in the gate.
- **Two banned-word and trailing-and slips in my own repairs**, caught by the gate and the
  scanners and fixed before commit.
- **Core v30: stale ledger entries were invisible.** coherence compared entries with accepted
  *hits*, and one entry can accept several hits, so dead entries hid under the surplus. The
  count now comes from the entries themselves. **Eight stale entries were pruned**, and the
  selftest reproduces the case.
- **My own prune script deleted all 107 acceptances once.** It read a freshly imported
  exceptions module in place of the instrument's own. `ledger.py`'s one-step `.bak` restored the
  file whole, and the rerun refused to remove anything unless its list matched the count the
  instrument printed.
- **Five claims carriers re-pointed.** DL-92, DL-98, DL-99 (×2) and DL-105 guard phrases my
  rewrites touched. Each ruling's fact is still carried, and each phrase now guards the
  fact-bearing words, not the conjunction.

## Not done here, and why

- **The instruments diverged three ways:** core v30, master's gate fragment counter, and the proof
  session's DL-97 light_verb fix plus its coherence, prose_diet and telling edits. This step lands
  prose and ledger measured with v30 from outside, and **leaves the branch's instruments as they
  are.** Reconciling them is a decision in its own right.
- **So the branch's own coherence fails `drift`.** It still enforces the retired self-baseline
  (*"manifest says 12.4%, measures 5.5%"*) and fails because the prose improved. It clears when
  the zero-target manifest lands with the instrument reconciliation.
- **`ch5_memoir_move.py`'s SECTION4 anchor** fails as it did on the proof line.

## Not pushed

Local branch. If the proof session pushes more to `claude/book-pdf-epub-production-ybxa11`,
merge that in before step 4.
