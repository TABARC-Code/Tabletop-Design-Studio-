# Utility Engines Reference

Read the section matching the user's design need.

## Table of Contents
1. Balance Tuning
2. Pacing and Flow
3. Player Psychology
4. Randomness and Variance
5. Thematic Integration
6. Rules Writer
7. UX and Components
8. Production Awareness
9. Pitching and Communication
10. Critical Analysis
11. Design Reduction

---

## 1. Balance Tuning

Tunes balance: asymmetry, dominant strategies, snowball control, catch-up mechanisms, exploit detection.

### Diagnostic Questions
- Can one strategy consistently win regardless of opponent choices?
- Does an early lead compound into an unbeatable position?
- Are asymmetric powers within 5–10% of each other in win rate?
- Does the scoring system reward diverse strategies or funnel into one?

### Common Balance Failure Modes
- **Dominant strategy**: one path is always optimal
- **Runaway leader**: early advantage compounds
- **Kingmaker**: losing player determines winner
- **Snowball economy**: resources generate more resources unchecked
- **Elimination stagnation**: eliminated players have nothing to do

### Balance Levers
- Catch-up mechanisms (rubber-band scoring, underdog bonuses, cost curves)
- Diminishing returns on accumulation
- Negative feedback loops (success increases cost/risk)
- Asymmetric start positions with balanced total value
- End-trigger timing (prevents infinite snowball)

### Outputs
- BALANCE_AUDIT (dominant strategies, snowball risks, catch-up gaps)
- ASYMMETRY_ASSESSMENT (power comparison matrix)
- FIX_PRIORITY_LIST (ranked by impact/complexity)
- PLAYTEST_SCENARIOS (specific setups to stress-test balance)

---

## 2. Pacing and Flow

Tunes pacing and flow: build-up, climax, endgame acceleration, avoiding overstaying.

### Pacing Curve Model
- **Opening**: setup, early choices, establishing position (should feel quick)
- **Mid-game**: engine building, interaction peaks, key decisions (longest phase)
- **Late game**: convergence, tension, endgame trigger approaching (should accelerate)
- **Resolution**: scoring, winner determination (should be clear and fast)

### Pacing Failure Modes
- Slow start (too much setup, not enough early agency)
- Sagging middle (repetitive turns, no escalation)
- Overstaying (game should have ended 20 minutes ago)
- Anticlimactic finish (scoring reveals winner with no drama)

### Pacing Levers
- Escalation curves (increasing power/options over time)
- Timer mechanisms (countdown, resource depletion, event deck)
- Phase compression (fewer actions per turn as game progresses)
- Visible endgame triggers (players can see the finish approaching)

### Outputs
- PACING_CURVE_MAP (phase by phase analysis)
- TEMPO_DIAGNOSIS (where it drags, where it rushes)
- ESCALATION_PLAN (how tension builds)
- ENDGAME_TRIGGER_OPTIONS

---

## 3. Player Psychology

Analyses player psychology: decision fatigue, risk perception, reward schedules, social dynamics, loss aversion.

### Key Psychological Factors
- **Decision fatigue**: too many choices per turn degrades quality of play
- **Risk perception**: players overweight losses vs gains (loss aversion ~2:1)
- **Reward schedules**: variable rewards (like loot drops) create engagement; predictable rewards create satisfaction
- **Social dynamics**: ganging up, quarterbacking, kingmaking, table talk
- **Agency perception**: players need to feel their choices matter, even when they don't fully

### Incentive Alignment
Ask: what behaviour do the rules reward? If the rules reward hoarding but the game needs trading, incentives are misaligned.

### Outputs
- PSYCHOLOGY_PROFILE (fatigue points, risk appetite, loss aversion triggers)
- INCENTIVE_MAP (what behaviour the rules actually reward)
- EMOTION_CURVE (where tension/relief happens)
- SOCIAL_DYNAMICS_RISKS (bullying, ganging-up, quarterbacking)

