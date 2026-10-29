# Optional glossary handover

The external oxford-editorial-indexer is not bundled. This mapping documents the intended handover; compatibility with a separately supplied version must be checked before use. It does not establish that the external service has run.

Without that service, basic register construction follows the [local SWD schema](rce-1-swd-schema.md) and [register elicitation](register-elicitation.md). Keep all seven schema columns, with null only where permitted. Confirm the five lexicon decisions and Register entry before finished rules drafting. Produce the SWD and derive the readable glossary from it; external cross-reference and indexing services remain NOT ASSESSED. If the requested spreadsheet format cannot be produced, report that delivery gap rather than claiming a workbook exists.

## What stays with rules-clarity-drafter (never delegated)

- Deciding *which* terms need registering in the first place — this requires RCE-1's own domain judgement (RCE1.1.1's aura-vs-tag classification, RCE1.2.5's keyword shape classification) that oxford-editorial-indexer has no way to make, since it isn't a tabletop-rules-specific skill.
- The register-decision elicitation (RCE1.3.3) — natural English vs jargon-forward, confirmed with the author. This is RCE-1-specific process, not a general editorial task.
- Applying the finished register to actual drafted rules text — oxford-editorial-indexer indexes and maintains; it doesn't draft game rules.

## What gets delegated to oxford-editorial-indexer

The mechanical construction and maintenance of the register once RCE-1 has decided what needs to be in it: building the actual glossary file, applying consistent formatting, cross-reference discipline (linking related entries), and the ongoing audit-for-consistency work oxford-editorial-indexer already does for any project.

## Field mapping — RCE-1 SWD schema → oxford-editorial-indexer glossary schema

The two schemas are not identical and must not be treated as interchangeable without this mapping. RCE-1's schema is the source of truth for tabletop rules content; this table is how it's translated into oxford-editorial-indexer's format for construction, and translated back when oxford-editorial-indexer's output needs to satisfy RCE-1's own requirements (e.g. the mandatory Keyword Shape field, which oxford-editorial-indexer's schema has no equivalent for).

| RCE-1 SWD field | Oxford glossary field | Notes |
|---|---|---|
| Term | Term | Direct mapping |
| Category (`lexicon`/`keyword`/`game term`/`mechanic pattern`/`project setting`) | Category | Not a direct enum match — see category mapping below |
| Definition | Definition | Direct mapping, but RCE-1 requires full mechanical text for `keyword` entries where Oxford's is more general-purpose; use RCE-1's fuller requirement when the two conflict |
| First used | First occurrence | Direct mapping |
| Formatting | *(no direct equivalent)* | Record in Oxford's "Usage note" field, since Oxford has no dedicated formatting-convention field |
| Status (`locked`/`under review`/`deprecated`) | Status (`Approved`/`provisional`/`conflicting`/`deprecated`/`needs author decision`) | Not identical enums — `locked` maps to `Approved`; `under review` maps to `provisional`; `deprecated` maps directly; RCE-1 has no equivalent to `conflicting` or `needs author decision` — when Oxford's audit surfaces either of those states, it is reported back to rules-clarity-drafter as a defect requiring RCE-1-side resolution (a category/lexicon decision), not resolved by Oxford alone |
| Keyword Shape (RCE1.2.5: Shape 1–4, mandatory for `keyword` category) | *(no equivalent field)* | **This has no home in Oxford's schema.** Oxford's own "Keyword" category type exists but carries no grammatical-shape distinction. Keyword Shape is recorded in Oxford's "Usage note" field as a workaround, but the RCE-1-side SWD file remains the authoritative record of Shape — the Oxford-built glossary is a *derived, human-readable view*, not a replacement for the RCE-1 schema file itself |

### Category mapping (RCE-1 → Oxford)

| RCE-1 category | Oxford category |
|---|---|
| `lexicon` | Style term (governs word choice, not content meaning) |
| `keyword` | Keyword |
| `game term` | Concept (or Mechanic, if the term names a gameplay system rather than an abstract idea — judgement call, state which was chosen) |
| `mechanic pattern` | Mechanic |
| `project setting` | Other (note the reason, per Oxford's own "Other" category rule) |

## Deliverables produced by this delegation

Two files, both real and both delivered to the author, not merely described:

1. **The RCE-1 SWD** (Excel, per `rce-1-swd-schema.md`'s exact 7-field schema) — the authoritative, RCE-1-schema-complete register. This is what `rules-clarity-drafter` and `arbiter-engine` actually check drafts and edits against.
2. **A standalone keyword list / glossary document** (derived from the SWD, using verified external conventions only when available) — the human-readable, author-facing reference, cross-referenced and indexed the way Oxford already does for any project. This is what the author reads and shares with playtesters or co-designers; it is a *view* of the SWD, not a second independent source of truth.

If the two ever disagree (an edit lands in one but not the other), the RCE-1 SWD wins, and the glossary document is regenerated from it — never the reverse. This mirrors the standing rule that a locked SWD entry is never silently overridden.
