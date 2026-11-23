---
unit: secrets-oil-depot-2026-11-23-001
regular: secrets
activity: secret-missions
segment: 3
priority: 2
created_at: 2026-11-23T12:59:50Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T13:30:00Z
window: oil depot secret start
est_minutes: 6
serves: PL-17
chain_id: oil-depot-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T14:06:57Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Oil Depot secret pays 30K oil once a day and today's was claimed at 08:51:08Z (record of secrets-2026-11-23-0742)
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# secrets

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Depot secret start, Steer A oil model)

serves: PL-17

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Start the Oil Depot secret (30K oil once a day): open Secret Missions, find the Oil Depot task, read whether it is available and whether today's 30K is already paid, and dispatch it as the Secrets unit does; write the start time to the second, because the claim is due four hours later. Use the method in `_records_/2026-11-22/secret-missions/2049-queue-run.md`; no Plunder Others, no Mega Refresh, no diamonds, no speed-up.

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
