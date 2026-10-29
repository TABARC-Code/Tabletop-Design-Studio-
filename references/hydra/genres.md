# Genre Design Engines Reference

Read the section matching the user's target genre. Each section contains a design checklist and expected outputs.

---

## § 18xx

Design 18xx-style economic/rail games: shares, stock/operating rounds, train rush.

### Core design checklist
- Capital formation and liquidity cycles
- Train roster and rust schedule (tempo control)
- Share structure and presidency incentives
- Private companies: early asymmetry without runaway
- Map topology: routes, chokepoints, tile economy
- Endgame trigger and valuation clarity

### Outputs
- 18XX_FRAMEWORK (SR/OR structure + phases)
- TRAIN_ROSTER_DRAFT (with rust/obsolescence logic)
- MARKET_RULES_DRAFT (buy/sell limits, priority, floats)
- EXPLOIT_RISK_REPORT (common 18xx degeneracies)
- PLAYTEST_SCENARIOS (early/late, bankruptcy edge, 2p/3p/4p)

---

## § 4X

Design 4X boardgames with tuned snowball controls, tech pacing, and meaningful interaction.

### Core design checklist
- Expansion curve and map control
- Economy engine: conversion rates, sinks, upkeep
- Tech progression: breadth vs depth, timing windows
- Conflict: decisive but not table-killing; kingmaking controls
- Victory structure: points vs objective vs domination; end trigger clarity
- Downtime: simultaneous phases, planning, action compression

### Outputs
- 4X_CORE_LOOP (phase structure + action economy)
- TECH_TREE_SKETCH (tiers, gates, timing)
- CONFLICT_MODEL (combat + diplomacy + deterrence)
- SNOWBALL_CONTROLS (catch-up levers)
- PLAYTEST_FOCUS (early rush, turtle, diplomacy meta)

---

## § Puzzle

Design puzzle/logic boardgames with solvable constraints, clean feedback, and replayable difficulty dials.

### Core design checklist
- State representation: what players can see and track
- Constraint density: enough to be interesting, not opaque
- Feedback loops: how players know they are closer/farther
- Hint systems: graceful fail states, adjustable difficulty
- Anti-stall: avoid brute-force search and analysis paralysis
- Replayability: variable setup, modular constraints, scenario decks

### Outputs
- PUZZLE_MODEL (constraints, actions, feedback)
- DIFFICULTY_DIALS (knobs that preserve elegance)
- SOLVABILITY_NOTES (what must be true for fair puzzles)
- RULES_CLARITY_TRAPS (common ambiguity points)
- PLAYTEST_SCRIPT (observe stall points, misreads, aha moments)

---

## § Abstract

Design abstract strategy games: perfect/near-perfect information, low randomness, high skill depth.

### Focus areas
- Information structure (perfect vs near-perfect)
- Positional evaluation and emergent complexity
- Draw/tie avoidance
- Elegance: minimal rules, maximum depth
- Scalability to different player counts (if applicable)

### Outputs
- ABSTRACT_CORE_LOOP
- POSITIONAL_ANALYSIS (what creates asymmetry from symmetric starts)
- DEPTH_ASSESSMENT (decision tree complexity vs teach time)
- TIE_PREVENTION_RULES

---

## § Ameritrash

Design thematic conflict games: drama, direct interaction, controlled swing, story moments.

### Checklist
- Input vs output randomness (keep agency)
- Combat resolution clarity and excitement
- "Story moments" generation without grind
- Comeback and anti-snowball controls
- Player elimination avoidance (or explicit intent)

### Outputs
- DRAMA_CORE_LOOP (setup → escalation → climax)
- CONFLICT_MODEL (combat, damage, mitigation)
- SWING_CONTROL_MENU (ways to keep fairness)
- EVENT_DECK_SHAPE (frequency of spikes)

---

## § Party

Design party games: fast onboarding, big groups, social fun, low cognitive overhead.

### Checklist
- Teach time under 2 minutes
- Scales to 6+ players without downtime death
- Social interaction is the fun, not the mechanism
- Low-stakes elimination or none at all
- Spectator value (fun to watch others play)

### Outputs
- PARTY_CORE_LOOP
- ONBOARDING_SCRIPT (teach in under 2 min)
- SCALING_PLAN (how it works at 4 vs 8 vs 12)
- SOCIAL_DYNAMICS_NOTES

---

## § Deckbuilder

Design deck-building games: deck as evolving algorithm, tempo, thinning, market design.

### Checklist
- Market design (static, river, draft, rotating)
- Deck-thinning and churn rates
- Snowball and tempo control
- Combo ceilings and anti-degenerate rules

### Outputs
- MARKET_MODEL (how cards enter/leave supply)
- POWER_CURVE_PLAN (early/mid/late)
- COMBO_RISK_REPORT
- PLAYTEST_MATRIX (opening buys, rush vs engine, hate-draft)

---

## § Worker Placement

Design worker placement games: action scarcity, blocking tension, opportunity cost.

