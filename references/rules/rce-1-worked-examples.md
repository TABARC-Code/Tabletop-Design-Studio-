# RCE-1 — Rules Clarity Engine, Standard No. 1

## Part 3: Worked Examples

**Author:** TABARC-Code
**Author URL:** https://github.com/TABARC-Code/
**Status:** Issue 1

---

Each rule ID below carries a non-compliant/compliant pair, following STE-100's own `nonste_example`/`ste_example` convention. Where the source material (a Sam Pearson video essay on tabletop rules-writing craft, cross-referencing Mordheim 1999, Age of Sigmar 2nd/3rd/4th edition, and WarCry 2) contains a directly attributable worked case, that provenance is noted. Where no direct source example exists for a rule, the pair is original, constructed to the same principle, and marked as such.

---

## RCE1.1.1 — The Aura-vs-Tag Test

**Provenance:** directly from source material (made-up "Blessing of Might" ability, used as the video's opening diagnostic case).

**non_compliant:**
> Blessing of Might: until the start of the next round, add one to the toughness value of friendly units within 6 inches of this unit.

**Why it fails:** states both a range (6 inches) and a duration (until the start of the next round) with no marker distinguishing continuous-proximity effect from resolve-once effect. Genuinely readable two ways — as an aura that ends the moment a unit leaves the 6-inch radius, or as a status tag applied once and held regardless of subsequent movement.

**compliant (aura reading):**
> Blessing of Might: add one to the toughness value of friendly units **while** they are within 6 inches of this unit.

**compliant (tag reading):**
> Indomitable Will: each friendly unit within 6 inches **becomes indomitable until** the start of the next round. While a unit is indomitable, add one to its toughness value.

**Note:** the two compliant versions are not paraphrases of each other — they are two different games. This is RCE-1's central point: the ambiguous form conceals a real design decision the drafter has to actually make, not just word better.

---

## RCE1.1.2 — Bullet-Point Disambiguation for Multi-Effect Triggers

**Provenance:** directly from source material (generic damage-plus-status ability used to demonstrate the technique).

**non_compliant:**
> Pick a visible enemy unit within range and roll a d6. On a 4+ inflict d6 damage on that unit. In addition, that unit is staggered until the start of your next turn.

**Why it fails:** "in addition" joins a second effect to a first that was explicitly conditional on a 4+ roll. A reader cannot determine from word order alone whether "staggered" also requires the 4+, or is unconditional.

**compliant:**
> Pick a visible enemy unit within range and roll a d6. On a 4+: (1) inflict d6 damage on that unit, (2) that unit is staggered until the start of your next turn.

**If the intent were different** (staggered unconditional, damage conditional), the compliant form separates them entirely rather than relying on list order to imply it:
> Pick a visible enemy unit within range. That unit is staggered until the start of your next turn. Then roll a d6 — on a 4+, also inflict d6 damage on that unit.

---

## RCE1.2.1 — Controlled Lexicon, Locked Early

**Provenance:** directly from source material (real inconsistency cited from Mordheim, 1999, where "movement rate," "movement value," and "speed" all refer to the same defined term, "movement characteristic").

**non_compliant:**
> The normal movement value of models represents a warrior moving at a fairly rapid rate... A running warrior can move at double speed.

**Why it fails:** three different phrases — movement value, movement rate, speed — refer to a single defined concept ("movement characteristic," itself defined three pages earlier in the source text). A reader has to infer synonymy rather than being told it directly.

**compliant:**
> The normal **movement characteristic** of models represents a warrior moving at a fairly rapid rate... A running warrior can move at double its movement characteristic.

**Second illustration** (selection-verb lexicon, constructed): a drafter alternating "select," "choose," and "pick" within two adjacent sentences —

**non_compliant:**
> The player must select a unit. Once chosen, that unit may pick a target within range.

**compliant:**
> The player must pick a unit. Once picked, that unit may pick a target within range.

---

## RCE1.2.2 — Redundant Modal Purge

**Provenance:** directly from source material (the two-example "must" test).

**non_compliant (decorative, should be cut):**
> To make a run roll, the player must roll a d6 and add the score to the unit's move value.

**Why it fails:** nothing about this instruction was ever optional; there is no prior freedom being restricted. `must` adds emphasis without adding meaning.

**compliant (cut):**
> To make a run roll, the player rolls a d6 and adds the score to the unit's move value.

**Contrast — a correct, load-bearing use of "must":**
> When a unit makes a normal move, it must finish the move more than three inches away from all enemy units.

**Why this one is correct:** the ruleset has established elsewhere that a unit may move freely in any direction up to its move value. This sentence removes part of that granted freedom, and `must` correctly signals a restriction is being applied, not merely an instruction being given.

---

## RCE1.2.3 — Game Terms as Compression

**Provenance:** directly from source material (the "active player" coinage, and the historical "draw an imaginary straight line 1mm wide" case from Age of Sigmar 2nd/3rd edition).

**non_compliant (repeated full phrase):**
> In the movement phase, the player whose turn is taking place can pick friendly units to make moves.
> *(the phrase "the player whose turn is taking place" recurs verbatim four further times across the document)*

**Why it fails:** an eight-word phrase used five times with no coined short form. Each repetition costs the reader nothing individually but the document accumulates unnecessary length and each instance is a separate opportunity for a copy-paste variant to introduce inconsistency.

**compliant:**
> **Active player:** the player whose turn is taking place. *(glossary entry, defined once)*
>
> In the movement phase, the active player can pick friendly units to make moves. *(and four further uses, all reading "active player")*

**Historical cautionary case (from source, Age of Sigmar):** 2nd edition repeated "Draw an imaginary straight line 1mm wide" verbatim every time a rule required a measured line — an unsightly, repeated construction with no coined term. 3rd edition fixed this not by shortening the phrase inline but by defining it once in a core-concepts section ("if a rule tells you to draw a straight line, it is imaginary and 1mm wide") and thereafter simply writing "draw a straight line." Illustrates that the fix for over-repetition is definition-once, not phrase-shortening-in-place.

---

## RCE1.2.4 — Keywords as Levers

**Provenance:** directly from source material — the "aura ability" keyword built for the persisting-buff version, and "enchant ability" as its sibling keyword for the resolve-once version, applying a separately named status ("indomitable"). Two type-level keywords for the two mechanic types established under RCE1.1.1, each demonstrated below.

**non_compliant (mechanic exists but has no keyword, so a later rule cannot cleanly reference it):**
> Blessing of Might grants friendly units within 6 inches a toughness bonus while they remain in range.
>
> *(elsewhere in the same document)* Enemy units cannot benefit from friendly toughness auras within 12 inches of this unit.

**Why it fails:** the second rule needs to reference the first rule's mechanic *type*, but the first rule was never given a formatted keyword — "toughness auras" is a vague, non-canonical reference rather than a precise citation.

**compliant:**
> Blessing of Might *(aura ability)*: grants friendly units within 6 inches a toughness bonus while they remain in range.
>
> *(elsewhere)* Enemy units cannot use *aura abilities* while within 12 inches of this unit.

**Second worked pair — the resolve-once sibling keyword, non-compliant:**
> Indomitable Will grants friendly units within 6 inches the indomitable status, adding 1 to toughness, until the start of the next round.
>
> *(elsewhere)* A later item needs to reference "abilities that grant a status on use" as a category, but no keyword exists for that mechanic type — only the status name "indomitable" is defined, which names the effect, not the ability type that grants it.

**compliant:**
> Indomitable Will *(enchant ability)*: each friendly unit within 6 inches becomes indomitable until the start of the next round.
>
> *(elsewhere)* This item cannot be equipped by a bearer of any *enchant ability*.

**Note on the two-level naming:** RCE1.2.4 (keyword) and RCE1.2.3 (game term) are distinct categories precisely because a single ability can need both — "enchant ability" is the keyword naming the *mechanic type* (a lever other rules hook onto), while "indomitable" is a game term naming the *status the mechanic produces* (a compression, not a cross-reference hook). Collapsing the two into one SWD entry, as an earlier draft of this document did, loses the distinction RCE-1 exists to enforce. See the worked SWD table under RCE1.3.4 for both entered correctly, at their correct category.

**Note on formatting convention:** the source material uses italics for this project; RCE-1 does not mandate italics specifically — see SWD schema §3, `keyword` category — but requires the chosen convention be applied without exception once set.

**Note on Shape (added on audit against RCE1.2.5):** both *aura ability* and *enchant ability* are Shape 1 — bare tags with no variable slot. Their grammar is nominal ("grants... a toughness bonus," "cannot use *aura abilities*"), and plural inflection ("aura abilities" for more than one instance) is legal for Shape 1 — RCE1.2.5 only restricts inflection and partial reference for Shape 3 compound phrases, not Shape 1 bare tags. Neither keyword carries a numeric or category slot, so neither could be mistaken for Shape 2 or Shape 4; the earlier draft of this document (before RCE1.2.5 existed) demonstrated Shape 1 correctly without ever having named it as such. See RCE1.2.5 below for the three shapes this document had not yet demonstrated.

---

## RCE1.2.5 — Keyword Grammar: Four Shapes, Four Sets of Rules

**Provenance:** the four-shape taxonomy itself is TABARC-Code's own formalisation, not stated in the source material — Sam Pearson's video treats keyword formatting as a consistency question only ("any of these are fine as long as it is consistent") and never addresses keyword grammar. The specific keyword terms used to illustrate each shape below are independently confirmed against current published Warhammer 40,000 10th/11th edition material (verified against official rules text and datasheets during this project's separate wargaming-lexicon research work), not invented for this document — a deliberate choice, since the earlier Shape 1 examples in RCE1.2.4 were original constructions and this rule benefits from grounding in terms a reader may already recognise from a real, large ruleset.

### Shape 1 — bare tag

**non_compliant (grammar not fixed — mixes nominal and adjectival reference to the same Shape 1 keyword across two rules):**
> This unit **has Stealth**: each time a ranged attack is made against it, subtract 1 from that attack's Hit roll.
>
> *(elsewhere in the same document)* A unit that **is Stealth** cannot also benefit from Benefit of Cover against the same attack.

**Why it fails:** "has Stealth" and "is Stealth" are both grammatically fine English, but the document never fixed which one governs project-wide — a reader hits both forms and has to guess whether they're the same relationship stated two ways, or two different things. This is RCE1.2.1's controlled-lexicon discipline, unapplied to a keyword specifically.

**compliant:**
> This unit **has** Stealth: each time a ranged attack is made against it, subtract 1 from that attack's Hit roll.
>
> *(elsewhere)* A unit that **has** Stealth cannot also benefit from Benefit of Cover against the same attack.

### Shape 2 — parameterised keyword (single variable slot)

**non_compliant (value dropped from an instance reference, reintroducing an aura-vs-tag-style ambiguity):**
> This weapon has Rapid Fire 2.
>
> *(elsewhere)* When this weapon fires at a target within half range, add its Rapid Fire to the Attacks characteristic.

**Why it fails:** "add its Rapid Fire" with no value stated drops the parameter that makes the keyword resolvable — a reader cannot execute the rule without hunting back for the instance's stated value, and if the weapon's profile is presented separately from this rule text (a common layout), the value may not even be visible at the point of use.

**compliant:**
> This weapon has Rapid Fire 2.
>
> *(elsewhere)* When this weapon fires at a target within half range, add 2 to the Attacks characteristic (its Rapid Fire value).

**Legal family reference, for contrast (no value needed because no specific instance is being resolved):**
> Weapons with the Rapid Fire ability gain additional attacks at short range; the exact bonus depends on the weapon's stated value.

### Shape 3 — compound phrase-keyword

**non_compliant (partial reference to a locked compound phrase, inventing an undefined category):**
> This weapon has Devastating Wounds.
>
> *(elsewhere)* Units immune to Hits-type abilities ignore this weapon's Sustained Hits and Devastating Wounds.

**Why it fails:** "Hits-type abilities" is not a defined category — it looks like a reasonable informal grouping of *Sustained Hits* and *Devastating Wounds* because both compound phrases happen to contain "Hits," but nothing in the SWD ever locked a family relationship between them, and *Devastating Wounds* doesn't even contain the word "Hits." A reader has no way to know whether this informal grouping is meant to include other keywords or not.

**compliant (if a genuine family relationship is intended, it is locked explicitly as its own `mechanic pattern` entry first):**
> *Critical-result weapon abilities* (mechanic pattern, SWD-locked): Sustained Hits, Lethal Hits, and Devastating Wounds are jointly the critical-result weapon abilities — each triggers only on a Critical Hit or Critical Wound result. Rules referencing this family cite it by this locked name.
>
> *(elsewhere)* Units immune to critical-result weapon abilities ignore this weapon's Sustained Hits and Devastating Wounds.

### Shape 4 — compound-parameterised keyword

**non_compliant (category slot left implicit, only the numeric slot filled):**
> This weapon has Anti-Vehicle 3+.
>
> *(elsewhere)* Against a matching target, an Anti ability of this weapon scores a Critical Wound on the stated roll or higher.

**Why it fails:** "an Anti ability of this weapon" doesn't say which of the weapon's Anti- instances is meant if the weapon has been given more than one (a weapon can legally have both Anti-Vehicle X+ and Anti-Infantry Y+ as separate instances) — the category slot (Vehicle, Infantry, Monster, or whatever closed list the project defines) has been silently dropped, and only the numeric threshold survived. This is Shape 4's version of RCE1.2.5's Shape 2 failure, compounded by having two slots instead of one.

**compliant:**
> This weapon has Anti-Vehicle 3+.
>
> *(elsewhere)* Against a Vehicle target, this weapon's Anti-Vehicle ability scores a Critical Wound on a wound roll of 3+ or higher.

**SWD entry for the Shape 4 template (both slots specified, per Part 2 §2):**
> **Anti-X Y+** (keyword, Shape 4): category slot X — closed list: Vehicle, Infantry, Monster (project-defined; add categories here only by locked SWD revision, not ad hoc); numeric slot Y+ — threshold, comparison operator "or higher," applies to the wound roll. Definition: a matching attack scores a Critical Wound if its wound roll meets or exceeds Y, against a target with keyword X.

**Why this set of four works together:** each shape failure is structurally the same failure RCE1.1.1 names for aura-vs-tag — a value or relationship the rule depends on has been left for the reader to infer rather than stated. RCE1.2.5 exists because that same failure recurs at the level of individual keywords, not just whole-effect duration, and a project's SWD cannot enforce grammar it never named.

---

## RCE1.3.1 — Agency Consistency

**Provenance:** directly from source material (Blood Bowl's Rodney Roachbait rule as an all-unit-agency cautionary case; 3rd edition Age of Sigmar's all-player-agency as the opposite cautionary case).

**non_compliant (all-unit agency, reads as anthropomorphising the miniature):**
> Catch of the Day: once per half, if Rodney is standing and begins his activation within three squares of a ball on the ground, he may roll a d6. On a three-plus, Rodney immediately gains possession of the ball.

**non_compliant (all-player agency, reads as detached from the fiction — opposite failure):**
> When you shoot or fight with a unit, you make attacks with the weapons the models in the unit are armed with.

**compliant (mixed model, RCE-1's recommended default):**
> The player picks a friendly unit to make a move. The unit then moves up to its move value.

**Why this works:** the player is given agency over selection and dice-rolling (the human actions at the table); the unit is given agency over movement and combat (the fictional actions in the game world). This split is not arbitrary — it tracks which actions genuinely belong to the person playing versus the piece on the table — and, once chosen, is held consistently across every rule in the document, including victory conditions and objective control.

---

## RCE1.3.2 — Header-Signpost Dense Caveats

**Provenance:** directly from source material (WarCry 2 cover-from-terrain rule, cited as the author's own published work and acknowledged shortfall).

**non_compliant (context given only after the confusing clause, as a trailing parenthetical):**
> To determine if a target fighter is in cover due to any obstacles, draw an imaginary line between the closest points of each fighter's base. If the line passes through an obstacle, the target fighter is in cover.
>
> If the fighters are more than one inch away from each other, do not count parts of obstacles within half an inch of the fighter making the attack action.
>
> *(This represents fighters that have weapons with a longer range, being able to aim around corners, through gaps in nearby terrain, and so on.)*

**Why it fails:** the second paragraph reads as arbitrary and confusing on first encounter — a reader has no way to know it exists to prevent an unintuitive interaction (an archer standing behind a wall granting cover to everyone else they shoot at) until they reach the trailing explanation, by which point the confusion has already occurred.

**compliant:**
> **Attacks from behind terrain.** When making an attack action, draw a straight line between the closest points on each fighter's base. If the line passes through an obstacle, the target fighter is in cover.
>
> If the fighters are more than 1 inch apart, ignore parts of obstacles within 1 inch of the attacking fighter when determining cover. *See diagram.*
>
> This allows fighters directly behind low walls and similar obstacles to make attacks from afar without granting cover to their target.

**Why this works:** the header ("Attacks from behind terrain") tells the reader what kind of situation the rule addresses before they reach the mechanically unusual clause, so the exception reads as purposeful rather than arbitrary from the first sentence onward — the trailing explanatory line is retained as reinforcement, not relied on as the sole aid.

---

## RCE1.3.3 — Register Is a Decision, Not a Default

**Provenance:** conceptually from source material (the Fireball 5th-edition-vs-4th-edition natural-English-vs-jargon comparison); no single non-compliant/compliant textual pair applies, since this rule governs a project-level *process decision*, not a sentence-level defect.

**Illustration of the spectrum (source material, both genuinely compliant at their respective positions):**

**Natural-English-forward (D&D 5th edition style):**
> A bright streak flashes from your pointing finger to a point you choose within range and blossoms into a fireball. Each creature in a 20-foot-radius sphere centred on that point must make a Dexterity saving throw, taking 8d6 fire damage on a failed save, or half as much on a successful one.

**Jargon-forward (D&D 4th edition style, same spell, different register):**
> Fireball. Standard Action. Area burst 3 within 20 squares. Target: each creature in burst. Attack: your intelligence modifier vs. Reflex. Hit: 3d6 + intelligence modifier fire damage.

**Why both are compliant:** neither register is more correct under RCE-1; both are executed to a high standard at their own position on the spectrum. What RCE1.3.3 actually governs is that the *choice* between them was made deliberately and confirmed, not defaulted — see Part 1, §0 and Part 2, §2.1 for how the decision is elicited and locked in the SWD.

---

## RCE1.3.4 — The Standard Wording Document (SWD)

**Provenance:** conceptually from source material (the video's "standard wording document" Google Sheets practice, and the Age of Sigmar 2nd-edition "Strikes-First" inconsistency as a cautionary case of what happens without one).

**non_compliant (no SWD, resulting real-world inconsistency, drawn from source):** two published rules from the same game edition, both intending an identical "fights first" mechanic, worded two different ways in different books:
> "The bearer fights at the start of the combat phase before the players pick any other units to fight in that combat phase."
>
> "This general and their mount fights at the start of the combat phase."

**Why it failed:** with no SWD cross-checking new rules against the exact locked phrasing of prior ones, players inferred the two wordings were two different, tiered mechanics ("Strikes-First" and a stronger "super-Strikes-First") rather than one mechanic worded two ways — an inconsistency the source material calls "the activation wars," created by an undocumented editorial decision that the longer clause was "redundant" without checking it against everywhere the shorter form had already shipped.

**compliant (worked minimum SWD, populated rather than placeholder — see Part 2 §7 for the schema this table follows, and Part 2 §2 for the Keyword Shape column added on the RCE1.2.5 audit pass):**

| Term | Category | Definition | First used | Formatting | Status | Keyword Shape |
|---|---|---|---|---|---|---|
| pick | lexicon | Selection verb for choosing a unit or target | Movement phase | — | locked | — |
| can | lexicon | Permission modal for optional actions | Movement phase | — | locked | — |
| battlefield | lexicon | The play surface | Core rules | — | locked | — |
| fighting a battle | lexicon | The activity the players undertake | Core rules | — | locked | — |
| the army wins | lexicon | Victory attribution | Victory conditions | — | locked | — |
| Register | project setting | Natural-English-forward, confirmed with client after first draft, per RCE1.3.3 | Session 1 | — | locked | — |
| active player | game term | The player whose turn is taking place | Movement phase | — | locked | — |
| indomitable | game term | Status name granted by an enchant ability; while held, add 1 to the bearer's toughness value | Indomitable Will | italic | locked | — |
| aura ability | keyword | Ability type-tag: effect granted continuously while a condition (usually range) holds; ends immediately when the condition stops holding | Blessing of Might | italic | locked | Shape 1 (bare tag) |
| enchant ability | keyword | Ability type-tag: effect measured once at the moment of use, applying a named status (see game terms) that persists to end condition regardless of subsequent movement | Indomitable Will | italic | locked | Shape 1 (bare tag) |
| Standard buff-aura pattern | mechanic pattern | All continuous-proximity buffs use "while [unit] is within [X] of [source]"; never "until [duration]" alone | Blessing of Might | — | locked | — |

**Why this works:** every locked entry above is checked before any new rule is drafted that touches selection, permission, the play surface, victory, register, recurring phrasing, or either keyword. A drafter encountering a new ability that grants a continuous proximity buff does not re-derive the aura-vs-tag wording from first principles — they check the Standard buff-aura pattern entry and match it, which is precisely how the Age of Sigmar "Strikes-First" inconsistency would have been caught before publication rather than after.

---

## Revision Log

| Issue | Date | Change |
|---|---|---|
| Issue 1 | 2026-09-23 | First publication. 10 rule pairs, 8 directly sourced from cited material, 2 (register, SWD) constructed as process illustrations since they govern project decisions rather than sentence-level textual defects. |
| Issue 1 (revised) | 2026-09-23 | Added RCE1.2.5 worked section (Shape 1–4 keyword grammar), grounded in terms independently confirmed against real Warhammer 40,000 material rather than original construction. Retrofitted RCE1.2.4's existing aura ability/enchant ability pair with explicit Shape 1 classification, added the Keyword Shape column to the RCE1.3.4 worked SWD table (backfilled for both existing keyword rows, null for all other categories per Part 2 schema). |
