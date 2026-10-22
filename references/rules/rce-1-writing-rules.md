# RCE-1 — Rules Clarity Engine, Standard No. 1

## Part 1: Writing Rules

**Author:** TABARC-Code
**Author URL:** https://github.com/TABARC-Code/
**Status:** Issue 1
**Subtitle:** Standard for Tabletop Rules Clarity

---

## 0. Scope and Purpose

RCE-1 is a drafting-time standard for writing tabletop game rules text: miniatures wargames, board games, card games — any ruleset that has to be interpreted identically by people at a table without the designer present to arbitrate.

RCE-1 is not a rewrite of ASD-STE100. STE-100 is a controlled-vocabulary standard: it constrains which words a technical-manual writer may use, aimed at non-native English readers of aircraft maintenance documentation. RCE-1 constrains something STE-100 does not address at all: **mechanical resolution ambiguity** — the gap between a rule reading grammatically fine and a rule producing one identical game state at every table that plays it.

Where the two standards' concerns genuinely overlap — short sentences, one term with one meaning, cutting decorative modal verbs — RCE-1 states the overlap and does not re-derive what STE-100 already solved. See §0.3.

### 0.1 Document Structure

RCE-1 is issued as three parts, each its own file:

| Part | File | Function |
|---|---|---|
| **Part 1 — Writing Rules** | `rce-1-writing-rules.md` (this document) | The 11 rules, grouped into 3 sections, each with ID, summary, and one minimal compliant illustration |
| **Part 2 — SWD Schema** | `rce-1-swd-schema.md` | The Standard Wording Document schema — RCE-1's equivalent of STE-100's dictionary: a controlled, per-project terminology register, not a global word list |
| **Part 3 — Worked Examples** | `rce-1-worked-examples.md` | Full compliant/non-compliant pairs for every rule, addressable by rule ID, sourced against real published material where possible |

A rule is not fully specified by Part 1 alone. Part 1 states *what* the rule requires; Part 3 shows *compliance and violation side by side*, which is where genuine judgement calibrates. Read both before applying RCE-1 to a live drafting task.

### 0.2 Rule Identifiers

Every rule carries an ID in the form **RCE1.S.N** — Section number, then rule number within that section. IDs are stable across issues; a rule's content may be refined between issues, but its ID does not change once published, matching STE-100's own practice of refining rule text without renumbering.

### 0.3 Relationship to ASD-STE100

| Concern | STE-100 | RCE-1 |
|---|---|---|
| Vocabulary control | Controlled dictionary, ~900 approved words, one meaning/one part of speech each | Not addressed — RCE-1 assumes ordinary English vocabulary; §2 controls *which term you pick for a project-specific concept*, not the English language generally |
| Sentence mechanics | 53 rules on grammar, sentence length, voice | Partially overlapping — RCE1.2.2 (redundant modal) is STE-100-adjacent; RCE-1 does not restate STE-100's grammar rules wholesale |
| Mechanical/resolution ambiguity | Not addressed — STE-100 has no concept of "does this effect persist or resolve once" | Core concern — §1 exists for exactly this |
| Enforcement mechanism | The controlled dictionary itself, checked word by word | The Standard Wording Document (§3, Part 2) — checked phrase by phrase, mechanic by mechanic |

RCE-1 is a narrower, domain-specific standard. It does not compete with STE-100 and a project using both is not applying redundant rules — they govern different failure modes.

---

## Section 1 — Mechanical Precision

Rules governing what a game effect actually *does*, independent of how it is phrased.

### RCE1.1.1 — The Aura-vs-Tag Test

**Summary:** Every effect stating both a range and a duration must be classified as exactly one of two mechanical types before drafting, and that classification must be signalled by a fixed lexical marker.

- **Aura (continuous):** the effect persists only while the stated condition holds. Marker: `while`.
- **Tag (resolved):** the effect is measured once, at the moment of use, and persists independently of position thereafter. Marker: `becomes [status] until [end condition]`.

