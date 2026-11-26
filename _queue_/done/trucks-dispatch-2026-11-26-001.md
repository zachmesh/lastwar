---
unit: trucks-dispatch-2026-11-26-001
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-25T22:17:41Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T02:15:00Z
window: trade cycle e first window of the 11-26 day settle and dispatch three and plunder
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T04:43:47Z
lease_until: 2026-11-26T05:03:47Z
result:
  status: partial
  started_at: 2026-11-26T04:43:47Z
  finished_at: 2026-11-26T04:45:44Z
  duration_seconds: 117
  executor: operator
  summary: Cycle E first window: Hospital free room 1,531 (wounded 1,364 of 7,999, Completed 5,104); tram icon NO badge at 04:44:37.1Z and again after one WORLD then BASE (04:45:02.2Z): 'badge absent: no tap'; the trade screen never opened: nothing dispatched, settled or plundered; the different-device dialog never showed; drags 0. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0443-queue-run.md and 0443-queue-run.csv; run 20261126T044348Z-51e480
  state_change: no
  follow_up: the Coordinator re-dispatches after 15 minutes (3 tries at most)
  stats:
    target: settle, dispatch up to three, plunder up to four
    achieved: Hospital room read; badge absent: no tap
    resources_gained: none
    points: 0
    costs: none spent; model 0.154176 USD
    verified: yes
    run_id: 20261126T044348Z-51e480
    run_steps: 12
    actions_done: 6
    actions_refused: 0
    cost_usd: 0.154176
    device_takeovers: 0
    claims: 0
    blocker_category: badge absent: no tap
    hospital_free_room: 1531
    tram_badge: none at both reads
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# trucks

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE E, the 11-26 day, Steer A 22:15Z)

serves: PL-18

Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` (steps 0 to 4, Hospital first) and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. FIRST write the tram badge state AND ITS COUNT with the UTC time, and BOTH tab badges. First window of the 11-26 day: SETTLE every returned truck (cycle C's may still wait: claim Reward Recovery), then DISPATCH into each EMPTY slot, up to THREE (count to 3/5), the downgrade test on the first SR, and PLUNDER up to FOUR with the siege rule (none after 22:00Z): all per the sheet.
NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), read ONCE: lit: enter; dark: close 'badge absent: no tap'. Write the icon state (absent, bare or badge N) and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
