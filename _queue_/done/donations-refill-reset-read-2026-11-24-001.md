---
unit: donations-refill-reset-read-2026-11-24-001
regular: donations
activity: alliance-donations
segment: 1
priority: 1
created_at: 2026-11-24T00:40:25Z
expires_at: 2026-11-24T01:55:00Z
planned_for:
not_before: 2026-11-24T01:48:00Z
window: read only count read before the 0200z reset no donate tap
est_minutes: 6
serves: PL-04
chain_id: refill-reset-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T01:48:02Z
lease_until: 2026-11-24T02:08:02Z
result:
  status: done
  started_at: 2026-11-24T01:48:02Z
  finished_at: 2026-11-24T01:49:50Z
  duration_seconds: 108
  executor: operator
  summary: READ A: Donation Count 4/30 at 01:48:36.549Z and 01:48:44.579Z as registered, coin Donate green, no timer; nothing pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/0148-queue-run.md and 0148-queue-run.csv; run 20261124T014802Z-eba5ee
  follow_up: READ B at 02:03Z after the reset; the next grid point 01:57:57
  stats:
    target: read the donation count in the window 01:48:00Z to 01:55:00Z
    achieved: count 4/30 at 01:48:36.549Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.117774 USD
    verified: yes
    run_id: 20261124T014802Z-eba5ee
    run_steps: 10
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.117774
    device_takeovers: 0
    count_read: 4
    read_utc: 01:48:36.549
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (definition pointer, from the roster)

This unit is the regular `donations`: Alliance tech donations - every run: donate with the coin button to the recommended tech whenever today coin donations remain (never diamonds); claim the daily donation reward when claimable. Its definition is the activity folder `_activities_/alliance-donations/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY count read A of 2, before the 02:00Z reset, Researcher's brief)

serves: PL-04

Brief `_records_/2026-11-22/research/refill-reset-read-brief.md`. LEAVES THE GAME: NONE. NO Donate tap, nothing spent: the pass anchor 00:37:57.17Z must stay valid. If another app comes to the front, STOP and touch nothing. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first.

Steps (about 5): 1. LastWar frontmost; Alliance shield (ground it fresh), Techs tile, the recommended node (Quick Construction 9/10). 2. Read the count, or the grey timer if the count is hidden; write the UTC time to the second. 3. Close with the panel X and the back arrow.

THE WINDOW IS THE POINT: read A must be time-stamped between 01:48:00Z and 01:55:00Z (before the 01:57:57 grid point). If the count read would fall outside it, close SKIPPED 'window missed' and write the time. Predicted 4 [1 + floor((entry - 00:37:57.17Z) / 20 min)]. Write the count, the time, the timer end if grey, and any difference from 4.
Cost cap, stated: 0.40 USD.
