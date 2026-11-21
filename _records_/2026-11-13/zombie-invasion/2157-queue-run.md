---
title: Zombie Invasion unit 031 queue run
created: 2026-11-14T11:42:00Z
modified: 2026-11-14T11:42:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-2152, zombie-invasion unit 031 failed - Mac mini still offline at the device transport (15th occurrence of the new failure mode, not Issue 689); VPS SSH outage continues, delivery partial
status: unverified
---

# 21:52 to about 22:00 - Ticker pass ticker-2152, zombie-invasion unit 031 failed

- Pass identity: scheduled Fri 2026-11-13 21:34 PT
  (trigger dependency_probe), executor ticker-2152, game work
  executed 21:52-22:00 PT Nov 13. Token acquired 05:56:xxZ,
  released 05:58:53Z. This record itself was written about
  03:42 PT Nov 14, after a service and VM restart stalled the
  run between the unit close and the filing and delivery
  steps (see the outage note below).
- Own PRs first: connector list_pull_requests read after the
  resume - the only open PRs are #711 (knowledge fold,
  head e3c3dfd0, Owner lastwar-knowledge-organizer), #708
  (records 2026-11-12, head 2f59c270, Owner
  lastwar-pr-integrator) and #425 (tools log gate, head
  4f41cdd6, Owner lastwar-tool-developer), all heads unchanged
  since Nov 12; no records/2026-11-13 PR exists. Comment state
  per the pr-integration 2330 run (23:36 PT): PR 711 one
  comment (2026-11-12T19:55:59Z, the known superseded-705
  note), PR 708 zero comments, PR 425 latest comment
  2026-11-12T19:29:36Z. Nothing in any open PR addresses this
  job or asks it a question. VPS gh is unreachable (SSH outage
  below), so no live PR re-check was possible from the VPS
  route.
