---
unit: trucks-plunder-scan-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T16:33:57Z
expires_at: 2026-11-24T03:10:00Z
planned_for:
not_before: 2026-11-24T02:30:00Z
window: one plunder scan after the reset
est_minutes: 6
serves: PL-18
chain_id: plunder-scan-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T02:30:41Z
lease_until: 2026-11-24T02:50:41Z
result:
  status: partial
  started_at: 2026-11-24T02:30:41Z
  finished_at: 2026-11-24T02:40:21Z
  duration_seconds: 580
  executor: operator
  summary: Closed partial after a foreground switch: the trade icon is present again, the hospital guard read free room 1,329, and macOS UserNotificationCenter came to the front at 02:34:19Z after the one tap at 02:34:16.5Z; no scan, no fight
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0230-queue-run.md and 0230-queue-run.csv; run 20261124T023408Z-ddf387
  follow_up: hold for the answer on UserNotificationCenter; the trade icon is not tapped again; scans 002 to 008 wait
  stats:
    target: one scan, one fight, per the unit, after the casualty guard
    achieved: guard read (free room 1,329), trade icon present, scan not run
    resources_gained: none
    points: 0
    costs: none spent; model 0.188 USD
    verified: yes
    run_id: 20261124T023408Z-ddf387
    run_steps: 5
    actions_done: 10
    actions_refused: 0
    cost_usd: 0.188
    device_takeovers: 0
    blocker_category: f missing precondition (foreground switch to UserNotificationCenter after the trade icon tap at 02:34:16.5Z)
    free_room: 1329
    rules_used: 1,10
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ONE plunder scan, 30 minutes apart from the 02:00Z reset)

serves: PL-18

OD-20261123-20: TRADE TRUCKS ONLY; no other PvP. Look ONCE, never loop. Read the Plunder Count first; STOP at 4 of 4.

1. Intercity Trade, Others' Trucks: read the list once, no refresh unless its button reads Free.
2. TARGET: a gold (UR) or purple (SSR) truck, a UR 500-badge stack in EITHER half, guard under Squad 1 (25.61M), arrival over 30 minutes away. Four fights: x9, x3 of 6, 0 of 6, x6 of 9: the half does not decide. PREFER the card with the MOST shards; the opened card decides.
3. With a target: CASUALTY GUARD first: read the Hospital Lv.25 figures behind its tag's orange middle button (free room = 7,999 minus wounded minus 'Completed'; 1,329 at 02:07Z, wounded 1,364); STOP under 1,000: 'blocked by capacity: hospital room'. Never Collect, Heal or Speed Up. Quick Plunder once, Battle once: ONE fight per unit.
4. Per fight record: shards won; per item the share of the cargo taken; the card's shard count and stack slots; troops wounded; the count; Total Power. Two fights in a row each wounding over 100: write a stop.

If another scan finished under 15 minutes ago, close this one skipped: 'too soon'.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report.
The trade icon (107,580) has been ABSENT since 16:39Z: look for it first (the 02:00Z reset may return it); if absent, close 'blocked by route: trade icon absent' with the frame.
Cost cap, stated: 0.40 USD.
