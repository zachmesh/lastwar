---
title: Play Record 2026-11-13
created: 2026-11-13T22:30:00Z
modified: 2026-11-13T22:30:00Z
level: L0
version: 1.0.0
description: The 1408 queue ticker pass (scheduled 2026-11-12 14:04, executed 2026-11-13 14:15) with 1 unit failed (zombie-invasion, Mac offline)
status: unverified
---

# 2026-11-13

All times America/Los_Angeles. Actor Muse, under the owner standing
instruction of 2026-10-25 to run the regulars and the queue design
of 2026-10-28.

## 14:08 to about 14:30 - Ticker pass ticker-1408, zombie-invasion unit failed (Mac offline)

- Scheduler delivered the 2026-11-12 14:04 tick a day late: the run
  context is stamped Thu 2026-11-12 14:08 PT but the VM clock and
  the GitHub server Date header agree it is Fri 2026-11-13 14:25
  PT. First Nov 13 execution; record under _records_/2026-11-13,
  branch records/2026-11-13.
- Own PRs first: records PR 708 (2026-11-12) verified LIVE via the
  GitHub public API: OPEN, MERGEABLE/CLEAN, head 2f59c27047, 0
  comments, awaits the integrator batch - no question addressed to
  this job. PR 711 and PR 425 are owned by other jobs. Newest
  issues #712 and #709 already known.
- Sync (current tool, fresh main worktree at a858a0fca): reaped 0,
  expired 0, blockers_reaped ["control-lock"] - the blocker
  recorded 2026-11-12T20:08:13Z was 26h old, past the 4h stale
  bound, so the reap was correct and the probe was due. Produced
  none (due 24, already queued 24). Roster warning stands:
  zombie-invasion missing from the roster (Issue #198).
- Zombie-invasion unit 028 (ticker-1408, failed, chain
  zombie-2026-11-10 seq 28): the Mac mini is unreachable at the
  device transport - 2 computer.session starts failed node_offline
  (no wake-up path, last seen 2026-11-12T17:52:28Z), recovery-device
  repair and health both timed out at 25s. No game state observable,
  no input sent, nothing spent. This is a NEW failure mode, not the
  Issue #689 outcome_unknown lock (no outcome_unknown observed, no
  read-only snap possible): closed failed, blocker_category f, no
  blocker_overlay. With no blocker standing, every tick will burn
  one failed probe unit until the Mac returns - the draft issue for
  a device-offline pause is preserved in the unit record (filing
  blocked: connector issue_write 403 Resource not accessible by
  integration; VPS gh unreachable). Successor 029 enqueued to start
  now. Full detail in zombie-invasion/1415-queue-run.md.
- Delivery PARTIAL: push blocked by the VPS SSH outage (Permission
  denied publickey); the commit stays on local records/2026-11-13
  and no PR can be opened until the push succeeds.
- Zombie-invasion unit 029 (ticker-1813, failed, chain
  zombie-2026-11-10 seq 29): the Mac mini is still unreachable
  at the device transport - 2 computer.session starts failed
  node_offline (no wake-up path, last seen 2026-11-12T17:52:28Z,
  about 32.5h), connection.repair on the Mac failed the same
  way, recovery-device repair timed out at 25s. No game state
  observable, no input sent, nothing spent. Same NEW failure
  mode as unit 028, not the Issue #689 outcome_unknown lock
  (no outcome_unknown observed, no read-only snap possible):
  closed failed, blocker_category f, no blocker_overlay. 12th
  occurrence of the device-offline probe failure. Sync expired
  27 units (16:30/17:00/17:30 and 14:03 windows), produced
  none, due 22 already queued; live pool inbox 73, claimed 1,
  done 1866. The pass's sync and claim first ran through the
  main tree's stale queue.py (afe45a60, Nov 3) and were
  verified afterwards with the current tool (366b3b76,
  currency current, git_head a858a0fca); the local main tip
  22601972 (PR #700 merge) is ahead of the remote main and
  its queue.py reports stale, so it is not the current tool.
  Successor 030 enqueued to start now. Full detail in
  zombie-invasion/1823-queue-run.md.
- Delivery PARTIAL: push blocked by the VPS SSH outage
  (Permission denied publickey, about 30 hours); the commit
  stays on local records/2026-11-13 and no PR can be opened
  until the push succeeds. PR #708 will miss its 8th batch
  point at 19:00 PT tonight if the VPS is still down.
- Scout unit 010 (ticker-1933, failed, chain
  scout-2026-11-10 seq 10): the Mac mini is still unreachable
  at the device transport - computer.session start failed
  node_offline (no wake-up path, last seen 2026-11-12T17:52:28Z,
  about 49.5h), connection.repair on the Mac failed the same
  way, recovery-device repair and health both timed out at 25s.
  No game state observable, no input sent, nothing spent. Same
  NEW failure mode as units 028 and 029, not the Issue #689
  outcome_unknown lock (no outcome_unknown observed, no
  read-only snap possible): closed failed, blocker_category f,
  no blocker_overlay. 13th occurrence of the device-offline
  probe failure. Retro stats keys all present this time
  (stats_missing empty). Successor 011 enqueued to start now.
  Full detail in perception-scout/1933-queue-run.md.
- Delivery PARTIAL: push blocked by the VPS SSH outage
  (Permission denied publickey, about 31 hours); the commit
  stays on local records/2026-11-13 and no PR can be opened
  until the push succeeds. PR #708 has now missed its 8th batch
  point (19:00 PT tonight).
