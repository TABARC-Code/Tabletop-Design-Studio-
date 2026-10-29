# B — Miniatures Game Design Core

Unit design, stat architecture, damage/survivability curves, probability tools, points systems, keywords, and mechanical feel.

← Back to hub: `../../SKILL.md`
Cross-loads: D (activation costs), E (fragility thresholds), C (battlefield geometry), R (stat block writing)

---

## B §1 — Unit Design Framework

Stats are decision levers, not arbitrary numbers. Every stat must create a distinct tactical role.

Core stat categories:

| Stat | Controls |
|------|----------|
| Movement (M) | Mobility, objective pressure, threat range |
| Accuracy / BS / WS | Probability to hit; range effectiveness |
| Strength / AP | Ability to penetrate defence |
| Defence / Toughness / Save | Survivability axis |
| Wounds / HP | Endurance under fire |
| Damage (DMG) | Output per successful hit |
| Special Rules / Keywords | Mechanical and faction identity |

**Design rule:** Never assign a stat without knowing what behaviour you want to produce.

→ Cross-load D §1: activation frequency requirements follow directly from stat profiles.
→ Cross-load R §2: stat blocks require precise terminology — define each stat once, use it consistently.

---

## B §2 — Role-First Design (Top-Down)

Define the role first. Build mechanics to serve it.

| Role | Stat Emphasis | Design Intent |
|------|--------------|---------------|
| Skirmisher | High M, low D | Harassment, objective racing, pressure |
| Tank / Brute | Low M, high D/W | Anchor lines, absorb fire, area denial |
| Glass Cannon | High DMG, low W | Spike damage; assassination; high risk |
| Support / Controller | Auras, debuffs | Buff chains, zone control, activation manipulation |
| Elite Specialist | All-round high, low count | High-cost centrepieces; ability spikes |

Role determines: movement profile, stat emphasis, special rules tier, cost band, intended counters.

→ Cross-load C §3: roles must map to genuine decision trade-offs in the decision space.

---

## B §3 — Bottom-Up Design (Stat-First)

Use when the mechanical engine is fixed and tight balance is the goal.

Process:
1. Establish a baseline infantry profile (the "1-for-1" calibration unit).
2. Modify one attribute at a time — +1 attack, +1 movement, etc.
3. Evaluate cascading effects: damage output, survivability, threat range.
4. Rebalance through probability modelling (§11).

**Rule:** Every stat upgrade must have a visible cost elsewhere or a higher point value.

---

## B §4 — Damage Curve (Expected Output)

Core formula:

> DO = Hit Probability × Wound Probability × Damage per Hit

Interpretation:

| Curve Shape | Unit Type | Risk |
|-------------|-----------|------|
| High, flat | Reliable line infantry | Predictable meta anchor |
| High, spiky | Glass cannon / assassin | Alpha strike risk — see D §6.1 |
| Low, flat | Objective holder | Under-threat in small format — see E §1 |
| Low, spiky | Unreliable skirmisher | Poor competitive viability |

Balance by tuning: attack count, accuracy, penetration, damage profile, re-roll access.

→ Cross-load E §5.4: spike damage is especially dangerous in small-format games.
→ Cross-load D §3.2: IGOUGO amplifies alpha-strike damage curves; AA moderates them.

---

## B §5 — Survivability Curve

Measured as: expected wounds taken before death.

