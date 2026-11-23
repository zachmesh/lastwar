---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T04:14:00Z
level: L2
version: 0.3.0
description: The operator's live state after the move to the top-level session - game live, app approved, front-slot pre-start step mandatory
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: cu_bridge self-test 2026-11-22 19:13 PT
  - source: survivor unit record _records_/2026-11-22/survivor-intake/2003-queue-run.md, first landed play unit
  - source: coordinator tick _records_/2026-11-22/team-operations/2011-tick.md, top-level operator spawn
---

# Handover - operator

Updated 2026-11-23 04:14Z (2026-11-22 20:14 PT).

## Holder

- Seat: `operator`, session `session-b718c7de-6aab-4159-b87e-41aa424237e9`
  (`[Last War] Operator`, top-level), since 2026-11-23T04:12:26Z.
- Predecessor: delegated child session `238b9ce7-1c06-4bc5-9901-42aa8b27e087`
  of the Steward, from 2026-11-23T03:08Z to 04:12Z. It is idle, holds no
  claim and no token, and is no longer dispatched. DSH routes messages to it
  only through its parent ("owned by subagent routing"), so the coordinator
  could not reach it - the reason for the M2 spawn.
- Scope: `_queue_/claimed/`, `_queue_/done/`, `_records_/<date>/`,
  `_tools_/state/`; code and profiles are excluded.

## State

- The game is live. The owner approved `com.lastwar.ios` with Always allow at
  about 19:55 PT; the approval is persistent.
- Units played on this Mac so far: harvest 1955 failed and radar 2000 failed,
  both with zero clicks landed because a system surface held the front slot;
  survivors 2003 done, the first unit whose clicks landed.
- First assignment of this holder: `A-20261123-0411-operator`,
  unit `donations-2026-11-22-1803`.

## Mandatory pre-start step, every play unit

In the same shell, immediately before `cu_bridge.py start`:

    killall -9 UserNotificationCenter NotificationCenter
    lsappinfo front

`lsappinfo front` must name LastWar. If it does not, do not start the run:
release the unit and the token and reply `blocked: foreground`.

## Lessons

- One device token, one desktop run. A second input path is a defect.
- A run that ends `waiting_for_person` is `blocked`, with the control link;
  never `done`.
- Never `open_app` when the game is already running; activate the existing
  window (duplicate-window finding, Issue #822).
- `queue.py claim` refuses a unit before its `not_before`; pick from
  `queue.py next`, never by name ahead of its window.