- Tool currency (R10, Issue #694): the main tree's
  tools/queue.py is STALE (sha256 afe45a60, Nov 3 vintage;
  tools is a symlink to _tools_ in the main checkout). The
  current tool is _tools_/queue.py sha256
  366b3b76bf638befbc1d0cb81c6ba8417d21ef216e5cfb5fbc9fc903c1f476b0,
  git_head a858a0fca, currency current (verified by the version
  command in ~/workspace/lastwar-worktrees/ticker-1408-main).
  All queue operations in this pass (sync, token-acquire,
  claim, complete, enqueue, token-release, stats) ran through
  the current tool with --root /home/hatch/workspace/lastwar.
  Unlike the 2041 pass, no stale-tool sync ran first.
- Sync (current tool, live pool): reaped 0, expired 0, due 24,
  produced none (already queued 24: mail, help, gifts,
  harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, research,
  building-queues, donations, events, arms-race,
  star-ceremony, duel-score, scout, scout-midday). The
  completion marker for zombie unit 030 was reaped. Branch
  reconcile skipped (records/2026-11-13 not on the remote).
  Roster warning stands: the live pool holds units for
  zombie-invasion, a regular missing from the loaded roster
  (Issue #198). No zombie seeding needed (unit 031 already in
  inbox, chain zombie-2026-11-10, done 30, pending 1). `next`
  returned scout-scout-2026-11-10-011 (chain scout-2026-11-10
  seq 11, created 19:39 PT) - it was NOT claimed: a real
  perception unit is not burned on a doomed probe. Zombie
  unit 031 was claimed as the probe instead, per the 2041
  precedent. Live pool after sync: inbox 83, claimed 0,
  done 1880. A later sync during the outage expired 33 units
  (done 1881 to 1914, expired 710 to 743 by 03:41 PT); the
  VIP unit was not among them - its file carries expires_at
  2026-11-15T02:00:00Z and sync did not reap it, though its
  18:00 slot freebies lapsed at the 19:00 reset.
- Zombie-invasion unit 031 (ticker-2152, failed, chain
  zombie-2026-11-10 seq 31): no game action was possible -
  the Mac mini is unreachable at the device transport. Two
  computer.session starts failed with node_offline ("device is
  offline and does not advertise a wake-up path");
  connection.repair on the Mac failed the same way; a
  connection.repair through the recovery device
  (endo-recovery-8a2744fe) timed out after 25s
  (node_invoke_timeout). The device last_seen is
  2026-11-12T17:52:28Z, about 36 hours before this probe
  (about 42 hours by the time this record was written after
  the restart). No game state was observable at all - not
  even a read-only snap, so unlike the Issue #689 lock there
  is no live base-screen read to report. No input was sent,
  nothing was spent, no dialog was seen.
- This is the same NEW failure mode as units 028, 029 and
  030, not Issue #689: #689 is the outcome_unknown
  control-channel lock with read-only observation still live;
  here the device transport itself is down, so no
  outcome_unknown was ever observed. The unit therefore closed
  failed with blocker_category f (missing precondition) and NO
  blocker_overlay - naming control-lock would misstate the
  error and corrupt #689's evidence. No comment was left on
  #689. This is the 15th occurrence of the device-offline
  probe failure. Consequence, stated plainly: with no blocker
  standing, `next` hands out a unit on every tick and each
  tick burns one failed unit (plus a successor enqueue) until
  the Mac returns - the same burn pattern the control-lock
  blocker exists to prevent. The fix is a device-offline
  pause; see the filing note below.
- Result stats: zombies_killed 0, cleared false, coin_before
  unread, coin_after unread, coins_collected 0, medals_before
  unread, medals_after unread, chests_opened 0,
  squads_parallel 0, control_attempts 4 (2 session starts,
  repair on the Mac, repair via the recovery device). Retro
  keys all present (target, achieved, resources_gained,
  costs, verified no, blocker_category f), stats_missing
  empty. No coin, medal or stamina counts were measured -
  the game was never reached. No diamonds or money spent.
  verified no (no live game read in this unit).
- Chain: successor 032 enqueued in the same chain
  (zombie-2026-11-10) to start now, following the precedent
  of units 028, 029 and 030, which each enqueued their
  successor after an access failure. The pass stopped after
  this unit rather than cascading failed units. Tracker
  untouched (failed unit).
- Issue filing: the device-offline pause draft (preserved in
  the unit 028 record, 1415-queue-run.md) was retried through
  the GitHub connector issue_write after the resume. Attempt 1
  died in the service restart before returning (verified not
  created: newest open issue still #712). Attempt 2 returned
  "failed to create issue: POST
  https://api.github.com/repos/zachmesh/lastwar/issues: 403
  Resource not accessible by integration" - filing is still
  blocked; the VPS gh route is the filing path once SSH
  returns. The draft stays preserved in the 028 record. No
  issue number can be named for this unit.
- Outage note: between the unit close (21:58 PT Nov 13) and
  this record's writing, the service and VM restarted (VM
  uptime 21 min at 03:41 PT Nov 14; the GitHub API Date header
  agrees it is 11:41Z). No ticker pass executed a unit in the
  gap - the newest executed closing was still 05:58:45Z at
  03:41 PT and unit 032 was still in inbox. The pr-integration
  2230 and 2330 runs did run in the gap (local mirror only):
  the 2330 run is a BATCH pass and the 32nd consecutive failed
  integrator pass, and it records the 23:00 batch as MISSED -
  the ninth missed batch; next batch point 03:00 PT Nov 14
  (window open at this writing, VPS still down).
- Delivery: PARTIAL - the push is blocked by the VPS SSH
  outage (Permission denied publickey, since about 12:46
  Nov 12, about 39 hours at this writing; the ~/.ssh loss
  from the Nov 12 cleanup; re-verified at this pass's start).
  The commit stays on local records/2026-11-13; no PR can be
  opened for it until the push succeeds. The bundle route was
  not re-attempted: the SSH step is the blocker and it fails
  identically every time.
