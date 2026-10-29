# RCE-1 — Rules Clarity Engine, Standard No. 1

## Part 2: SWD Schema

**Author:** TABARC-Code
**Author URL:** https://github.com/TABARC-Code/
**Status:** Issue 1

---

## 1. Purpose

Part 1 (Writing Rules) states what a compliant rule looks like. This document specifies the **Standard Wording Document** — the register a project maintains to make those rules enforceable rather than aspirational.

Where STE-100's dictionary is global and fixed (approximately 900 approved words, valid across every STE-compliant document regardless of subject), the SWD is **local to one project and grows as that project grows**. This is a structural difference RCE-1 makes deliberately: a tabletop ruleset's vocabulary is inherently project-specific — "pick" versus "select" is not a fact about the English language, it is a fact about one game's house style. RCE-1 does not attempt a global controlled dictionary for a domain with no stable shared vocabulary across projects.

## 2. SWD Entry Schema

Every SWD entry carries six required fields, plus a seventh conditionally required for `keyword` category entries. An entry missing any field its category requires is incomplete and must not be treated as locked.

| Field | Type | Purpose |
|---|---|---|
| **Term** | string | The exact, locked wording — verbatim, including capitalisation |
| **Category** | enum | One of: `lexicon` · `keyword` · `game term` · `mechanic pattern` · `project setting` |
| **Definition** | string | Full meaning, stated once, in full — never abbreviated in the SWD itself even if the term compresses the ruleset's prose |
| **First used** | reference | Where the term entered the document (rule name, section, or page) — traceability, not decoration |
| **Formatting** | enum or null | `italic` · `bold` · `bracket` · `plain` — required for `keyword` category, optional/null for others |
| **Status** | enum | `locked` · `under review` · `deprecated` |
| **Keyword Shape** | enum or null | One of: `Shape 1 (bare tag)` · `Shape 2 (parameterised)` · `Shape 3 (compound phrase)` · `Shape 4 (compound-parameterised)`, per RCE1.2.5. **Required for `keyword` category, must be null for every other category.** For Shape 2 and Shape 4 entries, the Definition field must additionally state each variable slot's legal value range (Shape 2: the numeric slot; Shape 4: both the category slot's closed list and the numeric threshold slot's comparison operator) |

### 2.1 The Register Entry

Per RCE1.3.3, every project's SWD carries exactly one entry of category `project setting` with Term = "Register", recording the drafting-register decision (natural English / mixed / jargon-forward) and a short note on how it was confirmed. This entry is created at the point the register decision is locked and is never duplicated — a project has one register, not one per rule.

## 3. Category Definitions

**`lexicon`** — a controlled choice between English synonyms for an ordinary concept the project needs to name consistently (pick/select/choose; can/may). These are RCE1.2.1 entries. A lexicon entry's Definition field states which synonyms were rejected and why, if a reason beyond "arbitrary but locked" exists.

**`keyword`** — a game term promoted to formatting-marked, mechanically referenceable status per RCE1.2.4. Formatting field is mandatory here, as is Keyword Shape per RCE1.2.5 — every keyword entry states which of the four grammatical shapes it is, since the shape governs what later rules are permitted to do with it (modify, parameterise, cite in part, pluralise). A keyword entry's Definition is the full mechanical rule text the keyword stands in for, not a summary, and for Shape 2/4 entries additionally states each variable slot's legal range per the schema table in §2.

**`game term`** — a coined compression per RCE1.2.3, not (yet) promoted to keyword status. No mandatory formatting. If a game term later needs cross-referencing by other rules, it is promoted to `keyword` category — see §4, Promotion.

**`mechanic pattern`** — a locked structural decision that is not a single term but a recurring pattern, most commonly the project's chosen aura-vs-tag convention for a family of similar effects (RCE1.1.1), or a locked agency distribution (RCE1.3.1). The Term field for a mechanic-pattern entry is a short label ("Standard buff-aura pattern"), and Definition carries the full pattern specification.

**`project setting`** — non-terminological project-level decisions the SWD still needs to record for consistency: the register entry (§2.1), and any other standing decision (e.g. "victory points attributed to armies, not players") that governs multiple rules without being a term in the ordinary sense.

## 4. Maintenance Procedure

1. **Before drafting a new rule**, check every existing entry relevant to the rule's subject matter. Do not re-decide a `locked` term.
2. **When a rule requires a term not yet in the SWD**, decide it once, add the entry at `locked` status (not `under review` — RCE-1 does not treat first-use as provisional; see §5 for the review path), and use the exact locked wording from that point forward.
3. **Promotion:** if a `game term` entry accumulates cross-references from other rules — i.e. other rules start needing to invoke it without re-explaining it — promote it to `keyword` category, add the required Formatting field, and note the promotion in the entry's history (see §6).
4. **At final edit**, cross-reference every rule in the finished document against the complete SWD, line by line. This is the equivalent of STE-100's dictionary check applied to project-specific terminology rather than general vocabulary.

## 5. Revising a Locked Entry

A `locked` entry is not immutable, but revision is not casual. To revise:

1. Set Status to `under review`.
2. State the reason revision is needed (a genuine drafting problem the current term causes — not stylistic preference discovered mid-project).
3. Identify every existing rule using the current wording.
4. Confirm the new wording with whoever is authorising the ruleset before propagating the change.
5. On confirmation, update every affected rule in the same pass, set Status back to `locked`, and log the change (§6).

A `deprecated` entry is retained in the SWD rather than deleted, so historical traceability of why a term was abandoned survives — this matters most for `keyword` entries, where a deprecated keyword may still appear in older expansion material the project has to remain compatible with.

## 6. Change History

Each SWD, being project-specific, maintains its own change history as an appendix to the entry table — not part of RCE-1's own Revision Log (that log tracks changes to the *standard*, not to any one project's SWD). A minimal change-history line records: date, term affected, what changed, and why.

## 7. Minimum Starting SWD

RCE1.2.1 specifies five lexicon decisions required before drafting begins. A new project's SWD is not considered initialised until these five entries exist at `locked` status, plus the register entry from §2.1 — six entries minimum before rule one is drafted.

| Term (example) | Category | Status |
|---|---|---|
| *(selection verb: pick / select / choose — pick one)* | lexicon | locked |
| *(permission modal: can / may — pick one)* | lexicon | locked |
| *(play-surface noun: battlefield / board / table — pick one)* | lexicon | locked |
| *(activity verb: playing a game / fighting a battle — pick one)* | lexicon | locked |
| *(victory attribution: player wins / army wins — pick one)* | lexicon | locked |
| Register | project setting | locked |

See **Part 3: Worked Examples** for a complete populated SWD table drawn from a real drafting sequence, not placeholder rows.

## Revision Log

| Issue | Date | Change |
|---|---|---|
| Issue 1 | 2026-09-23 | First publication. Schema, five categories, maintenance and revision procedure, minimum-starting-SWD requirement. |
| Issue 1 (revised) | 2026-09-23 | Added Keyword Shape as a seventh field, mandatory for `keyword` category entries, null elsewhere — codifies RCE1.2.5's four keyword grammatical shapes into the schema so a keyword entry states not just its formatting but its permitted usage grammar. |
