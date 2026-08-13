# Handoff — announcing the book, in `johnair01/bars-engine`

**Written from `wendell-britt/mtgoa-manuscript` at `cc9185a`, 2026-08-10.**
**Open this in a session whose repo is `johnair01/bars-engine`.**

This exists because the two repos cannot be attached to one session — `add_repo` refuses a
cross-owner add, so the manuscript session can read `bars-engine` but cannot push to it.
Everything below was checked against a real clone of `bars-engine` at
`main`/`HEAD` on 2026-08-10, not from memory. **Line numbers and current values are quoted
so the next session can confirm nothing moved before editing.**

---

## 0 · Read this before you touch `public/`

**`johnair01/bars-engine` is a PUBLIC repository, and `public/` is served unauthenticated
at the site root.** A file committed to `public/` is (a) downloadable by anyone who guesses
or is told the URL, with no paywall in front of it, and (b) permanent in git history even
if a later commit deletes it.

The book is a paid product — `book-digital` is PWYW anchored at **$15**, `book-physical` is
**$25** preorder, `founding-ally` is **$150**. **Committing the full book to `public/` gives
it away and cannot be undone by deleting it afterward.**

So "make sure a copy of the book is in there" splits into two different asks, and only one
of them is safe to do in this repo:

| what | where it belongs | why |
| --- | --- | --- |
| the **paid** book (PDF editions, EPUB) | **Gumroad**, as the product's delivered files | Gumroad is already the commerce layer (`src/lib/launch/offers.ts`), it gates delivery on purchase, and it can be updated without a deploy |
| the **cover image** | `public/` in this repo | already public by intent — it is marketing |
| the **free sample chapter** | `public/` in this repo | already public by intent — it is the lead magnet |
| an **archival copy** of the book | the manuscript repo, which already has it, or a private store | version control for a paid artifact does not belong in a public marketing repo |

**Recommendation: do not put the full book in `bars-engine`.** Upload the files to the
Gumroad products and point the site at Gumroad, which is exactly what the offer registry was
built to do. If Wendell wants a copy in `bars-engine` anyway, that is his call to make
explicitly, knowing the book becomes free at that moment.

---

## 1 · The book's final state — the facts to quote

Everything on this line is verified on the shipping build, not estimated.

| | |
| --- | --- |
| body | 114,865 words, nine chapters |
| trade interior | 6×9in, **382 pages** — no cover, the printer wraps it |
| workbook interior | 7.5×9.25in, **390 pages** — no cover |
| trade PDF edition | **383 pages**, cover on page 1, 335-entry outline |
| workbook PDF edition | **391 pages**, same |
| EPUB | 28 documents, reflows, cover declared three ways |
| board | shipcheck SHIPPABLE · proofread 0 widow / 0 orphan / 0 stack / 0 fragment · gate PASS · xref 0/0 |
| manuscript commit | `cc9185a` on `claude/mtgoa-final-proof-1sizjz` |

**Artifacts, with checksums so the next session can confirm it has the right file:**

```
MTGOA_2026-08-10_trade.pdf           2.27 MB  sha256 eabf5d72efa1cbf1…   print interior
MTGOA_2026-08-10_workbook.pdf        2.24 MB  sha256 6c8dc2b69509589e…   print interior
MTGOA_2026-08-10_trade_ebook.pdf     4.84 MB  sha256 e69888b7c4c754d0…   PDF ebook  ← sell this
MTGOA_2026-08-10_workbook_ebook.pdf  4.83 MB  sha256 3493b2a5fcd33838…   PDF ebook, wide margin
MTGOA_2026-08-10.epub                4.63 MB  sha256 1f9d1a4a7200f794…   EPUB
```

They are in `build/` of the manuscript repo, which is **gitignored** — so they are not on
any branch. They have to be carried over by hand or rebuilt with
`python3 instruments/build_pdf.py`, `--trim=workbook`, `build_pdf_ebook.py`, `build_epub.py`.

