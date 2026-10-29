# Example Playtest Audit Report

Fictional demonstration using simulated personas. The sessions, scores and feedback below are illustrative, not observed playtest evidence.

## 1. Executive Summary

**Game:** Iron Orchard  
**Version:** v0.2  
**Test type:** Balanced + stress follow-up  
**Sessions:** 3  
**Tester count:** 18  
**Overall verdict:** Promising but uneven.

The core resource engine is strong, especially for euro and 4X players, but the combat timing rules repeatedly caused disputes. The design should keep the asymmetric factions but simplify reaction windows before further balance testing.

## 2. Audit Dashboard

| Area | Score | Colour | Evidence | Recommendation |
|---|---:|---|---|---|
| Rule clarity | 46 | Orange | 11 of 18 testers asked timing questions during combat | Rewrite combat sequence |
| Onboarding | 62 | Yellow | New players understood harvesting but not diplomacy | Add first-round guide |
| Strategic depth | 82 | Green | Four viable strategies emerged across three sessions | Preserve core engine |
| Balance | 58 | Yellow | Iron Guild won 4 of 6 games | Re-test after combat rewrite |
| Accessibility | 55 | Yellow | Iconography relies too much on colour | Add symbols and reference cards |
| Theme integration | 88 | Blue | Testers naturally described factions by theme | Preserve faction identity |

## 3. Persona Feedback

```yaml
tester_id: 147
tester_name: Milo "Fleet" Ibrahim
persona_type: Euro/Economic Simulation, House-ruler
feedback: The engine is readable after round two, but the first round feels like choosing from fog. I need an example of a good opening.
confidence: medium
possible_bias: May patch unclear rules and under-report the resulting friction.
design_relevance: High for onboarding and decision scaffolding.
```

## 4. Rule Change Log

| ID | Symbol | Area | Change | Effect | Status |
|---|---|---|---|---|---|
| R-001 | ~ | Combat | Reordered reaction timing | Reduced disputes but slowed combat | Needs simplification |
| R-002 | + | Onboarding | Added faction opening hints | Improved first-round confidence | Keep |
| R-003 | ? | Diplomacy | Trialled binding trade promises | Increased negotiation but caused rules questions | Re-test |
