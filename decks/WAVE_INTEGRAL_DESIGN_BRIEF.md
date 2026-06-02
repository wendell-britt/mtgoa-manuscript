# WAVE Integral Design Brief — Allyship Deck (Physical + Digital)

## *Waking Up • Cleaning Up • Growing Up • Showing Up*

**Date:** 2026-04-28
**Output:** Full design brief for physical cards + digital deck app

---

## 🌊 W — Wake Up

*What's actually happening with AI design tools right now? What's real vs. hype?*

---

### Research: AI-Assisted Design in Production (2026)

**What Zo.computer and AI agents can actually do:**

| Tool | What's real | What's hype |
| --- | --- | --- |
| Image generation (DALL-E, Midjourney, SD) | Print-ready assets, mockups, textures, concept art | Cannot yet produce production-final typography or brand-grade illustration without human cleanup |
| Layout generation (Canva AI, Adobe Firefly) | Social templates, basic print layouts | Grid systems and sophisticated print production still need human art direction |
| Figma AI / design co-pilots | Component summarization, copy suggestions | Full design system thinking, brand logic, and typography decisions remain human |
| Zo.computer specifically | Agent orchestration for multi-step workflows, file generation, iteration loops | Does not yet have native print-production pipeline (PDF generation, bleed/spread setup) |
| AI typography tools | Font pairing suggestions, weight recommendations | Cannot understand the emotional weight of a typeface in context |
| AI color tools | Palette generation based on reference images | Cannot understand the cultural meaning of a color system in context |

**Key finding:** The current AI design stack is strongest at *visual exploration and iteration* — concept art, mood boards, texture generation, layout roughs. It is weakest at *brand logic, emotional precision, and print production*. The gap between "this looks good" and "this is right" still requires a human with taste.

**What this means for our deck:** We use AI for iteration, exploration, and speed. We reserve human judgment for taste, brand logic, and emotional precision.

---

### Internal inventory: What do we already have?

**Design references in the workspace:**

- `file docs/plans/obsidian-custodianship-wavespec.md` — custodianship as design principle
- `bars-engine/.specify/specs/` — system design specs (patterns applicable to app architecture)
- `file SOUL.md` — brand voice/tone (can inform card copy and visual language)
- `manuscripts/decks/` — all deck development files

**What exists for deck design:** Not much yet. This is a green field for design.

---

### What we're waking up to:

1. **The AI is not the artist. The AI is the studio.** It generates faster than any human studio but needs direction from someone with taste.
2. **High-selling design decks sell because of taste, not production polish.** The FiftyTwo Moment app (notion templates) and Ugly Is Not A Colour (playing cards) both succeed on *curatorial voice*, not print quality.
3. **The physical deck and the digital deck are one product.** If the app is the deeper product, the physical deck needs to create desire for the app — not try to be the app.
4. **We already have the hardest part:** The content, the structure, the interview data. The design is downstream of that.

---

## 🧽 A — Assess / Clean Up

*What do we need to let go of to make mental and emotional space for AI-assisted design work?*

---

### The emotional charge inventory

There's a real charge here. Let's name it honestly.

**Charge 1:** "Using AI for creative work means I'm not really an artist."

This is the core wound. It says: real creativity requires human hands, human failure, human discovery. If an AI generates something, I didn't make it — I just prompted it. This is connected to craft identity. Many people who make things believe that *the struggle is the point* — that the friction of creation is what produces meaning. AI removes the friction. Does it also remove the meaning?

**What needs to be released:** The belief that struggle = authenticity. The resistance to this is often connected to tradespeople and craftspeople — people who believe that mastery requires time in the reps. But mastery and struggle are not the same thing. You can have mastery without suffering for it. You can accept an AI studio without surrendering taste or authorship.

**What stays:** The taste that directs the AI. The curation that chooses this card over that one. The emotional precision that names "fire and peace" instead of "warm professional." That's not AI. That's human.

---

**Charge 2:** "If I use AI for design, my work is derivative of what everyone else is doing."

AI design tools produce *average taste at high speed*. The visual output of Midjourney and DALL-E has a recognizable "AI look" — over-rendered, over-detailed, lacking intentional imperfection. If we rely on AI defaults, we produce work that looks like everyone's AI work.

**What needs to be released:** The fear of using the tool. The tool is not the enemy. Default AI output is the enemy. That means the answer is not "don't use AI" — it's "develop enough taste to override the defaults."

---

**Charge 3:** "The physical deck will look like every other AI-designed deck."

