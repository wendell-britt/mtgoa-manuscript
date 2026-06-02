# 6-Face GM Analysis — WAVE Integral Design Brief
## *Does the Design System Actually Produce the Right Deck?*

**Source:** WAVE_INTEGRAL_DESIGN_BRIEF.md, 2026-04-28
**Primary lenses:** Diplomat + Architect
**Secondary lenses:** Challenger + Sage

---

## 🧠 Architect's Diagnosis

**What this spec does well:**
The API-first framing is correct. Breaking the design system into discrete endpoints (brand_identity, card_format, suit_visual_language, etc.) is the right architecture. Each endpoint has input rules, approval gates, and clear ownership. This is how you make sure a contractor or AI can execute without losing the brand logic.

**What the spec misses:**

**The card face is underspecified at the point that matters most.**

The spec says: "Recognition prompt at top, move in center, bridge at bottom." That's layout. But what about:
- What happens when recognition prompt + move + bridge together exceed the card face space?
- How much hierarchy separates the recognition from the move? (Is the move 2x the size of the recognition? 3x?)
- What's the minimum font size for each element at poker size (2.5" × 3.5")?
- Is there a bleed zone that forces text away from the edge?
- Where specifically does the QR code live? (Corner could mean upper-right, lower-right, or could conflict with the bridge text)

**The spec describes the *concept* of the card layout. It does not specify the *layout system*.** These are different things. The concept says "recognition top, move center, bridge bottom." The layout system says "recognition lives in a 0.25" zone at the top of the card, set in 8pt sans, centered, with 0.125" margin from the edge. Move lives in a 0.75" zone in the center, set in 14pt serif, centered, flush-left ragged-right. Bridge lives in a 0.2" zone at the bottom..."

This is the level of specificity that prevents a contractor from building the wrong thing and prevents AI from generating outputs that look like other AI-generated decks.

**The physical card specs need their own spec.** The 300gsm, UV coating, custom tuck box — that's a production spec, not a design spec. These are different documents. The design spec tells someone what to make. The production spec tells a vendor how to print it.

**The suit colors are underspecified.** The spec says "muted, not neon." But "deep forest" for ♣️ is not a color — it's a texture or an adjective. If you hand a print vendor "deep forest" they'll interpret it five different ways. The architect needs: HEX codes or CMYK values. Not adjectives. Not intentions. Numbers.

**Recommendation:** Before generating anything, the Architect needs a Card Layout Spec that specifies:
1. The exact zones on the card face (dimensions + position)
2. Typography hierarchy with type sizes
3. Bleed zone definition
4. QR code placement with conflict resolution
5. Suit color as values, not names

---

## 🎭 Diplomat's Diagnosis

**What this spec does well:**
The emotional design spec section ("What the deck should feel like in the hand") is the most important paragraph in the document. "Precise. Warm. Certain. Like a tool someone actually made for a specific person, not a generic product manufactured to look helpful." That's the brand voice. That's the promise. Everything else in the spec must serve that sentence.

**What the spec misses:**

**The shuffle/divination page is the emotional centerpiece of the digital product.**

The user said "we need a shuffle page" and "the main feature is people will use it as digital divination." But the WAVE brief has this as a bullet in the app structure — "Home: Browse all 52 cards by suit." That's the wrong framing.

A *shuffle page* is not a browsing interface. A shuffle page is an *oracle*. The difference:
- **Browsing:** You go there, you scroll, you choose.
- **Divination:** You surrender, you receive, you trust.

For the target user — Integral Green White Female, working through fawning, psychospiritually abused by current allyship culture — the *shuffle page is the moment the deck shows up for her.* Not as a tool she picks, but as a presence that meets her. The browse page is for when she's exploring. The shuffle page is for when she's in the moment.

The WAVE brief doesn't give the shuffle page its own design spec. It's treating it as one more screen in the app. It needs to be treated as the emotional core of the digital product.

**What the shuffle page needs:**
- The experience of not knowing what you're going to get
- The pause between shuffle and reveal
- The reverence of a card landing
- The message: "someone is here with you in this moment"

**Recommendation:** The Diplomat needs a separate Shuffle Page Spec — not as part of the app structure, but as its own emotional unit. The question it answers is: "What does it feel like to receive a card from this deck?" Not "what buttons are on this screen."

