# Relationship Contracts — rules-clarity-drafter

Written to the schema in skill-builder's `relationship-contract-engine/SUBSKILL.md`. This file holds every contract where `rules-clarity-drafter` is source or target.

## Relationship Contract: Rules Clarity Drafter → Arbiter Engine

**Source:**
Rules Clarity Drafter (RCE-1)

**Target:**
Arbiter Engine

**Relationship Direction:**
Rules Clarity Drafter → Arbiter Engine (drafting output becomes audit input)

**Reciprocal Direction:**
Arbiter Engine → Rules Clarity Drafter when an audit finds a defect class RCE-1 doesn't yet cover, or when arbiter-engine's five lenses (precision, consistency, agency, complexity, SWD) drift out of alignment with RCE-1's ten rules and need reconciling

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Strength Reason:**
Arbiter-engine's precision lens (aura-vs-tag), agency lens, and SWD lens are the same categories as RCE-1 Rules 1, 4, and 10 respectively — not independently derived, the same diagnostic split across a drafting/audit boundary. Not critical, because arbiter-engine can still audit rules text that was never drafted under RCE-1 at all (its actual primary use case is auditing existing published or legacy text). But when a project does use RCE-1 for drafting, arbiter-engine's checks against that project's SWD are meaningfully stronger and more precise than a cold audit with no SWD to check against.

**Direct or Indirect:**
direct

**Chain Position:**
upstream (RCE-1 drafts → SWD is produced → arbiter-engine consumes that SWD as its audit reference for that project)

**Reason for Relationship:**
Same craft source (Sam Pearson technical-writing-for-tabletop-rules material), same core diagnostic categories, deliberately split across two moments (drafting vs post-hoc audit) rather than merged into one skill, per explicit build decision. The two skills would silently duplicate or contradict each other without a stated contract governing who owns the SWD.

**Behavioural Impact:**
Rules-clarity-drafter MUST NOT audit finished/legacy text — that's arbiter-engine's job, and Stage 0 of this skill's SKILL.md hands off rather than running RCE-1 checks against someone else's prose. Arbiter-engine MUST NOT generate a fresh SWD from nothing when one doesn't exist for a project — SWD authorship stays with rules-clarity-drafter; arbiter-engine audits against an existing SWD or flags that none exists rather than fabricating one.

**Source Update Requirement:**
rules-clarity-drafter's SKILL.md Stage 0 must explicitly redirect audit/review requests rather than silently absorbing them. This file (RELATIONSHIP_CONTRACTS.md) must exist and state the SWD-ownership boundary explicitly.

**Target Update Requirement:**
arbiter-engine's own memory/repo file must record the reciprocal contract: that its SWD lens, when auditing a project with an RCE-1-generated SWD, should check against that SWD rather than building its own from scratch, and that its precision/agency lens categories trace to RCE-1 Rules 1 and 4 by shared origin, not independent derivation. As of this build, arbiter-engine is not installed in this environment (confirmed via disk check), so this reciprocal update is recorded as **pending** in memory (`/areas/rules-clarity-drafter.md`) rather than written to a phantom file — same honest-queueing pattern arbiter-engine itself used for its technical-clarity-engine and writing-standards-engine links when those skills weren't present on disk either.

**Affected Files:**
`rules-clarity-drafter/SKILL.md`, `rules-clarity-drafter/RELATIONSHIP_CONTRACTS.md`, `rules-clarity-drafter/references/rce-1-standard.md` (cross-reference note) — and, once arbiter-engine is next opened for edit, `arbiter-engine`'s own relationship-contracts file and its SWD-lens module.

**Audit Status:**
partially applied — source side complete and verified in this build; target side pending until arbiter-engine is next opened in a session where it's actually on disk.

## Skill Identity

**Author:** TABARC-Code
**Author URL:** https://github.com/TABARC-Code/
**Dewey-style Code:** 808.028
**Classification:** Rhetoric and technical writing — tabletop rules drafting discipline

---

## Relationship Contract: Rules Register Orchestrator → Rules Clarity Drafter (reciprocal record)

