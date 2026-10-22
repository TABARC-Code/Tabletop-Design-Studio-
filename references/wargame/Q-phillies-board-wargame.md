# Q — Phillies: Board Wargame Mechanics & Playtesting Methodology

Zone of Control, stacking, Combat Results Tables, supply lines and isolation, replacement systems, deployment design, victory conditions design, and systematic playtesting methodology drawn from academic game design practice.

**Primary source:** George Phillies — *Designing Wargames: Introduction* (2014)

← Back to hub: `../SKILL.md`
Cross-loads: C (design philosophy), D (turn sequence), B (unit design), R (rules writing and playtesting)

---

## Q §1 — The Rules-as-Program Model

Phillies' central metaphor: a set of game rules is a computer program given to a Natural Intelligence (the players).

Implications:
- **Playtesting = debugging.** The only reliable way to discover that your program runs as intended is to run it.
- **Rules language = code.** Ambiguous rules are like ambiguous code — they produce unpredictable outputs.
- **Players = CPUs with different instruction sets.** Different players will interpret the same rules differently; this is a feature to be managed, not an anomaly.
- **Playtesting at different skill levels = testing at different load levels.** A solution found by expert players may be invisible to novices, and vice versa.

**Critical principle:** Balance of a game between top-level players may be very different from balance between merely good players. Playtest with people of varying skill levels. Expert fixes that average players cannot find have no value.

→ Cross-load R §4: playtesting methodology — Phillies' academic approach in full.

---

## Q §2 — Zone of Control (ZOC)

