---
unit: building-queues-heal-preview-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T02:31:45Z
expires_at: 2026-11-24T07:50:00Z
planned_for:
not_before: 2026-11-24T02:45:00Z
window: read only the heal preview for the wounded no heal collect or speed up
est_minutes: 10
serves: PL-09
chain_id: heal-preview-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T04:57:10Z
lease_until: 2026-11-24T05:17:10Z
result:
  status: partial
  started_at: 2026-11-24T04:57:10Z
  finished_at: 2026-11-24T04:58:39Z
  duration_seconds: 89
  executor: operator
  summary: Closed blocked by prerequisite: the Heal preview needs a press: the Hospital Lv.25 panel shows Severely Wounded 1,364 of 7,999, Completed 5,306, free room 1,329 and no heal cost, time or speed-up line, no Heal button; nothing pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0457-queue-run.md and 0457-queue-run.csv; run 20261124T045710Z-5911c1
  follow_up: the info icon and any Heal route stay unread; the Strategist decides whether a press is allowed
  stats:
    target: read the heal cost, time and speed-up line without pressing Heal
    achieved: not shown without a press: closed blocked
    resources_gained: none
    points: 0
    costs: none spent; model 0.112763 USD
    verified: yes
    run_id: 20261124T045710Z-5911c1
    run_steps: 9
    actions_done: 8
    actions_refused: 0
    cost_usd: 0.112763
    device_takeovers: 0
    blocker_category: f missing precondition (the Heal preview needs a press: no cost, time or speed-up line shown)
    free_room: 1329
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-09

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the Heal preview for the 1,364 wounded, Steer A)

serves: PL-09

EXIT PLAN. PRESSED: only the Hospital (tent E about (678,510), tag text Hospital Lv.25) and the orange middle button of its tag, which show the wounded figures (as in `_records_/2026-11-22/building-queues/0205-queue-run.md`). NEVER PRESSED: Heal, Collect, Speed Up, Buy, Use, or any confirm button. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.

Read what the Hospital panel shows WITHOUT pressing Heal: the cost to heal the 1,364 (each resource and amount), the heal time, any speed-up use line, the free room (1,329 at 02:07Z) and the Severely Wounded and Completed counts. If no cost, time or speed-up line shows without pressing Heal, STOP: close 'blocked by prerequisite: the Heal preview needs a press' and write what is visible; do not press. Never Collect: it is all-or-nothing and the healed pile waits behind the same Drill Ground Full.

Up to two runs, 10 steps each. Tag text beside every number; none means [G].
Cost cap, stated: 0.40 USD per run.
