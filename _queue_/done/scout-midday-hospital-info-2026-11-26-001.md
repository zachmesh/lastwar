---
unit: scout-midday-hospital-info-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-26T17:52:55Z
expires_at: 2026-11-26T17:56:28Z
planned_for:
not_before: 2026-11-26T17:58:00Z
window: hospital info button read (steer a 17:51z)
est_minutes: 4
serves: snapshot
chain_id: hospital-info-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-26T17:56:28Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the coordinator ran the 'i' read as part two of the hospital-completed unit (perception-scout/1752): the popup prints only the wounded-treatment instructions, no tier or count; the tier is read by the Lv.10 count's rise at the conveyor's Hospital step
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off Hospital 'i' read (not the midday walk); definition `_activities_/perception-scout/`.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE HOSPITAL 'i' BUTTON, read only: Steer A 17:51Z 'info button approved'; plan reason: the room pricing)

serves: snapshot

The Hospital panel prints 5,104 'Completed' troops and NO tier (the 17:43Z read): the tier is unread; the wounded pool is one Lv.10 tile.
(1) From the base, find the Hospital (tent E about (678,510); a portrait bubble over a barracks may be the Hospital, not a batch): read its tag in a frame (expected 'Hospital Lv.25') and tap only the building that reads Hospital.
(2) Tap the tag's orange middle button ONCE: write capacity, wounded, Completed and free room BY TEXT.
(3) Tap the 'i' (info) button beside the green Collect ONCE: read what opens BY TEXT (the tier of the Completed troops if it prints one: every line). Close it by the X or the back arrow, then the panel by the blue back arrow.
(4) NEVER press the green Collect, Heal, Recover, Speed Up or Finish Now: nothing is pressed in the Hospital except the 'i'. A price or any other dialog: close it by its X and STOP. CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the 'i' read (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
