---
title: Queue Planning Zombie Siege Watch Unit 2210 2026-11-22
created: 2026-11-22T22:16:00-08:00
modified: 2026-11-22T22:16:00-08:00
level: L0
version: 1.0.0
description: Planner staging pass for assignment A-20261123-0607 - one read-only watch unit minted for the Zombie Siege of 2026-11-24T01:15Z, no coverage found for Alliance Exercise or Winter Battlefield, two units proposed and not minted, validate exit 0
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2210-watch-unit
trigger: coordinator assignment A-20261123-0607-planner
started_at: 2026-11-22T22:07:26-08:00
finished_at: 2026-11-22T22:16:00-08:00
verified: unit file read back after minting and after the body edit; validate exit 0 after the edit; sweep-status, slot_coverage and next captured; reap and sync not run
grounded_in:
  - source: _records_/2026-11-22/perception-scout/2205-queue-run.md, operator read of the To-do List at 06:05Z, UTC-2 to the second
  - source: _records_/2026-11-22/queue-planning/2210-watch-unit-rows.json rows 1 to 7 and the proof block
  - source: _tools_/queue.py enqueue and _window_aged_priority1, read before minting
---

# Zombie Siege watch unit, 2210

Rows, commands and proof are in [the sidecar](2210-watch-unit-rows.json).

## 1. Minted

`scout-midday-2026-11-23-0609`, regular `scout-midday`, activity `perception-scout`, priority 2, 15 minutes.
`not_before` 2026-11-24T01:10:00Z, `expires_at` 2026-11-24T02:00:00Z, for the siege at 01:15Z (17:15 PT on 11-23). `enqueue` exit 0.

- **Priority 2 is deliberate.** At priority 1, `sync` re-times an unscheduled unit once its `not_before` passes and it is over four hours old, replacing the window with now plus four hours. That would erase this window at 01:10Z.
- **The brief is in the unit body**, appended after minting, because `enqueue` writes boilerplate only. The frontmatter is untouched. It carries the observe-the-stage and result-mail steps and the red lines: no attack, rally, join, march or PvP, and any such surface stops as `needs-owner`.
- **One slice only.** The stage runs 01:15Z to 01:45Z and the result mail follows, but the unit cap is 15 minutes. The brief tells the dispatcher to start near 01:10Z (prep and banner) or near 01:35Z (stage end and mail).
- **Dispatch by name.** `next` does not hand the unit out before 01:10Z, and other work will outrank it by priority.

## 2. Coverage of the other two

Neither event has a regular, an activity folder or an inbox or claimed unit.

- **Alliance Exercise, 23:00Z today (15:00 PT).** Not covered as a watch. Its reward mail is read by the every-run `mail` regular at its 02:30Z slot on 11-24, not yet staged. Proposed: one watch unit, window 22:55Z to 23:35Z.
- **Winter Battlefield, 11:00Z today (03:00 PT).** Not covered as play. The `events` regular claims its Rewards chest, but no events unit is staged. Match is 5v5 PvP, gated by OD-20261123-03, which is open. Proposed: hold. If wanted, a read-only opening watch, window 10:55Z to 11:30Z.

Both commands are in the sidecar. Neither was run.

## 3. Proof

- `validate`: exit 0, run after the body edit.
- `sweep-status` for 11-22: exit 1, pair 0 of 2; that day ended at 02:00Z and is recorded as missed, not backfilled.
- `sweep-status` for 11-23: exit 1, pair 0 of 2, not staged yet.
- `slot_coverage` for 11-22: exit 1, 44 recordless past-window slots, historical.
- Counts: inbox 17, claimed 0 to 2, done 2,632.
- `reap` and `sync` were not run: they move units into done and stage new ones, outside the inbox-only scope.

## 4. Follow-up

- **Collision:** the 11-23 zero-sweep final pass opens at 01:00Z and may run 15 minutes, so it abuts the watch at 01:10Z. The coordinator should sequence them or take the 01:35Z slice.
- **Next planning pass:** stage the 11-23 sweep pair, slots 00:00Z and 01:00Z on 11-24.
