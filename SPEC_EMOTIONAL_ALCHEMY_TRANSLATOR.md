# SPEC: Emotional Alchemy Translator
## A Writer's Reference Tool for MTGOA + Igniting Joy

**Purpose:** Resolve any "what EA label fits this feeling?" question by lookup — not inference.
**Audience:** Author, editor, or AI drafting session. Used when a feeling-word needs to be checked against canonical EA labels.
**Status:** BACKLOG — spec ready, implementation deferred

---

## The Problem This Solves

When drafting, a writer might ask: "What do you call the feeling underneath showing up and knowing what you're doing?"

Possible answers:
- "Competence" — sounds corporate, isn't canonical
- "Satisfaction of mastery" — closer, still not precise
- "Wood/Joy: Vitality alignment" — canonical but opaque to ICA reader
- "The satisfaction of competent practice" — readable but still vague

The EA Translator exists to close the gap between "the feeling the body recognizes" and "the canonical label that anchors it to the system."

**Rule:** Never invent a new EA label. Always map to the 5 canonical channels + transcend names.

---

## The 5 Canonical Channels + Signal/Satisfaction Pairs

| Channel | Metal | Water | Wood | Fire | Earth |
|---------|-------|-------|------|------|-------|
| **Signal (Dissatisfaction)** | Fear | Sadness | Joy (suppressed/flattened) | Anger | Neutrality (confused/stuck) |
| **Transcend Move** | Fear → Excitement | Sadness → Poignancy | Joy → Vitality-Alive | Anger → Triumph | Neutrality → Grounded-Stillness |
| **Satisfaction Name** | "The thrill of what matters enough to risk" | "The grief that proves what you loved was real" | "The surge of what aligned — energy moving in the right direction" | "The heat of what you defended and held" | "The clarity that comes from seeing clearly" |

**Signal (Dissatisfaction) naming rules:**
1. Name the body-experience — what does the dissatisfaction feel like in the body?
2. The Signal is the raw feeling before transcendence — not a judgment, not a story
3. Suppressed/flattened Joy (Wood dissatisfaction) is distinct from suppressed Anger (Fire dissatisfaction)

**Satisfaction naming rules:**
1. Name the body-experience after the transcendence move — what does completion feel like?
2. Use one phrase per channel — no compound descriptions
3. Keep all 5 in working memory so you can reference any without inferring

---

## Compound Emotional Concept Words — Research & Development Backlog

**Status:** BACKLOG — research needed

### The Gap

