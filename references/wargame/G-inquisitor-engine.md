# G — Inquisitor Narrative Engine

Referee-led play, character-first philosophy, the action-chain activation mechanic, location-based damage, GM tools, scenario design with divergent motivations, and campaign consequence architecture.

← Back to hub: `../SKILL.md`
Cross-loads: F (narrative infrastructure), D (action-chain as activation variant), C (wargame theory scaffolding), H (persona for writing Inquisitor-style material)

---

## G §1 — Root Design Philosophy

### G §1.1 — Characters, Not Units
Every model on the board is:
- A fully motivated actor with internal logic
- A flawed protagonist — not a stat line
- A narrative vector capable of generating drama
- A source of emergent story through their decisions and failures

**Mechanics must support personality-driven decisions, not list optimisation.**

A unit in a standard wargame is an asset. A character in an Inquisitor-style game is a person. The design implications are profound.

→ Cross-load F §1: narrative skirmish shares this principle at a slightly lighter intensity.
→ Cross-load H (Dorian Blackwood persona): the appropriate writing voice for character-driven narrative material.

### G §1.2 — Narrative Before Mechanics
> "Mechanics serve story. They never dominate it."

Therefore:
- The scene defines which rules are relevant — not the rulebook index
- The GM adjudicates special cases based on fictional logic
- The game simulates what *should* happen, not just what the dice decree

### G §1.3 — Play the Character, Not the Game
Inherited from 1970s Western Gunfight wargaming lineage:
- Players choose actions based on what their *character* knows — not what the *player* knows
- Perfect-information metagame decisions are violations of the social contract
- Narrative integrity is sustained by character-perspective decision-making

This eliminates the metagame problem of "my character wouldn't do this but it's optimal" — in Inquisitor-style play, that conflict doesn't arise.

---

## G §2 — The Action-Chain Activation Engine

The signature mechanic of Inquisitor. A character-level activation system that treats every second of combat as a micro-drama.

### G §2.1 — The Chain Process
1. Player declares a sequence of micro-actions for their character.
2. Player rolls Speed number of dice.
3. Each success = one declared micro-action executed.
4. Failures introduce chaos, interruption, or partial completion.

### G §2.2 — Micro-Action Menu
Actions that can be chained in a single activation:

| Physical Actions | Interactive Actions |
|-----------------|-------------------|
| Turning in place | Drawing / holstering a weapon |
| Running (partial move) | Aiming (bonus to next shot) |
| Vaulting terrain | Interacting with an object |
| Diving for cover | Communicating (shout, signal) |
| Charging | Opening / closing a door |
| Reloading | Picking up an item |
| Shooting | Pulling a lever / triggering an event |

### G §2.3 — Benefits of the Action Chain
- Cinematic feel — every roll is a micro-drama
- Tension in every activation — a string of failures is a story moment
- Emergent narrative — unplanned failures create the most memorable scenes
- Realistic staggered motion — a character cannot teleport across a room in one burst

### G §2.4 — Modern Simplifications
The original system can be slow in practice. Modern refinements:
- Use simplified lookup tables for the most common action combinations
- Consolidate micro-actions into 3–5 categories (Move, Interact, Fight, Shoot, React)
- Reduce or automate derived calculations
- Keep narrative richness; reduce bookkeeping friction

→ Cross-load D §2: the action chain is a distinctive activation variant on the low end of the AA spectrum — fully character-granular.
→ Cross-load R §2–3: action chains require exceptionally precise rules language to avoid ambiguity.

---

## G §3 — Derived Character Statistics

Inquisitor's original stat system modelled physical reality in detail:

| Stat | Controls |
|------|---------|
| Speed | Number of dice in the action chain |
| System Shock Value | Threshold for being stunned |
| Consciousness Threshold | When unconscious state triggers |
| Injury Value | Cumulative damage before death |
| Instant Death Limit | Single-hit kill threshold |

**These create nuanced physical modelling but generate significant play friction.**

Modern design approach — consolidate without losing narrative depth:
- Replace multiple derived stats with lookup thresholds
- Combine System Shock + Consciousness into a single "Resilience" track
- Automate injury state transitions
- Use a tiered state system: **Active → Shaken → Wounded → Critical → Dead**

→ Cross-load B §1: the stat framework from the miniatures design core provides a cleaner modern template.

---

## G §4 — Location-Based Damage

A hallmark mechanic of Inquisitor. Separate wound tracking for different body zones creates narrative specificity.

**Original system — four zones:**
- Head (instant-death risk; high-value target)
- Torso (core wound pool; heaviest combat zone)
- Arms (affects combat effectiveness; weapon use impaired)
- Legs (movement impaired; falling risk)

**Damage generates narrative states:**
Light Wounds → Heavy Wounds → Crippling Effects → Bleeding → Knockdown → Stun

**Modern simplification approach — three zones:**

| Zone | Narrative Effect | Mechanical Effect |
|------|-----------------|------------------|
| Head | Stun, disorientation | Action chain shortened next activation |
| Torso | Core injury | Reduces wound threshold |
| Limbs | Impairment | Movement or combat penalty |

**Tokenise conditions:** use a small set of tokens rather than sub-tracking:
- Stunned (–dice next activation)
- Bleeding (take 1 damage at start of each activation)
- Crippled (movement halved; cannot sprint)

**Goal:** Preserve the drama of specific injury without the bureaucracy of tracking each zone separately.

→ Cross-load B §5: survivability curve design — location damage creates asymmetric survivability profiles.

