---
title: Zombie Invasion unit 024 queue run
created: 2026-11-12T10:47:00Z
modified: 2026-11-12T10:47:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0234, zombie-invasion unit 024 failed - device input blocked (Issue 689)
status: unverified
---

# 02:34 to about 02:47 - Ticker pass ticker-0234, zombie-invasion unit 024 failed

- Own PRs first: records PR 685 (2026-11-12) OPEN and mergeable
  (CLEAN), no comments; records PR 681 (2026-11-11, post-2300
  batch) OPEN and CLEAN, no comments; tools PR 425 is owned by
  lastwar-tool-developer, not this job. No question addressed to
  this job.
- Sync: reaped 0, expired 7 (the 2026-11-11 2203/2230 stale inbox
  copies already closed on records/2026-11-12), produced none
  (due 23, already queued). No zombie seeding needed (units 024
  and 025 already in inbox; chain zombie-2026-11-10).
- Zombie-invasion unit 024 (ticker-0234, failed, chain
  zombie-2026-11-10 seq 24): no game action was possible. The
  computer-control channel locked at the first input in three
  fresh sessions (cc-700, cc-701, cc-702) - every activate of
  LastWar failed with outcome_unknown, "An earlier action has
  an unresolved outcome. Stop sending input; read-only
  inspection is allowed. ... A new local user submission is
  required before input can resume. The reconcile action cannot
  clear this state." A connection.repair attempt does not apply
  (target must be web, not computer-control). This is the same
  failure mode as ticker-0134 (scout 006, 01:34) and ticker-0204
  (help, 02:04) - the third consecutive ticker pass blocked by
  Issue 689, and the second consecutive pass blocked at the very
  first input with no dispatch at all.
- Game state verified live by read-only inspection: screen.snap
  (observation 7D61CA3A-CAE0-4918-8EE4-0E2FD2C19690) shows the
  game on the base screen, window 642x951, Total Power
  149,218,973, coin 145.7M HUD, food 701.5M, iron 1.0G, banner
  quest Build: Oil Well (0/1). Power and coin are identical to
  ticker-0134's 01:34 reading, so no play has happened since
  the channel locked. The lock is in the control channel, not
  the game and not authorization - the game needs no login and
  shows no dialog.
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 3. No exact coin panel reading was taken
  (control blocked before any game interaction); medals and
  stamina counts not re-measured. No diamonds or money spent.
- Chain: successor 025 is already in inbox (created 09:16:19Z,
  no not_before), so no new unit was enqueued; the next tick
  will pick it up and will hit the same wall unless the channel
  clears. Tracker untouched (failed unit). Token released.
- Follow-up: Issue 689 comment added this pass (third
  consecutive blocked ticker pass, same signature). The channel
  lock needs a local user submission on the Mac mini or a
  channel clear; retrying from this side has been exhausted
  three passes in a row.