Factors:
- Save/armour value vs incoming strength
- Toughness differential (opponent's weapon strength relative to T)
- Wound pool size
- Mitigation abilities (invulnerable saves, "Feel No Pain" equivalents)

**Hard design rule:** No unit should combine high damage output AND high survivability unless it is deliberately rare, very expensive, and has a clear counter strategy.

→ Cross-load E §4.5: unit-level negative feedback (wounded units gaining buffs) interacts with survivability.
→ Cross-load C §9: weapon system design must create viable counters to each survivability profile.

---

## B §6 — Special Rules Economy

Special rules create mechanical flavour but must obey an economy to prevent complexity collapse.

| Tier | Examples | Frequency |
|------|----------|-----------|
| 1 — Common | Reroll 1s, charge bonuses, minor buffs | Many units |
| 2 — Moderate | Conditional extra actions, small auras | Several units |
| 3 — Limited | Teleportation, once-per-battle abilities, multi-model activations | Few units, costly |
| 4 — Game-Warping | Activation manipulation, reinforcement engines, objective redefinition | Maximum 1–2 per faction |

**Rules:**
- Tier 3–4 must be rare, costly, or limited-use.
- Keywords gate synergies; without caps, Tier 1 effects stack into Tier 4 outcomes.
- Hard cap: 3–4 special rules per unit maximum for small-format games.

→ Cross-load D §8.4: excessive special rules are a primary cause of analysis paralysis.
→ Cross-load R §3: special rules are the most common source of ambiguous sentences.

---

## B §7 — Keywords & Tag Systems

Keywords define: faction, class, size, movement type, vulnerabilities, buff eligibility, synergy gating.

**Design principles:**
- Keywords must not form infinite combo loops.
- Each keyword should unlock one clearly bounded class of interactions.
- "Too few keywords → bland homogeneity; too many → player overwhelm."
- Keyword-gated synergies are safer than open-ended ability stacking.

→ Cross-load R §2: keywords are defined terms — define once, use consistently, never drift.
→ Cross-load C §3: keyword soup is a primary cause of dominant-strategy collapse.

---

## B §8 — Points & Cost Models

**Additive costing (precision model):**
1. Define baseline infantry unit cost.
2. Assign incremental values: +1 M = X, +1 attack = Y, Tier 1/2/3/4 rule = 1/2/3/5/8.
3. Sum all components; round to nearest 5 or 10.

**Band costing (accessibility model):**
Units priced in clusters: 50 / 75 / 100 / 150 / 200+. Less precise, more intuitive. Best for casual and narrative games.

**Category caps (balance enforcement):**
- Limit duplicate units per list.
- Require role slots (minimum 1 support per 3 combat units, etc.).
- Cap per-keyword counts to prevent skew lists.

→ Cross-load E §5.2: skew lists are a primary small-format balance problem; points caps are the first fix.
→ Cross-load C §14: meta sculpting requires transparent points adjustments over time.

---

## B §9 — Terrain & Battlefield Geometry

Terrain is the "silent third player."

| Terrain Effect | Gameplay Impact |
|----------------|----------------|
| Blocks LOS | Reduces alpha strikes; rewards positioning |
| Provides cover | Increases survivability; encourages movement |
| Creates chokepoints | Forces tactical routing decisions |
| Adds verticality | Rewards spatial skill; enables skirmish depth |
| Opens kill zones | Punishes exposed movement; rewards flanking |

Good terrain: encourages manoeuvre, prevents long-range dominance, creates meaningful chokepoints.
Poor terrain: creates dead zones, enables alpha-strike lanes, produces static gunlines.

→ Cross-load D §6.1: terrain is the most elegant alpha-strike prevention tool.
→ Cross-load C §11: table geometry is a core wargame theory topic with dedicated treatment.

---

## B §10 — Symmetry vs Asymmetry

| Approach | Strengths | Risks |
|----------|-----------|-------|
| Symmetric factions | Competitive integrity, easy balance, lower barrier to entry | Bland, less narrative expression |
| Asymmetric factions | Narrative authenticity, distinctive playstyles, richer decisions | Higher imbalance risk |

Balance asymmetry with: built-in weaknesses, higher cost, scenario constraints, unique vulnerability profiles.

→ Cross-load C §10: abstraction level affects how much asymmetry is readable to players.

---

## B §11 — Probability Tools

Tools for balancing weapons, predicting outcomes, stress-testing combinations:

- Binomial expectation curves (average outcomes over N dice)
- Variance analysis (how swingy is this profile?)
- Cumulative probability (what is the chance of eliminating a unit in one activation?)
- Breakpoint identification (at what stat differential does a matchup become non-competitive?)

→ Cross-load E §5.4: use probability tools specifically to identify and cap spike-damage ceiling.

---

## B §12 — Mechanical Feel

| Design Choice | Feel Created |
|---------------|-------------|
| D6, low count | Familiar, coarse — high variance per roll |
| D6 pools | Smoothed variance, tactical re-roll decisions |
| D10 / D20 | Fine granularity, better stat differentiation |
| Custom dice | Intuitive to use, expensive to produce |
| Single roll resolution | Fast, streamlined, lower crunchy feel |
| Multi-step (hit → wound → save) | Slower, more tactical, classic GW feel |
| High spikiness | Dramatic moments; risks frustration |
| Low spikiness | Competitive stability; risks feeling flat |

Match mechanical feel to target audience and persona (→ H).

---

## B §13 — Common Design Pitfalls

- "Christmas tree" units overloaded with special rules
- Auto-win combos from uncapped keyword stacking
- Infinite loops from poorly bounded abilities
- Death stars (single models stronger than whole armies)
- Paper-rock-scissors meta lock with no counterplay
- Too many tracking tokens (marker overload)
- Damage curves that make turn 1 decisive (→ Crisis: Alpha Strikes)

---

## BIDIRECTIONAL LINKS FROM B

| To | B gives | B receives |
|----|---------|-----------|
| **D** | Activation needs per unit role | Tempo constraints shaping unit viability |
| **E** | Fragility and damage profiles | Balance pressure for small-format corrections |
| **C** | Faction asymmetry and role taxonomy | Scenario geometry shaping movement profiles |
| **R** | Keyword and stat definitions | Terminology discipline for stat block writing |
| **P** | Unit stat architecture informing how many logical types are needed | Logical types framework constraining unit categorisation design |
| **Q** | Unit stats expressed as combat factors for CRT; stacking as a unit-concentration cap | Board wargame context for when combat factor reduction works |
