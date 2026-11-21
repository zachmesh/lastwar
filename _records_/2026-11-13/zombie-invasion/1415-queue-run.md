---
title: Zombie Invasion unit 028 queue run
created: 2026-11-13T22:30:00Z
modified: 2026-11-13T22:30:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-1408, zombie-invasion unit 028 failed - Mac mini offline at the device transport (new failure mode, not Issue 689); scheduler delivered the 2026-11-12 14:04 tick a day late
status: unverified
---

# 14:15 to about 14:30 - Ticker pass ticker-1408, zombie-invasion unit 028 failed

- Date discrepancy, read first: this pass was scheduled for
  2026-11-12 14:04 PT and its run context is stamped Thu
  2026-11-12 14:08 PT, but it executed on Fri 2026-11-13
  14:08-14:30 PT. The VM clock and the GitHub server Date
  header agree it is Nov 13 (Fri 13 Nov 2026 22:25 GMT); the
  iPhone 16 Plus last_seen of 2026-11-13T00:19:12Z would be
  two hours in the future under Nov 12, which is impossible.
  This is the first Nov 13 execution, so the record lives
  under _records_/2026-11-13, the day INDEX is new, and the
  branch is records/2026-11-13 (created from main a858a0fca).
  The scheduler delivered the Nov 12 14:04 tick a day late
  (trigger dependency_probe); the cause is a scheduler matter,
  not a repo issue, and is noted here and in the final report
  rather than filed as one.
- Own PRs first: records PR 708 (2026-11-12) verified LIVE via
  the GitHub public API (VPS gh unreachable, local gh not
  logged in): OPEN, MERGEABLE/CLEAN, head 2f59c27047, base
  2260197212, 0 comments - no question addressed to this job.
  It awaits the integrator batch; it is yesterday's branch, not
  this pass's. PR 711 (knowledge fold, head
  work/ko-1132-lock-1047) and PR 425 (tools, still owner-gated
  OD-20261108-01) are owned by other jobs. Issues: newest open
  are #712 and #709, both tooling, both already known - no issue
  action by this job on those. One new gap found by this unit is
  filed below as a draft (filing itself blocked).