A rule stating both a range and a duration but using neither marker is non-compliant by default — this is RCE-1's single highest-frequency defect class, and it is correctable with one word choice rather than a redraft.

*Minimal compliant illustration:* "Add 1 to the toughness of friendly units **while** they are within 6 inches of this unit." — See RCE1.1.1 in Part 3 for the full non-compliant/compliant pair and the tag-form equivalent.

### RCE1.1.2 — Bullet-Point Disambiguation for Multi-Effect Triggers

**Summary:** When a single trigger condition (a dice roll, a check, a threshold) governs more than one downstream effect, the scope of that condition over each effect must be shown structurally, not left to prose word order.

Prose joining a second effect to a first with "in addition" after a conditional first effect creates a genuine, non-cosmetic ambiguity: does the condition govern both effects or only the nearer one? A reader cannot resolve this from grammar alone.

*Minimal compliant illustration:* "On a 4+: (1) inflict d6 damage, (2) that unit is staggered." — numbered structure makes both effects visibly subordinate to the same condition. See RCE1.1.2 in Part 3.

---

## Section 2 — Controlled Terminology

Rules governing what words mean and how consistently they are used, once chosen.

### RCE1.2.1 — Controlled Lexicon, Locked Early

**Summary:** Fix one term per project-specific concept before drafting begins, and do not vary it. Every synonym introduced is a second string the reader must confirm is identical in meaning to the first, and that confirmation cost compounds across a full ruleset.

Minimum lexicon decisions required before rule one is drafted: the selection verb (pick/select/choose), the permission modal (can/may), the play-surface noun (battlefield/board/table), the activity verb (playing a game/fighting a battle), and victory attribution (the player wins/the army wins). Project-specific concepts beyond this minimum are locked as they arise; see Part 2.

*Minimal compliant illustration:* "The player must **pick** a unit. Once **picked**, that unit may **pick** a target." — one term, three uses. See RCE1.2.1 in Part 3.

### RCE1.2.2 — Redundant Modal Purge

**Summary:** `must` is correctly used only when it restricts a freedom the rules text has already granted elsewhere. Where no prior freedom exists to restrict, `must` is decorative and is removed.

Test: remove `must` from the sentence. If the instruction's meaning is unchanged, the word was doing no work and should not have been there.

*Minimal compliant illustration:* "To make a run roll, the player rolls a d6" (no `must` — nothing was ever optional) vs. "it **must** finish more than 3 inches from all enemy units" (`must` correctly restricts previously-granted free movement). See RCE1.2.2 in Part 3.

### RCE1.2.3 — Game Terms as Compression

**Summary:** A phrase expected to recur across multiple rules entries is coined as a defined term once, then used only in its short form thereafter. This is a controlled compression, not a stylistic shortcut — the definition exists exactly once, so every later use is guaranteed identical.

A term is not coined for single-use phrasing; a glossary entry with one occurrence is a second document to hold in memory with no compression benefit returned.

*Minimal compliant illustration:* "the player whose turn is taking place" (8 words, recurs 5 times) → coined as **active player** (1 term, defined once). See RCE1.2.3 in Part 3.

### RCE1.2.4 — Keywords as Levers

**Summary:** A game term is promoted to a formatting-marked keyword when other rules — present or anticipated future expansions — will need to reference the mechanic directly without re-describing it. The formatting convention (italic, bold, or bracket) is chosen once at project level and applied without exception.

A keyword functions as a hook: later rules cite the keyword rather than re-explaining the mechanic it names.

*Minimal compliant illustration:* *"Aura ability"* as a keyword lets a later rule state "enemy units cannot use *aura abilities* within 12 inches of this unit" without redefining what an aura ability is. See RCE1.2.4 in Part 3.

### RCE1.2.5 — Keyword Grammar: Four Shapes, Four Sets of Rules

**Summary:** "Keyword" is not one grammatical object. A keyword takes one of four distinct shapes, and each shape has its own rules for how it may be modified, parameterised, negated, and referenced in later text. A project's SWD entry for a keyword must record which shape it is, because the shape determines what a later rule is allowed to do with it.

