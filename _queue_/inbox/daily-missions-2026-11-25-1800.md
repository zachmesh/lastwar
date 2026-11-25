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
est_minutes: 3
serves: upkeep
chain_id:
chain_seq:
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the specifics)

MAIN TASKS (Steer A 01:21Z, folded in): the panel may open on the Main Tasks tab (read the tab labels first). Read every Main Tasks row by text; tap a plain green CLAIM once per row (no price, no gem icon, not Buy, Unlock, Upgrade or Activate), re-reading the list after each; EVERY Go stays unpressed; record the rewards. Then the Daily Tasks tab as below.
Daily missions: claim each completed Mission task's plain Claim one by one, re-checking after each; claim an activity chest at its threshold only when its button is a plain Claim (never a diamond or price line). Write the points before and after.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
