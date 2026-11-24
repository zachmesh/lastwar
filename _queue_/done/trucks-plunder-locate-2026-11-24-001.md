---
unit: trucks-plunder-locate-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T07:12:01Z
expires_at: 2026-11-24T09:45:00Z
planned_for:
not_before: 2026-11-24T07:13:00Z
window: read only locate of the intercity trade entry no trade no truck no plunder
est_minutes: 10
serves: PL-18
chain_id: plunder-locate-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T07:13:04Z
lease_until: 2026-11-24T07:33:04Z
result:
  status: partial
  started_at: 2026-11-24T07:13:04Z
  finished_at: 2026-11-24T07:15:34Z
  duration_seconds: 150
  executor: operator
  summary: Intercity Trade entry not found on the HUD, the Alliance menu, the world map edges or the Events tab row; candidates not tapped: truck-glyph bubbles on the train station and truck yard of the base, a green truck marker on the world map; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0713-queue-run.md and 0713-queue-run.csv; run 20261124T071304Z-016b16
  follow_up: a supervised tap on a truck-yard bubble (about (165,408) on the station-camera frame) is the next test if Steer A allows; the yard holds parked trucks
  stats:
    target: find the Intercity Trade entry (point and path) or not found
    achieved: not found; candidates named
    resources_gained: none
    points: 0
    costs: none spent; model 0.172843 USD
    verified: yes
    run_id: 20261124T071304Z-016b16
    run_steps: 13
    actions_done: 21
    actions_refused: 0
    cost_usd: 0.172843
    device_takeovers: 0
    blocker_category: f missing precondition (the Intercity Trade entry is not on the HUD, the Alliance menu, the world map edges or the Events tab row)
    drags_tried: 0
    rules_used: 6
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY LOCATE: where is the Intercity Trade entry now, PL-18)

serves: PL-18

The supervised first tap (`_records_/2026-11-22/truck-plunder/0708-queue-run.md`) showed that (107,580) is the ALLIANCE TRAIN SHORTCUT (the camera panned to the Alliance Train station), not the Trade entry. 12 steps, READ ONLY, one frame per page; ONE drag at most, from a blank margin.

1. WORLD then BASE: list every HUD icon by position and label: the left column, the right column and the top bar.
2. The Alliance shield menu (ground fresh): look for a Trade or Truck entry; list the menu's tiles.
3. The world map: look for a trade button.
4. Anything else naming Trade (Events hub, a daily-task line): read it only.
Write where the entry is (the point and the path from the fresh base frame) or 'not found' with everything tried. If an entry's screen opens, take a frame and close it with X. NEVER start a trade, send a truck, press Plunder or Battle.

TIMING: it must END by 07:33Z, or start after 08:36Z (the depot claim 07:35:30Z to 07:58Z, the cu window 08:00Z to 08:25Z and the Oil Well hand-off 08:25:30Z to about 08:36Z are fixed): if the clock is inside one, wait. The TIPS 'Enable notifications' dialog: take a frame, identify Cancel BY ITS TEXT, one tap, never Enable Now; any other unrecognised dialog: stop. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Tag text beside every number; none means [G].
Cost cap, stated: 0.50 USD.
