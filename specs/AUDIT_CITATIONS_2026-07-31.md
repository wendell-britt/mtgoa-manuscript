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

- ~~**Meadows and *leverage point*.** Not a borrowing.~~ **WRONG, and corrected an hour
  later.** I read two of eighteen hits and generalised. ch6:122 does mock the phrase as
  jargon and it is the only hit that does. ch6:261 asks *"where is the actual leverage
  point?"*, ch6:349 says *"you will have a leverage point before you have a channel"*, and
  ch6:512 sets *"the leverage point instead of the brute-force push"* against the Architect's
  five moves. That is the concept carrying weight, and Appendix G was right where I was
  wrong: it *"runs through the Architect chapter as a term of art, and it is hers."* The
  pattern is restored, and ch6 now carries an attribution below its seam, the same fix
  Appendix F got. **Eighteen uses of a coined term with the author named nowhere was the
  second-largest finding in this audit and I nearly closed it as a false positive.**
- **wu xing.** ch3:431 carries a full, bolded confession of the borrowing and what was
  changed. Kaptchuk is a further-reading pointer rather than the source, so his living only
  in Appendix G and `copyright.md` is correct.
- **Gendlin and *felt sense*, 8 hits.** Credited in Appendix G, which is where Appendix G
  says this kind of debt goes.
- **Laloux.** Named at ch8:256 as of 2026-07-30. The remaining issue is its position, §4.
- **Elliott and *Existential Kink*.** Named in ch1, ch2, ch3 and `copyright.md`.
- **Wilber.** Named in the author's note, ch3:596 and ch8:254.

## 6 · Wendell's rulings, applied

**Carse is now in ch1**, one paragraph, seated where the chapter argues that a chore model
burns people down. The finite and infinite distinction is stated plainly and then used: allyship
has no finish line, nearly everything built to support it is finite, and burnout is what it
feels like to run finite equipment on an infinite road. It pays off the chapter's title, which
was standing there uncredited the whole time. ch1's em-dash count is unchanged and still at cap.

**The three ch8 attributions are below the seam.** The Big Mind paragraph was already a lineage
note rather than treatise, so it moved whole and grew: it now credits Merzel, Wilber and Laloux
together at the head of Section 4, in Wendell's voice, where credit belongs. Above the seam Orr
states the two principles without the names, which the Earth-travel ruling allows and which
CREDIT requires. ch8's BOOK and CREDIT hits both go to zero.

**The separation of tasks is named**, in the Kishimi entry, as the discipline underneath the
book's one non-negotiable rule.

**Two states that will keep being reported, on purpose.** *Evolutionary purpose* and *Teal* now
appear above ch8's seam with the credit sitting below it, which is exactly what the two-hands
rule asks for and exactly what a 400-character window cannot see. Leaving them visible is
correct: if the lineage note is ever cut, the finding should come back.

**Watts is the one thing left.** Appendix G still credits him as the philosophical ground of
the game frame and he appears nowhere. Unlike Carse he has no single distinction to seat, so
the honest options are still to use him or to move him to a further-reading line.

## 7 · What the instrument reports now

```
0 uncredited, 7 borrowed, 3 dead
```

The seven BORROWED are all cleared in §5 and remain reported on purpose: the tier is
judgement rather than measurement, and a future edit could turn any of them back into a real
finding. `EXEMPT_DEAD` carries a recorded reason per entry, which is `gate.py`'s convention.
