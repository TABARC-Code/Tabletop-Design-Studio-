# R — Rules Writing

Rulebook structure, style principles, forensic analysis techniques, tone, terminology discipline, navigation design, indexing, cross-referencing, and playtesting methodology.

← Back to hub: `../SKILL.md`
Cross-loads: C (design philosophy), B (keyword definitions), H (tone/persona), D (rules that describe activation)

---

## R §1 — Macro Structure of a Rulebook

Every successful rulebook follows this shape, regardless of voice or style:

| Section | Contents | Purpose |
|---------|----------|---------|
| Front matter | Thematic intro; "what is this game?" overview; win condition summary | Build mental model before detail |
| Reference foundation | Components list; setup procedure; how to read profiles, dice, cards; core glossary | Establish shared vocabulary |
| Procedure sections | Turn structure; action types; movement; conflict resolution; special cases; endgame/scoring | Teach the game in play order |
| Appendices | Summary sheets; index; glossary; FAQ; scenario packs; designer notes | Support reference during play |

**Organise sections in the order players encounter them in play** — not in taxonomic order (don't group all movement rules together if movement appears in three different contexts).

→ Cross-load C §6: scenario design comes after the core procedure is established.
→ Cross-load B §7: keyword definitions belong in the Reference Foundation, not scattered through procedure sections.

---

## R §2 — Style Principles

### R §2.1 — Clarity Is Not Optional
A rule that is elegantly phrased but ambiguous at the table has failed. A rule that is plain and reliably applied has succeeded.

**Core style rules:**
- **One sentence, one rule.** Avoid multi-clause constructions that embed conditions inside conditions.
- **Direct imperatives.** "Roll two dice." "Remove the model." "Measure from the base edge." Not "the player may choose to roll two dice in order to resolve the attack."
- **Active voice.** "The attacker rolls first" not "The dice are first rolled by the attacker."
- **Consistent terminology.** Define each game element once. Use that name exclusively throughout. "Token," "marker," and "counter" are not synonyms unless you intend them to be.
- **Separate procedure from flavour.** Rules blocks are technical documentation. Theme belongs in sidebars, examples, and fiction sections — not embedded in core procedures.

### R §2.2 — Terminology Discipline
Terminology drift is the most common source of player disputes.

**Protocol:**
1. Create a master glossary before writing the rulebook.
2. Assign one canonical term to each game element.
3. Every writer must use that term without variation.
4. Flag synonyms in the index with "See [canonical term]."
5. Never use colloquial alternatives in procedure text (even if they feel more natural).

→ Cross-load B §7: keyword systems are the mechanical expression of terminology discipline.
→ Cross-load Crisis "Rules Are Ambiguous in Play."

### R §2.3 — Tone Selection
The most effective tone for wargame rules: **neutral, direct, and moderately conversational** — authoritative enough to be trusted, accessible enough that players do not feel they are reading a legal contract.

| Game Type | Recommended Tone | Flavour Location |
|-----------|-----------------|-----------------|
| Competitive / tournament | Clinical minimalism | Sidebars only |
| Narrative / skirmish | Technical + thematic | Examples and fiction sections |
| Historical simulation | Academic clarity | Designer notes section |
| Gateway / casual | Natural-English, conversational | Throughout, with care |

**Rule:** Match tone to game tone through examples, not through embedded rule prose. A grimdark game can have clinical rules text and vivid examples.

→ Cross-load H §2.5 (Quinn): default rules-writing persona.
→ Cross-load H §2.1 (Dorian): appropriate for flavour text and scenario fiction sections.
→ Cross-load F §6: natural-English rules language as a design principle for accessible games.

---

## R §3 — Forensic Analysis Techniques

A forensic approach treats rules text as linguistic evidence. Every sentence is auditable.

### R §3.1 — Sentence Labelling
Label every sentence in a rules draft by type:

| Label | Definition | Healthy | Troubled |
|-------|-----------|---------|---------|
| **Imperative** | "Do X" | Dominant in procedure | Buried in flavour paragraphs |
| **Conditional** | "If Y, then Z" | Clear if-then | Nested 3+ levels deep |
| **Definition** | "X is defined as…" | Appears early, used consistently | Missing or duplicated inconsistently |
| **Example** | "For instance…" | Follows complex conditionals | Replaces definitions rather than supporting them |
| **Flavour** | Thematic or voice text | In sidebars and intros only | Mixed into rule procedure |

A healthy procedure section: mostly imperatives, supported by conditionals and definitions, with examples after complexity spikes. Flavour absent from the procedure body.

### R §3.2 — Pattern & Exception Hunting
Check that similar procedures follow the same pattern of steps, symbols, and headings.

Flag "rule A and B are steps 1–2–3 but rule C is steps 1–3–Gamma" — this breaks player expectations and causes misremembering.

**Test:** Can a player predict the shape of a rule before reading it, based on similar rules they have already read? If not, standardise the pattern.

### R §3.3 — Terminology Drift Audit
Run a Find/Replace search for every synonym of each defined term. If "unit," "model," "figure," and "miniature" all appear in the same document when only "model" is canonical, every instance is a potential dispute at the table.

### R §3.4 — Authorship Fingerprints
When auditing someone else's rules text, look for:
- Favourite sentence shapes (favourite conditionals, recurring hedges)
- Punctuation habits (em-dash overuse, comma splices)
- How ambiguity is handled (deferred to player? to designer? to GM?)
- Nested clause depth as a complexity signature

These patterns reveal where the original writer's habits are creating systemic issues.

---

## R §4 — Playtesting Methodology

Playtesting is debugging. Apply the same discipline you would to testing a complex software build.

### R §4.1 — What Playtesting Discovers
- Logic errors (rules contradicting each other or creating undefined states)
- Exploits (rules combinations producing anomalous results)
- Imbalance (dominant strategies requiring no meaningful decision)
- Pacing failures (games ending too early, dragging mid-game, or stalling at disengagement points)
- Teaching failures (where cold readers consistently stumble)

### R §4.2 — Playtesting Stages
1. **Alpha (designer-present):** Find logic errors and gross imbalances before blind testing.
2. **Blind playtest (designer absent):** Observe where groups stall, argue, or misapply rules. The designer must not intervene — that's the whole point.
3. **Extreme-option testing:** Deliberately test the most unusual rules combinations, terrain states, and faction matchups.
4. **Varied skill-level testing:** Test with beginners and experienced players separately.
5. **Iterate from evidence:** Rewrite based on observed failure points, not assumptions about what players should understand.

**Critical principle:**
> If the designer must be present to explain a rule, the rule has not yet been written. The book must stand alone.

### R §4.3 — Cold-Read Testing Protocol
Give a fresh group the rulebook. Ask them to:
- Find how a specific rule works (e.g., "find how flanking works")
- Explain the turn sequence without prompting
- Play the first two turns with no designer present

Time each lookup. Adjust headings, index entries, and cross-references where they struggle.

---

## R §5 — Navigation Architecture

A rulebook is a tool, not a linear essay. Design it to serve two simultaneous use cases: first-read learner and mid-game lookup.

### R §5.1 — Heading Hierarchy
Two levels is usually sufficient:
- **Chapter** (Move Phase, Combat Phase, Morale)
- **Section** (Measuring Movement, Difficult Terrain, Charging)

Three levels maximum. Beyond three, the hierarchy becomes its own navigation burden.

### R §5.2 — Navigation Toolkit (Non-Negotiable for Any Rulebook)
- Detailed table of contents (2-level minimum)
- Full index with player-language synonyms
- Glossary of all defined terms
- Quick-reference summary card (turn sequence + key tables)
- Consistent visual language: bold for defined terms on first use, italics for examples, boxed callouts for critical exceptions

### R §5.3 — Index Design
Building a good index:

1. **Index game concepts, not just words.** List mechanics (Actions, Advantage, Cover), sub-topics (Cover — partial, total), and named procedures (Turn sequence, Initiative, Chase rules).
2. **Favour player language.** Include synonyms players will say at the table and redirect to canonical terms with "See."
3. **Structure:** 1–2 levels deep. One strong heading with clear sub-entries.
4. **"See" for redirects** (term has no page references; only sends to canonical entry).
5. **"See also" for neighbours** (term has entries and related material elsewhere).
6. **Build the index from a topic list** — mark terms as you write, not at the end.
7. **Blind-test lookup:** ask playtesters to find specific rules, timing how long it takes.

### R §5.4 — Cross-Reference Discipline
- Use stable targets: reference section numbers or heading names, not "as described above."
- Keep chains shallow: no cross-reference should require more than one hop.
- Maximum depth: one cross-reference leads to a section that fully answers the question. No "see X, which refers you to Y, which refers you to Z."

---

## R §6 — Common Rulebook Pitfalls

| Pitfall | Fix | Cross-Reference |
|---------|-----|----------------|
| No overview before components detail | Open with 1-page game summary | R §1 |
| Non-chronological rules order | Reorganise to match play sequence | R §1 |
| Teaching and reference mixed | Design explicitly for both with clear headings | R §5 |
| Multi-clause sentences | One sentence per rule | R §2.1 |
| Synonym drift | Master glossary + Find/Replace audit | R §3.3, B §7 |
| Flavour in procedure body | Move all flavour to sidebars and fiction sections | R §2.1 |
| Ambiguous pronouns | Name every actor explicitly every time | R §2.1 |
| First draft treated as final | Mandatory blind playtesting after every major revision | R §4.2 |
| Designer always explains | Blind-only playtesting sessions | R §4.2 |
| Passive victory conditions | "Why engage?" audit | C §6 |
| Nested conditionals 3+ levels deep | Break into numbered steps | R §3.1 |
| Index missing player-language terms | Rebuild from player vocabulary | R §5.3 |

---

## R §7 — Rules Text Audit Checklist

Run this before finalising any rules document:

**Structure**
- [ ] Does the document open with a "what is this game and how do you win?" summary?
- [ ] Are sections organised in play order, not taxonomy?
- [ ] Is there a complete table of contents, glossary, and index?

**Language**
- [ ] Is every defined term in the master glossary?
- [ ] Is each term used consistently throughout? (Run Find/Replace audit)
- [ ] Does every procedure sentence use direct imperatives?
- [ ] Is flavour text separated from procedure text?
- [ ] Are all actors named explicitly (no ambiguous pronouns)?

**Logic**
- [ ] Has every rule been labelled (imperative/conditional/definition/example/flavour)?
- [ ] Are similar rules in the same structural pattern?
- [ ] Are there any cross-references more than one hop deep?

**Testing**
- [ ] Has a blind playtest been run from this draft?
- [ ] Have cold-read lookups been timed?
- [ ] Have extreme-option combinations been tested?

---

## BIDIRECTIONAL LINKS FROM R

| To | R gives | R receives |
|----|---------|-----------|
| **B** | Terminology discipline; sentence structure for stat blocks and special rules | Keyword and stat definitions requiring precise language |
| **C** | Rules audit confirming decision space is clearly communicated | Design philosophy determining what rules need to cover |
| **H** | Rules structure constraining which persona fits a given document type | Persona cognitive frame shaping how rules text is written |
| **D** | Precise language standards for activation rule writing | Complex activation rules that test language precision most severely |
| **P** | Functional layer model; Say Why; Rule of Three; Troublemakers as craft techniques | Learning vs referencing dichotomy; tenor framework for tone selection |
| **Q** | Blind playtesting protocols for validating rules text under cold-read conditions | Playtesting methodology — specific stage-by-stage process |
