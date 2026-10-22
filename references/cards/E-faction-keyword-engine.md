# Reference E: Faction and Keyword Engine

## E §1 — Faction Design Foundations

A faction is a grouping of cards that share identity, playstyle, and mechanical vocabulary. Factions create:
- **Differentiation:** Each faction feels different to play
- **Collectability:** Players build loyalty to a faction and collect its cards
- **Balance scope:** Designers can iterate faction-by-faction
- **Deck construction rules:** How many factions can appear in one deck

**Faction identity stack — every faction needs all of these:**
1. **Thematic identity** — what this faction is in the world (warriors, mages, undead, machines)
2. **Strategic identity** — how this faction typically wins (aggro, control, value, combo)
3. **Keyword set** — two to five keywords exclusive or strongly associated with this faction
4. **Resource relationship** — does this faction generate, spend, or manipulate resources in a distinctive way?
5. **Signature weakness** — what is this faction bad at? A faction with no weaknesses creates dominant strategies

**Faction count:**
- 2 factions: easy to balance; limited strategic diversity
- 3–5 factions: sweet spot for most games; enough variety without unmanageable complexity
- 6+ factions: manageable only with strong keyword scoping and format design; Magic manages it because mana colour acts as a faction filter

**Adding a new faction after launch:**
This is one of the hardest design tasks in a card game. A new faction must:
- Have unique keywords not already in the game
- Have all its cards balanced against the entire existing card pool, not just other new cards
- Come with a complete card set at launch (not a partial faction)
- Be integrated into the existing resource system

Do not add factions reactively to fix meta problems. Factions are structural, not tactical responses.

## E §2 — Faction Asymmetry Design

The best faction designs create meaningful asymmetry — factions that play differently, not just factions with different skin on the same mechanics.

**Meaningful asymmetry examples:**
- One faction generates temporary advantages and must win fast (aggro)
- One faction has high individual card power but slow tempo (control)
- One faction has weak individual cards that become powerful through keyword stacking (synergy/combo)
- One faction has cards that punish opponent actions reactively (control-reaction)
- One faction controls the resource system itself (resource manipulation)

**Surface asymmetry to avoid:**
- Factions that differ only in the names of their keywords (both factions have "damage when played" but call it different things)
- Factions where the identity is expressed entirely in art and flavour text, not mechanics
- Factions where one is clearly better at everything

**Balance check:** For any two factions, identify the conditions under which each beats the other. If faction A has no realistic path to beating faction B, the asymmetry is broken.

## E §3 — Neutral Cards

Neutral cards belong to no faction and can be included in any deck.

**Design purposes of neutrals:**
- Fill strategic gaps that factions don't cover
- Provide tools for new players who don't have full faction collections
- Create cross-faction synergy without opening full multi-faction deckbuilding
- Act as balance levers — a neutral card that counters a dominant strategy can be introduced without disrupting faction identity

**Design rules for neutrals:**
- Neutral cards should be slightly weaker than faction cards at the same cost, representing the flexibility tax
- Neutral keywords should be simpler versions of faction keywords, not equivalents
- The number of neutrals should not exceed 15–20% of the total card pool or deck composition becomes too faction-agnostic

## E §4 — Keyword Creation

See B §4 for keyword anatomy rules. Additional faction-level considerations:

**Keyword scoping — three types:**
1. **Faction-exclusive keyword** — only appears on cards of one faction; creates identity; can be created for an expansion without worrying about cross-faction interaction
2. **Cross-faction keyword** — appears in multiple factions; creates interaction potential; requires full cross-pool testing
3. **Universal keyword** — appears on any card; used sparingly; must interact cleanly with everything

**Keyword ecosystem map:** Before finalising any keyword, draw a simple diagram of:
- Which existing keywords does this keyword interact with?
- Does any interaction create an infinite loop, guaranteed win, or unbreakable defensive state?
- Is there a counter-keyword already in the game, or does one need to be created?

