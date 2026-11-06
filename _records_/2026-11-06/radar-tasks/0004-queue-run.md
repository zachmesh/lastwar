---
title: Radar queue run 0004
created: 2026-11-06T08:30:00Z
modified: 2026-11-06T08:30:00Z
level: L0
version: 1.0.0
description: Ticker-0004 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0004 queue run - Radar

Executor: ticker-0004. Unit: radar-2026-11-05-2203.
Session window about 00:17 to 00:30 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the radar release was never opened, no radar tasks were read,
  and nothing was claimed. The loss is the unexecuted radar
  release-day check for this slot (duel day 5).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 16 hours 50 minutes at the
  00:20 re-check, unchanged since the ticker-2303 pass.
- Five device invokes, zero responses, all node_offline with
  "device is offline and does not advertise a wake-up path":
  connection.health (attempts 1 and 5), computer.session start
  (attempts 2 and 4), connection.repair web (attempt 3). This
  meets the standing retry rule of at least 3 attempts before
  recording a unit as access-failed.
- No recovery-device attempts were made in this pass: the
  recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c)
  is offline with the same frozen last_seen 15:36:52Z, and its
  attempts in the ticker-2041 pass timed out after 25 seconds
  each, so nothing new would be learned by repeating them
  (same reasoning as the ticker-2152 and ticker-2303 passes).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the sixty-third
  recorded consecutive pass with a Mac device-access blocker,
  twenty-fourth in the worsened zero-response form. The last
  recorded one was ticker-2303, the sixty-second and
  twenty-third. This pass commented on #284 instead of
  filing a duplicate. Until the Mac gateway recovers, further
  ticker passes will fail their first unit the same way; the
  inbox held 76 units at this pass's close (77 at sync).

## Other pass steps

- Own PRs checked first: PR 347 (records/2026-11-06, opened by
  the 00:00 pr-integration pass) is MERGEABLE CLEAN with no
  comments; PR 345 (records/2026-11-05 post-2300 batch, opened
  by ticker-2303) has no comments. The four older open records
  PRs (324, 301, 265, 256) carry no new comments since the
  ticker-2303 branch-side reconciliation at 23:06-23:07 PST;
  nothing addressed to this job. No PR action needed this pass.
- Sync: reaped 0, expired 0, due 20, produced nothing new, all
  20 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) was restored to the live
  pool inbox by the ticker-2303 pass (not_before 01:30Z and
  02:30Z); not yet due, untouched by this pass.
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
