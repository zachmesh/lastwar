---
unit: scout-midday-bridge-supervised-read-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T08:18:43Z
expires_at: 2026-11-24T09:30:00Z
planned_for:
not_before: 2026-11-24T08:35:00Z
window: first supervised read only run after the bridge restart owner idle seconds and every dialog
est_minutes: 4
serves: snapshot
chain_id: bridge-supervised-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T08:45:23Z
lease_until: 2026-11-24T09:05:23Z
result:
  status: done
  started_at: 2026-11-24T08:45:23Z
  finished_at: 2026-11-24T08:46:39Z
  duration_seconds: 76
  executor: operator
  summary: First supervised run on the new bridge tree: owner_idle_seconds=300 (source: default), lock admitted in 0.7 s (wait 0), no dialog or consent request, Oil Well Lv.22 to 23 08:41:47 left (ends 17:27:27.4Z), oil 675.1K, Total Power 150,051,860, run commit b52c84ba391e clean; no drag
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0845-queue-run.md and 0845-queue-run.csv; run 20261124T084523Z-158d7c
  follow_up: my scripts' status parsing needs the new format (bridge.runs, status --run-id); the Oil Well Lv.23 ends 17:27:27.4Z
  stats:
    target: the first supervised read after the bridge restart
    achieved: read, nothing odd except a control-link line and the status format
    resources_gained: none
    points: 0
    costs: none spent; model 0.073156 USD
    verified: yes
    run_id: 20261124T084523Z-158d7c
    run_steps: 6
    actions_done: 5
    actions_refused: 0
    cost_usd: 0.073156
    device_takeovers: 0
    owner_idle_seconds: 300
    wait_before_first_click_s: 0
    dialogs: 0
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE FIRST SUPERVISED READ-ONLY RUN after the bridge restart at 09:10Z)

serves: snapshot

A plain read the operator knows, no new surface: open the Oil Well builders panel (the hammer panel entry), read the oil counter and Total Power, close the panel. NO tap beyond opening and closing it; no drag.

WRITE: (1) `owner_idle_seconds` exactly as the bridge prints it; (2) the wait before this run's first click (seconds); (3) EVERY dialog that appeared, with its text and the UTC time: the new tree may ask consent in more places: ANSWER NOTHING (do not tap Cancel, Allow, Confirm or any button of a consent request: consent requests are human-only), STOP and tell the Coordinator. (4) the Oil Well entry's time left, the oil counter and Total Power, each with its tag text and the UTC time.

4 steps at most, one run. The standing rule applies. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