RCE1.2.4 governs *when* to promote a term to keyword status. This rule governs *how that keyword behaves once promoted* — the grammar a drafter and every later rule in the document must follow when using it. Getting the shape wrong produces the same class of ambiguity RCE1.1.1 exists to prevent, just at the level of a single word rather than a whole effect.

**Shape 1 — Bare tag (adjectival/nominal).** A single word or short fixed phrase with no variable slot, functioning as a property something either has or does not have. *Stealth, Slow, Torrent, Sniper.* The drafter must fix, once, which grammatical form governs project-wide reference to a Shape 1 keyword — typically "has [keyword]" (nominal: the keyword is a possession) or "is [keyword]" (adjectival: the keyword is a state) — and hold it without exception, the same discipline RCE1.2.1 requires of ordinary lexicon choices. Mixing "this unit has Stealth" in one rule and "this unit is Stealth" in another is a controlled-lexicon violation applied to keyword grammar specifically. A Shape 1 keyword is never given a numeric or category slot; if it later needs one, it has become Shape 2 or Shape 4 and must be re-classified, not silently extended.

**Shape 2 — Parameterised keyword (single variable slot).** A keyword template with one numeric or magnitude slot the specific instance fills in. *Blast X, Tough X, Melta X, Rapid Fire X.* The SWD entry is written for the template, not each instance — one entry for "Rapid Fire X," not a separate entry for every value of X that appears in the document. A later rule referencing the *family* rather than one instance ("weapons with the Rapid Fire ability," no value stated) is legal and does not require the value; a later rule referencing a *specific* instance must carry the value ("this weapon's Rapid Fire 2"). RCE-1 does not permit referencing an instance's value without the keyword ("its Rapid Fire" with no number) — that drops the parameter that makes the keyword meaningful and reintroduces exactly the ambiguity RCE1.1.1's aura-vs-tag test exists to close.

**Shape 3 — Compound phrase-keyword.** A multi-word noun phrase that functions as a single indivisible tag, not a modifiable phrase. *Sustained Hits, Devastating Wounds, Twin-linked.* The phrase is locked in the SWD as one unbreakable string. A later rule may not reference part of it ("units with Hits-type abilities" is not a legal reference to *Sustained Hits* — it invents a category that was never defined) and may not silently pluralise or inflect it in a way that changes its cited form (if the locked string is "Devastating Wounds," a rule citing "Devastating Wound" singular is citing something that, strictly, does not exist in the SWD). Where a genuine *family* relationship across several Shape 3 keywords is intended — several keywords that should be jointly referenceable — that relationship is itself a `mechanic pattern` SWD entry (RCE1.3.4, Part 2 §3), created and locked explicitly, not implied by informal name resemblance.

**Shape 4 — Compound-parameterised keyword.** A keyword carrying two or more independent variable slots, at least one of which is itself a category rather than a number. *Anti-X Y+* (X is a target-category slot, Y is a numeric threshold slot). This is the most complex shape and the one existing rules-writing craft treats least carefully, because it looks like Shape 2 at a glance. A Shape 4 SWD entry records each slot separately — what kind of value X takes (a closed list of legal categories, stated explicitly) and what kind of value Y takes (a numeric threshold with its comparison operator, e.g. "X or higher") — and a later rule instantiating the keyword must fill every slot; a rule that fills only the numeric slot and leaves the category slot implicit or contextual has not correctly used a Shape 4 keyword and has recreated the aura-vs-tag ambiguity one level up, in category-selection rather than duration.

**Minimal illustration set** (Shape identified against terms independently confirmed in current published rulesets rather than invented for this rule): *Stealth* (Shape 1, nominal — "has Stealth"), *Blast X* (Shape 2), *Devastating Wounds* (Shape 3), *Anti-X Y+* (Shape 4). See RCE1.2.5 in Part 3 for the full worked set with non-compliant/compliant pairs per shape.

---

## Section 3 — Document Architecture

Rules governing how an entire ruleset holds together as one consistent document, above the level of any single rule.