### Checklist
- Action space economy (scarcity, scaling, refresh)
- Blocking vs compensation (bump, pay-to-use, reservation)
- Turn order and tempo
- Preventing dominant action loops

### Outputs
- ACTION_SPACE_MAP (what exists, why)
- SCARCITY_PROFILE (where tension comes from)
- TURN_ORDER_MODEL
- DOWNTIME_CONTROLS

---

## § Area Control

Design area control/majority games: spatial power, interaction, conflict or influence systems.

### Checklist
- Map topology and chokepoints
- Presence vs influence vs control
- Conflict resolution (combat, bidding, politics)
- Kingmaking controls and end triggers

### Outputs
- MAP_TOPOLOGY_NOTES
- CONTROL_RULES (what counts, when scored)
- INTERACTION_MODEL (fight, vote, tax, embargo)
- ENDGAME_TRIGGER (avoids stagnation)

---

## § Co-op

Design co-operative games: table vs system, communication, difficulty curves, quarterbacking control.

### Checklist
- Information structure (open vs hidden)
- Quarterbacking prevention
- Difficulty ramp and loss clarity
- Crisis cadence and recovery windows

### Outputs
- COOP_CORE_LOOP
- SYSTEM_PRESSURE_MODEL (threats, timers, entropy)
- QB_PREVENTION_MENU
- DIFFICULTY_DIALS

---

## § Hidden Role

Design hidden role/social deduction: trust economy, lying incentives, readable tells, fairness.

### Checklist
- Role distribution math (player counts)
- Information drip and accusation economy
- Elimination rules and engagement after death
- Social safety and comfort

### Outputs
- ROLE_SET (counts by player number)
- INFORMATION_FLOW_PLAN
- ACCUSATION_ACTIONS (what players can do besides talk)
- SAFETY_NOTES

---

## § Legacy

Design legacy/campaign games: persistent change, evolving rules, component mutation, narrative pacing.

### Checklist
- Permanent change types (stickers, unlocks, branching)
- Catch-up and campaign balance
- Content pacing and reveal structure
- Replayability vs one-and-done intent

### Outputs
- CAMPAIGN_ARC (sessions, unlock cadence)
- PERSISTENCE_SYSTEM (what changes, how)
- BALANCE_GUARDRAILS
- RESET_OPTIONS (if desired)

---

## § Roll-and-Write

Design roll/flip-and-write: shared randomness, private optimisation, fast turns, satisfying combos.

### Checklist
- Input generation (dice/cards) frequency and shape
- Sheet architecture and combo loops
- Solo scalability and player count
- Downtime near-zero design

### Outputs
- INPUT_GENERATOR
- SHEET_SYSTEM_MAP
- COMBO_CHAIN_RISKS
- SCORING_CLARITY_PASS

---

## § Wargame

Design wargames: tactical/historical conflict modelling, logistics, clear procedures.

### Checklist
- Scale and abstraction (tactical/operational/strategic)
- Line of sight, movement, terrain effects
- Combat resolution transparency
- Logistics and supply without paperwork bloat

### Outputs
- ORDER_OF_PLAY
- UNIT_MODEL (stats, morale, supply)
- TERRAIN_RULES
- SCENARIO_PACK_OUTLINE

---

## § Dexterity

Design dexterity games: physical skill, repeatable setups, fairness, accessibility.

### Checklist
- Physical action clarity (flick/stack/balance)
- Reset speed and robustness
- Accessibility variants and safe materials
- Scoring that rewards skill not chaos

### Outputs
- PHYSICAL_ACTION_SPEC
- RESET_AND_SETUP_FLOW
- ACCESSIBILITY_VARIANTS
- SCORING_MODEL

---

## § Trivia

Design trivia games: question quality, category balance, accessibility, pacing.

### Checklist
- Difficulty calibration and category spread
- Anti-runaway scoring and catch-up
- Dispute resolution
- Pacing (questions per minute)

### Outputs
- QUESTION_PIPELINE (how to curate/test)
- SCORING_AND_CATCHUP
- DISPUTE_RULES
- CONTENT_REFRESH_PLAN

---

## § Racing

Design racing games: tempo, catch-up, movement efficiency, blocking, risk decisions.

### Checklist
- Movement model (fixed, hand management, dice, momentum)
- Catch-up systems without rubber-band cheese
- Blocking and interaction
- Lap/finish trigger clarity

### Outputs
- MOVEMENT_MODEL
- TEMPO_AND_CATCHUP
- INTERACTION_RULES
- TRACK_DESIGN_NOTES

---

## § Strategy

Design strategy boardgames: long arcs, optimisation, interactive tension, low-luck skill expression.

### Focus areas
- Resource economies and conversion rates
- Long-term planning vs tactical pivots
- Interaction models (direct conflict, indirect races, blocking, auctions)
- Skill expression without spreadsheet overload

### Outputs
- STRATEGY_CORE_LOOP (phases, action economy)
- DECISION_TREE_MAP (what choices matter, when)
- DOMINANCE_RISK_REPORT (dominant lines, kingmaking, runaway leaders)
- PLAYTEST_SCENARIOS (early rush, turtle, denial, timing windows)
