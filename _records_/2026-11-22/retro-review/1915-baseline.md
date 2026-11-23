---
title: Retro review baseline run 1915
created: 2026-11-23T03:15:00Z
modified: 2026-11-23T03:15:00Z
version: 1.0.0
description: Coach baseline pass for the continuous-play team - the first improvement dashboard, its three seven-day target movements, and the pool basis gap the run had to name, read-only on the game
status: done
activity: retro-review
run_id: retro-review-2026-11-22-1915
trigger: owner
started_at: 2026-11-23T03:11:03Z
finished_at: 2026-11-23T03:15:00Z
duration_seconds: 237
verified: no
grounded_in:
  - source: retro_report.py 1.5.5 run on the repository pool, window 2026-11-16 to 2026-11-22, appendix /tmp/lw-baseline
  - source: daily retro 2026-11-21, dashboard sections A to D, top leak points, pool snapshot
  - source: evaluation metrics families A to D and the Monitoring threshold set
  - source: continuous-play-team.md section 8, phase acceptances P1 to P3
---

# Baseline run (2026-11-22 19:15)

The coach seat's first pass - build the baseline dashboard for the
continuous-play team. Read-only on the game, which is stopped at
establishment. The run is bounded to the dashboard and its record; it
rewrote no retro file, no backlog entry, and no play or queue record.

## Inputs

- The repository pool `_queue_/done` - 2310 done units scanned, pool
  sha256 `82c7e7fd8ee0aa40...` - read by `_tools_/retro_report.py`
  1.5.5 over 2026-11-16 to 2026-11-22. Appendix at
  `/tmp/lw-baseline/2026-11-22-data.json`, deliberately outside the
  repository, because the canonical appendix for a date is written by
  that date's retro.
- [2026-11-21](../../retro/2026-11-21.md), dashboard A to D, top leak
  points, and the pool snapshot that fixes the VPS live pool at 2800
  done units under tool 1.5.1.
- [evaluation-metrics.md](../../../_conventions_/local-conventions/evaluation-metrics.md)
  families A to D and the Monitoring thresholds;
  [continuous-play-team.md](../../../_conventions_/local-conventions/continuous-play-team.md)
  section 8.
- Seat pages `_seats_/coach/INDEX.md`, `duties.md`, `handover.md` and
  `_seats_/SEAT-PROTOCOL.md`.

## Outputs

- `_records_/retro/improvement-dashboard.md` v1.0.0 - the L1, L2 and L3
  baselines, the basis caveat, the three target movements M1 to M3, and
  the named data gaps.
- `_records_/retro/INDEX.md` v1.0.2 - lists the dashboard under contents
  by file shape.
- This record, `_records_/2026-11-22/retro-review/1915-baseline.md`.
- Not written, and named here so the omission is explicit - the
  `_records_/2026-11-22/INDEX.md` day section (outside this seat's write
  scope, for the coordinator), the retro file, the improvements
  backlog, and anything under `_queue_/`.

## Stats

- L1 baseline, 215 executions in window - done 15 of 215 (7.0 percent),
  unverified 129 of 215 (60.0 percent), median 309.5 seconds, p90 600
  seconds, attempts mean 0.5907, max 2.
- Per-regular top five by volume - harvest 26, scout 22, radar 21,
  survivors 14, passes 14, with donations also 14 in a fifth-slot tie.
- L2 baseline - ledger coverage 5 of 23 lines, unexplained red dots 1
  against 0 unresolved (#800), 11 top leaks carried by number.
- L3 baseline - 2 closed and 7 filed at the 2026-11-21 read, 172 open,
  oldest #118 at 19 days; eight metric groups named as data gaps.
- Basis gap measured - the six overlapping days carry 174 repository
  executions against the retro's 634, so no trend is claimed across the
  two pools.
- Files written 2, index edits 1, write-scope violations 0.

## Follow-up

- Coach, 2026-11-23 - re-run the same command and append the M1 to M3
  movement rows to the dashboard; the comparison is only valid on the
  same pool and tool 1.5.5.
- Coordinator - append this run to the 2026-11-22 day index, which is
  outside the coach write scope.
- Coordinator, for the owner register if it stands - the pool basis gap
  (174 against 634 executions on the same six days) is a C1 records
  question, filed nowhere yet, and it is the reason a baseline exists
  rather than a trend. The named mechanisms are tool drift (#724) and
  the live/branch split (#800, #801, and the conflicting records stack
  of top leak 4).
