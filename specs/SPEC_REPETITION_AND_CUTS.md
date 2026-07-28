# EDITORIAL SPEC — REPETITION MAP AND CUT TARGETS
**Built:** 2026-07-28 · **Manuscript:** 95,075 words (ch1–ch9) · **Governing ruling:** transcend and include

---

## 0. THE HEADLINE, BEFORE THE EVIDENCE

Your hypothesis was that callbacks would let us cut most of the bloat, because being able to point back means we stop repeating ourselves.

I measured it. **The repetition is real, but it is not where most of the bloat is.**

Cross-chapter repetition, measured at the sentence level with a fuzzy matcher across all nine chapters, is **2,919 recoverable words** — 3.1% of the manuscript — and several hundred of those are deliberate refrains that should survive. Net recovery from pure de-duplication is closer to **1,800 words**.

That is worth taking. It is not the answer to the word count.

What the measurement did find is bigger and different from what we were looking for. The chapters are not repeating each other's *sentences*. They are repeating each other's *shapes*, and the book carries **13,405 words of recurring per-chapter apparatus** filling those shapes — roughly twice the load of its closest structural comparable and infinitely more than its other one.

The two source texts are now measured, and they put a hard ceiling on what any structural move can recover: **under 3,600 words.** They also cost me an instrument. I proposed band normalization in §4 Tier 2 on the theory that a parallel section should hold the size the book set for it. Neither source does that. Elliott lets a parallel family run thirteenfold; Chou lets his chapters run nearly fourfold. Both hold their *apparatus* to a fixed size and let their *content* be as long as it needs to be. **I am retracting Tier 2 and the 3,300 words it claimed.**

With the mechanical de-duplication, the three surviving structural cuts, and a line audit at the rate Ch2 actually returned, the honest ceiling for this pass is **5,000–5,700 words**, or 5–6% of the book. §5.5 is the part to read first.

The callback work still has to happen. Its payoff is momentum rather than word count, and I want to be exact about that before you spend four days on the wrong instrument.

---

## 1. WHERE THE MASS ACTUALLY SITS

Every section in ch3–ch9, prose only, tables and headings excluded.

| Section | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 | **Total** |
|---|---|---|---|---|---|---|---|---|
| S1 The Exile | 559 | 599 | 1136 | 605 | 725 | 1363 | 267 | **5,254** |
| S2 The Distortion | 652 | 678 | 905 | 584 | 405 | 1133 | 427 | **4,784** |
| S3 The Concept | 1950 | 1041 | 917 | 1003 | 965 | 1663 | 464 | **8,003** |
| S4 The Practice | 4167 | 4217 | 2249 | 1589 | 4991 | 3240 | 2238 | **22,691** |
| S5 The Daemon | 2247 | 1461 | 1722 | 2492 | 1640 | 1578 | 4612 | **15,752** |
| S6 The Game | 3048 | 1066 | 452 | 1198 | 2376 | 1641 | 1998 | **11,779** |
| Deck apparatus | 908 | 691 | 681 | 744 | 819 | 1020 | 0 | **4,863** |
| S7 Recap | 656 | 791 | 252 | 583 | 387 | 374 | 182 | **3,225** |

**Section 4 and Section 5 together are 38,443 words — 40% of the manuscript.** The two zones we spent the last several passes examining, the Exile/Distortion cold starts and the deck apparatus, are 14,901 words combined, and most of that is content rather than duplication.

That reframes the target. The Practice section is where the book is expensive, and it is expensive in a specific, fixable way described in §4.

---

## 2. THE REPETITION MAP

### 2.1 What actually recurs, book-wide

