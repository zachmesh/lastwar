---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T01:12:00Z
level: L2
version: 0.20.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, the growth Epic, in-flight landings and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 20:20Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: `tool_sync.py`, `model_guard.py --apply`, `queue.py next`); daily `schedule-e1887d97` 12:00Z (word budget; wakes Coach and Planner); weekly `schedule-fee71877`.
- TEAM.yaml 0.7.4, 10 seats (the operator's id is there). Steer A (`session-eb024f72-e661-4a77-9303-66af95dbcfd1`) and Steer B (`session-e127662e-07ba-4385-b905-3d0e90fd1eeb`) relay the owner and settle collisions.

## Triggers (each dispatches the operator BY NAME; check the desktop lock first)

Builders free 2026-11-23T23:20:12Z TODAY (not 09:20Z: a misread): pre-check 23:10Z, ping 23:14:30Z, dispatch 23:21Z `schedule-f3804b22`; forecast flip 2026-11-24T00:05Z `schedule-41383442`; donation pass 21:15Z; Complete 17:30:30Z; cu quiet window 08:00Z to 08:25Z daily (claim nothing, press nothing; the cu team holds the device token with `--exclusive`). A TIPS 'different device' dialog means STOP: never Confirm without the owner.

## Oil Well chain (from 23:21Z today)

Units `building-queues-oil-well-2026-11-24-001` to `-010` (Lv.20 to 30, iron only) sort last in `queue.py next`: DISPATCH EACH BY NAME at the real finish: after the operator reports a finish time, create a one-shot at finish plus 30 s that dispatches the next unit and says to create the one after. Earliest finishes: `_records_/2026-11-22/queue-planning/3000-builders-free-at-2320z-today.md`.

## Respawn and landings

Respawn on the HARNESS meter (`session-relay inspect`, not the seat's estimate) at 88 percent, in a quiet window or a gap, never mid-Complete: `python3 _tools_/spawn-seat/spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>`; record the id in TEAM.yaml, the handover and /tmp/lw-new-operator-id.txt; tell Steer A; stand the old session down. Landings (Integrator; never push local main): stage explicit paths, commit, `git branch land/records-<UTC> HEAD`, verify in a CLEAN worktree (`check --base origin/main --landing`) and `/tmp/lw-scan-branch.py`, hand over the name; after a merge `git fetch && git rebase --autostash origin/main`. No checkout, switch, reset or stash in the live tree.

## Facts to carry

- Research divisor 3.678 (plus 268 percent): read the Finish Now clock.
- Standing rule (Steer A): anything that could open another app, browser, store or payment surface needs his approval first; an unexpected foreground switch stops the run; consent requests are human-only; only the operator seat touches the desktop (others: `lsappinfo front`, no osascript).
- The harness's own clicks count as idle input (self click): the wait is TEMPORARILY 0 (OD-27) until CU-720.
- Plunder scans 02:30Z to 06:00Z (one fight each, stop at 4/4): the trade icon (107,580) has been absent since 16:39Z; if scan 001 closes 'blocked by route: trade icon absent', HOLD 002 to 008 until the icon is seen (each blocked run costs the 300 s gate).

## Open owner decisions

- OD-20261123-21 (second device): the owner's phone donations raise the odds, not an answer: keep OPEN.
- CU-721 APPROVED (OD-28): worktree under computer-use-wt created by cu-integrator in a 08:00Z window; the Toolsmith restarts between runs; OD-27 (wait 0) ends then.
