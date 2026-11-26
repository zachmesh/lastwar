---
unit: scout-midday-hospital-room-before-siege-2026-11-27-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-25T03:17:23Z
expires_at: 2026-11-27T00:55:00Z
planned_for:
not_before: 2026-11-27T00:25:00Z
window: read the hospital free room before the zombie siege of 11-27 01:15z owner schedule unchanged steer a 03:16z
est_minutes: 4
serves: snapshot
chain_id: hospital-room-before-siege-2026-11-27
chain_seq: 1
attempts: 0
max_attempts: 2
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE HOSPITAL FREE ROOM before the siege, read only, Steer A 03:16Z)

serves: snapshot

The owner's zombie siege search runs at 2026-11-27T01:15Z and is NOT delayed (the owner accepted the risk). This unit reads the Hospital's free room 45 minutes before it; the Coordinator tells the owner in one line (Steer B carries it); the plunder casualty guard (free room at least 1,000) stands. 4 steps:
(1) From the base, find the Hospital (tent E about (678,510); a portrait bubble over a barracks may be the Hospital, not a batch; the tag may read Lv.20 or Lv.25): read its tag in a frame and tap only the building that reads Hospital.
(2) Tap the tag's orange middle button ONCE: read the figures by TEXT: capacity, wounded, 'Completed' (healed, waiting: the COUNT; the panel prints no tier). Free room = capacity minus wounded minus Completed. Write each number with the UTC time (digits cropped at 6x).
(3) NEVER Collect, Heal, Recover or Speed Up: nothing is pressed in the Hospital. Close with the blue back arrow.
(4) Any dialog, price or other app: STOP. `--state-change no`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.30 USD.
