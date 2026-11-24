---
unit: research-slot-read-labs-2026-11-24-001
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T13:35:25Z
expires_at: 2026-11-24T04:35:00Z
planned_for:
not_before: 2026-11-24T02:30:00Z
window: labs read tonight idle slots blocker named
est_minutes: 8
serves: PL-04
chain_id: slot-read-labs-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T04:10:02Z
lease_until: 2026-11-24T04:30:02Z
result:
  status: done
  started_at: 2026-11-24T04:10:02Z
  finished_at: 2026-11-24T04:12:09Z
  duration_seconds: 127
  executor: operator
  summary: Both labs busy (Food Output V 13:19:31 left, ends 2026-11-24T17:29:55Z; Iron Output V 22:28:32 left, ends 2026-11-25T02:38:56Z); Finish Now clock = bar plus 10 s; none idle; nothing pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/research-queue/0410-queue-run.md and 0410-queue-run.csv; run 20261124T041002Z-1b41f4
  follow_up: Food Output V completes 17:29:55Z on 2026-11-24, Iron Output V 02:38:56Z on 11-25; the brief's Coin Output V is not in a lab
  stats:
    target: read both labs to the second and the Finish Now clock
    achieved: both labs and both Finish Now clocks read
    resources_gained: none
    points: 0
    costs: none spent; model 0.144013 USD
    verified: yes
    run_id: 20261124T041002Z-1b41f4
    run_steps: 12
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.144013
    device_takeovers: 0
    slots_idle: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (planner, labs read tonight, conformance alarm, Steer A flip plan)

serves: PL-04

Refresh the lab read. Open the flask icon (with both labs busy it shows only the Research Queue list: that is enough): for each lab write the node tag text, level, time left to the second and whether it is busy or idle (Coin Output V in lab 2 ends about 2026-11-24T14:59:10Z, Food Output V in lab 1 about 17:29:58Z). Read the oil counter and write it with the UTC time. `slots_idle` is the TOTAL idle labs.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; follow it (the safe tap is the bare spot (310,660), not (400,640) after a camera shift; never WORLD with a menu open low). If a slot is idle and the cause is the full Drill Ground, write exactly 'blocked by capacity: Drill Ground Full' with the building's tag text (name and level above it after the tap) and record it in the closing `queue.py complete` line as `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (the blocker text at most 40 characters; a count with no blocker named exempts nothing; the count is capped at the open slots); `--stat slots_idle=<N>` is the TOTAL number of open slots, INCLUDING the blocked ones; the blocked count is a subset of it (the tool subtracts it). A TIPS dialog about another device: STOP and report, never Confirm. Read only: never Upgrade, Research, Train, Collect, Promote, Speed Up or Finish Now. Tag text beside every number; none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
