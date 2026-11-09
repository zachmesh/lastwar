---
title: Radar queue run 0342
created: 2026-11-06T11:47:00Z
modified: 2026-11-06T11:47:00Z
level: L0
version: 1.0.0
description: Ticker-0342 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0342 queue run - Radar

Executor: ticker-0342. Unit: radar-2026-11-06-0203.
Session window about 03:42 to 03:47 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the radar release was never opened, no radar tasks were read,
  and nothing was claimed. The loss is the unexecuted radar
  release-day check for this slot (duel day 5, planned 02:03
  local 2026-11-06, expires 06:03 local 2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 20 hours 10 minutes at the
  03:47 re-check, unchanged since the ticker-0234 pass.
- Five device invokes, zero responses, all node_offline with
  "device is offline and does not advertise a wake-up path":
  connection.health (attempts 1 and 4), connection.repair web
  (attempt 2), computer.session start (attempts 3 and 5). This
  meets the standing retry rule of at least 3 attempts before
  recording a unit as access-failed.
- No recovery-device attempts were made in this pass: the
  recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c)
  is offline with the same frozen last_seen 15:36:52Z, and the
  ticker-0234 pass about an hour earlier attempted its recovery
  channel and timed out after 25 seconds, so nothing new would
  be learned by repeating it (same reasoning as the
  ticker-0104 pass).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the sixty-sixth
  recorded consecutive pass with a Mac device-access blocker,
  twenty-seventh in the worsened zero-response form. The last
  recorded one was ticker-0234, the sixty-fifth and
  twenty-sixth. No executed pass is recorded between 0234 and
  this one: the latest executed failure in the pool is the
  0234 passes unit (finished 10:39:34Z). This pass commented
  on #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 76 units at this pass's close
  (77 at sync).

## Other pass steps

- Own PRs checked first: PR 347 (records/2026-11-06) carried a
  new owner comment from the 03:00 batch pass - a merge
  conflict with main on _logs_/repo-actions/action-log.jsonl
  (append-append, main advanced by the merges of records PRs
  324 and 345). Reconciled on the branch side this pass:
  merged main 3b054bcf into records/2026-11-06 (commit
  9a716619ce, pushed and verified with git ls-remote) as the
  ordered union of both sides' appends (937 base + 7 branch +
  4 main = 948 lines, no duplicates, no lines dropped), and
  replied on PR 347. PR 351 (records/2026-11-05 post-0300
  batch) has no comments.
- Sync: reaped 0, expired 0, due 20, produced nothing new, all
  20 regulars already queued. Note: four 2257-slot units
  (events, secrets, treasures, trucks, all 2026-11-05) sit in
  done with status expired and finished_at 2026-11-06T11:41:17Z
  (03:41:17 local), before this pass's sync - they were already
  reaped when this pass started, so this pass's sync reported
  expired 0.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (not_before 01:30Z and 02:30Z on 2026-11-07, expires
  03:00Z); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the radar unit.
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

Failed. No radar screen read, no tasks run, no rewards claimed.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
