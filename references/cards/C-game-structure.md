# Reference C: Game Structure

## C §1 — The Play Area

Every TCG/CCG requires a defined play space. Establish this before any card is designed. Layout affects card legibility, game pace, and rules complexity.

**Mandatory zones:**
- **Deck zone** — where the draw pile sits; position affects draw speed and visual clarity
- **Hand** — held by player; partially visible (top edges) in some physical designs
- **Play field** — where cards are placed and remain active; must have defined maximum occupancy per side
- **Graveyard/discard pile** — cards removed from play; physically separate from deck; must be accessible for effects that reference it
- **Remove-from-game zone** — for effects that exile/banish cards; distinguished from graveyard

**Optional zones:**
- **Resource zone** — if resource cards are physical (land, energy)
- **Special zone** — for cards with unique placement rules (e.g. a card that sits between both fields)
- **Limbo/exile** — cards removed more permanently than the graveyard

**Design rule:** The maximum number of cards in the field at any time per player must be stated in the rules. Uncapped field sizes create visual chaos, turn-length problems, and unanticipated scaling issues.

## C §2 — Turn Structure and Phases

The standard minimal turn:
1. Draw phase — player draws card(s)
2. Resource phase — if applicable, player plays or generates resource
3. Main phase — player plays cards
4. Attack phase — if applicable, creatures attack
5. End phase — hand size check, discard if over limit, effects that trigger at end-of-turn resolve

**Phase design rules:**
- Name every phase explicitly in the rulebook; do not rely on implied ordering
- Define which card types can be played in which phases
- Define whether an opponent can respond during the active player's phases
- Define what happens when effects trigger simultaneously (priority stack or declared resolution order)

**First-turn advantage:**
This is one of the most-debated problems in card game design. The player who goes first controls the initial tempo. Solutions used across successful games:
- Second player receives compensation (extra card, one-time resource bonus, a "coin" card)
- First player cannot attack on turn 1
- First player draws one fewer card
- Certain card types cannot be played on turn 1
- Both players play their main phase simultaneously (rare; requires specific design architecture)

No perfect solution exists. Pick one approach and playtest its sufficiency. The goal is that the average win rate for going first is no more than 52–55% at the competitive level.

## C §3 — Win Conditions

**Direct life point damage (most common):** Each player begins with X life points. Reduce opponent to zero to win. Simple, intuitive, well-understood by players. Risk: games can be decided before interesting decisions arise if aggro strategies win too fast.

**Point accumulation:** Cards contribute points to a running total. Player with the most points at end of game (or when a trigger condition is met) wins. Good for designs that want to avoid "sudden death" finishes. Gwent uses this. Allows more strategic depth around when to commit cards.

**Alternative win conditions:** Specific card combos automatically win the game (e.g. Exodia). High risk. If the combo is achievable early, the game stops being about strategy and becomes about assembling the combo or disrupting it. Use sparingly and only when the assembly cost is prohibitive.

**Deck-out:** Player who cannot draw a card loses. Common secondary win condition. Creates a counter-strategy (milling). Design with care — if both players can mill and one is better at it, games devolve into mill races.

**Multiple simultaneous win conditions:** Possible but requires careful documentation. When a player can pursue life damage, combo, or mill, the game has genuine strategic branching. Requires the rules to clearly define which condition takes priority when multiple trigger on the same turn.

## C §4 — Deck Construction Rules

These must be defined before any card is printed:

**Minimum deck size:** Prevents optimal 5-card decks. Larger minimums increase randomness and strategic depth. 40–60 cards is the effective range. Below 20 creates a solved-feeling game; above 80 creates draw inconsistency that punishes strategy.

**Maximum deck size:** Not always required. Some games (Magic) have minimum but no maximum. Unlimited maximums allow defensive strategies that mill opponents while never running out.

**Copy limits per card:** Essential for balance. Common standard: maximum 2–4 copies of any one card except legendary/mythic (1 copy maximum). Games without copy limits devolve into "optimal 4-of-every-best-card" construction.

