---
title: Rolling 7 day metrics
created: 2026-11-01T05:30:00Z
modified: 2026-11-21T05:00:00Z
version: 1.0.0
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