**Nothing about the book is a preorder any more.** Both `book-physical` and the
`founding-ally` bundle still say *"ships after the print run"*, which is still true for the
printed object, but the digital book is finished and deliverable today.

---

## 2 · What the site does right now

Routes and files, all confirmed present:

```
src/app/mastering-allyship/page.tsx        501 lines   the long-form sales letter
src/app/mastering-allyship/chapter-1/      the lead magnet: email → sample chapter
src/lib/launch/offers.ts                   the SKU registry, the source of truth
src/lib/awaken/content.ts                  a SECOND, hard-coded book link — see 3.2
public/mastering-allyship/cover-front.png  1200x1800 — the OLD cover
public/launch/cover-front.png              1200x1800 — same file, same old cover
public/mastering-allyship-chapter-1.pdf    16pp — a STALE draft, see 3.3
```

**How a book CTA resolves today** (`page.tsx:39-42`):

```ts
const BOOK_OFFER_HREF = (() => {
  const offer = offerByKey('book-digital')
  return offer && isOfferLive(offer) ? offer.gumroadUrl : null
})()
```

`isOfferLive` is just *is the URL non-empty* (`offers.ts`, end of file), and the URL comes
from `NEXT_PUBLIC_GUMROAD_BOOK_DIGITAL_URL`. When it is unset, `BookPurchaseCta`
(`page.tsx:61-72`) renders a **disabled span reading "Book link coming soon."**

That design is good and should not be replaced. **The announce work is mostly filling it in,
not rewriting it.**

---

## 3 · The four findings, in the order they bite

### 3.1 — The cover on the site is the old artwork *(certain)*

`public/mastering-allyship/cover-front.png` and `public/launch/cover-front.png` are the same
file: **1200×1800**, sha `9a75d3566beb…`. The final cover is **1600×2560**, sha
`57aeb67f998b…`, and it lives at `front_matter/cover.png` in the manuscript repo.

Rendered and compared side by side: **same design, but the site's copy is missing the
tagline** *"STUCKNESS IS DATA, NOT FAILURE."* along the bottom, and it is a 1.5 ratio
against the final 1.6.

**Do:** copy `front_matter/cover.png` from the manuscript repo over both paths. They are
byte-identical to each other today, so replace both or the launch grid and the sales page
will disagree.

### 3.2 — There are two sources of truth for the book's buy link *(certain)*

```
src/lib/launch/offers.ts       gumroadUrl: process.env.NEXT_PUBLIC_GUMROAD_BOOK_DIGITAL_URL ?? ''
src/lib/awaken/content.ts:116  export const AWAKEN_BOOK_SALES_HREF = 'https://wendellbritt.gumroad.com/l/MTGOAbook'
```

The sales letter reads the registry and degrades to *"Book link coming soon"*. The chapter-1
page (`chapter-1/page.tsx`, card 2, *"Buy the full book"*) uses the **hard-coded literal**
and always renders a live "Buy on Gumroad" button.

**So the site can currently tell a reader both things at once** — one page saying the link
is coming, another selling it. The announce is exactly the traffic spike that surfaces this.

**Do:** pick the registry as the single source, set the env var, and change
`AWAKEN_BOOK_SALES_HREF` to read from `offerByKey('book-digital')` rather than a literal.
If the literal URL is the real product, it is also the value the env var should get.

### 3.3 — The free sample chapter is a materially older draft *(measured)*

`public/mastering-allyship-chapter-1.pdf` is 16 pages, PDF title *"…— Chapter 0"*, and
diffed against the shipping `manuscript/ch1.md`:

```
sample:  7,245 words        current ch1: 9,130 words        similarity: 67.7%
```

