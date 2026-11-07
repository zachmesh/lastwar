---
title: Survivor intake queue run 2004
created: 2026-11-07T04:11:00Z
modified: 2026-11-07T04:11:00Z
level: L0
version: 1.0.0
description: Ticker-2004 survivors unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 2004 queue run - Survivor intake

Executor: ticker-2004. Unit: survivors-2026-11-06-1803.
Session window about 20:04 to 20:11 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, and
  the recovery channel timed out, so no survivor was taken in,
  no gate line was verified, and no Quick Dispatch ran. The loss
  is the unexecuted survivors slot for this cycle.
- Live duel posture from tools/duel.py at 20:09 local: duel day
  6, Enemy Buster, radar posture stack (day ends 2026-11-07
  18:00 local, 21.8 hours left). Combat is owner-led; nothing
  in this unit touches combat.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 36 hours 40 minutes at the
  20:09 re-check, unchanged since the ticker-1025 pass on
  2026-11-05. The last_seen value is known-stale (it did not
  move while ticker passes played the game on 2026-11-05), so
  it is reported as the listed value only, not as the outage
  start.
- Six substantive device invokes, zero responses:
  - Mac mini connection.health, node_offline.
  - Mac mini connection.repair (web), node_offline.
  - Mac mini computer.session start x3, node_offline.
    All five with "device is offline and does not advertise a
    wake-up path".
  - Recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
    connection.health timed out after 25 seconds.
- This is the eighty-ninth consecutive ticker pass with this
  Mac device-access blocker, fiftieth in the worsened
  zero-response form (ticker-1934 was the eighty-eighth /
  forty-ninth, same unit family, radar-2026-11-06-1803 failed
  there). The tracker is untouched, so the next tick
  re-produces this regular.

## Queue-state note

- This pass first claimed radar-2026-11-06-1803 in the stale
  local working tree (branch work/ops-execution-records, last
  records commit 2026-11-03), where it still sat in inbox.
  That unit is already done/failed on the live records branch
  (ticker-1934, PR 374). The claim was reverted in the local
  tree (file restored to inbox, attempts back to 0, token file
  removed) and the pass continued in a temporary worktree of
  github/records/2026-11-06 at 7018a228f6, where sync produced
  nothing new and the next due unit was survivors-2026-11-06-1803.
  The local working tree and the records branch queue states
  have diverged - the same divergence class the 2026-11-01
  0041 survivors record named as an open process item. No
  duplicate issue is filed here; the divergence is named in
  this record and in the Issue 284 comment for this pass.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  login or verification demanded (none was reachable), no
  different-device dialog seen.
