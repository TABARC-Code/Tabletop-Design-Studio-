# D — Activation Systems Engine

IGOUGO vs Alternate Activation, hybrid systems, tempo engineering, turn 1 protection, negative feedback via activation, and failure mode fixes.

← Back to hub: `../SKILL.md`
Cross-loads: B (unit activation needs), C (scenario tempo), E (small-format pacing), F (Warcry dice economy), G (action-chain micro-activation)

---

## D §1 — Core Principle: Activation = Time Control

An activation system controls:
- Who acts first and how often
- How long each player waits between decisions
- How fast the board state changes
- Whether the game feels strategic, tactical, chaotic, or deliberate

It determines: game feel, pace, fairness perception, and alpha-strike vulnerability.

**Activation is the heartbeat of a wargame.** Everything else — units, weapons, missions — is built upon it.

→ Cross-load C §5: sequence of play architecture for the macro-level turn structure context.
→ Cross-load B §1: unit stat profiles dictate how often a unit must activate to fulfil its role.

---

## D §2 — The Two Primary Poles

```
[I-GO-YOU-GO] ————————————————————— [ALTERNATE ACTIVATION]
 Strategic sweep                         Tactical immediacy
 Big swing turns                         Constant response
 Alpha-strike hazard                     Lopsided activation hazard
```

Most modern designs sit between the extremes. Understanding both poles clarifies every hybrid.

---

## D §3 — I-Go-You-Go (IGOUGO)

### D §3.1 — Characteristics
Player A activates all units. Player B activates all units. Turns form large, sweeping phases.

### D §3.2 — Strengths
- Strategic, top-down, grand-scale feel
- Supports complex combos and synergy chains
- Easy to teach; intuitive sequencing
- Thematic resonance for mass battles

### D §3.3 — Weaknesses
- **Alpha strikes:** Player A can destroy key units before Player B acts
- **Death spirals:** Losing units reduces ability to retaliate → further losses
- **Combo vulnerability:** Coordinated buff-stacks can break the game in one phase
- **Downtime:** Non-active player may wait minutes with no decision to make

### D §3.4 — Design Tools to Mitigate IGOUGO Weaknesses
- Deployment constraints separating forces
- Turn 1 range limits or "no shooting turn 1" rules
- Counter-activation reactions (opponent can interrupt)
- Alternating phase priority within the IGOUGO framework
- Terrain density breaking LOS

→ Cross-load E §5.1: IGOUGO alpha strikes require external structural correction.
→ Cross-load C §11: terrain is the most elegant IGOUGO correction tool.

---

## D §4 — Alternate Activation (AA)

### D §4.1 — Characteristics
Players alternate activating one unit at a time. Turn length stays stable throughout.

### D §4.2 — Strengths
- Minimal downtime — players are constantly involved
- Natural negative feedback: fewer models = fewer activations = shorter rounds (underdog recovers pacing)
- Dynamic back-and-forth tension
- Positioning becomes the star mechanic

### D §4.3 — Weaknesses
- **Lopsided activations:** The player with more units can "dump" weak activations early, then take uncontested actions at the end (the Warcry flaw)
- **Activation padding:** Cheap filler units taken purely for tempo advantage

### D §4.4 — Tools to Stabilise AA
- Second-activation costs (Kill Team model: second activation of same unit costs a resource)
- Activation groups (activate a small squad, not a single model)
- Token burn / delay mechanics
- Priority roll with catch-up bias for fewer-model side
- Fatigue tracking on repeated activations
- Momentum caps: hard limit on consecutive same-player activations

→ Cross-load E §4.4: activation-level negative feedback for detailed AA stabilisation tools.
→ Cross-load F §3: Warcry's specific AA implementation and its known flaw.

---

## D §5 — Hybrid Activation Systems

### D §5.1 — Unreliable Activation (Lion Rampant, Warmaster)
Units test to activate; failure ends the activation run.
- Benefits: unpredictable tempo, shorter turns, narrative misfires feel dramatic
- Risk: repeated failures frustrate; requires thematic justification

### D §5.2 — Dice-in-a-Bag (Bolt Action)
Each unit contributes a coloured die to a shared bag. Drawn randomly.
- Benefits: narrative chaos, dynamic order, good for mid-scale forces
- Risk: activation padding (more units = more dice = more turns)

### D §5.3 — Command + Random Draw (Star Wars: Legion)
Key units receive direct order tokens; remaining units activate from a random pool.
- Hybrid of player control + organic friction
- Best of both: agency for critical units, unpredictability for others

### D §5.4 — Alternating Detachments
Units activate in defined groups (squads, fireteams, detachments).
- Best for company-level, combined-arms, large battles with tactical granularity
- Reduces per-model cognitive overhead while preserving AA benefits

### D §5.5 — Phase-Split (MESBG model)
"I move, you move; I shoot, you shoot" — each phase alternates priority.
- Extremely fair; very tactical; supports hero-centric design
- Minimal alpha-strike risk; shared initiative feel

