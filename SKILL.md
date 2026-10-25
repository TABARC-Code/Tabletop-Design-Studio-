---
name: tabletop-design-studio
description: "One entry point for designing war games, miniatures games, board games and card games: concept, mechanics, balance and odds, rules writing, scenarios and maps, components and production, and playtesting. Routes each request to the right reference set and gate. Use for any tabletop design question, from 'my game feels swingy' to a full new game from a napkin idea."
---

# Tabletop Design Studio

One skill, nine modes. You describe the problem and the studio works out which mode it belongs to, which reference files to read and what the output should look like. You do not need to know which of the source skills a piece of advice came from.

The studio does not replace the designer. It remembers the boring questions: where the turn structure is, what the win condition is, whether the rules say what they mean, and whether anyone has actually played the thing.

## How to use it

1. Classify the request using the table below. If it spans modes, take them in the order given in the Pipeline section.
2. Read only the reference files the mode names. They are long, and most of a request needs a section, not the whole file.
3. Produce the output the mode asks for, using the template named.
4. Close with a verdict from the vocabulary in the Gates section, and say what you did not check.

## Step 1: Classify the request

| The designer says | Mode | Read first |
|---|---|---|
| "I have an idea", "help me design something", "pitch" | 1. Concept | `references/hydra/genres.md`, `templates/hydra/intake_form.md` |
| "How should this mechanic work", "invent a mechanic", "turn structure", "activation" | 2. Mechanics | `references/hydra/mechanic-invention.md`, `references/hydra/engines.md`, `references/wargame/D-activation-systems.md` |
| "Too swingy", "first-turn problem", "runaway leader", "does this balance", "odds" | 3. Balance and odds | `references/hydra/engines.md` (balance, randomness), `references/wargame/E-negative-feedback.md`, `references/cards/F-balance-and-meta.md` |
| "Card design", "card template", "faction", "keyword", "deck builder", "expansion" | 4. Cards | `references/cards/` (start at `A-design-philosophy.md`) |
| "Write this rule", "rulebook", "is this wording clear", "keyword register" | 5. Rules writing | `references/rules/rce-1-writing-rules.md`, `references/wargame/R-rules-writing.md` |
| "Scenario", "map", "campaign", "victory condition", "hex and counter", "zone of control" | 6. Scenarios and maps | `references/wargame/C-wargame-theory.md`, `references/wargame/Q-phillies-board-wargame.md` |
| "Components", "print run", "cost per copy", "proofs", "box" | 7. Components and production | `references/hydra/engines.md` (production), `references/cards/O-physical-production.md` |
| "Playtest plan", "run a playtest", "who should test this", "playtest report" | 8. Playtesting | `references/playtesting/persona_database_spec.md`, `references/hydra/playtest-system.md` |
| "Where are we", "what is blocking", "should I kill this" | 9. Gates and status | `references/hydra/pipeline.md`, `references/hydra/referee.md` |

Euro-style and hobby-culture questions go to `references/eurogames/master.md`. That is a reference module under Mode 2, not a separate mode.

## The modes

### 1. Concept

Get the intake answers before you design anything. The hydra intake asks for the hook, audience, player count, duration, interaction style, core verbs, randomness and any must-have constraints. Ask at most eight questions, and only the missing ones. If the designer gives a raw idea, fill the gaps with defaults and mark them as low-confidence:

- Duration: party 15 to 30 minutes, family 30 to 60, hobby 60 to 120.
- Interaction: "together", "survive" or "solve" means co-operative. "Betray" or "traitor" means semi-co-operative. Anything else is competitive.

Output a design brief against `contracts/design_brief_v1.schema.json`, with two to four success metrics.

### 2. Mechanics

Produce the four things the design must have before detailed work starts: a turn or round structure, a primary player verb set, a win or loss condition, and a minimal component model. If any is missing, draft that first and stop there.

Then build the core loop in three to five steps. Cap each iteration at one or two new mechanics. The first version has to be playable, not perfect.

Euro-style designs (low elimination, low downtime, constructive competition) also read `references/eurogames/master.md`, with the subskills it routes to.

Output a prototype pack, using `templates/hydra/prototype_pack.md` and `templates/hydra/rules_v0_1.md`.

### 3. Balance and odds

Work from the random and skill spectrum first. Heavy dice systems read the randomness section in `references/hydra/engines.md`. Miniatures games read the damage curves and survivability in `references/wargame/B-miniatures-core.md`. Card games read the power curve in `references/cards/F-balance-and-meta.md`.

Check specifically for:

- first-turn dominance, from `references/wargame/E-negative-feedback.md`;
- runaway leaders and kingmaking;
- dominant strategies, meaning a single line that every player finds;
- analysis paralysis, meaning too many decision branches.

Do not state odds you have not calculated. If the numbers are unknown, say so and suggest the simulation to run.

### 4. Cards

Read `references/cards/A-design-philosophy.md` first. It sets the decision-space test, which every card set has to pass. Then read the module for the specific problem: anatomy in `B`, resources in `D`, factions and keywords in `E`, expansions in `G`, and player archetypes in `H`.

The card-game material is written for collectible and deck-building games. The digital-first case studies in `references/cards/R-ccg-case-studies.md` and the digital deck-builder notes in `references/cards/S-deck-builder-and-formats.md` are kept as design examples. Read them as examples of decisions, not as a model to copy.

### 5. Rules writing

Use RCE-1. The standard is in `references/rules/rce-1-writing-rules.md`, the Standard Wording Document schema is in `references/rules/rce-1-swd-schema.md`, and worked pairs are in `references/rules/rce-1-worked-examples.md`.

