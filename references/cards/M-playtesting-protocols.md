# Reference M: Playtesting Protocols

## M §1 — Why Card Game Playtesting Is Different

Card game playtesting is harder than most game playtesting for specific reasons:

1. **The card pool is large.** Testing every card against every other card at every point in a game is impossible by brute force. Structured protocols are essential.
2. **Context dependency.** A card that is fine in isolation may be broken when three specific other cards are in the pool. Finding these combinations requires both targeted testing and emergent discovery.
3. **Player variance.** An aggressive tester will find balance problems a casual tester won't. The playtest group must include players who deliberately try to break the game.
4. **Meta emergence.** The dominant strategy is not always obvious from card text. It emerges from the interaction of many cards over many games. Early playtesting catches obvious problems; extended playtesting catches emergent meta dominance.

## M §2 — Playtest Phases

**Phase 1: Core rules testing (before card design)**
Test the bare rules structure with placeholder cards. Does the turn sequence work? Is the win condition reachable? Does the resource system pace the game correctly? Fix rules problems before designing cards.

**Phase 2: Base card set testing (first cards designed)**
Test 20–30 cards per faction. The goal is not to find broken combos yet; it is to confirm that the card anatomy, keyword system, and cost benchmarks work. Questions: Do the cards feel different from each other? Does every cost bracket feel useful? Does the rarity distribution make sense?

**Phase 3: Deck-building testing (enough cards to build intentional decks)**
Build archetype decks (aggro, control, midrange, combo) for each faction and test them against each other. Questions: Can each archetype win? Are any matchups completely one-sided? Is there a dominant archetype emerging?

**Phase 4: Full pool testing (complete base set)**
Test the full card pool. Deliberately try to find degenerate combos. Build the worst possible deck intentionally and test its win rate. Build the most powerful deck you can and measure how consistently it wins. Questions: Is there a dominant strategy? Are there cards that never see play? Are there cards that are in every deck?

**Phase 5: Extended meta testing (if time allows)**
Run 50+ games with a range of decks to identify meta patterns that only emerge over extended play. This phase often reveals the slow-creep dominance of a strategy that seemed fine in Phase 4 testing.

## M §3 — Directed Playtesting for Specific Problems

When a specific balance problem has been identified, directed testing is more efficient than general playtesting.

**Directed test setup:**
1. Identify the specific problem: "Faction A is winning 70% of its matches against Faction B in aggro vs control matchups"
2. Build the two specific decks that represent the problem
3. Run a minimum of 20 games with the problem decks, recording results
4. Test proposed fixes one at a time (changing cost, stats, or keywords of suspected problem cards)
5. Rerun the 20-game test for each fix
6. Select the fix that achieves the closest to 50% win rate without introducing new imbalances

**Never test multiple fixes simultaneously.** You will not know which fix resolved the problem.

## M §4 — Blind Testing Protocol

Blind testing is where players who did not help design the game try to learn and play it using only the rules document and cards.

**What blind testing reveals:**
- Rules that designers understand implicitly but have not written explicitly
- Keyword text that is ambiguous to someone without design context
- Onboarding problems (what new players find confusing)
- Rules arguments — any place players disagree about how a rule works is a rules writing failure

**Blind test process:**
1. Give testers the rules document and card set
2. Observe without intervening (unless a tester is about to give up entirely)
3. Note every question a tester asks
4. Note every rules dispute
5. Note every moment of confusion
6. After the session, the designer answers all questions — the answers become FAQ entries or rules rewrites

## M §5 — Persona-Based Playtesting

A playtest group should include players deliberately playing as each of the three core archetypes (H §1). This is especially important for finding balance problems that only emerge from competitive play styles.

**Spike tester mandate:** Try to find the most broken deck in the pool. Build and play every potentially degenerate combo. If you find something that wins 80%+ of its games reliably, report it. Do not soften the finding because you like the card.

**Johnny tester mandate:** Build decks that combine unusual cards and mechanics. Find interactions the designer didn't expect. Some of these will be positive surprises (emergent depth). Some will be negative (degenerate interactions). Report both.

**Timmy tester mandate:** Build decks around the most impressive, high-cost cards. Test whether the late-game big plays actually arrive. Test whether the game pace allows these cards to be meaningfully used before the game is decided.

## M §6 — Data Collection for Card Games

Track these metrics across playtests:

| Metric | What it tells you |
|--------|-------------------|
| Win rate by faction matchup | Faction balance problems |
| Win rate by deck archetype | Archetype viability |
| Average game length | Pacing issues (too fast = aggro dominant; too slow = game drags) |
| Cards that appear in 80%+ of decks | Mandatory cards (possible over-power) |
| Cards that appear in 0% of tested decks | Underpowered cards (need buff or removal) |
| Turn of decisive board state | Early dominance or late-game swing frequency |
| Win rate for first player vs second player | First-turn advantage severity |

