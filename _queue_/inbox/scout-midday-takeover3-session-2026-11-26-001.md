---
unit: scout-midday-takeover3-session-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 0
created_at: 2026-11-26T05:50:29Z
expires_at: 2026-11-26T11:45:00Z
planned_for:
not_before: 2026-11-26T07:44:00Z
window: third session takeover, one confirm, gated, backoff rule (coordinator 05:55z)
est_minutes: 6
serves: upkeep
chain_id: takeover3-session-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is a one-off session takeover, NOT the midday scout walk: do only the steps below. Definition folder `_activities_/perception-scout/` (its `rule-digest.md` first).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THIRD SESSION TAKEOVER: one Confirm, gated, backoff rule, Coordinator 05:55Z)

serves: upkeep

DISPATCH ONLY WHEN NAMED (the Coordinator, at 07:46Z, or 08:26Z if the quiet window blocks); not before 07:44Z. This unit does ONLY the steps below.
(1) The 300 s owner-idle gate applies: if refused, wait. FRONT: record `lsappinfo front`; if it is not LastWar, run the standing front script ONLY IF it names UserNotificationCenter; any other app in front, or still not LastWar: STOP, release, tell the Coordinator. NO killall: the one approved at 04:17Z is spent.
(2) ONE frame: the UTC time and the screen text. If 'Your account is currently active on a different device!' with ONE button 'Confirm' still stands, go to (3). If the base is live and no dialog shows: close 'no dialog: no takeover needed'. ANY OTHER DIALOG OR WORDING: STOP.
(3) ONE tap on Confirm; write the UTC time and the reason: 'the third Confirm: backoff rule of Steer A 05:48Z: 2 hours after the quick return of 05:46:23.8Z (the second Confirm of 05:41:10.9Z held 5 min 13 s)'. NEVER a second tap.
(4) THE FRAME AFTER. If the game quits, run the standing front script ONCE. On 'Update complete, please restart the game.': ONE tap on that exact text only (Steer A 04:31Z). Then frames only: the HUD as shown (food, iron, coin, oil, diamonds, Total Power if shown) and the builders panel: write 'takeover done HH:MM:SSZ'. TIPS 'Enable notifications': Cancel only. No Lottery tab, avatar, bubble or claim.
(5) THE 30-MINUTE GUARD (backoff, Steer A 05:48Z) from this Confirm: if the dialog returns within 30 minutes: STOP, NO TAP; the next wait is 4 HOURS (the Coordinator tells Steer A); a hold of 2 HOURS or more resets the wait to 30 minutes.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Confirm tapped and the base live (`--state-change yes`) or a verified no-dialog (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap: 0.40 USD.
