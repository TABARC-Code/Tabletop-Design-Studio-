# Pipeline Reference — Control Plane, Wizard, Autopilot

## Table of Contents
1. Beginner Wizard (idea → structured brief)
2. Autopilot Runner (brief → prototype pack)
3. Control Plane (multi-lens arbitration)

---

## 1. Beginner Wizard

Converts a rough board game idea into a structured design brief.

### When to use
When the user provides a vague or incomplete idea and needs it turned into something the pipeline can work with.

### Intake Form (max 8 questions)

1. Hook (one sentence)
2. Audience (kids / family / hobby / party / solo)
3. Players (min–max)
4. Duration (minutes)
5. Interaction (competitive / co-op / team / semi-coop)
6. Core turn verbs (1–3: plan, negotiate, draft, fight, build, puzzle, bluff, explore, optimise)
7. Randomness (low / medium / high)
8. Must-have theme / components / constraints

### Defaults (if not provided)
- Duration: party 15–30, family 30–60, hobby 60–120
- Interaction: "together"/"survive"/"solve" → co-op; "betray"/"traitor" → semi-coop; else → competitive
- If player verbs missing: infer from hook, mark as low confidence

### Output
`design_brief_v1` JSON object containing:
- title (short working title)
- elevator_pitch (hook + player activity + victory vibe)
- mode: "standard"
- players: { min, max }
- duration_minutes
- interaction
- core_player_verbs[]
- randomness
- success_metrics[] (2–4, auto-filled from audience + duration + interaction)

---

## 2. Autopilot Runner

Runs a repeatable design pipeline from a brief, producing a prototype pack.

### Input
A `design_brief_v1` (from the wizard or user-provided).

### Pipeline Steps
1. Generate core loop (3–5 step cycle, one paragraph)
2. Define win condition / end trigger
3. Design player interaction model
4. Draft component list (minimum viable)
5. Write rules v0.1 (use rules template)
6. Design playtest plan (use playtest template)
7. Identify risks and known weaknesses
8. Define next iteration TODOs

### Hard Gates (must pass before proceeding)
- Turn/round structure exists
- Primary player verb set defined
- Clear win/end condition
- Minimal component model

### Output
- prototype_pack_v1.md
- rules_v0_1.md
- components list (inline or CSV)
- playtest_plan_v1.md
- risk/weakness notes
- next actions

---

## 3. Control Plane (Multi-Lens Arbitration)

When multiple design concerns conflict (theme vs clarity, variance vs balance, novelty vs teach time), the control plane provides a structured resolution method.

### When to use
- Multiple design goals compete
- A change would improve one axis but harm another
- You need a principled way to choose between options

### Scoring Method

For each recommendation, score on:
- **Utility** (0–10): improves stated success metrics
- **Confidence** (0–1): how certain the recommendation is
- **Impact** (1–5): how much it matters to experience
- **Cost** (0–5): complexity / teach / setup / components burden
- **Risk** (0–5): balance risk, rules risk, playtest risk

Score = 0.40 × utility + 0.20 × (confidence × 10) + 0.20 × (impact × 2) − 0.10 × (cost × 2) − 0.10 × (risk × 2)

### Collision Detection
A collision exists if two recommendations touch the same subsystem (core loop, economy, info, interaction, endgame, components, rules load) and push in opposite directions.

### Tie-Break Lenses (in order)
1. **Learnability**: teach time, onboarding friction, rules load
2. **Experience**: agency, downtime, pacing curve, tension
3. **Fairness**: runaway leader, kingmaking, dominant strategies
4. **Production**: component count, table space, setup time
5. **Novelty**: only if the brief explicitly values innovation

If still tied: pick the option easier to test in the next playtest.

### Output
- Top-scoring compatible recommendations (accepted)
- Rejected recommendations (with reason)
- Unresolved questions (framed as playtest hypotheses)
- Decision log (trade-offs, conflicts, rationale)

### Re-Arbitration Triggers
Re-run arbitration when between iterations:
- Component count/types increase materially (+25% pieces or +1 new type)
- Rules load increases (new phase, action type, or exception rules)
- Randomness level shifts (low↔medium↔high)
- Scoring/endgame conditions change
- Player interaction structure changes
- Estimated downtime increases

### Mandatory Behaviour
- Do not invent playtest results
- If a recommendation changes the core loop, revalidate win condition, scoring, and end triggers
- Maintain version tags: v0.1, v0.2…
- Always keep the build playable at each iteration

---

## 4. Credibility Tracker (post-playtest calibration)

Prevents long-run score inflation by calibrating each engine's credibility using playtest evidence.

### Update Rule
For each **accepted** recommendation linked to an engine:
- If evidence supports improvement on success metrics: credibility += 0.02
- If evidence indicates harm, friction, or no measurable benefit: credibility -= 0.03
- Clamp credibility to [0.5, 1.5]
- Default credibility for all engines: 1.0

### Evidence Requirements
Every credibility change must include a short rationale pointing to a specific playtest note, issue, metric shift, or repeated complaint. No evidence → no change. Do not hallucinate metrics or playtest outcomes.

### Effect on Scoring
During control plane arbitration, multiply each recommendation's confidence by the relevant engine's credibility (clamped to [0, 1]).

---

## 5. Dashboard Views

Present a human-operable view of the current build state. Use `templates/hydra/dashboard.md` for format.

### Views to render
1. Brief Summary
2. Current Build Snapshot (core loop, win condition, components)
3. Risk Register (runaway, kingmaking, downtime, dominant strategies)
4. Playtest Checklist + Metrics
5. Rerun Menu (choose which analysis to rerun)
6. Iteration History (what changed between versions)

### Rerun Menu Options
- Balance only
- Pacing only
- UX/components only
- Rules rewrite only
- Mechanic invention (limit 1 new mechanic per iteration)
- Full pipeline rerun