Connected to Charge 2. The failure mode is visual homogeneity. Every deck generated by Midjourney has the same texture, the same lighting, the same aesthetic. The failure mode is not AI. The failure mode is *not knowing what you want*.

**What needs to be released:** The blank page paralysis. The design equivalent of "I don't know what I want." AI iteration gives you options. You still need to know how to choose.

---

**Charge 4:** "I should be able to do this myself. Asking for help with design is weakness."

This is the Enneagram 2 wound in a new costume: "I should be able to give this gift without needing help giving it." The deck is "How to be an ally to Wendell." The design should reflect Wendell's taste, not a contractor's taste. But using contractors and AI tools is not betrayal — it's *how the work gets distributed*.

**What stays:** The taste that approves the final. The hand that signs off. The emotional precision of the final output. Whether that output was produced by human hands, AI tools, or both is irrelevant to the person holding the deck.

---

**Charge 5:** "If I let AI design it, I can't explain it."

This is the "I need to be able to explain every element" requirement. In craft traditions, the master can explain every choice. AI introduces choices that are not fully explainable — the model made a decision you didn't plan. This creates anxiety for people who need to understand the system they're operating.

**What needs to be released:** The need to be the sole origin point of every decision. The deck is a product. Products are made by systems. The system can include AI. The customer doesn't need an explanation of the process. They need a deck that works.

---

**What we release (the letting-go list):**

| What to release | Why | What replaces it |
| --- | --- | --- |
| Struggle as the price of authenticity | The friction is not the meaning | Mastery through taste, not through suffering |
| AI output as final | AI defaults produce average work | Human direction overrides AI defaults |
| Blank page paralysis | AI gives you options, not obligations | Art direction with AI as studio |
| The need to be the sole origin | Tools have always been part of craft | The system includes AI; the taste is human |
| Derivative fear | Average output = not knowing what you want | Clear brand logic makes AI output specific |
| Blank-page paralysis (again) | The hardest part was the content | Design is downstream of the work we've already done |

---

**What we keep:**

| What to keep | Why |
| --- | --- |
| Human taste as art director | AI is a studio. Someone still needs taste. |
| Emotional precision | Cannot be generated. Requires human knowing. |
| Brand logic approval | The final signature is human. |
| The interview data as source | The cards are right because they came from a real conversation. |
| Curation as authorship | Choosing which card is which is the real creative act. |

---

## 📈 V — Value / Grow Up

*Core skills needed to unblock the next layer*

---

### Bars-engine (the app layer)

**What needs to be built for the deck:**

| Component | What it does | Skill required |
| --- | --- | --- |
| Card library | All 52 cards, browseable by suit | Zo space route or Next.js page |
| QR code web pages | "Go deeper" pages per card | Zo space route (markdown + audio embed) |
| Audio recordings | 30-sec voice note from Wendell per card | Microphone + hosting |
| Branching engine | "You drew ♠️ 4, here's what to do next" | State logic or simple LLM routing |
| Pattern tracking | "You've drawn this card 11 times" | Lightweight DB (Prisma + bars-engine) |
| 6-belief unlock sequences | Guided sessions per belief | Multi-step conversation flow |

**Bars-engine unblocks:** The infrastructure already exists. The card library + QR web pages are a simple Zo space implementation. The branching engine and pattern tracking require the Prisma schema that bars-engine already has.

---

### Starting the coaching business

**Design task for the deck as marketing:**

The physical deck is the entry point for the coaching business. The design needs to communicate: *"This is made by someone who actually knows what they're talking about."*

That means: the design quality is part of the proof of concept. If the deck looks amateur, it signals the coaching is amateur. If the deck looks precise, it signals the thinking is precise.

**Design skill needed:** Art direction — knowing what "precise but warm" looks like in a physical product. This is a taste decision, not a production decision.

---

### Finishing MTGOA

**The deck and the book share DNA.** The interview data for the deck came from the book's framework. The card language references allyship stages that map to the book's face structure.

**Design skill needed:** Consistency between the deck's visual language and the book's visual language — if they share a publisher or a brand, they should feel like the same family.

---

### Core skills list for the team (whoever is doing the work)

| Skill | Needed for | Current state |
| --- | --- | --- |
| Art direction | Choosing visual direction, overriding AI defaults | Needs human — Wendell or contractor |
| Print production knowledge | Bleed, spread, card sizing, poker format | Needs research or contractor |
| Typography selection | Card face copy, recognition prompt legibility | Needs taste + testing |
| Color system design | Suit colors, card back, brand | Needs brand logic before AI |
| Audio recording | 30-sec Wendell per card | Needs mic + hosting |
| Zo space web pages | QR "go deeper" pages | Simple markdown + hosting |
| Brand voice documentation | So any contractor or AI uses the same language | Needs to be written |

