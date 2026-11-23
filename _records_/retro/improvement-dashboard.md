---
title: Improvement dashboard
created: 2026-11-23T03:14:00Z
modified: 2026-11-23T03:14:00Z
level: L2
version: 1.0.0
description: First baseline dashboard of the continuous-play team - the L1 execution, L2 perception and L3 improvement baselines read on 2026-11-22, plus three seven-day target movements with their source field and threshold
status: unverified
grounded_in:
  - source: retro_report.py 1.5.5 run on the repository pool, window 2026-11-16 to 2026-11-22, appendix at /tmp/lw-baseline
  - source: daily retro 2026-11-21, sections Evaluation dashboard A to G, Top leak points, and Pool snapshot
  - source: evaluation metrics family A to D and its Monitoring threshold set
  - source: continuous-play-team.md section 8 phase acceptances P1 to P3
---

# Improvement dashboard

The standing L1, L2 and L3 baseline for the continuous-play team. Read
it with the rule the [evaluation metrics](../../_conventions_/local-conventions/evaluation-metrics.md)
set - every number carries its source, and a number the records do
not produce is a data gap, never a zero.

Sources are cited short here. `BASELINE` means the fresh run of
`python3 _tools_/retro_report.py --days 7 --format json --out-dir /tmp/lw-baseline`
on 2026-11-22, tool 1.5.5, window 2026-11-16 to 2026-11-22, appendix
`/tmp/lw-baseline/2026-11-22-data.json`. `RETRO` means
[2026-11-21](../../_records_/retro/2026-11-21.md), its dashboard
sections cited by letter.

## 0. The basis caveat that governs every L1 number here

The two sources are not the same pool, and no direction is claimed
across them.

| | BASELINE | RETRO |
|---|---|---|
| Tool | retro_report.py 1.5.5 | retro_report.py 1.5.1 |
| Pool | repository pool, 2310 done units scanned | VPS live pool `/home/hatch/workspace/lastwar`, 2800 done units |
| Pool sha256 (first 8) | `82c7e7fd` | `1ba02827` |
| Window | 2026-11-16 to 2026-11-22 | 2026-11-15 to 2026-11-21 |
| Executions in window | 215 | 755 |

- The two pools overlap on six days. Over 2026-11-16 to 2026-11-21
  the repository pool counts 174 executions where RETRO counts 634 -
  the repository `_queue_/done` here carries about 27 percent of the
  volume the VPS live pool carried for the same days (BASELINE
  `regulars.*.by_day` against RETRO per-day recount).
