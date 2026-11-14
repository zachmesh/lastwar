---
title: Zombie Invasion unit 029 queue run
created: 2026-11-14T02:23:00Z
modified: 2026-11-14T02:23:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-1813, zombie-invasion unit 029 failed - Mac mini still offline at the device transport (12th occurrence of the new failure mode, not Issue 689); VPS SSH outage continues, delivery partial
status: unverified
---

# 18:13 to about 18:30 - Ticker pass ticker-1813, zombie-invasion unit 029 failed

- Pass identity: scheduled Fri 2026-11-13 18:04 PT
  (trigger dependency_probe), executor ticker-1813, executed
  18:13-18:30 PT. Token acquired 02:13:xxZ, released after the
  commit (see below).
- Own PRs first: no records/2026-11-13 PR exists to own - the
  pr-catchall 1739 run verified via the read-only GitHub API at
  18:12-18:15 PT, minutes before this pass, that the only open
  PRs are #711 (knowledge fold), #708 (records/2026-11-12) and
  #425 (owner-gated OD-20261108-01), newest merged still #710,
  and the remote has no records/2026-11-13 branch. VPS gh is
  unreachable (SSH outage below), so no live PR re-check was
  possible from the VPS route; nothing in the 1739 read names
  this job or asks it a question. PR #708 has missed 7 batch
  points (15:00, 19:00, 23:00, 03:00, 07:00, 11:00, 15:00);
  the next batch point is 19:00 PT tonight and will be the
  8th miss if the VPS is still down.
- Tool currency (R10, Issue #694): the pass's sync and claim
  first ran through the main tree's tools/queue.py, which is
  STALE (sha256 afe45a60, Nov 3 vintage, predates #692/#694/
  #696/#699/#704/#706/#710). Caught before completion: the
  current tool is _tools_/queue.py sha256
  366b3b76bf638befbc1d0cb81c6ba8417d21ef216e5cfb5fbc9fc903c1f476b0,
  git_head a858a0fca, currency current (verified by the version
  command in ~/workspace/lastwar-worktrees/ticker-1408-main;
  its main_sha256 matches). The local main branch tip
  22601972 (merge of PR #700) is a local-only merge ahead of
  the remote main a858a0fca; its queue.py (ba9bee07) reports
  currency stale against the remote main, so it is NOT the
  current tool. All completion, enqueue and verification steps
  below ran through the current tool with
  --root /home/hatch/workspace/lastwar. The stale-tool sync
  and claim were verified against the live pool with the
  current tool and agree (see Sync).
- Sync (stale tool first, verified with the current tool):
  reaped 0, expired 27, due 22, produced none (already queued
  22: mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). The 27 expirations are the
  16:30/17:00/17:30 pre-reset-sweep and 14:03/14:30/14:57
  windows whose expiry passed at 18:00-18:30 PT. Live pool
  after sync, per the current tool: inbox 73, claimed 1,
  done 1866 (1839 + 27 expired). No blocker was reaped and
  none stands. Roster warning stands: the live pool holds
  units for zombie-invasion, building-queues and research,
  regulars missing from the loaded roster (Issue #198).
  No zombie seeding needed (unit 029 already in inbox, chain
  zombie-2026-11-10, done 21, pending 1).
- Zombie-invasion unit 029 (ticker-1813, failed, chain
  zombie-2026-11-10 seq 29): no game action was possible - the
  Mac mini is unreachable at the device transport. Two
  computer.session starts failed with node_offline ("device is
  offline and does not advertise a wake-up path");
  connection.repair on the Mac failed the same way; a
  connection.repair through the recovery device
  (endo-recovery-8a2744fe) timed out after 25s
  (node_invoke_timeout). The device last_seen is
  2026-11-12T17:52:28Z, about 32.5 hours before this probe.
  (One extra call, a repair on the recovery device with
  target "web", was rejected as invalid params - that
  command expects "native"; it was a parameter error, not a
  control attempt, and is not counted.) No game state was
  observable at all - not even a read-only snap, so unlike
  the Issue #689 lock there is no live base-screen read to
  report. No input was sent, nothing was spent, no dialog
  was seen.
- This is the same NEW failure mode as unit 028, not Issue
  #689: #689 is the outcome_unknown control-channel lock
  with read-only observation still live; here the device
  transport itself is down, so no outcome_unknown was ever
  observed. The unit therefore closed failed with
  blocker_category f (missing precondition) and NO
  blocker_overlay - naming control-lock would misstate the
  error and corrupt #689's evidence. No comment was left on
  #689. This is the 12th occurrence of the device-offline
  probe failure (unit 028 was the 11th). Consequence, stated
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
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 4 (2 session starts, repair on the Mac,
  repair via the recovery device). No coin, medal or stamina
  counts were measured - the game was never reached. No
  diamonds or money spent. verified no (no live game read in
  this unit). Note: the complete call passed only the six
  activity stats, so the tool recorded stats_missing [target,
  achieved, resources_gained, costs, verified,
  blocker_category] and the closing counts as unverified in
  the retro aggregation; a re-complete was refused (state is
  done), so the gap stands as the tool wrote it.
- Chain: successor 030 enqueued in the same chain
  (zombie-2026-11-10) to start now (cleared false). The pass
  stopped after this unit rather than cascading failed units.
  Tracker untouched (failed unit). The pass deliberately did
  NOT claim the expiry-critical vip-2026-11-13-1800 unit
  (expires at the 19:00 reset) for this doomed probe: the
  zombie chain self-continues, so the probe burns the
  background unit, and a later tick can still run the VIP
  unit if the Mac returns before 19:00.
- Delivery: PARTIAL - the push is blocked by the VPS SSH
  outage (Permission denied publickey, since about 12:46
  Nov 12, about 30 hours; the ~/.ssh loss from the Nov 12
  cleanup). The commit stays on local records/2026-11-13;
  no PR can be opened for it until the push succeeds. The
  bundle route was not re-attempted: the SSH step is the
  blocker and it fails identically every time.