**Minimum sample sizes:** Do not draw conclusions from fewer than 20 games for any matchup. 50+ games is a reliable sample for balance conclusions. For a full meta survey, 100+ games is the minimum.

## M §7 — Playtesting a Legacy/Refit Game

Playtesting an existing game being refitted has different goals than playtesting a new game.

**What to establish before testing begins:**
- Which cards are in scope for the refit (the full legacy pool, or only recent sets?)
- Which format(s) are being tested (Standard with rotation, Legacy with full pool)
- What the success criteria are (target win rates, target game length, target archetype variety)

**Testing priorities for a refit:**
1. Test whether the refitted rules resolve the problems that motivated the refit
2. Test whether the refitted rules create new problems (all rule changes have side effects)
3. Test whether beloved legacy decks/combos still work in the refitted environment
4. Test whether new player onboarding works with the updated rules document

**Legacy player involvement:** Include players who were deeply invested in the original game. They will find problems with the refit that new players will not. They will also sometimes be resistant to legitimate improvements — distinguish between "this change breaks something important" and "I don't like change."

## M §8 — Remote and Asynchronous Playtesting

Physical co-location is not always possible. Remote playtesting is viable but requires specific tooling and adjusted protocols.

**Tools for remote physical card game playtesting:**
- Tabletop Simulator: full physics simulation; card images uploaded as custom content; supports rule enforcement plugins; cross-platform; requires all testers to own the software
- Tabletopia: browser-based; lower technical barrier; less customisation than TTS
- Screentop.gg: rapid setup for prototypes; designed specifically for playtesting not finished games
- Video call with shared camera: lowest tech; works for small card counts; fails for complex board states

**Asynchronous remote playtesting:** One player takes their turn, records decisions (photograph + written note or recorded video), sends to the next player. Slow but allows testers across time zones. Only viable for Phase 1 and Phase 2 testing where turn counts are low. Not viable for full-pool meta testing.

**Remote protocol adjustments:**
- Shuffle must use a shared random seed or a designated shuffler to prevent both players accidentally shuffling differently
- Hidden information (hand) requires a trusted client or a third-party hand-tracking tool
- Rules disputes must be logged and resolved asynchronously by the designer rather than adjudicated in-session
- Session length should be reduced for remote play — attention degrades faster without physical presence; 90 minutes maximum per session

## M §9 — Session Structure and Debrief Protocol

**Optimal session structure:**
- Session length: 2–3 hours maximum for focused design playtesting; 90 minutes for remote
- Number of games: aim for 5–8 complete games per session at the base set stage; 3–4 for full-pool testing where games are longer
- Breaks: 10 minutes after every 60 minutes of play
- Session objective: one primary hypothesis per session; secondary observations welcome