Whole passages in the sample are not in the book any more (*"I could see the pattern
clearly, and I kept playing."*, the *"You are a Game Master"* stretch). The opening line
*"This book is three years late."* does survive, so it is recognisably the same chapter —
but a third of it has changed, and it is the **first thing a new reader downloads on
announce day.**

**Do:** regenerate the sample from the final manuscript before announcing. The manuscript
repo has no single-chapter build target today; ask for one — it is a small addition to
`build_pdf.py` and the manuscript session can produce it.

### 3.4 — Preorder language now describes only the physical object *(judgement)*

`offers.ts:203` and `page-content.ts:147` both say the physical book *"ships after the print
run"*, and `preorder: true` is set. Still accurate. But `book-digital`'s blurb —
*"The book, instantly"* — is now literally true for the first time, and nothing on the page
says the book is **finished**. That is the announce's actual news.

**Do:** this is copy, not code, and it needs Wendell. See §5.

---

## 4 · The work, as a checklist for the bars-engine session

```
[ ] 1. Copy the final cover into both public paths (3.1). Confirm 1600x2560, sha 57aeb67f998b.
[ ] 2. Upload the book files to the Gumroad products (§0). Digital = trade_ebook.pdf + .epub.
[ ] 3. Set NEXT_PUBLIC_GUMROAD_BOOK_DIGITAL_URL in Vercel (all envs) — see
       docs/runbooks/GUMROAD_LAUNCH_SETUP.md and docs/ENV_AND_VERCEL.md, both present.
[ ] 4. Collapse AWAKEN_BOOK_SALES_HREF onto the registry (3.2).
[ ] 5. Replace the chapter-1 sample PDF once the manuscript session regenerates it (3.3).
[ ] 6. Apply the announce copy once Wendell rules §5.
[ ] 7. Verify: npm run validate:routes, then load /mastering-allyship and
       /mastering-allyship/chapter-1 and confirm both show the SAME live buy link.
[ ] 8. Confirm no "coming soon" state renders anywhere once the env var is set.
```

**Do not** commit the book itself to `public/` without an explicit ruling from Wendell (§0).

---

## 5 · Two decisions that are Wendell's, carried over from the proof

Both were raised when the cover arrived and neither is resolved. **Both affect site copy and
retailer metadata, so they block the announce rather than the build.**

**Subtitle.** The cover's top line is *A Field Guide*, set as an eyebrow above the title.
`front_matter/title_page.md:3` says *How to Build an Allyship Practice That Lasts*. The
Next.js metadata (`page.tsx:27-31`) uses neither — its description is the *"game you were
handed"* line. Three surfaces, three answers, and a retailer listing takes exactly one.

**The cover's tagline is not in the book.** *Stuckness is data, not failure.* is the
strongest line on the cover and the manuscript never says it. `stuckness` appears five times
and never in that shape; the nearest is `ch2:484`'s *"That location is data."* A reader who
buys on that line will look for it. Either it becomes a line in the book — new prose, which
needs the review pass — or the site should not lean on it as if it were a quotation.

---

## 6 · What could not be done from the manuscript session, and why

- **Attaching `bars-engine`.** `add_repo` returns *"cross-tier adds are not supported in v1"*
  for a different owner. Read access works — public repos are served by the git proxy — so
  everything above was verified against a real clone. **Push access was not available**, so
  no change has been made to `bars-engine` and nothing is staged there.
- **Putting the book in `bars-engine`.** Blocked by the above, and blocked again by §0,
  which is the more important of the two.
- **Regenerating the sample chapter.** Needs a single-chapter build target that does not
  exist yet. The manuscript session can add one on request.

## 7 · Where things live

```
manuscript      wendell-britt/mtgoa-manuscript @ cc9185a
                branch claude/mtgoa-final-proof-1sizjz
site            johnair01/bars-engine (public, Next.js on Vercel)
final cover     mtgoa-manuscript: front_matter/cover.png    1600x2560
artifacts       mtgoa-manuscript: build/  — GITIGNORED, carry by hand or rebuild
the full record specs/LOG_FINAL_PROOF_2026-08-09.md, sittings 1-16
open decisions  specs/STYLE_SHEET.md (all ruled) + §5 above (both open)
```
