---
title: Queue Ticker 0404 Run - Survivors Access Failed
created: 2026-11-16T12:26:00Z
modified: 2026-11-16T12:26:00Z
level: L0
version: 1.0.0
description: Ticker 0404 pass - survivors unit failed, Mac mini offline since 2026-11-15 05:19 PT, 3 session probes node_offline with no wake-up path; 13th consecutive ticker pass to fail on the offline Mac; VPS SSH still denied, no PR check or push possible
activity: survivor-intake
run_id: ticker-0404
trigger: schedule (dependency_probe)
started_at: 2026-11-16T12:04:00Z
finished_at: 2026-11-16T12:26:00Z
duration_seconds: 1320
status: failed
---

# 0404 queue run - survivors access-failed

## Session

- Executor ticker-0404, 04:04 to about 04:26 PT, 2026-11-16.
- Token taken 12:13Z; unit survivors-2026-11-16-0203 picked by
  `queue.py next` (earliest expiry), claimed 12:18:11Z.
- Sync: 22 due, 0 produced (all already queued by the planner);
  one completion marker reaped (radar-2026-11-16-0203); no
  expired units, no stale done dropped.
- Zombie seeding skipped: the Glacieradon event ended and chain
  zombie-2026-11-10 was closed by unit 037 on 2026-11-15
  (no Zombie Invasion tab in the Events hub); no fresh chain
  until a Zombie Invasion tab is seen live again.

## What happened

- Device probes: computer.session start, three attempts
  (about 04:17, 04:19 and 04:21 PT) - all failed
  node_offline, "device is offline and does not advertise a
  wake-up path". device.list and device.describe agree:
  Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19:56 PT).
- This is a physical channel block, not an authorization
  failure: the owner authorization stands (2026-10-26);
  the machine is unreachable. No game input was dispatched.
- Unit completed as failed (blocker_category f, missing
  precondition - device offline); tracker untouched, as
  the rules require for failed units. One unit only: the
  blocker is device-wide, so further units this pass would
  fail identically; no further claims were made.
- Thirteenth consecutive ticker pass to fail on the offline
  Mac (ticker-0004 at 00:10 PT was the sixth, per the
  2026-11-15 23:40 planning record; ticker-0112, 0134,
  0204, 0234, 0304 and 0334 followed with one failed unit
  each, all node_offline).

## What was not done

- No survivors taken in, nothing claimed, no game state read.
- OWN PRS FIRST could not run: VPS SSH still returns
  "Permission denied (publickey)" (tested 04:05 PT) - the
  2026-11-12 ~/.ssh loss is still unrepaired; the owner
  chose the IONOS-console recovery on 2026-11-14, not yet
  landed. No PR comments were read and none were answered.
- No push and no PR: same VPS break. This record is
  committed locally on branch ticker-0404-1116-delivery,
  UNPUSHED - push via the standard VPS route once SSH
  returns. No records PR exists for 2026-11-16 work from
  this pass.

## Follow-up

- Retry next tick when the Mac is back online; the
  survivors-2026-11-16-0203 unit carries attempt 1 of 3.
- The Mac has now been offline about 23 hours. Nothing
  further this pass can do: both the game route (Mac) and
  the delivery route (VPS SSH) are down.
