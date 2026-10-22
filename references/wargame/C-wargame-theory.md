# C — Wargame Design & Theory

Design philosophy, decision space architecture, command and control, morale, scenario design, abstraction levels, tempo, player psychology, and meta longevity.

← Back to hub: `../SKILL.md`
Cross-loads: B (unit taxonomy), D (activation choice), E (mission feedback), F (narrative systems), G (referee-led design), R (rules writing)

---

## C §1 — Foundational Design Philosophy

Wargames exist at the intersection of four forces. Every design decision is a negotiation between them:

| Force | Represents |
|-------|-----------|
| Simulation | Representational authenticity — does this feel like real or fictional warfare? |
| Abstraction | Playability — is this fast and clear enough to actually play? |
| Theme | Aesthetic and fictional identity — what world does this evoke? |
| Player Experience | Tension, fairness, agency — is this fun and meaningful? |

**The core question every wargame must answer before anything else:**
> "What kind of battle does this game want to portray?"

All mechanics, activation choices, scenario structures, and unit roles must follow from the answer to that question.

→ Cross-load G §1: Inquisitor-style games centre this question on character, not battlefield geometry.
→ Cross-load H: the answer to this question also determines which writing persona is appropriate.

---

## C §2 — Top-Down vs Bottom-Up Design

**Top-Down (Theme → Mechanics)**
Used when fiction or history must feel authentic; when faction identity is central.

Process:
1. Define era, tech level, or fictional premise.
2. Identify battlefield assumptions (engagement ranges, mobility, command friction).
3. Set tone: gritty, heroic, chaotic, clean.
4. Build mechanics that evoke those assumptions.

Good for: historical games, grimdark settings, faction-heavy narrative games.

**Bottom-Up (Mechanics → Theme)**
Used when mechanical innovation is the core goal; when competitive balance is paramount.

Process:
1. Prototype the mechanics (dice systems, activation flow).
2. Find a theme that complements the emergent feel.
3. Build units and factions to fit the mechanical system.

Good for: competitive tournament games, elegant rulesets, system-first design.

→ Cross-load B §2–3: top-down maps to role-first design; bottom-up maps to stat-first design.
→ Cross-load D §2: activation system choice is often the first mechanical decision in bottom-up design.

---

## C §3 — Decision-Space Design

A wargame's quality is measured by the quality of its decisions.

**A good decision space:**
- Multiple viable strategies and force compositions
- Genuine trade-offs at every decision point
- Counterplay options for every dominant tactic
- No single optimal strategy that makes others irrelevant
- Rewards foresight and skill, not just dice
- Keeps players engaged continuously — no passive phases

**A bad decision space:**
- One best list; all others are clearly inferior
- Overreliance on alpha strikes
- Passive phases where one player waits helplessly
- Overpowered synergies with no counter
- Autopilot strategies that reward familiarity over thinking

→ Cross-load E §2: negative feedback loops are the primary structural tool for protecting decision space.
→ Cross-load D §3.3–4.3: IGOUGO and AA have distinct decision-space strengths and failure modes.

---

## C §4 — Friction & Uncertainty

Friction: any system that introduces limits, unpredictability, or resource tension.

Common sources:
- Random activation order ("dice in a bag")
- Orders tests and command range limits
- Suppression and morale effects
- Fog of war and hidden information
- Action point economies with hard caps
- Initiative contests and activation gambits

**Benefits:** narrative realism, prevention of perfect-information dominance, encouragement of adaptive play.
**Costs:** frustration if overused; can feel arbitrary if not thematically grounded.

**Rule:** Friction must be explicable in the fiction. Players should feel the chaos of battle, not the chaos of dice.

→ Cross-load D §5.1: unreliable activation is the most common friction mechanism.
→ Cross-load G §2: character action-chains introduce micro-level friction with narrative payoff.

---

## C §5 — Sequence of Play Architecture

The turn structure defines the emotional rhythm of the game. Choose deliberately.