A fuzzy sentence matcher (Jaccard ≥ 0.62, Face names normalized so *Shaman*/*Regent* variants collapse) run across all nine chapters found **105 recurring groups totaling 2,919 recoverable words.** The top of the list:

| Recoverable | Chapters | Text |
|---|---|---|
| 135 | 6 | *The Show Up row is where quests come from — every card in it ends in an artifact…* |
| 120 | 6 | *Write yours in one line with four things in it: what you will do, who it reaches, by when…* |
| 100 | 5 | *Look at the sequence, not the verdict — that is the only place the pattern is visible…* |
| 90 | 6 | *A card that ends in a quest is a card you played, and the difference is a person.* |
| 85 | 6 | *Log the BAR, then convert it into one quest with a name and a date in it.* |
| 80 | 5 | *…is not one; nobody can tell whether you did it, including you.* |
| 76 | 5 | *Draw from your twenty rather than the hundred and twenty — though not from a single row.* |
| 75 | 4 | *The Fixer-Healer decides something none of them touch…* |
| 60 | 6 | *A card that ends in the app is a card you read.* |
| 60 | 5 | *Now here is why this daemon stands where it stands, in a book about allyship.* |
| 52 | 5 | *The Controller decides how you are allowed to behave once you are inside.* |
| 50 | 6 | *The tell that a quest is alive is not enthusiasm.* |
| 48 | 7 | *Two minutes to capture it as a BAR.* |

Two of these are protected. *Two minutes to capture it as a BAR* is a refrain that does the same job as a recurring stage direction, and the daemon-jurisdiction roster (*The Protector decides whether you go in at all / The Controller decides how you are allowed to behave / The Skeptic decides whether what you are reacting to was ever real / The Fixer-Healer decides whether the thing in front of you is in fact yours to fix*) is the recognition device Ch2 explicitly promises at line 228 — *"You will see the daemons more than once: first as a map, then as a walk, then as a move. The repetition is deliberate."* That promise is load-bearing. Do not cut against it.

### 2.2 The Exile cold starts are not duplication

I tested the seven `Section 1: The Exile` openings against each other with the same matcher and Face names normalized. **Fuzzy-templated share: 3%.** They open with a shared cadence — *There was a time when the Architect lived in the village* — and then diverge completely, because each one is teaching a different Face's history.

This matters because we had these flagged as a 7,000-word cut target. **They are not one.** Cutting them cuts content. The escalation test confirms it: cut Ch4's Exile and Ch6's does not collapse, but nothing in Ch6 recovers what Ch4's was teaching either. They are parallel, not sequential.

What is wrong with them is a different defect, and it costs words to fix rather than saving them. Every one of them cold-starts. The reader closes Ch5 holding the Regent's stewardship question and opens Ch6 on *There was a time when the Architect lived in the village* — no hand-off, no acknowledgment that she has been anywhere. That is the transcend-without-include failure, and the repair is §3.

### 2.3 The deck apparatus is smaller than we thought

Measured with tables excluded, the deck block is 4,863 words across ch3–ch8. Broken down:

| Block | Total | Templated (≥4 chapters) | Recoverable |
|---|---|---|---|
| Your Twenty Cards | 840 | 164 (20%) | ~137 |
| Drawing Against the Shadow | 2,639 | 192 (7%) | ~160 |
| From Card to Quest | 1,384 | **804 (58%)** | **~670** |

`Drawing Against the Shadow` is 93% chapter-specific — it is the five daemon failures for that chapter's Face, and it is good. Leave it. `From Card to Quest` is 58% boilerplate and is the single cleanest cut in the book: keep Ch3's instance whole as the teaching pass, reduce Ch4–Ch8 to the worked example and the one dread sentence, and point back.

**Total deck recovery: ~970 words**, and every one of them is mechanically identifiable rather than a judgment call.

---

## 3. THE CALLBACK SPEC

This is a momentum instrument, not a word-count instrument. Budget it as **adding** roughly 250–350 words across nine chapter seams.

### 3.1 The device, from your own prose

The book already does this correctly in five places. Two clauses: what the earlier chapter handed her, in the book's own image language, then what this chapter does with it that the earlier one could not.

> Chapter 1 put the joystick in your hands. This chapter teaches you how to walk the book. — `ch2:226`

> Chapter 1 named the fuel; this chapter is where you learn to make it. — `ch3:374`

> Chapter 1 taught you to read the meter: what a move costs you. The Shaman adds the next layer: what that spending does to the living field. — `ch3:360`

> The Shaman (Ch3) taught you to read the five EA channels: Metal/Fear, Water/Sadness, Wood/Joy, Fire/Anger, Earth/Neutrality. The Challenger uses them at a different altitude. — `ch4:179`

> You met the Polarity Map in Chapter 3. Here is the Challenger's pair. — `ch4:111`

The failing form points without refreshing, and reads as administration:

> For the full game taxonomy and mechanics, see Chapter 1. This chapter uses that frame only as a bridge into inner work. — `ch2:113`

A consistent refresher should sound the same every time it appears. The verbatim recurrence of *You met the Polarity Map in Chapter 3* at ch5:155, ch7:85 and of the meter/field pair at ch4:239, ch5:267 is correct and must be exempted from the duplicate scanner.

### 3.2 Coverage, measured

Cross-chapter references per chapter: **ch1: 3 · ch2: 4 · ch3: 10 · ch4: 4 · ch5: 2 · ch6: 0 · ch7: 3 · ch8: 0 · ch9: 3.**

Ch6 and Ch8 have zero. Ch8 is the Sage — the chapter whose entire subject is holding more than one altitude at once — and it never once looks back at the altitudes the reader climbed to get there. Ch3's ten is why it reads as connected despite being 14,857 words.

### 3.3 Where the callbacks go

Nine slots, one per seam, each at the top of the chapter before `Section 1: The Exile` fires:

| Seam | What the previous chapter handed her |
|---|---|
| Ch1 → Ch2 | the joystick, the Oath, the one she picked at `ch1:61` |
| Ch2 → Ch3 | the daemon roster, the threshold walk, the first two moves |
| Ch3 → Ch4 | the five channels, the WAVE-Spiral, 3-2-1 |
| Ch4 → Ch5 | the clean no, the line, Force↔Restraint |
| Ch5 → Ch6 | the inheritance, Honor↔Reform |
| Ch6 → Ch7 | the leverage point, Structure↔Agency |
| Ch7 → Ch8 | the field, the repair, Care↔Impact |
| Ch8 → Ch9 | game selection, altitude, the walk back |

**`The Game So Far` does not exist in the manuscript.** Zero hits across all nine chapters, despite the project glossary describing it as a recurring element with seven instances Ch2–Ch8. The council ruling that debated killing it was running on a stale instrument. **The slot it was supposed to occupy is exactly where the backward callback belongs**, which means we have a named, already-designed home for this and do not need to invent one.

Ch1 also has to plant the Forest, the daemons, and the joystick by name before its last line, and reconcile *the controls* (ch1:15, ch1:61) with *joystick* (Ch2's central image). Right now Ch1 mentions the Forest exactly once — the closing line — and the daemons and the joystick zero times, so Ch2's opening has nothing to call back to.

---

## 4. THE CUT LIST, RANKED BY YIELD AND RISK

### Tier 1 — mechanical, ~1,800 words, low risk

**T1a · `From Card to Quest` taper, ch4–ch8 · ~670w.** Keep Ch3's instance whole. In Ch4–Ch8 keep the worked example and the dread sentence, cut the app/quest pair, the Show Up row rationale, the four-part quest formula, and the *nobody can tell whether you did it* frame, and replace with a callback. Mechanically identifiable, six verbatim strings.

**T1b · Deck mechanics sentences, ch4–ch8 · ~300w.** The grid-restating sentence under `Your Twenty Cards` and the *Down is the sequence, across is where it lands* closer. Ch3 teaches the grid; the rest can name their Face's twenty and move.

**T1c · Non-refrain near-dupes outside the deck · ~800w.** From the 105 groups in §2.1, excluding the daemon-jurisdiction roster and the BAR refrain. Requires a per-group disposition pass like the Ch2 ledger, not a blind sweep.

### Tier 2 — RETRACTED

This tier proposed cutting 3,300 words from Ch8, Ch5, and Ch6 for exceeding the size the book set for each parallel section family in Ch3 and Ch4. §5.4 kills it. Neither source text bands content, and I had no evidence for the instrument when I proposed it. The band table is preserved below as a map of where the mass sits, with no cut attached to it.

| Family | Band | Excess | Where |
|---|---|---|---|
| S3 The Concept | 1,041 | 1,531 | ch3 +909 · ch8 +622 |
| S5 The Daemon | 1,722 | 1,295 | ch6 +770 · ch3 +525 |
| S1 The Exile | 725 | 1,049 | ch8 +638 · ch5 +411 |
| S2 The Distortion | 678 | 682 | ch8 +455 · ch5 +227 |
| S7 Recap | 583 | 281 | ch4 +208 · ch3 +73 |

What survives from it is narrower and better supported: **apparatus holds a fixed size, content does not.** That rule cuts two blocks, and only two — Tier 3 and Tier 4 below.

### Tier 3 — the Ch8 EA block, 1,151 words, low risk

`EA Channel Alignment — How Each Mode Moves Energy` appears in ch4 (546), ch5 (309), ch6 (756), ch8 (**1,897**). Ch3 is the teaching instance. Ch7 restructures it into the five Channel blocks.

Ch8's is 2.5× the next largest and 6× Ch5's, and it is doing the same job: five paragraphs mapping five modes onto the five channels. **Excess over the ch6 ceiling: 1,141 words.** This is the single largest identified overrun in the manuscript.

Ch4's instance opens with the correct callback (`ch4:179`). Ch6's and Ch8's drop the table cold. Fixing that is §3 work; cutting Ch8 to band is this tier.

Section 4 is 22,691 words and I have only accounted for 1,151 of it here. §5.5 is why the rest is not a structural target: Elliott's application section is 22,161 words, so this book's Practice mass is within 2.4% of its closest comparable. The remainder comes out at the line or stays in.

### Tier 4 — the recap cap, 833 to 1,545 words, low risk

Chou recaps every chapter of a 481-page book in **105 words and five bullets.** The `What the [Face] Teaches` bodies run 253 to 793 words, average 508, and measure 2% templated — they are not repeating each other, they are each individually long. Ch5 does the job in 253, so the floor is the book's own.

A 400-word cap takes 833 words out of ch3, ch4, and ch6. A 250-word cap takes 1,545 out of five chapters. Your call on which, and it is the cheapest structural cut left on the board.

### What this totals

| Item | Words |
|---|---|
| T1 mechanical — deck taper, deck mechanics, non-refrain dupes | 1,770 |
| T2 band normalization | **retracted** |
| T3 Ch8 `EA Channel Alignment` to band | 1,151 |
| T4 recap cap at 400 words | 833 |
| Callbacks (added) | −300 |
| **Structural subtotal** | **3,454** |

Plus the line audit at its measured rate — Ch2 returned 1.8% — applied across the remaining 91,600 words is another **~1,650**. Call it **5,100 words, or 5.4%**, and 95,075 becomes roughly 90,000. Taking the 250-word recap cap instead moves it to **5,800 and 5.6%**.

That is a smaller number than the one I gave you this morning, and the reason is in §5.4: the source comparison took away a 3,300-word instrument and gave back 833. I would rather hand you 5,100 words I can defend than 7,400 I cannot.

---

## 5. THE SOURCE-TEXT COMPARISON

Both texts are now in hand. **Yu-kai Chou, *10,000 Hours of Play* (Octalysis Media, 2025)** and **Carolyn Elliott, PhD, *Existential Kink* (Weiser Books, 2020)**.

A caveat on the evidence before the findings. The Chou extraction runs 8,497 words and stops mid-Chapter 1 at page 19, so the Chou half of this comparison rests on his table of contents, which is complete and carries page numbers for every subsection. That gives me his architecture and his block sizes in pages. It does not give me his prose. The Elliott extraction runs 58,176 words and is substantially complete, so her half rests on measured text.

### 5.1 Elliott quarantines everything

Body word counts, measured:

| Unit | Words | Share |
|---|---|---|
| Preface + Prologue | 2,748 | 5% |
| **Part One — teaching** (Shadow, The Unconscious, Lessons 1–3) | **18,644** | **33%** |
| **Lesson 4 — application** (12 exercises, the whole of Part Two) | **22,161** | **39%** |
| Interludes 1 and 2 — testimony | 7,769 | 14% |
| Part Three — Q&A | 4,213 | 7% |
| Appendix — reference | 1,415 | 2% |
| **Body total** | **56,950** | |

Each function lives in exactly one place. Teaching happens in Part One and never again. Application happens in Lesson 4 and never again. Testimony is pulled out of the argument entirely into two Interludes. Questions go in the back. Reference goes in the appendix.

The consequence is that Elliott carries **zero recurring per-chapter apparatus**. No chapter recap, no per-chapter exercise block, no per-chapter reference table. When she needs the reader to remember the Seven Axioms, she names them and moves.

Her twelve exercises run from **459 words to 5,947 words** — a thirteenfold spread inside a single parallel family. She does not band them.

### 5.2 Chou fixes the apparatus and lets the content run

Chapter spans and apparatus, from the TOC page numbers:

| Ch | Pages | Fixed apparatus | Apparatus pp |
|---|---|---|---|
| 1 | 22 | Turn to Play 35 · Highlights 36–37 | 3 |
| 2 | 31 | Turn to Play 62 · Highlights 67–68 | 3 |
| 3 | 63 | Turn to Play 102, 120 · Highlights 130–131 | 4 |
| 4 | 51 | Turn to Play 156, 173 · Highlights 181–182 | 4 |
| 5 | 83 | Turn to Play 214, 242 · Highlights 264–265 | 4 |
| 6 | 44 | Turn to Play 292 · Highlights 308–309 | 3 |
| 7 | 55 | Turn to Play 333 · Highlights 363–364 | 3 |
| 8 | 47 | Turn to Play 394 · Highlights 410–411 | 3 |
| 9 | 63 | Turn to Play 471 · Highlights 472–474 | 4 |
| 10 | 7 | none | 0 |

**Chapter length varies 22 to 83 pages — a 3.8× spread. The apparatus never varies.** `It's Your Turn to Play` is one page every time it appears, twelve times. `Chapter N Highlights` is two pages every time, eleven times. I measured the one Highlights block that survives in the extraction: **105 words, five bullets.** In a 481-page book.

Three further things his structure does that bear directly on us:

**He teaches the frame once.** The Six Steps to Master Your Game are laid out at page 22 of Chapter 1 and never re-explained. Chapters 2 through 8 each *are* one step. That is the transcend-and-include architecture you described, executed by the closest structural comparable this book has.

**He varies the label where the content is unique.** All twelve `It's Your Turn to Play` blocks carry distinct subtitles: Talent Triangles, Skill Triangles, Slay The Scary Dragon, Your Hero Name and Hero Code. The reader recognizes the slot and still gets told what is in it.

**His closer carries no apparatus at all.** Chapter 10 is seven pages, and it drops the Turn to Play block, the Hero Profile, and the Highlights. Your ruling that Ch9 does not go back to the deck has an outside precedent.

His `OP Hero Profile` is not apparatus. It runs 4 to 29 pages and carries a different life each time, so it is content sitting in a recurring slot — the same category as your Exile sections.

### 5.3 MTGOA measured against both

Every recurring labeled block in ch3–ch8, with its spread:

| Block | n | Total | Min | Max | Spread |
|---|---|---|---|---|---|
| EA Channel Alignment | 5 | 3,573 | 51 | 1,908 | **37×** |
| Polarity Encounter | 6 | 2,706 | 367 | 508 | 1.4× |
| Drawing Against the Shadow | 6 | 2,639 | 374 | 494 | 1.3× |
| From Card to Quest | 6 | 1,258 | 190 | 248 | 1.3× |
| What You Take Out of the Forest | 6 | 1,278 | 126 | 270 | 2.1× |
| What Winning Looks Like | 7 | 1,111 | 59 | 204 | 3.5× |
| Your Twenty Cards | 6 | 840 | 82 | 183 | 2.2× |
| **Fixed apparatus total** | | **13,405** | | | **14.1% of the book** |

Against the comparables: **Chou 6.7%. Elliott 0%. MTGOA 14.1%.** The book carries roughly twice the per-chapter apparatus load of its closest structural neighbor.

The good news inside that number is that six of the seven blocks are already disciplined. `Drawing Against the Shadow`, `From Card to Quest`, and `Polarity Encounter` sit inside a 1.3–1.4× spread, which is tighter than anything Chou does by hand. The book already knows how to hold a block to size.

`EA Channel Alignment` is the exception, at 37×.

### 5.4 What the comparison changes

**It kills Tier 2.** Neither source bands content. Elliott lets a parallel family run 13×; Chou lets his chapters run 3.8×. Both hold their *apparatus* to a fixed size and let the *content* be as long as the content is. Cutting Ch8's Concept section or Ch6's Daemon section because they exceed a band the book set in Ch3 has no support in either comparable, and I proposed it without one. **Retract 3,300 words from the ceiling.**

**It hardens the Ch8 EA cut.** That block is apparatus by every test — same job in every chapter, five paragraphs mapping five modes onto five channels — and it broke its own band by 37×. Both sources say apparatus holds a fixed size. **1,151 words stands.**

**It opens the recap.** Chou's chapter recap is 105 words. MTGOA's `What the [Face] Teaches` bodies run 253 to 793, averaging 508, and measure **2% templated**, which means they are not repeating each other; they are each individually long. Ch5 does the job in 253 words, so the book has already proved the job can be done in 253 words. A 400-word cap recovers **833**. A 250-word cap recovers **1,545**.

**The deck quarantine is smaller than it looked.** I tested the Elliott move — pull the deck instruction into one back-matter section, leave each chapter its grid and its five daemon failures. Measured templated share: `From Card to Quest` 62%, `Your Twenty Cards` 10%, `Drawing Against the Shadow` 7%, `Polarity Encounter` 1%. The recoverable mass is 761 words, and it is already counted as T1a. **There is no second harvest here.**

### 5.5 The finding I did not expect

MTGOA's teaching mass — Sections 1, 2, and 3 across ch3–ch9 — is **18,041 words**. Elliott's teaching mass is **18,644**.

MTGOA's application mass — Section 4 — is **22,691 words**. Elliott's application mass is **22,161**.

Both within 3%. The book's two largest functional blocks are sized almost exactly like the closest comparable on the shelf, written by an author with the same audience and a working publisher behind her.

That means the manuscript is not long because of its architecture. It is long because it carries 13,405 words of per-chapter apparatus where Chou carries half that and Elliott carries none, and because the prose inside every block is verbose at the line.

**There is no structural cut of ten thousand words in this book.** The three structural moves left — the Ch8 EA block, the recap cap, and the deck taper — total under 3,600 words between them. Everything past that comes out at the line or stays in.

You have been saying this since the compression conversation. The comparison confirms it.

### 5.6 The fourth corpus — *Igniting Joy*

The three-book comparison was missing the only control that could settle a voice question: a book you already wrote. *Igniting Joy: Transforming Anger's Fire into Creative Passion via Humor* went through the same instrument as the other three.

The sample is now the whole book. The 121-page PDF was re-extracted from source: reading order rebuilt line by line so the bold runs sit back inside their sentences, the three true two-column pages ordered by column instead of by height, and the Type3 font's broken character map repaired (it renders *fi* as *y* and *fl* as *z*, which is why the earlier text was full of `conzict` and `difycult`). That yields 24,735 words of correctly ordered manuscript. Stripping headings, bullets, the per-chapter BARs-challenge apparatus and the 52-card appendix leaves **20,077 words of running prose** — four times the sample every number in the previous draft of this section rested on.

| | MTGOA | Igniting Joy | Elliott | Chou |
|---|---|---|---|---|
| Words measured | 90,263 | 20,077 | 50,766 | 5,109 |
| Mean sentence length | 13.4 | 18.8 | 23.7 | 22.5 |
| Median | 11 | 18 | 19 | 19 |
| Sentences ≤ 6 words | **27.5%** | **4.2%** | 12.4% | 12.8% |
| Commas per sentence | 0.53 | 1.12 | 1.41 | 1.62 |
| Subordinate-clause openers | 4.1% | 9.6% | 9.0% | 9.3% |
| Copula per 1k | 62.8 | 28.8 | 40.9 | 41.1 |
| Em-dash per 1k | 13.0 | 5.4 | 4.2 | 0.0 |
| Hedges per 1k | 6.2 | 2.8 | 12.2 | 5.9 |
| you / your per 1k | 39.2 | 56.1 | 35.5 | 24.9 |
| we / our / us per 1k | 1.7 | 8.2 | 12.3 | 4.1 |
| I / me / my per 1k | 11.6 | 4.0 | 34.0 | 22.7 |
| Sentences opening And / But / So | 1.0% | 1.9% | 10.1% | 5.3% |
| Flesch reading ease | 73.7 | 47.2 | 54.9 | 53.8 |
| Grade level | 6.3 | 11.3 | 11.5 | 11.3 |

Sentence-length distribution, share of sentences by band:

| Band | MTGOA | Igniting Joy | Elliott | Chou |
|---|---|---|---|---|
| 1–6 words | 27.5% | 4.2% | 12.4% | 12.8% |
| 7–10 | 21.6% | 8.8% | 11.9% | 12.3% |
| 11–14 | 15.7% | 16.7% | 11.8% | 11.0% |
| 15–19 | 13.1% | 25.5% | 14.2% | 16.7% |
| 20–26 | 11.4% | 30.2% | 16.7% | 15.9% |
| 27–35 | 7.2% | 12.3% | 14.5% | 18.5% |
| 36+ | 3.4% | 2.3% | 18.6% | 12.8% |

*Igniting Joy* lands beside Elliott and Chou on length and grade, and tighter than either on copula density and hedging. MTGOA sits outside all three on the short end. The distributions are close to inverted: your previous book puts 55.7% of its sentences in the 15-to-26-word band and 4.2% at six words or fewer; MTGOA puts 24.5% in that band and 27.5% at six or fewer. The correct sample moved that reading further apart, not closer: on the four-times-larger text the mean rose from 17.9 to 18.8 and the short-sentence share fell from 4.9% to 4.2%.

The tightest ratio in the table is the copula. MTGOA runs *is / are / was / were* at 62.8 per thousand against 28.8 — 2.2 times the rate. Every one of those is a sentence built as **X is Y** rather than as a sentence where somebody does something. Hedging runs the same 2.2 ratio, 6.2 against 2.8. The em-dash gap widened once the real text came in: 13.0 against 5.4, so MTGOA reaches for the dash 2.4 times as often as you did.

Two further readings that are measurements, not recommendations. First, person: *we / our / us* runs at 8.2 per thousand in *Igniting Joy* and 1.7 in MTGOA, while *I / me / my* runs 4.0 against 11.6. Your previous book is written from a *we* that this manuscript almost never uses, and this manuscript is written from an *I* that your previous book almost never uses. Second, *you / your* runs 56.1 against 39.2 — the control text is on the reader harder than the manuscript is.

One metric in the table has to be read with a caveat, and one has to come out of it. The colon comparison is not clean: *Igniting Joy* sets its run-in labels in bold rather than on their own line (`How to Do It:` alone accounts for 29 of them), and the extraction folds those back into the paragraph, where the MTGOA filter would have stripped the equivalent as a heading. So the colon rate is measuring the book's typography, not its sentences, and I have pulled it from the table. The And/But/So figure is the one that changed direction. The damaged sample read 5.2%; the real text reads **1.9%** against the manuscript's 1.0%. You do open sentences that way, at roughly twice the manuscript's rate, and it is nowhere near a defining feature of your prose. The conflict I recorded between the voice rule and the control text was mostly an artifact of a broken sample.

**What the register repair returns in words.** Twelve real adjacent pairs, rewritten to the connective pattern the control text uses, measured: 182 words in, 161 out, mean **−1.75 per site**. The detector finds **464** pairs of that shape book-wide, of which 67 are true restatements. The whole narrow pool is therefore worth about **810 words**. A wider pass reaching into the 1,961 sentences of six words or fewer might reach 1,500 to 2,000. The register repair is a voice move that returns some words, not a word-count move.

**Housekeeping:** the source-analysis stub in the project credits *Existential Kink* to "Bob Elliott." It is **Carolyn Elliott, PhD**, confirmed against the title page of the text you sent. The manuscript has it right at `ch2:35`. If back matter or a bibliography ever gets generated from that library, it ships wrong.

---

## 6. WHAT I NEED FROM YOU

1. **Tier 1 — go or no.** Mechanical, ~1,770 words, and I can produce the ledger the way I did for Ch2.
2. **Tier 3 — Ch8's `EA Channel Alignment` to band.** 1,908 words down to Ch6's 757. The apparatus rule from §5.2 says yes. Ch8 being the last teaching chapter is the only argument I can see against it.
3. **Tier 4 — recap cap at 400 or at 250.** Chou's is 105.
4. **The callback slots — all nine, or start with Ch6 and Ch8** (the two at zero) and Ch1's plant?
5. **Protect list confirmation:** the daemon-jurisdiction roster, *Two minutes to capture it as a BAR*, *You met the Polarity Map in Chapter 3*, and the meter/field pair are exempt from the duplicate scanner as intentional refrains.
6. **The line audit is now the whole game.** §5.5 says structure gives us 3,454 words and nothing more. If you want the manuscript meaningfully shorter than 90,000, the remaining passes have to be line-level compression across ch3–ch9 at the rate Ch2 returned, chapter by chapter, on the Three Keep-Tests. Confirm that is where the last four days go.

---

## 7. WHAT I GOT WRONG EARLIER IN THIS ANALYSIS

The Exile/Distortion cold starts were carried into this session as a 7,093-word cut target on the strength of a coarse concept-frequency detector that flagged *Village* at 86 definition-events across 8 chapters, clustered at chapter tops. That number is real. The inference from it was not. Measured at the sentence level, those sections are **3% templated**, which means they are seven different pieces of teaching that happen to share an opening cadence, not seven copies of the same passage.

I should have run the sentence-level test before carrying the figure forward. The concept detector locates masses. It does not identify duplication, and I used it as if it did.

The second one is Tier 2. I built band normalization out of a table I made — the size each parallel section family happened to reach in Ch3 and Ch4 — and presented it as an editorial instrument worth 4,838 words. I flagged that it needed your ruling, which was the right instinct and the wrong response. The right response was to go find out whether any book that works does this. Two of them were sitting in the project waiting to be read. Neither does it. Elliott's twelve exercises span thirteenfold and Chou's chapters span nearly fourfold, and both books are better for it.

The third one you caught yourself. I wrote that the short declarative register *is* your voice, and it is not — it is the register this manuscript drifted into, and I was the one holding the pen for most of that drift. It is the second time in this project I have handed you prose I generated and described it back to you as something you built. The And/But taxonomy was the first. Calling it yours converts a defect into an asset and protects it from the pass that should be removing it. The control text settles the question at 4.2% against 27.5%.

The fourth one you also caught. Every number in the first version of §5.6 was computed on 4,779 words of a text file whose extraction had torn bold runs out of the middle of sentences and dropped them below the paragraph. You said you could not trust it, and you were right. The re-extraction from the PDF recovered 24,735 words in correct order. Most of the readings survived and two widened, but the And/But/So figure fell from 5.2% to 1.9%, which retires a conflict I had put in front of you as a ruling to make. A finding built on a sample I never audited is the same failure as a finding built on an instrument I never tested.

The pattern in all four mistakes is the same: I built a number out of an instrument I had made myself, and I carried it forward without testing the instrument. The Three Keep-Tests apply to my own findings, not only to your sentences. Two corollaries. When a feature of the prose needs defending, check whose hand put it there before defending it. When a number decides something, check the sample it came from before it decides anything.
