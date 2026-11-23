---
title: Daily measurement report - first, 2026-11-23Z
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T07:50:00Z
version: 1.0.0
description: First coach daily report after the measurement restart - snapshot log growth and gaps, fixed-state power readings, idle-slot misses, and gain by category against plan
status: partial
activity: coach
run_id: coach-2026-11-22-2350
trigger: coordinator order to restart the measurement, owner-delegated decision record 2350
started_at: 2026-11-23T07:47:00Z
finished_at: 2026-11-23T07:50:00Z
duration_seconds: 180
verified: no
grounded_in:
  - source: _tools_/state/resources.jsonl read at 07:49Z, 15 rows
  - source: _records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md
  - source: run records listed in misses-log.csv and fixed-state-readings.csv
---

# Daily measurement, first report

Preliminary at 07:50Z; the due report at 12:00Z re-counts. Reads only; the coach holds no device token.

## 1. Snapshots

`resources.jsonl` grew today: one row at 07:49:06Z, the operator's growth read (total power 150,211,809, food 638.0M, iron entered as a rounded 1,000M, coin 9.6M). Before it: 14 rows, last 2026-10-28T02:40 local, a gap of 25.9 days. Other gaps: 28.1 hours on 10-26 to 10-27; only 4 of those 14 rows carried total power; no row carries a breakdown. Against the reserve floors, food is 6.4 times and iron 6.7 times its floor; coin sits 0.4M under 10M.

## 2. Power readings, fixed state

Slot A (02:00Z to 04:00Z): 150,080,120 at 03:55Z, total only. Slot B (13:00Z to 15:00Z): pending, after the 12:00Z deadline. Pairs complete to date: 0 of 2 ([readings](fixed-state-readings.csv)). The window widths are my proposal for the coordinator to confirm. Breakdown reads today: 0; the last was 2026-11-08. Request to the operator: read every Power Details line, tech and troop included, at slots A and B and run snap with the breakdown.

## 3. Misses

On 2026-11-22 Pacific, 10 reads showed slot state ([log](misses-log.csv)). Idle found in 7: builders in 6 reads (22 idle slots), one barracks in 1 read (Lv.24, idle over 10 hours, blocked by Drill Ground Full, issue 678). Labs: idle in 0 of the 7 reads that showed them. All 7 precede the 07:43Z fill order, so they are the baseline. `_records_/2026-11-22/growth/` does not exist yet, so misses after the restart are not measured; that is not zero.

## 4. Gain by category, plan versus actual

Not computable: one breakdown exists. The [ledger](power-gain-ledger.csv) has measured gains per action instead. No plan exists until the charter, so weekly row W6 in [weekly-tracking.csv](weekly-tracking.csv) stays blank. Net pace stays 13,466 a day and daily-maximum 19,124.

## Next

At 12:00Z: re-read the log, add slot A and B rows, and count misses from the growth folder.
