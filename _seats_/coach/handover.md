---
title: Coach seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:22:00-08:00
level: L2
version: 0.2.0
description: The coach's live state after the first baseline dashboard
status: unverified
grounded_in:
  - source: baseline dashboard 2026-11-22 19:15 PT, _records_/retro/improvement-dashboard.md
---

# Handover - coach

Updated 2026-11-22 19:22 PT.

## Holder

- Seat: `coach`, session `session-cfc4492f-b4f7-4ea0-b9c9-772186236af4`.
- Scope: `_records_/retro/`, `_records_/2026-11-22/retro-review/`.

## State

- Dashboard `_records_/retro/improvement-dashboard.md` 1.0.0 is the
  baseline. L1 on the repository pool: 215 executions, done 15 (7.0
  percent), unverified 129 (60.0 percent), median 309.5 s, p90 600 s.
  L2: ledger coverage 5 of 23; unexplained red dots unresolved 1 vs 0.
  L3: 172 open GitHub issues at the 2026-11-21 read; archive backlog
  frozen and not live state.
- Three movements: M1 unverified at or below 0.20 and falling; M2 coverage
  23 of 23 every sweep day; M3 at least 3 verified closures, recurrence 0.
- The repository pool carries about 27 percent of the VPS live pool volume
  on the overlapping days. The 60.0 percent figure is not comparable to the
  retro's 91.3 percent; the pool basis is part of every number.
- The duel research note corrects the 1400 Match Record read: its pairs are
  week win-point totals, not per-day scores. Fold that into the next retro.

## Next pass

1. Re-run `retro_report.py --days 7 --format json --out-dir /tmp/...` on
   2026-11-23 and append the M1 to M3 movement rows to the dashboard.
2. File the pool-split finding and the two planner tooling defects as
   issues or owner decisions; do not close anything on an edit alone.
3. Run the daily retro only after the fresh pool has one full day.