| Structure | Best For | Risk |
|-----------|----------|------|
| IGOUGO | Mass battle, strategic sweep, big combos | Alpha strikes, long downtime |
| Alternate Activation | Skirmish, reactive play, tactical immediacy | Lopsided activation counts |
| Phase-Split | Balanced tactical play, hero-centric games | Can feel mechanical |
| Alternating Detachments | Company-level, combined arms | Complexity of group definition |
| Unreliable Activation | Friction-heavy narrative games | Frustration on repeated failures |
| Random Draw (Bolt Action) | Mid-scale narrative chaos | Padding risk, unpredictability |

→ Full treatment in D (Activation Systems).

---

## C §6 — Mission & Scenario Design

Scenarios are half the game. They determine movement incentives, conflict zones, force viability, and tempo.

**A good scenario:**
- Is asymmetric yet fair
- Encourages movement and forward play
- Prevents castle/turtle strategies
- Has multiple viable paths to victory
- Doesn't reward passive optimisation
- Scores progressively (not just at end)

**Scenario components:**
- Objective placement and weighting
- Scoring windows (which turns score, at what value)
- Deployment variation (affects first engagement geometry)
- Environmental effects (fog, storms, hazards)
- Twist/randomisation systems for variety

**The "why engage?" test:** For every victory condition, ask "Can a player win by doing nothing?" If yes, redesign.

→ Cross-load E §4.3: scenario-level negative feedback is the most elegant balance tool.
→ Cross-load F §5: modular scenario card engines for high-replayability systems.
→ Cross-load Crisis: "Victory Conditions Incentivise Passive Play."

---

## C §7 — Command & Control (C2) Systems

C2 models simulate battlefield command friction and hierarchy.

| Model | Mechanics | Best For |
|-------|-----------|---------|
| Strict C2 | Orders tests, command ranges, failure events | Historical games, operational scale |
| Light C2 | Leader buffs, simple morale, minimal restriction | Skirmish, character-centric games |
| Narrative C2 | Story triggers, escalating complications | Inquisitor-style, referee-led games |

**Design principle:** C2 must constrain player choice without removing agency. A player who cannot act is not having fun; a player who chooses not to act because conditions punish action is playing tactically.

→ Cross-load G §5: the GM as narrative C2 director in referee-led games.

---

## C §8 — Morale, Suppression & Battlefield State

Morale simulates psychological warfare. It is a tactical layer, never a punishment.

Tools:
- Suppression tokens (temporary action penalty)
- Pinned/shaken states (movement or shooting restrictions)
- Break tests (risk of rout on casualties)
- Retreat mechanics (forced backward movement)
- Fear/terror effects (morale penalties when near certain units)

Purpose:
- Limit unchecked lethality
- Force cover usage and positional play
- Create dramatic reversals and narrative beats
- Reinforce theme (panic, rallying, last stands)

**Warning:** Morale that removes a player from the game early is not tension — it's elimination. Design morale to keep players engaged, not to end their game.

→ Cross-load F §1: narrative skirmish games use morale as story engine, not binary elimination.

---

## C §9 — Weapon Systems Design

Weapons define: unit roles, tactical counters, threat bands, faction identity, and synergies.

Design for:
- Clear role differentiation (anti-armour, anti-horde, sniper, suppression)
- Counter-weapon relationships (every weapon has a weakness)
- Thematic resonance (a sniper is slow and deadly; a grenade explodes in an area)
- Faction identity reinforcement (faction A favours range, faction B favours shock melee)

Balance through: range bands, rate of fire, armour penetration, damage profile, special effects (blast, suppression), reliability variance.

→ Cross-load B §4: weapon stats feed directly into damage curve calculations.
→ Cross-load F §1: in narrative skirmish, weapons must behave as players expect from fiction.

---

## C §10 — Abstraction Levels

Choose abstraction scale early — it determines how much complexity players can sustain.

| Level | Features | Audience |
|-------|----------|---------|
| Low (Simulationist) | Facing, exact LoS, hit locations, ammo tracking | Dedicated hobbyist; historical grognard |
| Medium | Saves, toughness, simplified terrain, generalised facing | Mainstream miniatures market |
| High | Zones, bands, minimal tokens, few stats | Gateway products; casual players |

**Rule:** The higher the abstraction, the more narrative and theme must compensate. Players accept less precision when the game gives them more story.

