# Relationship Contracts — rules-register-orchestrator

Written to the schema in skill-builder's `relationship-contract-engine/SUBSKILL.md`. This file holds every contract where `rules-register-orchestrator` is source or target.

## Relationship Contract: Rules Register Orchestrator → Rules Clarity Drafter

**Source:**
Rules Register Orchestrator

**Target:**
Rules Clarity Drafter (RCE-1)

**Relationship Direction:**
Rules Register Orchestrator → Rules Clarity Drafter (routing dispatch — orchestrator decides a register needs building, hands the actual construction work to the drafter)

**Reciprocal Direction:**
Rules Clarity Drafter → Rules Register Orchestrator when a drafting session discovers the loaded register is stale, incomplete, or contradicted by the project folder's actual contents — the drafter reports back rather than silently patching around a bad register

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Strength Reason:**
The orchestrator cannot build a register itself — it has no RCE-1 domain logic, only filesystem-scanning and routing logic. Every "no register found, build one" outcome is unusable without this link. Equally, rules-clarity-drafter has no folder-scanning behaviour of its own (it previously assumed drafting starts from a blank project or an already-known SWD) — this link is what gives it real project-awareness rather than operating from chat context alone.

**Direct or Indirect:**
direct

**Chain Position:**
upstream (orchestrator scans and decides → drafter builds → the resulting SWD becomes what arbiter-engine later audits against, per the existing Rules Clarity Drafter → Arbiter Engine contract)

**Reason for Relationship:**
Explicit build decision: the "never assume a register exists, actively push back and help build one" behaviour needed a home that wasn't drafting-time logic (rules-clarity-drafter) or audit-time logic (arbiter-engine) alone, since it has to run *before* either, on real filesystem evidence. Splitting scan/detect/route into its own skill keeps rules-clarity-drafter focused on construction once told to build, rather than also carrying detection logic that belongs to a different moment in the workflow.

**Behavioural Impact:**
Rules-register-orchestrator MUST NOT build SWD content itself — no inventing terms, no filling gaps unasked. It scans, reports what it finds (or doesn't), and routes. Rules-clarity-drafter, once unparked and receiving a routed request, MUST run its SWD-building workflow (which itself delegates to oxford-editorial-indexer per `references/delegation-to-oxford-editorial-indexer.md`) rather than silently proceeding with drafting on an assumed convention.

**Source Update Requirement:**
This file must exist and state the scan/route boundary explicitly. `SKILL.md` Stage 3 must route rather than absorb SWD-construction work.

**Target Update Requirement:**
rules-clarity-drafter's own SKILL.md and RELATIONSHIP_CONTRACTS.md must be updated to record this inbound link and the unparking (see rules-clarity-drafter's own changelog for that update, made in the same session as this file).

**Affected Files:**
`rules-register-orchestrator/SKILL.md`, `rules-register-orchestrator/RELATIONSHIP_CONTRACTS.md`, `rules-clarity-drafter/SKILL.md`, `rules-clarity-drafter/RELATIONSHIP_CONTRACTS.md`

**Audit Status:**
fully applied — both sides present on disk and updated in this session.

---

## Relationship Contract: Rules Register Orchestrator → Arbiter Engine

**Source:**
Rules Register Orchestrator

**Target:**
Arbiter Engine

**Relationship Direction:**
Rules Register Orchestrator → Arbiter Engine (routing dispatch — orchestrator confirms a register exists and hands editing/audit work to arbiter-engine with that register as reference)

**Reciprocal Direction:**
Arbiter Engine → Rules Register Orchestrator at the *start* of any audit task, arbiter-engine should itself first check whether it was invoked directly (bypassing the orchestrator) with no register loaded — in which case arbiter-engine's own behaviour (see Target Update Requirement below) is to perform the same "check for a register, push back if absent" behaviour the orchestrator would have run, rather than assume the orchestrator was always used as the entry point

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Strength Reason:**
Arbiter-engine's SWD lens is meaningfully weaker without a real register to check against — a cold audit with no SWD can still catch some defect classes (precision/aura-vs-tag, agency) from the text alone, but cannot catch inconsistency against a project's own established conventions, which is exactly what the SWD lens is for. This link is what supplies that register reliably rather than leaving arbiter-engine to discover mid-audit that none exists.

**Direct or Indirect:**
direct

**Chain Position:**
downstream of both the orchestrator's scan and (when applicable) rules-clarity-drafter's construction — arbiter-engine is the last stage in the chain: scan → (build if needed) → audit.

**Reason for Relationship:**
Same reasoning as the drafter link: detection/pushback logic belongs before audit-time, not inside it, so arbiter-engine can stay focused on its five diagnostic lenses rather than also carrying folder-scanning logic. But arbiter-engine must not become *unusable* when invoked directly without going through the orchestrator first — hence the reciprocal requirement below, so the standing rule ("never assume a register exists") holds even if a user or a future session calls arbiter-engine directly.

**Behavioural Impact:**
Rules-register-orchestrator MUST NOT perform audit work itself — routing only. Arbiter-engine, when invoked via this orchestrator, uses the supplied register as its SWD-lens reference without re-scanning (the orchestrator has already done that work). Arbiter-engine, when invoked *without* going through this orchestrator, MUST perform its own lightweight version of Stage 1/2 (scan for a register, state plainly if none is found, ask before proceeding) rather than silently auditing with no SWD reference and no explanation of that gap.

