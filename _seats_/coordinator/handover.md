---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-26T04:20:00Z
level: L2
version: 0.26.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, schedules, the trade cycle, the macOS alert and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-25 17:25Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: tool_sync, model_guard, `queue.py next`; `next` can name a held unit: check). Planner ping `schedule-4803c6f4` (02, 06, 10, 14, 18, 22Z); daily `schedule-e1887d97` 11:55Z; records delivery `schedule-70993579` every 2 h (first 17:56Z); weekly `schedule-fee71877` 11-30 01:00Z.
- TEAM.yaml 0.7.6: model claude-sonnet-5-5 at HIGH (owner request 11-25; the guard reads it). The operator's id is in /tmp/lw-new-operator-id.txt. Steer A `session-eb024f72-e661-4a77-9303-66af95dbcfd1` and Steer B `session-e127662e-07ba-4385-b905-3d0e90fd1eeb` relay the owner. Helpers in /tmp: lw-pre-rebase.sh, lw-scan-branch.py (rebuild if gone).

## The halt (since 06:25:52Z) and the takeover

The game showed 'active on a different device' (the owner's phone). I held 22 h on Steer A's 06:36Z ruling; Steer A WITHDREW it at 04:05Z on 11-26 (OD-20261126-01): the 'nobody Confirms again without the owner' clause was the Steers' own 11-23 resume procedure (record 2738), not the owner's; the owner's words are OD-05 (standing approval, 30-minute guard) and OD-17 ('take ownership, kick out others'). Takeover unit `scout-midday-takeover-session-2026-11-26-001`: one Confirm on the exact dialog text, no second tap, no more than two Confirms in two hours. 04:07Z it stopped at the front step: the front script does not lift LastWar over a UserNotificationCenter window; Steer A decides one killall. Then the order: radar and duel-score claim, lab Complete, Oil Well `-005`, Drill Ground hand-off, cycle E, room collect, UR claim, train batch. Cost of the halt: 35,650 duel chests, about 49M and 4 percent of the build per further day.

## Rules learned

- Composed pan: mouse_move, left_mouse_down, wait 1, one 175 px move, wait 1, left_mouse_up, screenshot, only from blank ground or a tile gap (never on a building: move mode).
- Tram badge equals the Your Truck tab. HUNG SCREEN (15 min): relaunch unit, tell Steer A after. Never the lottery tab; the avatar only by the VIP unit's named exception.
- Closing rule 3170 with a `state_read:` line. A claim about what a unit carries is a grep for each fact. Dispatch texts never cite another unit's rules.
- Calm windows: 02:59 to 03:02Z, 08:00 to 08:25Z, 09:58 to 10:05Z, 11:25 to 11:40Z. Branch names carry the date; check HEAD before any amend.

## Open

- Owner: the dialog answer. Strategist: 12 overdue reads (due to Steer A 20:00Z); cycle E staged. Integrator: four old branches, work/gate-list-ignored.
- WEEKLY DIGEST owner lines (11-30): the Glittering Market mail residue; rename the board's Agent option from the owner's login to 'owner' (a ten-second settings edit, no token; Steer A 22:27Z; then the Toolsmith's two-line branch and the Scribe's lines 26 and 36 of the project-p1 page follow).
- Rotate at 85 to 88 percent in a gap with `spawn_seat.py`; record the id; tell Steer A. Never push local main; no checkout, switch, reset or stash in the live tree.
