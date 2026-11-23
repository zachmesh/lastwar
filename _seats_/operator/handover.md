---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:22:00-08:00
level: L2
version: 0.2.0
description: The operator's live state after establishment - game stopped, bridge ready, first play not yet run
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: cu_bridge self-test 2026-11-22 19:13 PT
---

# Handover - operator

Updated 2026-11-22 19:22 PT.

## Holder

- Seat: `operator`, session `session-238b9ce7-1c06-4bc5-9901-42aa8b27e087`.
- Scope: `_queue_/claimed/`, `_queue_/done/`, `_records_/2026-11-22/`,
  `_tools_/state/`; code and profiles are excluded.

## State

- The game is stopped by the owner. Do not start it.
- The device token is free; no unit is claimed.
- The bridge `_tools_/cu_bridge.py` passes `self-test` with
  `computer_use_start`, `_status`, `_respond` and `_control`.
- The Last War app `com.lastwar.ios` has never been approved by a person in
  the computer-use app store. The first desktop run will wait; the owner
  approves it through the control link printed by `start`, in a real
  terminal. Never approve an app through the bridge.
- The next queue unit is `harvest-2026-11-22-1803` at the genesis pool, but
  no play starts until the owner restarts the game.

## First turn after restart

1. `python3 _tools_/cu_bridge.py ensure` and `self-test`.
2. Start one state-read run with `start --task "Read the Last War base
   screen and report the visible panels, red dots and resource totals;
   do not tap anything" --max-steps 4 --max-minutes 5`.
3. Print the control-link command and wait for the owner's approval.
4. Record the observation, then claim one low-risk unit. Never run a second
   desktop run while the first is live.

## Lessons

- One device token, one desktop run. A second input path is a defect.
- A run that ends `waiting_for_person` is `blocked`, with the control link;
  never `done`.
