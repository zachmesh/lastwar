---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-25T04:00:00Z
level: L2
version: 0.24.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, schedules, the trade cycle, the macOS alert and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-25 04:00Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: tool_sync, model_guard, `queue.py next`; `next` can name a moot or blocked unit: check). Planner ping `schedule-4803c6f4` (02, 06, 10, 14, 18, 22Z); daily `schedule-e1887d97` 11:55Z; weekly `schedule-fee71877` 11-30 01:00Z (scout seat: retire or assign).
- TEAM.yaml 0.7.5, 10 seats; the operator's id is in /tmp/lw-new-operator-id.txt. Steer A `session-eb024f72-e661-4a77-9303-66af95dbcfd1` and Steer B `session-e127662e-07ba-4385-b905-3d0e90fd1eeb` relay the owner. Meters 04:00Z: me 74, operator 62, toolsmith 69, coach 61.

## Dispatch (the operator BY NAME, one claim at a time; lock and `lsappinfo front` first)

Wakes are in `schedule_list`: pass 010 04:08Z (ends before 04:28Z), pass 011 07:10Z; cycle D 06:40:30Z (trucks return UR 06:19:17, SR 06:19:38, SSR 06:39:30Z); Oil Well Lv.24 hand-off 07:11:50Z (end 07:11:19.6Z; builder first); room collect 11-25 13:39:30Z (Lv.26 ground ends 13:38:36Z; the freed builder's job is still the Strategist's); lab Completes 19:39:30Z and 11-26 08:38Z; hospital read 11-27 00:30Z (siege 01:15Z). Claim units the planner staged: refugee 04:21Z (expires 04:29Z), rescue-depot 07:25Z. Calm: 04:30 to 04:45Z, cu 08:00 to 08:25Z, owner job 09:58 to 10:05Z and 02:59 to 03:02Z, cu nightly 11:25 to 11:40Z.

## Rules learned

- Composed pan (one message): mouse_move, left_mouse_down, wait 1, one 175 px move, wait 1, left_mouse_up, screenshot: 150 px from the right margin (Weekly Pass, History) or the centre of a tile gap (Backpack); a refused pan sends Escape and a button-up to the outside app (CU-794, not before 08:25Z).
- Tram badge equals the Your Truck tab (returned trucks plus empty slots below 5; the reset lights it). No badge: WORLD then BASE, read once. Downgrade test: one extra refresh on the first SR truck, five tests.
- HUNG SCREEN (15 minutes): dispatch the relaunch unit, tell Steer A after. Never open the lottery tab; never tap the avatar; Backpack reads only for a plan reason; a new unit names its value.
- Closing rule 3170: DONE for a claim or a verified nothing-to-do with a `state_read:` line. A dispatch text never cites another unit's rules.
- Branch names carry the date; check HEAD before any amend; name a count by its tile.

## Owner and alerts

OD-20261125-01 to 04: the macOS prompt is handled (if one returns: tell Steer B, the operator holds, five minutes at most); ai-sync is his job; OD-21 closed (11-24 15:56 to 17:31Z and the second box drain stay unattributed); the siege stays.

## Open

- Steer A: VIP avatar exception (A or B); composed pans meanwhile. Strategist: H81 and H118, the freed builder. Integrator compacted (46 percent): branches pending.
- Rotate at 85 to 88 percent in a gap, never mid-cycle, with `spawn_seat.py`; record the id; tell Steer A. Never push local main; no checkout, switch, reset or stash in the live tree.
