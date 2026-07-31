# SPEC — Excepting a named block, not just a whole file

**2026-07-31.** Wendell: *"I'm certain it takes less than that. Give me a spec for how to make
this change and I'll assess how long it will take."*

He is right to push. **I wrote "costs an afternoon" with nothing behind it**, which is the
estimate equivalent of the thing this repo keeps catching: a number typed rather than
measured. This document is the material to judge it on instead. No estimate appears in it.

---

## 1 · The problem, stated exactly

`prose_diet.REGISTERS` grants a raised ceiling **per file**. Quill's charter is **409 words
inside a 10,000-word `ch5.md`**, so the exception fires when the draft file is scored and
never when the chapter is. Measured today: ch5 reports `passive 1.83`; excise the charter and
the same chapter reports `1.42`. The counter will keep reporting 1.83 and the reason will keep
being correct, which is the worst state for an instrument to be in — accurate, unactionable,
and permanently ignored.

The same shape applies to anything the book embeds in a different register: the six handbooks
before `BLOCK` learned to strip them, a ch3 casebook entry, ch8's five signed margin notes.

## 2 · Option A — anchor-pair blocks. The minimal change.

### The data

`REGISTERS` gains an optional `blocks` list. Each entry is a start anchor, an end anchor, its
own ceilings, and a reason:

```python
"ch5.md": {
    "blocks": [{
        "start": "**Clause four.**",
        "end":   "It records no case of a keeper who stopped attempting it either.",
        "zombie": 1.60, "be": 1.60, "expletive": 2.00, "passive": 2.00,
        "why": "Quill's annotated charter. Same ruling as CH5_REGISTER, 2026-07-31.",
    }],
},
```

Anchors are literal strings, not regexes, and both must match **exactly once**.

### The code

Three edits inside `instruments/prose_diet.py`, which is 285 lines today.

**1. A new function**, next to `register_for` at line 156:

```python
def split_blocks(text, spec):
    """Return (body, [(block_text, block_spec), ...]).

    A block anchor that matches zero times or more than once is a HARD ERROR rather than a
    silent pass. A register is an exemption, and an exemption that stops applying without
    saying so is how a defect gets licensed by accident."""
    out = []
    for b in spec.get("blocks", []):
        for key in ("start", "end"):
            if text.count(b[key]) != 1:
                raise SystemExit("register anchor %r matched %d times"
                                 % (b[key][:50], text.count(b[key])))
        i = text.index(b["start"])
        j = text.index(b["end"]) + len(b["end"])
        out.append((text[i:j], b))
        text = text[:i] + text[j:]
    return text, out
```

**2. `main()`'s per-file loop**, line 239. Today it scores `t` once. It becomes: split, score
the body against `BASE`, score each block against the block's own ceilings, print the block as
an indented second row.

**3. The `-v` site listings**, lines 260, 268 and 276. Each re-reads the file and would report
sites inside excepted blocks. Each needs the same split applied.

**Reference points for size.** The three `-v` loops are four lines each. The function above is
sixteen lines as written. The `main()` change touches the body of one `for` loop. `register_for`
already exists and is unchanged.

### What can go wrong, and what catches it

| risk | what stops it |
|---|---|
| an anchor drifts when the prose is edited | the hard error above. It fails loudly rather than silently scoring the block into the body |
| a block is scored twice, in the body and on its own | `split_blocks` removes it from `text` as it goes |
| `-v` reports sites inside an excepted block | edit 3. If skipped, the counters are right and the site list lies |
| exemptions spread by copying | unchanged from today: an unnamed file gets `BASE`, and only Wendell rules a register |

### How it gets verified

1. `python3 instruments/prose_diet.py` — ch5 body reads **1.42** on passive, not 1.83, and the
   charter appears as its own row.
2. Every other chapter's numbers are **unchanged**, which is the real test: a file with no
   `blocks` key must take the identical path it takes today.
3. Break an anchor on purpose. The run must fail, not pass.

## 3 · Option B — split every chapter at the seam instead

Worth stating because it may be the better change and it is not much larger.

**The whole book is two voices and one baseline.** Sections 1 to 3 are a Head's treatise,
Sections 4 to 7 are Wendell. They are measured against a single ruler built from Wendell's
expository prose, which means every Head is scored against a register they were written not to
share.

`instruments/seam_sweep.py` already computes the boundary, in `sections_1_to_3`, and
`marginalia/compile.py` already has `seam_point`. Option B imports one of them and reports two
rows per chapter, treatise and author. It replaces the block mechanism for the six handbooks,
the ch5 register and the ch3 casebook entry at once, because all of them are above the seam.

**It does not replace Option A entirely.** ch5's charter sits above the seam, so B covers it;
a future excepted block below the seam would still want A.

**What B needs that A does not:** a second baseline. `BASE` was measured on whole chapters, so
a treatise-only ruler has to be measured before it means anything, and per-Head is probably
the honest unit rather than per-book.

## 3a · Implemented 2026-07-31, and what it found

Wendell: *"let's do option A. And implement it now."* Built as specced. All three checks pass.

| check | result |
|---|---|
| ch5's body reads 1.42 on passive, charter as its own row | **yes.** 1.83 to 1.42, and `block 1` prints indented beneath it |
| every other chapter byte-identical | **yes.** The diff is one line and it is ch5's |
| a broken anchor fails the run | **yes.** `exit 1: register anchor '**Clause forty.**' matched 0 times, expected 1` |

**The ceilings in §2 of this document were guesses and two of them are wrong.** Measured on
the 399-word charter, against the book per thousand:

| counter | measured | the ceiling I wrote | verdict |
|---|---|---|---|
| be | **1.40x** | 1.60 | holds |
| copula | 1.25x | none, so 1.30 | holds |
| waste | 0.85x | none | holds |
| zombie | **1.84x** | 1.60 | **too low** |
| expletive | **1.89x** | 2.00 | holds, barely |
| passive | **11.32x** | 2.00 | **too low by a factor of five** |

**The ceilings stay as written and the block reports heavy.** Raising a ceiling to whatever
the prose happens to measure is not a ceiling, it is a rubber stamp, and
`SPEC_EMDASH_AND_DENSITY` §3 already rules that case: *"it cannot be raised to make a batch
pass."* **Only Wendell rules a register.**

**What the 11.32 actually says.** Fourteen passives in 399 words is thirty-five per thousand
against the book's 3.1. That is not drift and it is not a near miss; **an annotated charter
runs an order of magnitude more passive than expository prose**, because stating what shall be
done without naming who does it is the entire grammatical form. The number is larger than I
guessed when writing §2 and larger than the ch5 classification implied. It is the strongest
single piece of evidence that a per-register ruler is the right idea, which is Option B's
argument arriving from Option A's data.

**The ruling needed:** set the charter's `passive` ceiling from the measurement, at 11.32 or
just above, or leave it reporting heavy as a standing note that this passage is measured by
the wrong ruler. Either is defensible. Neither is mine to take.

## 4 · The recommendation

**Option A, and not before the book ships.** It is the smaller change, it closes the exact hole
that was found, and its failure mode is loud. Option B is the better idea and needs a baseline
measured first, which is the part that would take real time and is not urgent tonight.

**Nothing about ch5 is wrong.** §5 of `SPEC_EMDASH_AND_DENSITY` classified all 48 passives:
fourteen are the charter, sixteen are inheritance vocabulary that has no active form, several
are the exile fable withholding its agent on purpose, and two or three are genuinely fixable.
This change makes the instrument stop reporting a number nobody should act on. It does not
improve a sentence.
