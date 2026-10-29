> **Sub-skill of `rules-clarity-drafter`.** Not independently installable — read only when the router (`../../SKILL.md`) directs here. Identifier: `drafting-checklist`.

# Drafting Checklist

Run this before handing back any drafted rule text. It follows RCE-1's rule structure, converted to a pass/fail pass over the actual draft rather than a description of the rules themselves.

## Checklist

1. **Aura-vs-tag (RCE1.1.1):** Does this rule have both a range and a duration? If yes — is it worded with `while` (aura) or `becomes [status] until` (tag)? If neither pattern appears, stop and fix before anything else — this is the highest-cost ambiguity class.
2. **Lexicon (RCE1.2.1):** Does every term used here already exist in the project SWD? If a new term appears, is it genuinely new, or a synonym for something already locked?
3. **Redundant modal (RCE1.2.2):** Search the draft for `must`. For each instance, ask: does removing it change what the sentence instructs? If no, cut it.
4. **Agency (RCE1.3.1):** Do the verbs in this rule match the project's locked agency distribution (player rolls/picks, unit moves/attacks, or whatever was set in Stage 1)? A stray "the unit rolls a d6" in a player-agency project is a defect, not a style choice.
5. **Game terms (RCE1.2.3):** Does this rule use a phrase likely to recur three or more times across the document? If so, is it already a coined term, or should it become one now rather than after the third occurrence?
6. **Keywords (RCE1.2.4):** Does this rule introduce a mechanic other rules will need to reference later? If so, has it been given a keyword and marked with the project's chosen formatting convention?
7. **Keyword Shape (RCE1.2.5):** For every keyword touched by this rule — new or existing — has its Shape been classified (1 bare tag / 2 parameterised / 3 compound phrase / 4 compound-parameterised)? For Shape 2/4 instances, is the variable slot value actually stated at the point of use, not dropped ("its Rapid Fire" with no number is a Shape 2 failure; "an Anti ability" with no category stated is a Shape 4 failure)? For Shape 3 compound phrases, has the rule cited the full locked string rather than a partial or informally-inflected form?
8. **Multi-effect scope (RCE1.1.2):** Does one trigger condition govern more than one effect? If so, is the scope shown structurally (bullets/numbering) rather than left to prose word order?
9. **Header-signpost (RCE1.3.2):** Does this rule contain a clause that only makes sense with unstated context (an edge case, an exploit closure)? If so, does it have a header naming what it addresses, placed before the confusing clause?
10. **SWD sync (RCE1.3.4):** Has every new decision made while drafting this rule (new term, new keyword and its Shape, newly locked phrasing) actually been written into the SWD, not just decided in the moment and left implicit?

## Failure handling

If any check fails, fix it before returning the draft — do not return a draft with a known, named defect and a note saying "you might want to check X." RCE-1 exists so this doesn't happen; running the checklist and reporting the failure back to the user instead of fixing it defeats the point of a drafting-time skill.

If a check is ambiguous (genuinely unclear whether a term is new or a synonym, for instance), say so plainly to the user rather than guessing either direction — consistent with treating a wrong silent guess as worse than a stated uncertainty.