**Faction limits:** How many factions can a single deck draw from? Options:
- Single faction only (strict identity, clear design space)
- Dual faction (most popular; allows combo discovery, manageable)
- Open (any card from any faction; very high complexity; requires provisions/budget cap to control)

**Format-specific overrides:** Constructed formats may impose additional restrictions. Draft/sealed formats build decks from a limited pool; standard copy limits may not apply.

## C §5 — Hand Management Rules

**Starting hand size:** Typically 5–7 cards. Smaller starting hands create faster games with less strategic depth. Larger starting hands create slower games with more pre-game strategy.

**Mulligan rules:** Define what a player can do if their opening hand is unplayable. Options:
- Free mulligan (shuffle back, redraw, once)
- London mulligan (redraw full hand, put back N cards equal to number of mulligans taken)
- No mulligan (high-variance; suits some casual designs)

**Hand size limit:** Maximum cards a player may hold at end of turn. Forces discard decisions and prevents hoarding. Most games use 7–10. No hand limit creates card hoarding strategies; very low limits create resource anxiety.

**Draw consistency:** The probability of drawing a specific card in a given turn is a function of deck size and copies. With a 60-card deck and 4 copies of a card, the chance of drawing at least one in a 7-card opening hand is approximately 40%. This math should inform copy limit design.

## C §6 — Formats

Formats define which cards are legal and what rules apply. Format design is covered fully in J §4. The structural implications:

- Different formats may have different deck size minimums
- Different formats may have different copy limits
- Limited formats (draft, sealed) have their own deck-building rules
- Rotating formats require the base game rules to be independent of which cards are legal

## C §7 — Deck Size, Match Length, and Randomness

Deck size determines three things simultaneously: randomness level, match length, and barrier to entry.

**Deck size and randomness:** A 60-card deck with 4 copies of a strategy enabler gives approximately 40% chance of drawing it in the opening hand. A 12-card deck with 1 copy of the same card gives 58% chance. Smaller decks produce more consistent strategies and shorter, more deterministic games. This is a design choice with clear trade-offs — consistency reduces strategic depth.

**Deck size and match length:** Larger decks mean more cards can be played before either player exhausts their deck. A competitive match between skilled players who know their decks runs approximately 10 minutes for most major CCGs at 40–60 card sizes. Very small deck sizes (12 cards) produce 6-turn matches by design (Marvel Snap). If your game should produce 10-minute casual matches, design deck size accordingly. If you want longer strategic games, larger decks are required.

**Deck size and new player barrier:** A 40-card minimum is achievable for a new player with one starter deck and a few booster packs. A 60-card minimum requires significantly more collection depth. For new player acquisition, a smaller minimum deck size (even if competitive play trends toward larger) lowers the entry cost.

**The deck-out rule:** When a player cannot draw because their deck is empty, they lose. This prevents infinite-game scenarios and creates a secondary strategic axis (mill strategies, forcing opponent to draw). Design this rule deliberately — some games reshuffle the discard pile as a new deck instead of deck-out, which completely changes the strategic relationship with card draw.

## C §8 — Faction System: The Decision That Cannot Be Undone

Whether your game uses a faction system must be determined during the design phase and before any cards are manufactured. This is one of the few design decisions in TCG/CCG design that is effectively irreversible once the game is released.

**Why it cannot be undone after launch:** Adding a new faction requires creating a complete card set for every rarity tier in the game, all of which must be balanced against every existing card. In a game with rigidly faction-locked keywords (Gwent model), adding a faction is possible because the keyword design space is compartmentalised. In a game with free-form multi-faction deck building (Magic model), adding a faction at the colour identity level would require re-examining every possible combination with every existing card — effectively impossible at scale.

