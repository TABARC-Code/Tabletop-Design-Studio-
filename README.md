# Tabletop Design Studio

One Claude skill for designing war games, miniatures games, board games and card games.

Most of my tabletop skills were separate. Each one knew its own corner of the hobby and none of them knew about the others. This repo puts them behind one entry point, `SKILL.md`, which works out what kind of question you have asked and sends you to the right material. The idea is the same as the video game design package I already use, with the engine and screen-side parts taken out.

## What is in it

| Folder | What it holds |
|---|---|
| `SKILL.md` | The entry point. Nine modes, the routing table, the verdict words and the known gaps. |
| `references/hydra/` | Board game design engines: genres, balance, pacing, randomness, mechanic invention, referee rules, playtest method, personas, pipeline and the house writing style. |
| `references/wargame/` | Wargame and miniatures theory, from activation systems and negative feedback through to rules writing and board wargame mechanics. Thirteen modules, lettered A to R with gaps where the source had no module. |
| `references/cards/` | Card game design, modules A to S. Anatomy, resources, factions, balance, expansions, monetisation, refits, rules, playtesting and physical production. |
| `references/playtesting/` | Persona database spec, tester taxonomy, audit rubric, psychology notes and command grammar. |
| `references/rules/` | RCE-1, the rules writing standard. The Standard Wording Document schema, worked examples and the drafting checklist. |
| `references/eurogames/` | Euro-style design and hobby culture, from the eurogames workshop material. |
| `templates/` | Working templates for briefs, prototype packs, rules drafts, component lists, playtest plans, session records and final reports. |
| `data/` | The 380-profile persona pool used for simulated playtesting. |
| `examples/` | A worked playtest report. |
| `contracts/` | The design brief JSON schema. |

The file counts are 9 hydra, 13 wargame, 18 card, 5 playtesting, 9 rules and 10 eurogames references, plus the templates, data and examples.

## How to use it

Put the folder where your skill loader can see it, or open it as a project and point Claude at `SKILL.md`. Then ask the question in plain English. Something like "my wargame's first turn is decided before anyone moves" will do.

You do not need to know which mode your question belongs to. The skill decides, and tells you which mode it chose.

## What I took out

Video game and engine material is gone. That covers the engine specialists, the engine reference docs, the shader and netcode rules, the frame budgets, the scene and asset pipeline and the engine CI scripts. The Game Studios framework I looked at for the gate and status ideas was MIT licensed, and I have copied none of its text.

I also left out the digital card-game module, `Q-digital-ccg.md`. It was all about client UI, ladders and online play, which is not table design.

## Decisions I made without you

You asked for the repo to be built without questions, so I picked defaults. Change any of them.

- Verdict words are PASS, CONCERNS, FAIL and NOT ASSESSED. The sources do not define a shared set, so these are mine.
- Rigor is minimal. The skill asks for the one-page brief and the four hard-gate items before it asks for anything heavier.
- The digital-first case studies in `references/cards/R-ccg-case-studies.md` and the deck-builder notes in `references/cards/S-deck-builder-and-formats.md` are kept as examples. If you want board games only, delete them.

## Known gaps

These are written up in full in the Gaps section of `SKILL.md`. The short version:

- The rules auditing skill that `rules-clarity-drafter` depended on is not in here. Drafting works. Auditing does not exist yet.
- The glossary builder that the rules skill hands its index work to is not in here either.
- Some contract notes still point at the original skill folders. Treat them as history.

## Sources

The wargame material follows the books listed in that skill's source library: George Phillies on wargame design, Glenn Ford and Mike Hutchinson on miniatures design, Rick Priestley and John Lambshead on tabletop wargames, Jack Bickham on scene and structure, and designer notes on Warcry, Spearhead and Inquisitor. The card-game skill and the RCE-1 rules standard are credited to TABARC-Code in their own metadata. The eurogames material comes from a book that the source skill was built from. This repo does not record that book's title or author, so I have not guessed them.

## Licence

MIT. See `LICENSE`.

Author: TABARC-Code
