---
unit: scout-midday-relaunch-lastwar-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T19:45:59Z
expires_at: 2026-11-24T23:52:00Z
planned_for:
not_before: 2026-11-24T23:50:00Z
window: controlled relaunch of lastwar after the lottery loading screen held for steer a
est_minutes: 8
serves: upkeep
chain_id: relaunch-lastwar-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, CONTROLLED RELAUNCH of LastWar after the Lottery loading screen, WAITING FOR STEER A)

serves: upkeep

DO NOT RUN until the Coordinator names this unit after Steer A's word; else close 'blocked by prerequisite', press nothing.
Facts [M]: the Lottery is a full-window loading screen since 19:29:18Z (no controls, no back arrow); a tap at (175,930) changed nothing; the game is alive. THE RED DRAW BUTTON, THE LOTTERY TAB AND EVERY PURCHASE SURFACE: NEVER.
(1) A frame now: what shows, the time.
(2) Quit LastWar by its APP MENU (LastWar, then Quit), the item identified by its text in a frame before the click; no key chord unless Steer A names it, no force quit; no menu: stop.
(3) Wait 10 s. Reopen LastWar through the cu launcher (one click on its Dock icon, read by its label).
(4) Wait for the login; write the first frame. TIPS 'Enable notifications': Cancel only. The 'active on a different device' dialog: ONE Confirm per the standing order OD-17, never twice in 30 minutes, its text read in a frame first, the time written.
(5) Write the HUD (diamonds, iron, food, coin, oil, Total Power), the tram icon (absent, bare or badge N), whether the Lottery screen is gone, and every timer readable without a tap (Oil Well Lv.24 end 11-25T07:11:19.6Z, labs, grounds), with the time. NO other tap.
(6) Any other dialog, price line or other app: STOP. `--state-change yes`, `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
