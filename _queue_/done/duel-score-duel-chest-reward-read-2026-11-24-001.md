---
unit: duel-score-duel-chest-reward-read-2026-11-24-001
regular: duel-score
activity: alliance-duel
segment: 2
priority: 1
created_at: 2026-11-24T23:43:18Z
expires_at: 2026-11-25T00:20:00Z
planned_for:
not_before: 2026-11-24T23:43:00Z
window: read the 7.2m personal chest reward line on the vs duel panel no tap on the chest
est_minutes: 3
serves: snapshot
chain_id: duel-chest-reward-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 1
claimed_by: operator
claimed_at: 2026-11-24T23:44:12Z
lease_until: 2026-11-25T00:04:12Z
result:
  status: done
  started_at: 2026-11-24T23:44:12Z
  finished_at: 2026-11-24T23:45:43Z
  duration_seconds: 91
  executor: operator
  summary: Duel chest read: the personal daily total 7,017,000 (unchanged), the 2,600,000 and 3,600,000 chests drawn with lids open and the 7,200,000 gold chest closed (red-gem tags 24,900, 46,900, 67,800; no Claim button); the 7,200,000 chest's reward line is not shown without a tap: unread; nothing pressed but the VS medallion and the back arrow; the tram icon not drawn; drags 0. state_change: no. state_read: Today's Theme personal total 7,017,000; chests 2,600,000 and 3,600,000 lids open, 7,200,000 closed; reward line not shown without a tap | step 3 | 23:44:32Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-duel/2344-queue-run.md and 2344-queue-run.csv; run 20261124T234412Z-f44827
  state_read: Today's Theme personal total 7,017,000; chests 2,600,000 and 3,600,000 lids open, 7,200,000 closed; reward line not shown without a tap | step 3 | 23:44:32Z
  state_change: no
  follow_up: the 7,200,000 chest's reward line needs a tap on the chest icon (Steer A's call); 183,000 points short
  stats:
    target: read the 7,200,000 chest's reward line by plain reading
    achieved: reward line needs a tap: unread
    resources_gained: none
    points: 0
    costs: none spent; model 0.113528 USD
    verified: yes
    run_id: 20261124T234412Z-f44827
    run_steps: 9
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.113528
    device_takeovers: 0
    personal_total: 7017000
    reward_line: needs a tap: unread
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# duel-score

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `duel-score`: Alliance Duel score - read the personal daily total on the VS duel panel and record it against the 3,600,000 target (stats target/achieved/gap, live read only); the last read before the daily reset (02:00 UTC) is the day closing figure; read-only, never grind, spend or buy. Its definition is the activity folder `_activities_/alliance-duel/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE 7.2M CHEST REWARD LINE: plain reading, NO tap on the chest, one run)

serves: snapshot

The Strategist cannot price the 7,200,000 personal chest because its reward line is unread in every record. Open the VS duel panel by the duel-score route (the activity digest). 4 steps:
(1) A frame with the UTC time: write the personal daily total and the three chest thresholds (2,600,000, 3,600,000, 7,200,000) with each chest's state.
(2) READ the 7,200,000 chest's reward line by plain reading in the frame: every item NAME and QUANTITY; digits cropped from the SAVED frame at 6x.
(3) TAP NOTHING but the route's own taps: not the chest icon, no Claim, Go or button of any kind. If the reward line is not shown without a tap: close 'reward line needs a tap: unread', tap nothing more.
(4) Close with the back arrow. `--state-change no`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
