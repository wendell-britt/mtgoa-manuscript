# Design Kit Spec — Allyship Deck
## *The Document That Documents the Taste*

**Type:** Implementation spec
**Purpose:** Create a reusable design kit that allows consistent deck execution at scale — physical and digital — with taste transfer to contractors and AI tools.
**Status:** Pre-draft
**Owner:** Wendell
**Audience:** Contractors, AI tools, future self

---

## What Is the Design Kit?

The design kit is the document that answers: **why does the deck look and feel the way it does?**

Not just "what are the visual choices" but "what is the emotional logic that produced those choices." A contractor who reads the kit should be able to make decisions without Wendell in the room for every approval. An AI tool that reads the kit should be able to generate outputs that fall within the taste envelope. Future Wendell should be able to hand this to a print vendor and get a result that matches what he would have made himself.

The kit is the taste made transferable. The deck is one output of the kit.

---

## Why This Document Exists

**The problem:** 52 cards, 19 pages of QR content, digital app, audio notes, bars-engine wiring — all need to feel like they came from the same person. That person cannot be in every room for every decision.

**The failure mode we are preventing:** "I know it when I see it" approval. The version of this project where Wendell has to approve every card individually, every layout decision individually, every audio note individually — because without his eye on it, the output feels generic.

**The solution:** Document the taste at the system level. Define the rules that produce consistent output. The human is the veto. The system is the art director.

---

## Design Kit Contents

### 1. Brand Voice Document

**What it contains:**
- How the deck speaks (voice, tone, word choices)
- What words are forbidden and why
- Why the move is always one sentence (not two)
- Why the recognition prompt is always a felt question (not a label)
- Why the allyship bridge is always a small observation (not a lecture)
- The emotional signature: fire + peace (and why that matters for every word choice)
- How Wendell talks about allyship in person — transcribed from interview

**Why it matters:** The brand voice doc is not a style guide. It's a taste transfer document. It explains *why* — not just what. A contractor who understands why the deck uses short sentences will make better decisions in edge cases than one who just knows "use short sentences."

**The spec test:** Give the brand voice doc to someone who has never met Wendell. Have them write 5 cards without talking to him. Compare those cards to the V3 cards. The closer they are, the better the doc.

---

### 2. Visual System Spec

**What it contains:**
- Suit symbols: geometry, sizing, color palette (specific hex codes)
- Card anatomy: recognition prompt / move / bridge — spatial rules for each zone
- Typography: fonts, sizes, weights (spec'd as rules, not inspiration)
- Color by suit: exact values for each suit's palette
- Card back design: what it communicates when face-down
- Box / packaging: what the physical product communicates
- Tactile spec: paper weight, finish, any special tactile feature

**The spatial rules:** The recognition prompt occupies this much space. The move has this proportion of the card. The bridge is placed here and has this size range. These are not aesthetic preferences — they are functional rules that produce the card's readability.

**The spec test:** Give the visual spec to a contractor. Have them design one card without reference images. Compare it to V3 cards. If it looks like it belongs, the spec worked. If it looks slightly off, the spec needs more rules.

**The print vendor problem:** Poker size cards require precise specifications. The vendor needs exact dimensions (3.5" × 2.5"), bleed area, color space (CMYK vs RGB), and any special finishes. This section should be written as a vendor brief.

---

### 3. QR Page Spec

**What each QR page contains:**
- The full card content (recognition prompt, move, bridge)
- Audio note from Wendell (30-60 seconds)
- A "go deeper" prompt — one question that extends the card's teaching
- A practice scenario — a moment where this card would show up
- A reflection prompt — what the ally noticed about themselves after doing the move

**Why audio matters:** The card with Wendell's voice is different from the card without it. The warmth is in the voice. The QR page is the only place the physical deck can include that voice.

**The spec test:** Read the QR page without hearing the audio. Read it with the audio. The audio should change how the text reads. If it doesn't, the audio isn't adding enough.

---

### 4. Digital App Spec

**What it contains:**
- Shuffle page: the moment of divination — how it looks and feels
- Card reveal: the animation, timing, and emotional arc of drawing a card
- Branching flow: "what happened after you drew this card?"
- Pattern tracking: which cards have you drawn most? What does that mean?
- 6-belief unlock sequences: the sub-routines for each self-sabotaging belief
- Practice mode: "practice with me" — listen, respond, compare

**Why digital comes after physical:** The physical deck creates the desire for the digital. The digital delivers what the physical promises. This means: the physical cards must be the primary design target. The digital app is an extension of the physical, not the other way around.

**The bars-engine wire:** The app logs which cards are drawn and when. This produces data about the ally's development arc. The pattern tracking is not diagnostic — it's a practice mirror. "You've drawn the capacity-check card 11 times this month. Here's what that might be telling you."

---

### 5. Photography / Art Direction Brief

**What it contains:**
- The photography style: warm, specific, not stock
- How to find or direct photography that matches the deck's energy
- What the photography should NOT look like (the "AI look" and why to avoid it)
- Image treatment: filters, aspect ratios, any consistent visual processing
- Illustration vs. photography: when to use which

**The art direction problem:** Stock photography reads as "allyship training deck." We want "made by someone with specific taste." This section defines what "specific taste" looks like in photographic terms.

**The spec test:** Give the art direction brief to a photographer or stock site searcher. Have them select 5 images. Compare to what the deck currently uses. If they're different, the brief needs more specificity.

---

### 6. Icon / Symbol Library

**What it contains:**
- The 4 suit symbols: origin, meaning, geometric construction
- Any additional icons used in the design (direction arrows, checkmarks, etc.)
- Face card indicators: how J/Q/K are visually distinguished
- Domain taxonomy markers: RAISE_AWARENESS / GATHERING_RESOURCES / ORGANIZING / DIRECT_ACTION — if these appear visually, how?
- The "allyship moment" icon: the visual motif that signals "this is the moment the card is for"

**Why this section:** Symbols are the fastest way to communicate suit. The suit symbol must be readable at poker size, recognizable from memory, and specific enough to be distinct. This section constructs each symbol from first principles.

---

### 7. Vendor / Production Briefs

**What it contains:**
- Print vendor brief: poker size specs, paper, finish, quantity tiers, vendor shortlist
- Digital app vendor brief: if contracting development, what's the brief?
- Audio recording guide: what equipment, what environment, what Wendell should say

**Why separate:** These are practical briefs for working with external vendors. They should be standalone documents — written so someone else can execute without Wendell in the room for every decision.

---

## The Spec Test

**For each section, the test is the same:**

> Can a contractor or AI tool make consistent decisions without Wendell in the room for every approval?

The answer should be "yes" for each section. If the section requires Wendell to be present, it's not spec'd enough yet.

---

## The Audit Trail

Every design decision in the kit needs an answer to: **why this and not something else?**

The "why" is the taste. It's what makes the output consistent across 52 cards, 19 QR pages, a digital app, and bars-engine wiring.

---

## Spec Status

**Not started.** This document is the spec to create the design kit. The kit is the prerequisite for:
- Physical deck production
- Digital app development
- QR page content generation
- Contractor onboarding

**Next step:** Create the design kit sections one by one, starting with Brand Voice (the highest leverage document). The Brand Voice doc is the one that makes every other section easier.