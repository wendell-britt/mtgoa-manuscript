# Collision audit — the four canon terms

**Wendell 2026-08-03:** *"collision audit on the four canon terms first."*

Run after his catch on `ch4:712` — *"'closing out a no' … what is a no?"* — which turned out
not to be vagueness but a **referent collision**: `no` meaning the Challenger's refusal at
16 sites, and a hiring rejection at 2.

`empty_head.py` cannot see this class. It counts head nouns. A collision is one *contentful*
word doing two jobs, which is the ch7 `field` finding and now the ch4 `no` finding. The
method here is the one that worked on `field`: count, split by source domain, and look for
the sites where the two senses sit close enough to touch.

**No prose changed.**

---

## The measurement

| | ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **line** | 7 | 4 | 26 | **159** | 13 | 5 | 6 | 35 | 15 | **270** |
| **read** | 8 | 23 | **89** | 17 | 15 | 17 | 17 | 47 | 13 | **246** |
| **charge** | 10 | 7 | 28 | **72** | 5 | 7 | 28 | 6 | 0 | **163** |
| **board** | 3 | 1 | 0 | 0 | 1 | 0 | 0 | **31** | 1 | **37** |

Three of the four collide. `read` does not, and the reason is worth keeping.

---

## 1 · `line` — **the worst finding, and it is in the instructions**

`line` means the Challenger's boundary at roughly 154 sites, 102 of them in ch4. It also
means **a line of text on a worksheet**, and that second sense lives in the two most
repeated instructions in the book:

- **`One line: what you will do, who it reaches, by when, and what it costs you.`** — the
  quest formula, in **ch3, ch4, ch5, ch6, ch7 and ch8**.
- **`Add a line to the sheet.`** — the between-chapters instruction, in **ch2, ch3, ch4,
  ch5, ch6, ch7 and ch8**.

Both are fine in seven chapters. **In ch4 they are not**, and `ch4:795` puts both senses
twelve words apart:

> **Add a line to the sheet.** Under the channel you skip, **write the line you have not
> drawn**: what you owe a specific person and have been softening since before you picked
> up this book.

*Add a line* = write a row. *The line you have not drawn* = the boundary. In the chapter
that spends 102 instances teaching the second meaning, the sentence opens with the first.

`ch4:752` has the same shape, softer: *"**One line**: what you will do… ***Draw the Line***
becomes:"*

**And I made this worse today.** The `thing` sweep standardised `One line, four things:` to
`One line:` in five chapters, on the correct reasoning that the colon already names the four
elements. That fix is right everywhere and it removed the one word — `things` — that was
signalling *a line of text* rather than *a boundary*. The formula is now maximally ambiguous
in exactly the chapter where it matters.

**RULED 2026-08-03 — Wendell: *"do the line fix, one sentence and add a row."*** Applied by
`instruments/line_collision.py`, 13 sites across seven chapters:

    One line: / Write yours in one line:   ->  One sentence:          6 sites
    Add a line to the sheet                ->  Add a row to the sheet 7 sites

Both replacements are more accurate as well as unambiguous. `ch9:508` already defines the
artifact as *"said in a sentence a stranger could repeat"* and `ch4:712` already writes *"One
sentence of line and one of offer"* — the formula was asking for a sentence and calling it a
line. And the sheet is a table built across the book (myth, daemon, channel, line,
inheritance, harm, walk-away price, game), one entry per chapter, so a row is what it takes.

`line` now means the boundary everywhere in the manuscript except `ch2:328` and `ch7:77`,
which are the boundary sense too.

---

## 2 · `charge` — a collision of exactly two sites, and it may be deliberate

`charge` is Emotional Alchemy's coined term, kept by a 6-Face council in June specifically
because it *"grants agency"*, and it runs 163 times as energy.

It also means **to bill**, at two sites, both in ch7's Victim material — which is the one
passage in the book built on an accounting metaphor (*ledger, account, balance, refinance,
entries, spend*):

> `ch7:588` — *"it lets you know exactly what your presence costs and **decline to bill for
> it**"*
> `ch7:590` — *"only a cost you can name and **do not charge for** reads as a choice"*

ch7 runs `charge` in the energy sense 28 times, including inside this same section.

**RULED 2026-08-03 — Wendell: *"do the charge and board collisions."*** Not a pun, so
`charge` gives the accounting slot up:

> `ch7:590` — *"only a cost you can name and **do not bill for** reads as a choice"*

The fix was already sitting in the same paragraph. `bill` appears two sentences earlier in
*"decline to bill for it"*, so the passage had picked its accounting verb and then reached
for `charge` on the restatement. One word changed, and `charge` now means energy everywhere
in the manuscript.

The repetition of `bill` across the two sentences is deliberate: they are the same claim
stated twice, once as the Victim's capacity and once as the reason it matters, and matching
the verb makes the parallel visible.

---

## 3 · `board` — one site, and it is a different institution

`board` is game furniture: `the whole board` at 31 sites in ch8, plus 5 elsewhere, all the
game.

`ch5` uses it once for a governance body:

> *"handing the community fund to Marcus, who has run nothing this size and **did not come
> up through the board**"*

That is a board of directors, in a book where `the board` is where the pieces are. The only
site in the manuscript where `board` means an institution.

**RULED 2026-08-03, same instruction.** → *"did not come up through the **committee**."*

`committee` over `council`, which was the first candidate: ch5's six councils are all the
village fable's, and the Marcus scene is a present-day handover. Borrowing the fable's word
for it would trade a small collision for a larger one. `committee` is unused in ch5 and
carries no game sense anywhere in the book.

`board` now means the game board at all 37 sites.

---

## 4 · `read` — **not a collision, and the reason matters**

`read` splits as *the Shaman's perception* (roughly 60 sites, 53 in ch3) against *reads as
X* (16 sites, spread across ch5, ch7 and ch8), plus a handful of *read this book*.

**`reads as` is the same source domain seen from the other side.** *You read a situation*
and *it reads as aggression* are one act described from the perceiver and from the
perceived. Nothing has to be told apart, because a reader who understands one understands
the other automatically.

This is the control case for the audit. `field` had two source domains — physics and
terrain. `no` had two referents — a refusal and an outcome. `line` has two — a boundary and
a row of text. `read` has one domain and two voices, which is what a healthy dense term
looks like, and it runs at 246 without confusing anybody.

**So density is not the signal.** `read` at 246 is clean; `board` at 37 has a defect. What
matters is whether the second sense comes from a different place.

---

## 5 · What this says about the instrument

`empty_head.py` finds placeholders. It found 266 and the sweep cleared half.

**Every genuine ambiguity Wendell has caught by hand this week was the other class** — a
contentful word with two referents. `field`, `no`, and now `line`. The instrument is blind
to all three, because in each case the noun is doing its job and the problem is that it is
doing two of them.

A counter cannot detect this: it needs to know which referent is meant, which is a reading
task. What *can* be mechanised is the **proximity flag** — a canon term appearing within N
words of a different sense of itself, given a hand-built sense list per term. That is how
`ch4:795` would have surfaced without anybody reading ch4.

Worth building only if a third collision turns up. Two so far were found by Wendell reading,
which is currently cheaper.
