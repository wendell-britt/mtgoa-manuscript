# 6-Face Improvement Pass: MTGOA 52-Card Prompts

**Date:** 2026-04-20
**Status:** Analysis complete. Ready for selective revisions.

---

## 🧠 ARCHITECT — Structural Integrity

### Assessment
The 52-card structure is sound:
- ✅ 4 domains × 13 cards = complete
- ✅ Recognition → Deepening → Commitment progression clear
- ✅ Seasonal distribution balanced (13 per season)
- ✅ Gate distribution mapped (with Loyalty/Powerlessness to rebalance)
- ✅ Guide lens assigned per domain (clean, simple)

### Gaps Found
1. **Prompt Parallels Across Domains:** Some themes repeat too similarly across domains
   - DA-1 "Hesitation" & SO-1 "Circle" both start with recognition but feel disconnected
   - RA-1 "Naming" addresses the same recognition space differently
   - Opportunity: Make each domain's Recognition phase more distinctly aligned to domain metaphor

2. **Deepening Logic:** Cards 5-9 don't always clearly deepen from Recognition
   - GR-5 "Inherited" (family resources) is a good deepening from GR-1 "Inventory" (what you have)
   - But SO-5 "Influence" doesn't obviously deepen SO-1-4 (who's in circle)
   - Opportunity: Strengthen the thematic throughline from Recognition → Deepening

3. **Commitment as Action:** Cards 10-13 should show commitment *to action*, not just reflection
   - GR-11 "Claim" is strong (actively claiming resources)
   - But GR-12 "Generosity" is more reflective than committed
   - Opportunity: Shift Commitment cards more toward *what you're committing to do*

### Recommendations (Priority: Medium)
- [ ] Review Deepening cards (5-9) to ensure they deepen Recognition (1-4) thematically, not just shift topic
- [ ] Strengthen Commitment cards (10-13) to emphasize action/pledge over reflection
- [ ] Cross-domain check: Do Recognition phases in each domain feel distinctly different from each other?

---

## 🏛 REGENT — Elegant Preservation

### Assessment
The TASKS document is well-structured for preservation:
- ✅ Clear metadata per prompt (Season, Gates, Intensity)
- ✅ Consistent format (easy to version, audit, track changes)
- ✅ Design notes explain the cyclical deepening principle
- ✅ Gate distribution audit included

### Gaps Found
1. **Version Entry Points:** Prompts don't show where Year 1/Year 2/Year 3 variations will split
   - Example: DA-3 "What are you avoiding confronting?" is fine for Year 1, but Year 2 & 3 versions aren't drafted
   - Not a problem (those come in JSON), but Regent wants to see the split points named
   - Opportunity: Mark which prompts will need Year 2 shadow variants, which will deepen to Year 3 gift

2. **Stability Assumptions:** The TASKS doesn't specify which prompts are "core" vs "flexible"
   - Some prompts feel immovable (GR-1 "Inventory", DA-3 "Barrier")
   - Others feel like they could be refined (GR-12 "Generosity", RA-8 "Paradox")
   - Opportunity: Mark stability level (stable/experimental/flexible) per prompt

3. **Audit Trail Gaps:** No note of who authored each prompt (all Claude, implicitly)
   - Future phases may have other authors contributing
   - Opportunity: Add author attribution field to JSON schema (default "claude_v1")

### Recommendations (Priority: Low)
- [ ] Mark which prompts are Year 1-only vs support Year 2/Year 3 variations
- [ ] Tag stability level per prompt (will guide verification rigor)
- [ ] Plan author/version field for JSON schema (prep for collaboration)

---

## ⚔️ CHALLENGER — Critical Edge

### Assessment
The prompts are solid but there are some quality gaps:

**Strong Prompts (these work):**
- DA-3 "What are you avoiding confronting?" — Clear, activates gates, actionable, deepenable
- RA-3 "What truth have you been avoiding saying?" — Sharp, specific, gate-aligned
- GR-11 "What are you claiming as yours?" — Action-oriented, strong emotional pull
- SO-3 "Where is your group fractured?" — Group-specific, activates anger/betrayal gates

**Weak Prompts (need sharpening):**
- GR-2 "What strength in you have you not named?" — Too introspective for allyship, feels therapeutic not activist
- GR-12 "What are you offering without expectation?" — Vague, "without expectation" is passive
- SO-5 "Who influences you without knowing it?" — Weak, doesn't activate anything
- RA-8 "What's true about the people you're critiquing?" — Paradox is good, but phrasing feels softer than the gate demand

### Specific Fixes