**Source:**
Rules Register Orchestrator

**Target:**
Rules Clarity Drafter (RCE-1)

**Reciprocal note:** the full contract for this link is authored from the orchestrator's side, in `rules-register-orchestrator/RELATIONSHIP_CONTRACTS.md` — reproduced here in summary per this project's bidirectional-linking discipline, so this skill's own contracts file is a complete picture without requiring a second file open.

**Relationship Direction:**
Rules Register Orchestrator → Rules Clarity Drafter (routing dispatch — orchestrator scans a project folder, decides whether a register exists, and if not, routes here to build one)

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Behavioural Impact on this skill specifically:**
rules-clarity-drafter no longer assumes drafting starts from either a blank project or an already-known SWD — Stage 0 now branches explicitly into Stage 2A (build from nothing, when routed here for that purpose) versus Stage 2B (maintain an existing register). This skill still performs no folder-scanning itself; that evidence arrives via the orchestrator's routing, not by this skill inspecting the filesystem independently.

**Audit Status:**
fully applied — both sides present on disk and updated in this session.

---

## Relationship Contract: Rules Clarity Drafter → Oxford Editorial Indexer

**Source:**
Rules Clarity Drafter (RCE-1)

**Target:**
Oxford Editorial Indexer

**Relationship Direction:**
Rules Clarity Drafter → Oxford Editorial Indexer (this skill's SWD-building workflow, Stage 2A, delegates the actual glossary/keyword-list construction to Oxford rather than rebuilding that machinery)

**Reciprocal Direction:**
Oxford Editorial Indexer → Rules Clarity Drafter when its own consistency audit surfaces a Status of `conflicting` or `needs author decision` with no RCE-1 schema equivalent — reported back for RCE-1-side resolution, never resolved unilaterally by Oxford (see the Status-field mapping table in `references/delegation-to-oxford-editorial-indexer.md`)

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Strength Reason:**
Oxford-editorial-indexer already has working glossary, cross-reference, and indexing machinery. Without this link, Stage 2A would need to duplicate it. The two schemas are not identical (RCE-1's Keyword Shape field has no Oxford equivalent, among other gaps) so the field-mapping table in `references/delegation-to-oxford-editorial-indexer.md` is load-bearing, not decorative.

**Direct or Indirect:**
direct

**Chain Position:**
parallel/supporting — invoked as a construction service within Stage 2A, not a separate stage in the drafting workflow.

**Reason for Relationship:**
Explicit build decision to delegate rather than duplicate, made the same session this link was established.

**Behavioural Impact:**
This skill MUST use the field-mapping table when calling Oxford, not assume schema compatibility. Oxford's output (the glossary/keyword-list document) is a derived view of the RCE-1 SWD — if the two disagree, the RCE-1 SWD wins and the glossary is regenerated, never the reverse.

**Source Update Requirement:**
`references/delegation-to-oxford-editorial-indexer.md` must exist (it does) and stay in sync if either schema changes. SKILL.md Stage 2A must reference it explicitly (it does).

**Target Update Requirement:**
oxford-editorial-indexer's own `related_external_skills` frontmatter should list `rules-clarity-drafter` and `rules-register-orchestrator`. Edited in this session's container copy of `/mnt/skills/user/oxford-editorial-indexer/SKILL.md` — but this environment's filesystem resets between sessions, so persistence to the user's real installed copy is unconfirmed from here. Treat as a patch to verify or reapply, not a confirmed permanent fix.

**Affected Files:**
`rules-clarity-drafter/SKILL.md`, `rules-clarity-drafter/RELATIONSHIP_CONTRACTS.md`, `rules-clarity-drafter/references/delegation-to-oxford-editorial-indexer.md`, and `/mnt/skills/user/oxford-editorial-indexer/SKILL.md` frontmatter (edited this session, persistence unconfirmed).

**Audit Status:**
source side complete; target side edited in-container this session, persistence to the user's real environment unconfirmed — same caveat as recorded in `rules-register-orchestrator/RELATIONSHIP_CONTRACTS.md`.
