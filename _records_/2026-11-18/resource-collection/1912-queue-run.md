---
title: Harvest queue run 1912
created: 2026-11-19T03:18:00Z
modified: 2026-11-19T03:18:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-18-1803 failed - Last War game window unavailable on the Mac mini
---

# Harvest queue run 1912

- Executor: ticker-1912
- Unit: harvest-2026-11-18-1803 (regular harvest, activity resource-collection)
- Session window: 19:12-19:20 PST, 2026-11-18
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 19:13: 22 due, 0 produced (all already queued), 4 expired,
  1 completion marker reaped. Inbox holds 68 units.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- Token acquired by ticker-1912 until 19:30:47 PST. Next unit picked:
  harvest-2026-11-18-1803, claimed.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE again -
  device.list shows connection_state online, last seen 19:04:50 PST.
  This is a change from the offline state since 2026-11-15 05:19 PT.
- environment.describe lists LastWar among running apps, but the app
  has no window: computer.control activate failed with
  ax_windows_empty, and list_windows (11 windows, twice) lists no
  LastWar window. This is the same window-lost state as since
  2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-109:
  - open_app LastWar - outcome_unknown (action 0FC5E2DD)
  - computer.observe - observation_unavailable, no target window
  - activate LastWar - ax_windows_empty, no bound window
  - list_windows - no LastWar window
  - screen.snap - observation_unavailable
  - open_app LastWar again, after inspection - outcome_unknown
    (action D37CD988), still no window on the second list_windows
- No game input was possible, so no bubbles were collected and no
  resource totals were read. Nothing was tapped, spent, or claimed.
- The failure is device-level, not unit-level: every further unit in
  this pass would fail the same way, so the execute loop stops here
  instead of burning the pass on identical failures.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), same as since about 2026-11-12
  12:46 PT. The owner-chosen IONOS console recovery (2026-11-14)
  is still not landed or verified.
- Because the VPS is unreachable, the OWN PRS FIRST check (gh pr
  list / comments via the VPS gh CLI) could not run, and the
  push-and-PR delivery for this pass cannot run either: no bundle
  to the VPS, no push of records/2026-11-18, no PR check or
  creation. This pass is partial on delivery; its commits stay on
  the local records branch.
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state (2,503 changed paths,
  including staged deletions of tools/* while the files exist on
  disk). Per the task body, that state was not disturbed; this
  pass's records were committed from a temporary worktree instead.

## Consequences

- The 19:00 reset passed during this outage window with the VIP,
  passes, mail, gifts, help, events and other reset-day units still
  sitting in the inbox (68 units). Nothing due was played in this
  pass.
- The Mac being back online is new, but without a game window the
  ticker still cannot play. The wedged windowless LastWar process
  needs a quit-and-relaunch on the Mac (or the owner's intervention)
  before any ticker pass can execute again.
- Previous pass was also an access failure; this pass reports in
  Chinese per the reporting rule.