| Prompt | Issue | Suggested Reframe |
|--------|-------|------------------|
| GR-2 | Too therapeutic | "What strength do you have that your community needs?" (connects strength to allyship work) |
| GR-12 | Passive/reflective | "What are you willing to give to this movement?" (action + commitment) |
| SO-5 | Weak activation | "Who has power over your organizing and you haven't named?" (clearer power analysis) |
| RA-8 | Softer than gates need | "What do you refuse to hate about the people you're opposing?" (explicit shadow work) |
| DA-2 | "Privilege" too abstract | "Where are you comfortable because of injustice?" (concrete, activates shame) |
| RA-4 | "Silence" past-tense | "Who is hurt right now by what you're not saying?" (present tense, urgent) |

### Recommendations (Priority: High)
- [ ] Sharpen weak prompts using suggested reframes
- [ ] Ensure all prompts feel *activist*, not just introspective
- [ ] Test: Can you imagine someone drawing this card and immediately knowing what to reflect on?

---

## 🎭 DIPLOMAT — Bridge & Relationship

### Assessment
The Player Interface looks good, but GM bridge points could be clearer:

**Strengths:**
- Each prompt has clear player-facing primary question
- Guide lens assigned (Sage/Diplomat/Challenger/Shaman) gives GM anchors
- Worldbuilding hooks implied (Geography/Social/History/Magic) in design notes

**Gaps:**
1. **GM Context Not Visible in TASKS:** GMs need to know at a glance how to contextualize each prompt
   - The TASKS shows gates but not the 4 worldbuilding hooks per prompt
   - Opportunity: Add minimal hook labels in TASKS (e.g., "GR-1: Geography focus - what resources does your land/body have?")

2. **Player Accessibility:** Some prompts assume previous-year context
   - DA-8 "Who do you need to see you act?" assumes player knows their hesitation (from DA-1, DA-5)
   - RA-9 "Who gave you permission?" assumes player has struggled with authority (from RA-2, RA-3)
   - Opportunity: Ensure each prompt is standalone but also deepens if replayed

3. **Group Facilitation Gap:** Commitment cards (10-13) don't show how to facilitate in groups vs solo
   - SO-12 "What do you pledge to your people?" is group-facing
   - GR-13 "What resource will you tend?" could be solo or group
   - Opportunity: Note which cards work best for group facilitation (will inform GM toolkit)

### Recommendations (Priority: Medium)
- [ ] Add single-line worldbuilding hook per prompt (for GM scanning)
- [ ] Ensure each prompt works solo *and* deepens on replay (especially Deepening/Commitment)
- [ ] Mark which Commitment cards are group-facilitation-ready

---

## 🌊 SHAMAN — Shadow & Metaphysics

### Assessment
The prompts do name shadow gates (Victim, Shame, Fear), but the shadow work isn't always explicit enough:

**Shadow Work Present:**
- RA-7 "What shadow truth are you dancing around?" — Explicitly names the shadow
- DA-7 "What are you afraid of being seen doing?" — Implies secret shame
- GR-7 "What are you holding that isn't yours to keep?" — Shadow hoarding

**Shadow Work Implicit (needs naming):**
- GR-1 "What resources do you already have?" — Assumes you see yourself as having *something* (Victim gate: "I have nothing")
- SO-1 "Who's in your circle of trust?" — Isolation gate lurking but not named
- DA-1 "What move are you thinking about but haven't made?" — Hesitation without naming the paralysis

### Specific Improvements

**Add shadow invitation to weak Recognition cards:**

| Prompt | Current | Shadow Invitation |
|--------|---------|-------------------|
| GR-1 | "What resources do you already have?" | Add: "(What do you claim? What have you dismissed?)" |
| SO-1 | "Who's in your circle of trust?" | Add: "(Who's missing? Who's been excluded?)" |
| DA-1 | "What move are you thinking about but haven't made?" | Add: "(What scares you about it?)" |
| RA-1 | "What have you been calling by the wrong name?" | ✅ Already invites shadow |

### Year 2/Year 3 Shadow Arcs

These deepening patterns should be explicitly drafted:

**Example: DA-3 "What are you avoiding confronting?"**
- Year 1: External barrier ("I can't confront my boss because...")
- Year 2: Internal barrier ("The part of me that won't confront is..." → "What's it protecting?")
- Year 3: Integrated resource ("What has my avoidance taught me about when to act and when to wait?")

**Recommendation:** Create a Shadow Deepening Matrix for all 52 prompts showing Year 1→Year 2→Year 3 arc.

### Recommendations (Priority: High)
- [ ] Add shadow invitation parentheticals to weak Recognition cards (especially GR-1, SO-1, DA-1)
- [ ] Draft Year 1→Year 2→Year 3 shadow arcs for all 52 prompts
- [ ] Ensure Deepening phase (5-9) invites the shadow explicitly ("What part of you...?")

---

## 📖 SAGE — Timeless Principle & Long View

### Assessment
The prompts support long-term practice, but deepening pathway isn't explicit enough:

