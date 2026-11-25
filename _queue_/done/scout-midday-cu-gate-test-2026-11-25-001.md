---
unit: scout-midday-cu-gate-test-2026-11-25-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T11:49:30Z
expires_at: 2026-11-25T11:40:00Z
planned_for:
not_before: 2026-11-25T11:28:30Z
window: one short read request inside the possible nightly cu gate window
est_minutes: 4
serves: snapshot
chain_id: cu-gate-test-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at: 
  finished_at: 2026-11-25T14:01:05Z
  duration_seconds: 
  executor: 
  summary: window passed before execution
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

## Brief (planner, ONE SHORT READ inside the possible nightly cu gate window, the Coach's test CK1)

serves: snapshot

A plain read the operator knows, no new surface: open the Oil Well builders panel (the hammer panel entry), read the entry's time left, the oil counter and Total Power, close the panel. NO tap beyond opening and closing it; no drag. 4 steps, one run.
WRITE: the wait before the run's first click exactly as the bridge prints it and whether it says DESKTOP BUSY (the cu lock is held by a NIGHTLY run, seen once at 11:28:44Z on 11-24 (about 2.4 minutes), and by unpredictable PR gate runs: this request is the test of the nightly; a wait of about 2.4 minutes is expected and is NOT a fault); `owner_idle_seconds`; the entry's time left, the oil counter and Total Power with tag text and the UTC time. Any dialog: answer nothing, stop and tell the Coordinator. FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