**Keyword naming conventions:**
- Physical actions (Flying, Trample, Charge) — intuitive; describe what the card does
- Status effects (Poisoned, Frozen, Stunned) — intuitive; describe the card's state
- Faction identity keywords (names specific to the faction's lore) — require glossary; create setting texture
- Generic utility (First Strike, Last Breath, Regeneration) — intuitive; transferable across settings

## E §5 — Keyword Interaction Audit

Run this before any set releases:

**Step 1: Interaction matrix**
For each new keyword, test it against every existing keyword in these combinations:
- Keyword A on attacking card, Keyword B on defending card
- Keyword A and Keyword B both on the same card
- Keyword A triggered by Keyword B's effect
- Keyword A countering Keyword B

**Step 2: Degenerate state check**
Ask of each combination:
- Can this combination create an unkillable card?
- Can this combination create an infinite loop?
- Can this combination win the game automatically from a non-advantaged position?
- Can this combination be assembled by turn 4 or earlier?

If any answer is yes, either scope-limit one of the keywords, add an exception clause, or redesign.

**Step 3: Corner case documentation**
Document every interaction that required a decision during testing. This becomes the FAQ for the set.

**The Undying + Last Breath problem:**
Classic example of unresolved keyword interaction creating a degenerate state. Two keywords that both trigger on death, where the combined effect is immortality. Resolution: add a clause to at least one keyword specifying what happens when both trigger on the same card simultaneously. The rule should be: when two death-trigger keywords apply to the same card simultaneously, the designer must specify priority order explicitly in the rulebook.

## E §6 — Faction Progression and Expansion

When a faction receives new cards in an expansion:

- New cards must reinforce or evolve the faction's identity, not contradict it
- New keywords introduced for a faction in an expansion should connect to the faction's existing keyword vocabulary
- Avoid power scaling: a new card that makes all previous faction cards obsolete is power creep
- Expansions should sometimes add cards that strengthen underused strategies within a faction, not just amplify already-dominant ones

**Faction "codex creep" (power scaling by faction):**
When successive expansions make a faction progressively stronger, it becomes the dominant choice and player loyalty to weaker factions erodes. Prevention: balance expansion planning across all active factions, not just the most popular one.

## E §7 — Exclusive Hero and Leader Powers

Some CCGs give each faction or deck a power that operates outside the normal card mechanics. These are abilities tied to the faction leader or hero that can be used independently of the cards in play. Design considerations:

**What exclusive powers do:** They provide a baseline strategic option every turn that is not dependent on drawing specific cards. This means even if a player draws poorly, they have something to do. Hearthstone's hero powers (1 or 2 mana, activated once per turn) provide a consistent floor of strategic action. Gwent's leader abilities provide high-impact plays with limited uses, creating an additional resource the player manages alongside their hand.

**Balance approach:** Exclusive powers are balanced against each other (each faction's power should be roughly equivalent in overall utility) and against the cards in the game (the power should not make certain cards mandatory or obsolete). They cannot be changed by most card effects unless deliberately designed to be alterable — this design space (changing your hero power via a card) is an expansion opportunity that must be introduced carefully.

**When to add:** The decision to include exclusive powers must be made during the design phase. Post-launch introduction of an exclusive power system requires every faction to receive one simultaneously, all balanced against the entire existing card pool. This is a major design undertaking and the reason it is almost never done after launch.

**Planeswalkers and VMax as in-card exclusive powers:** Some games implement exclusive mechanics at the individual card level rather than the faction level. Planeswalkers (Magic) have their own loyalty resource and three abilities, making them function differently from every other card type. Pokémon's V Max cards have higher stats and a premium ability at the cost of giving the opponent more prize cards when defeated. These in-card exclusive mechanics must have their own rules section and interact with the keyword glossary. Introducing them mid-game is possible but requires a dedicated rules update.

## E §8 — Adding a New Faction: Why It Is Harder Than It Looks

Adding a faction to an existing TCG/CCG is one of the highest-risk design decisions possible. It looks like a content decision (write the cards) but is actually a systemic one.

**What a new faction requires:**
- At least one card at every rarity tier in the game (not optional — an incomplete faction is a competitive disadvantage)
- At least two to four faction-exclusive keywords (otherwise the faction has no identity)
- All faction cards balanced against every card in the existing pool, not just other new cards
- A defined relationship with the neutral card pool
- A defined relationship with every other faction's keyword set for multi-faction formats

**Why keyword locking matters for faction expansion:** Gwent can add a faction (as it did with The Syndicate) because every faction's keywords are rigidly exclusive. The balance analysis for a new faction is bounded — it only needs to test its cards against neutral cards and the existing faction cards in the formats where mixing is allowed. Magic cannot trivially add a new mana colour because every card in the game is potentially combinable with every other card, and a new colour creates exponential new combinations to balance.

**Design principle:** If you anticipate needing to add factions over the life of your game, design the faction system with hard keyword scoping from the start. Open faction systems trade early design flexibility for permanent difficulty in expansion.
