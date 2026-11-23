---
title: Planner decisions and the scribe re-split go - 2026-11-22 22:11 PT
created: 2026-11-22T22:11:00-08:00
modified: 2026-11-22T22:12:00-08:00
level: L3
version: 0.1.0
description: The Zombie Siege watch unit reviewed, three sequencing and coverage decisions, the sweep pair staged next, and the go for the alliance-donations re-split
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2211-planner-decisions
trigger: planner reply on A-20261123-0607 (note 2210-watch-unit); scribe digest and toolsmith splitter delivered
started_at: 2026-11-22T22:10:00-08:00
finished_at: 2026-11-22T22:12:00-08:00
duration_seconds: 120
verified: the minted unit file read directly (priority 2, not_before 2026-11-24T01:10Z, expires_at 2026-11-24T02:00Z)
---

# Planner decisions and the scribe re-split go

## Watch unit

`scout-midday-2026-11-23-0609` (queue inbox): priority 2 on purpose, because sync re-times an aged priority 1 unit once its `not_before` passes and would erase the window; `not_before` 2026-11-24T01:10Z, `expires_at` 02:00Z; 15 minutes.

## Decisions (assignment `A-20261123-0611-planner`, due 06:45Z)

1. **Sequence on 11-24 UTC:** the zero-sweep final pass (priority 1, 01:00Z, up to 15 minutes) runs first; the siege watch follows through `next` from about 01:15Z and reads the result mail after the 01:45Z stage end, inside the 02:00Z expiry. No unit is re-timed; one sentence is added to the watch brief.
2. **Stage the sweep pair** for 11-24 (00:00Z and 01:00Z, roster 120 and 60) with `queue.py sweep`, proven by validate and sweep-status.
3. **Alliance Exercise** at 23:00Z on 11-23: approved, a read-only watch for 22:55Z to 23:35Z with both fields. **Winter Battlefield** at 11:00Z: not minted, 5v5 PvP, held for OD-20261123-03.

## Planner findings

Alliance Exercise and Winter Battlefield had no coverage. sweep-status exits 1 for 11-22 (ended and missed, not backfilled) and for 11-23 (pair not staged yet); slot_coverage exits 1 on 44 historical recordless slots.

## Scribe

`A-20261123-0611-scribe`, due 06:50Z: re-split `alliance-donations` with the key-named splitter on a fresh branch from main, bring the digest over with remapped article names, and fold the verified UTC-2 server clock into `_knowledge_/events-and-cycles`.

## Planner reply and decision B (appended 2026-11-23T06:15Z)

- Staged by `queue.py sweep --regular zero-sweep --date 2026-11-23`: `zero-sweep-2026-11-23-1600` (priority 1, not_before 2026-11-24T00:00Z, expires 02:00Z) and `zero-sweep-2026-11-23-1700` (priority 1, not_before 01:00Z, expires 02:00Z), both created 06:12:47Z, plus 12 priority-1 fix-ups (not_before 00:30Z, est 67 minutes). The Alliance Exercise watch `scout-midday-2026-11-23-0612` (priority 2, 22:55Z to 23:35Z) is minted. Winter Battlefield is held for OD-20261123-03. Unit files read by the coordinator match.
- Finding: the queue would NOT have sequenced the pair before the siege watch. A priority 2 unit older than 2 hours counts as priority 1, and the watch (created 06:09:09Z) is older than the pair; the planner's simulation ranks the watch third at 01:10Z, ahead of the fix-ups and both passes.
- Decision B (`A-20261123-0615-planner`): withdraw `scout-midday-2026-11-23-0609` with the tool's expired completion and mint a replacement created after the sweep units, same window and brief; re-run the ranking at 01:10Z and 01:50Z. The ordering must live in the queue, not in a name-based dispatch.
- Accepted as designed: the 12 fix-ups. The load note (97 minutes estimated in the 90 from 00:30Z) is to be watched against the observed pace of about 3.0 minutes per unit.
