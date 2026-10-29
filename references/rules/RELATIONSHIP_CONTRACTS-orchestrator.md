# Rules routing contract

Author: TABARC-Code

## Inputs and local route

The [studio rules mode](../../SKILL.md) receives the supplied project rules, requested task and any existing SWD. It records which files were actually available. If several registers disagree, the author chooses the authoritative version before dependent drafting continues.

An existing SWD is checked against the [local schema](rce-1-swd-schema.md). A new SWD is constructed through the [drafting contract](RELATIONSHIP_CONTRACTS-drafter.md), using the five required lexicon decisions and the confirmed Register entry. Missing decisions remain unresolved rather than becoming invented locked entries. A short register-calibration passage may precede that confirmation; finished rules drafting may not.

## External services

| Service | Availability in this package | Unavailable outcome |
|---|---|---|
| arbiter-engine | Not bundled | Independent finished-text audit is NOT ASSESSED. Return the specific missing audit without claiming a pass. |
| oxford-editorial-indexer | Not bundled | Use the local SWD schema for basic register work. External indexing is NOT ASSESSED. See [handover mapping](delegation-to-oxford-editorial-indexer.md). |
| General wargaming lexicon | Not bundled | Advisory crosscheck is NOT ASSESSED; local drafting can continue. See [crosscheck](general-lexicon-crosscheck.md). |

An external service is available only when its actual files or interface have been verified for the current task. This package neither installs services nor edits their files. Unavailable services do not block unrelated concept, mechanics or component work.
