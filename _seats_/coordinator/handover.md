---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T16:19:00Z
level: L2
version: 0.17.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, the growth Epic, in-flight landings and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 16:10Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s: `tool_sync.py`, `model_guard.py --apply`, then `queue.py next`); daily `schedule-e1887d97` 12:00Z (word-budget watch; wakes Coach and Planner); weekly `schedule-fee71877`.
- TEAM.yaml 0.7.3, 10 seats; the operator's current id is in TEAM.yaml. Steer A (`session-eb024f72-e661-4a77-9303-66af95dbcfd1`) and Steer B (`session-e127662e-07ba-4385-b905-3d0e90fd1eeb`) relay the owner and settle collisions between themselves.

## Triggers (each dispatches the operator BY NAME; check the desktop lock first)

Builders 2026-11-24T09:21Z `schedule-f3804b22`; forecast-refusal flip 2026-11-24T00:05Z `schedule-41383442`; Complete times 17:30:30Z `schedule-de14b612`. Quiet windows for the cu team: 08:00Z to 08:25Z daily and three one-offs today; during one, claim nothing, press nothing; the cu team takes the device token with `--exclusive`. A TIPS 'different device' dialog means STOP: never Confirm without the owner.

## Oil Well chain (from 2026-11-24 09:21Z)

Units `building-queues-oil-well-2026-11-24-001` to `-010` (Lv.20 to 30, iron only) sort last in `queue.py next`: DISPATCH EACH BY NAME at the real finish. After the operator reports unit N's finish time, create a one-shot at finish plus 30 s that dispatches N+1 and says to create the next. Earliest finishes: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`; Lv.24 to 25 may fall in the quiet window.

## Respawn and landings

On the HARNESS meter (`session-relay inspect` context percent, not the seat's own estimate) at 88 percent or failing compaction, in a quiet window or a gap between units, never in a Complete or a plunder session, with the seat's handover under 500 words: `python3 _tools_/spawn-seat/spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>`; record the id in TEAM.yaml, the handover and /tmp/lw-new-operator-id.txt; tell Steer A; stand the old session down. Landings (Integrator; never push local main): stage explicit paths, commit, `git branch land/records-<UTC> HEAD`, verify in a CLEAN worktree (`check --base origin/main --landing`) and with `/tmp/lw-scan-branch.py`, hand over the name; after each merge `git fetch && git rebase --autostash origin/main`. No checkout, switch, reset or stash in the live tree.

## Facts to carry

- Research speed measured: divisor 3.678 (plus 268 percent); read the Finish Now clock. Oil, not the labs, limits the date if the speed-up stock is spent.
- Standing rule (Steer A): anything that could open another app, browser, store or payment surface needs his approval first; an unexpected foreground switch stops the run; consent requests are human-only; only the operator seat touches the desktop (others: `lsappinfo front` at most, no osascript).
- Owner orders: Base Expansion first (OD-18, -19, -22); truck plunder with a casualty guard (OD-20).

## Open owner decisions

OD-20261123-21: was the second device the owner (likely yes)? D-066: the owner-idle opt-out (`work/owner-idle-restore` held).
