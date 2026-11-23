---
title: Growth charter draft v0.1 - 2026-11-22 23:40 PT
created: 2026-11-22T23:40:00-08:00
modified: 2026-11-23T08:05:00Z
level: L3
version: 0.4.0
description: Draft growth charter for Epic 867 with a default and a reason for every choice, seven questions for the owner, and a challenge to the mental model from measured numbers
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2340-growth-charter
trigger: Story 872 from the owner question relayed by Steer A at 07:40Z
started_at: 2026-11-22T23:40:00-08:00
finished_at:
duration_seconds:
verified: arithmetic from the repo's own readings (OD-20261109-02 panel, Steer A's two power readings); no state-changing game input
---

# Growth charter draft v0.1

## What the numbers say

Total Power rose 13,466 a day over 29 days (+0.26 percent). A Builders Hut upgrade gives 2,400 power per builder-day (four builders about 9,600 a day). 200M in 90 days needs 554,665 a day (41x). **Troops are the measured lever:** a 666-troop T8 batch gave +707,958 power (1,063 each) for 2.9M food and 2.9M iron in 1 day 4 hours, about 600,000 power per barracks-day, 250x a builder-day. A Lv.30 barracks trains T10: 793 per batch at +1,647 each for 5.5M food and 5.5M iron (+1,306,071, record 2026-10-31 0304); a Lv.24 one only T8.

## Why troops stalled: capacity, not resources

Training is blocked since 2026-10-31 by the toast "Drill Ground Full" (82 troop-training articles; 39,460 of 39,460); the building was "unlocated" in 8 articles; the promote arrow "did nothing" once. At 5.5M per T10 batch, stock pays for about 100 batches above the floors.

## Defaults

Objective: Total Power gain per day. Target: 200M in 90 days is not reachable on this plateau (2 to 5 percent a month is realistic); capture every lever and report gain per day by category weekly; revisit when Season 3 starts (date unknown, verify in game). Rank: power per binding constraint, from previews. Focus: Drill Ground capacity first (read-only find, then upgrade when a builder is idle and the 3x rule passes), then barracks Lv.24 to 30, troop promotion and queues, then research, heroes, other buildings. Guardrails: no diamonds, real money, speed-ups or fights; spend only what costs at most a third of each stock. **Reserves:** floors of food 100M, iron 150M, coin 10M, diamonds untouched, and the duel-day reservation; everything above the floors goes to growth. Cadence: snapshot twice a day; plan review and owner digest weekly.

## Questions for the owner (each with its default)

Q1 Is Total Power per day the objective, or do you want weights? Q2 Is 200M in 90 days a goal or an illustration? Q3 Any heroes, skills or weapons you want ahead of the troop path? Q4 Are the floors right (coin 10M is above today's 9.6M, so coin spending waits)? Q5 Digest day? Q6 Team decision threshold: decisions above one builder-day or 5 percent of a stock get a record and a digest line; below, the team decides. Q7 May troop training use stock that events need?

## Home

`_knowledge_/growth-plan/` (scribe); raw readings stay in `_records_/<date>/growth/`.

## Erratum 2026-11-23 08:05Z (measurement)

The figure 2,486,382 is **derived**, not a recorded measurement: my subtraction of two recorded readings, 149,217,331 (2026-11-09 07:45, many records) and 146,730,949 (2026-11-09 17:53, radar record 1754). The 11-10 building-queues record (`run-20261110-0112-p1`) documents "a fall of about 2.47M", flagged with no cause, three consecutive reads at the lower level. The issue 482 step is 641,100 (2026-11-08, a disconnect and relaunch). Cause **unverified**; an uncollected-troop-batch artifact is plausible and untested. Treat the 29-day change as uncertain by a few million; the fixed-state read (collect every finished batch first, then read) is mandatory.
