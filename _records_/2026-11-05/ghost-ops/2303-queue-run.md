---
title: Ghost Ops queue run 2303
created: 2026-11-06T07:14:00Z
modified: 2026-11-06T07:14:00Z
level: L0
version: 1.0.0
description: Ticker-2303 ghost-ops unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 2303 queue run - Ghost Ops

Executor: ticker-2303. Unit: ghost-ops-2026-11-05-0000.
Session window about 23:10 to 23:14 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the Secret Command Post Ghost Ops tab was never opened, the
  Thursday missions, help count and claimable rewards were never
  read, and nothing was claimed. The loss is the unexecuted
  Ghost Ops Thursday check and the missing closing read for this
  slot.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 15 hours 35 minutes at the
  23:11 re-check, unchanged since the ticker-1025 pass and
  identical to the ticker-2152 pass reading.
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
  each, so nothing new would be learned by repeating them
  (same reasoning as the ticker-2152 pass).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the sixty-second
  recorded consecutive pass with a Mac device-access blocker,
  twenty-third in the worsened zero-response form. The last
  recorded one was ticker-2152, the sixty-first and
  twenty-second. Passes between 2152 and 2303 left no record
  on the branch, so the true consecutive count may be higher;
  this pass counts recorded passes only. This pass commented on
  #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 71 units at this pass (73
  after the zero-sweep pair was restored to the live pool).

## Other pass steps

- Own PRs checked first: the four open records PRs
  (324 for 2026-11-01, 265 for 2026-11-02, 256 for
  2026-11-03, 301 for 2026-11-04) all conflicted on the
  single file _logs_/repo-actions/action-log.jsonl
  (append-append) against current main dd95a0d8, per the
  integrator 2045 re-check. This pass reconciled all four
  on the branch side (merged main, union of the action-log
  appends deduplicated and ordered by timestamp, 938/938/
  941/941 lines), pushed each via the bundle route and
  commented on each PR. All four should now be mergeable
  at the next batch point. PR 340 (records/2026-11-05,
  post-1900 batch) has merged; this pass opens a new
  post-2300 batch PR for records/2026-11-05.
- Sync: reaped 0, expired 5 (events, passes, secrets,
  treasures and trucks 2026-11-05-1857, window passed
  before execution), due 21, produced nothing new, all
  21 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06): the ticker-2152 pass
  staged the pair, but only onto the records branch - the
  live pool inbox did not hold them, so they could not
  execute. This pass copied the two branch files verbatim
  into the live pool inbox (not_before 2026-11-07T01:30:00Z
  and 02:30:00Z, both priority 1, expiring at the reset
  2026-11-07T03:00:00Z). No new enqueue was created, so
  the branch copy is unchanged.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the ghost-ops unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Ghost Ops tab read, no missions run, no help given,
no rewards claimed. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