→ Cross-load G §3: Inquisitor uses low abstraction on purpose — it is the source of its drama.
→ Cross-load F §6: natural-English rules language is a prerequisite for high-abstraction accessibility.

---

## C §11 — Table Geometry & Movement Economy

Movement is a primary resource. Terrain shapes all movement decisions.

Design terrain to:
- Shape lines of advance and restrict alpha strike lanes
- Create flanking routes and multiple paths to objectives
- Form meaningful chokepoints (contested ground with real tactical value)
- Break sightlines to reduce first-turn lethality
- Provide verticality for skirmish play

Poor terrain: dead zones, gunline dominance, static first turns, no positional decision-making.

→ Cross-load B §9: full terrain and geometry treatment as a unit-design factor.
→ Cross-load E §4.8: hidden negative feedback through terrain density.

---

## C §12 — Pace & Tempo Engineering

Tempo must escalate toward a climax, not peak at turn 1.

To increase tempo:
- Reduce complexity per activation
- Incentivise aggressive play through scoring
- Shorten activation loops
- Tighten scoring windows

To slow tempo:
- Introduce friction (orders tests, C2 limits)
- Add defensive incentives in early turns
- Use reserves and delayed deployment

**Design target:** Turn 1 is positioning. Turn 2 is first engagement. Turns 3–4 are crisis and resolution.

→ Cross-load D §6: turn 1 engineering is an activation-system tool.
→ Cross-load E §6: the optimal small-format tempo curve (turns 1–4).

---

## C §13 — Player Psychology & Game Feel

Players must feel: fair treatment, responsive mechanics, genuine tension, dramatic peaks, the possibility of recovery.

Key principles:
- Reward proactive behaviour; penalise passivity
- Mitigate extreme randomness without eliminating uncertainty
- Offer comeback mechanics that feel earned, not artificial
- Make losses meaningful but not catastrophic
- Ensure the game communicates its state clearly (who is winning, and why)

→ Cross-load E §2: negative feedback loops are the mechanical expression of player psychology principles.
→ Cross-load H: persona selection affects how these principles are communicated in rules text.

---

## C §14 — Meta-Sculpting & Balance Longevity

A healthy long-term meta requires:
- No single dominant faction or strategy
- Scenario diversity (no "meta scenario" that invalidates others)
- Regular but gradual points adjustments
- Transparent designer communication
- Controlled introduction of new mechanics over time

**Rule:** Meta changes must be evolutionary, not violent. Sudden major balance swings destroy player investment and trust.

→ Cross-load B §8: points system design is the primary meta-sculpting tool.

---

## C §15 — Failure Modes Reference

| Problem | Primary Fix | Cross-Reference |
|---------|------------|----------------|
| Alpha strike dominance | Terrain, deployment rules, turn 1 restrictions | D §6.1, E §5.1 |
| Overpowered synergy stacking | Keyword caps, Tier limits | B §6–7 |
| Static defensive meta | Forward scoring objectives, time limits | C §6 |
| Passive openings | Mission pressure, deployment spread | E §4.6 |
| Excessive randomness | Smooth damage curves, gate crits | B §4, E §5.4 |
| Complexity overload | Special rule caps, keyword reduction | B §6, R §2 |
| Unfun missions | "Why engage?" audit on every objective | C §6, E §4.3 |

---

## BIDIRECTIONAL LINKS FROM C

| To | C gives | C receives |
|----|---------|-----------|
| **B** | Scenario geometry shaping movement profiles | Faction asymmetry and role taxonomy |
| **D** | Scenario design governing activation flow | Activation choice governing how scenarios play out |
| **E** | Mission-level negative feedback | Small-format refinements sharpening scenario design |
| **F** | Macro philosophy grounding narrative systems | Narrative scenario structures enriching all scenario design |
| **G** | Wargame theory scaffolding for referee-led design | Character-driven scenario DNA informing all wargame missions |
| **P** | Tight/loose axis, tipping point principle, logical types vocabulary | Design philosophy anchoring which position on the axis fits a given game |
| **Q** | ZOC, CRT, supply as specific friction and decision-space implementations | Board wargame context for when simulation depth is appropriate |
