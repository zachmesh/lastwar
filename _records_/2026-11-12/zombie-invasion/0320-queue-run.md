---
title: Zombie Invasion unit 025 queue run
created: 2026-11-12T11:20:00Z
modified: 2026-11-12T11:20:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0304, zombie-invasion unit 025 failed - device input blocked (Issue 689, fourth consecutive pass)
status: unverified
---

# 03:04 to about 03:20 - Ticker pass ticker-0304, zombie-invasion unit 025 failed

- Own PRs first: records PR 685 (2026-11-12) went CONFLICTING after
  PR 681 merged at 03:02 PT (integrator note, 21 files). Resolved
  branch-side before any game work: merged main 0dc85d79 into
  records/2026-11-12 in this worktree (merge commit 8cdab1cb2f5,
  to be pushed with this delivery) - _queue_/done 2026-11-11
  files take main as authoritative (radar-1803 done and
  survivors-1803 partial kept over this branch's expired
  copies); stale inbox duplicates scout-006 and zombie-023
  removed (already executed on this branch); future 14:03/14:30
  staged units and scout-007 kept; action-log union of both
  tails (main 9 + branch 16 over the 1867-line base). Two
  merge artefacts repaired before committing: a conflict-marker
  block staged into inbox/scout-007 and main's expired result
  block merged into inbox/donations-1403 (both restored to the
  branch version); one done file (donations-1803) needed an
  explicit rewrite to main's version after checkout --theirs
  left a hybrid header. Verified clean: no unmerged paths, no
  conflict markers, no inbox file with a result block, no
  inbox/done duplicate, all 14 conflicted done files
  byte-identical to main. Tools PR 425 is owned by
  lastwar-tool-developer, not this job. The branch tip moved
  during this pass (integrator 0300 record, 7c30af3183b);
  delivery merges it in.
- Sync: worktree-pool sync reaped 0, expired 10 (the
  2026-11-11 2230/2257 stale inbox copies), produced none
  (due 25, already queued). Live-pool sync reaped 0, expired
  5 (the 2257 units whose 02:57 PT expiry had passed
  unexpired in the live pool). No zombie seeding needed
  (unit 025 already in the live inbox; chain
  zombie-2026-11-10). Roster stale warning on the live sync
  (zombie-invasion missing from the loaded roster, issue
  #198) - the chain, not the tracker, governs this regular.
- Zombie-invasion unit 025 (ticker-0304, failed, chain
  zombie-2026-11-10 seq 25): no game action was possible. The
  computer-control channel locked at the first input in three
  fresh sessions (cc-703, cc-704, cc-705) - every open_app of
  LastWar failed with outcome_unknown, "An earlier action has
  an unresolved outcome. Stop sending input; read-only
  inspection is allowed. ... A new local user submission is
  required before input can resume. The reconcile action cannot
  clear this state." This is the same failure mode as
  ticker-0134 (scout 006, 01:34), ticker-0204 (help, 02:04)
  and ticker-0234 (zombie 024, 02:34) - the fourth consecutive
  ticker pass blocked by Issue 689, the eleventh consecutive
  failed first input across those passes. The standing
  three-attempt rule was met inside this pass (cc-703/704/705).
- Game state verified live by read-only inspection: screen.snap
  (observation 1D827308-9563-4158-9A2E-4CA6E821EC79) shows the
  game on the base screen, window 642x951, Total Power
  149,218,973, coin 145.7M HUD, food 701.5M, iron 1.0G,
  stamina 84, banner quest Build: Oil Well (0/1). Power and
  coin are identical to ticker-0134's 01:34 and ticker-0234's
  02:40 readings, so no play has happened since the channel
  locked. The lock is in the control channel, not the game
  and not authorization - the game needs no login and shows
  no dialog, and no "active on a different device" dialog
  appeared.
- Result stats: zombies_killed 0, cleared false,
  coins_collected 0, squads_parallel 0, chests_opened 0,
  control_attempts 3. No exact coin panel reading was taken
  (control blocked before any game interaction; the 145.7M
  is a HUD rounding, not a panel read); medals and inventory
  stamina counts not measured. No diamonds or money spent.
- Chain: successor 026 enqueued in the same chain after
  completion (chain zombie-2026-11-10); the control-lock
  blocker recorded at completion (rule R9, issue #689, PR
  #692) gates the pick until the lock ages out (4 hours) or
  input succeeds, so the successor waits instead of burning
  another failed unit. Tracker untouched (failed unit).
  Token released.
- Follow-up: Issue 689 comment added this pass (fourth
  consecutive blocked ticker pass, same signature; R9
  control-lock blocker now recorded, first use of the
  mechanism). The channel lock needs a local user submission
  on the Mac mini or a channel clear; retrying from this side
  has been exhausted four passes in a row.
- Delivery: merge resolution 8cdab1cb2f5 plus this record
  pushed to records/2026-11-12 (PR 685), verified with git
  ls-remote; PR 685 conflict-resolution reply posted.
