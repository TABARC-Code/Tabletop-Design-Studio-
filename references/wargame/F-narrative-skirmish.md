# F — Narrative Skirmish Engine (Warcry DNA)

Warcry's design philosophy, the dice economy initiative system, parkour movement, modular scenario card engines, natural-English rules language, and campaign architecture.

← Back to hub: `../SKILL.md`
Cross-loads: D (AA core loop), E (negative feedback), B (unit roles), G (Inquisitor narrative depth), C (scenario integration)

---

## F §1 — Foundational Principles

A Warcry-style narrative skirmish game prioritises:

- Fluid, parkour-style movement — the board is an obstacle course, not a constraint
- Constant player engagement — no long waits, no passive phases
- Fast alternating activations — the tempo is the drama
- Visual clarity — readable board state at a glance
- Simple, legible stats — minimal chart-checking
- Strong narrative scaffolding — the game generates stories, not just outcomes
- High replayability — no two sessions tell the same story
- Emergence over planning — fun surprises happen by default

**The design philosophy in one sentence:**
> Fun, surprising, story-rich moments should happen as a natural output of the system, not by accident.

→ Cross-load G §1.2: the parallel Inquisitor principle — "mechanics serve story, they never dominate it."
→ Cross-load C §1: the core question "what kind of battle does this game portray?" is answered by narrative skirmish as "a cinematic chase-and-brawl."

---

## F §2 — The Dice Economy Initiative System

Warcry's most significant design innovation. A dual resource economy built into every round.

**The mechanics:**
1. Both players roll 6 dice at the start of each round.
2. Dice are grouped by matching values: Singles / Doubles / Triples / Quads.
3. **Singles (unique results) → Initiative control.** More singles = better chance of going first.
4. **Doubles, Triples, Quads → Ability fuel.** Matched dice unlock special abilities of matching type.

**The core tension each round:**
> "Do I sacrifice initiative control for a powerful ability, or hold singles for priority?"

**Wild dice:** Players may modify one or more dice within narrow limits, enabling clutch initiative swings and risk-reward tension.

**Design benefits:**
- Natural variety — most rounds feel mechanically distinct
- No deterministic combo chains from turn to turn
- Gentle natural negative feedback (bad ability round = strong initiative round)
- Extremely high replayability from probabilistic variety
- Every round is a small decision puzzle

**Generalising this system:**
- Replace rolled dice with drawn tokens (token pool variant)
- Use multi-colour dice (different colours = different resource types)
- Add "momentum dice" that carry over between rounds
- Command dice variants for C2-flavoured systems

**Key insight:**
> "What you can do each round is shaped by probability, not preparation." This fuels genuine replayability because no round is the same.

→ Cross-load D §5.2: the dice economy is a highly specific variant of the random-draw hybrid activation system.
→ Cross-load E §4.7: the dice economy is also a built-in resource-level negative feedback mechanism.

---

## F §3 — Alternate Activation as the Core Loop

Warcry was the first mainline GW game with full alternate activation. This was a deliberate design choice for its emotional effect.

**Why AA fits narrative skirmish:**
- Back-and-forth immediacy mirrors the feeling of a real brawl
- Players are never waiting long — maximum involvement
- Individual models matter; each activation is a small drama
- Positioning becomes the decisive skill
- No long downtime windows for disengagement

**The Warcry AA flaw:**
Lopsided warbands — where one side has significantly more models — create free activations at round-end. The larger warband "dumps" activation of weak models, then takes uncontested final actions.

**Solutions for new designs:**
- Activation token decay: excess activations lose their value past a cap
- Second-activation cost: activating the same model twice costs a resource
- Alternating micro-groups: small squads activate as a unit when one side is larger
- "Tactical surge" once per round: smaller warband can activate an extra model when outnumbered
- Momentum cap: maximum 2 consecutive activations by the same player

→ Cross-load D §4.3–4.4: full AA failure modes and fix toolkit.
→ Cross-load E §4.4: activation-level negative feedback for underdog situations.

---

## F §4 — Movement Philosophy ("Parkour Play")

Designer principle from Warcry development notes:
> "The game must reward players for using the board, not punish them."

**Warcry movement principles:**
- Climbing costs half movement or is free
- Verticality is actively encouraged
- Terrain is dense and multi-level
- Movement is frictionless — no dice rolls, no tests
- Jumping uses flat difficulty targets only
- Models treat the table as a 3D obstacle course

**Design effects:**
- Encourages melee and ranged units to share 3D space
- Creates cinematic chases and rooftop confrontations
- Rewards spatial skill and prediction
- Makes terrain an opportunity, not a penalty

**Design heuristics:**
- Never punish bold movement choices with dice rolls
- Allow charging downward from height as a tactical option
- Build terrain that is camera-ready (interesting sight lines at model eye level)
- Equal access to verticality for all unit types

Movement should feel like action cinema, not a footslogger's tax.

→ Cross-load B §9: terrain and battlefield geometry as a unit-design factor.
→ Cross-load C §11: table geometry and movement economy from macro theory.

---

## F §5 — Modular Scenario Generation (Card Engine)

Warcry uses four modular card decks. This produces thousands of legal game combinations.

**The four decks:**