**Deepening Support:**
- Same 52 cards across Year 1, 2, 3 ✅
- Emotional intensity curve supports pacing ✅
- Recognition → Deepening → Commitment progresses player maturity ✅

**Deepening Gaps:**
1. **Cross-Domain Learning:** Players might not see connections between domains across years
   - GR-5 "Inherited" (resources from family) connects to SO-8 "Repair" (tending broken community)
   - But the connection isn't explicit
   - Opportunity: Show inter-domain deepening patterns (e.g., Year 1 GR → Year 2 SO → Year 3 DA progression)

2. **Cyclical Return:** Prompts should feel like returning to an old friend, not revisiting old ground
   - GR-1 "What resources do you have?" Year 1 vs Year 3 should feel like "Oh, I see what I couldn't see before"
   - Not every prompt shows that arc clearly
   - Opportunity: Test each prompt for deepenability (can it be answered differently each year?)

3. **Integration Wisdom:** Cards 10-13 (Commitment) should point toward integration, not closure
   - GR-13 "What resource will you tend in the next season?" ✅ Good (points forward)
   - But DA-12 "How will you keep moving when it gets hard?" feels like the *answer*, not an invitation to deeper practice
   - Opportunity: Commitment cards should invite mastery, not completion

### Deepenability Test

Run this test on each prompt: *"Can someone answer this question differently in Year 1, Year 2, and Year 3?"*

**High deepenability (good):**
- DA-3 "What are you avoiding confronting?" → Year 1: external barrier, Year 2: internal pattern, Year 3: systemic role
- RA-3 "What truth have you been avoiding saying?" → Year 1: speaking up, Year 2: why I stayed silent, Year 3: what my silence was protecting

**Low deepenability (needs work):**
- GR-2 "What strength in you have you not named?" → Hard to answer differently across years (yes/no answer)
- SO-6 "When did you disappoint someone?" → Past-tense, limits deepening (what if they answer differently each year? Unclear)

### Recommendations (Priority: High)
- [ ] Test all 52 prompts for deepenability (3+ legitimate answers across years)
- [ ] Mark which prompts need reframing for better Year 2/Year 3 pathways
- [ ] Draft deepening arcs for all prompts (Year 1→Year 2→Year 3)
- [ ] Ensure Commitment cards point forward (toward mastery) not backward (toward completion)

---

## Summary: 6-Face Improvement Scorecard

| Face | Assessment | Priority | Action Items |
|------|------------|----------|--------------|
| **Architect** | Sound structure, thematic gaps | Medium | Strengthen Deepening throughline, sharpen Commitment as action |
| **Regent** | Well-preserved, versioning prep needed | Low | Mark Year 1/2/3 split points, tag stability levels |
| **Challenger** | Solid overall, 6 prompts need sharpening | High | Reframe weak prompts (GR-2, GR-12, SO-5, RA-8, DA-2, RA-4) |
| **Diplomat** | Good player interface, GM bridge unclear | Medium | Add worldbuilding hooks, mark group-facilitation-ready cards |
| **Shaman** | Shadow present, not always explicit | High | Add shadow invitations to weak Recognition, draft Year 2 shadow arcs |
| **Sage** | Supports long-term practice, deepening untested | High | Test deepenability on all 52, draft deepening arcs |

---

## Prioritized Revision Plan

### Phase 1: High-Priority Fixes (Do before JSON)
1. **Challenger's 6 weak prompts:** Reframe GR-2, GR-12, SO-5, RA-8, DA-2, RA-4
2. **Sage's deepenability test:** Verify all 52 can be answered 3+ ways, revise as needed
3. **Shaman's shadow arcs:** Draft Year 1→Year 2→Year 3 for all 52 prompts

### Phase 2: Medium-Priority Polish (During JSON conversion)
1. **Architect's throughline:** Ensure Recognition→Deepening→Commitment are thematically connected per domain
2. **Diplomat's worldbuilding hooks:** Add 1-line hook per prompt (Geography/Social/History/Magic focus)
3. **Regent's versioning prep:** Mark Year 1-only vs Year 1+2+3 prompts, tag stability

### Phase 3: Low-Priority Documentation (Post-JSON, Pre-Verification)
1. **Regent's author attribution:** Add author field to schema
2. **Diplomat's group facilitation:** Note which Commitment cards work best in group settings

---

## Immediate Next Steps

1. **Revise weak prompts** (6 Challenger fixes)
2. **Draft deepening arcs** (52 Sage arcs)
3. **Test deepenability** (verify 3+ answers per prompt)
4. **Convert to JSON** (with updated prompts)
5. **Verification run** (automated + manual checks)

**Estimated effort:** 1-2 rounds of revision, then ready for JSON schema conversion.

---

**Status:** 6-Face analysis complete. Recommended revisions are concrete and actionable.
**Next action:** Should we do Phase 1 revisions before JSON conversion, or proceed to JSON and revise in parallel?
