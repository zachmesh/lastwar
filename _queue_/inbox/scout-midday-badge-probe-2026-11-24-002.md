---
unit: scout-midday-badge-probe-2026-11-24-002
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T15:29:53Z
expires_at: 2026-11-24T18:40:00Z
planned_for:
not_before: 2026-11-24T18:04:00Z
window: no tap tram badge probe two before the second truck returns at 18:00:30z
est_minutes: 2
serves: PL-18
chain_id: badge-probe-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE TRAM BADGE PROBE TWO: a no-tap read, the Coach's test of 15:29Z)

serves: PL-18

The badge lit (a red 1) at 15:48Z after an 11-minute macOS alert window; the SR of the first dispatch is being settled. The SR of cycle A returns about 18:00:30Z, the UR about 18:46:07Z. With the game in front since the last event: a badge of 1 at about 18:05Z means the return lit it (the SR is back); none means a dot that waits for a foreground regain. TAP NOTHING: no tram tap, no drag, no scroll, no pan. FIRST write the time of the last foreground loss or alert: if one happened in the previous 30 minutes this is NOT a test: close 'probe cannot separate: foreground lost at <time>' (re-dispatched 15 minutes later). 3 steps:
(1) Take one frame of the base screen. If another screen is in front, close it by its back arrow.
(2) CROP the left column from the SAVED frame at 6x (never a zoom action): write the tram icon's badge (present or none) AND ITS COUNT, the pickup and radar badges, the HUD (diamonds, iron, food, coin) and the UTC time.
(3) Close 'probe: badge N' or 'probe: none' (dark: write the clock time; the SR of cycle A is derived back 18:00:30Z: a dark dot after it is data): a dark read is a COMPLETE. Any dialog: touch nothing, take the frame, stop. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