---

## G §5 — The Role of the Referee (GM)

Inquisitor is not a balanced competitive game. It requires a GM to function as written.

**GM responsibilities:**
- Frame the scenario and deliver narrative hooks
- Control all NPCs and neutral characters
- Deliver timed narrative events
- Adjudicate ambiguous actions based on fictional logic
- Manage hidden information asymmetrically
- Maintain pacing and dramatic tension
- Balance dramatic fairness (not mechanical fairness)

**The GM as AI director of the tabletop.**

**What this unlocks:**
- Scenarios can have hidden objectives per player
- Events can trigger based on narrative logic rather than mechanical triggers
- Outcomes can be adjudicated based on what is most dramatically appropriate
- Players can attempt actions not covered by rules (GM rules on the spot)

→ Cross-load F §5: the modular scenario card engine is a GM-optional structure that partially formalises the GM role for pickup play.
→ Cross-load C §7: narrative C2 is the light version of GM-led adjudication.

---

## G §6 — Scenario Design Principles

An Inquisitor-style scenario includes:

**Required elements:**
- A strong narrative hook (why are these characters here, today?)
- Divergent motivations per faction (not everyone wants the same thing)
- Hidden information (not all players know the full picture)
- NPC complications (third parties with their own agendas)
- Environmental hazards (the world itself is dangerous)
- Open-ended objectives (players should be able to achieve goals in unexpected ways)
- Timed events (things happen whether players are ready or not)
- Branching outcomes (the session's result shapes the next session)

**Scenarios must reward creativity and lateral thinking, not min-maxing.**

If a player can "solve" a scenario the same way every time by optimising their character stats, the scenario has failed.

→ Cross-load C §6: the "why engage?" audit applies here — every objective must reward active engagement.
→ Cross-load F §5: modular scenario elements can be drawn from an Inquisitor-themed card system.

---

## G §7 — Campaign Architecture

Inquisitor campaigns emphasise stakes and permanent consequence.

**Progression elements:**
- Permanent injuries (lost limbs, scars, chronic conditions)
- Reputation shifts (Inquisition standing; faction relationship changes)
- Moral corruption arcs (characters drift toward radicalism or purism)
- Political entanglements (decisions create enemies and allies)
- Faction influence trees (your warband's standing in broader power structures)
- Equipment acquisition and loss (not just upgrades — downgrading is possible)

**Campaign arc design:**
- Each session should feel like a chapter in a novel
- No session should be meaningless — always have stakes
- Player investment must be protected — death should be rare and earned
- Corruption and moral compromise should escalate gradually, not spike suddenly

**Tone:** The campaign should feel like reading a grimdark novel one chapter at a time.

→ Cross-load F §7: Warcry-style campaign structure for lighter versions of these principles.
→ Cross-load E §6: tempo curve applies to the campaign arc as well as individual sessions.

---

## G §8 — Thematic Pillars

Core tone for Inquisitor-style design:

| Pillar | Expresses As |
|--------|-------------|
| Gothic | Architecture, horror imagery, decay and grandeur |
| Industrial | Grinding mechanisms, pollution, oppressive infrastructure |
| Paranoid | Hidden enemies, unreliable allies, information asymmetry |
| Morally ambiguous | No clean heroes; every faction has blood on its hands |
| Investigative | The game is often about finding out what is happening |
| Character-centric | Individual relationships matter more than armies |

**Core narrative themes:**
- Radical vs puritan conflict (ends and means)
- Internal political warfare within the Inquisition
- Secret cults and hidden heresies
- Covert missions with moral complexity
- Purges and their unintended consequences

→ Cross-load H (Dorian Blackwood + Dr. Lucian Graves personas): these are the appropriate cognitive frames for writing this material.

---

## G §9 — The Western Gunfight Heritage

**Inquisitor's actual lineage:** 1970s man-to-man Western Gunfight skirmish rules — not traditional RPGs.

This explains:
- GM-led adjudication (the referee controlled NPCs and the world)
- Personality-driven action decisions
- Narrative primacy over mechanical procedure
- Micro-action declarations
- Map-based tactical puzzle design

**Design implication:** Do not "RPG-ise" Inquisitor-style games incorrectly. The GM is an arbiter of a wargame with narrative richness, not a dungeon master for a roleplaying game. The distinction matters for how rules are written and how scenarios are structured.

---

## G §10 — Modern Inquisitor Design Checklist

**Preserve:**
- Story-first focus
- GM-led adjudication
- Micro-action flow (simplified)
- Location-aware injury
- Character-driven drama and divergent motivations

**Improve for modern play:**
- Accessibility (cleaner stat blocks)
- Play speed (shorter chain lengths, faster tables)
- Scenario creation tools (starter missions, templates)
- Optional points system for pick-up games
- Simplified injury states (3 zones, tokenised conditions)
- Clearer rules language (→ R)

---

## BIDIRECTIONAL LINKS FROM G

| To | G gives | G receives |
|----|---------|-----------|
| **F** | GM-led depth; investigative scenario content; character-driven mission DNA | Narrative infrastructure (terrain, modular scenarios, campaign frameworks) |
| **D** | Action-chain as a granular activation variant | Micro-action timing framework from activation theory |
| **C** | Character-driven scenario DNA informing all wargame mission design | Wargame theory scaffolding for referee-led structure |
| **H** | Content and tone that triggers Dorian Blackwood + Graves personas | Writing voice that gives Inquisitor material its distinctive atmosphere |
