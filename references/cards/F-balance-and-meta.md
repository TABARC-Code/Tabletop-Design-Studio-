# Reference F: Balance and Meta

## F §1 — The Baseline Power Curve

Every TCG/CCG needs a cost-to-power baseline. This is the reference point for all balance decisions.

**Standard benchmark (adjust for your number range):**
- 1-cost creature: 1/1 stats, no keywords, OR 1/2 with one minor keyword
- 2-cost creature: 2/2 stats, no keywords, OR 2/1 with one minor keyword, OR 1/3 with one minor keyword
- 3-cost creature: 3/3 benchmark. Any 3-cost card should aspire to this equivalence
- 4-cost creature: 4/4 benchmark, or smaller stats plus one meaningful keyword
- 5-cost creature: 5/5 benchmark, or smaller stats plus one strong keyword or effect

**The benchmark deviation rule:** Every card that deviates from its cost's benchmark must earn that deviation with a corresponding downside, condition, or complexity cost.
- Below benchmark stats → compensating keyword or effect
- Above benchmark stats → keyword weakness, conditional activation, faction lock, or higher rarity with copy limit

**Spell cost benchmarks:**
- A spell that deals X damage should cost approximately X/2 in mana (dealing 4 damage for 2 cost is fair; dealing 4 for 1 is broken)
- A spell that draws one card should cost 1–2 (the value of card draw is high; pure draw spells need elevated cost)
- A spell that removes one card from the field should cost 2–3 depending on conditions

**These benchmarks are not laws — they are calibration tools.** Use them to identify outliers in your card pool.

## F §2 — The Cost-Stat-Keyword Triangle

Every card is a three-way negotiation between cost, stats, and keywords/effects.

- Increase cost → can increase stats OR add keyword
- Add keyword → should decrease stats OR increase cost
- Decrease cost → must decrease stats AND remove or weaken keywords
- Increase stats above benchmark → must increase cost OR add weakness keyword

**Worked examples:**
- Aquatic Guardian (2-cost, 1/1): underpowered at benchmark. Solution: add "Tidal Bond — if other water creatures are on your side, gain +2/+2." Now the card is situationally strong without being generically efficient.
- Feral Imp (1-cost, 3/3): massively overstat for cost. Solution: add "Blind Rage — only attacks creature cards at random." Now it cannot be directed at the opponent directly; randomness is the downside.

## F §3 — Tempo and Value Balance

See D §3 for definitions of tempo and value. Balance implications:

**Tempo-breaking cards:** Cards that cost less than their tempo impact should be flagged immediately. A 1-cost spell that destroys a 5-cost creature is a tempo break of massive scale. These cards create "feel-bad" moments even if technically balanced by rare conditions.

**Value-breaking cards:** Cards that generate more cards in hand, more resources, or more board presence than their cost implies are value breaks. Pure card draw is the most common example.

**The draw-card problem:** Any card whose sole effect is drawing more cards is extremely dangerous. Card advantage is the game's primary resource. A 1-cost "draw 2" card gives the player an extra turn's worth of resources for half a turn's cost. Cards like this have historically been among the first to be banned in competitive formats.

**Rules for draw effects:**
- Pure draw (draw N cards, no conditions) → high rarity, high cost, or both
- Conditional draw (draw a card when X happens) → can be common; conditions are the cost
- Targeted draw (search deck for specific card) → very powerful; must cost at least 2 and have a narrow search condition
- Opponent draw (both players draw) → neutral effect; can be cheaper; used in control strategies

## F §4 — Combo Detection

A combo is a set of cards whose combined effect exceeds the sum of their individual effects. Some combos are desirable (creating the "Johnny" experience of discovery). Degenerate combos are not.

**Degenerate combo checklist:**
- [ ] Can the combo be assembled by turn 4 or earlier without exceptional luck?
- [ ] Does the combo result in an instant win, or near-instant win (opponent has no meaningful response window)?
- [ ] Does the combo require an answer that costs significantly more to assemble than the combo itself?
- [ ] Does the combo use only common or uncommon cards (high deck availability)?
- [ ] Is the counter to the combo limited to a single narrow card or strategy?

If three or more of these are true, the combo is degenerate and must be addressed before launch.

**Addressing degenerate combos:**
1. Raise the rarity of one combo piece (limits availability)
2. Raise the cost of one combo piece by 1 (delays by one turn)
3. Add a conditional clause to one piece (assembly now requires meeting a condition)
4. Add a counter-keyword or counter-card to the pool
5. As a last resort: restrict the combo piece to 1 copy per deck

**Never remove the combo entirely** if it has become a fan favourite strategy. Restriction or costing adjustment preserves the strategy while making it non-dominant.

## F §5 — Hard Counter Design

A hard counter is a card that completely negates a strategy or card type.

