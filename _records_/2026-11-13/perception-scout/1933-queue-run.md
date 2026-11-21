---
title: Scout unit 010 queue run
created: 2026-11-14T03:42:00Z
modified: 2026-11-14T03:42:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-1933, scout unit 010 failed - Mac mini still offline at the device transport (13th occurrence of the new failure mode, not Issue 689); VPS SSH outage continues, delivery partial
status: unverified
---

# 19:33 to about 19:45 - Ticker pass ticker-1933, scout unit 010 failed

- Pass identity: scheduled Fri 2026-11-13 19:04 PT
  (trigger dependency_probe), executor ticker-1933, executed
  19:33-19:45 PT. Token acquired 03:34:49Z, released after the
  commit (see below).
- Own PRs first: no records/2026-11-13 PR exists to own - the
  pr-catchall 1739 read (verified via the read-only GitHub API
  at 18:12-18:15 PT, recorded in the ticker-1813 record) found
  the only open PRs are #711 (knowledge fold), #708
  (records/2026-11-12) and #425 (owner-gated OD-20261108-01),
  newest merged still #710, and the remote has no
  records/2026-11-13 branch. VPS gh is unreachable (SSH outage
  below), so no live PR re-check was possible from the VPS
  route; nothing in the 1739 read names this job or asks it a
  question. PR #708 has now missed its 8th batch point (19:00
  PT tonight), as the ticker-1813 record predicted.
- Tool currency (R10, Issue #694): the pass's sync and claim
  first ran through the main tree's tools/queue.py, which is
  STALE (sha256 afe45a60, Nov 3 vintage). Caught before
  completion: the current tool is _tools_/queue.py sha256
  366b3b76bf638befbc1d0cb81c6ba8417d21ef216e5cfb5fbc9fc903c1f476b0,
  git_head a858a0fca, currency current (verified by the version
  command in ~/workspace/lastwar-worktrees/ticker-1408-main;
  its main_sha256 matches). All completion, enqueue and
  verification steps ran through the current tool with
  --root /home/hatch/workspace/lastwar. The stale-tool sync
  and claim were verified against the live pool with the
  current tool and agree (see Sync).
- Sync (stale tool first, verified with the current tool):
  reaped 0, expired 0, due 22, produced none (already queued
  22: mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). Live pool after sync, per
  the current tool: inbox 83, claimed 0, done 1878; after this
  unit's claim and completion, inbox 82, claimed 1 (token),
  done 1879 with the successor 011 back in inbox. No blocker
  was reaped and none stands. Roster warning stands: the live
  pool holds units for zombie-invasion, building-queues and
  research, regulars missing from the loaded roster (Issue
  #198). No zombie seeding needed (unit
  zombie-invasion-zombie-2026-11-10-030 already in inbox,
  chain zombie-2026-11-10).
- Scout unit 010 (ticker-1933, failed, chain scout-2026-11-10
  seq 10): no game action was possible - the Mac mini is
  unreachable at the device transport. One computer.session
  start failed with node_offline ("device is offline and does
  not advertise a wake-up path"); connection.repair on the Mac
  failed the same way; a connection.repair through the
  recovery device (endo-recovery-8a2744fe) timed out after
  25s (node_invoke_timeout); a connection.health check on the
  recovery device timed out after 25s as well. The device
  last_seen is 2026-11-12T17:52:28Z, about 49.5 hours before
  this probe. No game state was observable at all - not even
  a read-only snap, so unlike the Issue #689 lock there is no
  live base-screen read to report. No input was sent, nothing
  was spent, no dialog was seen.
- This is the same NEW failure mode as units 028 and 029, not
  Issue #689: #689 is the outcome_unknown control-channel
  lock with read-only observation still live; here the device
  transport itself is down, so no outcome_unknown was ever
  observed. The unit therefore closed failed with
  blocker_category f (missing precondition) and NO
  blocker_overlay - naming control-lock would misstate the
  error and corrupt #689's evidence. No comment was left on
  #689. This is the 13th occurrence of the device-offline
  probe failure (unit 029 was the 12th). Consequence, stated
  plainly: with no blocker standing, `next` hands out a unit
  on every tick and each tick burns one failed unit (plus a
  successor enqueue) until the Mac returns - the same burn
  pattern the control-lock blocker exists to prevent. The
  fix is a device-offline pause; the draft issue is preserved
  in the unit 028 record (1415-queue-run.md) - filing is
  still blocked (VPS gh unreachable; the GitHub connector
  issue_write returned 403 Resource not accessible by
  integration on three attempts in the 1408 pass), so it was
  not re-attempted here.
- Result stats: surfaces_walked 0, items_observed 0,
  red_dots_seen 0, red_dots_explained 0, unexplained_red_dots
  0, unknown_items 0, control_attempts 4 (1 session start,
  repair on the Mac, repair via the recovery device, health
  via the recovery device). Retro keys all present this time
  (target, achieved, resources_gained, costs, verified no,
  blocker_category f), stats_missing empty - the stats gap
  the ticker-1813 record noted for unit 029 is closed in
  this unit. No coin, medal or stamina counts were measured -
  the game was never reached. No diamonds or money spent.
  verified no (no live game read in this unit).
- Chain: successor 011 enqueued in the same chain
  (scout-2026-11-10) to start now, following the precedent of
  units 008 and 009, which each enqueued their successor
  after an access failure. The pass stopped after this unit
  rather than cascading failed units. Tracker untouched
  (failed unit). The pass deliberately did NOT claim the
  expiry-critical vip-2026-11-13-1800 unit (expired at the
  19:00 reset) or the zombie-invasion 030 unit for this doomed
  probe: the scout chain self-continues, so the probe burns
  the background-priority unit, and a later tick can still
  run the other units if the Mac returns.
- Delivery: PARTIAL - the push is blocked by the VPS SSH
  outage (Permission denied publickey, since about 12:46
  Nov 12, about 31 hours; the ~/.ssh loss from the Nov 12
  cleanup; re-verified at this pass's start). The commit stays
  on local records/2026-11-13; no PR can be opened for it
  until the push succeeds. The bundle route was not
  re-attempted: the SSH step is the blocker and it fails
  identically every time. The delivery worktree
  ticker-1408-delivery was reused (it already held
  records/2026-11-13 at the branch tip); no new worktree was
  created because a second checkout of the same branch would
  have failed.
