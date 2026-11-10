---
title: Shop claims queue run 0234
created: 2026-11-06T10:43:00Z
modified: 2026-11-06T10:43:00Z
level: L0
version: 1.0.0
description: Ticker-0234 passes unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0234 queue run - Shop claims

Executor: ticker-0234. Unit: passes-2026-11-05-2257.
Session window about 02:34 to 02:43 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out on the recovery channel, so the shop was never
  opened, no free pack or pass daily gift was claimed. The loss
  is the unexecuted passes check for this slot (planned 22:57
  local 2026-11-05, expires 02:57 local 2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 19 hours at the 02:36 re-check,
  unchanged since the ticker-0104 pass.
- Four device invokes, zero responses, all against the frozen
  last_seen: connection.health (attempt 1) node_offline with
  "device is offline and does not advertise a wake-up path";
  connection.repair web (attempt 2) node_offline;
  connection.repair native on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
  attempt 3) node_invoke_timeout after 25 seconds;
  computer.session start (attempt 4) node_offline. This meets
  the standing retry rule of at least 3 attempts before
  recording a unit as access-failed.
- New data point against ticker-0104: this pass did attempt
  the recovery device, and its native repair timed out after
  25 seconds, matching the ticker-2041 timeouts - the
  recovery channel is unresponsive too, not just untested.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the sixty-fifth
  recorded consecutive pass with a Mac device-access blocker,
  twenty-sixth in the worsened zero-response form. The last
  recorded one was ticker-0104, the sixty-fourth and
  twenty-fifth. This pass commented on #284 instead of
  filing a duplicate. Until the Mac gateway recovers, further
  ticker passes will fail their first unit the same way; the
  inbox held 75 units before this pass's sync reaped the 9
  expired ones.

## Other pass steps

- Own PRs checked first: PR 347 (records/2026-11-06) is
  MERGEABLE CLEAN with no comments; PR 345 (records/2026-11-05
  post-2300 batch) and the four older open records PRs (324,
  301, 265, 256) carry no new comments since the ticker-0104
  pass; nothing addressed to this job. No PR action needed
  this pass.
- Sync: reaped 0, expired 9, due 20, produced nothing new, all
  20 regulars already queued.
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
  so the next tick re-produces the passes unit.
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

Failed. No shop screen read, no free pack or pass gift claimed.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 284