Hard counters are necessary. Without them, dominant strategies become unbreakable. But hard counters have costs:
- They create narrow deck-building obligations (players must run the counter or lose to the strategy)
- They reduce strategic variety (if counter X is mandatory, all decks carry counter X)
- They feel unrewarding to play (you won because you had the counter, not because you played well)

**Hard counter design rules:**
- Hard counters should require timing and setup, not just "play this card and win"
- Prefer soft counters (cards that disadvantage a strategy) over hard counters (cards that nullify it) where possible
- If a hard counter is necessary, it should cost resources proportional to the power of what it counters
- Hard counters should be rare enough that they're not mandatory in every deck

## F §6 — Dominant Strategy Identification

A strategy is dominant when:
- It wins at a rate above 60% against the full field of viable strategies
- It creates a binary meta (run the strategy or run the counter)
- It discourages variety by making all other strategies statistically suboptimal
- Player perception is that not running it is a handicap

**Identifying dominant strategies:**
- Track win rates across a sample of at least 50 games per matchup pairing
- Identify which deck types are disappearing from play (sign that something has driven them out)
- Monitor community feedback — players identify dominant strategies faster than designers

**Response options in order of preference:**
1. Introduce counter-cards in the next expansion (preserves the strategy; adds counterplay)
2. Raise the rarity of a key enabler (reduces availability; slows the strategy)
3. Increase the cost of a key enabler by 1 (delays the strategy by one turn)
4. Restrict the enabler to 1 copy per deck
5. Emergency ban (last resort; damages trust; should come with an explanation)

## F §7 — Banning Cards

Banning a card removes it from legal play in one or more formats. It is a last resort.

**When to ban:**
- The card makes the game genuinely unplayable for a significant portion of the playerbase
- No other intervention short of a ban can address the problem before the next expansion release
- The card is creating matches that are decided before meaningful interaction occurs

**What to avoid when banning:**
- Never ban without a public explanation of why
- Never ban reactively to player complaints without data
- Never ban a card that is popular but not dominant
- Never ban a card that can be addressed by other means

**Restricted list vs banned list:**
- Restricted: card is legal at 1 copy per deck (weakens the strategy without removing it)
- Banned: card is not legal in a specific format
- These can coexist — a card banned in Standard may be restricted in Legacy

**Communication:** When banning or restricting, acknowledge the community's investment in the card. Explain the data behind the decision. Provide advance notice of at least two weeks for competitive players.

## F §8 — Power Creep Prevention

Power creep is the gradual inflation of card stats and effects across successive sets, making older cards obsolete.

**Causes:**
- Designers unconsciously making new cards slightly better than old ones to justify the new set
- Player expectation that new cards should be "upgrades"
- Competitive pressure from players who have older cards becoming unviable

**Prevention:**
- Design new cards around utility, not raw power. A card with a unique effect remains relevant; a card with higher stats becomes obsolete when a still-higher-stat card arrives
- Track the benchmark curve with every set. If new commons are exceeding the benchmark, the curve is inflating
- Rotating formats: remove old sets from Standard play, preventing the oldest cards from competing with the newest
- Errata old cards upward: occasionally reprinting old cards with slight improvements preserves their viability (controversial; use sparingly)

## F §9 — Patch Cycle Doctrine (Digital CCGs)

Digital CCGs have the ability to patch cards between sets. This is a double-edged tool.

**Patch best practices:**
- Minor cost adjustments (±1) are low-risk patches; announce in advance
- Stat changes (±1 on attack or health) are moderate-risk; require testing
- Effect text changes are high-risk; may require compensatory refunds to players who own the card
- Never patch more than 5–10 cards at once; broad patches destabilise the meta and reduce player confidence
- Never patch a card without a public explanation

**Patch cycles and competitive play:** If patches occur during a competitive season, the competitive schedule should include a mandatory adjustment period after any significant patch before the next tournament.

## F §10 — Deck Builder Balance (Non-Collectible)

Standalone deck builders (Dominion-style; roguelike deck builders) have different balance challenges:

- There is no secondary market, so power doesn't need to be gatekept behind rarity
- Cards are acquired and upgraded during play, not built beforehand
- The balance question shifts from "is this card too powerful at its cost" to "is this card always picked or never picked"
- Cards that are always selected dominate the strategic space; cards that are never selected waste design space
- Aim for every card to be the best choice in some configuration of the current game state

## F §11 — Cost-Stat Ratio Rules (Exact)

For creature cards with attack and defence stats, the starting benchmark for a 1-cost card with no keywords is one of three ratios: 1/1, 2/1, or 1/2. Any 1-cost card with higher combined stats than 3 total without a compensating keyword or downside is broken. The cost-stat relationship scales linearly: a 3-cost creature should sit near 3/3 as a benchmark. Deviation above benchmark requires justification; deviation below benchmark requires a keyword payoff.

