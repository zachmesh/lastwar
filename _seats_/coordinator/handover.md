---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:21:00-08:00
level: L2
version: 0.2.0
description: The live state a replacement coordinator starts from after the 2026-11-22 establishment
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT, _records_/2026-11-22/team-operations/setup.md
  - source: queue genesis 2026-11-22 19:17 PT, _records_/2026-11-22/queue-planning/1917-genesis.md
---

# Handover - coordinator

Updated 2026-11-22 19:21 PT.

## Holder

- Seat: `coordinator`, session `session-eb024f72-e661-4a77-9303-66af95dbcfd1`.
- Loop clock: `schedule-9de37067-4365-474f-8d53-eb57d44f8166`, every 900
  seconds, first firing 2026-11-23T03:23:31Z.

## Open commitments

- PR #858 `work/continuous-play-team` is open and carries the team setup
  and the records commit. It is not merged; `main` is protected and `gh`
  is not installed, so the PR was opened through the GitHub API.
- The game is stopped by the owner. Do not start it; the owner restarts it
  after the team is fully working.
- When the game returns: the operator's first act is a state read, then the
  one-time computer-use app approval for `com.lastwar.ios` through the
  control link.

## Current state

- Queue genesis done: inbox 37, claimed 0, done 2,612; 302 expired, 427
  duplicate copies dropped. The previous host's live pool was not migrated;
  its done units are a data gap, not zero. Owner decision OD-20261122-01
  asks whether to recover it or accept the reset.
- Baseline dashboard: `_records_/retro/improvement-dashboard.md` 1.0.0.
  L1 done 7.0 percent, unverified 60.0 percent on the repository pool;
  L2 coverage 5 of 23; L3 172 open issues at the 2026-11-21 snapshot.
- Duel research note: `_records_/2026-11-22/research/duel-day-loss.md`.
  The 13-point six-day table and the 02:00Z day window are supported; the
  2026-11-21 day-6 outcome is unverified. The falsification test is assigned
  to the operator for the next live duel day.
- The experimental Agent Teams bundle was tested and removed from the web
  profile: its installed version was older than the DSH core, and the
  current session could not be populated as its Lead. The eight seats are
  delegated child sessions; the first weekly review decides whether to
  migrate them to top-level workspace sessions.

## Lessons

- The queue in this checkout is a stale snapshot, not the live pool. Never
  treat a main-checkout `_queue_` count as the live pool without reading the
  day index and the records branch.
- A queue reset is a genesis reset. Record the genesis timestamp; never
  backfill missed cycles.
- The coach must not compare this repository pool's L1 numbers with the
  retro's VPS live-pool numbers. The pool basis is part of every figure.

## Next actions

1. At the first tick after the owner restarts the game: operator state read,
   then one low-risk unit; record the app approval wait if it appears.
2. Assign the scout the first full ledger walk of the new game day.
3. Have the coach re-run the baseline command on 2026-11-23 and append the
   M1 to M3 movement rows.
4. Keep PR #858 moving; when the owner provides `gh` or a merge route, land
   it and reset local `main` to `origin/main`.
