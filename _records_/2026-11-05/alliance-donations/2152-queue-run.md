---
title: Donations queue run 2152
created: 2026-11-06T06:05:00Z
modified: 2026-11-06T06:05:00Z
level: L0
version: 1.0.0
description: Ticker-2152 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 2152 queue run - Alliance donations

Executor: ticker-2152. Unit: donations-2026-11-05-1803.
Session window about 21:52 to 22:05 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  Alliance Techs could not be opened, the live Donation Count
  was never read, no coin donation was made and nothing was
  claimed. The loss is the unexecuted donation work and the
  missing closing read for this slot.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 14 hours 25 minutes at the
  22:01 re-check, unchanged since the ticker-1025 pass.
- Five device invokes, zero responses, all node_offline with
  "device is offline and does not advertise a wake-up path":
  connection.health (attempt 1), computer.session start
  (attempts 2 and 4), connection.repair web (attempt 3),
  connection.health again (attempt 5). This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.
- No recovery-device attempts were made in this pass: the
  recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c)
  is offline with the same frozen last_seen 15:36:52Z, and its
  attempts in the ticker-2041 pass timed out after 25 seconds
  each, so nothing new would be learned by repeating them.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the sixty-first
  recorded consecutive pass with a Mac device-access blocker,
  twenty-second in the worsened zero-response form. The last
  recorded one was ticker-2041, the sixtieth and twenty-first.
  Ticker-2104 (like 2004 and 2034) left no record on the
  branch, so the true consecutive count may be higher; this
  pass counts recorded passes only. This pass commented on
  #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 69 units at this pass.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 340 (records/2026-11-05, post-1900 batch), Owner
  lastwar-pr-integrator, with no comments. No question
  addressed to this job, so nothing was owed before game work.
- Sync: reaped 0, expired 0, due 23, produced nothing new,
  all 23 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair staged for the 2026-11-06 19:00
  reset, chain pre-reset-sweep-2026-11-06: unit 001
  not_before 2026-11-07T01:30:00Z, unit 002 not_before
  2026-11-07T02:30:00Z, both priority 1, expiring at the
  reset 2026-11-07T03:00:00Z. Tonight's pair expired
  unexecuted on the same Mac device blocker, second
  consecutive night.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the donations unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Donation Count read, no donation made, no
diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 30, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
