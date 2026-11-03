---
title: Rolling 7 day metrics
created: 2026-11-01T05:30:00Z
modified: 2026-11-03T05:30:00Z
version: 1.2.0
description: Standing cross-day series beside the daily retro files, regenerated from unit results
status: complete
grounded_in:
  - source: unit results in _queue_ done
  - source: daily retro 2026-10-31 in this folder
  - source: daily retro 2026-11-01 in this folder
  - source: daily retro 2026-11-02 in this folder
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