---

## ⚔️ Challenger's Diagnosis

**What this spec does well:**
The "letting go list" is the most honest part. Naming Charge 4 ("I should be able to do this myself") is the blocker that stops most creators from leveraging contractors and AI effectively. The list correctly identifies what stays vs. what goes.

**What the spec misses:**

**The "next steps" table is too long and not owned.**

The table at the end has 7 rows: art direction brief, brand voice doc, 3 visual directions, print production research, QR web pages, bars-engine build, 52 audio recordings. Who owns each? The table says "Human (Wendell)" for the first two and "Human + AI" for one row. But the others have no owner. "AI / Zo space" and "Bars-engine" are not owners — they're systems. Someone has to make the decisions in those systems.

**The challenger says: you cannot spec your way to execution. You need an owner for every row.**

The WAVE brief is a design brief, not a project plan. The next document after this spec should be an execution plan — one owner per row, one deadline, one approval gate. Without that, this becomes another spec that lives in the vault and waits.

**The spec also avoids naming the most important design question:** "Who is the art director?"

The spec says: "Art direction — knowing what 'precise but warm' looks like in a physical product. This is a taste decision, not a production decision." That's true. But it doesn't answer: who makes those taste decisions? Wendell? A contractor? An AI? If Wendell, how much time do they have to be in the approval loop for every card? If a contractor, how do we make sure the contractor understands the emotional precision of the interview data?

This is the veto power question. Every design system needs a clear veto power — the person who can say "this is right" or "this is wrong." Without that, the spec produces outputs nobody can approve.

**Recommendation:** Before the design kit spec, the Challenger needs an execution plan with one owner per deliverable. The spec describes what. The execution plan describes who and when.

---

## 📖 Sage's Diagnosis

**What this spec does well:**
The section on AI limitations is honest: "The current AI design stack is strongest at *visual exploration and iteration*. It is weakest at *brand logic, emotional precision, and print production*." That's a true map of the territory. It correctly positions AI as a studio, not an artist.

**What the spec misses:**

**The historical precedent for "taste as the art director, AI as the studio" is not new.**

