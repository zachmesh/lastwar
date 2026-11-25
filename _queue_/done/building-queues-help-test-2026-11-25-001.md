---
unit: building-queues-help-test-2026-11-25-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-25T04:12:19Z
expires_at: 2026-11-25T06:20:00Z
planned_for:
not_before: 2026-11-25T04:50:00Z
window: h118 help request and reads: before and +1 minute
est_minutes: 5
serves: PL-08
chain_id: help-test-2026-11-25
chain_seq: 1
attempts: 1
max_attempts: 2
claimed_by: operator
claimed_at: 2026-11-25T05:25:04Z
lease_until: 2026-11-25T05:45:04Z
result:
  status: partial
  started_at: 2026-11-25T05:25:04Z
  finished_at: 2026-11-25T05:28:15Z
  duration_seconds: 191
  executor: operator
  summary: Help test void: blocked by route: the builders panel has no Oil Well row (the Oil Well Lv.24 upgrade, expected end 07:11:19.6Z, finished before 05:25Z) and no help control on any row; one builder idle (Construct); Lv.26 Drill Ground 08:13:10 left (ends 13:38:35.8Z), Lv.27 4d 20:05:36, Lv.28 8d 18:24:48; no help tapped; drags 0. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0525-queue-run.md and 0525-queue-run.csv; run 20261125T052504Z-53fcc0
  state_change: no
  follow_up: the idle builder waits (the Oil Well chain's next step); units 2 and 3 of the test have nothing to read
  stats:
    target: request help on the Oil Well row and read the end before and after
    achieved: no Oil Well row: test void
    resources_gained: none
    points: 0
    costs: none spent; model 0.149623 USD
    verified: yes
    run_id: 20261125T052504Z-53fcc0
    run_steps: 13
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.149623
    device_takeovers: 0
    claims: 0
    blocker_category: route: no Oil Well row, the upgrade finished
    slots_idle: 1
    tram_badge: icon drawn without a badge
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, H118 HELP REQUEST on the Oil Well Lv.24, PL-08)

serves: PL-08

H118, THE CLEAN TEST (Steer A 04:10Z). This unit REQUESTS the help and reads the end BEFORE and 1 minute after.
(1) Route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md` (the hammer panel). Read the Oil Well Lv.24 entry's time left; write the END in UTC to the second (expect 07:11:19.6Z) and the UTC time: the BEFORE read.
(2) On that row write the helps count ('n of 30') if shown: if it already shows helps or a request, do NOT tap: STOP 'test void: a request exists' and write the row. Else find the plain Help request control: read its label by TEXT or glyph in a frame; tap it ONCE only if it is a plain request with no price, no gem icon, no Go or Buy; write the UTC time of the tap and the row after. Absent or other: STOP 'blocked by route', write the row.
(3) Wait 60 seconds, re-read the end as in (1), and the helps count: the +1 read. Close it by its X.
Cost cap, stated: 0.25 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the reads written, with ONE `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change` yes only if the help request was tapped.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label first. Never Speed Up, Finish Now or any other builder's row.
