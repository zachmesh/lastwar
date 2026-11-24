---
unit: scout-midday-pickup-bubble-tap-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T22:27:26Z
expires_at: 2026-11-24T22:32:01Z
planned_for:
not_before: 2026-11-24T22:30:00Z
window: one tap on the question mark bubble beside the pickup icon held for steer a
est_minutes: 3
serves: snapshot
chain_id: pickup-bubble-tap-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 1
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T22:32:01Z
  duration_seconds: 
  executor:
  summary: retired by the planner: Steer A cancelled the tap at 22:30Z (the bubble is the survivors gate's ambient figure, three earlier taps gave a speech bubble only)
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE PICKUP-ICON '?' BUBBLE: ONE tap, read only, approved by Steer A 22:29Z)

serves: snapshot

Facts [M]: a white speech bubble with a black '?' and no text sits beside the pickup icon at about (145,649); seen at 20:19Z, 21:21Z and 22:21Z: a standing state. ONE RUN. 5 steps:
(1) A frame BEFORE with the UTC time: write the bubble's position, the pickup icon's state and the tram icon state (the left-column log).
(2) Tap the BUBBLE ONCE (not the pickup icon itself).
(3) A frame AFTER. Read the surface by TEXT only: what it is called, what it offers, every button label, any price line.
(4) NOTHING is accepted, claimed, confirmed, sent or purchased here. ANY price, gem or diamond icon, Buy, Go, share, link, web view, another app or banner: close it by its X or the blue back arrow and STOP: no second tap. If it is an ordinary survivor or pickup prompt, say so and what the accept would do (a later unit).
(5) Close by the back arrow if a surface opened. `--state-change no`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
