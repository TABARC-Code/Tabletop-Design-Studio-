# Reference S: Deck Builder Design and Format Operations

## S §1 — Deck Builder Design vs TCG/CCG Design: The Key Differences

Deck builders (Slay the Spire, Monster Train, Inscryption, Library of Ruina) share DNA with TCGs/CCGs but operate under fundamentally different constraints. Most balance and design doctrine in other modules applies to TCGs/CCGs where players build their decks before play. Deck builders break several of those assumptions.

**What deck builders change:**

**No pre-built decks:** The deck is assembled during play, not before it. The player cannot guarantee which cards they will have access to in any given run. Balance must account for both the worst realistic deck a player can end up with and the best.

**Resource pools are typically fixed per turn, not growing:** Where CCGs use growing mana pools (1 per turn to cap 10), most deck builders give the player a fixed resource budget each turn (e.g., 3 energy per turn for the entire run). Cards must be balanced around the starting resource pool, not a late-game maximum. Special effects that increase the resource budget are significant upgrades.

**No minimum deck size enforcement:** Because the player builds the deck over a run and cannot control exactly what cards appear, deck size rules are impractical. Advanced play focuses on building the leanest possible deck — removing cards to increase the probability of drawing the desired strategy. Deck thinning (removing cards) is often available through shops or events with limited uses.

**Human vs AI, not human vs human:** Deck builder opponents are AI with fixed ability sets. This changes the balance calculus: strategies designed to "break the game" in favour of the player are acceptable because the AI also has unfair-seeming abilities at higher difficulty levels. The arms race between player and AI is part of the experience.

**Stat inflation is acceptable within a run:** Where TCG/CCG low-number design prohibits stat inflation, deck builders can allow a card to scale from 5 damage to 50 damage over a run through upgrades and synergies. The run ends; the inflation resets. This is a sanctioned design exception.

## S §2 — Deck Builder Card Picking and Variance

Card acquisition in deck builders is typically: choose one card from a randomly presented selection (after combat, at a shop, as an event reward). This creates a specific variance structure:

**Player agency within randomness:** The player does not control which cards appear, but chooses among what is offered. This is more skill-expressive than pure random draw (you cannot choose what you draw in a TCG) but less than full deck construction (you cannot select exactly what you want).

**Run strategy emerges from picks:** Because the available cards are random, optimal play is about reading the current run's card offerings and converging on the best achievable strategy given those offers. A player who commits early to a strategy that the subsequent card offers do not support will have a weak deck. Flexible early picks that work in multiple strategies, followed by commitment once a strategy becomes available, is generally correct.

**Card power must be evaluated contextually:** A card worth taking in one run context (you have three synergising cards already) may be wrong to take in another (no synergy available). Deck builder balance must consider cards at different synergy levels, not just in isolation.

## S §3 — Deck Builder Draw Mechanics

Deck builder draw rules differ significantly from TCG/CCG draw rules:

**Full hand refresh:** Many deck builders discard the player's entire hand at end of turn and draw a new hand (Slay the Spire). This means there is no "hand advantage" concept — every turn is a fresh draw. Card draw effects change how many cards are in the new hand.

**Deck-reshuffle instead of deck-out:** When a deck builder's draw pile is exhausted, the discard pile is reshuffled and becomes the new draw pile. This repeats indefinitely. There is no deck-out loss condition in most deck builders — the game continues until the boss is defeated or the player dies. Milling strategies do not apply.

**Energy-as-draw (resource-for-cards variant):** Some deck builders allow the player to sacrifice cards to increase available energy, effectively trading card access for action economy. This creates a unique tension absent from TCGs/CCGs.

## S §4 — Deck Builder Enemy Design Rules

Enemy design in deck builders has its own doctrine distinct from TCG/CCG balance:

