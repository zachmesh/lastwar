---
unit: building-queues-oil-well-help-2026-11-25-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-25T05:38:39Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-25T05:38:00Z
window: h118 help request on the new oil well lv25 job steer a 05:37z
est_minutes: 4
serves: PL-08
chain_id: oil-well-help-2026-11-25
chain_seq: 1
attempts: 1
max_attempts: 2
claimed_by: operator
claimed_at: 2026-11-26T11:10:04Z
lease_until: 2026-11-26T11:30:04Z
result:
  status: partial
  started_at: 2026-11-26T11:10:04Z
  finished_at: 2026-11-26T11:11:29Z
  duration_seconds: 85
  executor: operator
  summary: Oil Well help request not made: the hammer counter opened the Building Queue; the Oil Well Lv.25 row (Time Left 01:59:27 at 11:10:29.5Z, ends about 13:09:56.5Z) carries only a Speed Up button: no help count, hand glyph or Help control (as at 05:25Z); the timer before and after is not comparable (no gesture); nothing pressed on the rows; drags 0. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1110-queue-run.md and 1110-queue-run.csv; run 20261126T111005Z-a6be62
  state_change: no
  follow_up: retry only if a build shows a help control on the row
  stats:
    target: ask alliance help on the Oil Well build once
    achieved: no help control exists on the row: not requested
    resources_gained: none
    points: 0
    costs: none spent; model 0.092186 USD
    verified: yes
    run_id: 20261126T111005Z-a6be62
    run_steps: 8
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.092186
    device_takeovers: 0
    claims: 0
    oil_well_left: 01:59:27
    oil_well_end_utc: 2026-11-26T13:09:56
    blocker_category: no help control on the Oil Well row
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, H118 HELP REQUEST on the new Oil Well Lv.25 job, PL-08)

serves: PL-08

Steer A 05:37Z (approved gesture). SKIP this unit if the record of `building-queues-oil-well-2026-11-24-005` already holds the request (the operator may have done it inline); say so and close DONE.
(1) Open the hammer panel (route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`). Read the Oil Well entry: its tag must show the Lv.25 job ('Lv.24 to 25'); anything else: STOP and report. Write the builder row's help count ('n of 30') and its END in UTC to the second, with the UTC time.
(2) GUARD: if the row already shows helps before the request, the test is VOID: do NOT press: write the row and close.
(3) Else tap the row's own Help or hand button ONCE (a free cooperative request, the same class as Help All): read its label first: no price, no gem icon, no Go or Buy. Wait 60 seconds, re-read the END and the help count. Close the panel by its X.
Never Speed Up, Finish Now or another builder's row.
Cost cap, stated: 0.25 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the reads written (and the gesture if tapped), with ONE `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change` yes only if the help request was tapped.
Hammer: if one verified tap opens nothing, record the frame and try the second route in the routes table (builders row) once; else STOP and report: never a fourth tap.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