**Source Update Requirement:**
This file must state the reciprocal requirement explicitly so it isn't lost. `SKILL.md` Stage 3's arbiter-engine routing line must note the "if arbiter-engine unavailable, say so plainly" fallback.

**Target Update Requirement:**
arbiter-engine's own SKILL.md must gain a Stage 0-equivalent check (scan-or-request-register before running the SWD lens) so it doesn't silently assume a register exists just because it's usually invoked via the orchestrator. As of this build, arbiter-engine is not installed in this environment (confirmed via disk check this session — same result as prior sessions), so this update is recorded as **pending**, same as the existing pending item in `rules-clarity-drafter/RELATIONSHIP_CONTRACTS.md`. Both pending items should be applied together the next time arbiter-engine is opened for edit, since they touch the same Stage-0-equivalent area of that skill.

**Affected Files:**
`rules-register-orchestrator/SKILL.md`, `rules-register-orchestrator/RELATIONSHIP_CONTRACTS.md` — and, once arbiter-engine is next opened for edit, arbiter-engine's own SKILL.md and RELATIONSHIP_CONTRACTS.md.

**Audit Status:**
partially applied — source side complete; target side pending, consistent with the existing pending status recorded in `rules-clarity-drafter/RELATIONSHIP_CONTRACTS.md`.

---

## Relationship Contract: Rules Register Orchestrator → Oxford Editorial Indexer

**Source:**
Rules Register Orchestrator (via Rules Clarity Drafter — see note below)

**Target:**
Oxford Editorial Indexer

**Relationship Direction:**
Rules Clarity Drafter → Oxford Editorial Indexer (the orchestrator routes the *decision* to build a register to rules-clarity-drafter; rules-clarity-drafter is the one that actually calls oxford-editorial-indexer for construction — see `references/delegation-to-oxford-editorial-indexer.md` for the full field-level delegation boundary). Recorded here because the orchestrator is the one that first establishes oxford-editorial-indexer will be needed, even though it isn't the one that calls it directly.

**Reciprocal Direction:**
Oxford Editorial Indexer → Rules Clarity Drafter when its own consistency audit surfaces a Status of `conflicting` or `needs author decision` that has no RCE-1 schema equivalent — reported back for RCE-1-side resolution rather than resolved unilaterally by Oxford (see the Status-field mapping table in `references/delegation-to-oxford-editorial-indexer.md`)

**Relationship Type:**
chain propagation

**Relationship Strength:**
strong

**Strength Reason:**
Without this link, rules-clarity-drafter's SWD-building workflow would need to rebuild glossary/cross-reference/index machinery oxford-editorial-indexer already has, working and tested. The two schemas are not identical (see the field-mapping table), so this is a real, load-bearing translation dependency, not a loose mention.

**Direct or Indirect:**
indirect (orchestrator establishes the need; rules-clarity-drafter is the direct caller)

**Chain Position:**
parallel/supporting — oxford-editorial-indexer is invoked as a construction service within the drafter's SWD-building step, not as a separate stage in the scan→build→audit chain.

**Reason for Relationship:**
oxford-editorial-indexer already declares related-skill links to `wargame-designer` and `professional-technical-writing` in its own frontmatter but had no link to RCE-1, rules-clarity-drafter, or this orchestrator, since none of them existed when it was last written. This contract is the missing link, established from this side per the explicit build decision to delegate rather than duplicate.

**Behavioural Impact:**
Rules-clarity-drafter MUST use the field-mapping table when calling oxford-editorial-indexer, not assume schema compatibility. Oxford-editorial-indexer's output (the glossary/keyword-list document) is a *derived view* of the RCE-1 SWD, never the authoritative source — if the two disagree, the RCE-1 SWD wins and the glossary is regenerated, never the reverse (stated explicitly in the delegation reference to prevent silent authority drift).

**Source Update Requirement:**
`references/delegation-to-oxford-editorial-indexer.md` must exist with the full field mapping (it does, as of this build) and must be kept in sync if either schema changes.

**Target Update Requirement:**
oxford-editorial-indexer's own `skill_links.related_external_skills` frontmatter list should gain `rules-clarity-drafter` and `rules-register-orchestrator` entries, and ideally a short note in its own doctrine referencing the field-mapping table as the authoritative translation when called for RCE-1 SWD construction. As of this build, oxford-editorial-indexer IS present on disk in this environment (confirmed — unlike arbiter-engine), so this update should be applied now rather than left pending.

**Affected Files:**
`rules-register-orchestrator/RELATIONSHIP_CONTRACTS.md`, `rules-register-orchestrator/references/delegation-to-oxford-editorial-indexer.md`, and `/mnt/skills/user/oxford-editorial-indexer/SKILL.md` frontmatter (target update — see note on audit status).

**Audit Status:**
source side complete; target side edited in this session's container (`/mnt/skills/user/oxford-editorial-indexer/SKILL.md` frontmatter now lists both new links) — but this environment's filesystem resets between sessions/tasks per this environment's own stated behaviour, and there is no way to confirm from here whether this edit persists to the user's actual installed copy of oxford-editorial-indexer outside this container. Treat this edit as a **patch to apply**, not a confirmed permanent fix — the user should verify their real installed file reflects this change, or re-apply it, the next time they're working with oxford-editorial-indexer directly.

## Skill Identity

**Author:** TABARC-Code
**Author URL:** https://github.com/TABARC-Code/
**Dewey-style Code:** 003.750
**Classification:** Systems coordination — project-state detection and cross-skill routing