---

## 4. Randomness and Variance

Designs and diagnoses dice/randomness systems; balances agency, fairness, and variance.

### When to use
- Dice systems, randomness, fairness, swinginess
- Output randomness vs input randomness
- Variance control, mitigation, catch-up systems
- Probability tuning for drama without coinflip outcomes

### Key Concepts

**Input randomness** (before decision): draw cards, then choose which to play. Player has agency over outcome.

**Output randomness** (after decision): choose to attack, then roll dice. Outcome determined after commitment.

Input randomness tends to feel more "strategic"; output randomness tends to feel more "dramatic". Most games use both. The ratio is the design choice.

### Variance Analysis Questions
- Where does randomness enter the system?
- What does variance affect? (Resource gain? Combat? Turn order? Map generation?)
- Can players mitigate bad luck? (Rerolls, wilds, conversion, banking)
- Does variance compound? (Early bad luck → weaker position → more bad luck)
- Is the swing proportional to player investment? (High-risk high-reward feels fair; random punishment doesn't)

### Mitigation Menu
- Draw smoothing (multi-draw, keep-one, mulligan)
- Predictable refills (open markets, deterministic income)
- Mitigation resources (rerolls, wilds, conversion tokens)
- Timing windows (act before the random event resolves)
- Insurance systems (guaranteed minimums even on bad rolls)
- Compensation (bad luck gives secondary benefit)

### Outputs
- RANDOMNESS_PROFILE (where randomness enters, what it affects)
- VARIANCE_RISKS (swing points, runaway variance, kingmaking from luck)
- MITIGATION_MENU (ways to keep agency without removing excitement)
- NUMERIC_TUNING_NOTES (what to test empirically, not fake precision)

---

## 5. Thematic Integration

Aligns mechanics to theme and builds emergent narrative without lore bloat.

### When to use
- Theme-mechanics alignment ("this doesn't feel like the theme")
- Emergent narrative from systems (stories arise from play, not flavour text)
- Making actions "feel like" the theme
- Tone control (cosy, grim, heroic, absurd) via mechanics not text

### Theme-Mechanics Alignment Method
1. List the core mechanical verbs (place, draft, trade, fight, build, convert)
2. List what the theme says players should be doing (exploring, surviving, governing, crafting)
3. Map each mechanical verb to a thematic action. If a verb has no thematic counterpart, it's either a pasted-on mechanic or the theme needs adjusting
4. Check resonance: when a player does the mechanical action, does it *feel like* the thematic action?

### Tone Control via Mechanics
- **Cosy**: low stakes per decision, recovery is easy, accumulation over loss
- **Grim**: high cost of failure, resource scarcity, permanent consequences
- **Heroic**: big swings, dramatic reversals, personal power growth
- **Absurd**: unexpected combinations, escalating chaos, comedy from systems

### Emergent Narrative Hooks
Stories arise when players can say "and then I…" about interesting sequences:
- Chain reactions across systems
- Dramatic reversals from tactical choices
- Memorable moments from unusual combinations
- Player rivalries emerging from positional competition

### Outputs
- THEME_TO_MECHANIC_MAP (verbs, resources, constraints matched to theme)
- RESONANCE_CHECKLIST (where theme leaks or contradicts mechanics)
- STORY_EMERGENCE_HOOKS (how stories arise naturally from systems)
- COMPONENT_LANGUAGE_GUIDE (naming, iconography, tone alignment)

---

## 6. Rules Writer

Writes and refines boardgame rules: clear structure, timing, edge cases, teach flow.

### Method
1. Extract the core loop, turn structure, and win condition
2. Convert mechanics into procedural rules (do X, then Y) with consistent terminology
3. Identify ambiguity: timing, targeting, hidden information, edge cases
4. Produce structured output

### Rules Structure (standard sections)
- Overview (elevator pitch, 2–3 sentences)
- Objective (how to win)
- Setup (step by step)
- Anatomy of a Turn (phases, in order)
- Actions (what players can do)
- End of Round (if applicable)
- End of Game (trigger + scoring)
- Glossary (key terms)
- Quick Reference (turn summary card)

### Common Clarity Traps
- Timing ambiguity ("before" vs "at the start of")
- Targeting scope ("choose a player" — can you choose yourself?)
- Simultaneous resolution conflicts
- Hidden information reveal triggers
- "Whenever" vs "once per turn" confusion

### Outputs
- RULES_SKELETON (structure outline)
- FULL_RULES_DRAFT
- EDGE_CASES_AND_RULINGS
- TEACH_SCRIPT (how to teach the game in 5 minutes)

---

## 7. UX and Components

Designs UX and components: iconography, information hierarchy, ergonomics, table footprint.

### Information Hierarchy Principles
- Most-needed info should be most visible (resource counts, available actions)
- Hidden info should be clearly hidden (face-down cards, screens)
- Derived info (scores, standings) should be trackable without calculation

### Iconography Rules
- Icons must pass the "squint test" (recognisable at arm's length)
- Colour-blind safety: never rely on colour alone; pair with shape/icon
- Redundancy: text + icon + colour for critical game state

### Outputs
- INFORMATION_HIERARCHY (what must be visible, where)
- ICONOGRAPHY_GUIDE (symbols, redundancy, colour-blind safety)
- TABLE_FOOTPRINT_PLAN
- COMPONENT_ERGONOMICS_NOTES (handling, shuffling, readability)

---

## 8. Production Awareness

Designs within manufacturing constraints: component costs, box size, retail realities.

### Key Constraints
- Standard box sizes and retail shelf requirements
- Component costs scale non-linearly (custom minis vs cubes vs cards)
- Setup time correlates with component count
- Print-and-play viability for prototyping

### Outputs
- BOM_SKELETON (bill of materials outline)
- COST_RISK_AREAS (what makes it expensive)
- COMPONENT_REDUCTION_SUGGESTIONS
- MANUFACTURING_CONSTRAINTS_CHECKLIST

---

## 9. Pitching and Communication

Crafts pitches: hook, player experience, differentiation, sell sheet structure.

### Hook Formula
[Player count] players [do X] to [achieve Y], but [tension/twist]. [Duration] minutes.

### Sell Sheet Structure
- Title + tagline
- Player count / duration / age
- 3–5 bullet points: what makes this different
- One image of the game in play
- Contact info

### Outputs
- HOOK_AND_LOG_LINE
- SELL_SHEET_OUTLINE
- 60_SECOND_PITCH_SCRIPT
- DIFFERENTIATION_CLAIMS (provable, not "fun for all ages")

---

## 10. Critical Analysis

Reverse-engineers published games to learn tension sources, meaningful decisions, downtime causes, and transferable patterns.

### Analysis Framework
1. Identify the core loop (what players do most of the time)
2. Map tension sources (scarcity, uncertainty, social pressure, timing)
3. Find meaningful decisions (choices where both options have real trade-offs)
4. Diagnose downtime (what causes waiting, how it could be reduced)
5. Extract transferable patterns (what to borrow ethically for your own design)

### Outputs
- TENSION_SOURCES (where pressure comes from)
- DECISIONS_THAT_MATTER (and why)
- DOWNTIME_DIAGNOSIS
- TRANSFERABLE_PATTERNS (what to steal ethically)

---

## 11. Design Reduction (Kill Your Darlings)

Removes mechanics that don't serve the experience; compresses rules and components.

### Reduction Questions
- Does this mechanic serve the core loop?
- Would the game break without it? (If no, cut it)
- Can two mechanics be merged into one?
- Does this component justify its rules weight?

### Outputs
- REDUNDANCY_LIST (what can be removed)
- MERGE_CANDIDATES (systems to consolidate)
- MINIMUM_VIABLE_RULESET
- RISK_OF_REMOVAL (what tension might be lost)
