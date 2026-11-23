---
title: The growth partial rate - three causes and a fix each
created: 2026-11-23T16:15:00Z
modified: 2026-11-23T16:15:00Z
version: 1.0.0
description: Coach reading of the thirteen partial growth-chain units of the last 24 hours at 16:05Z, grouped into three causes by the operator's own text, each with a fix and the metric that closes it
status: done
activity: coach
run_id: coach-2026-11-23-0813
trigger: Steer A watchdog pass of 16:00Z, growth partial rate alarm
started_at: 2026-11-23T16:03:00Z
finished_at: 2026-11-23T16:15:00Z
duration_seconds: 720
verified: no
grounded_in:
  - source: _queue_/done growth-chain units finished since 2026-11-22T16:05Z, result target, achieved and follow_up lines
  - source: growth-partial-causes.csv in this folder
---

# Growth partial rate: three causes

At 16:05Z the growth chain has 24 executed units in 24 hours: 11 done, 13 partial, 54.2 percent (the watchdog read 52; the limit is 35). Steer A's letters read c tap method 11 and f missing precondition 2; the units' own text splits them three ways ([units and fixes](growth-partial-causes.csv)).

| # | Cause | Units | Share |
|---|---|---|---|
| 1 | A target not located: the run could not find the building or screen | 5 | 38% |
| 2 | An over-scoped read: several surfaces in 8 steps, only part read | 5 | 38% |
| 3 | A precondition absent, or nothing to do | 3 | 23% |

**1. Not located.** The Tech Center twice, the Builders Hut, the Decoration Gallery, the Drill Ground Expansion node, and a tent taken for the wrong building. The follow-ups say "find X" with no route. *Fix:* a locate-and-record unit for each missing building, with no reading attached; the operator records the tag text and the frame position in `growth/tag-index.csv`, which already exists, and read units start from that anchor. This is the tag-text rule doing its work.

**2. Over-scoped.** Stocks, stores, the drone centre, coin sinks and the tech trees each asked for several surfaces and stopped at the cap with the first read done. *Fix:* one surface and one question per unit, the primary target first and extras optional, done when the primary is read. The planner splits these briefs.

**3. Precondition.** The promote read needs an idle barracks with Drill Ground room; two fill units found every slot busy and closed partial. *Fix:* stage a unit after its precondition event, and let a fill unit that reads every slot and finds none idle close done, as policy 2532 does for donations.

## Projection

If the two fill units close done, partials fall from 13 to 11 (46 percent); if cause 2 is split and its primary reads land, to about 6 (25 percent, under the limit); cause 1 removes what is left. This is arithmetic on today's mix, not a forecast, and new units will fail in new ways.

## Check

Each fix has its own number: partials with a not-located text, partial rate of read units, and letter f partials, read in each daily report. An entry closes only when its metric moves.
