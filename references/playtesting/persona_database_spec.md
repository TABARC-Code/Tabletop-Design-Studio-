# Persona Database Specification

Canonical CSV:

```text
data/tabletop_playtester_profiles_FULL_1_380_claude_skill.csv
```

Expected columns:

- #
- Name
- Age
- Gender
- Sexuality
- SES
- Experience
- Primary Types
- Play Style
- Key Testing Focus

Use `#` as `tester_id`.

## Selection examples

```yaml
query:
  primary_types_contains: "4X"
  play_style: "Optimiser"
  experience_in:
    - "Regular (4–10)"
    - "Veteran (11–30)"
```

```yaml
query:
  primary_types_contains: "Accessible"
  key_testing_focus_contains:
    - "cognitive"
    - "sensory"
    - "physical"
```

## Anti-hallucination rule

Do not invent testers outside the CSV unless the user explicitly asks for temporary generated testers.
