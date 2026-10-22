

# Mechanic Invention Engine

Use this skill when the user asks for **new mechanics** (not just “a new game idea”):
- “invent a mechanic”
- “create a new core loop”
- “design something that hasn’t been done before”
- “mutate this mechanic into something novel”

This skill invents mechanics via **structured disruption of design space** and returns prototype-ready specs.

## Required input (pick at least one)
- A target genre (euro/18xx/4x/puzzle/etc.)
- A target mechanic to mutate (worker placement, deckbuilding, area control, etc.)
- A target experience (tense negotiation, serene optimisation, cinematic chaos, etc.)

If none is provided, ask for exactly one: **genre OR mechanic OR experience**.

---

## 🧠 Meta-skills for mechanic invention (with exercises)

### 1) Constraint Field Manipulation
Every mechanic lives inside constraints:
- Information (hidden/open/partial/decaying)
- Agency (high control vs forced randomness)
- Time (simultaneous/sequential/real-time)
- Resources (scarce/abundant/regenerating)
- Interaction (direct/indirect/none)

**Exercise:** Take *worker placement*. Change only **time structure** (sequential → simultaneous placement). Note the new tension pattern.

### 2) Verb Discovery
Mechanics are built from player verbs. Many designers overuse: place, draw, move, attack.

**Exercise:** List uncommon verbs and turn each into a rule kernel:
rotate, reorder, combine, trade memory, share risk, lock/unlock state.

### 3) System State Transformation
Invent mechanics where the game state mutates structurally:
- map topology shifts
- action spaces evolve
- rules unlock/decay
- resource values fluctuate

**Exercise:** Pick one subsystem (market, map, action spaces) and define a rule that changes its structure every round.

### 4) Decision Topology Design
Design decisions with different geometries:
- Branching (many options diverge)
- Converging (paths merge)
- Cyclical (recurring loop tension)
- Layered (micro affects macro)

**Exercise:** Rewrite a core loop so early micro-choices permanently constrain late-game macro options.

### 5) Tension Source Reassignment
Move pressure between scarcity/uncertainty/social risk/timing.

**Exercise:** Convert an “action scarcity” game into an “information scarcity” game without changing the action count.

### 6) Information Architecture Engineering
Hybridise information states:
- shared hidden info
- delayed revelation
- decaying certainty
- “belief makes it true” (social reality)

**Exercise:** Create a rule where players can act on *imperfect* info and then pay to refine certainty.

### 7) Feedback Loop Engineering
Combine positive and negative feedback in conflict.
Example: growth increases power but reduces flexibility.

**Exercise:** Add a “power vs agility” trade-off loop to an engine builder.

### 8) Time-Scale Layering
Layer fast and slow systems: tactical vs strategic vs campaign mutation.

**Exercise:** Add a slow, irreversible track that is only advanced by fast tactical decisions.

### 9) Player Role Asymmetry Architecture
Go beyond “different powers”: change rule access or information authority.

**Exercise:** Give one role control of *timing windows* or *reveal structure* rather than combat bonuses.

### 10) System Purpose Inversion
Reward decay, loss, or sacrifice instead of accumulation.

**Exercise:** Design a scoring system where spending resources is worth more than saving them.

---

## 🧪 Mechanic invention framework (the pipeline)

1) Pick a known mechanic (or infer from genre).  
2) Change **one axis** (information/time/resource flow/agency/interaction).  
3) Add **one structural mutation** (evolving board, decaying rules, shared hidden info, topology change).  
4) Ensure a new **decision topology** appears (branching/converging/cyclical/layered).  
5) Validate tension and teachability; propose playtests.

---

## Outputs
- **MECHANIC_SEEDS** (3–7 options)
- **ONE_SELECTED_MECHANIC_SPEC** (deep spec for the best seed)
- **RISK_REPORT** (dominant strategy / degeneracy / cognitive load)
- **PLAYTEST_PLAN** (hypotheses + scenarios)

---

## Five invention examples (copy/pasteable seeds)

Each example includes:
- base mechanic
- axis mutation
- structural transformation
- why it creates new decisions
- minimal prototype spec

### Example 1: Shadow Bids (Auction + decaying information)
**Base:** auctions / value revelation  
**Axis mutation:** information becomes less reliable over time  
**Structural transformation:** bids “age” into vaguer categories

**Prototype spec:**
- Components: Lot cards, Bid cards, Aging sleeves (clear→fogged)
- Flow: reveal lot → commit bids → highest wins → next round, non-winners peek at one bid through fogged sleeve (range, not exact)
- Playtest focus: tune fog granularity so tension > frustration

### Example 2: Living Workspaces (Worker placement + evolving action spaces)
**Base:** worker placement  
**Axis mutation:** commit-reveal placement  
**Structural transformation:** used spaces mutate (upgrade/split/lock)

**Prototype spec:**
- When a space is used, place a mutation tile:
  - Upgrade (stronger, adds upkeep)
  - Split (two weaker actions)
  - Lock (closes, spawns a new action elsewhere)
- Playtest focus: prevent runaway “best space” via upkeep/diminishing returns

### Example 3: Debt Draft (Drafting + closed economy pressure)
**Base:** drafting  
**Axis mutation:** closed economy with persistent debt  
**Structural transformation:** picks create liabilities

**Prototype spec:**
- Drafted card has debt (1–3); unpaid debt reduces hand size or actions
- Playtest focus: debt must be scary but not lethal; include relief actions

### Example 4: Fracture Map (Area control + shifting topology)
**Base:** area control/majority  
**Axis mutation:** interaction via topology control, not combat  
**Structural transformation:** regions split/merge by influence thresholds

**Prototype spec:**
- Regions fracture into smaller scoring zones when influence spikes; merge when low
- Playtest focus: predictability of fractures; avoid arbitrary chaos

### Example 5: Memory Lock (Puzzle + shared hidden state)
**Base:** puzzle/logic deduction  
**Axis mutation:** shared-but-hidden info economy  
**Structural transformation:** actions lock info until unlocked

**Prototype spec:**
- Clues under opaque cups; actions to peek/move/lock
- Locking gains points but blocks peeks until unlock cost paid
- Playtest focus: prevent quarterbacking with private peeks + limited sharing

---

## Genre adaptation hints
- Eurogames: tighten numbers, reduce randomness, emphasise opportunity cost
- Ameritrash: add swing events + mitigation, preserve agency
- 18xx: translate mutation into market rules, train roster tempo, liquidity cycles
- 4X: topology shifts become exploration/colonisation; add snowball brakes
- Party: compress rules, turn uncertainty into comedy, short rounds
