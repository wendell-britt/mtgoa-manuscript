# Friendcraft v1 Ontology Spec

Status: Draft v1
Date: 2026-04-18
Scope: Preproduction proof-of-concept on BARs engine

## 1) Purpose and Design Constraints

Friendcraft extends the Mastering Allyship move set into friendship operations.

Primary goal:
- Move the player from reactive relationship management to proactive, context-aware friendship practice.

Constraint alignment:
- Core moves stay invariant: Wake Up, Clean Up, Grow Up, Show Up.
- BAR turn loop remains the action engine.
- Spaced repetition is mandatory as scheduling infrastructure ("Anki for friendships").
- Friendship is modeled as an infinite campaign, not a finite objective.

## 2) Canonical Ontology

### 2.1 Core entities

1. Player
- Definition: The practicing self who takes moves.
- Key fields: `player_id`, `capacity_profile`, `channel_preferences`, `daily_action_cap`.

2. Bond
- Definition: A friendship relationship between Player and one person.
- Key fields: `bond_id`, `person_name`, `tier`, `bond_health`, `last_touch_at`, `next_due_at`, `channel_affinity`, `consent_flags`.

3. Third Body (Fred)
- Definition: The emergent relational field of a Bond (the "we").
- Key fields: `fred_state`, `fred_signal_strength`, `fred_archetype`, `rituals_present`.
- Notes: Fred is not a character collectible in v1; it is a relational state lens.

4. Daemon
- Definition: Repeat blocker pattern reducing follow-through, repair, or trust.
- Key fields: `daemon_type`, `severity`, `trigger_signature`, `counter_moves`, `streak`.

5. Move
- Definition: One actionable step mapped to Wake Up, Clean Up, Grow Up, or Show Up.
- Key fields: `move_id`, `move_family`, `prompt_text`, `estimated_friction`, `channel`, `expected_duration_min`.

6. BAR Turn
- Definition: One full decision-and-action cycle.
- Key fields: `signal`, `meaning`, `action`, `consequence`, `face_lens`, `completed_at`.

7. Campaign
- Definition: Long-running friendship progression at player level.
- Key fields: `campaign_id`, `phase`, `cadence_score`, `network_health_score`, `allyship_readiness_score`.

### 2.2 Supporting entities

8. Prompt Card
- Definition: Reusable action pattern from deck technology.
- Key fields: `card_id`, `suit`, `tags`, `base_interval_days`, `cooldown_rules`.

9. Thread
- Definition: Open relational arc requiring closure (e.g., follow-up, repair, invite).
- Key fields: `thread_id`, `bond_id`, `thread_type`, `opened_at`, `due_at`, `status`.

10. Review Event
- Definition: Outcome log after an action attempt.
- Key fields: `quality`, `closeness_delta`, `friction_observed`, `notes`, `next_interval_days`.

## 3) State Model and Transitions

### 3.1 Bond states (v1)

- `Dormant`: no meaningful contact beyond threshold and no active plan.
- `Active`: regular contact, loops mostly closed.
- `Drifting`: contact exists but continuity weak or delayed.
- `Strained`: unresolved tension, avoidance, or broken trust signal.
- `Renewing`: recent successful repair/re-entry sequence underway.

### 3.2 Transition triggers

Dormant -> Renewing:
- no-pressure reconnect completed and acknowledged.

Renewing -> Active:
- 2+ successful follow-through events within rolling window.

Active -> Drifting:
- missed due windows and declining closeness delta trend.

Drifting -> Active:
- one meaningful touch + explicit next beat scheduled.

Any -> Strained:
- unresolved conflict marker, repeated avoidant misses, or trust breach.

Strained -> Renewing:
- clean repair event logged + one accepted forward action.

### 3.3 Daemon escalation logic

Daemon severity increases when:
- same thread type missed repeatedly,
- friction exceeds estimate for 2+ consecutive turns,
- response latency expands while intent statements remain high.

Daemon severity decreases when:
- counter-move executes successfully,
- thread closure rate recovers,
- player maintains low-resistance consistency.

## 4) Move Taxonomy (Invariant to Allyship Core)

### Wake Up (diagnose reality)
Solves:
- unnoticed drift, vague anxiety, blind spots.

Friendcraft translation:
- inspect relationship map,
- detect silence/heat/opportunity signals,
- identify active daemon and fred state.

Examples:
- "Who has gone quiet beyond expected cadence?"
- "Which bond needs interpretation correction before action?"

### Clean Up (restore integrity)
Solves:
- unresolved loops, avoidant backlog, trust erosion.

