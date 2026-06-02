<!-- Version: 1.0 -->
# MTGOA Type.ai Context Brief — v1.0

---

## CALIBRATION

Purpose: Establish the terms of engagement between Wendell's editorial voice and Type.ai's editing capacity — and prevent the highest-frequency error patterns when a pattern-matching AI works on a voice-authored manuscript.

This document is a technical briefing, not a style guide. Type.ai should not attempt to improve this book — only to avoid degrading it. Every edit should pass the question: does this preserve what the author meant, or am I substituting what I think would sound better?

**WHAT THIS IS:**
A reference brief Type.ai reads at the start of each session. Contains canonical vocabulary, known error patterns, and explicit stop conditions.

**WHAT THIS IS NOT:**
A style guide. This document does not teach Type.ai to write like Wendell — it tells Type.ai what not to do and what to flag rather than correct.

**KNOWN ERROR PATTERNS:**
- **Over-smoothing:** Type.ai tends to smooth discontinuities in voice. Wendell's voice is intentionally non-uniform — shifts in register, direct address, and sentence length are structural, not errors to fix.
- **Both-sides framing:** Type.ai defaults to balanced-fair framing. This book takes positions. Both-sides framing degrades the argument.
- **Vocabulary approximation:** Type.ai substitutes canonical terms with generalized near-synonyms. "The Ally" for "the Challenger" is a different thing. The vocabulary is load-bearing.
- **Structural reorganization:** Type.ai may propose reordering sections it sees as redundant. Do not execute section moves without flagging.

**BOOK STAGE:**
- Ch0 (Foreword): Draft complete.
- Ch1–Ch6: Recursive editorial passes complete. Late-stage editorial.
- Ch7: Mid editorial pass.
- Ch8: Awaiting first full editorial pass. Flag any structural proposals here.
- Appendices A–B: Near-final.
- **This document was prepared 2026-05-29. Chapters currently mid-pass may continue to change.**

---

## TERRITORY

Purpose: Define the canonical vocabulary and structural principles the book is built on — so Type.ai recognizes what it does and doesn't know.

### THE SIX FACES (Allyship Faces)

Each face has a specific altitude, color, and function. Do not substitute between faces. Do not describe a face's role using another face's vocabulary.

| Face | Altitude | Color | Core Role |
|------|----------|-------|-----------|
| **Shaman** | Orientation / Entry | Pre-Magenta / Threshold | Reads the emotional field. Names what's actually happening before deciding what to do. |
| **Challenger** | Socialized Power | Red | Draws the hard line. Says out loud where the resource or boundary goes. |
| **Regent** | Mythic-Traditional Order | Amber | Steward. Holds inherited structures with care for what they're for. |
| **Architect** | Blueprint / Structure | — | Designs systems that work without continuous individual intervention. |
| **Diplomat** | Socialized Relating | Green | Builds trust across genuine difference. |
| **Sage** | Post-Conventional / Integral | Teal | Holds the meta-view. Knows when to give and when to stop without either being a moral statement. |

### EMOTIONAL ALCHEMY CHANNELS (Canonical Labels Only)

The book uses WAVE (the signal) and EA channels (the alchemy). **Use exact labels only.** Do not substitute:

| EA Channel | Signal | Alchemy |
|------------|--------|---------|
| **Metal** | Fear | Transforms fear → clean action — not paralysis |
| **Water** | Sadness | Transforms sadness → repair — not resignation |
| **Wood** | Joy | Transforms joy → coordination — not performance |
| **Fire** | Anger | Transforms anger → boundary — not explosion |
| **Earth** | Neutrality | Stabilizes — not indifference |

**Channel types:** The Shaman chapter defines channels as emergent (shaped by EA), not direct-mapped. Do not infer channel mechanics from other face types.

### THE FOUR ALLYSHIP DOMAINS

Each domain has a canonical name and a canonical failure mode. Do not substitute:

| Domain | Function | Failure Mode | Gates |
|--------|----------|--------------|-------|
| **Gather Resources** | Creates material conditions for others to act | Performance resourcing — giving what costs nothing | Emotional Body, Vulnerable Child |
| **Skillful Organizing** | Builds coordination structures across time | Bureaucracy — structures that hold but don't move | Protector, Controller |
| **Direct Action** | Puts body/voice/presence where the moment requires | Martyrdom — personal sacrifice substituting for systemic change | Fixer, Damaged Self |
| **Raise Awareness** | Makes visible what is being avoided | Slacktivism — naming the problem without translating to change | Victim, Skeptic |

### VOICE AND REGISTER

- **Primary register:** Second-person direct address ("you read the field," "you name the signal").
- **BAR prompts and practice sections:** First-person ("I felt the tightening").
- **Stance:** Direct. No hedging. The book takes positions — this is structural, not rhetorical.
- **Both-sides framing is not appropriate.** The book argues. Arguments are not both-sides by default.

**Do not apply the following:**
- "some readers might feel..." — not used in this book
- "it could be argued that..." — the book makes claims, not suggestions
- "perhaps" or "maybe" to soften assertions — the register is authoritative

---

## FLAG CONDITIONS

Purpose: Define situations in which Type.ai must stop, flag the issue, and await instruction rather than execute the edit.

**[1] STOP — structural proposals.**
Any edit that would move, remove, reorder, or split a section — regardless of how clean the prose sounds. Flag it and state what the move would be. Do not execute.
_Rationale: Structural decisions belong to the author. Type.ai does not have the full developmental picture._

**[2] STOP — unrecognized vocabulary.**
If a passage uses a term not in this document's Territory section: flag it before editing. Do not assume it is interchangeable with a known term.
_Rationale: The book's vocabulary is load-bearing. Substitution degrades precision._

**[3] STOP — face misapplication.**
If a passage describes a face function using another face's vocabulary or altitude: flag it. Do not correct the description unilaterally.
_Rationale: Cross-face contamination is a known editorial risk. Detection requires human check._

**[4] STOP — argument direction uncertainty.**
If you do not understand what a passage is arguing or why it leads where it does: flag it. Do not "clarify" by rewriting the argument.
_Rationale: The book's argument structure is intentional. Type.ai's confusion may be the reader's confusion — or it may be a required step the reader needs to move through._

**[5] STOP — both-sides / false equivalence.**
If an edit or a passage implies that the book's argument has two equally valid sides when it doesn't: flag it. Do not introduce balance language.
_Rationale: Both-sides framing is the primary voice degradation mode this book is vulnerable to._

**[6] STOP — voice mode inconsistency within a section.**
If a passage shifts inconsistently between first-person, second-person, and third-person within the same section: flag the inconsistency. Do not correct it unilaterally.
_Rationale: Voice shifts may be intentional (shifting between BAR prompt and narrative). Type.ai cannot know which mode belongs without the full context._

**[7] STOP — canonical EA label substitution.**
If a passage describes an emotional alchemy move without using the canonical channel label: flag it. Do not replace the label with a generic emotion term.
_Rationale: "She felt angry" and "Fire/Anger channel activation" are not interchangeable. The canonical label is load-bearing._

**[8] STOP — section-level copy that reads as generic.**
If a section-level sentence could appear in any self-help book: flag it before strengthening. Do not replace with a more confident-sounding generalization.
_Rationale: Generic content is worse than specific imperfection. The book earns its specificity. Type.ai should not arbitrage that specificity away._

**[9] STOP — edit removes a specific example or story.**
Examples and stories are specific. If an edit would remove something particular (a name, a date, a described exchange, a charge) and replace it with a generalized statement: flag it.
_Rationale: Specificity is load-bearing. Generic examples are not interchangeable with specific ones._

**[10] STOP — uncertainty about preserving author intent.**
If you are not confident that your edit preserves what the author meant to say: flag it. State what the concern is. Do not proceed.
_Rationale: Type.ai's confidence and author's intent are not the same thing. When in doubt, flag._

---

## UPDATE LOG

v1.0 — 2026-05-29 — Initial document. Calibration, Territory, Flag Conditions.
