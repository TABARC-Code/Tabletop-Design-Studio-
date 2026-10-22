# P — Priestley & Lambshead: Design Language & Presentation

The vocabulary of design (tight vs loose), formalising the game space, the learning vs referencing rulebook dichotomy, functional rule layers, the "Say Why" principle, the Rule of Three, tone, troublemakers, skirmish game design, and campaign architecture.

**Primary source:** Rick Priestley & John Lambshead — *Tabletop Wargames: A Designers' and Writers' Handbook* (Pen & Sword, 2016)

← Back to hub: `../SKILL.md`
Cross-loads: C (design philosophy), R (rules writing), B (unit design), I (world/faction)

---

## P §1 — The Language of Design

Designers who work together develop shared terms for concepts. These terms aren't important in themselves — what matters is that the underlying concepts are understood. Priestley and Lambshead offer a specific vocabulary that clarifies what different design choices actually do.

> "A designer knows he has achieved perfection not when there is nothing left to add, but when there is nothing left to take away." — Saint-Exupéry

This is the governing philosophy of tight design. Every element must earn its presence.

---

## P §2 — Tight vs Loose Design

The most fundamental design axis in Priestley and Lambshead's framework.

### P §2.1 — Tight (Clean) Design
Games like Chess or Go: few rules, precisely defined, each piece moves only one defined way, no ambiguity about range or line of sight.

Properties of a tight design:
- Minimal logical types (few unit categories, each governed by its own fully defined rules)
- Single, clearly defined victory condition
- Consistent resolution mechanics applied uniformly across all contexts
- Player decisions directly influence probability outcomes
- No "ifs or buts" — the rules never leave a situation undefined

**Benefit:** Competitive integrity, fast play, no rules disputes.
**Cost:** Can feel sterile or lacking in character. Some players find it chess-like in a negative sense.

### P §2.2 — Loose Design
More open rules that frame outcomes and intent rather than mechanical procedures precisely. Players become participants in interpreting the rules during play.

**Benefit:** Atmospheric, flexible, supports narrative and social play.
**Cost:** Risks inexactitude; requires good faith between players to function.

**Design principle:** There is no right or wrong position on this axis. Use the right tool for the job. Know where your design sits and why.

→ Cross-load C §10: abstraction level is the structural expression of this axis.
→ Cross-load R §2.3: tone selection reflects where on the tight-loose axis a game sits.

---

## P §3 — Formalising the Game Space

Ways to impose tight geometry on a free-form tabletop:

| Method | How it works | Effect |
|--------|-------------|--------|
| Full grid (squares/hexes) | Discrete positions; all range, LOS, movement calculated from grid | Maximum tightness; feels board-gamey |
| Zone division | Battlefield split into large areas each containing multiple units | Semi-tight; good for operational/mass battle |
| Templates | Fixed-shape movement and range tools (X-Wing model) | Pseudo-grid; free-form movement with geometric precision |
| Base geometry | Rectangular bases with defined front/flank/rear zones | Local geometry exploited for facing and formation rules |
| Fixed measuring rods | Standardised sticks for movement and range | Eliminates measuring disputes; speeds play |

**Key insight:** A game doesn't need a physical grid to have grid-like tightness. Templates, bases, and fixed rods all impose geometry without looking like a boardgame.

→ Cross-load B §9: terrain and battlefield geometry as design tools.
→ Cross-load C §11: table geometry and movement economy.

---

## P §4 — Logical Types

A logical type is a category of unit governed by its own distinct rule set. Chess has six types. Most wargames have far more.

**Design rule:** The more logical types and sub-types, the less tight the design. Each new type adds cognitive load and creates potential rule-interaction problems.

**Change of state rules** (a unit becoming "shaken," "pinned," or "hull-down") effectively create sub-types. These must be handled carefully — a type that behaves differently in two states is two logical types sharing a miniature.

**Practical guidance:** Audit your types. If two units share 90% of their rules, merge them. If a type requires a separate sub-section of the rulebook to function, it may be a design smell.

