---
title: What a Drill Ground level releases - a step or a ramp
created: 2026-11-23T20:12:00Z
modified: 2026-11-23T20:12:00Z
version: 1.0.0
description: Coach reading of the finished troops stuck behind the full Drill Ground after the failed Lv.27 collect - the waiting pool, the arithmetic of the release curve, what is known and what is inferred, a free test, and the startable idle minutes
status: done
activity: coach
run_id: coach-2026-11-23-1206
trigger: coordinator message of 20:05Z to the Strategist, Steer A and the planner, coach copied
started_at: 2026-11-23T20:03:00Z
finished_at: 2026-11-23T20:12:00Z
duration_seconds: 540
verified: no
grounded_in:
  - source: _records_/2026-11-22/troop-training/1958-queue-run.md as relayed at 20:05Z
  - source: coach records 2400-hospital-finding.md and 2358-fall-analysis.md, and growth/0030-capacity-read.md
---

# Release curve

**The numbers agree with mine.** The finished batches are 726 x 1,352 = 981,552 and 793 x 1,647 = 1,306,071, 2,287,623 power, as the coordinator wrote; I carried 2.29M since 11-23 morning. One pool is missing from the message: the Hospital's 5,306 healed troops (5.64M to 8.74M power, tier mix unread) wait behind the same full ground. Waiting in all: 6,825 troops.

**Known [M].** The finished batch cannot be collected (19:59:22Z, both taps); the Hospital Collect has no quantity selector and its toast names all 5,306 at once, "Unable to add 5306 units"; uncollected troops add no power. **Inferred [G].** Whether a barracks batch is all or nothing: its toast says "Unable to add more units", with no number.

## Step or ramp

If a batch needs room for all of it, a level that adds 200 slots releases nothing until the free room reaches 726. From no free room that is 4 levels (726 / 200 = 3.63), then 4 more for the 793, and 27 for the Hospital's 5,306. The per-builder-day of about 32,000 is the best case, true only if a partial collect works; if it is all or nothing, the first levels return their building power alone, +21,600 over 10.1 days, about 2,100 a builder-day, until the threshold. Three builders on three grounds add 600 slots in one 10-day round if the four grounds' capacities add up, which is open. My 10-31 reading of the cap, 39,460 against a census of 40,235, may be stale after later level-ups, so how far the base is over the cap is not known.

## The free test

Before the ladder is bought, read the preview's capacity line for the free room, and after the first level completes tap Collect on the Lv.27 barracks: a partial admit shows a ramp, the same toast shows a step. Record the batch size before and after.

## For the forecast rows

Binary, the collect succeeds right after the first level: p about 0.15, tag G. Continuous, power released by the first level: low 0, high 0.33M (200 x 1,647); the range rule gives a low of 0 for a yield that may be zero.

## Idle

Over 24 hours to 20:06Z, 26.6 percent of slot-minutes are idle, and all 1,394 training minutes are blocked by capacity; startable idle is 15.9 percent, and 0 in the last 6 hours.