Most real-world feeling-words are compound states — not a single channel, but two channels interacting. Examples:
- **Disappointment** = Anger (boundary crossed) + Sadness (loss) → both dissatisfied
- **Dread** = Fear (risk detected) + Sadness (anticipatory loss)
- **Shame** = Fear (exposure) + Sadness (collapse of self-image)
- **Guilt** = Sadness (I did wrong) + Fear (consequences coming)
- **Jealousy** = Fear (losing what I have) + Anger (someone else has it)
- **Envy** = Sadness (I don't have it) + Anger (it's not fair)
- **Contempt** = Anger (you're beneath me) + Sadness (I don't respect you)
- **Anxiety** = Fear (something's coming) + Sadness (I can't stop it) + Earth confusion (I don't know what to do)
- **Resentment** = Anger (I was wronged) + Sadness (nobody acknowledged it)
- **Grief** = Sadness (profound loss) + Fear (it won't stop) + Anger (why did this happen)

These compound states are how people actually experience feelings — they are not single-channel. The canonical 5 channels are analytical tools; the compound words are phenomenological reality.

### What Research Is Needed

1. **Map 20-50 common compound feeling-words** to their channel components
2. **Identify which compounds are most relevant** to allyship, leadership, and personal development contexts
3. **Determine when compound words belong in MTGOA** (they may be more ICA-reader-recognizable than single-channel labels)
4. **Decide whether compound words need their own Transcend moves** or whether the resolution always reduces to one or more of the 5 canonical Transcend moves
5. **Distinguish functional compounds from collapse-pattern compounds:**
   - Functional: two genuine channels both active — the person is navigating a real multi-channel moment
   - Collapse-pattern: one channel dominates but gets labeled with a compound name to avoid the simplicity of the truth

### The Research Question

**"When a reader recognizes a compound word like 'disappointment,' does naming the component channels help them navigate the feeling better — or does it create unnecessary complexity?"**

This is an empirical question about reader psychology. It may require testing with real readers.

### Companion Research: Igniting Joy's Comedic Archetypes

The three comedic archetypes (Clown, Jerk, Cult Leader) in Igniting Joy may already be a compound-emotion handling system:
- The Clown handles shame (Fear + Sadness) through self-deprecation
- The Jerk handles anger (boundary violation) through performative aggression
- The Cult Leader handles systemic dread (Fear + Sadness + Earth confusion) through satirical certainty

**If this holds, the comedic archetypes are a compound-emotion navigation tool** — which means they belong in the EA Translator as a practical application, not just a comedy device.

### Backlog Item

Create `SPEC_EMOTIONAL_ALCHEMY_COMPOUND_RESEARCH.md` before writing any compound feeling-word language into MTGOA. This is a prerequisite, not an add-on.

---

## Lookup Protocol

When a drafting question arises ("what word fits here?"):

1. **Name the feeling in plain prose** — "the feeling of reading a room and knowing what to do"
2. **Map to the nearest canonical channel** — that feels like Wood (alignment, vitality)
3. **Use the satisfaction name** — "the surge of what aligned"
4. **Check against ICA reader test** — does it land in the body, or does it sound abstract?

If the feeling is a compound state (common word like "disappointment" or "dread"):
1. **Note it as a compound** — flag it for compound research backlog
2. **Map to component channels** — don't force a single channel if two are clearly active
3. **Use the compound word in prose** — readers recognize these; don't sanitize them

If the satisfaction name is too opaque for ICA readers (pre-Ch1 exposure), use the plain-prose description as the in-book phrase, with the EA label as the editorial note in the spec.

**Example (single channel):**
- Draft question: "What do you call the feeling underneath showing up and knowing what you're doing?"
- Channel: Wood (alignment, vitality)
- Satisfaction name: "the surge of what aligned"
- ICA in-book phrasing: "the warmth that comes from being in the right game, playing it well"
- EA spec note: "Wood/Joy vitality satisfaction"

**Example (compound — flagged):**
- Draft question: "She felt a pang of disappointment when no one acknowledged her contribution"
- Channels: Anger (boundary — my contribution deserves acknowledgment) + Sadness (loss — acknowledgment didn't come)
- Compound word: "disappointment" — recognized by ICA reader, contains two dissatisfied channels
- In-book phrasing: use "disappointment" as-is; flag for compound research to confirm channel mapping
- EA spec note: "COMPOUND: Anger + Sadness dissatisfied — confirm Transcend resolution path"

---

## Usage in Editorial Pass

For each chapter's emotional alchemy section, before writing the satisfaction language:

1. Run the lookup: what channel + what satisfaction name?
2. Write the ICA phrasing
3. Flag compound states with `[COMPOUND: channels]` in the spec
4. Flag the EA channel in the spec for later verification (Shaman chapter must confirm 5 channels have worked examples)

---

## Companion Documents

| Document | Purpose |
|----------|---------|
| `SPEC_EMOTIONAL_ALCHEMY_TRANSLATOR.md` | This spec |
| `SPEC_EMOTIONAL_ALCHEMY_COMPOUND_RESEARCH.md` | **[BACKLOG]** Compound word research — do before using compound words in prose |
| `bars-engine/.agent/context/emotional-alchemy-ontology.md` | Full EA system (canonical source) |
| `manuscripts/chapters/ch2-SHAMAN/SPEC.md` | Shaman chapter — where EA is first taught to reader |

---

**Spec status:** APPROVED — 2026-04-22
**Created:** 2026-04-22
**Updated:** 2026-04-22 — added dissatisfaction states + compound words backlog
**Owner:** Wendell Britt
