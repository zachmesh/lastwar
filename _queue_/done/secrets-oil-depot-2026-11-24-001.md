---
unit: secrets-oil-depot-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 3
priority: 2
created_at: 2026-11-23T12:59:52Z
expires_at: 2026-11-24T05:00:00Z
planned_for:
not_before: 2026-11-24T02:05:00Z
window: oil depot secret start
est_minutes: 6
serves: PL-17
chain_id: oil-depot-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T03:34:33Z
lease_until: 2026-11-24T03:54:33Z
result:
  status: done
  started_at: 2026-11-24T03:34:33Z
  finished_at: 2026-11-24T03:36:28Z
  duration_seconds: 115
  executor: operator
  summary: Mega Deploy sent the UR Capture the Oil Depot task with the others: Mega Deploy 03:35:02.460Z, Perform Now 03:35:16.130Z; the Oil Depot card reads 04:00:10 at 03:35:36.5Z so its claim is due about 07:35:46Z; nothing else touched
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/0334-queue-run.md and 0334-queue-run.csv; run 20261124T033433Z-4c9951
  follow_up: claim the Oil Depot about 07:35:46Z (after the 07:30Z sequence stop, before the 08:00Z quiet window); the two refugee tasks about 04:35Z and Rescue Missing Agent about 05:36Z
  stats:
    target: start the Oil Depot secret, write the start time to the second
    achieved: started at 03:35:16.130Z, claim due about 07:35:46Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.13417 USD
    verified: yes
    run_id: 20261124T033433Z-4c9951
    run_steps: 11
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.13417
    device_takeovers: 0
    deploy_utc: 03:35:16.130
    oil_claim_due: 07:35:46
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# secrets

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: oil routine for the Base Expansion path

## Brief (planner, Oil Depot secret start, Steer A oil model)

serves: PL-17

Oil model and routine: `_records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md`. Start the Oil Depot secret (30K oil once a day): open Secret Missions, find the Oil Depot task, read whether it is available and whether today's 30K is already paid, and dispatch it as the Secrets unit does; write the start time to the second, because the claim is due four hours later. Use the method in `_records_/2026-11-22/secret-missions/2049-queue-run.md`; no Plunder Others, no Mega Refresh, no diamonds, no speed-up.

Limits: collect and claim only; no purchase, speed-up or diamonds. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. Tag text beside every number, none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
