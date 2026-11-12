---
title: Zombie Invasion unit 027 queue run
created: 2026-11-12T17:52:00Z
modified: 2026-11-12T17:52:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0941, zombie-invasion unit 027 failed - device input blocked (Issue 689); stale-tool handout (Issue 694)
status: unverified
---

# 09:41 to about 09:56 - Ticker pass ticker-0941, zombie-invasion unit 027 failed

- Own PRs first: records PR 700 (2026-11-12) OPEN, no comments,
  mergeable UNKNOWN; tools PR 425 owned by lastwar-tool-developer,
  not this job. No question addressed to this job.
- Sync (stale tool, see below): reaped 0, expired 0, produced none
  (due 23, already queued 23). Roster warning stands: the live
  pool holds units for building-queues, research and
  zombie-invasion, regulars missing from the loaded roster
  (Issue #198). No zombie seeding needed (unit 027 already in
  inbox, chain zombie-2026-11-10, done 19, pending 1).
- Zombie-invasion unit 027 (ticker-0941, failed, chain
  zombie-2026-11-10 seq 27): no game action was possible. The
  computer-control channel locked at the first input in three
  fresh sessions (cc-713, cc-714, cc-715) - every activate of
  LastWar and open_app failed with outcome_unknown, "An earlier
  action has an unresolved outcome. Stop sending input; read-only
  inspection is allowed. ... A new local user submission is
  required before input can resume. The reconcile action cannot
  clear this state." Action IDs F826B498-B14A-4F50-B44A-312E7F2B4E85
  (cc-713 activate), 7AA9A015-95A7-4170-86A3-01B6AC0014DB (cc-714
  activate), B48EA218-038C-476D-A0BC-A838746C4B6E (cc-715 open_app).
  `input_dispatched: false` on all three - nothing was sent, so
  nothing was replayed. This is the same failure mode as
  ticker-0134 (scout 006, 01:34) and every blocked pass since -
  the lock has now persisted about 8 hours and survives fresh
  sessions started hours apart. This is the sixteenth consecutive
  ticker pass blocked by the lock (0134, 0204, 0234, 0304, 0334,
  0404, 0504, 0534, 0604, 0634, 0704, 0737, 0804, 0834, 0904,
  0941) and the seventh unit burned on it (006, help-2230, 024,
  025, 026, 008, 027).
- Game state verified live by read-only inspection: computer.observe
  (observation B6628CA8-6BF9-48FA-B60F-76283030A550) shows the game
  on the base screen, window 642x951, HEROES and WORLD buttons
  visible, no dialog. The power OCR in that observation was
  garbled and is not claimed as a fresh figure; the screen matches
  the 0737 pass's live read (power 149,218,973) in outline, so no
  play has happened since the channel locked. The lock is in the
  control channel, not the game and not authorization - the game
  needs no login and shows no dialog. No "active on a different
  device" dialog appeared.
- Stale-tool handout (Issue #694): this pass ran its sync, token,
  next and claim through the main working tree's `tools/queue.py`,
  which predates both the tools-to-`_tools_` move and PR #692 - it
  does not know the control-lock blocker and handed out unit 027
  although the blocker (recorded 15:47:00Z by ticker-0737 scout
  unit 008, 4-hour stale bound to 19:47Z) still stands. Verified
  after the failure with the current tool from a fresh worktree
  (`lastwar-wt-0941-ticker`, main 33cf659cd7): `next` there returns
  empty while the blocker stands, exactly as PR #692 designed.
  The unit was therefore completed as failed with the current
  tool, which refreshed the blocker. The main tree's stale
  `tools/queue.py` must not be used for decisions again - the
  #694 guard exists precisely to refuse it, and the old copy
  predates the guard.
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 3. No exact coin panel reading was taken
  (control blocked before any game interaction); medals and
  stamina counts not re-measured. No diamonds or money spent.
  blocker_category e (repeated blocker), blocker_overlay
  control-lock.
- Chain: successor 028 enqueued in the same chain
  (zombie-2026-11-10) to start now (cleared false); it will sit
  in inbox behind the control-lock blocker until the blocker ages
  out at 19:47Z (11:47 PT), when the next tick probes again. The
  pass stopped after this unit rather than cascading failed units.
  Tracker untouched (failed unit). Token released.
- Follow-up: Issue #689 commented this pass (eighth hour of the
  lock, seventh burned unit, three fresh sessions, same
  signature). Issue #694 commented this pass (stale-tool handout:
  the main tree's `tools/queue.py` decided on old behaviour and
  burned a unit the current tool would have held back).
- Delivery: pushed 30bb0568ea1eb930d3beac6c61aba16b9dd30d70 to records/2026-11-12 (PR 700), verified with
  git ls-remote.
