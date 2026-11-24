---
title: The flat reduction series and the builders' start against 23:20:12Z
created: 2026-11-23T23:40:00Z
modified: 2026-11-23T23:47:00Z
version: 1.0.1
description: Coach series of the three builds started tonight, each 23,520 s shorter on the builders panel than its preview, the comparison with the research flat difference of 15,120 s, the test registered before the next starts, and the builders' start against their free time
status: done
activity: coach
run_id: coach-2026-11-23-1537
trigger: coordinator urgent message of 23:34Z
started_at: 2026-11-23T23:34:00Z
finished_at: 2026-11-23T23:40:00Z
duration_seconds: 360
verified: no
grounded_in:
  - source: _records_/2026-11-22/building-queues/2320-queue-run.md and 2328-queue-run.md
  - source: coach rows for research timings, flat-reduction-series.csv
---

# The flat reduction series

Rows in [flat-reduction-series.csv](flat-reduction-series.csv). Preview effective time, minus the actual start-to-panel-end time, per build:

| Build | Preview | Actual | Difference |
|---|---|---|---|
| Lv.26 ground to 27 | 10d 02:30:19 | 9d 19:58:19 | 23,520.0 s |
| Lv.27 ground to 28 | 14d 03:30:26 | 13d 20:58:26 | 23,519.9 s |
| Oil Well Lv.20 to 21 | 09:20:18 | 02:48:18 | 23,519.6 s |
| Lv.28 ground to 29 | 18d 09:21:34 | 18d 02:49:34 | 23,520.0 s |

All four are 6 h 32 min 00 s, to within 0.4 s, on a 9 h, a 10, a 14 and an 18 day build: a flat reduction of 392 minutes, never a percentage (70 percent of the Oil Well, 2.7 percent of the 10 day ground).

**Related to the research difference?** The same shape, a different constant. The Research button minus the Finish Now clock is 15,120 s, 4 h 12 min, on both nodes I have: Iron Output V (147,000 - 131,880) and Oil Output I (205,800 - 190,680). 23,520 and 15,120 are not equal, so one bank of time does not serve both, but their ratio is 14 to 9 and both are whole multiples of 28 minutes (14 and 9): a coincidence until a third constant appears [G]. Both look like a flat grant applied when the item starts, one for construction and one for research; the source is unknown.

## Registered at 23:40Z, before the data

Next build start: panel end = start + preview effective minus 23,520 s, within 2 s. **Passed on the fourth build**, the Lv.28 ground to 29 started 23:39:45.957Z, ends 2026-12-12T02:29:20Z: 23,519.96 s, 0.04 s from the constant. Still to test: the next research start (Finish Now clock = Research button minus 15,120 s), another building type (Hut, Gold Mine, Farmland), a build shorter than 6 h 32 min (a floor), and whether the grant ends with an event.

## The builders' start against their free time: the headline

The four builders were free at 23:20:12.65Z, 23:20:16.65Z, 23:20:19.65Z and 23:20:23.65Z (1806-queue-run.md). They started after 2.09, 3.09, 9.25 and 19.37 minutes: **33.8 idle builder minutes**, 0.59 percent of a day's builder minutes (34.2 if all four are measured from the first free time). Starts: ground 001 at 23:22:18Z, ground 002 at 23:23:22Z, the Oil Well at 23:29:35Z, the Lv.28 ground at 23:39:46Z, after the food pre-conversion. None waited on the lock: the wait has been 0 since 21:25:53Z and the 21 rows since are all 0.00; the 33.8 minutes are claim and run latency. All four builders are now busy; the first to free is the Oil Well at 02:17:53Z.
