# trailing_and — the whole book, to zero

**Requested 2026-09-10:** *"now do the 781 trailing_and in MTGOA."*

**Result: `trailing_and unresolved=0 accepted=65 total=65`.** Every site was read in its
paragraph, chapter by chapter, ch1 → ch9, then the front matter, back matter and appendices.
Each one was either rewritten so the joint names its relation, or ledgered with the shape named.
Nothing went back to the author as "still yours".

---

## The number was 799, not 781

The instrument called its `RANK` tier (the ranking tag, as in *"…and it is the most useful idea I
can hand you"*) a defect outright, then left it out of the zero target and out of `--keys`. So
18 sites sat outside both the target and the ledger. That was fixed first as **core v22**, and
the count became 799.

## What happened to the 799

| | sites |
|---|---|
| **rewritten** so the joint says how the halves relate | 729 |
| **ledgered**, with the shape named (61 entries; one entry covers a sentence wherever it recurs) | 65 |
| stopped scoring because a scanner bug was fixed (net, measured on the original text) | 5 |

The count moved **both ways** during the pass. The recall fixes below surfaced real sites the
old regex had been swallowing, and those were rewritten too.

### How the joints were renamed — approximate, counted by pattern over the edit files

| joint | uses |
|---|---|
| full stop (both halves stand as sentences) | 214 |
| appositive or participle (*a trade that feels like safety*, *leaving nothing to carry*) | 113 |
| relative clause (*which*, *who*, *where*, *when*) | 82 |
| *so* | 42 |
| *but* | 37 |
| fronted condition (*If / When / Once / The moment*) | 28 |
| colon | 24 |
| *while* | 22 |
| *yet* | 20 |
| *though / although* | 18 |
| *then* | 15 |
| *nor* | 9 |
| *because / since* | 7 |
| *without* | 6 |

Full stops are the largest single class, about a third. None of them made a fragment: the
per-location diff below shows no fragment added at any line the pass touched.

### What the ledger holds

| shape | entries |
|---|---|
| serial list: the *and* closes a series of like items | 38 |
| paired questions: two questions of one kind | 14 |
| quoted parallel pairs and quoted series (the Architect's two *here is* statements; two repair scripts) | 4 |
| **voice anchors**, ruled by Wendell 2026-07-31: *"Do not polish these."* | 3 |
| a parallel pair and a two-part test | 2 |

**The voice anchors were a prior ruling, not a judgement made during the pass.** I edited anchor
2 (ch1:119) before I knew it was one. `density.py`'s drift check caught it, and the paragraph is
now byte-identical to the original, as are the other four. They were checked mechanically at the
end, not assumed.

---

## Scanner defects found by reading, and fixed in core rather than ledgered

Each fix is a validity release. Each was synced to all three projects, and each was measured on
the *original* MTGOA text so its effect is separable from the prose edits.

| core | defect | effect |
|---|---|---|
| **v22** | `RANK` outside the zero target and `--keys`. The printout still said *"Zero is a different tic, not a better voice"*, which argued against the house target. | 781 → 799 |
| **v23** | `RANK` fired on coordinate subordinate clauses (*"and why the answer is a better game"*); `fragment --keys` emitted a Python dict as its location | selftest asserts both |
| **v24** | `\w{3,}s` read *this*, *awareness*, *loss*, *axis*, *perhaps* as verbs, in both directions (`, and this matters` was **missed**); `fragment`'s lexicon lacked *date* and *steers* | 799 → 789 |
| v25 | added `am`/`be`; **added `what` to the subordinator list, which was wrong** | — |
| **v26** | **reverted `what`**: measured, it hid ~14 real clauses (*"and what surfaces is not a defense"*) to spare a few list entries. Added the fronted-adverbial rule (*", and when it gets inconvenient, the Controller…"*) | 789 → 795 |
| **v27** | `fragment`: contractions (`'m 're 've 'll 'd`) never entered the lexicon, so *"You're just late to the rules."* counted as verbless | fragment 298 → 284 on the original |
| **v28** | `which` in DEMONSTRATIVE, so a second relative clause read as a new sentence | 795 → 794 |

**v25 is the one to learn from.** It cut the count by 53, and I nearly took the drop as
precision. Listing what it suppressed showed a quarter of it was real defects. A reject rule that
lowers the number by hiding hits looks exactly like one that removes false positives, and the
only way to tell them apart is to read what it removed.

Selftest runs 20/20 (one new assertion, three new clean-fixture lines).

---

## My errors during the pass, all corrected

- **Voice anchor 2 edited**: restored byte-for-byte (above).
- **The quest examples' meaning inverted.** *"…and it will cost me being the easy vote"* means
  you lose that standing. I rewrote four of them as *"at the cost of being the easy vote"*,
  which reads as you become it. All five now use the author's own phrase: *"which will cost me
  being…"*.
- **A banned word introduced** (*"the very thing"*, ch6), caught by `gate` and replaced.
- **A polysyndeton introduced** (ch3:389, *"medicine and cosmology and predates"*), split.
- **A telling label and a not-X-but-Y shape introduced** (ch8), both rewritten.
- **Two ledger reasons swapped** when the list renumbered between calls. Both corrected through
  `ledger.py`, and the helper now selects by line number.

## The other boards — against zero, and against the count when this pass began

| instrument | at start | now | target |
|---|---|---|---|
| trailing_and | 799 | **0** | 0 |
| fragment | 298 | 283 | 0 (−14 is the v27 scanner fix; −1 from the prose) |
| telling | 222 | 196 | 0 (a side effect of the rewrites) |
| light_verb | 53 | 52 | 0 |
| slop_shapes | 36 | 36 | 0 |
| polysyndeton | 7 | 7 | 0 |
| gate | 2 | 2 | 0 |

**No hit was introduced anywhere.** After each chapter, hit counts were compared *per line*
against a copy of the book with the original prose. The only rises were the ones listed above,
and each was fixed. Ledgers: `readable ok`, `ledger ok`. Stale acceptances were pruned as they
appeared: three trailing_and entries made stale by v24, one polysyndeton entry whose sentence I
split, and one AI Psychologist entry v24 correctly stopped over-catching.

## What the instrument still cannot see

- **A noun clause as the subject of a new clause** after `how`/`why`/`that`: *"and how you carry
  it is the difference"* is a real clause the subordinator rule drops. Recorded, not fixed. The
  fix is a tagger, and `fragment.py` already records what a tagger costs.
- **A bare `and` with no comma** joining two clauses. That is the 322-sentence gap read by hand on
  2026-09-10, outside this instrument by design.

## Other projects on v28

The recall fixes moved their counts. They are reported here, not worked: the AI Psychologist's
trailing_and is **104** unresolved (was 95), Flirtcraft's is **72** (was 71).
