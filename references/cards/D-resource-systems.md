# Reference D: Resource Systems

## D §1 — Why Resource Systems Exist

Resource systems answer one question: how do you prevent a player from playing their entire hand on turn 1?

Without resource constraints, whoever draws the best cards first wins every game. Resource systems create pacing, strategic prioritisation, and meaningful decisions about what to play and when. They are the primary mechanical throttle on power expression.

Resource systems also create asymmetry between early-game and late-game cards, giving games a natural arc: low-cost cards dominate early; high-cost game-changing cards arrive late. This arc is what creates narrative tension within a match.

## D §2 — Resource System Types

### Auto-replenishing pool (Mana/Energy)
**How it works:** Each turn, the player's resource pool resets to a maximum that increases by 1 each turn (or by a fixed amount). Cards are played by spending from this pool.

**Characteristics:**
- Predictable tempo: both players know what the opponent can play each turn based on turn count
- Creates "tempo plays" — players must spend efficiently each turn or fall behind
- Deck building is shaped by the mana curve (how many cards at each cost bracket)
- Critics: reduces strategic depth around resource management because it's automatic
- Examples: Hearthstone (mana), most CCGs

**Design requirements when using this:**
- Define the maximum pool size (usually 10)
- Define whether unused resources carry over (almost never yes)
- Define whether certain card effects can increase or reduce the pool temporarily
- Mana curve must be designed into every expansion — too many high-cost cards means decks feel slow; too many low-cost cards means the late-game doesn't arrive

### Physical resource cards (Land/Energy)
**How it works:** Resource cards are part of the deck and must be drawn and played. A player who draws resource cards gains the ability to play higher-cost cards.

**Characteristics:**
- Higher variance: a player can be "mana screwed" (too few resource draws) or "mana flooded" (too many)
- Deck building is more complex: the ratio of resource cards to action cards is a genuine strategic decision
- More design space for resource cards themselves (dual-type resources, resources with additional effects)
- Examples: Magic (land cards), Pokémon (energy cards)

**Design requirements when using this:**
- Define how many resource cards can be played per turn (typically 1)
- Define whether resource cards have any effects beyond producing resources
- Define what happens to resource cards when their attached unit is defeated (Pokémon energy is discarded with the Pokémon; Magic land persists)
- Deck-building guidance for new players is essential — the optimal resource-to-action ratio should be communicated

### No-resource system
**How it works:** No explicit cost to play cards. All cards are free. Control is maintained through play volume limits (e.g. one card per turn).

**Characteristics:**
- Fastest to learn; lowest barrier to entry
- Strategy shifts entirely to which card to play when, not what can be afforded
- Card power design is more constrained — cannot use cost as a balance lever
- Every card must be independently balanced on its own utility
- Changing this system retroactively requires rebuilding every card in the game
- Example: Gwent (one card per turn; cards have provision costs for deckbuilding but not for playing)

**Design requirements when using this:**
- Define how many cards can be played per turn
- Define whether that limit can be exceeded by card effects (usually yes, carefully)
- Establish provision/budget limits for deck building to replace cost-based balance

### Sacrifice-based system
**How it works:** To play high-cost cards, the player must remove lower-cost cards from the field as tribute/sacrifice.

**Characteristics:**
- Creates interesting decision: is sacrificing Card A to summon Card B worth it?
- Creates aggressive counterplay: opponent can destroy cards the player is saving as sacrifices
- Scales naturally with level/tier systems
- Example: Yu-Gi-Oh! (sacrificing monsters to normal-summon high-level ones)

**Design requirements when using this:**
- Define the sacrifice-to-summon ratio at each tier (1 for level 5–6; 2 for level 7+)
- Define whether sacrificed cards provide any resources or effects when removed
- Define what "special summoning" means and how it differs from normal summoning

## D §3 — Tempo and Value

Two competing strategic axes in any resource system:

**Tempo:** Using your resources as efficiently as possible each turn to maintain board presence and apply constant pressure. Playing a 3-cost creature on turn 3 is good tempo. Playing nothing on turn 3 is a tempo loss.

**Value:** Getting more total utility from your cards than their cost implies. A 3-cost card that draws you two cards is high value. A 6-cost card that destroys two opponent cards is high value.

