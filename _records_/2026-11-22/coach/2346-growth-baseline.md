---
title: Growth baseline - Total Power series and gain ledger
created: 2026-11-23T07:46:00Z
modified: 2026-11-23T08:02:00Z
version: 1.0.1
description: Coach record for Story 871 - the Total Power time series from every repository reading, the net and daily maximum pace, the 2026-11-09 outlier, the measured gain ledger, the weekly tracking template and the improvement metric
status: done
activity: coach
run_id: coach-2026-11-22-2346
trigger: coordinator assignment A-20261123-0741-coach
started_at: 2026-11-23T07:37:00Z
finished_at: 2026-11-23T07:50:00Z
duration_seconds: 780
verified: no
grounded_in:
  - source: run records under _records_ date folders, Total Power and Power Details readings, listed in total-power-series.csv and power-gain-ledger.csv
  - source: coordinator evidence message received during the assignment, on the 2026-11-09 fall and the ledger request
---

# Growth baseline

## Readings

53 distinct Total Power values, 2026-10-25 21:20 PT to 2026-11-22 22:48 PT, on 19 of 29 trade days ([series](total-power-series.csv)). Gaps: 11-05, 11-06, 11-12 to 11-15, 11-17 to 11-20. Dates are Pacific. The "11-23" reading of 150,080,120 was taken 11-22 at 19:55 PT, so "29 days" is date arithmetic; elapsed time is 27.98 days.

## Pace, two bases

| Basis | Change | Per day |
|---|---|---|
| Net, baseline to 150,080,120 | +390,502 | 13,466 over 29 date days; 13,955 elapsed |
| Net, baseline to latest 150,211,809 | +522,191 | 18,581 over 28.10 days |
| Daily maximum, 10-26 to 11-22 | +516,351 | 19,124 over 27 days |

Neither is a rate. Weekly net pace from the existing readings runs from -208,552 to +291,465 a day ([weekly-tracking.csv](weekly-tracking.csv)).

## Outlier, 2026-11-09

Power read 149,217,331 (16:35) and 146,730,949 (about 17:53); the difference, 2,486,382 in 78 minutes, is DERIVED from two readings and UNVERIFIED as a fall. Issue 549 tracks it; issue 482 is the 641,100 step on 11-08. See [fall analysis](2358-fall-analysis.md). Records: `_records_/2026-11-09/daily-activities/1748-queue-run.md`, `radar-tasks/1754-queue-run.md`, `total-power-149217331/1149-queue-run.md`. Four more dips of 1.6M to 4.6M (10-26, 10-29, 11-07, 11-22) each recovered within one hour to three days. A hospital treatment restored +329,400 on 10-26 at 14:03; wounded troops as the cause is a hypothesis only.

## By category

One breakdown exists, Power Details, read once on 2026-11-08 at about 09:58 PT ([categories](power-by-category.csv)): Hero 65,282,351, Drone 5,807,288, Building 10,292,275, and 68,468,439 (45.7 percent) unread. One reading gives no pace, so the baseline by category is a data gap. The [ledger](power-gain-ledger.csv) has 18 rows: troop 4 (+152,009 to +707,958 a batch), hero 10 (9 with power, +5,480 to +8,219 a level for 75M to 83M EXP), research 1 (+15,000), building 3 (one realized +21,600, two panel previews). Gear, skill, weapon: none.

## Not yet measured (snapshot 868)

Power Details in every category, twice a day in one fixed state; hospital counts; unit power by tier above Lv.9; tech power and each research's gain, time and cost; per-hero skill, gear and weapon power; each build's power, time and cost.

## Weekly tracking

The weekly CSV is the template, W1 to W5 filled from readings, with columns for fixed-state readings (am, pm), daily-maximum pace, category gains, plan item served and plan versus actual. Digest, one paragraph: "Week W<n>, <dates>. Total Power <start> to <end>, <gain>, <per day> a day (fixed state <am> and <pm>; daily maximum <per day>). Served: <plan items>. Plan <x> a day, actual <y>, <ahead or behind> because <one reason>. Decisions: <ids>. Next change: <one>. Owner questions: <list>."

## Metric

Power gain per day; baseline 13,466 net and 19,124 daily maximum; target set by the owner in the charter; measured on fixed-state readings once the snapshot lands. Entry: [IMP-20261123-08](../../retro/improvements-log/imp-20261123-08.md).