→ Cross-load F §2: the Warcry dice economy is a highly specific hybrid of D §5.2 and initiative control.
→ Cross-load C §5: summary comparison of all turn structures for design selection.

---

## D §6 — Tempo Curve Engineering

### D §6.1 — Turn 1 Must Not Be the Most Impactful Turn

The core design rule of modern activation engineering.

Enforcement tools:

| Tool | Method |
|------|--------|
| Range limits | Units cannot shoot maximum range on turn 1 |
| Incomplete deployment | Units arrive in waves, reducing turn 1 combat mass |
| Scoring delay | Objectives do not score until turn 2 or 3 |
| Early cover bonuses | Units in deployment zones have enhanced saves |
| Action economy restrictions | Certain abilities unlock only from turn 2 |
| Fog of war | Hidden deployment reduces alpha targeting |
| Terrain density | LOS naturally blocked in deployment zones |

**Target arc:** Tempo rises steadily toward a climax mid-to-late game.

→ Cross-load E §4.6: tempo-level negative feedback treatment.
→ Cross-load C §12: pace and tempo engineering from a macro-theory perspective.

### D §6.2 — Comeback Mechanics via Activation
- Priority bias for the player who is losing
- "Underdog" reaction activations (once-per-round free response)
- Reserve activations that deploy based on game state
- Momentum caps preventing extended activation chains by the winning side

→ Cross-load E §4.4: comprehensive underdog activation tools.

---

## D §7 — Negative Feedback via Activation

Activation systems are one of the cleanest ways to implement natural balance correction:

- Priority roll bias toward the player behind
- "Second wind" activation for the losing player
- Momentum caps that prevent the leading player chaining activations
- Cooldown tracks on repeated activations
- Suppression effects that disproportionately limit the winning side's options

**Rule:** The best activation-based negative feedback is invisible to players — it should feel like the natural rhythm of battle, not a handicap system.

→ Cross-load E §2: the full theory and toolkit for negative feedback loops.

---

## D §8 — Failure Modes & Fixes

### D §8.1 — Alpha Strikes
Fix: terrain, deployment spread, turn 1 range limits, reaction activations, phase-split structure, turn 1 special ability restrictions.
→ E §5.1 for comprehensive alpha-strike countermeasures.

### D §8.2 — Lopsided Activations
Fix: second-activation penalties (Kill Team), activation grouping, token caps, initiative equalisation mechanics, combined activations for surplus models.
→ E §4.4 for small-format specific treatments.

### D §8.3 — Activation Padding
Fix: minimum unit cost thresholds, hard limits on duplicate units, combined activations for identical-unit pairs, category caps in list building.
→ B §8: points and category cap models.

### D §8.4 — Analysis Paralysis
Fix: reduce the decision tree per activation (3 options is ideal, 5+ causes stalling), add timer mechanics, simplify action menus, reduce branching for non-key units.
→ B §6: special rules economy — fewer rules per unit reduces decision complexity.
→ R §2: rules clarity reduces apparent complexity of the same decision.

---

## D §9 — Activation by Scale

| Scale | Model Count | Best Systems |
|-------|------------|-------------|
| Skirmish | 6–20 models | AA, random draws, reaction mechanics |
| Mid-scale | 20–60 models | Alternating detachments, phase-split, semi-random |
| Mass battle | 100+ models | IGOUGO, you-go-I-react, command friction systems |

Scale matters enormously. The same activation system that creates tension at skirmish scale produces chaos at mass battle.

→ Cross-load C §10: abstraction level and scale are linked design decisions.
→ Cross-load F §3: narrative skirmish uses AA as its core loop specifically because it suits 6–20 models.

---

## D §10 — Activation & Narrative

Activation timing = emotional rhythm of the game.

Used deliberately to shape:
- Dramatic reversals (sudden priority shift mid-round)
- Heroic moments (one model taking multiple risky actions)
- Tension spikes (unknown what comes out of the bag next)
- Narrative beats (failed activation = the troops hesitate; succeeded = they charge)
- Scenario flow (priority shifts at key turns)

→ Cross-load F §2: the Warcry dice economy is the fullest realisation of narrative activation design.
→ Cross-load G §2: Inquisitor action-chain activation as character-level narrative timing.

---

## BIDIRECTIONAL LINKS FROM D

| To | D gives | D receives |
|----|---------|-----------|
| **B** | Tempo constraints shaping unit design and viability | Activation needs per unit role |
| **C** | Activation choice governing how scenarios play out | Scenario design controlling tempo and activation flow |
| **E** | Tempo backbone; turn 1 timing data | Small-format corrections tightening tempo |
| **F** | Activation engine that Warcry-style games run on | Dice economy initiative as a distinctive activation hybrid |
| **G** | Micro-action timing framework | Action-chain mechanic as a specific activation variant |
