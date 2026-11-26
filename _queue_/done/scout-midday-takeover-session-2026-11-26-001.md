---
unit: scout-midday-takeover-session-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 0
created_at: 2026-11-26T04:06:48Z
expires_at: 2026-11-26T07:30:00Z
planned_for:
not_before: 2026-11-26T04:06:00Z
window: session takeover, one confirm (steer a 04:05z)
est_minutes: 6
serves: upkeep
chain_id: takeover-session-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T04:20:45Z
lease_until: 2026-11-26T04:40:45Z
result:
  status: done
  started_at: 2026-11-26T04:20:45Z
  finished_at: 2026-11-26T04:33:13Z
  duration_seconds: 748
  executor: operator
  summary: Session takeover: front UserNotificationCenter 04:19:30Z, the front script once, one killall at 04:20:00.2Z, LastWar front 04:20:03.3Z; the dialog 'Your account is currently active on a different device!' with ONE button 'Confirm' read at 04:20:51.6Z; ONE Confirm tap at 04:20:55.097Z; the game then quit (Chrome front 04:20:57.8Z) and came back live in the finish unit (record 0430, takeover done 04:31:51Z); the 30-minute guard to 04:50:55Z; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0420-queue-run.md and 0420-queue-run.csv; run 20261126T042046Z-42b0ad
  state_change: yes
  follow_up: the guard: if the different-device dialog returns before 04:50:55Z someone plays on the other device
  stats:
    target: one Confirm on the different-device dialog
    achieved: one Confirm tapped, the base live (record 0430)
    resources_gained: none
    points: 0
    costs: none spent; model 0.03 USD
    verified: yes
    run_id: 20261126T042046Z-42b0ad
    run_steps: 1
    actions_done: 1
    actions_refused: 0
    cost_usd: 0.03
    device_takeovers: 0
    claims: 0
    confirm_utc: 04:20:55.097
    killalls: 1
    tram_badge: not read
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

## Brief (planner, SESSION TAKEOVER: one Confirm on the different-device dialog, Steer A 04:05Z under OD-20261123-05 and OD-20261123-17)

serves: upkeep

Steer A's delegation (OD-05): ONE takeover, then stop.
(1) The 300 s owner-idle gate applies: if refused, wait. FRONT: if `lsappinfo front` is not LastWar, record it; run the standing front script ONLY IF it names UserNotificationCenter; if it still names UserNotificationCenter after the script, record front, run ONE `killall -9 UserNotificationCenter` (Steer A 04:17Z), record front again (it must name LastWar), then the front script again if needed; if the window is of ANOTHER KIND than a Chrome notification request, or it REAPPEARS within 10 minutes, STOP and report; NO SECOND killall without a record of why; the window itself is never read or clicked; any other app in front: STOP and touch nothing; still not LastWar: stop, release, tell the Coordinator.
(2) ONE frame: the UTC time and the dialog TEXT. It must read 'Your account is currently active on a different device!' with ONE button 'Confirm'. ANY OTHER DIALOG OR WORDING (a price, a diamond): STOP. No dialog, base live: close 'no dialog: no takeover needed'.
(3) ONE tap on Confirm; write the UTC time. NEVER a second tap.
(4) THE FRAME AFTER, before anything else: read the HUD (food, iron, coin, oil, diamonds) and Total Power (the baseline), then the base live (a resource bar and the builders panel) once more when the login ends: write 'takeover done HH:MM:SSZ'. TIPS 'Enable notifications': Cancel only. No Lottery tab, avatar, bubble or claim.
(5) THE 30-MINUTE GUARD (OD-05): write the Confirm time. If the dialog returns within 30 minutes, someone plays on the other device: the Coordinator stops the regulars, retries once after 30 minutes; a second return stops the team and tells the owner. At most two Confirms in two hours.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Confirm tapped and the base live (`--state-change yes`) or a verified no-dialog (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
