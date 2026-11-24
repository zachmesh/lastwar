---
unit: harvest-oil-well-2026-11-23-003
regular: harvest
activity: resource-collection
segment: 1
priority: 2
created_at: 2026-11-23T12:59:49Z
expires_at: 2026-11-24T09:00:00Z
planned_for:
not_before: 2026-11-24T05:30:00Z
window: oil well read and collect every eight hours
est_minutes: 6
serves: PL-17
chain_id: oil-well-2026-11-23
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T05:30:06Z
lease_until: 2026-11-24T05:50:06Z
result:
  status: done
  started_at: 2026-11-24T05:30:06Z
  finished_at: 2026-11-24T05:31:24Z
  duration_seconds: 78
  executor: operator
  summary: Collect once on the oil panel: available 2,352 to 0, owned 671,633 to 673,985 in 111.9 minutes since the 03:38:55Z collect (1.26K an hour, the Oil Well Lv.21); drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/resource-collection/0530-queue-run.md and 0530-queue-run.csv; run 20261124T053006Z-1c0377
  follow_up: the next oil collect about 07:30Z (the Oil Well Lv.22 completes 08:01:45Z)
  stats:
    target: collect the oil once, read the counter before and after
    achieved: +2,352 oil
    resources_gained: none
    points: 0
    costs: none spent; model 0.098744 USD
    verified: yes
    run_id: 20261124T053006Z-1c0377
    run_steps: 8
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.098744
    device_takeovers: 0
    oil_gain: 2352
    drags_tried: 0
    drags_cancelled: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# harvest

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Well read and collect, Steer A oil model)

serves: PL-17

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Collect by the OIL PANEL route measured on 2026-11-23 (the top-bar barrel icon; the Oil Well building is not located yet, so there is no tag to read): read Available, owned and the output per hour (1.2K at 15:34Z), press Collect ONCE, read them again and the oil counter, and write the minutes since the last collection (the third collection, due about 07:30Z). Do NOT press the panel's Details button: its effect is unrecorded and needs Steer A's approval first. 

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