Friendcraft translation:
- repair messages,
- apology/ownership,
- boundary clarification,
- thread closure.

Examples:
- "Close oldest open thread with one honest sentence + next step."

### Grow Up (increase capacity)
Solves:
- skill deficits that keep repeating the same failure modes.

Friendcraft translation:
- improve follow-up reliability,
- improve emotional literacy,
- improve conflict and consent handling.

Examples:
- "Practice explicit ask format with two time options."

### Show Up (embody in the world)
Solves:
- insight without behavior change.

Friendcraft translation:
- send the message,
- make the invite,
- offer support,
- set next touchpoint.

Examples:
- "Take one concrete action before noon in preferred channel."

## 5) BAR Turn Schema (v1 runtime contract)

Each turn is persisted as:

```json
{
  "turn_id": "uuid",
  "bond_id": "uuid",
  "timestamp": "ISO-8601",
  "move_family": "wake_up|clean_up|grow_up|show_up",
  "signal": {
    "type": "cadence_gap|open_thread|high_friction|opportunity|tension",
    "strength": 0.0,
    "evidence": ["..."]
  },
  "meaning": {
    "selected_problem": "string",
    "face_lens": ["architect","challenger","diplomat","shaman"],
    "daemon_hypothesis": "string|null",
    "fred_state": "warming|stable|fragile|fractured"
  },
  "action": {
    "card_id": "string",
    "channel": "text|voice_note|call|in_person",
    "instruction": "string",
    "due_at": "ISO-8601"
  },
  "consequence": {
    "attempted": true,
    "quality": 0,
    "closeness_delta": -1,
    "friction_observed": 0,
    "next_interval_days": 1,
    "next_due_at": "ISO-8601"
  }
}
```

Schema guardrails:
- A BAR turn is invalid without an action instruction.
- Consequence must be logged within review window, even if missed.
- Face lens informs meaning layer only; it does not replace player agency.

## 6) GM Faces Integration (Governance Layer)

Faces are a decision lens applied during Meaning stage.

- Architect: picks clean structure and minimum sufficient move.
- Challenger: identifies avoidance and selects stretch but feasible action.
- Diplomat: ensures tone, consent, and relational safety.
- Shaman: surfaces shadow pattern and daemon/Fred dynamics.

v1 rule:
- Use 1 primary face by default.
- Escalate to 2-4 faces only for high-friction or strained bonds.

Anti-pattern guard:
- Never automate interpretation to the point the player cannot choose their action.

## 7) Spaced Repetition Model for Friendship (SRS-F)

### 7.1 Review objects

- Bond card: global cadence for relationship.
- Thread card: unresolved arc requiring closure.
- Prompt card: action pattern effectiveness per bond.

### 7.2 Review outcomes

Per attempt capture:
- `quality`: 0 missed, 1 low, 2 good, 3 great
- `closeness_delta`: -1, 0, +1
- `friction_observed`: 0 low, 1 medium, 2 high

### 7.3 Interval adjustment (v1)

Base interval from card + historical ease.

Modifiers:
- High friction => shorten interval.
- Positive closeness => lengthen interval.
- Repeated silence => force urgent resurfacing.
- Core bonds have max interval cap to prevent disappearance.

Queue constraints:
- Daily queue size capped by player setting.
- Queue composition default: repair/follow-up first, then core maintenance, then drift reconnect.

## 8) BAR Deck Interop

Deck shuffling remains the creative variation layer.
SRS adds memory and timing precision.

Interop rule:
- Deck chooses "what move flavor".
- SRS chooses "who/when priority".
- BAR turn resolves "why and what happened".

## 9) Friendship -> Allyship Progression Bridge

Hypothesis:
- Stable friendship practice increases allyship durability because trust networks can mobilize.

Mechanism:
- Friendship campaign outputs `network_health_score` and `coordination_reliability`.
- Allyship systems consume those as readiness multipliers.

Example unlock gates:
1. Repair reliability gate
- Requirement: maintain repair completion threshold over rolling window.
- Unlock: higher-stakes allyship quests involving conflict navigation.

2. Cadence gate
- Requirement: sustained proactive friendship touches.
- Unlock: group allyship coordination quests.

3. Bridge gate
- Requirement: successful friend-to-friend bridge actions.
- Unlock: coalition-building allyship scenarios.

Principle:
- Allyship performance should not be detached from relational practice quality.

## 10) Multi-Relational Forking + New-Relationship Routing (v1.1)

### 10.1 Policy-pack model

