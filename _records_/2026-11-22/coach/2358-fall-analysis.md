---
title: Fall analysis - the 2026-11-09 drop, event series and collect-first rule
created: 2026-11-23T08:04:00Z
modified: 2026-11-23T08:04:00Z
version: 1.0.0
description: Coach record on the 2026-11-09 evening power drop - issues 482 and 549, the whole-troop-unit finding, the event reconstruction from collections, the candidate causes with tests, and the collect-first fixed-state rule
status: done
activity: coach
run_id: coach-2026-11-22-2358
trigger: coordinator assignments on issue 482 and the series reconstruction
started_at: 2026-11-23T07:55:00Z
finished_at: 2026-11-23T08:04:00Z
duration_seconds: 540
verified: no
grounded_in:
  - source: public issues 482 and 549 of the repository and their 18 comments, read 2026-11-23
  - source: run records listed in troop-events.csv and power-dips.csv
---

# Fall analysis

**Label.** The drop of 2,486,382 is DERIVED from two recorded readings (149,217,331 at 16:35, 146,730,949 at about 17:53) and UNVERIFIED as a fall. Issue 482 is the 641,100 step on 11-08; issue 549 tracks 11-09.

**What the records show.** 33 records fall between 16:00 and 18:45 PT: 9 with game input, 24 repository work; none a battle unit, none a relaunch. The lower level 146,736,949 was read in 7 independent records; the 17:53 value is 6,000 lower and stands alone, a digit artifact. On the confirmed level the drop is 2,480,382.

**Whole troop units.** The steps 654, 407 and 445 units times the panel-read T10 power 1,647 give exactly 2,480,382. Across the series, 8 of 29 consecutive-reading steps of 100,000 or more are exact single-tier multiples; chance predicts 0.07 ([steps](power-dips.csv)). They include drops of 365, 994, 407 (part of 11-09) and 970 units, three collections and one unattributed rise of 143. So the drops are troops leaving the power count; why is unverified.

**Event reconstruction** ([events](troop-events.csv)). From 146,751,949 on 11-09 evening to 149,218,973 on 11-10 22:09, +2,467,024 equals five recorded events exactly: T10 x793 (1,306,071), T8 x666 (707,958), Drill Ground (+21,600), T9 x313 (423,176), a hero level (+8,219). The drop was fully reversed; the level ended 1,642 above the pre-fall one. The Lv.30 batch was due 11-09 10:22 and registered 11-10 03:37, so a missing collection explains a late rise, not a drop: an uncollected batch was never counted.

**Capacity.** With the Drill Ground full (39,460 of 39,460), finished batches cannot be collected (10-31 0704). Unit power 63.51M against a full ground of 64.99M leaves 1.48M headroom; the pending Lv.27 T9 x726 (due 11-23 11:53 PT) and Lv.30 T10 x793 (due 11-24 03:13 PT) total 2.29M. Whether they register is the test.

**Candidates** ([table](candidate-causes.csv)). Hospitalized, killed, away from base, owner action on another device, building or hero change, formula change, read error, missing collection. Only the digit artifact is verified. Cheapest tests: ask the owner for the phone play at 16:35 to 17:53 PT on 11-09 and 10:10 to 10:59 PT on 11-22; read the Hospital and Drill Ground panels (wounded, outside, owned by tier) at slots A and B and after any drop of 300k or more.

**Rule.** A fixed-state read is collect first, then read, twice a day. A read taken before collecting is unfixed; the 03:55Z read of 150,080,120 is unfixed.

**Baseline.** The net pace stands; any two-point reading inside a drop is wrong by up to 4.6M. Weekly report: gain per day by category plus levers captured.
