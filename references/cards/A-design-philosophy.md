# Reference A: Design Philosophy

## A §1 — What Card Games Actually Are

Card games are decision-space contests. Players win or lose based on the quality of their decisions, not raw execution skill. Every design choice must protect and enrich that decision space. When mechanics reduce the game to a test of resources (who has better cards) or luck (who drew better), the game stops being a strategy game and becomes something else.

The essential value a card game delivers is this: the player is making meaningful decisions under uncertainty. Uncertainty comes from hidden information (opponent's hand), from randomness (draw), from the complexity of card interactions, and from the psychology of reading the opponent. These are features, not bugs.

**The four interactive forms:**
- **Toy** — no goal, pure exploration (a sandbox card environment with no win condition)
- **Puzzle** — binary goal, solved once (a single-use combo puzzle)
- **Contest** — measurement of execution (top-decking pure luck games)
- **Game** — contest of decision-making (what we are building)

A card game is a game. It must measure decision-making. If it degrades toward pure contest (whoever draws the power rare wins) or pure puzzle (assemble the combo, win automatically), it has failed as a game.

## A §2 — Decision Space Audit

The decision space of a card game is the set of meaningful choices available to the player at any given moment.

Audit questions for any design:
1. Can a player make choices that differ from the optimal play and still win?
2. Does the opponent's strategy require a genuine response, or can it be ignored?
3. Are there at least three distinct strategic axes in the game (e.g. aggro/control/combo)?
4. Do individual card choices feel like they matter, or does the outcome depend on the draw?
5. Is there a dominant strategy that makes all other choices suboptimal?

A healthy decision space has: multiple viable strategies, meaningful responses between players, genuine tension about what the opponent holds, and a feeling that clever play can overcome a worse hand.

A collapsed decision space has: one dominant strategy, no viable counters, games decided by turn 2 or 3 before meaningful interaction, and a meta where deck quality matters more than play quality.

## A §3 — Elegance Doctrine (The Clockwork Principle)

Elegance means accomplishing as much as possible with as little as possible. In card game design this means:
- Every card should have exactly as much text as it needs, not more
- Every mechanic should create multiple uses rather than one narrow use
- Every keyword should interact with the rest of the system, not exist in isolation
- Every rule should serve multiple purposes

**The content trap:** Card games are content-heavy by nature. Every card is a piece of content. The temptation is to add complexity to content (more keywords, more stats, more special rules) rather than building more elegant systems. Content complexity raises the barrier to entry without adding proportional depth.

**The clockwork alternative:** A system where a small number of rules generates a large number of interesting states. The best card games achieve this. A card with two stats and one keyword, interacting with ten other cards, produces more interesting decisions than a card with six stats and four keywords that only works in one combo.

**Practical application:**
- Start with the minimum viable ruleset. Add only what the design requires.
- When a card needs four lines of text, ask whether that complexity is earning its cost
- Prefer rules that create emergent interaction over rules that describe specific exceptions
- One rule that governs many cards is more elegant than ten rules that each govern one card

## A §4 — Low-Number Design

Low-number design means every stat point matters. It is the primary mathematical framework for TCG/CCG balance.

**Why it works:**
- When a card has 2 health and another does 2 damage, the relationship is exact and meaningful
- Changing a 2-damage card to 3 damage is a 50% increase in lethality against that target
- Designers can reason about interactions precisely without needing spreadsheets
- Players can understand the game without calculators

**What it enables:**
- Keywords with numerical interactions (e.g. "+1/+1 whenever X") have predictable cumulative effects
- Power curves are manageable: a 3-cost card with 3/3 stats is a benchmark; deviation from it is a design signal
- Futureproofing is easier because the number range is bounded

**What to avoid:**
- Inflation: if stats start creeping into double digits, the low-number benefit erodes
- Asymmetric inflation: if one faction's cards run higher numbers than another's, it breaks comparisons
- Power creep: new sets raising the baseline stats means old cards become unplayable

**Deck builder note:** Deck builders that run over a single session (roguelikes) can allow stat inflation within a run because the reset at run-end resets the baseline. This is a design exception, not a license for TCG/CCG inflation.

## A §5 — Content vs System Design

**Content-based systems** treat the game as a container for cards. The cards are the game. This approach maximises variety but creates problems:
- Balance becomes exponentially harder as the card pool grows
- The barrier to entry rises with each new set
- Individual cards carry narrative and mechanical weight that creates attachment and resistance to balance changes
- Dominant cards define the meta in ways the designer can't predict

**System-based design** treats cards as components of a system. The cards are the game pieces; the rules are the game. This approach creates elegance but can feel abstract. Most successful TCGs/CCGs are hybrids: strong systemic rules (turn structure, resource system, phase order) with content-layer cards.

**Implication:** When balancing, look at the system first. A card that is broken might be a symptom of a phase rule or resource rule that creates the exploit, not just a bad card number. Fixing the system level often neutralises multiple broken cards simultaneously.

## A §6 — The Thesis Mechanism Statement

Every card game should be reducible to a single-sentence description of what the core decision is.

Examples:
- "How do I use my limited mana efficiently while responding to my opponent's board?"
- "How do I assemble my combo before my opponent reduces my resources to zero?"
- "How do I maximise the points value of cards I play while minimising what my opponent scores?"

Before designing anything, write this sentence. Every card, keyword, and rule should serve it. When a mechanic does not serve the thesis mechanism, it is noise. Cut it.

## A §7 — The Chance/Skill Spectrum

Every card game occupies a position on the spectrum from pure chance (War — flip the top card, higher card wins) to pure skill (abstract chess-like games with no randomness). Neither extreme is the design target for a TCG/CCG.

**Why some randomness is necessary:**
- Variance makes outcomes feel meaningful — winning a close game through good decisions feels better than winning a solved game where the better player always wins
- Randomness creates replayability — the same deck plays differently each game
- Randomness levels the playing field between new and experienced players enough to sustain a casual audience
- Hidden information (the opponent's hand) is a form of randomness that rewards skill (reading the opponent)

**Why too much randomness is destructive:**
- Games decided before meaningful decisions arise are not games (see A §1)
- Players who lose to luck rather than skill feel cheated, not challenged
- Dominant strategies that rely on drawing specific cards make deck construction less meaningful

**The design target:** Randomness should create variety and tension; skill should determine outcomes more than 60–65% of the time at equivalent player levels. This means: a skilled player should beat a less skilled player most of the time, but not always. The minority loss cases keep the game accessible to less skilled players.

**Practical applications:**
- Mulligan rules reduce the impact of bad opening draws (pure luck) without eliminating draw variance entirely
- Higher deck minimum card counts reduce the probability of drawing a specific card (more variance) but increase consistency of deck strategies (more skill expression in deck construction)
- Cards that let you search your deck (tutors) increase skill expression by reducing draw variance — but must be costed highly or they remove too much variance

## A §8 — Inaction as a Valid Game State

Passing, holding cards, and deliberately doing nothing are game states that must be designed for, not around.

**Why inaction is valuable:**
- The decision not to play can be the optimal play — waiting for the opponent to overcommit before responding
- Passing is only meaningful if the alternative (playing a card) has real costs — tempo, card advantage, information leakage
- If passing is never correct, the game has degenerated into "always play your best card each turn," which reduces strategic depth

**Design requirements for inaction:**
- Passing must not give the opponent a cost-free benefit. If passing allows the opponent to act twice, that is a first-turn advantage problem (see C §2.1), not an inaction design.
- Some keywords (trap cards, instant-speed effects) should require holding a card until the right moment. These cards are only valuable if the player chooses correctly when to deploy them.
- Hand size limits create a passive pressure on inaction: players cannot hold indefinitely, which makes the timing of deployment a meaningful decision.

## A §9 — Player Agency vs Designer Control

The designer controls what is possible in the game. The player controls what actually happens. When the designer overspecifies outcomes (one dominant strategy, forced optimal play, no real choices), they are taking agency from the player.

**Agency as design goal:** The player should feel their decisions shaped the game's outcome. This does not mean the player always wins. It means the player can trace the causal chain from their choices to the result.

**Designer control as safety net:** The designer's control prevents degenerate states — infinite loops, guaranteed wins from a coin flip, one-card win conditions. This control is necessary. But it should be applied as constraints on the extreme ends of possibility, not as direction toward a single optimal path.

**The agency audit question:** For any rule or card effect, ask: does this create a choice for the player, or does it remove one? Rules that create choices (at your turn, you may X or Y) are agency-building. Rules that remove choices (you must X if Z is true) are agency-restricting. Both are necessary, but the balance should lean toward creation.

## A §10 — Core Fantasy and Emotional Design Target

Every card game delivers a core fantasy — a feeling the player is pursuing, not just a mechanical goal. Identifying the core fantasy before designing any mechanics is as important as the thesis mechanism (A §6), and complements it.

**What a core fantasy is:** The emotional experience the player wants to have. Not "win the game" — everyone wants to win — but the feeling of the winning. "Summoning an unstoppable creature that crushes everything" is a core fantasy. "Outmaneuvering a smarter-seeming opponent through preparation" is a core fantasy. "Building an elegant engine that runs itself" is a core fantasy.

**Common card game core fantasies:**
- Power fantasy: playing the biggest, most spectacular effects on the table
- Mastery fantasy: knowing something the opponent does not and using it decisively
- Builder fantasy: constructing a self-sustaining system that grows in power
- Survivor fantasy: being reduced to a desperate position and fighting back to win
- Tactician fantasy: making the correct sequence of decisions under pressure
- Collector fantasy: owning and completing a set of beautiful, rare objects

**Why it matters for design:** Every mechanic, keyword, and card should serve the core fantasy. A game with a power fantasy at its core should have cards that feel spectacular to play. A game with a mastery fantasy at its core should have information asymmetry, bluffing, and rewards for knowing the meta. A game that loses track of its core fantasy produces mechanics that are technically correct but emotionally flat.

**Design pillar crosscheck:** The core fantasy should map onto at least one design pillar (G §15). If it does not, the pillars do not capture the game's identity accurately.

## A §11 — The Revision Framework

When improving a design — whether a single card, a mechanic, or a full set — apply this revision framework in order. Do not jump to cutting or redesigning before checking whether the problem is a wording issue or a numbers issue.

**1. Keep what works.** Before touching anything, identify what is functioning correctly. Changes cascade; a change to a working element to fix a nearby broken one is a common mistake.

**2. Cut what only sounds clever.** Mechanics that are interesting to describe but generate no interesting decisions should be removed. If the best thing about a card is its concept and not its gameplay, cut it.

**3. Simplify unclear systems.** When a rule requires more than two sentences to explain or regularly causes disputes, the system needs simplification — not clarification. Adding more text to a complex rule makes it more complex. Redesign the underlying mechanic.

**4. Strengthen weak identity.** A faction, archetype, or card that could belong to any part of the game without changing anything has no identity. Give it something exclusive — a keyword, a play pattern, a strategic role — that only it does.

**5. Reduce unnecessary bookkeeping.** Any mechanic that requires the player to track more than two numbers simultaneously is a candidate for simplification. Counters, tokens, and trackers are acceptable; multiple simultaneous trackers per card are a design problem.

**6. Improve card wording.** After any mechanical change, re-read the card text as a new player. Rewrite anything that requires context to understand.

**7. Patch exploits.** Address specific broken interactions identified in playtesting. Prefer targeted patches (cost change, keyword scope limit, copy limit) over broad rule changes.

**8. Protect future expansion space.** Before finalising any mechanic, ask: does this close off design space that future expansions will need? A mechanic that exhausts its design space in the first set has nowhere to grow.

**9. Preserve the game's soul.** Identify what makes the game distinctive and make sure no revision removes it. A game that has been revised into safety and efficiency but lost its character has failed.

## A §12 — Operating Modes: Slime Mould and Ant Colony

Two complementary cognitive modes for card game design work. Neither is always correct. Switch between them based on the task.

**Slime Mould Mode — for rules, systems, and mechanical structure:**

Spread through the design space without committing to a path. Test every route. When a path produces a dead end (broken mechanic, degenerate state, unfun loop), abandon it and find another route. When a path works, reinforce it. Connect isolated working ideas into a stronger connected system.

In slime mould mode, look for:
- Mechanical bottlenecks (one resource, card, or rule that everything depends on too heavily)
- Repeated friction points (rules that cause disputes every session)
- Overcomplicated rules (any rule requiring a reference card to apply)
- Dead cards (cards no playtest group has ever used or considered)
- Dominant strategies (paths that make all others suboptimal)
- Unclear incentives (situations where the correct play is not apparent)
- False choices (decisions that look meaningful but have an obvious correct answer)
- Unfun loops (game states that extend the game without adding to the experience)
- Exploits (interactions the design did not intend and cannot defend against)
- Hidden elegance (existing mechanics that could do more with minor adjustment)

**Ant Colony Mode — for worldbuilding, factions, card pools, player experience, and product design:**

Dispatch specialist sub-agents to investigate different domains in parallel. Each agent reports findings independently before consolidation. Prevents tunnel vision; surfaces problems that systems-focused thinking misses.

Sub-agents and their mandates:
- **Rules clarity agent:** Is every rule unambiguous? Test every card against a new player reading it cold.
- **Balance agent:** Is any card, faction, or strategy obviously dominant or obviously useless?
- **Faction identity agent:** Does each faction feel genuinely different? Could any faction's cards be in a different faction without changing anything?
- **Card wording agent:** Is every card's text box using consistent terminology? Are all keywords in the glossary?
- **New player experience agent:** Can a first-session player have fun? Does the tutorial work? Does the starter deck?
- **Competitive play agent:** Is the meta healthy? Is there more than one viable strategy at the top level?
- **Casual fun agent:** Is the game enjoyable when not optimised? Does it produce memorable moments?
- **Expansion design agent:** Does the current set leave room for future design? What can the next set add?
- **Art direction agent:** Is the visual language consistent? Does the art communicate faction identity?
- **Lore and setting agent:** Is the world coherent? Do the flavour texts tell a consistent story?
- **Economy and rarity agent:** Is the rarity distribution appropriate? Are competitive cards accessible?
- **Draft format agent:** Can this set be drafted? Are commons interesting enough to build around?
- **Edge case hunter:** What are the five most unusual card interactions in the current pool? Do they all resolve correctly?
- **Layout and UX agent:** Is the card information hierarchy correct? Can the critical numbers be read at a glance?
- **Playtester simulation agent:** Simulate a game as each player archetype. What does each experience? What do they enjoy? What frustrates them?

After all agents report, consolidate findings into one prioritised list. Fix critical problems (broken mechanics, rules failures) first. Address identity and experience problems second. Improve refinements third.
