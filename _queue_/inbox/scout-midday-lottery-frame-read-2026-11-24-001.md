---
unit: scout-midday-lottery-frame-read-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T19:46:36Z
expires_at: 2026-11-24T20:45:00Z
planned_for:
not_before: 2026-11-24T20:15:00Z
window: one read only frame of the game window to see whether the lottery loading screen cleared by itself
est_minutes: 2
serves: snapshot
chain_id: lottery-frame-read-2026-11-24
chain_seq: 1
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

## Brief (planner, THE LOTTERY FRAME READ: one read-only frame at 20:15Z, Steer A's option B)

serves: snapshot

Facts [M] (operator, 19:45Z): the Thanksgiving Lottery has been a full-window loading screen since 19:29:18Z (an orange machine, a red draw button, no controls, no back arrow); one tap at (175,930) changed nothing; a toast still drew: the game is alive. THIS UNIT TAPS NOTHING: no key, no scroll, no click, never the red draw button. 3 steps:
(1) ONE frame of the game window; write the UTC time and what it shows: the base, the lottery page, or still the loading screen.
(2) If the base is visible: write the HUD (food, iron, coin, oil, diamonds, Total Power), the tram icon state (absent, bare or badge N), and any toast or dialog.
(3) If STILL the loading screen: close 'still loading at <time>' and DO NOT TAP. `--state-change no`, a `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
