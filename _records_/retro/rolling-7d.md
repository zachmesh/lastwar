---
title: Rolling 7 day metrics
created: 2026-11-01T05:30:00Z
modified: 2026-11-22T05:10:00Z
version: 1.9.0
description: Standing cross-day series beside the daily retro files, regenerated from unit results
status: complete
grounded_in:
  - source: unit results in _queue_ done
  - source: daily retro 2026-10-31 in this folder
---

# Rolling 7 day metrics

Standing series registered by task unit queue design section
14. Each entry states the pool state it was derived from,
because retro files are derived artifacts and unit results
remain the immutable source.

## Entry 2026-10-31

- Derived from - 428 done units, finished local PDT
  2026-10-28 to 2026-10-31, read 2026-11-01T05:24Z.
  Unit data covers 4 days, not 7, because the queue cut
  over on 2026-10-28. Pre-queue Oct 25 to Oct 27 records
  are not unit-comparable.
- Totals - done 219, partial 193, skipped-needs-owner 9,
  failed 7. Executor time 2,693.6 minutes, median unit
  303 seconds, 24 units over the 900 second cap.
- Worst types by done percent - survivors 0 of 22,
  training 1 of 22, trucks 5 of 25, arms-race 5 of 23,
  vip 1 of 4, zombie-invasion 8 of 66 with 65 chain
  continuation partials by design.
- Best types - star-ceremony 22 of 22, treasures 22 of
  22, train 21 of 22, help 19 of 22, mail 19 of 22.
- Measurement state - numeric target over achieved pairs
  0, units carrying blocker_category 0, units carrying
  verified 0, strict YAML failures 100 of 428. Next
  entry must report spec-key coverage first.
- Detail - daily retro 2026-10-31 in this folder.


## Entry 2026-11-01

- Derived from - 521 done units, finished local PDT
  2026-10-28 to 2026-11-01, read 2026-11-02T04:39Z
  to 05:06Z. Unit data covers 5 days, not 7,
  because the queue cut over on 2026-10-28.
  Pre-queue Oct 25 to Oct 27 records are not
  unit-comparable. Appendix pool state sha256
  f064b73e767701d2fd5002be2da589c134ed98937b1c2daea37a88e04432482c.
- Totals - done 246, partial 226, expired 20,
  failed 19, skipped-needs-owner 10. Executor time
  3,139.7 minutes, median unit 303 seconds, p90
  774 seconds, attempts mean 0.96, maximum 2.
- Nov 1 day alone - 90 units finished: done 26,
  partial 31, expired 20, failed 12,
  skipped-needs-owner 1. Unverified 71 of 90.
- Worst types by done percent - zero-sweep 0 of 2,
  survivors 1 of 29, training 1 of 27, trucks 5 of
  30, arms-race 5 of 29, vip 1 of 5, zombie-invasion
  8 of 66 with chain continuation partials by design
  (no zombie units ran after Oct 30).
- Best types - star-ceremony 25 of 27, treasures
  24 of 27, train 24 of 27, help 22 of 27, gifts
  21 of 27.
- Measurement state - numeric target over achieved
  pairs 28, summed attainment 0.1006, mean ratio
  0.4969. Nov 1 spec-key coverage: all five keys
  36 of 90 (40 percent), per-key about 50 percent,
  strict YAML failures 22 of 90 (25 percent).
  Unverified 500 of 521 rolling (96 percent).
  Sole no-data regular: duel-score (rostered,
  merged, 0 units).
- Threshold breaches - unexplained red dots 6 (5
  distinct); expired and unexecuted units 20;
  quota attainment trucks 0.2, donations 0.0923;
  unverified trajectory breach (79 percent on
  Nov 1 vs the 20 percent line for after the
  first full post-specification week, ending
  Nov 7). No breach on oldest open improvement,
  daily job artifacts, or ledger coverage.
