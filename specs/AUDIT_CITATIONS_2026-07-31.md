# AUDIT — every named source in the book, against Appendix G

**2026-07-31.** Commissioned by Wendell. `AUDIT_GAME_LOOP_CONFORMANCE` §4 named this *"the
first thing a hostile reviewer opens with, and also the cheapest thing to fix."*

Instrument: `instruments/citation_audit.py`. Surfaces are the build spine only, marginalia
stripped. Every count below is a grep.

---

## 0 · The finding, in one paragraph

**One genuine uncredited source, and it is fixed.** ch3 quotes a specific claim from *The
Courage to Be Disliked* and Appendix G had no entry. **Two attributions were missing from
pages that are built on the thing being attributed**, and one is fixed. **Four credits in
Appendix G point at sources that appear nowhere in the book** — that is Wendell's call, not
mine, and it is the largest remaining item. **Three attributions sit above ch8's seam**, in a
Head's mouth, where `SPEC_TWO_HANDS` says credit cannot go.

Nothing here is plagiarism. The pattern is a synthesis book whose lineage page ran ahead of
its chapters in one direction and behind them in the other.

---

## 1 · UNCREDITED — fixed

| where | what | state |
|---|---|---|
| `ch3:264` | *The Courage to Be Disliked* is quoted by title for a specific claim, *all problems are relational problems*, and the chapter then departs from it: *"I took it further. All problems are emotional problems."* Appendix G had no entry | **fixed** |

**Verified before writing the entry**, on the Laloux precedent. Ichiro Kishimi and Fumitake
Koga, Atria Books, English edition 8 May 2018, ISBN 978-1-5011-9727-7, original Japanese
title 嫌われる勇気 (*Kirawareru Yūki*). The book is a dialogue on Alfred Adler's psychology;
Kishimi is a translator of Adler into Japanese. Two independent search passes agreed on all
of it. **Not verified and therefore not stated in the entry:** the Japanese first-publication
year and the English translators' names. Every bookseller and Open Library returned 403
through the proxy, so those two are left out rather than asserted.

The entry is written to say what the book took *and* where it disagrees, because the
disagreement is load-bearing: Adler's claim is relational and Chapter 3's is emotional, and
that is a change rather than a refinement.

**One thing I did not write, because it is Wendell's to confirm.** The book's single
non-negotiable rule — *you make your move, and what the other person does with it stays
theirs* — is structurally Adler's separation of tasks. A reader who knows Adler will see it.
Whether it is an influence or a convergence is a fact about Wendell's reading that only he
has, so no claim about it went on the page.

## 2 · Attribution missing from the page it is built on

| page | source | state |
|---|---|---|
| `APPENDIX_F_POLARITY_MAP.md` | The whole appendix is Barry Johnson's polarity management, and his name appeared nowhere in it. 18 uses of the tool across four files | **fixed** — two sentences at the head |
| `ch8:230` | *"Big Mind gives this chapter its vocabulary for the inner voices."* Names the method, never Genpo Roshi (Dennis Genpo Merzel), who is in `copyright.md` and Appendix G | **open**, and see §4 |

## 3 · DEAD — credited in Appendix G, invisible in the book

Four, and this is the item that needs a ruling.

| credited | claim in Appendix G | in the book |
|---|---|---|
| **Alan Watts** | *"the philosophical ground"* of the game frame | zero. Name absent, *hide-and-seek* absent |
| **James Carse** | *"sharpened it into something usable"* | zero. Name absent, *finite game* and *infinite game* both absent. The Infinite Arcade is the book's own coinage |
| **Stephen Porges** | polyvagal, *"the architecture beneath what the chapters call old wiring"* | zero. Name absent, *polyvagal* absent |
| **Peter Levine** | somatic experiencing, *"the physiology under the charge"* | zero. Name absent, *somatic experiencing* absent |

**Why this is not automatically a defect.** Appendix G's own opening says it credits work the
chapters deliberately do not name: *"I don't use their clinical vocabulary in the chapters, on
purpose."* Under that rule Porges and Levine are correct as written, and so are Gendlin and
Johnson, whose ideas run through the book under other words.

**Why Watts and Carse are different.** Appendix G says the game frame *"isn't a metaphor I
reached for — it's a claim I inherited from four thinkers,"* and then names four. Two of them,
Chou and Nguyen, are worked hard in the author's note. The other two appear nowhere in
92,000 words. For a book titled *Mastering the Game*, having the finite-and-infinite-game
distinction credited and never used is the gap a reviewer would enjoy.

**Two honest ways to close it**, and the choice is Wendell's:

1. **Use them.** One or two sentences in ch1, where the Infinite Arcade is named, would make
   Carse's distinction visible and would pay for the credit. Watts is harder to place.
2. **Soften the claim.** Change *four thinkers* to name the two who are in the book, and move
   Watts and Carse to a further-reading line. Costs nothing and makes Appendix G true.

## 4 · Attribution above ch8's seam

`SPEC_TWO_HANDS` rules that above the signature only the Head speaks, and `seam_sweep.py`'s
CREDIT tier rules that *attribution belongs to the author rather than to a character.* ch8's
signature sits at line 280. Three attributions sit above it.

| line | text | tier |
|---|---|---|
| 230 | *"Big Mind gives this chapter its vocabulary for the inner voices."* | **BOOK and CREDIT.** Orr cannot say *this chapter*, and he cannot be the one crediting Merzel |
| 254 | *"Wilber makes the structural point: you don't abandon the lower altitudes…"* | CREDIT |
| 256 | *"Laloux names something he calls evolutionary purpose…"* | CREDIT |

All three are the same fix, and it is the one already run three times: move them below the
seam. 230 is the urgent one because it breaches twice.

## 5 · Checked and cleared

Recorded so nobody re-opens them.

- **Meadows and *leverage point*, 18 hits in ch6.** Not a borrowing. ch6:122 uses the phrase
  as the business jargon it has become and mocks people who say it without doing the work.
  Taking a phrase back from common usage is not taking it from her. The pattern is removed
  from the instrument with the reason recorded.
- **wu xing.** ch3:431 carries a full, bolded confession of the borrowing and what was
  changed. Kaptchuk is a further-reading pointer rather than the source, so his living only
  in Appendix G and `copyright.md` is correct.
- **Gendlin and *felt sense*, 8 hits.** Credited in Appendix G, which is where Appendix G
  says this kind of debt goes.
- **Laloux.** Named at ch8:256 as of 2026-07-30. The remaining issue is its position, §4.
- **Elliott and *Existential Kink*.** Named in ch1, ch2, ch3 and `copyright.md`.
- **Wilber.** Named in the author's note, ch3:596 and ch8:254.

## 6 · What the instrument reports now

```
0 uncredited, 7 borrowed, 4 dead
```

The seven BORROWED are all cleared in §5 and remain reported on purpose: the tier is
judgement rather than measurement, and a future edit could turn any of them back into a real
finding. `EXEMPT_DEAD` carries a recorded reason per entry, which is `gate.py`'s convention.
