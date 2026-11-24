---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T20:30:00Z
level: L2
version: 0.23.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, schedules, the trade cycle, the macOS alert and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-24 20:30Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: `tool_sync.py`, `model_guard.py --apply`, `queue.py next`). Planner ping `schedule-4803c6f4` (02, 06, 10, 14, 18, 22Z); daily `schedule-e1887d97` 11:55Z; weekly `schedule-fee71877` 11-30 01:00Z (scout seat: retire or assign).
- TEAM.yaml 0.7.5, 10 seats; the operator's id is in /tmp/lw-new-operator-id.txt. Steer A `session-eb024f72-e661-4a77-9303-66af95dbcfd1` and Steer B `session-e127662e-07ba-4385-b905-3d0e90fd1eeb` relay the owner.

## Dispatch (the operator BY NAME, one claim at a time; lock and `lsappinfo front` first)

Wakes (all one-shots): donation passes 008 21:10Z, 009 00:40Z, 010 04:30Z, 011 07:10Z (the hand-off first); extra planner ping 11-25 03:15Z; Coach wake 05:45Z (box test); Oil Well Lv.24 hand-off 07:11:50Z (end 07:11:20Z); lab Completes 11-25 19:39:30Z and 11-26 08:38Z; room collect 11-26 11:09:30Z (Lv.26 ground ends 11:08:36.6Z). Cycle C `trucks-dispatch-2026-11-24-004` opens 02:15Z, D `-006` 06:40Z; the 22:03Z wave opens 22:16Z.

## Rules learned

- Composed pan (one message): mouse_move, left_mouse_down, wait 1, one 175 px move, wait 1, left_mouse_up, screenshot: moves 150 px on the Weekly Pass page and History list; 0 px on the Backpack, shop cards and Store list.
- Tram badge is a STALE DOT: no badge at the first read means WORLD then BASE (one tap each, no icon), then read once: lit means enter; else close 'badge absent' (3 tries). A lone returned truck lights it; an empty slot at 5/5 does not. HUNG SCREEN (15 minutes, one back-arrow tap unchanged): I dispatch the relaunch unit at once (Steer A's standing rule 20:26Z: app menu Quit, front script, one Confirm at most, re-read the timers, cap 0.60 USD) and tell him after; never open the lottery tab.
- Closing rule 3170: DONE for a taken claim or a verified nothing-to-do with `state_change: no` and a `state_read:` line; else PARTIAL. `require_state_read` stays off until the audit shows 80 percent for two days.
- Contract refresh caps: ten a slot, 60 a day, floor 80. Plunder 4/4 today; 8 fights, 0 wounded.
- Branch names carry the date. The operator re-reads counters before any cost (another actor moved coin on 11-24).

## The macOS alert

A Screen Recording re-approval for the helper (CUHelper), at 02:34, 09:05 and 15:36Z (about 6 h 31 min); only the owner can answer. The owner restarted the game at 17:04Z (probably answering it); the next may not come: keep 22:00Z to 22:15Z calm anyway. Never touch it: hold 5 minutes, then the standing killall (twice if it respawns).

## Open

- Pending: OD-21 (second device); Backpack and Store row reads (parked); the Toolsmith's units-share alarm line; the Strategist's overdue reads; Integrator branches.
- Respawn at 88 percent on the harness meter in a gap: `spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>`; record the id; tell Steer A. Never push local main; no checkout, switch, reset or stash in the live tree.
