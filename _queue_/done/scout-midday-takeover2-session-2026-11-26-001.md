---
unit: scout-midday-takeover2-session-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 0
created_at: 2026-11-26T05:10:47Z
expires_at: 2026-11-26T09:30:00Z
planned_for:
not_before: 2026-11-26T05:38:00Z
window: second session takeover, one confirm, gated (coordinator 05:12z)
est_minutes: 6
serves: upkeep
chain_id: takeover2-session-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T05:40:59Z
lease_until: 2026-11-26T06:00:59Z
result:
  status: done
  started_at: 2026-11-26T05:40:59Z
  finished_at: 2026-11-26T05:47:01Z
  duration_seconds: 362
  executor: operator
  summary: Second takeover: the second Confirm tapped once at 05:41:10.9Z (the dialog had returned 05:04:46Z); the game quit and the front script once relaunched it; takeover done 05:41:55Z (the base live; Total Power 151,680,155, food 194.8M, iron 762.8M, coin 14.8M, oil 572.7K, diamonds 10,643, energy 181, builders 3/4); the dialog RETURNED at 05:46:23.8Z, 4 min 13 s after the Confirm: someone plays on the other device: no tap, no third Confirm, the team stops for two hours; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0540-queue-run.md and 0540-queue-run.csv; run 20261126T054100Z-1415ce
  state_change: yes
  follow_up: the guard: the team stops for two hours; the Coordinator tells Steer A
  stats:
    target: one Confirm on the different-device dialog
    achieved: Confirm tapped, base live 05:41:55Z; the dialog returned at 05:46:23.8Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.147 USD
    verified: yes
    run_id: 20261126T054100Z-1415ce
    run_steps: 10
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.147
    device_takeovers: 0
    claims: 0
    confirm_utc: 05:41:10.9
    takeover_done_utc: 05:41:55
    dialog_returned_utc: 05:46:23.8
    power: 151680155
    tram_badge: icon not read
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is a one-off session takeover, NOT the midday scout walk: do only the steps below. Definition folder `_activities_/perception-scout/` (its `rule-digest.md` first).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, SECOND SESSION TAKEOVER: one Confirm, gated, Coordinator 05:12Z)

serves: upkeep

DISPATCH ONLY WHEN NAMED (the Coordinator, on Steer A's or the owner's word); not before 05:38Z. Facts [M]: the 04:20:55Z Confirm held 43.8 minutes; the dialog returned at 05:04:46Z. This unit does ONLY the steps below.
(1) The 300 s owner-idle gate applies: if refused, wait. FRONT: record `lsappinfo front`; if it is not LastWar, run the standing front script ONLY IF it names UserNotificationCenter; any other app in front, or still not LastWar: STOP, release, tell the Coordinator. NO killall: the one approved at 04:17Z is spent.
(2) ONE frame: the UTC time and the screen text. If 'Your account is currently active on a different device!' with ONE button 'Confirm' still stands, go to (3). If the base is live and no dialog shows: close 'no dialog: no takeover needed'. ANY OTHER DIALOG OR WORDING: STOP.
(3) ONE tap on Confirm; write the UTC time and the reason: 'the second Confirm: the dialog returned 05:04:46Z after the 43.8-minute hold: Coordinator <time>, Steer A's word 05:19Z (wait 30, then one Confirm: allowed to 06:20:55Z)'. NEVER a second tap.
(4) THE FRAME AFTER. If the game quits, run the standing front script ONCE. On 'Update complete, please restart the game.': ONE tap on that exact text only (Steer A 04:31Z). Then frames only: the HUD as shown (food, iron, coin, oil, diamonds, Total Power if shown) and the builders panel: write 'takeover done HH:MM:SSZ'. TIPS 'Enable notifications': Cancel only. No Lottery tab, avatar, bubble or claim.
(5) THE 30-MINUTE GUARD again from this SECOND Confirm: if the dialog returns within 30 minutes: STOP, NO TAP, the team stops for TWO HOURS (he is evidently playing: no more kicks); the Coordinator tells Steer A, who tells the owner. No third Confirm.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Confirm tapped and the base live (`--state-change yes`) or a verified no-dialog (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap: 0.40 USD.
