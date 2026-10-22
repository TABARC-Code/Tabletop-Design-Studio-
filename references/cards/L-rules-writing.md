# Reference L: Rules Writing

## L §1 — Rulebook Structure

A card game rulebook serves two distinct functions, and most rulebooks try to do both at once, failing at both:

**Learning document:** Teaches a new player how to play. Needs to be linear, example-heavy, simple to start. Uses tutorial logic: introduce concepts in the order a player will encounter them.

**Reference document:** Lets an experienced player look up a specific rule quickly. Needs to be indexed, organised by topic, precise. Uses reference logic: find the exact rule, read the exact text.

These documents need different structures. For most card games, write both — a learning guide and a complete rules reference. The learning guide is the introductory pamphlet; the complete reference is the website or comprehensive rulebook.

**Rulebook sequence for a learning document:**
1. What the game is and who plays it
2. What is in the box/app (component list)
3. How to set up a game
4. What a turn looks like (overview, not detail)
5. How to play cards (basic mechanics)
6. Combat/resolution (if applicable)
7. How the game ends
8. Complete keyword glossary
9. Full rules reference

## L §2 — Terminology Discipline

Every mechanical concept must have exactly one name. Using two names for the same thing is a rules error that causes arguments.

**Terminology rules:**
- Choose a term early and use it everywhere, every time, without variation
- "Graveyard" and "discard pile" cannot both be used in the same game's rules text for the same concept
- "Destroy" and "remove from play" must mean different things if both are used — or one must be eliminated
- Define every term in the glossary before it appears in a card's text

**Active noun construction:** Card text should say "the owner" not "you" when the owner might not be the active player. Card text should say "this card" or name the card type, not "it," when multiple cards are in scope.

**Precision test:** Read each card's rules text in isolation. Can a player who has never seen any other card understand exactly what this card does? If not, the card depends on external context that should be made explicit.

## L §3 — Keyword Glossary Structure

Every keyword must have a glossary entry with exactly these components:

1. **Keyword name** in bold
2. **One-line summary** of what it does (the version that goes on cards)
3. **Full rules text** (the authoritative version)
4. **Interaction notes** — how it interacts with other specific keywords or card types
5. **Example** — at least one concrete example of the keyword in use
6. **Edge cases** — any situations where the keyword's application is non-obvious, with the ruling

**Glossary maintenance:** Every expansion that introduces new keywords must update the glossary. Every errata that changes a keyword must update both the glossary and the official card ruling.

## L §4 — Card Text Precision Standards

**Standard card text construction:**

For triggered effects (happens when a condition is met):
*"When [condition], [effect]."*
Example: "When this card is destroyed, deal 2 damage to your opponent."

For activated effects (player chooses to trigger):
*"[Cost]: [Effect]."*
Example: "Discard one card: Draw two cards."

For continuous effects (applies while the card is in play):
*"While [this card] is on the field, [effect]."*
Example: "While Storm Drake is on the field, all lightning spells cost 1 less."

For triggered effects with conditions:
*"When [event], if [condition], [effect]."*
Example: "When this card attacks, if the defending creature has Flying, deal 1 additional damage."

**Avoid:**
- Passive construction that obscures who is performing the action
- Pronouns that could refer to more than one card in the effect
- "May" when the player always will (creates false optionality) and missing "may" when the effect should be optional
- Text that uses a keyword before the keyword has been established in the text box

## L §5 — The "Say Why" Principle

Every rule exists for a reason. Card text that cannot be explained is card text that should be questioned.

When writing or reviewing rules, ask of every clause: why does this rule exist? What game state does it prevent or enable? If there is no good answer, the clause may not need to be there.

Applied to card text: "This card cannot be targeted by effects" — why? Is this faction identity? Is it preventing a degenerate interaction? Or was it added reflexively to make the card feel strong? If it's the latter, remove it.

Applied to phase rules: "No cards can be played during the attack phase" — why? Is this to prevent reactive spell chaining that would slow the game? Or is there no reason? If there's a reason, state it somewhere in the learning document.

## L §6 — FAQ and Errata Design

