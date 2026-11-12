---
title: Zombie Invasion unit 026 queue run
created: 2026-11-12T15:28:00Z
modified: 2026-11-12T15:28:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0704, zombie-invasion unit 026 failed - device input blocked (Issue 689, fifth consecutive probe pass, first R9 stale-bound probe)
status: unverified
---

# 07:04 to about 07:35 - Ticker pass ticker-0704, zombie-invasion unit 026 failed

- Own PRs first: records PR 685 (2026-11-12) was batch-MERGED
  at 07:08:53 PT during this pass (integrator 0700 run,
  b9bec1c9); the new records PR 700 for the same branch is
  OPEN and awaits the 11:00 batch - no new PR is owed by this
  pass. No question addressed to this job on either PR.
  Tools PR 425 is owned by lastwar-tool-developer, not this
  job. Tooling PR 699 (queue.py /tmp guard, rule R11) merged
  in the same batch.
- Branch handling: this pass worked from a fresh worktree on
  records/2026-11-12 (~/workspace/lastwar-wt-0704-ticker-1112)
  created at 62f803c9a. The main working tree
  ~/workspace/lastwar still sits on work/ops-execution-records
  with another job's in-flight state and was not touched. While
  this pass waited for the blocker stale bound, the branch
  advanced to 4e2ccf20 (tool-development 0632 run record,
  0632 correction, pr-integration 0700 run, 0700 push-hash
  fill); the worktree fast-forwarded to it after
  `git fetch --deepen=10` - the shallow-clone graft had made
  the merge refuse as unrelated histories until deepened.
  Current tool copy verified (_tools_/queue.py, R10 complied,
  no stale-tool recurrence).
- Sync: first sync reaped 0, expired 6 (the 0257-slot events,
  passes, secrets, treasures, trucks units and
  scout-midday-2026-11-11-0700), produced none (25 due,
  already queued). Zombie seeding: zombie-invasion unit 026
  already in inbox, no seeding needed; roster warning for
  zombie-invasion (issue #198) stands. Second sync at 07:20
  reaped the control-lock blocker (recorded 11:19:16Z, 4-hour
  stale bound reached 07:19:16 PT), expired 0, produced 0.
- Execute loop: after the blocker reaped, `next` handed out
  zombie-invasion unit 026 (chain zombie-2026-11-10 seq 26),
  claimed 07:20:49 PT. The probe: three fresh computer
  sessions (cc-708, cc-709, cc-710) all failed at the first
  input (open_app LastWar) with outcome_unknown - "An earlier
  action has an unresolved outcome. Stop sending input;
  read-only inspection is allowed. ... A new local user
  submission is required before input can resume. The
  reconcile action cannot clear this state." This is the same
  failure mode as ticker-0134, ticker-0204, ticker-0234 and
  ticker-0304 - the fifth consecutive ticker pass whose probe
  input was blocked by Issue 689, and the first probe since
  the R9 control-lock blocker was recorded: the 4-hour
  wait-and-retry did NOT clear the lock. The standing
  three-attempt rule was met inside this pass (cc-708/709/710).
- Game state verified live by read-only inspection: screen.snap
  (observation E48286C2-D7CA-4015-BB22-F6C8B4166BD0) shows the
  game on the base screen, window 642x951, Total Power
  149,218,973, coin 145.7M HUD, food 701.5M, iron 1.0G,
  banner quest Build: Oil Well (0/1). Power and coin are
  identical to ticker-0134's 01:34 and ticker-0304's 03:20
  readings, so no play has happened since the channel locked.
  Stamina is not visible on the base screen (last measured 84
  at 03:20). The lock is in the control channel, not the game
  and not authorization - the game needs no login and shows no
  dialog, and no "active on a different device" dialog appeared.
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 3. No exact coin panel reading was taken
  (control blocked before any game interaction; the 145.7M is
  a HUD rounding, not a panel read); medals and inventory
  stamina counts not measured. No diamonds or money spent.
- Chain: successor 027 enqueued in the same chain after
  completion (chain zombie-2026-11-10); the control-lock
  blocker re-recorded at completion (rule R9, issue #689), so
  the pool pauses until it ages out again (about 11:27 PT) or
  input succeeds. Tracker untouched (failed unit). Token
  released.
- Follow-up: Issue 689 comment added this pass (fifth
  consecutive blocked probe pass; first R9 stale-bound probe
  failed - no self-clear after 4 hours; a new local user
  submission on the Mac mini is still required before input
  can resume).
- Delivery: this record pushed to records/2026-11-12 (PR 700),
  verified with git ls-remote; push hash <PUSH_HASH>.