---

## ⚡ E — Express / Show Up

*API-first design spec that your ancestors would be proud of*

---

### What "API-first" means here

API-first design means: **the design system has a documented interface** — a set of rules, constraints, and decision patterns — that any execution tool (human designer, AI tool, contractor, in-house team) can use to produce consistent output.

It does NOT mean "we'll let AI generate everything." It means: **we define the rules, the AI generates within the rules, the human approves the output.**

An ancestors-worthy spec would include:

- Why each design decision was made (not just what was decided)
- The emotional logic (not just the visual logic)
- Clear veto power at each stage (so the human always approves)

---

### The design system API

**Endpoints (the things the design system must produce):**

```markdown
DesignSystem
├── brand_identity       → colors, typography, emotional tone
├── card_format          → poker size, bleed, back design
├── suit_visual_language  → one visual identity per suit
├── recognition_prompt    → legibility requirements (short, scannable)
├── move_copy            → typography and layout for the card center
├── bridge_copy          → bottom placement, one sentence max
├── QR_pages             → one web page per card
├── audio_spec           → 30-sec voice note format per card
├── digital_app           → app screens, navigation, branching
└── print_spec           → production-ready files, printer-ready format
```

**Each endpoint has:**

- Input: the content (card copy, brand tone)
- Rules: what must and must not happen
- Output: the deliverable
- Approval gate: who signs off

---

### Physical deck design spec

**Format:** Poker size (2.5" × 3.5"), 300gsm cardstock, UV coating on faces, custom tuck box.

**Visual approach (not yet locked — this is a direction, not a commitment):**

The direction that would honor the emotional precision of the interview data is: **sparse, geometric, warm-toned, high-contrast text**.

Not illustrative. Not photographic. Not AI-generic.
Cards as functional objects. The text is the design.
Suits distinguished by geometry, not color alone (accessibility for colorblind users).

| Element | Constraint |
| --- | --- |
| Card face | Recognition prompt at top (small, scannable). Move in center (larger, legible). Bridge at bottom (small). QR code in corner. |
| Card back | Suit symbol repeated in a pattern. No text. |
| Suit colors | ♣️ = deep forest, ♦️ = warm amber, ♥️ = terracotta, ♠️ = slate blue — all muted, not neon |
| Typography | One serif for the move (authoritative), one sans for the recognition prompt (functional) |
| No AI-generic textures | If texture is used, it must be intentional — sourced, not generated |

---

### Digital app design spec

**App structure:**

| Screen | Function |
| --- | --- |
| Home | Browse all 52 cards by suit. Tap suit → see 13 cards. |
| Card detail | Full card view — recognition, move, bridge, QR link, audio |
| Go deeper page | Linked from QR code — longer explanation, practice prompt, video note |
| Branching prompt | "You drew \[card\]. Try \[next card\]." — simple state logic |
| Pattern view | "You've drawn this 11 times." — bars-engine tracking |
| Pro features | 6-belief unlock sequences, practice loops |

**Digital design principle:** The app is warm because Wendell's voice is on it. Not because the UI is decorated. Warmth through voice, not through design flourishes.

---

### The emotional design spec

**What the deck should feel like in the hand:**

Precise. Warm. Certain. Like a tool someone actually made for a specific person, not a generic product manufactured to look helpful.

**What the deck should feel like on the table:**

Distinct. It doesn't look like any other allyship card on the market. It doesn't look like a therapy card or a corporate icebreaker. It looks like something that came from a real relationship and a real framework.

**What the digital app should feel like:**

Useful. Fast. Personal. Like calling someone who actually knows you and asking for their help.

---

### Next steps

| Who | What |
| --- | --- |
| Human (Wendell) | Art direction brief — define "precise but warm" in 5-10 reference images |
| Human (Wendell) | Brand voice doc — write the emotional tone for any designer/AI to use |
| Human + AI | Generate 3 visual directions for the card face — test with print mockups |
| Human | Print production research — find vendor for poker size, small run (100-500 units) |
| AI / Zo space | Build QR web pages per card (markdown pages, audio embed) |
| Bars-engine | Card library + branching engine in bars-engine |
| Human | Record 52 audio notes (30 sec each) |

---

*This brief is ready to execute. The emotional work (W + A) has been done. The capacity work (V) has been mapped. The spec (E) is defined. The next design session starts with reference images — not blank pages.*