---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T16:20:00Z
level: L2
version: 0.22.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, schedules, the trade cycle, the macOS alert and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-24 16:20Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: `tool_sync.py`, `model_guard.py --apply`, `queue.py next`). Planner ping `schedule-4803c6f4` at 02, 06, 10, 14, 18, 22Z; daily `schedule-e1887d97` 11:55Z; weekly `schedule-fee71877` 11-30 01:00Z (add: retire or assign the scout seat).
- TEAM.yaml 0.7.5, 10 seats; the operator's id is in /tmp/lw-new-operator-id.txt. Steer A `session-eb024f72-e661-4a77-9303-66af95dbcfd1` and Steer B `session-e127662e-07ba-4385-b905-3d0e90fd1eeb` relay the owner.

## Dispatch (the operator BY NAME, one claim at a time; lock and `lsappinfo front` first)

Wakes: 17:28Z Oil Well Lv.24 hand-off (Lv.23 ends 17:27:27.5Z), 17:30:30Z lab, 17:50Z pass 007, 18:03:30Z badge probe then cycle B2 (`trucks-dispatch-2026-11-24-005`, on a LIT badge: settle the SR first, two fights, History read), B3 `-010` 18:50Z (UR), pass 008 21:10Z, 009 00:40Z, 010 04:30Z, 011 07:10Z, cycle C 02:15Z, 11-26 21:11:30Z room collect. Set a wake for every staged pass.

## Rules learned

- Composed pan recipe (clipped pages, margin start, one message): mouse_move, left_mouse_down, wait 1, one move of 175 px, wait 1, left_mouse_up, screenshot; moves 150 px. The Backpack grid ignored it (0 px).
- The tram badge: a returned unsettled truck lights it (can lag); no badge, no tap. Hospital free room 1,000 stops plunder.
- Closing rule 3170: DONE for a taken claim or a `state_read:` line; else PARTIAL.
- Contract refresh caps: ten a slot, 60 a day, floor 80; one downgrade test in cycle C.
- Branch names carry the date; yesterday's land/records-1609 collided once.

## The macOS alert

A Screen Recording re-approval for CUHelper, every about 6 h 31 min (02:34, 09:05, 15:36Z; next about 22:07Z and 04:38Z). Only the owner can answer. Never touch it: hold, then after the deadline (5 minutes now) the operator runs the standing killall once and once more if it respawns. Keep 22:00Z to 22:15Z calm.

## Open

- Steer A decides the Backpack rows 4 (park, select tiles, or wheel) and OD-21 (second device).
- Pending seat work: the Toolsmith's `state_read` validation and units-share alarm line; the Strategist's overdue reads; Integrator branches.
- Respawn at 88 percent on the harness meter in a gap: `spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>`; record the id; tell Steer A. Landings: Integrator; never push local main; no checkout, switch, reset or stash in the live tree.
