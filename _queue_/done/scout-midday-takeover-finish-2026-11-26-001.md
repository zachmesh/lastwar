---
unit: scout-midday-takeover-finish-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 0
created_at: 2026-11-26T04:25:02Z
expires_at: 2026-11-26T07:30:00Z
planned_for:
not_before: 2026-11-26T04:25:00Z
window: takeover finish, relaunch and the first base frame (coordinator 04:26z)
est_minutes: 5
serves: upkeep
chain_id: takeover-finish-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T04:27:31Z
lease_until: 2026-11-26T04:47:31Z
result:
  status: done
  started_at: 2026-11-26T04:27:31Z
  finished_at: 2026-11-26T04:33:13Z
  duration_seconds: 342
  executor: operator
  summary: Takeover finish: the front script once launched LastWar (front 04:26:12Z); one tap on the update 'Confirm' at 04:31:08.6Z (Coordinator's decision); takeover done 04:31:51Z; the first base frame: Total Power 151,273,926, food 165.2M, iron 734.8M, coin 564, oil 564.8K, diamonds 10,943, energy 196, builders 3/4, labs 2/2; the different-device dialog never returned; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0426-queue-run.md and 0426-queue-run.csv; run 20261126T043057Z-301879
  state_change: yes
  follow_up: the 30-minute guard from the 04:20:55.1Z Confirm runs to 04:50:55Z
  stats:
    target: relaunch and read the first base frame
    achieved: the base live, HUD written
    resources_gained: none
    points: 0
    costs: none spent; model 0.122739 USD
    verified: yes
    run_id: 20261126T043057Z-301879
    run_steps: 9
    actions_done: 1
    actions_refused: 0
    cost_usd: 0.122739
    device_takeovers: 0
    claims: 0
    takeover_done_utc: 04:31:51
    power: 151273926
    tram_badge: icon drawn without a badge
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is a one-off takeover finish, NOT the midday scout walk: do only the steps below. Definition folder `_activities_/perception-scout/` (its `rule-digest.md` first).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TAKEOVER FINISH: relaunch and the first base frame, Coordinator 04:26Z)

serves: upkeep

Facts [M]: ONE Confirm was tapped at 04:20:55.1Z; the game then quit (no LastWar process, Chrome in front), as in record 2738 on 11-23. This unit does ONLY the steps below.
(1) Record `lsappinfo front` AND `lsappinfo find name=LastWar`. FRONT: if LastWar is already running and in front, go to (2); else run the standing front script ONCE (`_tools_/mac_lastwar_front.sh`: it launches LastWar; NO click on Chrome or any other app, NO killall), record front again; still not LastWar after 60 s: stop, release, tell the Coordinator.
(2) FRAMES ONLY while it logs in (up to about 90 s). If 'Your account is currently active on a different device!' appears AGAIN: STOP, NO TAP, tell the Coordinator (the OD-05 guard: someone plays on the other device; the 04:20:55Z Confirm is the one Confirm of this takeover). TIPS 'Enable notifications': Cancel only. Any other dialog, a price or a diamond: STOP.
(3) THE FIRST BASE FRAME: write the HUD as shown (Total Power if shown, food, iron, coin, oil, diamonds) and the builders panel, next to the Coach's 05:22Z values (power 150,701,116, food 140.4M, iron 760.2M, coin 25.8M), no comment. Write 'takeover done HH:MM:SSZ'. Nothing else is pressed: no claim, no bubble, no Lottery tab, no avatar.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the base live (`--state-change yes`); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