One of the key mechanical innovations of Charles Roberts (Avalon Hill's founder). A unit's Zone of Control extends over the squares adjacent to it, creating tactical depth without adding physical units.

### Q §2.1 — What ZOC Does
- Creates operational friction: enemy units cannot freely move through contested hexes
- Represents the threat radius of a deployed force without requiring individual models for every threat vector
- Forces attacker to "pin" defender's flanks before safely advancing
- Creates natural defensive lines from small numbers of units

### Q §2.2 — ZOC Variations
The same general mechanic can be instantiated in many ways:

| Variant | Mechanic | Effect |
|---------|---------|--------|
| Standard ZOC | Enemy units stopping in your ZOC; leaving costs extra MPs | Strong defensive anchor; tricky to bypass |
| Partial/fractional ZOC | ZOC only partially blocks; terrain modifies ZOC | More fluid; rewards positional play |
| Negation | Your ZOC cancels enemy ZOC in contested hexes | Allows counterattacks to "open" corridors |
| Extended ZOC | ZOC extends 2 hexes for high-quality units | Elite troops create wider threat radius |
| No ZOC | Units have no ZOC at all | Fast-play; mass battle feel |

**Design principle:** The ZOC model you choose fundamentally shapes how your game plays. High-ZOC games reward defensive positioning and line-holding; low-ZOC games reward mobility and exploitation.

→ Cross-load D §3: IGOUGO systems are most historically associated with ZOC-based board wargames.
→ Cross-load C §4: ZOC is a friction mechanism — it limits player agency in thematically motivated ways.

---

## Q §3 — Stacking

Placing multiple units on the same hex/square — stacking — requires rules governing how many units can occupy the same position.

**Stacking limits:** Typical limits are 1–4 units per hex depending on scale. Stacking limits serve several functions:
- Forces players to spread their forces (preventing "death stars" of concentrated power)
- Creates realistic frontage constraints at operational scale
- Generates interesting decision-making: when to stack and when to spread

**Stacking and movement:** Stacking limits typically apply at the end of the movement phase, not during movement. This allows concentration through a bottleneck (a unit can pass through a crowded hex if it doesn't end there).

**Stacking and zones of control:** Units already in an enemy ZOC cannot normally enter another enemy ZOC without first attacking. This is where stacking and ZOC interact most dramatically.

→ Cross-load B §7: keyword systems are the miniatures-game equivalent of stacking limits.

---

## Q §4 — Combat Results Tables (CRT)

The Combat Results Table is the core resolution mechanic of classical board wargames. Players calculate the ratio of attacking to defending strength, look up the column, roll a die, and apply the result.

### Q §4.1 — CRT Structure
Columns are typically labelled by attack-to-defence ratios: 1-3, 1-2, 1-1, 3-2, 2-1, 3-1, 4-1, 5-1, 6-1.

Results include combinations of:
- **Attacker Eliminated (AE):** All attacking units removed
- **Exchange (EX):** Both sides take losses equal to the weaker force
- **Attacker Back (AB):** Attacker retreats
- **Defender Back (DB):** Defender retreats
- **Defender Eliminated (DE):** All defending units removed

### Q §4.2 — Design Implications
- **Odds reduction:** When computing combat ratio, fractions are rounded down. 2.95-1 becomes 2-1. This compresses the effective range of ratios and rewards concentration.
- **Predictability vs uncertainty:** Higher-ratio columns have more predictable outcomes; lower ratios are more chaotic. Experienced players concentrate forces to achieve reliable high-ratio attacks.
- **AE results:** Attacker elimination at unfavourable odds creates a real cost for reckless attacks — a key design feature that rewards careful combined arms.
- **EX results:** Exchanges disproportionately hurt the numerically superior side, providing a natural negative feedback loop.

### Q §4.3 — Alternatives to the CRT
- **Unit-vs-unit resolution:** Each unit rolls separately; results are more granular but slower
- **Differential tables:** Use attack minus defence (rather than ratio); changes probability landscape significantly
- **Custom tables per terrain/unit type:** Add flavour but multiply complexity

→ Cross-load B §4: damage curve — the CRT is the board wargame expression of the damage output calculation.
→ Cross-load P §2.1: the CRT is a classic tight-design element.

---

## Q §5 — Supply Lines and Isolation

Supply rules simulate the logistical constraints of real warfare. They are one of the most powerful tools for creating strategic depth in a board wargame.

### Q §5.1 — Supply Line Mechanics
A unit is "in supply" if it has a continuous path (not blocked by enemy units, enemy ZOC, or impassable terrain) back to a supply source.

**Isolation effects** (when supply is cut):
- Units cannot receive replacements
- Combat effectiveness degrades (reduced attack factors, must retreat if attacked)
- After a defined number of turns isolated, units are eliminated

**Design purpose:** Supply rules force players to maintain coherent lines rather than making individual "suicide" attacks. They also reward the player who can sever enemy supply rather than engaging frontally.

### Q §5.2 — Supply as Negative Feedback
Supply rules create a natural negative feedback loop:
- The side that is winning (advancing) may overextend, cutting their own supply lines
- The side that is losing (retreating) may be falling back to shorten and strengthen supply
- This prevents runaway victories by creating logistical costs for rapid advances

→ Cross-load E §2: negative feedback loops — supply is a structural negative feedback mechanism.
→ Cross-load C §4: supply is a friction mechanism implementing command limitations.

---

## Q §6 — Replacement and Reinforcement Systems

How defeated or depleted forces recover is a major design variable.

### Q §6.1 — Replacement Systems
Units that have been eliminated can be rebuilt from "replacement factors" generated each turn by cities or supply sources. The replacing player pays the cost and places the rebuilt unit at a designated replacement city.

**Design variables:**
- Rate of replacement (how many factors per turn, per city)
- Who can be replaced (any eliminated unit vs specific unit types)
- Where replacement occurs (fixed cities vs any friendly territory)
- Interaction with isolation rules (can isolated cities generate replacements?)

### Q §6.2 — Reinforcement Systems
Pre-scheduled new units enter the map at specific turns and locations. Unlike replacements, reinforcements are independent of casualties.

**Design purpose:** Historical reinforcement schedules represent real-world production and deployment timelines. They also create known "events" that players can plan around, adding strategic depth without random mechanics.

### Q §6.3 — Balance via Replacement Rate
**Key insight from Phillies:** Games where victory depends on exploitation of particular rules features — rather than on the extensive mechanics — are very hard to retune. If the game is essentially decided by supply-line advance speed, then all the combat rules become irrelevant.

Test: Play through and observe which rules are actually used in a typical game. Rules that are never triggered are either dead weight or evidence that the game's victory path bypasses them.

→ Cross-load C §14: meta-sculpting — replacement rate adjustment is a primary balance tool.

---

## Q §7 — Opening Positions and Deployment Design

In many board wargames, players set up their own starting positions within defined constraints. This is itself a design element:

**Deployment as decision:** The Russian player (in Stalingrad) places their defence first; the German player responds. Each side's deployment reveals their initial strategy. A bad Russian defence loses the game before it starts; a bad German deployment costs the initiative.

**Design variables:**
- Who deploys first (usually the defender)
- Deployment zones (where can each side place units?)
- Stacking limits during setup (must stacking limits hold at placement?)
- Hidden deployment (do opponents know each other's positions?)
- Pre-determined deployment (fixed historical positions vs player choice)

**Design principle:** If you allow player-chosen deployment, the opening position becomes part of the game's decision space. This increases replay value but also increases the complexity of learning (new players may make unrecoverable deployment errors before understanding why).

→ Cross-load I §3.1: faction doctrine should be reflected in recommended deployment styles.
→ Cross-load C §6: scenario design includes setting the constraints of deployment.

---

## Q §8 — Victory Conditions for Board Wargames

Phillies' treatment of victory conditions is distinct from Ford's (which focuses on miniatures games). For board wargames:

**City capture conditions:** Holding key cities for a defined number of consecutive turns. Provides clear, geographically anchored objectives. Creates the "race" dynamic — attacker must advance; defender must hold.

**Elimination conditions:** All enemy units removed. Almost always secondary to city capture — the game will typically end via cities before elimination is achieved.

**Time limit conditions:** The defender wins by surviving to a defined turn. Creates asymmetric pressure: attacker must achieve objectives quickly; defender profits from delay.

**Multiple simultaneous victory conditions:** Risk of dominant strategy emerging where one condition (e.g., capture a single key city) becomes the solved path. Test: is any single path to victory always the "best" path?

**The near-obvious early winner problem:** When the outcome is effectively determined several turns before the formal victory condition is met, the losing player should feel free to concede. Forcing an obviously decided game to its formal conclusion is poor sportsmanship — but the winning player must never ask the loser to resign.

→ Cross-load C §6: the "why engage?" test for victory conditions.
→ Cross-load A §2.1: the scene's "disaster" must never be clean success — applies to turn-by-turn victory condition tracking.

---

## Q §9 — Playtesting Methodology (Academic Model)

Phillies' systematic approach to playtesting, drawn from academic game design courses:

### Q §9.1 — Stage 1: Designer-Present Verbal Play
The designer explains rules verbally and observes play. Goal: identify whether the mechanical concept works at all.

**Design implication:** At this stage, the game is deliberately underdeveloped. If the prototype is completely finished at the first playtest, the designer will be reluctant to make significant changes.

> "A good author must be prepared to murder her children." — rules modules that don't work must be discarded, not polished.

### Q §9.2 — Stage 2: Written Rules Playtest (Semi-Blind)
Players learn from a written draft. The designer observes but does not explain. Key protocols:
- Designer bites their tongue — only intervenes if play completely stalls
- Players say their rules interpretations aloud ("I move four squares, costing 2 MPs...")
- Designer records all moments of confusion, dispute, or unexpected interpretation
- **Approach by question, not correction:** "How did you calculate that movement cost?" not "You got that wrong."

### Q §9.3 — Stage 3: Blind Playtesting
Players in geographically remote locations receive only the written rules. The designer has zero involvement during play.

**What this discovers:** Problems that only appear when the designer cannot compensate. If the book cannot stand alone, the game is not ready.

Modern tools: electronic game modules (ZunTzu, Vassal) allow complete records of blind-test play to be reviewed by the designer.

### Q §9.4 — The Design Notebook
Every design decision, challenge, and evolution should be dated and recorded in a design notebook. An index is essential. Sackson (the greatest American board game designer) maintained indexed design notebooks throughout his career and attributed significant success to them.

**Practical value:** The notebook is the primary defence against "creeping assumptions" — the gradual accumulation of design decisions made verbally during playtesting that never get written into the rules.

### Q §9.5 — Extreme-Option Testing
Traditional warning: "test the extreme options." The example: can players exploit the most unusual rules interactions to produce anomalous results?

People who are excellent playtesting debuggers can:
- Identify rules features that disrupt play before even playing the game
- Find exploitation paths that other playtesters will never discover

→ Cross-load R §4: playtesting methodology — full treatment in the rules writing module.

---

## Q §10 — Rules Families and Iterative Design

A game designer can take the rules model of an existing game, apply it to a new campaign or battle, and create a new game. This is legitimate and commercially rational — players of earlier games in the family have already learned the rules.

**The challenge:** Rules appropriate for one historical epoch or scale may be inappropriate for another. Modern air combat genuinely does not resemble Roman legion warfare.

**The opportunity:** Studying rules families — groups of games sharing structural DNA — teaches designers what specific mechanics actually do, separate from their thematic context.

**The responsibility:** Structural similarities should be acknowledged; accidental similarity is not the same as innovation. A designer who has not studied the field will rediscover existing mechanics and call them novel.

→ Cross-load C §2: top-down vs bottom-up design — rules-family design is essentially bottom-up starting from an existing system.

---

## Q §11 — Key Design Variables Summary (Board Wargames)

A checklist of the primary mechanical choices specific to board wargame design:

| Variable | Options | Design Impact |
|----------|---------|--------------|
| Grid type | Hex, square, none (free-form), zone | Tightness, thematic fit, visual style |
| ZOC model | Strong, partial, fractional, none | Defensive depth vs mobility |
| Stacking limit | 1–6 units | Force density, frontage realism |
| Turn structure | IGOUGO, phase-split, alternating | Tempo, downtime, alpha-strike risk |
| Resolution | CRT, differential, unit-vs-unit | Probability landscape, speed |
| Supply | Strict, loose, none | Strategic depth, logistical realism |
| Replacement | Replacement factor, scheduled reinforcement, none | Recovery arc, late-game balance |
| Deployment | Player choice, historical, random | Opening decision depth, replay value |
| Victory | City capture, elimination, time limit, combination | Player motivation, game length |

---

## BIDIRECTIONAL LINKS FROM Q

| To | Q gives | Q receives |
|----|---------|-----------|
| **C** | ZOC, supply, and CRT as specific friction and decision-space tools | Design philosophy determining when simulation depth is appropriate |
| **D** | Turn structure as the operational context for ZOC and supply rules | Activation system choices determining where ZOC resolves in the turn |
| **B** | Stacking limits as the board-wargame equivalent of unit caps; CRT as damage curve | Unit stat design for when force strengths need to be expressed as combat factors |
| **R** | Playtesting methodology; the design notebook; blind testing discipline | Rules language standards that blind testing will probe |
| **E** | Supply as a structural negative feedback loop; EX results as negative feedback | Small-format balance tools that parallel supply's macro-level function |
