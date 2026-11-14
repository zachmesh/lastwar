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
