---
unit: daily-missions-2026-11-25-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-25T22:00:31Z
expires_at: 2026-11-27T02:00:00Z
planned_for: 2026-11-26T02:00:00Z
not_before: 2026-11-26T02:08:00Z
window:
est_minutes: 10
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T10:29:21Z
lease_until: 2026-11-26T10:49:21Z
result:
  status: partial
  started_at: 2026-11-26T10:29:21Z
  finished_at: 2026-11-26T10:47:00Z
  duration_seconds: 1059
  executor: operator
  summary: Daily missions: Main Tasks all Go (nothing to claim); Daily Tasks claim of 'Upgrade a Building' once (points 150 to 160) and the 160 activity chest once (gold paw item, truck-ticket item, scroll, gem item 30 (diamonds 10,643 to 10,673), a 1.6K crystal, 5m construction speed-up x3); the first run was cancelled by UserNotificationCenter (the screen-capture consent window, never read or answered) until one approved killall at 10:39:29Z; the Weekly Pass check was not done (cost cap 0.60 spent: 0.580); no Go pressed; drags 2. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/1029-queue-run.md and 1029-queue-run.csv; run 20261126T104345Z-a83b62
  state_change: yes
  follow_up: the Weekly Pass check waits for a next unit (its cards read Already claimed today at 09:38Z; reset 02:00Z)
  stats:
    target: claim the Main Tasks, the Daily Tasks and the chests; the Weekly Pass check
    achieved: one task claim and the 160 chest; the Weekly Pass check not done
    resources_gained: diamonds +30; 5m construction speed-up x3; scroll; crystal 1.6K; 10 activity points
    points: 0
    costs: none spent; model 0.580 USD
    verified: yes
    run_id: 20261126T104345Z-a83b62
    run_steps: 43
    actions_done: 12
    actions_refused: 0
    cost_usd: 0.580
    device_takeovers: 0
    claims: 2
    points_before: 150
    points_after: 160
    diamonds_after: 10673
    blocker_category: cost cap: the Weekly Pass check not done
    tram_badge: not read
    drags_tried: 2
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i, duration exceeds 15-minute unit cap]
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the specifics)

MAIN TASKS (Steer A 01:21Z, folded in): the panel may open on the Main Tasks tab (read the tab labels first). Read every Main Tasks row by text; tap a plain green CLAIM once per row (no price, no gem icon, not Buy, Unlock, Upgrade or Activate), re-reading the list after each; EVERY Go stays unpressed; record the rewards. Then the Daily Tasks tab as below.
Daily missions: claim each completed Mission task's plain Claim one by one, re-checking after each; claim an activity chest at its threshold only when its button is a plain Claim (never a diamond or price line). Write the points before and after. WEEKLY PASS CHECK (Steer A 09:43Z, folded from the passes unit): after the missions open the Weekly Pass tab only (never the G tab, never Go, Renew or Extension) and follow `_records_/2026-11-22/queue-planning/3130-weekly-pass-page-sequence.md`: a frame at the top, at most FIVE composed pans, each its own message with a frame after it; read each card's label, price line, gem icon and state BEFORE any tap; 'Already claimed today' is a complete; ONE plain Claim per owned card. Write the six cards' state words as shown (Claim, Already claimed today, Claimed).

Verify each HUD icon by its label or glyph in a frame before the tap. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