**For fixed-turn short games (e.g. 6-turn formats like Marvel Snap):** The benchmark loosens because the game ends before compounding stat advantages can be fully exploited. A 1-cost card might legitimately have 3/4 stats if the design requires high individual card impact. This is an explicit exception, not a licence for general stat inflation.

**Spell cost rule (from source):** A spell that deals numerical damage should cost approximately damage divided by 2. 4 damage for 2 mana is fair. 4 damage for 1 mana is broken. A 2-cost spell that blocks the next damage source is fair because timing skill is the cost. The more a spell impacts the board state as a whole, the higher the resource cost must be.

**Reactive cards:** Cards that respond to opponent actions (traps, instant-speed spells) are often free or very low cost because they require timing investment and are single-use. Single-use nature is a balancing factor in itself — it can justify higher impact at lower cost than a persistent effect of equivalent power.

## F §12 — Balancing Through Timing and Investment

A strategy's investment cost must be proportional to its impact and resistance to countering. This is the investment-impact-counterability triangle:

**High investment + high impact + hard to counter = broken.** A classic broken combo example: assembled by turn 4 using only commons and uncommons, produces a continuously scaling creature that requires multiple specific cards to stop, and those counter cards require more investment than the combo itself.

**High investment + high impact + easy to counter = acceptable risk.** The opponent can stop it, but when it works it is rewarding. This is the Johnny target: combos that feel spectacular when executed and can be disrupted by a skilled opponent.

**Low investment + low impact = filler.** Not broken, not interesting. Avoid.

**High investment + low impact = trap card.** Players will never use it. Wastes design space.

When evaluating a strategy that players or testers declare overpowered, first establish: what are the counters, how much do the counters cost, and is the counter cost proportional to the combo assembly cost? If stopping the strategy requires more cards or more resources than building it, the strategy is broken regardless of what its individual cards look like in isolation.

## F §13 — Card Draw Variants (Full Taxonomy)

Card draw is the most powerful category of effect in any TCG/CCG. Full taxonomy of draw effects with design notes:

**Draw X cards (pure draw):** Always good, no downside. Should be rare or very expensive. Pot of Greed (draw 2 free) was the first Yu-Gi-Oh! ban.

**Draw X, discard Y:** Introduces a cost. Can be common if X=Y=1 (hand cycling). Broken if X > Y at low cost.

**Search deck for specific card type, put in hand:** Extremely powerful. Removes randomness entirely for the searched card. Must cost at least 2 and have a narrow search condition. The narrower the condition, the cheaper it can be.

**Both players draw X:** Neutral effect. Usually cheap. Useful for aggressive players who empty their hand faster than the opponent and need refill.

**Draw until you reach X cards in hand:** Variable draw. Often an end-of-turn effect. Power level depends on typical hand size; if players routinely have 2 cards at end of turn and this draws up to 5, that is effectively drawing 3.

**Automatic draw under condition (on play, on kill, on death):** Conditional; acceptable at common/uncommon. The condition is the cost.

**Put card on top of deck then draw:** Deck manipulation disguised as draw. Guarantees a specific draw next turn. Highly powerful; treat as targeted search for balance purposes.

**Draw whole hand at once (mulligan effect in-game):** Game-state reset. Can be free if hand sizes are small; should cost significantly if hand sizes are large.

**Design rule:** Any card whose sole purpose is generating card draw — no combat stats, no other effect — is among the first to become problematic as the card pool grows. Draw effects are fine as secondary effects on cards that do something else. Pure draw spells with no conditions are high-risk from the moment they are designed.

## F §14 — Randomness in Card Effects

Cards that produce random outcomes divide the player base between those who enjoy controlled chaos and those who find it unfair. Both preferences are valid; the design question is how much random-outcome card territory the game occupies.

**Random generation cards (generate a random spell/creature):** Upside: creates unpredictable plays that can swing games and generate memorable moments. Downside: skill-punishing — a worse player who generates a high-value random card beats a better player who does not. These cards feel unfair to lose to.

**Design rule:** If the floor of the random outcome (the worst possible result) is still useful, the card is acceptable. If the ceiling (the best possible result) can instantly win the game, the card is broken. Random generation cards should not have a ceiling that equals or exceeds the direct equivalent cost of a non-random card.

**Deck-thinning as anti-randomness:** Search effects and automatic draw triggers reduce the random variance of the draw. These are powerful because they guarantee outcomes. Balance them against the game's intended variance level — a game designed around bluffing and uncertainty is harmed by excessive search effects.

## F §15 — The Dominant Strategy Identification: Net Deck Problem

