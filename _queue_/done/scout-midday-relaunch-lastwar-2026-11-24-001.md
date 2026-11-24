---
unit: scout-midday-relaunch-lastwar-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T19:45:59Z
expires_at: 2026-11-24T20:50:00Z
planned_for:
not_before: 2026-11-24T20:16:00Z
window: controlled relaunch of lastwar after the lottery loading screen held for steer a
est_minutes: 10
serves: upkeep
chain_id: relaunch-lastwar-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T20:17:06Z
lease_until: 2026-11-24T20:37:06Z
result:
  status: done
  started_at: 2026-11-24T20:17:06Z
  finished_at: 2026-11-24T20:21:59Z
  duration_seconds: 293
  executor: operator
  summary: Controlled relaunch: LastWar quit by its application menu (20:17:21.2Z), Google Chrome fell to the front (20:17:23Z, untouched), reopened by the standing front script at 20:17:48.5Z; the first frame (20:19:22.9Z) was already the base with no dialog (no Cancel or Confirm); the HUD and all six timers matched to 0.7 s; the tram icon not drawn; the Lottery never opened; drags 0. state_change: yes. state_read: after the relaunch the base shows, no dialog; builders Lv.26 11-26T11:08:36Z, Lv.27 11-30T01:31:01Z, Lv.28 12-03T23:50:14Z, Oil Well 11-25T07:11:20Z; labs 11-25T19:39:08Z and 11-26T08:37:35Z | step 3 | 20:20:24Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/2017-queue-run.md and 2017-queue-run.csv; run 20261124T201707Z-a80db7
  state_read: after the relaunch the base shows, no dialog; builders Lv.26 11-26T11:08:36Z, Lv.27 11-30T01:31:01Z, Lv.28 12-03T23:50:14Z, Oil Well 11-25T07:11:20Z; labs 11-25T19:39:08Z and 11-26T08:37:35Z | step 3 | 20:20:24Z
  state_change: yes
  follow_up: the game is back on the base: pass 008 at 21:10Z and the later units can run; the Thanksgiving Lottery tab must not be opened again
  stats:
    target: quit and reopen LastWar to clear the stuck loading screen and re-read timers
    achieved: relaunched; base; timers matched
    resources_gained: none
    points: 0
    costs: none spent; model 0.204533 USD
    verified: yes
    run_id: 20261124T201707Z-a80db7
    run_steps: 16
    actions_done: 19
    actions_refused: 0
    cost_usd: 0.204533
    device_takeovers: 0
    claims: 0
    timers_matched: 6 of 6
    tram_badge: icon not drawn
    drags_tried: 0
    dialogs: none
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, CONTROLLED RELAUNCH of LastWar if the Lottery screen still hangs at 20:15Z, authorized by Steer A 19:52Z)

serves: upkeep

Facts [M]: the Lottery has been a full-window loading screen since 19:29:18Z (no controls, no back arrow). THE RED DRAW BUTTON, THE LOTTERY TAB AND EVERY PURCHASE SURFACE: NEVER.
(1) ONE frame: the UTC time, what shows, any TOAST (text and time, e.g. 'Violet's Gift received!'). If the screen CLEARED: close 'cleared: no relaunch', tap nothing.
(2) STILL the loading screen: quit LastWar by its APP MENU (LastWar, then Quit; the item read by its text in a frame first): no key chord, no Escape, no force quit; no menu: stop.
(3) Wait 10 s. Reopen by the standing front script or the launcher. Wait for the login; write the first frame. TIPS 'Enable notifications': Cancel only. The 'active on a different device' dialog: ONE Confirm (Steer A's standing order), never a second within 30 minutes, its text read in a frame first, the time written.
(4) Write the HUD (food, iron, coin, oil, diamonds, Total Power) and these timers to the second, saying whether each matched: Lv.26 ground 11-26T11:08:36Z, Lv.27 11-30T01:31Z, Lv.28 12-03T23:50Z, Oil Well 11-25T07:11:19.6Z, Food Output V 11-25T19:39Z, Oil Output I 11-26T08:37Z.
(5) The 300 s owner-idle gate applies: if refused, wait. Any other dialog, price line or other app: STOP. `--state-change yes` (relaunched) or `no`, with a `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