→ Cross-load B §6: special rules economy — excessive special rules multiply effective logical types.
→ Cross-load R §3.2: pattern-and-exception hunting catches inconsistent logical type behaviour.

---

## P §5 — The Tipping Point Principle

On attrition and combat damage — one of Priestley's most actionable mechanical insights:

> "It is critical to avoid slow, grinding, mind-numbing attrition in favour of a delayed but clear tipping point, where the player who has more successfully marshalled his forces can hope to see the game swing decisively in his favour."

The tipping point design pattern:
- Units accumulate damage or stress markers across multiple combats
- When a threshold is reached, the unit's capability degrades sharply (becomes "Shaken," cannot attack)
- The player who has preserved undamaged reserve units can then commit them decisively
- This creates nail-biting suspense as forces accumulate hits, followed by a dramatic endgame

**Mechanical expression:** Hail Caesar's "Shaken" state, Lion Rampant's half-strength trigger. Both use this principle.

**Design test:** Does your game have a tipping point? Or does it grind linearly from start to finish? Linear attrition is rarely satisfying.

→ Cross-load E §6: the tempo curve (turns 1–4) — the tipping point should arrive at turn 3 (crisis).
→ Cross-load A §2.1: the tipping point is the "disaster" in the scene-sequel loop.

---

## P §6 — The Learning-Focused vs Referencing-Focused Rulebook

Priestley's most distinctive rulebook contribution: the two-mode framework.

### P §6.1 — Learning-Focused Approach
The text is written for a reader who knows nothing and is reading sequentially to learn the game.

Characteristics:
- Sequential structure; information builds on what came before
- Explains and discusses rules, not just states them
- Uses "reassurance asides" ("we'll handle the exception later, don't worry for now")
- Repeats rules in different contexts when helpful
- Longer text than strictly necessary; examples woven throughout

Risk: If rules are repeated in multiple places, any change must be made everywhere. Repetition introduces ambiguity if wording varies even slightly. Mark all repetitions in the working copy.

### P §6.2 — Referencing-Focused Approach
The text is written for players who already know the game and need to check details quickly during play.

Characteristics:
- Rules nested logically by domain (1.1.1 → 1.1.1.1)
- Terse; no discussion or examples unless essential
- Assumes player knowledge; no hand-holding
- Works best when game domains are cleanly separated (all shooting in its own phase)

Risk: Opaque to newcomers; limits accessibility; the Catch-22 problem (players must learn from the text to play, but the text assumes they already play).

### P §6.3 — The Practical Compromise
**The rulebook must serve two readers simultaneously:** the learner and the veteran in mid-game lookup.

Priestley's resolution:
- Write core rules learning-focused
- Organise with clear headers for mid-game referencing
- Provide a separate **quick-reference playsheet** (the single most important accessory)
- Add a glossary and, where possible, an index
- Use functional layers (§P7) to signal to the reader what kind of text they're reading

→ Cross-load R §1: macro structure of a rulebook — both approaches map onto the same macro structure.
→ Cross-load R §5: navigation architecture serves the referencing reader.

---

## P §7 — Functional Rule Layers

Priestley's layered model of how rules are organised by scope and dependency:

```
CORE RULES        — Turn sequence, movement, shooting, combat, morale
      ↓ (dependent on)
SCENARIO RULES    — Setup, deployment, objectives, terrain, victory conditions
      ↓ (dependent on)
FORCE RULES       — Army lists, points, unit-specific rules, national characteristics
      ↓ (dependent on)
EXTENDED RULES    — Supplements, fortifications, sieges, campaigns, edge cases
```

**Critical principle:** Rules at each layer must not be dependent on rules in an outer layer. Core rules cannot require scenario rules to function — but scenario rules can override or constrain core rules.