- Branch handling: the main working tree ~/workspace/lastwar
  still sits on work/ops-execution-records with another job's
  in-flight state and was not touched. This pass worked from a
  fresh main worktree ~/workspace/lastwar-worktrees/ticker-1408-main
  on branch ticker-1408-main at the remote main tip a858a0fca
  (PR #710 merge), created with pass_worktree.py and verified by
  HEAD and by the version command - no #709 stale-branch reuse
  this time. Delivery is a new worktree
  ~/workspace/lastwar-worktrees/ticker-1408-delivery on
  records/2026-11-13, also from a858a0fca.
- Tool currency (R10, Issue #694): current tool verified -
  _tools_/queue.py sha256
  366b3b76bf638befbc1d0cb81c6ba8417d21ef216e5cfb5fbc9fc903c1f476b0,
  git_head a858a0fca, currency current (same tool as
  ticker-1304 and ticker-1334). The main tree's tools/queue.py
  and the delivery worktree's copies are STALE and were not used
  for decisions. All queue operations ran through the current
  tool from the fresh main worktree against the live pool
  (--root ~/workspace/lastwar).
- Sync (current tool, live pool): reaped 0, expired 0,
  blockers_reaped ["control-lock"], produced none (due 24,
  already queued 24). The reaped blocker was recorded
  2026-11-12T20:08:13Z by ticker-1200 scout 009 - 26 hours old
  at sync, past the 4-hour stale bound, so the reap was correct
  and this probe was due (verified against the reap code and a
  scratch-pool test: a 26h-old control-lock blocker reaps, a
  fresh one is kept). Roster warning stands: the live pool holds
  units for zombie-invasion, a regular missing from the loaded
  roster (Issue #198). No zombie seeding needed (unit 028
  already in inbox, chain zombie-2026-11-10, done 20, pending 1).
- Zombie-invasion unit 028 (ticker-1408, failed, chain
  zombie-2026-11-10 seq 28): no game action was possible - the
  Mac mini is unreachable at the device transport. Two
  computer.session starts failed with node_offline ("device is
  offline and does not advertise a wake-up path"); connection.repair
  and connection.health through the recovery device both timed out
  after 25s (node_invoke_timeout). The device last_seen is
  2026-11-12T17:52:28Z, about 28 hours before this probe. No game
  state was observable at all - not even a read-only snap, so
  unlike the Issue #689 lock there is no live base-screen read to
  report. No input was sent, nothing was spent, no dialog was seen.
- This is a NEW failure mode, not Issue #689: #689 is the
  outcome_unknown control-channel lock with read-only observation
  still live; here the device transport itself is down, so no
  outcome_unknown was ever observed. The unit therefore closed
  failed with blocker_category f (missing precondition) and NO
  blocker_overlay - naming control-lock would misstate the error
  and corrupt #689's evidence. No comment was left on #689.
  Consequence, stated plainly: with no blocker standing, `next`
  hands out a unit on every tick and each tick burns one failed
  unit (plus a successor enqueue) until the Mac returns - the
  same burn pattern the control-lock blocker exists to prevent.
  The fix is a device-offline pause; see the draft issue below.
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 4 (2 session starts, repair, health).
  No coin, medal or stamina counts were measured - the game was
  never reached. No diamonds or money spent. verified no (no
  live game read in this unit).
- Evidence-path correction, disclosed: the unit was completed
  with evidence _records_/2026-11-12/zombie-invasion/1408-queue-run.md,
  written before the date discrepancy was found (the pass was
  scheduled for Nov 12). The record actually lives at
  _records_/2026-11-13/zombie-invasion/1415-queue-run.md (unit
  start 14:15 PT, Nov 13). The evidence line in the live done
  unit file was corrected to that path in the same pass; this
  paragraph is the disclosure. The done file is otherwise
  untouched.
- Chain: successor 029 enqueued in the same chain
  (zombie-2026-11-10) to start now (cleared false). The pass
  stopped after this unit rather than cascading failed units.
  Tracker untouched (failed unit). Token acquired 22:14:41Z and
  released 22:22:52Z.
- Follow-up - draft issue, filing BLOCKED (tooling): the new gap
  was filed three times through the GitHub connector and did not
  land. Attempt 1 died in a service restart before returning
  (verified not created: newest open issue still #712).
  Attempt 2 returned "missing required parameter: method".
  Attempt 3 with method create returned "failed to create issue:
  POST https://api.github.com/repos/zachmesh/lastwar/issues: 403
  Resource not accessible by integration". The VPS gh route that
  owns issue writes is unreachable (SSH outage below), so the
  draft is preserved here in full for filing from the VPS route
  once SSH returns. Title: "Ticker probe burns a failed unit
  every tick while the Mac is offline: no device-offline pause in
  the pool". Labels: tooling. Body: ticker-1408 claimed
  zombie-invasion unit 028 after the control-lock blocker aged
  out (recorded 2026-11-12T20:08:13Z, 26h old, past the 4h stale
  bound); the Mac mini was unreachable at the device transport
  (computer.session start failed twice with node_offline, no
  wake-up path, last seen 2026-11-12T17:52:28Z; connection.repair
  and connection.health through the recovery device both timed
  out after 25s); no game state observable, no input sent. This
  is not Issue #689 (outcome_unknown lock with observation live)
  - no outcome_unknown was observed, so no control-lock blocker
  was recorded. Consequence: with no blocker standing, next hands
  out a unit every tick and each burns failed until the Mac
  returns. Proposal: a device-offline blocker (or extended
  control-lock handling) recording the true transport error and
  the device last-seen time, pausing the picker while the device
  is unreachable, aging out on the same wait-and-retry rule.
  Evidence: this file.
- Delivery: PARTIAL - the push is blocked by the VPS SSH outage
  (Permission denied publickey, since about 12:46 Nov 12; the
  ~/.ssh loss from the Nov 12 cleanup). The commit stays on local
  records/2026-11-13; no PR can be opened for it until the push
  succeeds. PR 708 (Nov 12) is unaffected. The bundle route was
  attempted and failed at the SSH step; nothing was pushed.
