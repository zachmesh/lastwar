---
title: Passes queue run 1434
created: 2026-11-05T22:34:00Z
modified: 2026-11-05T22:44:00Z
level: L0
version: 1.0.0
description: Ticker-1434 passes unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1434 queue run - shop claims

Executor: ticker-1434. Unit: passes-2026-11-05-1057
(regular passes, activity shop-claims; planned_for
2026-11-05T18:57:00Z, expires 2026-11-05T22:57:00Z).
Session window about 14:34 to 14:44 America/Los_Angeles.
Device probes ran 14:34 to 14:41; branch-pool claim and
complete were bookkeeping-only at 14:43 to 14:44, so the
unit's duration_seconds reads 0 - the probe time is
recorded here, not in that field.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so no shop page was opened, no pass gift was
  claimed and nothing was checked. The passes unit's daily
  gifts stay unclaimed for this slot; the tracker is untouched
  so the next tick re-produces the regular.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 7 hours 7 minutes at pass time,
  unchanged since the ticker-1025 pass.
- computer.session start on the Mac mini: node_offline, device
  is offline and does not advertise a wake-up path (attempt 1).
- connection.health on the Mac mini: node_offline (attempt 2).
- connection.repair (web) on the Mac mini: node_offline
  (attempt 3).
- connection.repair (native) on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 4).
- connection.health on the recovery device:
  node_invoke_timeout after 25000ms (attempt 5).
- computer.session start on the Mac mini, second try:
  node_offline (attempt 6).
- Six attempts, zero responses. This meets the standing
  retry rule of at least 3 attempts before recording a unit
  as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the forty-ninth
  consecutive pass with a Mac device-access blocker was
  ticker-1404 (scout-midday unit, 14:04 local), and this pass
  is the fiftieth, eleventh in the worsened zero-response
  form. The form has worsened since the afternoon of 2026-11-04
  from capture failure (OFF_SCREEN_WINDOW) to a fully offline
  device with a stalled invoke channel; the ticker-1025 pass
  classified it CHANNEL_STALL and noted recovery needs the
  Mac-side agent gateway restart before re-probing, and
  re-probing is owed only after device.list last_seen
  refreshes. That condition is not met - last_seen is still
  15:36:52Z - so no further probe was run beyond the six
  attempts above. This pass commented on #284 instead of
  filing a duplicate. Until the Mac gateway recovers, further
  ticker passes will fail their first unit the same way.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 310 (records/2026-11-05), verified MERGEABLE and CLEAN
  by the integrator at the 11:45 non-batch pass and awaiting
  the 15:00 batch; the newest comments are status notes from
  the ticker-1304, ticker-1334, ticker-1404 and
  planner-1340 passes, no question addressed to this job, so
  nothing was owed before game work. The pr-integration
  1436 run (14:36) confirms 310 clean at head 5e5d63cb.
- Sync (authoritative, run against the records-branch pool
  in the delivery worktree): reaped 0, expired 6
  (duel-score, gifts, help, mail, star-ceremony, train
  2026-11-05-1030), due 23, produced 6 units (mail, help,
  gifts, train, star-ceremony, duel-score 2026-11-05-1430);
  17 due regulars already queued. The pass's first sync ran
  in the main working tree and expired 8 local copies, but
  that tree sits on the stale work/ops-execution-records
  branch (queue state from 2026-11-03) and holds another
  job's in-flight state - its copies of the 1030 units
  (created 06:41Z) are stale duplicates of the branch pool's
  live copies (created 20:35Z by the ticker-1234 sync), so
  the local sync's expirations were discarded and the
  branch-pool sync above is the one committed. The records
  branch is the authoritative pool for ticker passes.
- Zombie seeding skipped: zombie chain zombie-2026-10-28
  closed with unit 066 on 2026-10-30 (event ended about the
  19:00 reset 2026-10-30, no Zombie tab in the Events hub),
  and the seeding rule forbids a fresh chain until a Zombie
  Invasion tab is seen live again.
- No successor unit is enqueued from this unit - a successor
  would hit the same stalled channel. The pass stopped after
  this one unit.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the passes unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed. The worktree claim/complete used the
  branch pool's live copy of the unit (created 20:35:21Z);
  the local tree's stale copy was claimed and completed
  there first (22:35:59Z to 22:40:54Z, 295s) as the
  execution attempt record, then superseded by the
  branch-pool completion.

## Outcome

Failed. No shop page opened, no pass gift claimed, no
diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none, costs
  no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