- The mechanism is the pool split (#800, #801, RETRO top leak 10) - the
  repository copy of `_queue_/done` does not hold every unit the live
  pool held. Tool drift (#724) additionally makes points not
  comparable across the two. Until both close, the L1 baseline below is
  the reproducible figure for this repository and the RETRO figures are
  reference only.
- Consequence for the three movements in section 4 - their baselines
  are read on the BASELINE pool with tool 1.5.5, so a future run of
  the same command is directly comparable to them.

## 1. L1 baseline - execution

Window 2026-11-16 to 2026-11-22, 215 executions, 42,852 executor
seconds (BASELINE `totals`).

| Metric | Baseline | Source field |
|---|---|---|
| Done rate | 15 of 215, 0.070 (7.0 percent) | `totals.statuses.done` / `totals.executions` |
| Status mix | done 15, partial 49, failed 62, expired 89 | `totals.statuses` |
| Unverified rate | 129 of 215, 0.600 (60.0 percent) | `totals.unverified` / `totals.executions` |
| Unverified reasons | verified_not_yes 129, missing_required_stats 100, missing_result 0 | `totals.unverified_reasons` |
| Duration median | 309.5 seconds | `totals.duration_median_seconds` |
| Duration p90 | 600 seconds | `totals.duration_p90_seconds` |
| Attempts | mean 0.5907, max 2, share over one attempt 0.0047 (one unit) | `totals.attempts_mean`, `attempts_max`, `attempts_gt1_share` |
| Missing keys | achieved 98, target 98, verified 98, resources_gained 99, costs 100, blocker_category 8 | `totals.missing_key_counts` |

Per-regular top five by volume in the window (BASELINE
`regulars.<regular>.rolling.executions`) -

| Regular | Executions | Status mix | Unverified |
|---|---|---|---|
| harvest | 26 | expired 3, failed 17, partial 6 | 10 |
| scout | 22 | done 1, expired 1, failed 1, partial 19 | 2 |
| radar | 21 | done 4, expired 3, failed 13, partial 1 | 7 |
| survivors | 14 | done 1, expired 3, failed 6, partial 4 | 7 |
| passes | 14 | done 2, expired 4, failed 7, partial 1 | 10 |

`donations` also counts 14, so the fifth slot is a tie between
`passes` and `donations`; the table shows `passes` to keep five rows
and does not rank the two. `ghost-ops` reports no data
(`no_data_regulars`) and is a data gap, not a zero.

## 2. L2 baseline - perception

- **Ledger coverage 5 of 23 lines** with a same-day live status on
  the 2026-11-21 read (RETRO B). Threshold is 23 of 23 on a sweep
  day (evaluation metrics, Monitoring) - breach. The 2026-11-22
  coverage is a **data gap**, not 5 and not 0: the day folder holds
  no `perception-scout/` and no `daily-activities/` pass, so no line
  was walked today.
- **Unexplained red dots - UNRESOLVED, 1 against 0.** The latest
  pass narrative reports 1 (ticker-2004, a red target badge); the
  coverage file reports 0; the two contradict each other and the
  contradiction is filed as issue #800 (RETRO B and top leak 7).
  This dashboard does not average the two and does not pick one. The
  threshold is 0 on any perception day (evaluation metrics,
  Monitoring) - on the narrative reading it is a breach, on the
  coverage reading it is not.
- **Top leaks carried from 2026-11-21 - 11 named** (RETRO, Top leak
  points). They are the L2 and loop backlog this team inherits, in
  the retro's own numbering. The class column is assigned here by the
  coach seat for grouping; the retro names the leaks by number and does
  not classify them, so the class is not a retro finding.

| # | Leak | Class |
|---|---|---|
| 1 | Duel day 6 lost whole, fifth consecutive duel day lost | play |
| 2 | Donations 0 of 30 on a day the game ran, R2 fourth identical partial | play |
| 3 | Recovery merged twice in each batch window, same branch twice | process |
| 4 | Recovery records stack (Nov 14 to Nov 20) still conflicts with main | evidence |
| 5 | Sweep back but coverage 5 of 23 lines | perception |
| 6 | Unverified rate 91.3 percent, absolute breach (#130) | evidence |
| 7 | Perception one red dot from clean, coverage file contradicts narratives (#800) | perception |
| 8 | Day-1 retro wrong about day-2, fourth consecutive day a correction was needed | evidence |
| 9 | Recordless passes - ticker 1735, planner 0740 and 1640, knowledge-organizer 1132, catchall 1039 | loop health |
| 10 | Live/branch mirror split in both directions | evidence |
| 11 | Oldest open improvement #118 is 19 days old, owner decisions all over 48 hours | improvement |

- **Discovery counters are all data gaps.** Candidates filed 2 (#783
  Black Market, #784 Wanted Boss, RETRO C), but no conversion, dwell
  or unmatched-label series can be computed from the repository,
  and no perception day exists since the team was established.

## 3. L3 baseline - improvement of improvement

- **Archived backlog** - [improvements.md](../../_records_/retro/improvements.md)
  is FROZEN since 2026-11-01 and is an archive, not live state. Counted
  on 2026-11-22 from its `status` fields - 19 entries, 7 open, 1 in
  progress, 11 implemented, 0 closed. The section headings and the
  `status` fields disagree for four entries (three implemented entries
  sit under Open, one under In progress), so even this count is read
  from the field, not the heading. It is a stale snapshot and is
  reported only so nobody reads it as current state.
- **Live register, at the 2026-11-21 snapshot** - 172 open issues;
  oldest #118 filed 2026-11-02, 19 days old at that read; seven
  filed (#795 to #801); two closed (#608, #745); zero reopened
  (RETRO D and F). The register lives on GitHub, so its state is a
  data gap for any computation this repository can reproduce.
- **Data gaps, named** (each is a gap, not a zero) -

| Metric | Why it is a gap |
|---|---|
| Closure rate and closure dwell | the backlog that carried entry dates is frozen; the live register is not in the repository |
| Recurrence rate | RETRO D calls the Nov 18 check blind - no execution ran Nov 12 to Nov 18, so zero recurrence is not a pass |
| Learning rate, time to detect, time to fix | no dated detect or fix events are recorded in repository form |
| Research to rule conversion | one note filed 2026-11-22 19:13 (`_records_/2026-11-22/research/duel-day-loss.md`, itself `unverified`); none has yet become a verified play rule, so the ratio has no denominator |
| Tick yield, token wait, freshness | no 15-minute loop has run yet; the game is stopped at establishment |
| Discovery yield, candidate conversion, candidate dwell, unmatched labels | no perception day since establishment |
| Unexplained red dots | the 1 against 0 contradiction above (#800) |
| Points and attainment comparability | tool drift 1.5.1 against 1.5.5 (#724); attainment 0.3301 covers only 24 units and is not judged |

## 4. Three target movements for the first seven days

Window 2026-11-22 to 2026-11-29, all read on the BASELINE pool and
tool. Each movement names one source field, one threshold and the
document the threshold comes from.

| # | Movement | Baseline today | Target threshold | Threshold source |
|---|---|---|---|---|
| M1 | Unverified rate, L1 | 129 of 215, 0.600 (`totals.unverified`) | at or under 0.20, and lower than the week-earlier run | evaluation metrics, Monitoring - under 20 percent after the first full week, and never failing to fall week over week |
| M2 | Ledger coverage, L2 | 5 of 23 lines (RETRO B) | 23 of 23 lines closed on a live read every sweep day, with 20 of 23 as the acceptance floor | evaluation metrics, Monitoring - under 23 of 23, and continuous-play-team section 8 P2 |
| M3 | Closed improvements with verified movement, L3 | 2 closed at the 2026-11-21 retro, recurrence countable 0 of 0 (RETRO D) | at least 3 closed because the target metric moved or the verification passed, and recurrence 0 | continuous-play-team section 8 P3, and evaluation metrics D |

- M1 is measured by re-running the exact BASELINE command and
  comparing `totals.unverified` over `totals.executions`. The RETRO
  figure of 91.3 percent is not the M1 baseline - it is a different
  pool, and using it would manufacture a 31-point improvement that
  no repository measurement supports.
- M2 is measured from the day observation file and its coverage
  report; a day with no pass is a data gap, not a zero.
- M3 is measured from the issue register at closure time and the
  retro's own verification line, not from a merged PR.
- The thresholds are the documents' own, not negotiated here. A
  movement that misses its threshold is not called done - the retro
  re-plans it with the measured gap and one named change
  (continuous-play-team section 8), and that re-plan is this page's
  next real edit.

**Named threshold breaches carried into the baseline**, none of them
one of the three movements above -

- unexplained red dots above 0 on a perception day (1, disputed 0),
- ledger coverage under 23 of 23 (5),
- unverified rate above 20 percent (60.0 percent on the BASELINE
  pool),
- oldest open backlog entry above 7 days (19 days at the 2026-11-21
  read),
- any unit expired and unexecuted (89 expired in the BASELINE
  window).

## 5. How this page is kept

The daily retro replaces the L1 table with that day's run and appends
one row per movement to a dated series below M1 to M3, with the same
source fields. The weekly review compares the week against the
previous week and names one meta-change. A correction is a new dated
line, never an overwrite, in keeping with C1 and C2. Numbers are
regenerated, not carried forward - a figure with no run behind it in
this window is written as a data gap.
