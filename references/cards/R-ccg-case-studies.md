# Reference R: CCG Design Case Studies

A library of structural design decisions drawn from real CCGs. Use when designing a specific system to see how different games solved the same problem. Source identity suppression applies — no author names in outputs.

---

## R §1 — Hearthstone: Deliberate Simplification as Design Philosophy

Hearthstone's central design decision was to take physical TCG complexity and remove anything that slowed play or confused new players. This was not laziness — it was a deliberate product decision that created the most accessible competitive CCG of its era.

**Specific simplifications and their effects:**
- Auto-replenishing mana pool (1 per turn to cap 10): removed resource draw variance, made tempo planning predictable, allowed the game to focus player attention on card plays rather than resource management
- Turn timers: forced player decision-making speed, made mobile play viable, prevented analysis paralysis
- Fewer card phases per turn: reduced phase tracking cognitive load
- Asymmetric class system with fixed hero powers: every player always had a strategic option each turn regardless of hand quality

**What Hearthstone added that physical TCGs could not:** Animated boards with interactive elements; animated card attack sequences; reactive board elements for non-playing player. These made watching the game entertaining, which enabled streaming culture to accelerate the game's growth.

**Design lesson:** Simplification is not dumbing down. Reducing cognitive load in one area (resource management) frees player attention for strategic depth in another area (card play decisions). Every game should identify which areas of complexity are load-bearing (generate genuine decisions) versus incidental (just things to track).

---

## R §2 — Shadowverse: Evolution Points as a Second Resource

Shadowverse's evolution system creates a second strategic resource that operates on a different cadence from mana.

**Mechanical specifics:** Each player receives evolution points at match start. The first player receives 2 points; the second player receives 3 (second-player compensation built into the resource). Evolution points cannot be used until turn 4 (second player) or turn 5 (first player). Spending a point evolves a creature to a higher form with increased stats and sometimes changed properties.

**Design implications:**
- The limited point pool means every evolution is a high-stakes decision — wasting a point on the wrong creature or at the wrong time is a significant setback
- The different point allocation between first and second player is a structural second-player advantage that partially offsets first-turn tempo
- The turn threshold before evolution is available creates a guaranteed early-game phase where the mechanic does not exist, then a transition into a different strategic phase

**Design lesson for second-resource systems:** A second resource works when its timing and scope are different from the primary resource (so they are not just the same thing counted twice) and when the decision about how to spend it is genuinely difficult. If the correct evolution choice is always obvious, the system adds complexity without adding depth.

---

## R §3 — Gwent: Three-Round Structure and Card Advantage

Gwent's three-round match structure is one of the most distinctive structural designs in CCG history. It changes the relationship between card advantage and winning in ways that no other major CCG replicates.

**Structural mechanics:**
- A match is played over three rounds
- Each round ends when both players pass
- The player with more points at the end of a round wins that round
- Winning two of three rounds wins the match
- Cards played in one round are removed at the end of it (with exceptions)
- Players draw a few cards between rounds (not a full redraw)
- Winning requires managing both within-round points and cross-round card economy

**Strategic implications:**
- Playing all your best cards to win round one is usually wrong — you will have worse cards for rounds two and three
- "Bleeding" the opponent (forcing them to play valuable cards in round one by winning it, then conceding to preserve your own cards) is a fundamental strategy unique to this structure
- Card advantage (having more cards in hand going into later rounds) is a multi-round resource, not a within-turn resource
- Some decks are built around winning specific rounds rather than overall points

**The provision system:** Gwent caps deck construction not by card count limits per rarity but by a provision budget — a total points value that the entire deck cannot exceed, with more powerful cards costing more provisions. This replaces rarity-copy limits with a budget system that allows players to build varied decks while preventing simple "fill deck with best cards" construction.

**Design lesson:** Changing the unit of victory (from "reduce opponent's life to zero" to "win two of three rounds") creates entirely new strategic considerations. If your game's win condition feels solved or monotonous, reexamining the victory structure is one of the highest-leverage design interventions available.

---

## R §4 — Artifact: Lessons from a Design That Failed

Artifact is the most documented failure in CCG history and contains important design lessons.

**What Artifact did differently:**
- Three simultaneous lanes (from its MOBA source), each with their own mana pool and board state
- No hand size limit; no deck size limit
- Card attacks are semi-random (targets determined randomly within lane)
- Gold earned from kills used to buy cards from a shop between rounds
- Retail price at launch in a genre dominated by free-to-play

**Why it failed:**
- **Random combat targeting** removed the player's sense of control and agency. When your creatures attack random targets, you cannot plan precisely — the game feels like it happens to you rather than because of you
- **Retail price barrier** in a genre where all competitors were free to start created immediate rejection. Players unwilling to pay upfront to try an untested game in a crowded genre
- **No way to earn cards through play** made the game inaccessible to players who wanted to explore before committing money
- **Complexity mismatch**: three simultaneous lanes with their own economies required significantly more cognitive load than any competitor, and the game offered no simplification features for new players

