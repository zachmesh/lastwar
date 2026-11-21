---
title: Zombie Invasion unit 030 queue run
created: 2026-11-14T04:51:00Z
modified: 2026-11-14T04:51:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-2041, zombie-invasion unit 030 failed - Mac mini still offline at the device transport (14th occurrence of the new failure mode, not Issue 689); VPS SSH outage continues, delivery partial
status: unverified
---

# 20:41 to about 20:52 - Ticker pass ticker-2041, zombie-invasion unit 030 failed

- Pass identity: scheduled Fri 2026-11-13 20:34 PT
  (trigger dependency_probe), executor ticker-2041, executed
  20:41-20:52 PT. Token acquired 04:41:xxZ, released 04:49:42Z
  after the unit closed (see below).
- Own PRs first: no records/2026-11-13 PR exists to own - the
  pr-catchall 1939 run verified via the read-only GitHub API
  at 20:20-20:27 PT, minutes before this pass, that the only
  open PRs are #711 (knowledge fold), #708 (records/2026-11-12)
  and #425 (owner-gated OD-20261108-01), newest merged still
  #710, and the remote has no records/2026-11-13 branch. The
  pr-integration 2015 run confirmed the same three PRs and
  recorded the 19:00 batch point as MISSED - the eighth missed
  batch (15:00, 19:00, 23:00 on 11-12; 03:00, 07:00, 11:00,
  15:00, 19:00 on 11-13); next batch point 23:00 PT tonight.
  VPS gh is unreachable (SSH outage below), so no live PR
  re-check was possible from the VPS route; nothing in the
  1939 read names this job or asks it a question.
- Tool currency (R10, Issue #694): the pass's sync ran through
  the main tree's tools/queue.py, which is STALE (sha256
  afe45a60, Nov 3 vintage). Caught before completion: the
  current tool is _tools_/queue.py sha256
  366b3b76bf638befbc1d0cb81c6ba8417d21ef216e5cfb5fbc9fc903c1f476b0,
  git_head a858a0fca, currency current (verified by the version
  command in ~/workspace/lastwar-worktrees/ticker-1408-main;
  its main_sha256 matches). All claim, completion, enqueue
  and verification steps ran through the current tool with
  --root /home/hatch/workspace/lastwar. The stale-tool sync
  was verified against the live pool with the current tool
  and agrees (see Sync).
- Sync (stale tool first, verified with the current tool):
  reaped 0, expired 0, due 22, produced none (already queued
  22: mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). Live pool after sync, per
  the current tool: inbox 83, claimed 0, done 1879; after this
  unit's claim, completion and the successor enqueue, inbox
  83, claimed 0, done 1880, failed 117. No blocker was reaped
  and none stands. Roster warning stands: the live pool holds
  units for zombie-invasion, building-queues and research,
  regulars missing from the loaded roster (Issue #198). No
  zombie seeding needed (unit
  zombie-invasion-zombie-2026-11-10-030 already in inbox,
  chain zombie-2026-11-10, done 22, pending 1). The
  priority-1 vip-2026-11-13-1800 unit is stalled 14.1h - it
  expired at the 19:00 reset and cannot run while the Mac is
  offline; the next sync reaps it as expired.
- Zombie-invasion unit 030 (ticker-2041, failed, chain
  zombie-2026-11-10 seq 30): no game action was possible - the
  Mac mini is unreachable at the device transport. Two
  computer.session starts failed with node_offline ("device is
  offline and does not advertise a wake-up path");
  connection.repair on the Mac failed the same way; a
  connection.repair through the recovery device
  (endo-recovery-8a2744fe) timed out after 25s
  (node_invoke_timeout). One extra call, a repair on the Mac
  with target "native", was rejected as invalid params - this
  device's repair expects "web", the recovery device's
  expects "native"; it was a parameter error, not a control
  attempt, and is not counted. The device last_seen is
  2026-11-12T17:52:28Z, about 35 hours before this probe.
  (Correction: the ticker-1933 record states "about 49.5h"
  for the same last_seen; the arithmetic is about 35h at
  this pass, about 33.7h at the 1933 probe - the 49.5h
  figure was a miscalculation and is not repeated here.)
  No game state was observable at all - not even a read-only
  snap, so unlike the Issue #689 lock there is no live
  base-screen read to report. No input was sent, nothing was
  spent, no dialog was seen.
- This is the same NEW failure mode as units 028 and 029, not
  Issue #689: #689 is the outcome_unknown control-channel
  lock with read-only observation still live; here the device
  transport itself is down, so no outcome_unknown was ever
  observed. The unit therefore closed failed with
  blocker_category f (missing precondition) and NO
  blocker_overlay - naming control-lock would misstate the
  error and corrupt #689's evidence. No comment was left on
  #689. This is the 14th occurrence of the device-offline
  probe failure (unit 029 was the 12th, unit 010 the 13th).
  Consequence, stated plainly: with no blocker standing,
  `next` hands out a unit on every tick and each tick burns
  one failed unit (plus a successor enqueue) until the Mac
  returns - the same burn pattern the control-lock blocker
  exists to prevent. The fix is a device-offline pause; the
  draft issue is preserved in the unit 028 record
  (1415-queue-run.md) - filing is still blocked (VPS gh
  unreachable; the GitHub connector issue_write returned 403
  Resource not accessible by integration on three attempts in
  the 1408 pass), so it was not re-attempted here.
- Result stats: zombies_killed 0, cleared false, coin_before
  unread, coin_after unread, coins_collected 0, medals_before
  unread, medals_after unread, chests_opened 0,
  squads_parallel 0, control_attempts 4 (2 session starts,
  repair on the Mac, repair via the recovery device). Retro
  keys all present (target, achieved, resources_gained,
  costs, verified no, blocker_category f), stats_missing
  empty - the stats gap the ticker-1813 record noted for
  unit 029 stays closed. No coin, medal or stamina counts
  were measured - the game was never reached. No diamonds or
  money spent. verified no (no live game read in this unit).
- Chain: successor 031 enqueued in the same chain
  (zombie-2026-11-10) to start now, following the precedent
  of units 028 and 029, which each enqueued their successor
  after an access failure. The pass stopped after this unit
  rather than cascading failed units. Tracker untouched
  (failed unit).
- Delivery: PARTIAL - the push is blocked by the VPS SSH
  outage (Permission denied publickey, since about 12:46
  Nov 12, about 32 hours; the ~/.ssh loss from the Nov 12
  cleanup; re-verified at this pass's start). The commit stays
  on local records/2026-11-13; no PR can be opened for it
  until the push succeeds. The bundle route was not
  re-attempted: the SSH step is the blocker and it fails
  identically every time. The delivery worktree
  ticker-1408-delivery was reused (it already held
  records/2026-11-13 at the branch tip); no new worktree was
  created because a second checkout of the same branch would
  have failed.
