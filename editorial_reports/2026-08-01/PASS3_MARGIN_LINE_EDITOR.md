# PASS 3 · LINE EDITOR — the marginalia, as its own surface, 2026-08-01

**Role:** Line Editor, `specs/EDITORIAL_OPERATING_SYSTEM.md` §3 — readability only.
**Surface:** the frame. 66 blocks, 6,656 words, in `manuscript/ch2.md`–`ch9.md`.
**Ruled by Wendell 2026-08-01:** the margin gets its own pass, not a column in the body's.
**Status: DIAGNOSIS ONLY. Nothing is applied.** The body pass was applied on a ruling;
this one has not been ruled on yet.

DL-6 already says the margin is its own scored surface. It had never had a line pass —
`line_scan.py` stripped it, `prose_diet.py` strips it, and `marginalia/review.py` reads
it for voice rather than for readability. This closes that.

---

## 1 · Why the body's rules cannot simply be pointed at the margin

The annotator is a different hand in a different genre, and three of the six rules mean
something different here:

- **`orphan-ref` is the genre, not a defect.** A margin note *should* open on *This* or
  *They* — it is annotating the body sentence beside it, and the antecedent is on the
  same page in the other hand. Both margin hits (`ch6:347`, `ch7:143`) are this. In the
  body the same pattern is a real defect. Same rule, opposite verdict.
- **`hard` runs long here on purpose.** The Heads' admissions documents are
  administrative prose and the annotator's notes are one long breath followed by a short
  one. Six of the nine mechanical hits are that shape and all six hold.
- **`repeat` finds nothing** — 0 hits. The margin has no formula to repeat, because no
  two notes do the same job.

So `line_scan --margin` returns **9 candidates**, of which 1 is real. The other five
flags below came from reading all 66 blocks, which is the only way this surface was
ever going to be scanned.

```
python3 instruments/line_scan.py --margin        # counts
python3 instruments/line_scan.py --margin -v     # every hit, with its block type

file        orphan-ref      repeat     doubled        hard      notbut  banned-kin   total
ch3.md               0           0           0           1           0           0       1
ch5.md               0           0           0           1           0           0       1
ch6.md               1           0           0           0           1           0       2
ch7.md               1           0           0           2           0           0       3
ch8.md               0           0           0           2           0           0       2
TOTAL                2           0           0           6           1           0       9
```

`--margin` reports the **block type** with every hit, because MARGINALIA, HANDBOOK,
EPIGRAPH-BYLINE, POSTCARD and SIGNATURE are five genres and the adjudication differs in
each. A 53-word sentence in an admissions document is not the same finding as a 53-word
sentence in a note scrawled beside a paragraph.

## 2 · Before anything is applied — where a margin edit has to be made

**The margin exists twice.** `marginalia/insertions.py` is the source; `manuscript/`
carries the compiled result. Both copies verified to hold the same strings.

An edit made only in `manuscript/` survives until the next `compile.py --strip` /
`--apply` cycle and is then silently reverted. An edit made only in `insertions.py`
never reaches the book. **Every flag below has to be applied in both**, and
`compile.py --check` re-run afterwards — currently green, all anchors resolve across
eight chapters.

This is the margin's version of the lesson DL-18 records: the cheap failure is not
getting the edit wrong, it is getting it right in one place.

## 3 · The flags — 6

### MG-1 · `ch4:17`, HANDBOOK, School of the Line §3 · the only exclamation mark in the frame

> Students who wait until they feel ready have suffered as a result**!**

- **Diagnosis:** six admissions documents close their cost clause on the same formula,
  and five of them end it with a period — `ch3:17`, `ch5:17`, `ch6:17`, `ch7:17`,
  `ch8:17`. This is the sixth, and it is **the only exclamation mark in all 66 blocks
  and 6,656 words**. In a set of documents whose whole joke is that they are filed
  administrative returns, one raised voice reads as a typo rather than as Corin.
- **Minimal edit:** `!` → `.`
- **Reader problem solved:** the shared formula stays shared, which is what makes the
  six documents read as one archive.
- **Risk to voice:** low. Corin's register is clipped and blunt, not exclamatory —
  nothing else they write in the book uses one.
- **Leave as-is if:** the mark is deliberate characterisation. If so it should not be
  the only one on the surface; give Corin a second one somewhere and it becomes a tic
  instead of a slip.

### MG-2 · `ch6:49`, MARGINALIA · a tense error, in the note that turns the chapter

> They ask it of their own diagrams now. Not always in time — twice in one week I watched it arrive a day late, both times about somebody I liked — but they ask, which they did not used to, and the asking is all of what changed.

- **Diagnosis:** *did not used to* is not grammatical — *used to* does not survive the
  auxiliary. It sits on the note's last clause, which is the point of the note. The same
  sentence is also the surface's only `notbut` hit: 38 words held open between *Not* and
  *but*, with a two-dash aside inside the gap.
- **Minimal edit:** "…but they ask, which they **did not do before**, and the asking is
  all of what changed."
- **Reader problem solved:** the note's conclusion stops stumbling on its own verb.
- **Risk to voice:** none. *Did not do before* is plainer than *did not used to* and the
  annotator is plain.
- **Leave as-is if:** the slip is characterisation — but it is the only one of its kind
  in the frame, and the annotator elsewhere is a precise writer.
- **Note on the 38-word negation:** it survives a read-aloud, so it is not flagged
  separately. The verb is the defect.

### MG-3 · `ch8:495`, MARGINALIA, Irix Vale · the same verb three times in 24 words

> I looked at it again this week and **found** the omission — and then **found** that Sera had **found** it in the spring, and Maera the year before that.

