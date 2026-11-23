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
serves: PL-17
chain_id: oil-well-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T15:32:59Z
lease_until: 2026-11-23T15:52:59Z
result:
  status: partial
  started_at: 2026-11-23T15:32:59Z
  finished_at: 2026-11-23T15:35:59Z
  duration_seconds: 180
  executor: operator
  summary: OIL panel (top-bar barrel icon) Collect pressed once: Available 3760 to 0, owned 647,039 to 650,799 (+3,760), output 1.2K per hour, oil counter 647.0K to 650.7K, first collection (accrual about 188 minutes, started about 12:26Z [G]); the Oil Well tag, storage and the Lv.1 to 2 upgrade preview were not read: the building is not located and the panel shows no name, level or storage; Details, the Go rows and the offer pack not pressed; blocked by route
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/resource-collection/1534-queue-run.md and 1534-queue-run.csv; run 20261123T153410Z-ded5d6
  follow_up: next oil collect about 23:30Z (eight hours after 15:34Z) by the same panel route; a locate unit for the Oil Well building (tag, storage, Lv.1 to 2 preview) needs Steer A's word on pressing the panel's Details button (its effect is unrecorded) or a base scan
  stats:
    target: read the Oil Well panel and collect once; first run: tag, storage and the Lv.1 to 2 upgrade preview
    achieved: collect done (+3,760 oil, counter 647.0K to 650.7K, 1.2K/H); tag, storage and preview not read
    resources_gained: oil 3,760
    points: 0
    costs: none spent; model 0.060045 USD
    verified: yes
    blocker_category: f missing precondition (the Oil Well building is not located; the panel shows no tag text)
    run_id: 20261123T153410Z-ded5d6
    run_steps: 4
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.060045
    device_takeovers: 0
    rules_used: 4,5,10
    rule_failed: none
    rule_gap: no record locates the Oil Well building or says what the OIL panel's Details button opens
  stats_missing: []
  stats_warnings: []
---

# harvest

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Well read and collect, Steer A oil model)

serves: PL-17

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Open the Oil Well by tag text (name and level), read Output per hour, storage and the stored oil, and read the oil counter before. Press Collect once, read the oil counter after, and write the minutes since the last collection. First run: also read the Oil Well upgrade preview (Lv.1 to 2: cost in food, iron, coin and oil, time, power), as the first Base Expansion builder read.

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