**Faction system options and their constraints:**
- No factions (neutral pool only): Simplest. Maximum deck variety. Harder to create distinct playstyles without faction-locked keywords.
- Hard faction lock (decks must be mono-faction): Clear identity, easiest to balance in isolation. Limits cross-faction strategies that many players enjoy.
- Dual faction limit: Most popular. Allows creative deck building while remaining manageable. Requires defining how many non-neutral faction cards can cross the limit.
- Open (any faction, budget/provision limit): Maximum variety. Requires a separate constraint system (provisions) to prevent the dominant faction's cards filling every deck.

**Deciding faction count:** The more factions, the more expansion content that must service every faction. A game with 6 factions requires every expansion to have cards for all 6 or some factions fall behind, which is a balance and community problem. Start with the minimum number of factions that produces your intended variety of strategies, not the maximum you can imagine.

## C §9 — Multiplayer and Commander-Style Structure

Standard TCG/CCG design assumes 1v1. Multiplayer card games require structural modifications that affect almost every design decision.

**Core multiplayer changes:**
- Turn order becomes a strategic resource — going last in a 4-player game means reacting to three other players' plays before taking a turn
- Threat assessment replaces direct targeting — players must evaluate relative threat of three opponents and manage political dynamics
- Card effects that target "the opponent" must be redefined (target player, target opponents, all opponents, or chosen opponent)
- Win conditions must account for multiple simultaneous opponents — last player standing or points accumulation both work; the "reduce to zero life" condition remains but with multiple targets

**Commander/singleton format structure:**
- 100-card decks, exactly 1 copy of each non-basic resource card
- A designated "commander" card (typically a specific creature) that begins outside the deck and can be played from a command zone
- Deck construction is partially defined by the commander's faction/colour identity — cards outside that identity cannot be included
- The commander can be replayed from the command zone if defeated, at increasing cost each time
- Multiplayer (4 players) is the standard format

**Design implications of commander:**
- Individual card power must be evaluated in the context of 1v3 not 1v1 — cards that are weak in 1v1 may be dominant in multiplayer
- Cards that specifically affect "each opponent" scale with player count and must be balanced accordingly
- Political effects (make deals, redirect attacks) become mechanically meaningful in multiplayer in ways they cannot be in 1v1

## C §10 — Cooperative and Team Formats

**2v2 (Partnership):** Two players share a win condition and play against two opponents sharing theirs. Each player has their own deck and takes their own turn. Partners may or may not be able to assist each other directly (share resources, protect each other's cards). Design must define: can partners communicate during play? Can they share resources or life points?

**Full cooperative:** All players vs AI-controlled opposition or puzzle state. Requires:
- AI opponent design (see Q §5)
- Defined win condition that all players contribute to
- Card design that enables player synergy (cards that benefit multiple friendly players)
- Defeat condition that feels like a joint failure, not one player's mistake

**Cooperative design challenge:** In cooperative games, one player often becomes dominant (quarterbacking — one player makes all decisions for the group). Prevent this by giving each player exclusive control over specific resources or decision domains. If one player's deck is meaningfully different from every other player's deck, quarterbacking is reduced because no single player has full information about all available options.

## C §11 — Points Scoring Systems

Life total reduction is the default win condition. Points scoring is an alternative that changes strategic behaviour significantly.

**Points scoring characteristics:**
- Games don't end suddenly — both players can see how the score is evolving
- Cards have scoring value independent of board state — a card played for its points is useful even if it is destroyed
- Late-game tension is different — chasing a specific score threshold creates different pressure than racing to reduce a life total
- Scores can be contested directly (steal points) or built independently (accumulate own points)

**When to use points scoring:**
- When you want games to feel complete rather than abruptly ended
- When you want players to value playing cards for their intrinsic value, not just for board advantage
- When the game's theme involves accumulation (exploration, construction, collecting) rather than conflict

**Points + life hybrid:** Some games run both simultaneously — points accumulate during play and life is tracked separately. The first player to reach a points threshold OR reduce the opponent to zero life wins. This creates two parallel win paths and strategic depth around which path to prioritise.

**Scoring zone design:** Points-based games often use dedicated scoring zones (separate from the main field) where played cards accumulate for scoring. This physical separation reinforces the strategic distinction between "playing for score" and "playing for board control."