Two rules matter most:

- Build the register first. Do not draft rules until the terms are locked. Terms that have a locked entry are not re-decided mid-draft.
- Draft from natural English, then agree the register level with the author. Do not assume it.

The drafting self-check is in `references/rules/drafting-checklist.md`. It is mandatory before anything is handed back.

The orchestration notes are in `references/rules/RELATIONSHIP_CONTRACTS-orchestrator.md`. They describe an auditing skill and a glossary skill that are not part of this build. See the Gaps section below.

Output rules text using `templates/hydra/rules_v0_1.md`.

### 6. Scenarios and maps

For wargames, start from the core battle question. Then choose a tight or loose design axis from `references/wargame/P-priestley-design-language.md`. Use `references/wargame/Q-phillies-board-wargame.md` for zone of control, stacking, the combat results table, supply, replacements and victory conditions.

For campaigns, map the full arc first with `references/wargame/A-fiction-scene-engine.md`. Each scenario then needs a dramatic focus stated in one sentence before any mechanics are chosen.

Check every victory condition with one question: "Why would a player engage with this?" If the answer is "they wouldn't", the condition rewards passivity.

### 7. Components and production

Read the production section in `references/hydra/engines.md` and `references/cards/O-physical-production.md`.

Build the component list in `templates/hydra/components.csv`. Count every piece. Check the cost per copy against the price the brief implies. If the numbers do not work, cut components before you cut rules.

Print proofs and colour and symbol accessibility checks are part of production, not a last step.

### 8. Playtesting

Plan before you test. Use `templates/hydra/playtest_plan.md`. Choose a tester sampling preset from `references/playtesting/playtester_taxonomy.md`. The presets there include balanced, stress test and others. The query syntax for the persona pool is in `references/playtesting/persona_database_spec.md`.

Testers come from the persona pool in `data/tabletop_playtester_profiles_FULL_1_380_claude_skill.csv`. Keep the tester IDs, and keep the same people across sessions where you can. Record sessions with `templates/playtesting/session_record.yaml`, and log every rule change with `templates/playtesting/rule_change_log.yaml`.

Separate what testers said from what they did. Behaviour is stronger evidence than opinion.

The persona pool is simulated. Do not present simulated findings as the results of real play. A simulated pass is a hypothesis for a real table.

Finish with `templates/playtesting/final_report_template.md`. An example is in `examples/example_playtest_report.md`.

### 9. Gates and status

Check the build against the gate sequence below. Use `templates/hydra/dashboard.md` for the status view and `templates/hydra/decision_log.md` for trade-offs.

When two goals compete, use the lens order in `references/hydra/referee.md`: learnability, then experience, then fairness, then production, then novelty. If the tie still stands, pick the option easier to test at the next playtest.

Kill the project after three iterations if the core loop is unstable, the identity is unclear, or structural failures remain unresolved. Not every idea survives refinement.

## Gates and verdicts

The hard gate in the source is in `references/hydra/pipeline.md` (section "Hard Gates"). A build must have four things before detailed work starts: a turn or round structure, a primary verb set, a win or loss condition, and a minimal component model.

The verdict words below are a proposal of this build, not something the sources define. The source material has no shared vocabulary of its own, so they are marked as a decision still open for the designer to confirm:

| Verdict | Proposed meaning |
|---|---|
| PASS | The gate's checks are met. Move on. |
| CONCERNS | Met, with named risks. The designer decides whether to proceed. |
| FAIL | Not met. Do not proceed until the named check passes. |
| NOT ASSESSED | The check could not be run, for example because there was no playtest or no numbers. This is never a pass. |

The stage sequence the modes follow is also this build's proposal, not a copy of a source:

1. Concept: pillars and audience agreed.
2. Mechanics: the four hard-gate items present, and the core loop works on paper.
3. Balance: odds are calculated or simulated and inside the agreed bands.
4. Prototype: the first print-and-play playtest is complete.
5. Playtest: the target number of sessions has run, and rule changes are logged.
6. Production: the component list is costed, and proofs are checked.

## Pipeline

This order is a proposal of this build, not taken from a source. The hydra autopilot steps, a different ordering of the same work, are in `references/hydra/pipeline.md` under section 2.

A new game from a raw idea runs Concept, then Mechanics, then Balance and odds, then Playtesting. Rules writing runs alongside Mechanics once the core loop is stable. Cards, scenarios and components are added as the game needs them. Gates and status run throughout.

## Writing style

Follow `references/hydra/writing-doctrine.md`. In short: UK English, precision over ornament, and concrete examples. Keep one light sceptical edge in the notes, but do not let it bury the advice.

## Gaps

These are known and deliberate. They are listed so nobody mistakes them for working features.

- `rules-clarity-drafter` depended on an auditing skill, `arbiter-engine`, that is not in this build. The drafting side works without it. The audit side does not exist yet.
- The glossary construction it delegates to `oxford-editorial-indexer` is not in this build either. `references/rules/delegation-to-oxford-editorial-indexer.md` describes the handover and points to files that are not here.
- `references/rules/RELATIONSHIP_CONTRACTS-drafter.md` and `references/rules/RELATIONSHIP_CONTRACTS-orchestrator.md` still refer to the original separate skills by their old folder paths. Read them as history, not as live links.
- `references/eurogames/master.md` keeps the packaging rules from its original skill. Ignore them. They are not relevant to this build.
- The card and wargame modules were written as standalone masters with their own routers. Their internal router tables still refer to module letters. The module letters are kept so cross-references in the original texts still resolve.