**The interaction trap:** When a core rule creates a unit type capability, and a scenario rule restricts deployment, and those rules interact — you get the "Tiger tank upstairs" problem (Avalon Hill's Squad Leader). Close definition combined with "anything not forbidden is permitted" produces absurd outcomes.

**Design test:** Draw your dependency arrows. If any arrow points upward (outer layer to inner layer), you have a design problem.

→ Cross-load R §1: rulebook structure — the layer model determines section order.
→ Cross-load C §15: failure modes table includes scenario-core rule conflicts.

---

## P §8 — The Dice / Probability Chapter (Alea Iacta Est)

Key insights from Priestley on randomness:

**Rare events via triggers:** Rather than rolling for a 1% probability every turn (tedious), attach rare events to dice already being rolled for another purpose. A roll of 12 on a 2D6 command test triggers a "blunder" — the event happens approximately once every 30 rolls, but the second dice roll on a "what went wrong" table is exciting, not bureaucratic.

**Probability management:** Players must feel that their decisions influence outcomes. A game where outcomes are entirely random is a lottery. A game where probability is entirely determined by player skill has no tension. The ideal: player decisions shift probability in meaningful ways, but chance cannot be eliminated.

→ Cross-load B §11: probability tools for balancing — same mathematics, design application.
→ Cross-load D §1: activation systems control when those probability rolls happen.

---

## P §9 — Tone of Discourse (Tenor)

Priestley uses "tenor" to mean the register and manner in which rules are written:

- **High/formal tenor:** Precise, stiff, interpreted narrowly. Suits serious historical simulations and tournament games. Risk: dull and uninviting.
- **Low/informal tenor:** Open, accessible, interpreted broadly. Suits light-hearted games. Risk: inexactitude and verbosity.

**Design rule:** Match tenor to subject. A game about Napoleonic grand tactics can afford higher tenor than a skirmish game about zombie apocalypse survivors. The tenor signals to players how literally to interpret rules.

→ Cross-load R §2.3: tone selection in rules writing — same concept, full treatment.

---

## P §10 — The "Say Why" Principle

> "If you give an instruction or make a statement, explain why such a thing is necessary or why it is the case."

Saying why:
- Helps the reader remember a rule by providing a mental hook
- Smooths over rules that might seem arbitrary or counter-intuitive
- Addresses the process of play, not just the rule mechanics
- Speeds play ("rather than rolling each dice individually it will speed up play if the player rolls all the dice at once")

**Caution:** Too much "say why" becomes verbose and introduces doubt. Use it for important rules, unusual exceptions, and procedural shortcuts — not for every standard rule.

---

## P §11 — The Rule of Three

For critical rules that must be properly understood:

1. **Name and flag it:** "This rule is very important because it underpins the whole combat system."
2. **State it clearly and briefly.**
3. **Illustrate it:** Extended example or diagram resolving potential misinterpretation.

Also phrased as: "tell 'em you're telling 'em, tell 'em, then tell 'em you've told 'em."

Not necessary for every rule — reserve for rules where misunderstanding would break the game.

→ Cross-load R §3.1: sentence labelling — the Rule of Three maps onto imperative → definition → example.

---

## P §12 — Troublemakers (Language Pitfalls)

Specific language problems Priestley identifies for wargame rules writers:

| Troublemaker | Problem | Fix |
|-------------|---------|-----|
| "Die" vs "Dice" | "Die" is technically correct singular but unfamiliar and ambiguous ("a good day to die") | Use "dice" throughout, even in singular, for consistency and accessibility |
| Semi-colon | Technically valid but commonly misread; signals that prose is doing too much in one sentence | Replace with short sentences or dashes; if you need a semi-colon, the sentence is probably too long |
| Jargon desensitisation | Designers become blind to their own jargon during development | Get fresh eyes; blindtest specifically for terminology confusion |
| Modifier direction | In roll-under systems, positive modifiers are penalties; can confuse without clear definition | State explicitly early: "higher modifiers make this easier/harder" |
| Placeholder names | Working titles adopted for convenience become final through inertia; odd names survive to publication | Commit to proper terms early; audit all working names before finalising |
| Consistency of terms | Stats named similarly ("Move value" and "Missile value" → "Mo" and "Mi") become confused | Ensure stat abbreviations are clearly distinct at a glance |

---

## P §13 — Skirmish Game Design (Priestley Chapter 6)

Skirmish games (individual model focus, 6–20 models) have distinct design challenges:

**The sameness problem:** Without enough variation in individual models, skirmish games repeat the same encounter structure. Solutions:
1. Novel mechanics (Sfiligoi's Song of Blades probabilistic action sequence — roll up to 3 dice, two failures end your turn)
2. Scenario-driven narrative (story arcs, character progression)
3. Reference cards exporting complex character rules off the main table

**The speed imperative:** Modern skirmish games must flow scene-to-scene like a "fast-cut action movie." Core rules must be clean. Character detail, if included, must not slow the game — externalise it onto cards.

**The card trap:** When playing cards becomes more important for victory than manoeuvring models, the game has become a card game. Keep models central.

**Unpredictability at small scale:** Events predictable at large scale become chaotic at small scale (climate vs weather, crowd vs individual). Higher unpredictability is realistic and also reduces sameness.

→ Cross-load F §1: Warcry's foundational principles address the sameness and speed problems.
→ Cross-load E §1: small-format volatility — same problem, quantified.

---

## P §14 — Campaign Design (Priestley Chapter 9)

Campaigns = meta-games or serial games linking individual sessions.

**Types of campaign structure:**

| Type | Description | Best For |
|------|-------------|---------|
| Narrative campaign | Sessions form a story arc with branching outcomes | Character-driven games; Inquisitor-style |
| Territorial campaign | Forces control regions; gains and losses are strategic | Historical games; operational scale |
| Ladder campaign | Players build forces over time; progressive points totals | Club play; competitive environments |
| Event campaign | Linked scenarios with fixed outcomes feeding into a final battle | Tournament; fixed narrative |

**Army characterisation in campaigns:** Force choices must feel redolent of the army they represent, be distinct from other forces, offer a fighting chance, and use commercially available models. Historical campaigns carry the additional constraint of audience expectations about what a given army "should" be able to do.

**Codex Creep:** When multiple designers contribute to the same game system over time, force values inevitably escalate. Each supplement's units are slightly more powerful to feel exciting. The result is systemic inflation. Solution: establish design parameters clearly at the outset, with explicit cost ceilings per category.

→ Cross-load F §7: narrative campaign structures — Warcry-style approach.
→ Cross-load G §7: Inquisitor campaign consequence architecture.
→ Cross-load A §8: scene-sequel mapping for campaign designers.

---

## P §15 — Expanding the Rulebook

The modern rulebook is not only core rules. Players expect additional content:

- **Army lists:** Cover major combatants at launch; follow the law of diminishing returns (each additional list serves a progressively smaller audience)
- **Scenarios:** Illustrated play-throughs; showcase what the game looks like in practice
- **Hobby material:** Painting guides, modelling notes, background — optional but widens the audience
- **Playsheet:** The single most important accessory; all commonly used tables on one sheet; provide a downloadable version

**Design principle:** In the modern rulebook, core mechanisms may take up less than half the space. The rest is content that makes the rules come alive.

---

## BIDIRECTIONAL LINKS FROM P

| To | P gives | P receives |
|----|---------|-----------|
| **C** | Tight vs loose axis as a design vocabulary; the tipping point principle | Design philosophy anchoring which axis is appropriate for a given game |
| **R** | Learning vs referencing dichotomy; functional layers; Say Why; Rule of Three; Troublemakers | Rules text structure that implements these presentation principles |
| **B** | Logical types as a unit-design constraint; modifier direction clarity | Unit stat architecture that determines how many logical types are needed |
| **I** | Army characterisation principles; Codex Creep as a meta-sculpting failure mode | World and faction design that determines what each army must feel like |
| **E** | Skirmish speed imperative; the card trap warning | Small-format volatility problems that skirmish design must solve |