- **Diagnosis:** three *found*s inside one sentence, in the note that lands ch8's
  reveal — five Heads discovering they all left the same man off the diagram. The
  repetition flattens three different acts (noticing, learning, discovering) into one
  word, and the beat depends on them being different.
- **Minimal edit:** "I looked at it again this week and found the omission — and then
  **learned** that Sera had **seen** it in the spring, and Maera the year before that."
- **Reader problem solved:** the chain of discovery reads as a chain rather than as an
  echo.
- **Risk to voice:** low. Irix's register is specification-plain; three verbs where
  there are three acts is more precise, not less.
- **Leave as-is if:** the repetition is meant as an incantation. It does not read as one
  in a note this short.

### MG-4 · `ch3:53`, MARGINALIA · two numbers for the same span, 40 words apart

> She stopped in her **fourth year** here and has described the time since as the first she could hear anything at all. … you are shortly to be taught by somebody who spent **a decade** marking her own homework.

- **Diagnosis:** inside one 90-word note, Maera's grading habit runs four years and then
  a decade. Both can be true if she graded for six years before she arrived, but nothing
  says so, and the reader who notices has to build that reconciliation herself — in the
  note whose job is the joke at the end.
- **Minimal edit:** "…by somebody who spent **years** marking her own homework." One
  number governs, the joke is untouched.
- **Reader problem solved:** the punchline does not arrive carrying arithmetic.
- **Risk to voice:** none.
- **Leave as-is if:** the decade is deliberate and predates the ship, in which case say
  so in three words — *a decade of it, four of them here*.

### MG-5 · book-wide · *eleven* is doing three jobs, and one of them is not a joke

Measured: **12 occurrences in the margin, 6 in the body.**

The motif is deliberate and it works — Bram is *"asked eleven times"* to become faculty
and *"declined on eleven occasions"*, and the number then turns up as a wink: eleven
days at Oreve, eleven words, eleven people in the hall, eleven students on the postcard.

Where it stops working is tenure. **Three different people each measure their working
life in eleven years:**

| | |
|---|---|
| `ch7:737` | the annotator — *"In eleven years I have known it used four times"* |
| `ch8:199` | Elian Cross — *"I have taught the walk-away terms for eleven years"* |
| `ch8:578` | Bram Tull — *"He does not sleep the week before an intake. I have known this for eleven years"* |

- **Diagnosis:** the last two sit 379 lines apart in the same chapter, both about
  Thalen, in consecutive notes the reader reads back to back. At that point the number
  stops reading as the annotator's private joke and starts reading as the author's
  default, which is the thing a running gag cannot survive.
- **Proposed:** keep the joke and the counts; **change one of the two ch8 tenures.**
  Bram's is the one to move, because Elian's eleven years is tied to a curriculum and
  Bram's is tied to a person: *"I have known this since he came aboard."*
- **Reader problem solved:** the motif stays a motif.
- **Risk to voice:** none — it removes a number rather than adding one.
- **This is a ruling, not an edit.** It is your gag and the count is yours to set. If
  the collision is the point, the report records it and nothing changes.

### MG-6 · `ch8:21`, HANDBOOK, School of the Horizon §1 · recorded, recommend leave

> Maera would say we take the person who has stopped registering their own signal, and Corin would say we take the person who cannot spend a line, and both are describing the same applicant from inside their own school, which is the difficulty with this document and with us.

- **Diagnosis:** 53 words, the longest sentence in the six handbooks, and the first
  sentence of the last one.
- **Recommendation: leave it.** It is the only handbook that has to hold five other
  schools inside one sentence, and it enacts the difficulty it names. Splitting it makes
  the Horizon sound like the Pattern. Logged so the next pass does not re-flag it.

## 4 · Checked and clean — recorded so it is not re-run

- **`orphan-ref` `ch6:347` and `ch7:143`.** *"They see somebody who is fast"* and *"This
  is the sentence in the treatise I have quoted most"* both point into the body they
  annotate. That is the form. Not defects here; the identical pattern in the body is.
- **The five long sentences** at `ch3:97`, `ch5:227`, `ch7:33`, `ch7:294`, `ch8:21`. All
  read aloud in one breath with a clear spine. `ch7:294` — *"grace is the only
  variable"* — is the best close on the surface and is 49 words.
- **0 `repeat`, 0 `doubled`, 0 `banned-kin` in 6,656 words.** The frame is cleaner than
  the body on every mechanical count. Worth saying plainly.
- **Spaced em-dashes** are the margin's house style and `gate.py` reads 0 on the
  marginalia surface, as it has since 2026-07-29. Not a finding.
- **The Heads' signatures and epigraph bylines** carry no line-level defect. Checked all
  eight bylines and six signatures.

## 5 · What this pass did not do

- **It did not read the margin against the body it annotates.** A note can be perfectly
  written and answer a paragraph that no longer says what it answered — that is
  continuity work, and `MARGIN_ARC.md` owns the arc.
- **It did not touch the arc, the reveal, or the Heads' characterisation.** One job at a
  time.
- **It is not a copyedit.** Hyphenation, capitalisation of in-world terms, and the
  house-style questions in the handbooks come after line work freezes.

## 6 · Rulings needed

1. **MG-1 to MG-4** — four concrete defects with minimal edits. Yes/no each, or all.
2. **MG-5** — the *eleven* collision. Your gag, your count.
3. **Application route.** If these are approved, they go into `marginalia/insertions.py`
   **and** `manuscript/`, followed by `compile.py --check`. Confirm that route rather
   than a `--strip`/`--apply` cycle, which would rewrite all 66 blocks and make the diff
   unreviewable.

*Instrument: `instruments/line_scan.py --margin` (new mode). No file changed by this pass.*
