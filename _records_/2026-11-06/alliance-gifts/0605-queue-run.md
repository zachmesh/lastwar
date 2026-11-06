---
title: Gifts queue run 0605
created: 2026-11-06T14:05:00Z
modified: 2026-11-06T14:12:00Z
level: L0
version: 1.0.0
description: Ticker-0604 gifts unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0605 queue run - Gifts

Executor: ticker-0604. Unit: gifts-2026-11-06-0230.
Session window about 06:04 to 06:12 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so no Regular or Premium gift tab was opened, no
  Claim All was tapped, and no gift count was verified. The loss
  is the unexecuted alliance-gifts check for this slot.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 22 hours 35 minutes at the
  06:10 re-check, unchanged since the ticker-0534 pass. The
  last_seen value is known-stale (it did not move while
  ticker passes played the game on 2026-11-05), so it is
  reported as the listed value only, not as the outage start.
- Five device invokes, zero responses:
  - computer.session start, three attempts, all node_offline
    with "device is offline and does not advertise a wake-up
    path" (attempts 1, 4, 5; the last after a 60 second wait).
  - Recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
    connection.health timed out after 25 seconds (attempt 2),
    connection.repair native timed out after 25 seconds
    (attempt 3). Same timeout form the ticker-2041 pass saw;
    the recovery channel is not usable either.
- This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed, and it is not the
  unreliable "lacks owner-authorized device access" error:
  the error is node_offline on the transport, with no wake-up
  path advertised.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the seventy-first
  recorded consecutive pass with a Mac device-access blocker,
  thirty-second in the worsened zero-response form. The last
  recorded one was ticker-0534, the seventieth and
  thirty-first. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 71 units at this pass's close (71 at sync).

## Other pass steps

- Own PRs checked first: PR 347 (records/2026-11-06, the live
  records PR for today) carries no unanswered question - its
  newest comment is the ticker-0342 branch-side reconciliation
  (merged main 3b054bcf, commit 9a716619ce). The other open
  records PRs name lastwar-pr-integrator as Owner, not this
  job. No PR action needed this pass.
- Sync: reaped 0, expired 1, due 20, produced nothing new, all
  20 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the gifts unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed. PR 347 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No gifts claimed on either tab, no gift count verified.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