**Never make enemies immune to a whole strategy:** If an enemy is completely immune to fire damage and the player has built a fire-focused deck, the player has no counterplay except to die. This is not difficulty — it is design failure. Enemies can have resistances (reduced damage from fire) or conditional immunities (immune to fire while their shield is up), but not blanket permanent immunity to an entire deck archetype.

**Telegraph enemy intentions:** Modern deck builders display what enemies will do on their next turn. This is not a difficulty concession — it is fundamental to the strategic layer. If the player cannot see that an enemy will deal 20 damage next turn, they cannot make a meaningful decision about whether to prioritise offence or defence. Hide enemy intentions only in specific events designed around uncertainty.

**Enemy power curve must match player power ceiling:** If enemies in the first 5 encounters do at most 10 damage per turn, then encounter 6 does 32 damage per turn, the player's defensive capabilities (designed around the 10-damage ceiling) are useless. Enemy scaling must be gradual and matched to the expected player power level at that point in the run.

**Progressive difficulty (ascension systems):** Unlockable higher difficulty modes that increase enemy stats, add enemy abilities, or modify game rules. These should not change which cards are viable for experienced players — they should require better execution of the same viable strategies. If difficulty scaling makes certain card archetypes non-viable, those archetypes were not sufficiently powerful to compete at the baseline.

## S §5 — Format Operations for Live TCG/CCGs

**The meta management cycle:** For a live TCG/CCG, meta management operates on a cycle approximately equal to the expansion release schedule:

1. New set releases → meta disrupted as new strategies emerge
2. Community exploration phase (1–4 weeks) → net decks emerge
3. Meta stabilisation → one or two dominant strategies identified
4. Design response → announced for next expansion or ban list update
5. New set releases → cycle repeats

**Ideal meta state:** At the stabilised point of each cycle, at least four distinct deck archetypes should be viable at competitive level. If fewer than four are viable, the meta is too solved. If no single strategy is clearly stronger than others, the meta is healthy but may feel solved to players who prefer clear best choices. Both extremes have player costs.

**Net deck management:** The existence of net decks is not a failure state — it is the natural result of a healthy competitive community analysing and optimising the game. The problem is not that net decks exist but that they become the only viable choice. If a net deck exists alongside other viable strategies, it is a competitive benchmark, not a meta failure.

**Friendly mode and meta health:** Maintaining a non-ranked casual mode where players can test experimental decks without rank consequences is essential for meta health. Players who can only test strategies in ranked play are disincentivised from experimentation, which slows meta evolution and reduces deck variety. The casual mode is where innovation happens.

## S §6 — Digital Client Operations: Market Survival

From the study of CCG market history, the operational requirements for a digital CCG to survive:

**Day one client stability:** Server failure on launch day is close to unrecoverable in this genre. Players who try a new game on launch day and cannot connect do not return in significant numbers. Load testing at multiples of expected player volume is not optional.

**Cross-platform support:** CCGs are natural mobile games. A PC-only CCG in the current market is voluntarily excluding its largest potential audience. Cross-platform play (PC players vs mobile players in the same match pool) expands matchmaking and reduces queue times. Platform exclusivity is a commercial and player experience mistake for this genre.

**Digital bridge for physical TCGs:** Physical TCGs with digital clients should allow some form of physical-to-digital card access. The Pokémon code card model (physical pack includes a code redeemable in the digital client for the same packs) bridges the two communities. This requires manufacturing integration but significantly expands the value proposition of physical products.

**Tabletop Simulator as prototype platform:** The game Tabletop Simulator provides a physics-simulated virtual tabletop that designers can use to prototype physical card games digitally before committing to printing. Cards can be created as image files, shared with remote playtesters, and updated instantly. This reduces the iteration cost of physical game prototyping significantly.

**Bot population policy:** Digital CCGs need players to function — matchmaking requires a sufficient population. In the early days before the player base builds, AI bots filling match queues help new players experience the game at intended pace. This policy requires transparency: players should be able to identify when they are playing against AI and when they are playing against a human.
