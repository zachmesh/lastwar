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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T20:15:30Z
lease_until: 2026-11-24T20:35:30Z
result:
  status: done
  started_at: 2026-11-24T20:15:30Z
  finished_at: 2026-11-24T20:15:58Z
  duration_seconds: 28
  executor: operator
  summary: One frame at 20:15:34.7Z: still the full-window Lottery loading screen (46 minutes after the tab was opened), no toast, no dialog, the base not visible; nothing tapped; drags 0. state_change: no. state_read: Last War window still the full-window Lottery loading screen, no HUD, no toast, no dialog | step 1 | 20:15:34Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/2015-queue-run.md and 2015-queue-run.csv; run 20261124T201530Z-6e05a6
  state_read: Last War window still the full-window Lottery loading screen, no HUD, no toast, no dialog | step 1 | 20:15:34Z
  state_change: no
  follow_up: the relaunch unit follows (Steer A pre-authorized it)
  stats:
    target: read one frame of the game window
    achieved: still the loading screen at 20:15:34Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.032356 USD
    verified: yes
    run_id: 20261124T201530Z-6e05a6
    run_steps: 2
    actions_done: 0
    actions_refused: 0
    cost_usd: 0.032356
    device_takeovers: 0
    loading_screen: still
    tram_badge: not readable
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

## Brief (planner, THE LOTTERY FRAME READ: one read-only frame at 20:15Z, Steer A's option B)

serves: snapshot

Facts [M] (operator, 19:45Z): the Thanksgiving Lottery has been a full-window loading screen since 19:29:18Z (an orange machine, a red draw button, no controls, no back arrow); one tap at (175,930) changed nothing; a toast still drew: the game is alive. THIS UNIT TAPS NOTHING: no key, no scroll, no click, never the red draw button. 3 steps:
(1) ONE frame of the game window; write the UTC time and what it shows: the base, the lottery page, or still the loading screen; and any TOAST on it (its text, e.g. 'Violet's Gift received!', and its clock time: the Coach's series).
(2) If the base is visible: write the HUD (food, iron, coin, oil, diamonds, Total Power), the tram icon state (absent, bare or badge N), and any toast or dialog.
(3) If STILL the loading screen: close 'still loading at <time>' and DO NOT TAP. `--state-change no`, a `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
