# Command Grammar

Users may write formally or informally. Interpret intent flexibly.

## /run-playtest

```text
/run-playtest game="Name" sessions=3 testers=18 games=2 mode="balanced"
```

## /run-session

```text
/run-session session_focus="blind rules test" testers=6 games=1
```

## /change-testers

```text
/change-testers add=4 group="competitive optimisers"
```

```text
/change-testers replace="casual" with="historical wargamers"
```

## /change-rules

```text
/change-rules symbol="~" area="combat" change="Defender may react only once per round"
```

## /question-testers

```text
/question-testers group="accessibility" question="Where did cognitive load spike?"
```

```text
/question-testers tester_id=142 question="What would you exploit?"
```

## /audit-testers

```text
/audit-testers group="historical" focus="scenario fidelity and cultural sensitivity"
```

## /compare-sessions

```text
/compare-sessions a="Session 2" b="Session 4"
```

## /generate-report

```text
/generate-report style="professional audit" include="dashboard, feedback, technical writeup, rule log"
```

## /export-results

```text
/export-results format="markdown"
```

Supported output styles:

- markdown.
- yaml.
- csv-like tables.
- executive summary.
- technical report.
