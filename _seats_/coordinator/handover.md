---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T10:22:00Z
level: L2
version: 0.21.0
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

Pending one-shots: 10:25Z forecast flip (TEAM.yaml coordination.queue.require_forecast after the Strategist's fresh announcement; branch land/forecast-flip; Steer A probes a SCRATCH root); 14:15Z settle and dispatch the last two trucks; 15:04Z settle the SR then the four plunder scans (guards: hospital free room at least 1,000, stop after a fight wounding over 50); 17:28Z Oil Well Lv.24 hand-off (Lv.23 ends 17:27:27Z), 17:30:30Z lab Complete; 11-26 21:11:30Z room collect. OD-27 ended 08:36Z (bridge on lastwar-bridge). The tram icon opens Intercity Trade only WITH a badge. A TIPS 'different device' dialog means STOP: never Confirm. Any unexpected foreground switch: stop, answer nothing, tell Steer A.

## Oil Well chain

Units `building-queues-oil-well-2026-11-24-003` to `-010` (priority 9 until needed): DISPATCH EACH BY NAME at the real finish (the builders panel end, a flat 6 h 32 min under the preview); after each reply set a one-shot at finish plus 30 s; skip the 08:00Z window; re-rank B1 by power per builder-day and oil date. A finished building completes by tapping its wrapped gift box. Schedule: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`.

## Respawn and landings

Respawn on the HARNESS meter (`session-relay inspect`) at 88 percent, in a gap, never mid-Complete: `python3 _tools_/spawn-seat/spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>`; record the id in TEAM.yaml and /tmp/lw-new-operator-id.txt; tell Steer A; stand the old session down. Landings (Integrator; never push local main): stage explicit paths, commit, `git branch land/records-<UTC> HEAD`, verify in a CLEAN worktree (`check --base origin/main --landing`) and `/tmp/lw-scan-branch.py`, hand over the name; after a merge `git rebase --autostash origin/main`. No checkout, switch, reset or stash in the live tree.

## Facts to carry

- Standing rule (Steer A): anything that could open another app, browser, store or payment surface needs his approval first; an unexpected foreground switch stops the run; consent requests are human-only; only the operator seat touches the desktop (others: `lsappinfo front`, no osascript).
- The harness's own clicks count as idle input (self click): the wait is TEMPORARILY 0 (OD-27) until CU-720.
- Plunder: route unknown ((107,580) is the Alliance Train shortcut); verify every HUD icon by its label first. Guard: hospital free room under 1,000 stops. Room: a finished batch collects if the room covers it; press each barracks' pistol once per read.

## Open owner decisions

- OD-20261123-21 (second device): the owner's phone donations raise the odds, not an answer: keep OPEN.
- CU-721 APPROVED (OD-28): worktree under computer-use-wt created by cu-integrator in a 08:00Z window; the Toolsmith restarts between runs; OD-27 (wait 0) ends then.