### RCE1.3.1 — Agency Consistency

**Summary:** Every rules text implicitly assigns *agency* — whether the player, the army, or the individual unit is stated as performing the action. One distribution is chosen at project level and held without exception across movement, attacks, victory conditions, and status effects alike.

RCE-1's default recommendation is the mixed model (players roll and pick; units move and attack) as neither all-unit agency ("the fighter rolls a d6") nor all-player agency ("you make attacks with the weapons the models are armed with") reads naturally at scale — but RCE-1 does not mandate this default; it mandates that *a* distribution be chosen and audited for consistency.

*Minimal compliant illustration:* "The player picks a friendly unit to make a move. The unit then moves up to its move value." — clean agency handoff from player to unit. See RCE1.3.1 in Part 3.

### RCE1.3.2 — Header-Signpost Dense Caveats

**Summary:** A rule that only makes sense in light of unstated context — an edge case closed during playtesting, an exploit being prevented — requires a header naming what it addresses, placed *before* the reader encounters the confusing clause, not a trailing parenthetical explanation added after.

Trailing context helps a confused reader recover after the fact. Header signposting prevents the confusion occurring at all. RCE-1 prefers the header; a short trailing explanation may still be retained in addition, but not as the sole aid.

*Minimal compliant illustration:* A header reading "**Attacks from Behind Terrain**" placed immediately before a 1-inch obstacle-ignoring clause, so the reader has a frame of reference before the mechanically unusual text. See RCE1.3.2 in Part 3.

### RCE1.3.3 — Register Is a Decision, Not a Default

**Summary:** Every ruleset occupies a position on the spectrum between natural English (readable at a glance, costs more words) and dense project-specific jargon (compresses complex interactions, opaque to a new reader). Neither position is inherently more correct, and both can be executed to a high or low standard independent of position.

RCE-1 does not mandate a register. It mandates that the register be a **confirmed decision** — established through elicitation with whoever is authorising the ruleset, drafted-then-confirmed rather than assumed — and recorded as a locked project-level setting once made. See Part 2, §2.1 for how the register decision is recorded in the SWD.

### RCE1.3.4 — The Standard Wording Document (SWD) Is the Enforcement Mechanism

**Summary:** Every decision made under RCE1.1.1 through RCE1.3.3 is unenforceable the moment it exists only in the drafter's memory. The SWD is a living, per-project register — one entry per resolved mechanic, phrasing, or lexicon choice — checked against on every new rule drafted and cross-referenced in full at final edit.

The SWD is RCE-1's structural equivalent of STE-100's controlled dictionary: the second, separately maintained document that makes the first document's rules enforceable rather than aspirational. A ruleset with no SWD has no enforceable standard, whatever Sections 1 through 3 say on paper. The SWD's schema, required fields, and maintenance procedure are specified in full in **Part 2: SWD Schema**.

---

## Revision Log

| Issue | Date | Change |
|---|---|---|
| Issue 1 | 2026-09-23 | First publication. 10 rules across 3 sections. Source: Sam Pearson video essay on technical writing for tabletop rules, cross-checked against Mordheim (1999), Age of Sigmar 2nd/3rd/4th edition, and WarCry 2 as cited in that source. Restated and structured as original text, not transcript reproduction. |
| Issue 1 (revised) | 2026-09-23 | Added RCE1.2.5 (Keyword Grammar: Four Shapes, Four Sets of Rules) to Section 2 — 11 rules total. Not sourced from the original transcript, which treats keyword formatting as a consistency question only; this rule formalises grammatical behaviour Pearson's craft treatment never addressed. Corresponding schema change in Part 2 (Keyword Shape field) and worked-example audit in Part 3. |

## Origin and Attribution

RCE-1's core diagnostic content originates from a Sam Pearson video essay on technical writing in tabletop rules design. The rules above are TABARC-Code's own restatement, structuring, and section taxonomy — attributed here rather than presented as independently discovered. Direct source quotations do not appear in this document; all illustrations are original phrasing built from the same underlying craft principles.
