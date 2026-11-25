---
unit: building-queues-help-test-r10-2026-11-25-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-25T04:12:21Z
expires_at: 2026-11-25T05:29:51Z
planned_for:
not_before: 2026-11-25T05:01:00Z
window: h118 read at about +10 minutes
est_minutes: 3
serves: PL-08
chain_id: help-test-r10-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 2
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-25T05:29:51Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Oil Well Lv.24 row is gone (finished in the owner's session before 05:25Z), so the help test has no row to request on; the idea moves to the Lv.25 job
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, H118 READ at about +10 minutes, PL-08)

serves: PL-08

H118, THE CLEAN TEST (Steer A 04:10Z; the Coach's priors: the end falls 0.70, by 20 to 35 minutes 0.40; 30 of 30 helps within 30 minutes 0.60). READ ONLY: dispatched about 10 minutes after the help request; nothing is requested or pressed.
Route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md` (the hammer panel). Read the Oil Well Lv.24 entry's time left and write the END in UTC to the second (expected 2026-11-25T07:11:19.6Z, constant within 1 s since 17:31Z) with the UTC time of the read. Also write the helps count ('n of 30') if the row shows one, and how many minutes after the request this is (the request's UTC time is in the record of `building-queues-help-test-2026-11-25-001`). Close the panel by its X.
Cost cap, stated: 0.20 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the reads written, with ONE `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change` yes only if the help request was tapped.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label first. Never Speed Up, Finish Now or any other builder's row.