**Between-game moments:** After each game and before the next, capture:
- Who won and why (player's own assessment)
- One thing that felt unfair or confusing
- One thing that worked well
- Any card or interaction that came up repeatedly

**Post-session debrief (30 minutes minimum):**
1. Go around the table: one thing that worked, one thing that didn't (no discussion yet — capture first)
2. Designer presents today's primary hypothesis: did the data support or challenge it?
3. Open discussion of the most significant moments from today's session
4. Designer proposes changes; testers flag unintended consequences
5. Set next session's primary hypothesis before the group disbands

**What not to do in debrief:** Do not explain design intent before hearing tester feedback. A tester who knows what you were trying to achieve will unconsciously filter their feedback to be more charitable. Hear the raw experience first.

## M §10 — Convention and Public Event Playtesting

Convention playtesting (running a demo table at a public event) is distinct from structured design playtesting. Its purpose is feedback on accessibility and first-impression experience, not balance data.

**Convention playtest objectives:**
- Does a new player understand the core loop within 10 minutes?
- What is the first moment of confusion?
- What is the first moment of genuine enjoyment?
- What question does every new player ask?

**Convention demo setup:**
- Prepare two matched decks that demonstrate the game's identity — these are not optimal decks, they are showcases
- The demo should be completable in 15–20 minutes maximum
- One designer or demonstrator runs every demo session, controlling pacing
- Use a prepared script for the first 5 minutes (introductory explanation) then let the game teach itself
- Capture every question asked; every question is a game design data point

**Selecting convention testers:** The ideal convention tester is someone with no prior knowledge of the game. The worst convention tester is someone who knows the designer or has read about the game in advance. Their feedback is contaminated by prior expectation.

## M §11 — Alpha Strike Detection

Alpha strike is the condition where a player can win the game before the opponent has had a meaningful turn. It is the worst play experience in card games, worse than losing to a stronger card collection, because the opponent never had a chance to play.

**Detection protocol:**
- In every Phase 3 session, track which player won and on which turn
- If either player wins before turn 4 in more than 25% of games, alpha strike is a likely problem
- Specifically test the fastest possible aggro deck against the slowest possible control deck; record the earliest win turn
- Test with second-player advantage mechanics in place (coin, extra draw) — if removing those mechanics causes the win turn to drop below 3, the advantage mechanic is load-bearing and must be preserved

**Alpha strike failure conditions:**
- Win on turn 1 or turn 2: critical failure; game is broken regardless of other features
- Win on turn 3 with consistency above 40%: major problem; requires phase rules or cost adjustments
- Win on turn 4 with consistency above 30%: moderate problem; may require tuning aggro cards down or adding defensive options

**Fix approaches in order of preference:**
1. Add a first-turn restriction (cannot attack on turn 1; or restricted card plays on turn 1)
2. Increase the cost of the fastest aggro enablers by 1
3. Add a second-player compensation mechanic
4. Add defensive options at common rarity that are viable against turn-1 aggression
5. Last resort: redesign the phase structure to delay attack windows

## M §12 — Full Playtest Persona Library

M §5 covers the three core archetypes (Creative, Power, Competitor). A complete playtest group should also include:

**Kitchen-table casual:** Plays with friends at home; rarely reads strategy content; deck is built from what they own or what looks cool; will not tolerate rules that require a reference sheet to play; loses interest if a game feels mean-spirited. Tests: is the game accessible without meta knowledge? Is it still fun when not optimised?

**Rules lawyer:** Reads every word of the rulebook; finds edge cases; will play within the rules in technically correct but thematically uncomfortable ways; challenges ambiguity. Tests: are there rules gaps? Can the rules be exploited by a player determined to find the literal interpretation? Is every keyword defined?

**Draft player:** Evaluates cards differently in limited (draft/sealed) formats than in constructed; cares about individual card power rather than synergy; values flexibility and playability at common rarity. Tests: can the game support a draft format? Are commons interesting enough to build around? Does every faction have a draft-viable common card?

**Lore-focused player:** Reads every flavour text entry; notices when mechanical identity and thematic identity conflict; builds decks around favourite characters or factions regardless of competitive viability; will notice continuity errors. Tests: is the flavour text consistent? Do the mechanics feel like they belong in the world? Are there cards that feel thematically wrong?

**Accessibility-focused player:** May have visual, cognitive, or motor impairments; needs cards to be readable at small print sizes; needs rules that do not rely on precise card orientation; benefits from colour-plus-symbol (not colour alone) faction differentiation. Tests: does the card design pass O §4 accessibility standards? Can the game be played with any physical accessibility modification needed?

**New player (first session):** Has never seen the game; using the starter deck and rulebook only; will make play mistakes; gets frustrated quickly if rules are unclear or if they cannot affect the game state. Tests: does the rulebook explain the win condition within the first page? Can a first session new player have a meaningful turn by turn 2? Does the starter deck produce at least one memorable moment per game?

**Combo assembler:** Specifically trying to find and execute the most powerful card combination in the pool; will sacrifice board presence and tempo to assemble it; not interested in the game being fun as long as the combo works. Tests: what is the most powerful combination currently in the pool? At what turn can it be executed? What does it cost to stop it?

**Control purist:** Will not attack unless forced to; runs almost exclusively answer cards; wins by attrition and card advantage; loses patience with games that do not allow reactive play. Tests: is there a viable control strategy? Do answer cards exist at sufficient cost-efficiency? Does the game allow reactive play without committing to a board presence?

**The variance hunter:** Builds random or near-random decks; tests whether the game has a floor of fun regardless of deck quality; interested in unusual card interactions nobody designed intentionally. Tests: what happens when the game runs on weak draws? Are there accidental interactions that produce surprising outcomes?

## M §13 — Structured Playtest Report Format

Every playtest session should produce a report covering these six areas, in this order:

**1. What worked**
Mechanics, cards, or interactions that functioned as designed and produced positive player experiences. Specific examples required — "the faction ability worked" is not a finding; "the faction ability triggered five times across three games and always produced a meaningful decision" is.

**2. What failed**
Mechanics, cards, or interactions that did not function as designed, produced negative player experiences, or required clarification mid-game. Again, specific examples required.

**3. What confused players**
Rules questions asked during the session; card text that was misread or misapplied; timing disputes; phase order confusion. Every confusion is a rules writing task.

**4. What dominated**
Any strategy, deck type, card, or card combination that won at a significantly higher rate than expected, was identified as must-answer by all players, or made other strategies feel unviable. Quantify where possible.

**5. What felt underpowered**
Cards that were drawn and immediately discarded as unplayable; strategies that had no realistic win path; card types or factions that never appeared in any winning position. If something never got played, it is a balance problem or a design identity problem.

**6. What needs the most attention before next session**
One to three items maximum. The single most important finding and the proposed response. The designer must commit to a change or a reason for no change before the next session begins.

**Report format rule:** Reports longer than one page are not being used. Keep findings specific, named, and actionable. A finding without a proposed response is a note, not a finding.
