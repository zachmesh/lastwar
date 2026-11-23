---
unit: harvest-oil-well-2026-11-23-001
regular: harvest
activity: resource-collection
segment: 1
priority: 1
created_at: 2026-11-23T12:59:47Z
expires_at: 2026-11-23T16:00:00Z
planned_for:
not_before: 2026-11-23T13:15:00Z
window: oil well read and collect every eight hours
est_minutes: 6
serves: oil routine for the Base Expansion path
chain_id: oil-well-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# harvest

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Well read and collect, Steer A oil model)

serves: oil routine for the Base Expansion path

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Open the Oil Well by tag text (name and level), read Output per hour, storage and the stored oil, and read the oil counter before. Press Collect once, read the oil counter after, and write the minutes since the last collection. First run: also read the Oil Well upgrade preview (Lv.1 to 2: cost in food, iron, coin and oil, time, power), as the first Base Expansion builder read.

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