- Batch compliance - 38 records merges audited:
  25 off-window, all pre-policy (policy 2.3.0
  merged 16:41 PST Nov 1); post-policy merges 1
  (PR #117, in-window), violations 0.
- Detail - daily retro 2026-11-01 in this folder.


## Entry 2026-11-02

- Derived from - 633 done units, finished local
  2026-10-28 to 2026-11-02, read 2026-11-03T04:41Z
  from the records/2026-11-02 branch tip b391b6f35.
  Pool state sha256
  7c4da9b62aae35b13d7879668d1c3c8d83659890c414f37c3980e9dcf2f221b6.
  Unit data covers 6 days, not 7, because the queue
  cut over on 2026-10-28.
- Totals - done 290, partial 285, skipped-needs-owner
  10, expired 26, failed 22. Executor time 3,747.1
  minutes, median unit 302 seconds, p90 767 seconds.
  Attempts mean 0.9605, maximum 2.
- Nov 2 alone - 97 finished: done 39, partial 49,
  expired 6, failed 3, skipped 0. Median 243 seconds,
  p90 689 seconds. Unverified 74 of 97 (76 percent);
  all-five stats keys 37 of 97 (38 percent).
- Worst types by done percent - duel-score 0 of 3
  (all expired), zero-sweep 0 of 4, crystal-shop 0 of
  1, glittering-market 0 of 1, survivors 1 of 34,
  training 1 of 33, arms-race 5 of 35, trucks 5 of 36.
- Best types - star-ceremony 30 of 32, train 30 of
  33, treasures 28 of 32, gifts 27 of 33, help 27 of
  33.
- Measurement state - numeric target over achieved
  pairs 77, summed attainment 0.2194, mean ratio
  0.538. Points_total 878,233 is corrupted by one
  copied duel total (791,250, issue #197) and is not
  comparable to the previous window. Blocker_category
  named in the tool vocabulary on 77 units; 312 carry
  the key with a value outside the vocabulary, 244
  lack the key. Tool parse errors 0; strict
  yaml.safe_load flags 37 of 97 Nov 2 frontmatters.
- Threshold breaches - unexplained red dots 5 at the
  last pass; expired and unexecuted units (6 reaped
  plus 16 past-expiry in inbox at snapshot); quota
  attainment under 0.8 (trucks 0.3, donations
  0.1509). Unverified rate falling week over week
  (rolling 96 to 92 percent, day 79 to 76 percent),
  but the 20 percent line for after the first full
  post-specification week, ending Nov 7, is a
  trajectory warning. No breach on oldest open
  improvement, closed-improvement recurrence (0 over
  0), daily job artifacts, or final-sweep ledger
  coverage (final sweep pending at snapshot).
- Batch compliance - 6 records merges audited, all
  inside batch windows, violations 0.
- Detail - daily retro 2026-11-02 in this folder.


## Entry 2026-11-03

- Derived from - 670 done units, finished local
  2026-10-28 to 2026-11-03, read 2026-11-04T04:40Z
  from the records/2026-11-03 branch tip a0048c5d.
  Pool state sha256
  68e5f024a3cd48b5bc331c42cf6030d760ec90d7f924d9297fc56f1ae754182d.
  First full 7-day window of unit data. Live-pool
  read the same hour: 756 units, pool state sha256
  e5f8dfcc01358962614bf1a74255e0ce236b8fcfe0239656df6566f0a90e036c;
  the 86-unit gap is issue #251, and the branch
  figures below understate Nov 3 (branch day 16
  units, live day 95).
- Totals - done 307, partial 305, skipped-needs-owner
  10, expired 26, failed 22. Executor time 3,921.0
  minutes, median unit 300.5 seconds, p90 762
  seconds. Attempts mean 0.9627, maximum 2.
- Nov 3 alone, live pool - 95 finished: done 34,
  partial 56, expired 5, skipped 0. Duration total
  29,507 seconds. Unverified 56 of 95 (59 percent);
  all-five stats keys 57 of 95 (60 percent).
- Worst types by done percent - duel-score 0 of 3
  (no Nov 3 unit in the live pool), zero-sweep 0 of
  4, crystal-shop 0 of 1, glittering-market 0 of 1,
  survivors 1 of 35, training 1 of 34, trucks 5 of
  39, arms-race 5 of 37.
- Best types - star-ceremony 31 of 34, treasures 32
  of 36, train 30 of 35, help 29 of 35, gifts 28 of
  34.
- Measurement state - numeric target over achieved
  pairs 106 branch (158 live), summed attainment
  0.2177 branch, mean ratio 0.5779. Points_total
  46,481 reconciled: 3 copied-points units excluded
  under PR 203, issue #197 closed. Blocker_category
  named in the tool vocabulary on 91 branch units;
  251 lack the key. Tool parse errors 0.
- Threshold breaches - expired and unexecuted (32
  past-expiry in branch inbox, breach on the branch
  pool, 0 parsed on the live pool); quota attainment
  under 0.8 rolling (trucks 0.3611, donations 0.28)
  with trucks day quota met verified; unverified
  day rate falling (59 percent live Nov 3) but the
  20 percent line by Nov 7 is a trajectory warning.
  No breach on unexplained red dots (0 in walked
  surfaces), oldest open improvement, closed
  improvement recurrence (#128 checked, none), or
  daily standing job artifacts. Ledger coverage is
  a data-gap (no sweep ran), not a pass or fail.
- Batch compliance - 6 records merges audited, all
  inside batch windows, violations 0.
- Detail - daily retro 2026-11-03 in this folder.


## Entry 2026-11-04

- Derived from - 642 done units, finished local
  2026-10-29 to 2026-11-04, read from the
  records/2026-11-04 branch tip 6b439ee608.
  The branch pool lags the live pool by 108 units
  (live window 750); the branch day figures below
  understate Nov 3 (branch day 20 units, live day
  110) and Nov 4 is read from the live pool.
- Totals - done 267, partial 300, skipped-needs-owner
  6, expired 34, failed 35. Executor time 3,577.6
  minutes, median unit 291 seconds, p90 714
  seconds. Attempts mean 0.9486, maximum 2.
- Nov 4 alone, live pool - 90 finished: done 21,
  partial 34, failed 17, expired 18. Unverified 58
  of 90 (64 percent). The day is a capture-channel
  outage day, not a play day: at least 16 failures
  name the Mac screen-capture failure.
- Worst types by done percent - duel-score 0 of 3
  (no Nov 4 unit in this pool), zero-sweep 0 of 6,
  crystal-shop 0 of 1, glittering-market 0 of 1,
  training 0 of 35, survivors 1 of 36, harvest 4 of
  36, radar 4 of 37, arms-race 5 of 38, trucks 5 of
  38.
- Best types - star-ceremony 28 of 32, treasures 28
  of 34, help 27 of 34, gifts 27 of 34, train 25 of
  34, passes 25 of 35.
- Measurement state - numeric target over achieved
  pairs 155 branch (210 live), summed attainment
  0.7414 branch. Points_total 40,639 reconciled:
  5 copied-points units excluded under PR 203, 2
  of them new Nov 4 (issue #296 filed for the
  executor-side source defect; issue #197 stays
  closed on its mechanism target). Blocker_category
  named in the tool vocabulary on most non-legacy
  units; 212 branch units lack the key. Tool parse
  errors 0.
- Threshold breaches - expired and unexecuted (33
  past-expiry in branch inbox, breach on the branch
  pool, 0 parsed on the live pool); quota attainment
  under 0.8 rolling (trucks 0.439, donations 0.241)
  with trucks day quota met verified for a second
  day; unverified day rate failing to fall (61
  percent live Nov 3 revised, 64 percent live Nov 4)
  with the 20 percent line by Nov 7 unmet on
  trajectory. Unexplained red dots NOT PROVEN clean
  (coverage 0 vs observation base-group 2 carried).
  No breach on oldest open improvement, closed
  improvement recurrence on the strict definition,
  or daily standing job artifacts. Ledger coverage
  is a data-gap (no sweep ran), not a pass or fail.
- Batch compliance - 5 records merges audited, all
  inside batch windows, violations 0.
- Detail - daily retro 2026-11-04 in this folder.


## Entry 2026-11-05

- Derived from - 661 done units, finished local
  2026-10-30 to 2026-11-05, read from the
  records/2026-11-05 branch tip 2258401c06.
  The branch pool lags the live pool by 70 units
  (live window 731); the branch day figures below
  understate Nov 3 (branch day 20 units, live day
  110) and overstate Nov 5 (branch day 128 units,
  live day 83), and Nov 5 is read from both pools.
- Totals - done 208, partial 246, skipped-needs-owner
  5, expired 131, failed 71. Executor time 2,949.2
  minutes, median unit 263.5 seconds, p90 660
  seconds. Attempts mean 0.8018, maximum 1.
- Nov 5 alone, branch pool - 128 finished: done 0,
  partial 0, failed 35, expired 93. Unverified 128
  of 128 (100 percent). The day is a zero-execution
  day: the Mac screen-capture channel failed in the
  morning and the Mac mini went offline from about
  07:36 local; the 2041 pass at 20:43 is the
  sixtieth consecutive failed pass. No game screen
  read, no game input dispatched, no observation
  file, no duel total, no phase read.
- Worst types by done percent - duel-score 0 of 9
  (9 expired, 0 pairs), zero-sweep 0 of 10,
  crystal-shop 0 of 2, glittering-market 0 of 2,
  training 0 of 36, survivors 1 of 37, harvest 2 of
  36, radar 4 of 37, arms-race 2 of 37, trucks 3 of
  39.
- Best types - star-ceremony 22 of 33, treasures 23
  of 37, help 23 of 34, gifts 23 of 35, train 20 of
  35, passes 20 of 37.
- Measurement state - numeric target over achieved
  pairs 178 branch (224 live), summed attainment
  0.7414 branch (achieved_sum frozen at 5,610,394 -
  Nov 5 added zero achieved). Points_total 176
  reconciled: 2 copied-points units excluded under
  PR 203, 0 no-achieved-points units excluded under
  PR 326 (issues #300 and #316 closed this run on
  that evidence; issue #296 stays open, radar half
  reclassified by PR 298). Blocker_category named
  in the tool vocabulary on most non-legacy units;
  154 branch units lack the key. Tool parse errors 0.
- Threshold breaches - unexplained red dots NOT
  PROVEN clean (no Nov 5 observation file at all);
  expired and unexecuted in day counts (93 branch,
  58 live on Nov 5) with the inbox half clear (0
  past-expiry both pools); quota attainment under
  0.8 rolling (trucks 0.439, donations 0.1492) with
  no Nov 5 day outcome; unverified day rate 100
  percent both pools, rolling 85.9 percent branch,
  with the 20 percent line by Nov 7 unmet on
  trajectory; daily standing job artifact missing
  in part (ticker-0634 has no record anywhere,
  filed as issue #342; Nov 5 observation file
  missing). No breach on oldest open improvement
  (#118, 3 days) or closed improvement recurrence
  on the strict definition. Ledger coverage is
  a data-gap (no sweep ran), not a pass or fail.
- Batch compliance - 5 records merges audited, all
  inside batch windows, violations 0.
- Detail - daily retro 2026-11-05 in this folder.


## Entry 2026-11-06

- Derived from - 657 done units, finished local PDT
  2026-10-31 to 2026-11-06, read from the
  records/2026-11-06 branch tip 58ef10a9ef
  (knowledge-organization 2032 run), tool
  _tools_/retro_report.py 1.5.0, pool state sha256
  b247529bfe522e7951e51dc1f7fc29505b4a5789baf71980bd78cdf71e1baea2.
  Live working-tree pool holds 718 in the same
  window (pool sha256
  ba31ce09595506af5c46ec4fb61f45ede1f2c1747c788c613775876277d7ec70);
  gap 61, pool_gap.py FAIL. Nov 3 backfill deficit
  still 90; live tree stale for Nov 6 by 18.
- Totals - done 147, partial 192, failed 100,
  expired 214, skipped-needs-owner 4. Executor
  time 137,345 seconds, median unit 254 seconds,
  p90 614 seconds. Attempts mean 0.6743, max 1.
- Worst types by done percent - training 0 of 36,
  crystal-shop 0 of 2, glittering-market 0 of 2,
  zero-sweep 0 of 12, duel-score 0 of 13, arms-race
  1 of 37, survivors 1 of 38, harvest 2 of 37.
- Best types - gifts 18 of 35, help 17 of 34,
  treasures 17 of 37, star-ceremony 16 of 33,
  passes 16 of 37, events 14 of 35, train 14 of
  35, mail 14 of 34.
- Measurement state - numeric target over achieved
  pairs 206, summed attainment 0.7414, frozen
  (achieved_sum 5,610,394 identical to yesterday);
  units carrying blocker_category 558 of 657 (99
  lack the key); unverified closings 564 (85.8
  percent), flat against yesterday's 85.9 percent.
  Points 176, identical to yesterday; the tool
  excludes the same 2 copied-points units.
- Threshold breaches - unexplained red dots not
  proven clean (second blackout day, no
  observation); expired/unexecuted in day counts
  (78 branch, 67 live); quota attainment under
  0.8 rolling (trucks 0.439, donations 0.1351);
  unverified rate failing to fall (flat); closed
  improvement recurrence BREACH (#149 and #251
  prematurely closed by non-retro actors,
  reopened this run; recurrence 2 of 5); daily
  standing job artifact missing (ticker-0634
  record, #342); ledger coverage unmeasurable
  (no sweep). Oldest open improvement 4 days,
  no breach.
- Detail - daily retro 2026-11-06 in this folder.


## Entry 2026-11-07

- Derived from - 688 done units, finished local PST
  2026-11-01 to 2026-11-07, read from the
  records/2026-11-07 branch tip b8cf68e000
  (pr-integration 2011 run), tool
  _tools_/retro_report.py 1.5.0, pool state sha256
  a971973417c4dad91468c1692844878aec3a9b24fcc06903c5eac6a5090dbf08.
  Live working-tree pool holds 746 in the same
  window (pool sha256
  a58ae379a9979ff41f40eeaaf8fd055844ebcd1f0330243823966bd3d13fe6b1);
  gap 58, pool_gap.py FAIL. Nov 3 backfill deficit
  still 88; branch leads the live tree Nov 5-7 by
  36, 17 and 2.
- Totals - done 114, partial 162, failed 122,
  expired 288, skipped-needs-owner 2. Executor
  time 115,637 seconds, median unit 232.5 seconds,
  p90 592 seconds. Attempts mean 0.5814, max 1.
- Worst types by done percent - arms-race 0 of 37,
  crystal-shop 0 of 3, glittering-market 0 of 3,
  zero-sweep 0 of 16, duel-score 0 of 17, training
  0 of 37, survivors 1 of 39, harvest 1 of 37.
- Best types - gifts 15 of 36, help 14 of 35,
  passes 14 of 38, events 11 of 36, mail 11 of 35,
  treasures 11 of 37, star-ceremony 11 of 34,
  train 9 of 36.
- Measurement state - numeric target over achieved
  pairs 247, summed attainment 0.7377
  (achieved_sum 5,604,421, target_sum 7,597,211);
  units carrying blocker_category 637 of 688 (51
  lack the key); unverified closings 582 (84.6
  percent), down 1.2 points on yesterday's 85.8
  percent. Points 187, up 11 on yesterday; the
  tool excludes the same 2 copied-points units.
- Threshold breaches - unexplained red dots not
  proven clean (third blackout day, no
  observation); expired/unexecuted in day counts
  (62 branch, 64 live); quota attainment under
  0.8 rolling (trucks 0.439, donations 0.1184);
  unverified rate over 20 percent at the end of
  the first full post-specification week (84.6
  percent); closed improvement recurrence BREACH
  (#128, #149 and #251; recurrence 3 of 6,
  corrected from the Nov 6 retro's 2 of 5, which
  missed #128); daily standing job artifact
  missing (ticker-0634 record, #342; Nov 7 scout
  observation); ledger coverage 13 of 23 (sweep
  first pass partial, final pass missed).
  Oldest open improvement 5 days, no breach.
- Detail - daily retro 2026-11-07 in this folder.


## Entry 2026-11-08

- Derived from - 731 done units, finished local PST
  2026-11-02 to 2026-11-08, read from the
  records/2026-11-08 branch tip 78e34bfa23
  (merge reconcile ticker-2004-1108-delivery),
  tool _tools_/retro_report.py 1.5.1, pool state
  sha256
  5b325b733c823666b7235a872a1c11a081726dc5a6822e4bacc483bd41f36b71.
  Live working-tree pool holds 767 in the same
  window (pool sha256
  f86da8eadd65c78e422e3aab1dc9e00cc138fa10197430af0c7f95db1cddd45e);
  gap 36, pool_gap.py FAIL. Nov 3 backfill deficit
  still 88; branch leads the live tree Nov 5, 6
  and 8 by 36, 17 and 32.
- Totals - done 101, partial 178, failed 110,
  expired 340, skipped-needs-owner 2. Executor
  time 115,384 seconds, median unit 237 seconds,
  p90 586 seconds. Attempts mean 0.5349, max 1.
- Worst types by done percent - ghost-ops 0 of 1,
  crystal-shop 0 of 2, glittering-market 0 of 3,
  daily-missions 0 of 12, zero-sweep 0 of 16,
  duel-score 0 of 23, arms-race 0 of 37, harvest
  0 of 37, training 0 of 37, survivors 0 of 38.
- Best types - mail 12 of 35, gifts 12 of 36,
  passes 12 of 38, help 11 of 35, treasures 10
  of 38, events 9 of 36, star-ceremony 7 of 34,
  secrets 7 of 37.
- Measurement state - numeric target over achieved
  pairs 266, summed attainment 1.1907
  (achieved_sum 4,813,220, target_sum 4,042,308);
  the summed figure is NOT comparable: it is
  dominated by one misattributed figure
  (star-ceremony-2026-11-04-0630 carries a duel
  screen total 4,772,100 in achieved); without
  it the window attainment is about 0.093.
  Units carrying blocker_category 696 of 731 (35
  lack the key); unverified closings 590 (80.7
  percent), down 3.9 points on yesterday's 84.6
  percent. Points 404, up 217 on yesterday; the
  tool excludes the same 1 copied-points unit.
- Threshold breaches - unexplained red dots 14
  (planner diff, unchanged across the 1340-1940
  runs); expired/unexecuted in day counts (68
  branch, 64 live); quota attainment under 0.8
  rolling (trucks 0.5556, donations 0.1372);
  unverified rate over 20 percent (80.7 percent,
  down 3.9 points week over week); daily standing
  job artifact missing (ticker-0634 record, #342,
  about 88 hours); ledger coverage 18 of 23
  (sweep pair ran both passes, fix-ups staged
  past the reset). Oldest open improvement 6
  days (#118), no breach. Recurrence of closed
  improvements' root causes 0 of 3, no breach.
- Detail - daily retro 2026-11-08 in this folder.


## Entry 2026-11-09

- Derived from - 723 done units, finished local PDT
  2026-11-03 to 2026-11-09, read 2026-11-10T05:35Z.
  Branch pool (records/2026-11-09 tip d88d542b87, re-run
  from 50935183e1 when the branch advanced mid-run);
  live pool holds 734 in the same window, gap 11.
  Nov 9 is a partial day at the re-run (101 branch).
- Totals - done 103, partial 162, skipped-needs-owner 3,
  failed 107, expired 348. Executor time 111,803 seconds
  (31.1 hours), median unit 237 seconds, p90 612 seconds.
- Best types by done percent - scout 21 of 49, gifts 10
  of 35, help 9 of 33, mail 9 of 33, passes 9 of 37,
  treasures 8 of 36, secrets 7 of 36.
- Worst types by done percent - train 0 of 34, training
  0 of 36, vip 0 of 10, zero-sweep 0 of 15, crystal-shop
  0 of 2, glittering-market 0 of 2, ghost-ops 0 of 1.
- Measurement state - numeric target over achieved
  pairs 271, summed attainment 0.5541
  (achieved_sum 8,333,047, target_sum 15,039,671);
  the summed figure is NOT comparable: it is
  dominated by one misattributed figure
  (star-ceremony-2026-11-04-0630 carries a duel
  screen total 4,772,100 in achieved); without
  it the window attainment is about 0.31, itself
  dominated by the duel-score running totals
  (3,385,000 across 2 units reading the same rising
  total). Points 50,313 reported, 2,463 honest
  (gifts progress-as-points 47,850 excluded);
  the tool excludes 1 copied-points unit
  (arms-race-2026-11-09-0203, 82,500).
  Units carrying blocker_category: e 108, h 78,
  f 36, c 28, none 27, b 6, d 4, g 3, a 1, plus
  non-enum values access-failed 1, time 1, timer 1,
  unverified-close 1. Unverified closings 529 (73.2
  percent), down 7.5 points on yesterday's 80.7
  percent.
- Threshold breaches - expired/unexecuted in day
  counts (17 branch, 28 live); quota attainment under
  0.8 rolling (donations 0.1818; trucks 0.8333 no
  longer breaches but the trade-day close is unknown
  for the third day); unverified rate over 20 percent
  (73.2 percent, down 7.5 points week over week);
  oldest open improvement over 7 days (#118, 7 days
  old - first breach); recurrence of a closed
  improvement's root cause 1 (#300, gifts
  progress-as-points); daily standing job artifact
  missing (ticker-0634 record, #342, about 110
  hours); ledger coverage 12 of 23 (sweep pair ran
  both passes, walk thinned from 18 of 23).
  Unexplained red dots 0 - NO breach, first time.
  Batch compliance clean (0 violations out of 6).
- Detail - daily retro 2026-11-09 in this folder.


## Entry 2026-11-10

- Derived from - 826 done units, finished local PDT
  2026-11-04 to 2026-11-10, read 2026-11-11T05:35Z
  (second re-run from c9eb29ccd2; first read
  2026-11-11T05:05Z from 91f5dc59eb).
  Branch pool (records/2026-11-10 tip c9eb29ccd2, re-run
  twice when the branch advanced mid-run);
  live pool holds 795 in the same window, gap 31.
  Nov 10 is a partial day at the re-run (112 branch).
- Totals - done 153, partial 197, skipped-needs-owner 5,
  failed 108, expired 363. Executor time 142,073 seconds
  (39.5 hours), median unit 243 seconds, p90 618 seconds.
- Best types by done percent - scout 21 of 49, gifts 15
  of 41, help 15 of 39, passes 14 of 42, mail 13 of 39,
  secrets 11 of 40, treasures 11 of 39.
- Worst types by done percent - training 0 of 41,
  zero-sweep 0 of 17, crystal-shop 0 of 2,
  glittering-market 0 of 2, ghost-ops 0 of 1, harvest
  1 of 41, donations 1 of 63, survivors 2 of 43,
  train 2 of 39.
- Measurement state - numeric target over achieved
  pairs 329, summed attainment 0.3042
  (achieved_sum 9,006,144, target_sum 29,603,804);
  the summed figure is NOT comparable: tool 1.5.3
  excludes the star-ceremony duel screen totals
  (4 units) that inflated the Nov 9 figure to
  0.5541, and the remaining attainment is still
  dominated by the duel-score running totals
  (1,650,000 read 4 times on the same day). Points
  403,592 reported, 3,592 honest (trucks expected
  score 400,000 excluded - a Handbook-rate product,
  never read live); the tool excludes 1
  copied-points unit (arms-race-2026-11-09-0203,
  82,500).
  Units carrying blocker_category: e 120, h 97,
  f 38, c 36, none 63, b 5, d 5, g 5, a 1, plus
  non-enum values access-failed 1, time 1,
  unverified-close 1. Unverified closings 548 (66.3
  percent), down 6.9 points on yesterday's 73.2
  percent.
- Threshold breaches - unexplained red dots 3
  (narrative accounting; diff-counted 0 is blind);
  expired/unexecuted in day counts (15 branch, 4
  live); quota attainment under 0.8 rolling
  (donations 0.2266; trucks 1.0 over 1 pair but the
  trade-day close is unknown for the fourth day);
  unverified rate over 20 percent (66.3 percent,
  down 6.9 points week over week); oldest open
  improvement over 7 days (#118, 8 days old -
  second day); recurrence of a closed improvement's
  root cause 1 (#149, perception blackout, 1 day
  after closure); daily standing job artifact
  missing (ticker-0634 record, #342, about 134
  hours; planner 1840/1940 records undelivered,
  2040 landed 20:50; the 2040 run falsely claims
  the sweep pair complete; duel-score-2026-11-10-
  1803 absent from both pools with no done record);
  ledger coverage 1 of 23 (sweep 001 ran, sweep
  002 expired unexecuted). Batch compliance 1
  violation (PR 556 merged 22:59:55, 5 seconds
  before the 2300 window). Unit cap: 12 units over
  900 seconds in the window, 4 today.
- Detail - daily retro 2026-11-10 in this folder.


## Entry 2026-11-11

- Derived from - 1629 done units, finished local
  2026-11-05 to 2026-11-11, read 2026-11-12T05:24Z
  from the records/2026-11-11 branch tip
  dbec3539c57; the live pool holds 1614 done units
  (738 in window, gap 126). Nov 11 is a partial
  day at the snapshot (116 branch, finished_at
  local; 76 by filename date, plus 2 done units
  stranded off-branch in VPS commit f279d56d5,
  #647). Nov 5 and Nov 6 carry zero done and zero
  partial units in both pools - the known outage
  days (Mac mini offline, named in the Nov 5 and
  Nov 6 retros).
- Totals - done 154, partial 225, skipped-needs-owner 6,
  failed 88, expired 391. Executor time 163,156 seconds
  (45.3 hours), median unit 274 seconds, p90 677 seconds.
- Best types by done percent - scout 21 of 52, gifts 14
  of 39, help 14 of 38, secrets 14 of 41, passes 13
  of 41, mail 12 of 38, treasures 12 of 41.
- Worst types by done percent - training 0 of 42,
  zero-sweep 0 of 17, trucks 0 of 41, crystal-shop 0
  of 2, glittering-market 0 of 2, ghost-ops 0 of 1,
  donations 1 of 73, harvest 1 of 40, survivors 2 of
  42, train 2 of 38.
- Measurement state - numeric target over achieved
  pairs 306, summed attainment 0.3067
  (achieved_sum 9,047,633, target_sum 29,498,820);
  the summed figure is NOT comparable: it is still
  dominated by the duel-score running totals
  (8,785,000 of the achieved sum). Points
  1,653,678 reported, 3,678 honest (the
  duel-score 1,650,000 running-total read in
  duel-score-2026-11-10-2230 evades the tool's
  dup-exclusion because its achieved is a
  non-numeric string; the trucks 400,000
  expected-score figure is now excluded by tool
  1.5.4). Units carrying blocker_category: h 130,
  e 123, f 21, c 36, none 78, g 6, d 5, a 2, b 2,
  plus non-enum values session-drop 1, time 1,
  unverified-close 1. Unverified closings 554
  (64.1 percent), down 2.2 points on yesterday's
  66.3 percent.
- Threshold breaches - unexplained red dots 10
  (6 distinct; diff-counted 9 only from the
  frontmatter fallback, 0 structured items parsed,
  coverage file stale at 29/9);
  expired/unexecuted in day counts (39 branch,
  50 live); quota attainment under 0.8 rolling
  (donations 0.2214; trucks carries no pair and
  its trade-day close is unknown for the fifth
  day); unverified rate over 20 percent (64.3
  percent, down 2.2 points week over week);
  oldest open improvement over 7 days (#118, 9
  days old - third day); daily standing job
  artifact missing (ticker-0634 record, #342,
  about 150 hours; Nov 10 planner 1840/1940
  records never delivered, #607 - the gap is now
  permanent; Nov 11 planner 2040 record not landed
  at snapshot (pending); duel-score-2026-11-10-1803
  lost;
  stranded delivery #647 leaves 2 done units
  invisible to the branch); ledger coverage 6 of
  23 (sweep 001 ran 1 of 23, sweep 002 ran 5 of
  23, seq-2 expires_at still 18:00 despite PR
  #614); batch compliance 1 violation (PR 636
  merged 11:07:03, second records merge in the
  11:00 window after PR 615 at 11:06:27). Unit
  cap: 13 units over 900 seconds in the window,
  3 today. No new closed-improvement recurrence
  this run (#149 is open, so its continuation is
  not a new recurrence event).
- Detail - daily retro 2026-11-11 in this folder.


## Entry 2026-11-12

- Derived from - 1718 done units, finished local
  2026-11-06 to 2026-11-12, read 2026-11-13T05:00Z
  from the records/2026-11-12 branch tip
  2f59c27047; the live working-tree pool holds 765
  in window (gap 54, comparison degraded - the
  live tree is not the live pool, see the Nov 12
  retro). Nov 12 is a partial day at the snapshot
  (64 branch, finished_at local; 2 partials and 10
  failed by filename date, all 10 failed on the
  control-channel lock). Nov 6 and Nov 12 carry
  zero done in both pools - the dead days (Mac
  offline Nov 6; control-channel lock, then Mac
  offline, then the loop dark Nov 12).
- Totals - done 155, partial 233, skipped-needs-owner 7,
  failed 60, expired 364. Executor time 164,730 seconds
  (45.8 hours), median unit 296 seconds, p90 701 seconds.
- Best types by done percent - scout 21 of 53, gifts 14
  of 37, help 14 of 37, secrets 14 of 37, passes 13
  of 38, mail 12 of 37, treasures 12 of 37.
- Worst types by done percent - training 0 of 39,
  zero-sweep 0 of 14, trucks 0 of 38, zombie-invasion 0
  of 26, crystal-shop 0 of 1, glittering-market 0 of 1,
  donations 1 of 71, harvest 1 of 38, survivors 2 of
  40, train 2 of 36.
- Measurement state - numeric target over achieved
  pairs 290, summed attainment 0.3064
  (achieved_sum 9,047,641, target_sum 29,528,635);
  the summed figure is NOT comparable: it is still
  dominated by the duel-score running totals
  (about 8,785,000 of the achieved sum). Points
  3,608 reported, 3,608 honest (tool 1.5.5's sixth
  exception now excludes the duel-score 1,650,000
  running total and the daily-missions string
  achieved naming the same total). Units carrying
  blocker_category: h 136, e 94, none 78, c 37,
  f 22, g 7, d 5, a 2, b 2, plus non-enum values
  session-drop 1, time 1, unverified-close 1.
  Unverified closings 499 (60.9 percent), down 3.2
  points on yesterday's 64.1 percent.
- Threshold breaches - unexplained red dots 11
  (Nov 11 observation final state; no Nov 12
  observation exists, diff-counted 9 only from
  the stale frontmatter fallback, 0 structured
  items parsed); recurrence of a closed
  improvement's root cause (#631's stale-copy root
  cause recurred within 1 day of closure - the
  0941/1200 stale-tool handouts burned zombie 027
  and scout 009 during the R9 pause; #631 reopen
  attempted, blocked by the GitHub App 403, #694
  the active tracker);
  expired/unexecuted in day counts (52 branch,
  97 live); quota attainment under 0.8 rolling
  (donations 0.2871; trucks carries no pair and
  its trade-day close is unknown for the sixth
  day); unverified rate over 20 percent (60.9
  percent, down 3.2 points week over week);
  oldest open improvement over 7 days (#118, 10
  days old - fourth day); daily standing job
  artifact missing (the loop went dark about
  12:46 PT - no ticker, planner, KO, TD or
  integrator records after 12:30-12:46, no 15:00
  or 19:00 batch merge, PR #708 unmerged; new
  priority-1 issue DRAFTED, filing blocked by
  the GitHub App 403 (full text in the retro);
  #342, about 170 hours; Nov 12 planner
  0740/0840/0940/1040 records never delivered,
  #607; duel-score-2026-11-10-1803 lost;
  stranded delivery #647 leaves 2 done units
  invisible to the branch); ledger coverage 0 of
  23 (neither sweep ran); batch compliance 0
  violations in 4 merges (but the 15:00 and 19:00
  windows saw no merge at all). Unit cap: 15 units
  over 900 seconds in the window, 1 today.
- Detail - daily retro 2026-11-12 in this folder.


## Entry 2026-11-13

- Derived from - 1702 done units, finished local
  2026-11-07 to 2026-11-13, read 2026-11-14T05:00Z
  from the records/2026-11-13 branch tip
  692c2671c8; the live pool holds done 1879 (gap 177
  - the comparison is now fork divergence, not
  delivery lag: this branch forked from main and
  dropped 19 units that live only on the unmerged
  records/2026-11-12 branch, so the window is 684
  not 703). Nov 13 is 3 failed units and nothing
  else (second consecutive zero day). Nov 6, Nov 12
  and Nov 13 are the dead days of this window.
- Totals - done 155, partial 233, skipped-needs-owner 7,
  failed 33, expired 256. Executor time 159,816 seconds
  (44.4 hours), median unit 313 seconds, p90 732 seconds.
- Best types by done percent - secrets 14 of 30, gifts 14
  of 29, help 14 of 29, passes 13 of 31, mail 12 of 29,
  treasures 12 of 30, scout 21 of 51.
- Worst types by done percent - training 0 of 31,
  zero-sweep 0 of 11, trucks 0 of 31, zombie-invasion 0
  of 28, crystal-shop 0 of 1, glittering-market 0 of 1,
  donations 1 of 64, harvest 1 of 29, survivors 2 of
  32, train 2 of 28.
- Measurement state - numeric target over achieved
  pairs 261, summed attainment 0.3064
  (achieved_sum 9,047,641, target_sum 29,528,606);
  the summed figure is NOT comparable: it is still
  dominated by the duel-score running totals
  (about 8,785,000 of the achieved sum). Points
  3,608, unchanged from yesterday - nothing scored
  Nov 13. Unverified closings 364 (53.2 percent),
  down 7.7 points on yesterday's 60.9 percent -
  partly the fork loss (19 mostly-unverified units
  left the window), not a verified improvement.
  Blocker_category: h 136, e 65, none 78, c 37,
  f 23, g 7, d 5, a 2, b 2, plus non-enum values
  session-drop 1, time 1, unverified-close 1.
- Threshold breaches - unexplained red dots 11
  (Nov 11 observation final state; no Nov 12 or Nov
  13 observation exists); recurrence of a closed
  improvement's root cause (#631's stale-copy root
  cause recurred in attempt at ticker-1933, caught
  before burn); expired/unexecuted (branch inbox 71,
  69 older than 24 hours, oldest vip-2026-11-11-1800
  53.9 hours old); quota attainment under 0.8
  (donations 0.2894; trucks no pair, seventh day
  unknown); unverified rate over 20 percent (53.2
  percent, down 7.7 points week over week);
  oldest open improvement over 7 days (#118, 11
  days old - fifth day); daily standing job
  artifact missing (loop partitioned - 0 merges in
  all 6 windows Nov 13, PR #708 unmerged, 8th batch
  point missed; tool developer silent all day; #342,
  about 206 hours; #647 still stranded; the Nov 13
  records branch exists only locally); ledger
  coverage 0 of 23 (staged sweep pair expired
  unexecuted 18:13 PT, thirteenth consecutive day
  without a completed sweep); batch compliance 0
  violations in 0 merges (all 6 windows empty).
  Unit cap: 15 units over 900 seconds in the window,
  0 today.
- Detail - daily retro 2026-11-13 in this folder.

## Entry 2026-11-14

- Derived from - 1743 done units scanned, finished local
  2026-11-08 to 2026-11-14, read 2026-11-15T05:00Z
  from the records/2026-11-14 branch tip
  367158de20; the live pool holds done 2026 (gap 283
  - the comparison is now fork divergence, not
  delivery lag: this branch forked from main and
  dropped 5 Nov 13 units that live only on the
  unmerged records/2026-11-13 branch, plus the 19
  Nov 12 units still missing, so the window is 613
  not 642). Nov 14 is 12 failed units and 32 expired
  units and nothing else (third dead day of this
  window, but the first with live game access since
  Nov 12). Nov 8 to Nov 11 alone runs 524 executions
  with 148 done (28.2 percent).
- Totals - done 148, partial 214, skipped-needs-owner 6,
  failed 23, expired 222. Executor time 148,881 seconds
  (41.4 hours), median unit 329 seconds, p90 739 seconds.
- Best types by done percent - help 13 of 23, secrets 14
  of 26, gifts 12 of 24, passes 12 of 27, treasures 12
  of 26, scout 21 of 55, mail 10 of 24.
- Worst types by done percent - training 0 of 26,
  zero-sweep 0 of 11, trucks 0 of 28, zombie-invasion 0
  of 32, donations 1 of 59, harvest 1 of 26, survivors 2
  of 27, train 2 of 23.
- Measurement state - numeric target over achieved
  pairs 216, summed attainment 0.307
  (achieved_sum 9,047,615, target_sum 29,468,493); the summed figure is NOT comparable: it is
  still dominated by the duel-score running totals
  (about 8,785,000 of the achieved sum). Points
  3,608, unchanged from yesterday - nothing scored
  Nov 14. Unverified closings 311 (50.7 percent),
  down 2.5 points on yesterday's 53.2 percent -
  partly the fork loss (3 Nov 13 units, all
  unverified, left the window), not a verified
  improvement. Blocker_category: h 128, e 44, none 73,
  c 34, f 30, g 6, d 3, a 2, b 1, plus non-enum values
  session-drop 1, time 1, unverified-close 1.
- Threshold breaches - unexplained red dots 11
  (Nov 11 observation final state; no Nov 12, Nov 13
  or Nov 14 observation exists); no NEW recurrence
  of a closed improvement's root cause (the Nov 13
  #631 recurrence stands unrepaired, reopen still
  blocked); expired/unexecuted (branch inbox 77,
  70 older than 24 hours, oldest 86.3 hours old);
  quota attainment under 0.8 (donations 0.3007;
  trucks no pair, eighth day unknown); unverified
  rate over 20 percent (50.7 percent, down 2.5 points
  week over week); oldest open improvement over 7
  days (#118, 12 days old, sixth day); daily standing
  job artifact missing (0 merges, PR #708 at its
  14th missed batch point, no remote records/2026-11-13
  or records/2026-11-14 branch, no ticker record
  after 18:35 PT); ledger coverage 0 of 23
  (fourteenth consecutive day without a completed
  sweep); unit cap (14 units over 900 seconds in the
  window, 0 today).
- Detail - daily retro 2026-11-14 in this folder.
## Entry 2026-11-15

Note - entries for 2026-11-01 to 2026-11-11 live on main;
this mirror copy jumps from Oct 31 to this entry because
no retro ran Nov 12 to Nov 14 and the branch route is
down. The Nov 1 to Nov 11 entries are not reproduced
here; the delivery at VPS recovery reconciles them.

- Derived from - 831 done units in window, finished local
  PST 2026-11-09 to 2026-11-15, live pool only, read with
  tools/retro_report.py 1.5.1 (main carries 1.5.4).
  Pool state sha256 e6c8aa1885fcb478ccb3f7c52df1a5df3692de4cf69a73c0b1396ddb0e414879.
- Totals - done 91, partial 113, failed 38, expired 585,
  skipped-needs-owner 4. Executor time 93,849 seconds,
  median unit 318 seconds, p90 748 seconds, 9 units over
  the 900 second cap (worst 1,388s).
- Per-day done - Nov 9: 30, Nov 10: 42, Nov 11: 19,
  Nov 12 to Nov 15: 0. Four consecutive zero-execution
  days; last done unit finished Nov 11.
- Worst types by done percent - training 0 of 35,
  trucks 0 of 40, zero-sweep 0 of 21, zombie-invasion
  0 of 30, arms-race 1 of 34, donations 1 of 48,
  survivors 1 of 36, harvest 1 of 35, building-queues
  1 of 30. All dragged by the outage, not by play.
- Best types - scout 10 of 32, secrets 11 of 39,
  treasures 10 of 39, help 8 of 37, passes 8 of 40,
  all on Nov 9 to Nov 11 executions.
- Measurement state - attainment summed 0.2969 over 119
  units; unverified closings 661 of 831 (79.5 percent,
  up from 64.1 percent); points reported 2,139,000,
  honest 3,500 on the 1.5.4 exclusion basis; unexplained
  red dots 11 (Nov 11 observation, 4 days stale);
  ledger coverage 0 of 23; missed batches 20.
- Detail - daily retro 2026-11-15 in this folder.


## Entry 2026-11-16

- Derived from - 846 done units in window, finished local
  PST 2026-11-10 to 2026-11-16, live pool only, read with
  tools/retro_report.py 1.5.1 (main carries 1.5.4).
  Pool state sha256 054c0b2b58e128f0f11b32844782d51fae432e21fec23a18018b966fb8d87ac1.
  Per-day counts are a regex recount summing exactly to
  the tool's 846 (the YAML-based recount is retired: it
  silently drops about 10 percent of units).
- Totals - done 59, partial 81, failed 66, expired 636,
  skipped-needs-owner 4. Executor time 70,368 seconds,
  median unit 269 seconds, p90 684 seconds, 5 units over
  the 900 second cap (worst 1,388s, all Nov 10-11).
- Per-day done - Nov 10: 40, Nov 11: 19, Nov 12 to
  Nov 16: 0. Five consecutive zero-execution days; last
  done unit finished Nov 11. Duel day 1 Radar Training
  RELEASE lost whole (window closed 18:00 PT Nov 16).
- Worst types by done percent - harvest 0 of 38,
  survivors 0 of 36, training 0 of 36, trucks 0 of 42,
  zero-sweep 0 of 21, zombie-invasion 0 of 30, scout
  0 of 22, building-queues 1 of 31, donations 1 of 49.
  All dragged by the outage, not by play.
- Best types - secrets 8 of 40, passes 7 of 42,
  treasures 7 of 40, help 5 of 38, all on Nov 10-11
  executions.
- Measurement state - attainment summed 0.3481 over 77
  units; unverified closings 710 of 846 (83.9 percent,
  up from 79.5 percent); points reported 2,071,000,
  honest 1,280 on the 1.5.4 exclusion basis; unexplained
  red dots 11 (Nov 11 observation, 5 days stale);
  ledger coverage 0 of 23 (third missed sweep night);
  missed batches 26.
- Detail - daily retro 2026-11-16 in this folder.


## Entry 2026-11-17

- Derived from - 863 done units in window, finished local
  PST 2026-11-11 to 2026-11-17, live pool only, read with
  tools/retro_report.py 1.5.1 (main carries 1.5.4).
  Pool state sha256 6d134ddf716f08943a640c6cc93ed30ac784150a12aab24ead96a0b14c6cc318.
  Per-day counts are a regex recount summing exactly to
  the tool's 863 (the YAML-based recount is retired: it
  silently drops about 10 percent of units).
- Correction to Entry 2026-11-16 - Nov 16 was NOT a dead
  day. Its snapshot predated the Mac's 22:36 PT return;
  Nov 16 closed with 1 done and 5 partials, not 0 done.
  Corrected Nov 10-16 window: 863 executions, done 60,
  partial 86, failed 66, expired 647, skipped 4,
  unverified about 83.7 percent by regex recount. The
  zero-done run was Nov 12 to Nov 15, four days.
- Totals - done 22, partial 51, failed 83, expired 705,
  skipped-needs-owner 2. Executor time 51,989 seconds,
  median unit 275.5 seconds, p90 670 seconds, 3 units over
  the 900 second cap (worst 1,388s, all Nov 11-12).
- Per-day done - Nov 11: 19, Nov 12 to Nov 15: 0,
  Nov 16: 1 (late evening), Nov 17: 2 (before 02:30 PT).
  Last done unit finished Nov 17 02:25 PT
  (gifts-2026-11-16-2230). Mac online since Nov 16
  22:36 PT, but the game window was lost Nov 17 03:33 PT
  - thirty consecutive window-loss occurrences by
  ticker-2034. Duel day 2 Base Expansion lost whole
  (ended 18:00 PT Nov 17); duel day 3 Age of Science
  (radar RELEASE) runs to 18:00 PT Nov 18, blocked.
- Worst types by done percent - harvest 0 of 40,
  survivors 0 of 39, training 0 of 38, trucks 0 of 43,
  zero-sweep 0 of 21, zombie-invasion 0 of 28, scout
  0 of 22, building-queues 0 of 30, donations 0 of 46.
  All dragged by the outage, not by play.
- Best types - radar 4 of 41, secrets 3 of 40, gifts
  2 of 43, help 2 of 40, passes 2 of 43, all on Nov 11,
  Nov 16 late or Nov 17 early executions.
- Measurement state - attainment summed 0.0095 over 32
  units; unverified closings 778 of 863 (90.2 percent,
  up from about 83.7 percent corrected); points reported
  1,669,860, honest 140 on the 1.5.4 exclusion basis;
  unexplained red dots 11 (Nov 11 observation, 6 days
  stale); ledger coverage 0 of 23 (fourth missed sweep
  night); missed batches 32.
- Detail - daily retro 2026-11-17 in this folder.


## Entry 2026-11-18

- Derived from - 2474 done units, finished local PST
  2026-11-12 to 2026-11-18, read 2026-11-19T04:40Z.
  Tool retro_report.py 1.5.1 from the live tree (main
  carries 1.5.4); pool state sha256
  41fb394eb4998842a09048fdae64681becd1c8b2e3909aa4227f0fbff96a372c.
  CORRECTED by the Nov 19 retro (recomputed with the
  same tool over the current pool into /tmp, appendix
  not overwritten): 2580 done units, 853 executions,
  pool state sha256
  3250219fdf8976c703680bbd637ad3602219e345f13b3860dd78f445cf858b12.
- Totals - done 3, partial 6, failed 94, expired 735,
  skipped 0, out of 838 executions. Executor time
  435.3 minutes, median unit 228 seconds, p90 439
  seconds, 1 unit over the 900 second cap (zombie
  963s). Points 0; attainment summed 0.9533 over 13
  units (mean ratio 0.1538); unverified closings 797
  of 838 (95.1 percent). CORRECTED: done 3, partial 6,
  failed 95, expired 749, skipped 0, out of 853
  executions; executor time 436.5 minutes, median
  227.5 seconds, p90 439 seconds; unverified closings
  812 of 853 (95.2 percent).
- Per-day - Nov 12 124, Nov 13 140, Nov 14 145,
  Nov 15 121, Nov 16 108, Nov 17 108 (CORRECTED from
  the Nov 17 retro's 94 - fourteen units landed after
  its snapshot), Nov 18 92. Last done unit Nov 17
  02:25 PT; zero executions Nov 18. CORRECTED: Nov 18
  107 (expired 97, failed 10) - fifteen units landed
  after the Nov 18 retro's snapshot.
- Worst types by done percent - arms-race 0 of 39,
  building-queues 0 of 24, daily-missions 0 of 10,
  donations 0 of 42, duel-score 0 of 44, events 0 of
  40, harvest 0 of 42, help 0 of 40, mail 0 of 44,
  passes 0 of 43, research 0 of 24, scout 0 of 19,
  secrets 0 of 40, star-ceremony 0 of 44, survivors
  0 of 39, train 0 of 44, training 0 of 39,
  treasures 0 of 40, trucks 0 of 43, vip 0 of 10,
  zero-sweep 0 of 21, zombie-invasion 0 of 14. All
  dragged by the outage, not by play.
- Best types - radar 2 of 42, gifts 1 of 44, both on
  Nov 16 late or Nov 17 early executions.
- Measurement state - attainment summed 0.9533 over
  13 units (window-mix artifact, not improvement);
  unverified closings 797 of 838 (95.1 percent, up
  from 90.2 percent); points 0; unexplained red dots
  11 (Nov 11 observation, 7 days stale); ledger
  coverage 0 of 23 (fifth missed sweep night); missed
  batches 38; R2 fifty-third evidenced occurrence.
  CORRECTED: unverified 812 of 853 (95.2 percent);
  missed batches 38 stands; R2 fifty-third was the
  ticker-1912 reading - the count is now seventy-
  seventh by chain arithmetic.
- Detail - daily retro 2026-11-18 in this folder.


## Entry 2026-11-19

- Derived from - 2580 done units, finished local PST
  2026-11-13 to 2026-11-19, read 2026-11-20T04:40Z.
  Tool retro_report.py 1.5.1 from the live tree (main
  carries 1.5.4); pool state sha256
  3250219fdf8976c703680bbd637ad3602219e345f13b3860dd78f445cf858b12.
- Totals - done 3, partial 5, failed 97, expired 715,
  skipped 0, out of 820 executions. Executor time
  445.9 minutes, median unit 232 seconds, p90 446
  seconds, 0 units over the 900 second cap. Points 0;
  attainment summed 0.9608 over 12 units (mean ratio
  0.1667); unverified closings 775 of 820 (94.5
  percent).
- Per-day - Nov 13 140, Nov 14 145, Nov 15 121,
  Nov 16 108, Nov 17 108, Nov 18 107 (CORRECTED from
  the Nov 18 retro's 92 - fifteen units landed after
  its snapshot), Nov 19 91 at snapshot. Last done unit
  Nov 17 02:25 PT; zero executions Nov 19, third
  consecutive zero-execution day.
- Worst types by done percent - arms-race 0 of 41,
  building-queues 0 of 18, daily-missions 0 of 9,
  donations 0 of 43, duel-score 0 of 43, events 0 of
  41, harvest 0 of 42, help 0 of 41, mail 0 of 43,
  passes 0 of 43, research 0 of 18, scout 0 of 15,
  secrets 0 of 41, star-ceremony 0 of 43, survivors
  0 of 41, train 0 of 43, training 0 of 41,
  treasures 0 of 41, trucks 0 of 43, vip 0 of 9,
  zero-sweep 0 of 18, zombie-invasion 0 of 10. All
  dragged by the outage, not by play.
- Best types - radar 2 of 42, gifts 1 of 43, both on
  Nov 16 late or Nov 17 early executions.
- Measurement state - attainment summed 0.9608 over
  12 units (window-mix artifact, not improvement);
  unverified closings 775 of 820 (94.5 percent, down
  from 95.2 percent corrected); points 0; unexplained
  red dots 11 (Nov 11 observation, 8 days stale);
  ledger coverage 0 of 23 (sixth missed sweep night);
  missed batches 42 plus 2 due-but-unexecuted; R2
  seventy-seventh evidenced occurrence.
- Detail - daily retro 2026-11-19 in this folder.


## Entry 2026-11-20

- Derived from - 2689 done units, finished local PST
  2026-11-14 to 2026-11-20, read 2026-11-21T04:41Z.
  Tool retro_report.py 1.5.1 from the live tree (main
  carries 1.5.4); pool state sha256
  935dc6522019195c234a0e016ce5a70a3dcc9fdbe8680d224ce1ef93f09c36ce.
- Totals - done 3, partial 5, failed 94, expired 687,
  skipped 0, out of 789 executions. Executor time
  434.7 minutes, median unit 231 seconds, p90 446
  seconds, 0 units over the 900 second cap. Points 0;
  attainment summed 0.9608 over 12 units (mean ratio
  0.1667); unverified closings 743 of 789 (94.2
  percent).
- Per-day - Nov 14 145, Nov 15 121, Nov 16 108,
  Nov 17 108, Nov 18 107, Nov 19 108 (CORRECTED from
  the Nov 19 retro's 91 - seventeen units landed after
  its snapshot), Nov 20 92 at snapshot. Last done unit
  Nov 17 02:25 PT; zero executions Nov 20, fourth
  consecutive zero-execution day.
- Worst types by done percent - arms-race 0 of 41,
  building-queues 0 of 12, daily-missions 0 of 8,
  donations 0 of 42, duel-score 0 of 42, events 0 of
  41, harvest 0 of 41, help 0 of 41, mail 0 of 42,
  passes 0 of 42, research 0 of 12, scout 0 of 14,
  secrets 0 of 41, star-ceremony 0 of 42, survivors
  0 of 41, train 0 of 42, training 0 of 41,
  treasures 0 of 41, trucks 0 of 42, vip 0 of 8,
  zero-sweep 0 of 16, zombie-invasion 0 of 6. All
  dragged by the outage, not by play.
- Best types - radar 2 of 41, gifts 1 of 42, both on
  Nov 16 late or Nov 17 early executions.
- Measurement state - attainment summed 0.9608 over
  12 units (identical units to the prior window, not
  improvement); unverified closings 743 of 789 (94.2
  percent, down from 94.5 percent recomputed);
  points 0; unexplained red dots 11 (Nov 11
  observation, 9 days stale); ledger coverage 0 of
  23 (seventh missed sweep night); missed batches 42
  plus 8 due-but-unexecuted; Mac offline since
  ticker-2157 Nov 19, nineteenth device-offline
  occurrence at ticker-1930.
- Detail - daily retro 2026-11-20 in this folder.


## Entry 2026-11-21

- Derived from - 2800 done units, finished local PST
  2026-11-15 to 2026-11-21, read 2026-11-22T05:10Z
  (tool run 20:41 PT Nov 21). Tool retro_report.py
  1.5.1 from the live tree (main carries 1.5.5);
  pool state sha256
  1ba02827a78411c590d6a0a2bd452c66d778282db9890178d79899b96f74ef28.
  Live-pool figures; the branch pool holds 3 more
  Nov 21 partial units (donations, survivors,
  training ticker-1318) the live pool lacks.
- Totals - done 9, partial 14, failed 90, expired 642,
  skipped 0, out of 755 executions. Executor time
  510.9 minutes, median unit 256 seconds, p90 451
  seconds, 0 units over the 900 second cap (cap
  tested by live Nov 21 play, max 651 seconds).
  Points 0; attainment summed 0.9608 over 12 units
  (identical units to the prior window, not
  improvement); unverified closings 689 of 755 (91.3
  percent).
- Per-day - Nov 15 121, Nov 16 108, Nov 17 108,
  Nov 18 107, Nov 19 108, Nov 20 104 (CORRECTED from
  the Nov 20 retro's 92 - twelve units landed after
  its snapshot), Nov 21 99. Last done unit before
  recovery Nov 17 02:25 PT; first recovery done
  Nov 21 14:47 PT (passes). Duel day 6 Enemy Buster
  lost whole (fifth consecutive duel day lost); VIP
  chain ended at 8 (claimed Nov 21); first pre-reset
  sweep in eight nights, partial (5 of 23 lines).
- Worst types by done percent - arms-race 0 of 41,
  building-queues 0 of 8, donations 0 of 40,
  duel-score 0 of 41, events 0 of 41, harvest 0 of 40,
  help 0 of 41, research 0 of 8, scout 0 of 13,
  star-ceremony 0 of 41, train 0 of 41, training 0 of
  40, treasures 0 of 41, trucks 0 of 41, zero-sweep
  0 of 13, zombie-invasion 0 of 6. All dragged by the
  outage except the Nov 21 residue, not by play.
- Best types - vip 1 of 7, gifts 2 of 41, radar 2 of
  39, passes 2 of 41, mail 1 of 41, secrets 1 of 41,
  all on Nov 21 executions.
- Measurement state - attainment summed 0.9608 over
  12 units (window-mix artifact, not improvement);
  unverified closings 689 of 755 (91.3 percent, down
  from 94.2 percent recomputed); points 0;
  unexplained red dots 1 (new observation v1.1.0,
  down from 11 stale); ledger coverage 5 of 23 (first
  sweep in eight nights, partial); missed batches 42
  plus 12 due-but-unexecuted; 2 new batch violations
  (#795, #796); Mac back about 00:48 PT, VPS back
  about 12:18 PT; 16 merges landed on main.
- Detail - daily retro 2026-11-21 in this folder.