| Deck | Controls |
|------|---------|
| Terrain | Table layout and density |
| Deployment | Starting positions and force spacing |
| Victory conditions | What wins the game this session |
| Twists | Environmental, narrative, or mechanical modifiers |

**Design advantages:**
- Infinite replayability without infinite content creation
- Fast setup (draw 4 cards, play)
- Easy expansion (add cards to any deck)
- Supports narrative campaign variability naturally
- Occasional Twists act as soft negative feedback (→ E §4.2)

**Generalisation guidelines for new designs:**
- Use 3–5 decks; more creates combinatorial confusion
- Keep each deck at 8–12 cards for manageability
- Ensure all legal combinations remain playable (no impossible pairings)
- Use Twists for: environmental drama, narrative stakes, or mechanical modifiers
- Test all combinations in blind playtesting

→ Cross-load C §6: scenario design principles (asymmetric but fair, encourages movement).
→ Cross-load G §6: Inquisitor-style scenario DNA (divergent motivations, hidden information) enriches card deck content.

---

## F §6 — Natural-English Rules Language

Explicit design principle from Warcry's development:
> "Avoid legalese. Keep rules human."

**Guidelines:**
- Use short, declarative sentences
- Use active voice ("Roll two dice" not "Two dice should be rolled")
- Avoid nested conditional statements (if A, unless B, then C, except when D)
- Define keywords only when they genuinely reduce total word count across the book
- Prefer natural-language descriptions for one-off rules that appear only once

**What natural-English rules increase:**
- Accessibility for new players
- Speed of play (no mid-game rules consultation)
- Player retention
- Fairness perception (ambiguity creates disputes)
- Ease of house ruling and scenario design

**What to avoid:**
- Dense keyword bloat (B §7 warns against this)
- Paragraphs with multiple embedded conditions
- "Legal document" phrasing
- Inconsistent verb choice (→ R §2 for full treatment)

→ Cross-load R §2: the full rules-writing style guide for applying these principles.
→ Cross-load C §10: high abstraction level is a prerequisite for natural-English rules to work.

---

## F §7 — Narrative Campaign Structures

Narrative skirmish thrives on progression. A campaign gives every game stakes beyond the session.

**Campaign elements:**
- Branching quest paths (player choices shape the arc)
- Boss battles and dungeon-style scenarios
- Artefact unlocks and rare equipment hunts
- Territory control and resource systems
- Injury tables with meaningful but recoverable consequences
- Escalating missions with narrative stakes
- Definitive end states (the campaign has a conclusion)

**Design guidelines:**
- Progression must be steady, not exponential — avoid runaway power creep
- Permanent injuries should be meaningful but never make a warband non-viable
- Campaign rewards should expand options and story, not raw power
- Comeback viability must be maintained throughout — a player 3 sessions behind must still believe they can win
- Allow "soft resets" at campaign phase transitions (everyone levels up to a baseline)

→ Cross-load G §7: Inquisitor-style campaign architecture with permanent consequences and moral corruption arcs.
→ Cross-load E §6: tempo curve applies to individual sessions within a campaign arc.

---

## F §8 — The Inquisitor Connection

Warcry is not a descendant of Inquisitor, but they share a design lineage:

| Shared Element | In Warcry | In Inquisitor |
|----------------|-----------|---------------|
| Emergent narrative | Via dice economy and scenario variety | Via action chains and character motivation |
| Character-driven choices | Each fighter is distinct | Each model is a fully motivated actor |
| Terrain-centric combat | Parkour movement and 3D board | Detailed terrain interaction as micro-actions |
| GM-friendly scenarios | Modular card engine allows referee use | GM required for play |

This module integrates with G (Inquisitor Engine) to produce GM-led missions, investigative scenarios, and narrative-heavy play modes that are too complex for the card-deck system alone.

→ Cross-load G §1–6: full Inquisitor design treatment for referee-led, character-driven sessions.

---

## F §9 — Failure Modes & Fixes

| Problem | Fix | Cross-Reference |
|---------|-----|----------------|
| Lopsided activations | Activation penalties; momentum caps; micro-group activation | D §4.4, E §4.4 |
| Ability spam | Frequency limits; stacking restrictions; dice economy gating | F §2, B §6 |
| Movement exploits | Bounding jump distances; clarify "within" vs "wholly within"; vertical measure rules | F §4 |
| Campaign power creep | Hard bonus caps; soft resets; tiered threats; capstone missions | F §7, G §7 |
| Rules bloat | Max 3–4 special rules per fighter; compact ability text; universal keywords | B §6, R §2 |
| Scenario staleness | Expand card decks; add Twist variety; ensure all combinations are legal | F §5 |

---

## BIDIRECTIONAL LINKS FROM F

| To | F gives | F receives |
|----|---------|-----------|
| **D** | Dice economy initiative as a distinctive activation hybrid | Activation engine that Warcry-style games run on |
| **E** | Warcry comeback tools as concrete E §4.7 examples | Pacing pressure; alpha-strike prevention requirements |
| **B** | Movement and terrain interaction requirements shaping unit design | Unit roles and stats determining which movement freedoms are viable |
| **G** | Narrative infrastructure (terrain, scenarios, campaigns) as foundation | GM-led depth; investigative scenarios; character-driven mission content |
| **C** | Narrative scenario structures enriching all scenario design | Macro philosophy grounding narrative systems in design theory |
