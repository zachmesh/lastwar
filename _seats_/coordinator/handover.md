---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-25T22:30:00Z
level: L2
version: 0.25.1
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

## The halt (since 06:25:52Z)

The game shows 'active on a different device' (the owner's phone): NOTHING is pressed or dispatched without the owner's word (OD-20261125-01 to 04, Steer A 06:36Z); Steer B holds the question. Two builders idle (Oil Well, Lv.26 ground ended 13:38:36Z). After his word the front script restores LastWar, then (Steer A 17:47Z): the radar unit and the duel-score claim FIRST (the duel chests, value 35,650, expire 02:00Z; radar tasks cannot be done after the reset), then Oil Well `-005`, Drill Ground hand-off (preview, preconvert, floors), cycle D, room collect, UR claim, train batch (75 to 115 minutes). A cu test's Chrome notification window stands (the owner's to dismiss).

## Rules learned

- Composed pan: mouse_move, left_mouse_down, wait 1, one 175 px move, wait 1, left_mouse_up, screenshot, only from blank ground or a tile gap (never on a building: move mode).
- Tram badge equals the Your Truck tab. HUNG SCREEN (15 min): relaunch unit, tell Steer A after. Never the lottery tab; the avatar only by the VIP unit's named exception.
- Closing rule 3170 with a `state_read:` line. A claim about what a unit carries is a grep for each fact. Dispatch texts never cite another unit's rules.
- Calm windows: 02:59 to 03:02Z, 08:00 to 08:25Z, 09:58 to 10:05Z, 11:25 to 11:40Z. Branch names carry the date; check HEAD before any amend.

## Open

- Owner: the dialog answer. Strategist: 12 overdue reads (due to Steer A 20:00Z); cycle E staged. Integrator: four old branches, work/gate-list-ignored.
- WEEKLY DIGEST owner lines (11-30): the Glittering Market mail residue; rename the board's Agent option from the owner's login to 'owner' (a ten-second settings edit, no token; Steer A 22:27Z; then the Toolsmith's two-line branch and the Scribe's lines 26 and 36 of the project-p1 page follow).
- Rotate at 85 to 88 percent in a gap with `spawn_seat.py`; record the id; tell Steer A. Never push local main; no checkout, switch, reset or stash in the live tree.