The most sophisticated AI design work happening right now is in the game industry — specifically studios that have been doing procedural generation for a decade (No Man's Sky, Spore, algorithmic world-building) and are now adding LLMs on top of procedural systems. These are studios where human designers set the parameters, AI generates within those parameters, and the human approves the output.

The parallel to our deck: we set the emotional parameters (the interview data, the brand voice, the card copy). AI generates within those parameters. Human approves.

But here's what the spec doesn't name: **the most dangerous failure mode in AI design is not generic output. It's confident wrong output.**

When AI generates something that looks good but is wrong, it looks *more* wrong than human-generated wrong output — because the confidence is higher. A human designer who doesn't understand "precise but warm" will produce something tentative. An AI that doesn't understand it will produce something that *looks* like it understands it, at scale. That's the actual risk.

The Sage says: the spec needs to name this explicitly. The quality bar for human approval is not "does this look good?" It's "does this understand what this deck is actually for?"

**Recommendation:** Add a Design QA section to the spec — not just "human approves" but "human approves against these specific criteria." The criteria should be: (1) Does the card feel like it came from a real relationship? (2) Does it feel precise but warm? (3) Does it avoid the AI-generic look? These are taste questions, not technical questions. They require a human who knows what the deck is for.

---

## 🏛 Regent's Diagnosis

**What this spec does well:**
The API-first approach is the most disciplined framing for design systems I've seen applied to a deck project. The endpoints model (brand_identity → card_format → suit_visual_language → etc.) is how you make sure a contractor can execute without losing the brand. This is exactly right for a project that will involve multiple execution tools.

**What the spec misses:**

**The deck is missing a physical prototype before full production.**

The spec says "find vendor for poker size, small run (100-500 units)." That's the right production step. But before that, the Regent should insist on: one card, printed. Not a mockup. Not a screen. A physical poker-size card, in your hand, at the actual size the cards will be.

This is not a design decision. It's a production decision that affects design. Text that's legible on a screen at 100% zoom may be illegible at poker size when printed on 300gsm with UV coating. The recognition prompt that looks good in the spec may be too small to read in actual use. The QR code that looks fine in the corner may be unscanable when printed with a matte finish.

**The Regent says: one physical prototype before any production spec is finalized.**

This is the least expensive investment that prevents the most expensive mistake.

**Recommendation:** Add to the execution plan: "Print one test card before production spec is finalized." This is the Regent's veto — the thing that prevents a design system from producing something that doesn't work in the actual format.

---

## 🌊 Shaman's Diagnosis

**What this spec does well:**
The emotional charge inventory (the five charges) is the Shaman's contribution. Naming "I should be able to do this myself" as a blocker, and "struggle = authenticity" as a false belief, is exactly the inner work this design process needed. Without that inventory, the spec would have been written from the ego, not from clarity.

**What the spec misses:**

**The deck itself is a somatic object.**

A physical card deck is held in hands. It is shuffled. It is placed on a table. It is handed to another person. These are physical, embodied interactions. The design spec addresses what the cards *look like*. It doesn't address what they *feel like*.

The Shaman asks: what is the somatic experience of holding this deck?

Consider: the weight of the cardstock (300gsm is a choice — but 300gsm vs. 330gsm has a different physical feel in the hand). The texture of the UV coating. The corner radius (sharp vs. rounded affects how the cards feel when shuffling). The sound the cards make when shuffled. The way the tuck box feels when opened.

These are not aesthetic choices. They are *somatic design choices.* The deck should feel like it looks: precise, warm, certain.

**The Shaman says: the design system needs a Somatic Spec — not just visual and typographic, but haptic.**

This could be as simple as: "Cards feel substantial when shuffled (330gsm, soft-touch laminate). Corners are slightly rounded (2mm radius). Tuck box has a satisfying open/close click." These are specifications a vendor can follow.

**Recommendation:** Add a Physical Specifications section to the print spec: cardstock weight, laminate type, corner radius, tuck box material, open/close feel. These are spec-able once you know what you're optimizing for. The optimization target: "feels like a tool someone made for a specific person."

---

## Summary: What Survives All Six Faces

| Issue | Face | Action |
|---|---|---|
| Card layout zones underspecified | 🧠 Architect | Card Layout Spec with dimensions |
| Suit colors as adjectives not values | 🧠 Architect | HEX/CMYK values before vendor contact |
| Shuffle page underspecified as emotional center | 🎭 Diplomat | Separate Shuffle Page Spec |
| Execution plan has no owners | ⚔️ Challenger | Add execution plan with one owner per row |
| No explicit QA criteria for design approval | 📖 Sage | Design QA section — taste questions, not technical |
| No physical prototype before production spec | 🏛 Regent | One test card before print spec finalized |
| No somatic spec for physical cards | 🌊 Shaman | Physical Specifications section |

**The spec that ancestors would be proud of needs:**
1. **Card Layout Spec** — zones, typography sizes, bleed
2. **Shuffle Page Spec** — emotional center of the digital product
3. **Design QA section** — taste criteria for human approval
4. **Execution plan** — owners, deadlines, veto power
5. **Physical Specifications** — cardstock, laminate, corner radius
6. **One test card printed** — before production spec is finalized

---

## The Design Kit Spec

Based on this analysis, the design kit should contain:

```
ALLYSHIP_DECK_DESIGN_KIT/
├── BRAND_IDENTITY/
│   ├── emotional_tone.md          ← "precise but warm" documented
│   ├── suit_colors.md             ← HEX values, not adjectives
│   └── typography_system.md       ← fonts, sizes, hierarchy
├── PHYSICAL_CARD/
│   ├── card_layout_spec.md         ← zones, dimensions, bleed
│   ├── physical_specifications.md  ← cardstock, laminate, corners
│   └── print_production_checklist.md
├── DIGITAL_APP/
│   ├── app_structure.md            ← screens, navigation
│   ├── shuffle_page_spec.md        ← emotional center spec
│   └── QR_page_template.md         ← "go deeper" page template
├── APPROVAL/
│   ├── design_qa_criteria.md       ← taste questions for approval
│   └── veto_power_diagram.md       ← who approves what
├── EXECUTION/
│   ├── owner_matrix.md             ← one owner per deliverable
│   └── prototype_spec.md           ← one test card before production
└── REFERENCE/
    └── design_direction_refs.md    ← 5-10 reference images for art direction
```

**Next: Create the Design Kit Spec as a document.**