These axes are in tension. Tempo players must sometimes sacrifice value plays to maintain board control. Value players must sometimes accept tempo losses to set up high-value turns. Healthy game design ensures both axes are viable.

**Resource system implications:** Games with auto-replenishing pools favour tempo (every unspent resource is a loss). Games with physical resource cards create more value decisions (saving mana for reactive plays is possible). Games with no resource systems collapse tempo and value into turn sequencing only.

## D §4 — Resource as Faction Identity

Resource systems can reinforce faction design:

- Colour-locked resources (Magic mana colours) create faction identity at the resource level — a blue deck behaves differently from a red deck in how it generates and spends mana
- Energy types tied to Pokémon type create faction-adjacent costs
- In games without faction-locked resources, faction identity must be carried entirely by card effects and keywords

**Design rule:** If your game has factions, decide early whether resource acquisition varies by faction. Faction-neutral resources (Hearthstone mana) mean faction identity lives in the cards alone. Faction-specific resources (Magic lands) create double identity — the resource system expresses the faction, and so do the cards.

## D §5 — Resource System Change Doctrine

The resource system is foundational. It cannot be changed without rebuilding every card in the game.

If the resource system is wrong, fix it before manufacturing begins. After the first set is printed, the options are:
- Minor adjustments (change pool maximum from 10 to 12; add one new resource card type)
- A major format reset with a new edition (risky but sometimes necessary — see Gwent's full rebuild)

Never change the resource system because one deck is too strong. A deck exploiting the resource system is almost always exploiting a card design failure, not the resource system itself.

## D §6 — Advanced Resource Variants

**Carryover / Spell mana pools:** A secondary resource pool that only accepts unspent resources from a previous turn. Unspent mana from the main pool converts to a smaller carryover pool at turn end. This rewards reactive play — saving resources earns a small advantage — without allowing indefinite resource accumulation. Design consideration: the carryover pool must have a cap or players will stockpile indefinitely.

**Dual resource systems:** Games that run two simultaneous resources create deeper deck-building decisions (balance two cost types) and can express faction identity through resource ratios. Risk: dramatically increases new player complexity. Only add a second resource if the strategic decision it creates (balancing two pools) is more interesting than the complexity it adds. If both resources always run empty simultaneously, they are functionally one resource with extra steps.

**Combat-generated resources:** Defeating an opponent's card generates resources. Creates a positive feedback loop: winning fights gives more resources to play more cards to win more fights. This loop must be bounded — either the resource caps or there is a diminishing return mechanism — or the winning player snowballs uncontrollably. Combat resource generation rewards aggressive play styles and punishes passive ones; factor this into faction design.

**Resource denial strategies:** Cards that reduce, lock, or steal opponent resources. These are among the most frustrating effects in any card game if overdesigned, because denying someone's ability to play is denying them the experience of the game. Design rule: resource denial should slow an opponent, not stop them entirely. A card that locks all opponent resources for two turns removes that player from the game for two turns — this is rarely fun to play against and is almost always a design mistake. Prefer: cost-increasing effects (opponent's cards cost 1 more), resource reduction (opponent generates 1 less resource this turn), or temporary lock (opponent cannot use X resource type this turn only).

## D §7 — The Resource Cap Problem

When players reach the maximum resource pool every turn for multiple turns in a row, the resource system stops generating decisions. At maximum mana, the only constraint is card availability (hand size), not resource availability. The late game collapses into "play the most powerful card I can every turn."

**Solutions:**
- Variable-cost high-power cards: cards that can be paid at different costs for different effects (e.g. pay 5 for base effect, pay 8 for enhanced effect)
- Resource sink mechanics: ways to spend excess resources that generate value without playing cards (upgrading a card on field, activating a leader ability)
- Continuous resource investment: some cards require ongoing resource payment each turn to maintain their effect — idle resources are consumed by the field
- Set the pool maximum lower: if the game reaches interesting decisions at 7 mana but not at 10, cap the pool at 7

The resource cap problem is a design signal, not just a balance issue. If players have nothing interesting to spend resources on in the late game, the card pool does not have enough high-cost utility. Either the pool needs more late-game investment options or the cap needs to come down.
