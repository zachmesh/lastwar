---
unit: scout-midday-hospital-completed-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-26T17:36:07Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T17:42:00Z
window: hospital completed row tier, read only (researcher 17:40z)
est_minutes: 4
serves: snapshot
chain_id: hospital-completed-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T17:42:11Z
lease_until: 2026-11-26T18:02:11Z
result:
  status: done
  started_at: 2026-11-26T17:42:11Z
  finished_at: 2026-11-26T17:45:06Z
  duration_seconds: 175
  executor: operator
  summary: Hospital Lv.25 panel read: Severely Wounded 1,364 of 7,999 (all Lv.10), Completed 5,104 (a full bar; no tier printed), free room 1,531 (unchanged), capacity 7,999; a green Collect and an info icon, neither pressed; closed by the X; HUD unmoved; drags 0. state_change: no. state_read: Hospital Lv.25: wounded 1,364 of 7,999 (Lv.10), Completed 5,104, room 1,531; Collect not pressed | step 8 | 17:43:24Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1743-queue-run.md and 1743-queue-run.csv; run 20261126T174212Z-922229
  state_read: Hospital Lv.25: wounded 1,364 of 7,999 (Lv.10), Completed 5,104, room 1,531; Collect not pressed | step 8 | 17:43:24Z
  state_change: no
  follow_up: the Completed troops' tier is not printed on the panel (the wounded pool is Lv.10)
  stats:
    target: read the Completed row's tier and count
    achieved: read: count 5,104, tier not shown
    resources_gained: none
    points: 0
    costs: none spent; model 0.148348 USD
    verified: yes
    run_id: 20261126T174212Z-922229
    run_steps: 12
    actions_done: 6
    actions_refused: 0
    cost_usd: 0.148348
    device_takeovers: 0
    claims: 0
    wounded: 1364
    completed: 5104
    room: 1531
    capacity: 7999
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off Hospital read (not the midday walk); definition `_activities_/perception-scout/`.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE HOSPITAL COMPLETED ROW, read only; the Researcher 17:40Z; plan reason: the room pricing)

serves: snapshot

HOSPITAL READ APPROVED (Steer A 17:37Z): one building tap on the Hospital by its tag, a plain open, read only. The unit follows any running one.
The Hospital holds healed troops 'Completed' (5,306 on the 11-23 read, 5,104 at 04:45Z, the collect refused): their TIER is unread: if all are Lv.10 the pool is about 8.4M power.
(1) From the base, find the Hospital (tent E about (678,510); a portrait bubble over a barracks may be the Hospital, not a batch; the tag may read Lv.20 or Lv.25): read its tag in a frame (expected 'Hospital Lv.25') and tap only the building that reads Hospital.
(2) Tap the tag's orange middle button ONCE: read by TEXT: capacity, wounded count, free room, and the 'Completed' row: the TIER by level and the COUNT (by tier if several). Write each number with the UTC time (digits cropped at 6x).
(3) NEVER Collect, Heal, Recover, Speed Up or Finish Now: nothing is pressed in the Hospital. Close with the blue back arrow or the X.
(4) Any dialog, price or other app: STOP. `--state-change no`, a `state_read:` line. CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