Friendcraft runs as a core engine with forkable relationship policy packs.

Core engine (shared):
- BAR turn loop,
- Wake/Clean/Grow/Show move families,
- SRS-F scheduler,
- GM face meaning lens,
- daemon/Fred signal processing.

Policy packs (forked behavior):
- `friendship`,
- `new-undefined`,
- `poly-romantic`,
- `poly-metamour`,
- `custom-consensual`.

### 10.2 New required fields (v1.1)

Add to Bond or Container model:
- `relationship_mode`: `friendship|new-undefined|poly-romantic|poly-metamour|custom-consensual`
- `relationship_container`: `dyad|triad|pod|network`
- `consent_boundary_profile`: communication, pacing, privacy, and boundary constraints
- `intent_confidence`: 0.0-1.0 confidence about relationship path clarity

Routing rule:
- Low `intent_confidence` forces `new-undefined` prompts and blocks assumptive intimacy prompts.

### 10.3 Discovery BAR loop (when relationship path is unclear)

Question:
- "I met someone today. Which game should I play with them?"

Runtime answer:
1. Capture signals.
2. Interpret with uncertainty.
3. Choose low-risk consent-forward action.
4. Log consequence and update `intent_confidence`.

Signal families to metabolize into BAR meaning:
- reciprocity and initiation balance,
- response cadence stability,
- vulnerability depth,
- future-orientation language,
- explicit boundary clarity,
- social-context framing (friend, romantic, unclear).

Safety guard:
- Never auto-classify ambiguous signals as romantic or exclusive.
- Default to explicit check-ins and consent-safe pacing.

### 10.4 Move-family translation for new and poly contexts

Wake Up:
- Meet new person, learn preferences, map signals without premature narrative lock-in.

Clean Up:
- Metabolize positive charge from the new bond and adaptation charge from existing bonds reacting to the new person.
- Clear misattunements, assumptions, and boundary drift quickly.

Grow Up:
- Increase core relational competencies at each active GM face (structure, challenge, diplomacy, shadow literacy).
- Improve jealousy processing, expectation setting, and explicit agreements where relevant.

Show Up:
- Complete quests and campaigns together at the right container level (dyad, triad, pod, network).
- Convert insight into explicit plans, rituals, and follow-through actions.

### 10.5 Container-level quest targeting

Action targeting must match relationship container:
- Dyad quest: one-to-one action.
- Triad quest: all-three coordination or repair.
- Pod quest: subgroup ritual or planning.
- Network quest: bridge and ecosystem moves.

Anti-pattern guard:
- Do not apply dyadic assumptions to network containers.

### 10.6 Compatibility with Allyship progression

Bridge rule remains intact:
- Healthier relational practice increases allyship durability.

Extended implication:
- Multi-relational competency (clarity, consent, coordination) is a direct precursor to coalition-quality allyship.

## 11) MVP Scope Cut (Ontology-Driven)

In scope:
- Bond map (20-person pilot),
- BAR prompt deck,
- SRS queue generation,
- Review event logging,
- basic daemon types and counter-moves,
- primary face lens selection per turn.

Out of scope (defer):
- deep psychofauna progression trees,
- simulation-heavy Fred mechanics,
- geo/AR loop,
- full multi-agent face orchestration.

## 12) Instrumentation and Success Signals

Track at minimum:
- Action completion rate,
- loop closure rate,
- repair completion rate,
- median time-to-next-touch,
- % of actions rated "light/fun",
- week-4 retention,
- allyship_readiness_score trend.

Interpretation rule:
- Optimize for relational integrity and sustainability, not streak addiction.

## 13) Open Design Questions

1. How should Fred archetypes be represented in UI without over-gamifying people?
2. Which daemon taxonomy is minimal yet expressive for v1?
3. What threshold should trigger multi-face consultation in runtime?
4. Should allyship unlocks be explicit to the user or quietly adaptive?
5. What is the best failure UX when queue overload occurs?
6. Should `relationship_container` be modeled as first-class entity or enum + foreign key links?
7. What default `intent_confidence` threshold blocks romantic-coded prompts?
8. Which signals should be user-entered vs inferred from communication logs?
9. How should adaptation charge be logged across existing bonds when a new bond appears?
10. Should policy-pack switching require explicit user confirmation each time?

## 14) Next Build Artifacts

1. Data schema draft (Prisma/SQL + event logs).
2. Queue algorithm spec (deterministic pseudocode).
3. Prompt deck schema (card metadata and tagging).
4. Pilot protocol (20 bonds, 30 days, reporting cadence).
