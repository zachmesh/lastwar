---
unit: harvest-oil-well-2026-11-23-002
regular: harvest
activity: resource-collection
segment: 1
priority: 2
created_at: 2026-11-23T12:59:48Z
expires_at: 2026-11-24T00:30:00Z
planned_for:
not_before: 2026-11-23T21:30:00Z
window: oil well read and collect every eight hours
est_minutes: 6
serves: PL-17
chain_id: oil-well-2026-11-23
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T21:49:38Z
lease_until: 2026-11-23T22:09:38Z
result:
  status: done
  started_at: 2026-11-23T21:49:38Z
  finished_at: 2026-11-23T21:55:18Z
  duration_seconds: 340
  executor: operator
  summary: Oil panel Collect once: available 658,759 to 0, owned 658.7K to 662.9K (+4,220 in 3.5 hours since the 18:19Z collect), output 1.2K an hour; Details and Go not pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/resource-collection/2149-queue-run.md and 2149-queue-run.csv; run 20261123T214938Z-83f499
  follow_up: next collect about 8 hours after 21:50Z (the storage cap is not shown); the oil counter is 662.9K
  stats:
    target: collect the oil once by the oil panel route and read before and after
    achieved: +4,220 oil collected
    resources_gained: oil +4,220
    points: 0
    costs: none spent; model 0.090269 USD
    verified: yes
    run_id: 20261123T214938Z-83f499
    run_steps: 7
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.090269
    device_takeovers: 0
    oil_gain: 4220
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# harvest

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Well read and collect, Steer A oil model)

serves: PL-17

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Collect by the OIL PANEL route measured on 2026-11-23 (the top-bar barrel icon; the Oil Well building is not located yet, so there is no tag to read): read Available, owned and the output per hour (1.2K at 15:34Z), press Collect ONCE, read them again and the oil counter, and write the minutes since the last collection (the second collection, due about 23:30Z (eight hours after 15:34Z)). Do NOT press the panel's Details button: its effect is unrecorded and needs Steer A's approval first. 

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
