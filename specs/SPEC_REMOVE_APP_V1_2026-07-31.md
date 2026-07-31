# SPEC — Take the app out of v1, keep the diagnostics, keep the funnel

**Branch:** `claude/edit-remove-app-v1`. One editorial concern, per DL-18.

**Wendell 2026-07-31:** take the app out for v1 and let v2 carry the integration;
the URL `masteringallyship.com` exists now; **the Myths Read and the superpower
quiz can be live by ship, so those stay.**

Diagnosis only so far. Nothing applied.

---

## 1 · The finding that makes this cheap

**The book already contains the analog version of everything being removed**, in
Wendell's voice, as an origin story:

> `ch1:243` — "BARs came out of a fix for this. **Years ago I started carrying
> blank poker cards**… I was carrying a map of the moments that had changed me."

> `ch1:211` — "**Pen and paper hold this fine.** The app holds it better…"

The app was layered on top of a practice that was originally physical. Removing
it returns the book to the thing it says it came from, and the poker-card story
is better than the app paragraph it currently sets up.

## 2 · The inventory — 80 raw mentions, 3 real jobs

| Job | Sites | Kind |
|---|---|---|
| **A** — strip the routing tag | **29** `→ app` | mechanical |
| **B** — two repeated formulas | **12** | two edits, applied six times each |
| **C** — genuine rewrites | **~14** | sentence work |
| **KEEP** — diagnostics, re-pointed to the site | **4** | one-word swaps |

### Job A — the `→ app` tag, 29 sites

The tag decorates a practice prompt that is already complete:

> *"You just made the first move. Before the feeling fades, get down what you
> noticed, where it lived, and what it might be trying to say. Two minutes to
> capture it as a BAR."* **→ app**

Strip the tag. Jordan still knows exactly what to do. Nothing else changes.

### Job B — two formulas, six sites each

**B1 · "The app keeps count."** `ch3:812`, `ch4:579`, `ch5:538`, `ch6:395`,
`ch7:525`, `ch8:551`. This is the book's accountability mechanism — the thing
that catches you feeling deeply and calling it allyship. It needs a paper
replacement rather than deletion, because it is doing real work.

**B2 · "A card that ends in the app is a card you read. A card that ends in a
quest is a card you played."** `ch3:892`, `ch4:740`, `ch5:645`, `ch6:552`,
`ch7:716`, `ch8:698`. The contrast survives without the app — the opposition is
*read* against *played*, and the app is incidental to it.

One edit each, applied six times. **12 of the 80 close on two decisions.**

### Job C — the real rewrites

| Site | What it does |
|---|---|
| `ch1:211` | character sheet storage — already dual-path, *"Pen and paper hold this fine"* |
| `ch1:249` | *"The cards live in the app now, so you are not carrying a paper deck"* — reverses the origin story two paragraphs above it |
| `ch1:257` | *"Put it in the app"* — the first BAR's destination |
| `ch1:269` | the 30-day trial **and** the `[ URL / QR ]` placeholder, together |
| `ch3:843` | **`### The App Layer (the Tell)`** — a section heading |
| `ch3:900` | *"by hand or by letting the app deal it"* |
| `ch9:492` | the gate scan's routing |
| `APPENDIX_B` ×3 | *"Each quest routes to the app for BAR capture"* — design coupling |
| `back_matter/about_the_author.md` | *"builder of bars-engine, the app this book routes to"* |

**`ch3:843` is the one that looks worse than it is.** The section is headed *The
App Layer* but its content is four self-check questions — *"Did you say the true
thing to change the moment, or to be the one brave enough to have said it?"* —
which are entirely paper-compatible. Rename the heading and re-frame the
tracking sentence; the teaching is untouched.

## 3 · What stays — the diagnostics

**Ruled: keep.** These can be live at `masteringallyship.com` by ship, so they
change from *the app* to *the site* rather than coming out.

| Site | What |
|---|---|
| `ch1:83` | the Myths Read — *"a short, unflattering diagnostic that tells you which of these are yours"* |
| `ch1:205` | the Myths Read, named |
| `APPENDIX_A:165`, `:171` | the pre-draw domain diagnostic — *"open the bars-engine app. The pre-draw diagnostic will ask you."* |

**Measured, and it needs a ruling: the superpower quiz is not referenced anywhere
in the book.** Searched ch1 and ch2 for any pairing of *superpower* with a quiz,
a link, or the app: zero. So "keep the superpower quiz" is currently a no-op in
the text. Either it wants a reference written into ch1 or ch2 beside the Myths
Read, or nothing happens and it lives on the site unlinked.

## 4 · The funnel, and why it gets stronger

Today: book → app, thirty free days → …deck. **The app competes with the deck.**
It does the deck's job digitally, free, for a month, at the exact moment the
reader is deciding whether the physical deck is worth buying.

Without it: the reader captures on paper for nine chapters, builds a deck **by
hand**, and the 120-card deck is the obvious upgrade to a practice she is already
running. `masteringallyship.com` is the single door — deck, courses, the Myths
Read, and the book-goodies page whenever there are spoons for it.

Lost: the 30-day trial as an acquisition hook.
Gained: every practice in the book ends in her handwriting, and the product is
the thing that makes that practice better.

## 5 · Rulings needed

1. **B1 — what replaces "the app keeps count"?** It is the book's accountability
   mechanism at six sites and cannot simply be deleted.
2. **The pre-draw domain diagnostic** (`APPENDIX_A:171`) — shipping with the
   Myths Read, or out?
3. **The superpower quiz** — write it a reference, or leave it unlinked?
4. **`about_the_author`** — *"builder of bars-engine, the app this book routes
   to"* is a biography line, not a routing line. Keep as biography, or cut?
5. **Appendix B's quest routing** — quests end in a capture, full stop, or does
   the capture get a named home?

## 6 · Sequencing

`claude/mtgoa-manuscript-changes-swmp78` was 12 commits ahead at 20:26 and still
holds chapter work. Same rule as the last branch: **inventory and drafts here,
no chapter edit until that lands.** Every site above is anchored on quoted text.
