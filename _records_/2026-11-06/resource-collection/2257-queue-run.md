---
title: Resource collection queue run 2257
created: 2026-11-07T07:04:00Z
modified: 2026-11-07T07:04:00Z
level: L0
version: 1.0.0
description: Ticker-2257 harvest unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 2257 queue run - Resource collection

Executor: ticker-2257. Unit: harvest-2026-11-06-2203.
Session window about 22:57 to 23:04 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, and
  the recovery channel timed out, so the base view was never
  opened, no bubble was read live, and no resource was collected.
  The loss is the unexecuted harvest slot for this cycle (the
  full-map bubble sweep to zero remaining, Season 2 area
  excluded, armed-truck loot check outstanding since the
  2026-11-01 1101 close).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 39 hours at the 23:02
  re-check, unchanged since the ticker-1025 pass on
  2026-11-05. The last_seen value is known-stale (it did not
  move while ticker passes played the game on 2026-11-05), so
  it is reported as the listed value only, not as the outage
  start.
- Six substantive device invokes, zero responses:
  - Mac mini computer.session start x3, node_offline.
  - Mac mini connection.health, node_offline.
  - Mac mini connection.repair (web), node_offline.
    All five with "device is offline and does not advertise a
    wake-up path".
  - Recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
    connection.health timed out after 25 seconds.
- This is the ninety-second consecutive ticker pass with this
  Mac device-access blocker, fifty-third in the worsened
  zero-response form (ticker-2134 was the ninety-first /
  fifty-second, same blocker, donations-2026-11-06-1803 failed
  there). The tracker is untouched, so the next tick
  re-produces this regular.

## Queue-state note

- No working-tree divergence this pass. The pass fetched the
  remote tip first and worked in a fresh detached worktree of
  github/records/2026-11-06 at f5a85928e0 (planner-2240 tip),
  verified identical on the VPS and on github. Sync reaped 0,
  expired 6, due 22, produced 1 (duel-score-2026-11-06-2230;
  the other 21 already queued). No zombie seeding: the Zombie
  Invasion chain closed 2026-10-30 when the event ended, and no
  Zombie Invasion tab is to be seeded until one is seen live in
  the Events hub again.
- The 22:04 tick executed no unit: the newest executed closing
  before this pass was the 21:53 ticker-2134 close, and the day
  INDEX already carries ticker-2204 as a pass with no record on
  either branch. This pass does not resolve that gap; it is
  already tracked by the organizer and pr-catchall jobs.