A net deck is a publicly known optimal deck, widely copied once identified. When a net deck exists, the meta bifurcates: players running the net deck, and players running explicit counters to it. Every other strategy becomes suboptimal.

**Signs a net deck has emerged:**
- One deck type wins more than 60% of competitive matches
- Community discussion focuses on countering that specific deck, not general strategy
- New players are advised to run the net deck or lose
- Expansion of creative deck building stagnates

**Design response priority (from source — buff over nerf):** It is always preferable to make weaker strategies better than to weaken the dominant one. Nerfing the dominant strategy removes something players have invested in and trained with. Buffing alternatives adds to the game rather than subtracting. Nerf only when buffing alternatives would make the entire field too powerful or when the dominant strategy is so entrenched that buffs cannot reach competitive viability.

## F §16 — The Hard Counter Problem (Gwent Weather Case Study)

Gwent v2 weather cards provide the canonical hard counter failure mode. Weather cards applied a board-wide effect that could only be removed by weather-specific counter cards. The counter cards had no other utility — running them meant dedicating deck space to a single counter with no flexibility. Result: every deck had to run weather counters or lose to weather, and weather became mandatory strategy in the Monster faction.

**The hard counter trap design rule:** A counter to a strategy should not be a card whose only function is countering that strategy. Counters should have independent utility so that running them is a genuine deck-building decision, not a tax. If the counter has no use outside its counter function, players will resent being forced to run it.

**Fixing hard counter dominance without removal:** When a strategy has become dominant through its hard counter properties, the fix is almost always to change how the hard counter works rather than removing the strategy. In Gwent's case: redesigning weather to affect fewer cards, reducing its board-wide scope, or making it conditional rather than blanket. The strategy survives; the dominance is reduced.

## F §17 — Threat, Answer, and Pressure

Tempo and value (F §3) describe the efficiency axis. Threat, answer, and pressure describe the interactive axis — how cards relate to each other across the table.

**Threat:** A card or board state that, if unanswered, will win the game or generate an insurmountable advantage within a defined number of turns. A 5-cost creature that will kill the opponent in three attacks is a threat. Every deck needs threats or it has no win condition.

**Answer:** A card or board state that neutralises a threat. Destroy spell, silence effect, blocker with higher defence than the threat's attack. A deck with only threats and no answers loses to any stabilising opponent. A deck with only answers and no threats draws the game out but never wins.

**Pressure:** A board state that forces the opponent to respond rather than act freely. A 2/2 creature that is not immediately threatening but costs the opponent resources to remove maintains pressure. Pressure is what makes aggro decks function — not individual threats but cumulative resource demands.

**Design application:** Every card in the game can be classified as primarily a threat, an answer, a pressure generator, or a utility card (enables or accelerates one of the other three). A healthy card pool contains all four categories. A set heavy in threats and light in answers creates aggro-dominated metas. A set heavy in answers and light in threats creates slow, frustrating games where neither player can win.

**The threat-answer ratio test:** For each faction, count how many of its cards are primarily threats vs primarily answers. A ratio of more than 3:1 in either direction is a design signal. Pure aggro factions can tolerate more threats; control factions can tolerate more answers; midrange factions need near-parity.

## F §18 — The Card Purpose Checklist

Before finalising any card, run this purpose audit. A card that fails more than two of these is a design problem, not a balance problem.

- **What deck wants this card?** If the answer is "no specific deck" or "any deck regardless of strategy," the card either occupies a mandatory utility slot (fine if intentional) or has no strategic identity (cut it or give it one).
- **What decision does it create for the player?** A card that has an obviously correct play in every context creates no decision. Decisions require trade-offs.
- **What decision does it create for the opponent?** Cards that force no response from the opponent generate no interaction. Interaction is what makes games feel like games.
- **Is it too efficient?** Would a player always include this regardless of strategy? If so, it is either mandatory (problematic unless it is an intentional design staple) or broken.
- **Is it too weak?** Will it never see play because a strictly better option always exists? Dead cards waste design space and dilute the pool.
- **Is it fun to draw?** A card that creates no excitement when drawn is not earning its place in the hand.
- **Is it miserable when repeated?** Facing the same card three or four times in one game can make winning feel irrelevant and losing feel unfair. Cards with repeatable effects must be designed with the worst-case repeat experience in mind.
- **Does it support a theme?** Mechanically fine cards that do not connect to any faction identity, strategy, or narrative purpose are design noise.
- **Does it create a new line of play?** The best cards open up plays the game has not seen before. If a card does exactly what ten other cards already do, it is probably not necessary.
- **Is the wording unambiguous?** Read the card as though you have never seen the game before. If it requires designer context to interpret correctly, rewrite it.
- **Does it break anything?** Test it against the five most powerful cards already in the pool. If any combination creates a degenerate state, the card is not ready.