**FAQ (Frequently Asked Questions):** A living document that answers specific questions about card interactions. Not a substitute for well-written rules, but necessary for any game with sufficient card pool complexity.

**FAQ format:**
- Organised by card name (alphabetical) and by keyword (alphabetical)
- Each entry states the question in the form players actually ask it
- Each answer states the rule clearly, with the reasoning
- Each FAQ entry references the relevant glossary term or rulebook section

**Errata format:**
- Clearly identifies which version of the card the errata applies to
- States the original text
- States the new (correct) text
- States the reason for the change
- States the date the errata becomes effective
- States whether the errata affects competitive formats and from when

**Publication:** FAQ and errata should be on the official website, in the app (for digital games), and distributed to tournament organizers in advance of competitive play under the new ruling.

## L §7 — The Priority Stack: Simultaneous Effect Resolution

When multiple triggered effects fire at the same moment, the game needs a defined resolution order. Ambiguity here causes arguments at every table and is among the most common rules failures in TCG/CCG history.

**The priority stack principle:** Effects resolve in last-in-first-out (LIFO) order — the most recently triggered effect resolves first. This is the standard used by most major card games and should be adopted as the default unless the game has a specific reason to deviate.

**Explicit stack rules the rulebook must define:**
- When the active player and the non-active player both have effects triggered simultaneously, who places their effect on the stack first?
- Can effects be added to the stack in response to other effects (instant-speed interrupts)?
- When do "on death" triggers fire — before or after the card is removed from the field?
- What happens if an effect on the stack becomes impossible to resolve (its target is no longer in play)?

**Mandatory stack documentation:** Every time a new keyword is added to the game, document its stack behaviour explicitly. Does it add to the stack? Does it bypass the stack (immediate resolution)? Is it a replacement effect (changes what happens, rather than adding a new thing that happens)? These three categories — stack, immediate, replacement — cover all effect types and every keyword must be classified into one.

## L §8 — Tournament Documentation

Tournament documentation is distinct from the game rulebook and requires its own writing conventions:

**What tournament documentation must contain:**
- Match structure (best of 1, best of 3, time limits per match)
- Deck construction rules specific to the tournament format (legal sets, ban list, deck size minimum/maximum, copy limits)
- Procedure for beginning and ending a game (shuffle procedures, cut requirements, result reporting)
- Drawing and concession rules (is a draw possible? when can a player concede?)
- Unsporting conduct definitions and penalty guidelines
- Judge call procedure (how to summon a judge, what judges can and cannot decide)
- Appeals process

**Judge communication:** Judges must understand not just what the rules say but why. A judge who knows the reasoning behind a rule can adjudicate edge cases consistently. Distribute a judge reference card with:
- The 10 most common rules questions (with official answers)
- The 5 most common rules arguments (with resolution procedure)
- Contact for escalation when a judge is uncertain

**Floor rules:** Minimum standards for competitive play environments. These are distinct from game rules and cover:
- Mandatory deck sleeves (to prevent card marking)
- Prohibited note-taking during play
- Communication standards (what information must be shared freely, what is private)
- Slow play definitions and warnings

## L §9 — Rules Versioning and Translation

**Version control:** Every update to the rules requires a version number and a changelog. Players, judges, and tournament organisers must know which version is current and what changed between versions. Versioning format: Major.Minor (e.g. 2.1 — major edition 2, minor update 1). A version number on every rules document prevents disputes about which ruling applies.

**Changelog requirements:**
- Date of update
- Which rules changed (by section number)
- What the rule previously said
- What it now says
- Why it changed (optional but strongly recommended for community trust)

**Translation:** Precision in the source language does not automatically transfer to translation. Technical terms must be defined in every language separately — a translated keyword name must carry the same meaning as the original, not just the same words. Common translation failures:
- Literal translation of keyword names that lose their meaning (a keyword called "Trample" translates literally to a word meaning "crush underfoot" in some languages, losing the game-specific meaning)
- Legal language (terms like "owner", "controller", "target") having different everyday connotations in different languages
- Passive/active construction differences that change implied meaning

**Translation requirement:** Every language version requires a separate glossary with locally accurate definitions, not just translated definitions. An independent rules review by a native-speaking player is required before a translated rulebook is published.
