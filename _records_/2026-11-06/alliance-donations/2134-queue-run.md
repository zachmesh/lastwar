---
title: Alliance donations queue run 2134
created: 2026-11-07T05:54:00Z
modified: 2026-11-07T05:54:00Z
level: L0
version: 1.0.0
description: Ticker-2134 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 2134 queue run - Alliance donations

Executor: ticker-2134. Unit: donations-2026-11-06-1803.
Session window about 21:34 to 21:54 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, and
  the recovery channel timed out, so the Alliance Techs screen
  was never opened, no donation count was read live, and no coin
  donation was made. The loss is the unexecuted donations slot
  for this cycle (the daily 30 coin donations per reset day,
  coin button only).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 38 hours at the 21:53
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
- This is the ninety-first consecutive ticker pass with this
  Mac device-access blocker, fifty-second in the worsened
  zero-response form (ticker-2034 was the ninetieth /
  fifty-first, same blocker, arms-race-2026-11-06-1803 failed
  there). The tracker is untouched, so the next tick
  re-produces this regular.

## Queue-state note

- No working-tree divergence this pass. The pass fetched the
  remote tip first and worked in a fresh detached worktree of
  github/records/2026-11-06 at 6deba56400 (planner-2140 tip),
  verified identical on the VPS and on github. Sync reaped 0,
  expired 0, due 22, produced 0 (all already queued). No zombie
  seeding: the Zombie Invasion chain closed 2026-10-30 when the
  event ended, and no Zombie Invasion tab is to be seeded until
  one is seen live in the Events hub again.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  login or verification demanded (none was reachable), no
  different-device dialog seen.
