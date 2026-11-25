---
unit: daily-missions-main-tasks-claim-2026-11-24-001
regular: daily-missions
activity: daily-missions
segment: 3
priority: 2
created_at: 2026-11-25T01:22:59Z
expires_at: 2026-11-25T03:00:00Z
planned_for:
not_before: 2026-11-25T01:22:00Z
window: claim the plain green claims on the main tasks tab steer a 01:21z
est_minutes: 4
serves: upkeep
chain_id: main-tasks-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 1
claimed_by: operator
claimed_at: 2026-11-25T01:29:20Z
lease_until: 2026-11-25T01:49:20Z
result:
  status: done
  started_at: 2026-11-25T01:29:20Z
  finished_at: 2026-11-25T01:31:22Z
  duration_seconds: 122
  executor: operator
  summary: Main Tasks claim: 'Upgrade Oil Well to Lv.24 (1/1)' claimed once with its green Claim (5.0K food and 5.0K iron as printed on the row; no popup); the list re-read: Headquarters, Builder's Hut, Hospital, Training Base and Gear Factory rows all blue Go, never pressed; tram icon not drawn; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0129-queue-run.md and 0129-queue-run.csv; run 20261125T012920Z-df31c8
  state_change: yes
  follow_up: the remaining Main Tasks need upgrades (Go): not seat actions
  stats:
    target: claim each plain green Claim on the Main Tasks list
    achieved: 1 claim
    resources_gained: food 5.0K; iron 5.0K
    points: 0
    costs: none spent; model 0.184237 USD
    verified: yes
    run_id: 20261125T012920Z-df31c8
    run_steps: 15
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.184237
    device_takeovers: 0
    claims: 1
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.


## Brief (planner, THE MAIN TASKS TAB: plain green Claims once, Steer A 01:21Z)

serves: upkeep

Facts [M]: the sweep of 01:05Z saw the Main Tasks tab row 'Upgrade Oil Well to Lv.24 (1/1)' with a green Claim (the build started 17:31Z). No regular claims Main Tasks: this unit does. 5 steps:
(1) Open Mission from the orange terminal on the base screen. Read the tab labels in a frame; tap the MAIN TASKS tab by its label.
(2) Read EVERY row by text: title, progress, reward, button label (Claim or Go).
(3) For each row whose button is a plain green CLAIM: read the reward by text first; the button has no price, no gem icon and is not Buy, Unlock, Upgrade or Activate: tap it ONCE, then re-read the list before the next row (a stale tap can land on Go).
(4) Read the popup by text (every reward, to the last row); close it by its X, or Confirm only a plain 'Congratulations'. EVERY Go stays unpressed.
(5) Any price, dialog or other app: STOP. Close the panel. `--state-change yes` if a claim was taken, else no; a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
