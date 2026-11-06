---
title: Perception scout queue run 1836
created: 2026-11-06T02:36:00Z
modified: 2026-11-06T02:50:00Z
level: L0
version: 1.0.0
description: Ticker-1834 scout unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1836 queue run - perception scout

Executor: ticker-1834. Unit: scout-scout-2026-11-02-005
(chain scout-2026-11-02, seq 5; window the chain remainder
after unit 004, which walked the alliance remainder and
carried the rest to this successor; created
2026-11-03T21:15:50Z, first attempt this pass).
Session window about 18:36 to 18:50 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so no surface was walked, no observed item was
  recorded, no red dot was resolved and nothing was claimed.
  A scout unit observes only in any case, so the loss is the
  unrecorded observation, not leaked claims.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 11 hours at pass time,
  unchanged since the ticker-1025 pass and identical to the
  ticker-1804 reading 30 minutes earlier. A fresh device.list
  at about 18:44 confirms the same last_seen, still
  unrefreshed.
- connection.health on the Mac mini: node_offline, device is
  offline and does not advertise a wake-up path (attempt 1).
- connection.repair (target web) on the Mac mini:
  node_offline, no wake-up path (attempt 2).
- computer.session start on the Mac mini: node_offline
  (attempt 3).
- computer.control frontmost_app on the Mac mini:
  node_offline (attempt 4).
- connection.health on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 5).
- Five attempts, zero responses. This meets the standing
  retry rule of at least 3 attempts before recording a unit
  as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the fifty-seventh
  consecutive pass with a Mac device-access blocker was
  ticker-1804 (mail unit, 18:04 local), and this pass is the
  fifty-eighth, nineteenth in the worsened zero-response form.
  The form has worsened since the afternoon of 2026-11-04
  from capture failure (OFF_SCREEN_WINDOW) to a fully offline
  device with a stalled invoke channel; the ticker-1025 pass
  classified it CHANNEL_STALL and noted recovery needs the
  Mac-side agent gateway restart before re-probing, and
  re-probing is owed only after device.list last_seen
  refreshes. That condition is not met - last_seen is still
  15:36:52Z - so no further probe was run this pass. This
  pass commented on #284 instead of filing a duplicate.
  Until the Mac gateway recovers, further ticker passes will
  fail their first unit the same way; the inbox held 73 units
  at this pass (pool as synced from the main worktree disk).

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 334 (records/2026-11-05, Owner lastwar-pr-integrator),
  with no comments, so nothing was owed before game work.
  The other open records PRs (324, 301, 265, 256) are not
  owned by this job.
- Sync: reaped 0, due 23, produced 4 units (vip,
  daily-missions, duel-score and scout 2026-11-05-1800);
  18 due regulars already queued. The first sync of this pass
  also expired 4 units (train, star-ceremony, help and gifts
  2026-11-05-1430); a concurrent job expired those same four
  on the shared disk pool at 18:42:34, so the redo sync
  expired 0 and the expiry is not this pass's change.
  Zombie seeding skipped: zombie chain zombie-2026-10-28
  closed with unit 066 on 2026-10-30 (event ended about the
  19:00 reset 2026-10-30, no Zombie tab in the Events hub),
  and the seeding rule forbids a fresh chain until a Zombie
  Invasion tab is seen live again.
- Pool note: the main working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state, so this pass ran in a temporary worktree
  on the records/2026-11-05 branch. The _queue_ state used
  for sync was copied from the main worktree disk (inbox 73,
  done 949 at sync time); the branch pool on its own reads
  smaller (inbox 42 at the 1404 pass), so the disk copy
  carries units the branch lacks, including this unit itself.
  The four produced units are absent from the branch, so no
  duplicate was staged. Only this pass's own changes are
  committed below; the remaining disk-vs-branch pool drift is
  left for the pool owner, not swept in.
- Worktree loss and redo: the pass first ran in
  /tmp/lastwar-ticker-1834, which the runtime wiped mid-run
  (the whole /tmp was empty when the token-release step ran,
  about 18:44), taking the uncommitted sync output, claim,
  record and INDEX append with it. The GitHub comment on
  Issue 284 had already been posted and was not duplicated.
  The pass was redone in full in a workspace worktree
  (~/workspace/lastwar-worktrees/ticker-1834-1105): sync
  re-run (same 4 units produced), token re-acquired, unit
  re-claimed, device.list re-confirmed the same stale
  last_seen, record rewritten and unit completed here.
  Lesson for later passes: never put pass work in /tmp;
  worktrees live under ~/workspace/lastwar-worktrees/.
- No successor unit is enqueued from this unit - the chain's
  remainder is unchanged by a pass that read nothing, and a
  successor would hit the same stalled channel.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the scout regular.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed. Tier-2 note: the worktree diff shows
  pre-existing _tools_/state drift (disk vs branch) and a
  _tools_ rename already in the tree; none of it is this
  pass's, and none of it is committed here.

## Outcome

Failed. No surface walked or observed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none, costs
  no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
