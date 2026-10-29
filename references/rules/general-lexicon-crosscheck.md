> Reference module of `rules-register-orchestrator`. Read when a project's SWD is being built or checked and the general wargaming design lexicon is available to cross-reference against.

# General Lexicon Crosscheck

## What this is

Separately from any single project's SWD, this ecosystem maintains a general wargaming design lexicon (`wargaming_design_lexicon_v11.xlsx` or its current version) — a cross-system, cross-genre register of widely-used tabletop design terminology, independently sourced and verified. It answers a different question than a project's own SWD: not "what does *this* game call this concept" but "what do tabletop games in general call this *kind* of concept."

This module governs how the two inform each other without either overriding the other.

## The direction that matters: general lexicon informs, project SWD governs

A project's own locked SWD entry is always authoritative for that project's actual rules text — this is non-negotiable and mirrors the standing rule that RCE-1's SWD is per-project by design (see `rce-1-swd-schema.md` §1), not global. The general lexicon is never used to silently override or auto-populate a project's SWD entry.

What the general lexicon *is* for:

1. **Flagging convergence.** When a project's drafter is about to coin a new keyword or game term, checking the general lexicon first shows whether tabletop design already has a widely-recognised term for that concept. This is offered as information, not imposed as a requirement — the author may still prefer their own coinage for flavour, differentiation, or IP reasons, but they should get to make that choice knowingly rather than accidentally reinventing "Devastating Wounds" under a different name with no idea it's a common pattern.
2. **Flagging genuine ambiguity risk.** If a project's chosen term already carries a strong, different meaning in the general lexicon (e.g. using "Overwatch" for something that isn't a reactive-fire mechanic, when the term is near-universally associated with one), that's worth surfacing — players arriving from other systems may bring the wrong expectation.
3. **Grounding Keyword Shape classification (RCE1.2.5).** The general lexicon's `Mechanical role` and `Typical value / unit` columns are useful evidence for classifying a new project keyword's Shape — a term the lexicon already records as parameterised (e.g. anything logged with a `Typical value / unit` of "X" or a numeric slot) is good corroborating evidence the project's equivalent term is Shape 2 or Shape 4, not an assumption made from the project term alone.

## The crosscheck procedure

When `rules-clarity-drafter` is about to lock a new SWD entry for a project (per RCE-1's maintenance procedure, Part 2 §4):

1. Search the general lexicon's `Term` and `Aliases / Related labels` columns for the concept being named (not necessarily the exact string — search by the mechanic being described, since the project may be using different wording for the same concept).
2. If a match exists, surface it to the author in one line: what the general lexicon calls it, which systems use that term (`Example systems` column), and ask whether they want to align, diverge deliberately, or proceed without comment. Do not block on this — it's advisory, and the author's answer (including "doesn't matter, keep my term") is recorded and respected, not re-litigated.
3. If no match exists, proceed with the project's coinage as normal — an absence from the general lexicon is not itself a defect; plenty of good project-specific terms are legitimately novel.
4. Whatever the outcome, the project's own SWD entry is written as the author decided — this procedure never substitutes lexicon text for the author's own definition.

## What does NOT flow back into the general lexicon automatically

A project's coined terms are not added to the general lexicon as part of this crosscheck. The general lexicon's own research and intake process (the v11 taxonomy-repair and backlog-verification work) is separate, deliberately more rigorous (source-verified against published rulebooks, not a single project's internal drafting session), and governed by its own README and maintenance log. If a project's term is genuinely novel and well-evidenced enough to be worth adding to the general register, that's a distinct, explicit request to make — not an automatic side effect of drafting one game's rules.