**Design lesson:** Player agency is foundational. Cards that determine their own outcomes through random targeting remove the primary satisfaction of CCG play (making a correct strategic decision and having it succeed). Any mechanic that separates the player's decision from the outcome must be designed with extreme care. The Artifact case demonstrates that novelty does not compensate for undermining core player agency.

---

## R §5 — Legends of Runeterra: Alternating Attack Structure

Legends of Runeterra changed the attack phase into an alternating mechanic rather than each player having a dedicated attack phase.

**Structural mechanics:**
- Players alternate between "attacker" role and "defender" role each turn
- The attacker chooses which units to send into each combat
- The defender chooses which units block each attack after seeing the attack formation
- This continues until neither player can or wants to extend the attack

**Design implications:**
- Both players are active during combat, making the attack phase a multi-step negotiation rather than a passive experience for the defending player
- The defender has full information about the attacker's formation before committing to blocks — this rewards defensive reading and punishes all-in attacks

**Champion level-up system:** Each champion card has specific conditions that cause it to permanently level up during play, increasing stats and changing abilities. The level-up condition is stated on the card. This creates a secondary objective within each game: working toward the level-up condition while managing the primary win condition.

**Design lesson:** The defending player in most CCGs is passive during the attack phase. Making both players active during combat creates more engagement per turn and more decisions per minute. If your game has a single-direction attack phase, consider whether some form of defender interactivity would add depth without adding confusion.

---

## R §6 — Marvel Snap: Extreme Minimalism

Marvel Snap represents the furthest point on the minimalism spectrum in CCG history: 12-card decks, 6-turn matches, 3 randomly determined locations as the win condition.

**Structural mechanics:**
- 12 cards per deck — no more, no less
- Matches last exactly 6 turns
- Three locations are revealed progressively (one per two turns); each has a unique effect
- Players place cards to try to control locations; whoever has highest total points in a location controls it
- Controlling two or more of three locations wins the match
- A "snap" mechanic allows doubling the stakes mid-match

**Design implications:**
- With 12 cards, almost any strategy can be built with exactly the cards intended — minimal draw variance
- 6 turns creates extremely fast games (3–5 minutes) suitable for mobile
- Random location effects each game prevent any deck from being universally optimal — every deck has locations it is better or worse at
- The pool progression system (players unlock cards based on overall collection level) staggers competitive access but creates issues when different players are at different pool levels

**Limitation identified in source:** The 12-card limit means customisation options are heavily constrained. If a strategy requires certain cards, those cards are already determined by the strategy — there is little room for personal variation within archetypes. Extreme minimalism trades depth for accessibility.

**Design lesson:** Minimalism is a product positioning decision, not a design quality judgment. Marvel Snap is excellent for its target audience (mobile, quick play, low commitment). It is not better or worse than a 60-card game — it is designed for different players and contexts. Identify your target context and design minimum viable complexity for it.

---

## R §7 — The Market Entry Rule

Every CCG study produces the same finding about market entry: the genre does not forgive poor launches. The games that failed (Artifact, The Elder Scrolls: Legends, Duelyst) share common patterns. The games that survived (Hearthstone, Shadowverse, Gwent, Legends of Runeterra) share different ones.

**Patterns in failed launches:**
- Asking players to pay before they can evaluate the product (Artifact's retail price)
- Insufficient differentiation from an established competitor (Elder Scrolls: Legends was Hearthstone with Elder Scrolls art)
- Core mechanics that undermine player agency (Artifact's random combat)
- Incomplete feature set at launch compared to established games

**Patterns in successful launches:**
- Free to start with a visible free-to-play path
- Distinct identity that cannot be easily dismissed as "copy of X"
- Core mechanic that creates a memorable experience in the first 5 minutes
- Stable server performance on day one (digital CCG launch = player surge; client failure on day one is close to unrecoverable)

**The community-first rule:** No CCG can survive without a player base. A technically excellent game with no players is unplayable. Marketing, community building, content creator outreach, and beta player cultivation must begin months before launch. The game must arrive with players, not acquire them after.

**The Gwent exception:** Gwent is the only major CCG that underwent a complete redesign (including rebuilding every card) after launch and survived. This is attributed to two factors: the player community remained engaged through the transition period because the development team was transparent about what was being changed and why, and the game retained its core structural identity (three rounds, provisions, faction leaders) even while rebuilding the card pool. The lesson is not "complete redesigns can work" — it is "complete redesigns can work only with extraordinary community trust built over years."
