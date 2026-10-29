# Rules drafting contract

Author: TABARC-Code

## Local ownership

The [studio](../../SKILL.md) owns rules drafting. The [routing contract](RELATIONSHIP_CONTRACTS-orchestrator.md) supplies the project rules and register. Drafting follows [RCE-1](rce-1-writing-rules.md), the [SWD schema](rce-1-swd-schema.md), [register elicitation](register-elicitation.md) and the [drafting checklist](drafting-checklist.md).

The project SWD is authoritative. Existing locked entries remain unchanged unless the author confirms a revision under the schema's maintenance procedure. A glossary is a derived view and cannot silently override the SWD.

## Dependency boundaries

The external arbiter-engine audit service is not bundled. The drafting checklist is a self-check, not an independent audit. Without a verified external audit, that audit remains NOT ASSESSED.

The external oxford-editorial-indexer service is not bundled. [Glossary handover](delegation-to-oxford-editorial-indexer.md) records the optional field mapping. Basic SWD construction uses the local schema and author-confirmed decisions; external glossary indexing remains NOT ASSESSED when unavailable.

No reciprocal changes to external packages are claimed or required by this package. This contract covers only the files linked above.
