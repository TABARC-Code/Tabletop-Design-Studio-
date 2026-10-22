# Playtest System Reference

## Purpose

Simulate or plan playtests: multi-persona sessions, structured feedback capture, issue ranking.

---

## Use Cases
- Plan real-world playtest sessions with structured metrics
- Simulate 1:1 interviews or group playtests using personas
- Capture: fun, clarity, friction, likes/dislikes, issues, confusion
- Rank and prioritise issues for iteration

---

## Playtest Planning Workflow

1. **Define goals** — what are you testing? (Core loop? Balance? Teach time? Pacing?)
2. **Set hypotheses** — "If we change X, then Y will improve because Z"
3. **Design the session** — player count, duration, teach script, observation protocol
4. **Define metrics** — what to measure (see below)
5. **Run the playtest** — with real humans
6. **Debrief** — structured feedback capture
7. **Synthesise** — rank issues, identify patterns, prioritise fixes

---

## Standard Metrics to Capture

- Time to first meaningful choice
- Downtime per player (average and worst case)
- Rules questions count (and which rules)
- Runaway leader signals (score gap at midpoint)
- Kingmaking signals (did a losing player determine the winner?)
- Fun/frustration spikes (timestamped if possible)
- Teach time (actual vs target)

---

## Post-Game Survey (4 questions)

1. What felt unclear?
2. What felt slow?
3. Where did you feel clever?
4. Would you play again? Why?

---

## Persona-Based Simulation

When real playtesting isn't available, simulate using personas. Each persona has defined traits that affect how they play and what they notice.

### Persona Dimensions
- **Experience level**: new to games / casual / hobby / hardcore
- **Play style**: competitive optimiser / social player / explorer / rules lawyer
- **Patience threshold**: low (wants quick games) / medium / high (enjoys complexity)
- **Interaction preference**: loves negotiation / prefers solo puzzles / enjoys conflict
- **Rules sensitivity**: tolerates ambiguity / needs precision / breaks things intentionally

### Running a Simulated Playtest
1. Select 3–5 personas appropriate to the target audience
2. Walk through the game turn-by-turn from each persona's perspective
3. Flag: confusion points, frustration points, delight points, broken interactions
4. Compile issues and rank by severity

### Persona Examples (quick starters)
- **Emma, 34**: Hobby gamer, competitive optimiser, low patience for long teach, medium interaction preference. Will find the dominant strategy if it exists.
- **Raj, 28**: Casual gamer, social player, high patience, loves negotiation. Will ignore optimal play for funny moments.
- **Sofia, 42**: Hardcore gamer, rules lawyer, medium patience, prefers solo puzzles. Will find every edge case and timing ambiguity.
- **Marcus, 19**: New to games, explorer, low patience, likes conflict. Will struggle with complex iconography and lose interest if turns take too long.

### Full Persona Library
For detailed, fully-realised playtest personas (14 NPC-ready character sheets with voice, stakes, quirks, and table behaviour), read `references/hydra/personas.md`.

---

## Issue Ranking Framework

After collecting playtest data (real or simulated), rank issues using:

| Factor | Weight |
|--------|--------|
| Frequency (how often it occurs) | High |
| Severity (how much it hurts the experience) | High |
| Fix complexity (how hard to resolve) | Medium |
| Discoverability (how quickly players hit it) | Medium |

Priority = (Frequency × Severity) / Fix complexity

Address high-priority issues first. Resist fixing low-frequency cosmetic issues before structural problems.

---

## Iteration Rules
- Fix no more than 3 things between playtests
- Test one hypothesis per change when possible
- Keep the build playable at every iteration
- If a fix creates two new problems, revert it
