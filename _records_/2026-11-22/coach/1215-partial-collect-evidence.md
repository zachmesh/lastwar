---
title: Barracks collects look partial - the evidence, the tests, and what it changes
created: 2026-11-24T04:25:00Z
modified: 2026-11-24T04:32:00Z
version: 1.0.0
description: Coach reading of the Lv.24 barracks batch history, 666 queued then 143 and 274 collected, which suggests a barracks collect admits what fits and leaves a remainder waiting, with the predictions registered before the data and the correction this makes to the earlier release-curve note
status: done
activity: coach
run_id: coach-2026-11-24-1215
trigger: Steer A message of 04:13Z on the open batch-size question
started_at: 2026-11-24T04:13:00Z
finished_at: 2026-11-24T04:25:00Z
duration_seconds: 720
verified: no
grounded_in:
  - source: troop-training 1229 (11-10), arms-race 1005 (11-22 10:05 PT), troop-training 0351 (11-24), growth 0030-capacity-read
  - source: 1206-capacity-release-curve.md, which this note corrects
---

# Barracks collects look partial

## The evidence [D]

The Lv.24 barracks was requeued with T8 x666 on 11-10 at 12:29 PT, finishing about 11-11 16:49 PT. Then:

| When | What | Size |
|---|---|---|
| 11-22 10:05 PT | pistol collect, +152,009 | 143 |
| 11-23 07:49Z | digits under a portrait bubble, a 6x crop, unconfirmed | about 523 |
| 11-24 03:51Z | pistol collect, +291,262 | 274 |

666 - 143 = 523, the digits read between the two collects. And 274 is exactly the room left after the 726 collect (1,000 freed - 726). The 11-22 record says Lv.24 was left idle with no requeue, so nobody queued a new batch of 274. A batch that happened to equal the free room would be a coincidence of about 0.2 percent. The simplest reading: a barracks collect admits what fits and leaves the rest waiting, so **the Lv.24 barracks probably still holds 249 T8** (523 - 274), +264,687 power, waiting for room.

## What it corrects

My release-curve note (1206) said a level adding 200 slots might release nothing until the free room reached a whole batch: a step. This evidence favours a **ramp**: each level's +200 would release 200 troops at once, 0.21M (T8) to 0.33M (T10), so the ladder's return is about 23,000 a builder-day with T8 first and 35,000 with T10, not 2,100. The Hospital is different: its collect has no selector and its toast named all 5,306 at once.

## Registered before the data

The 11-26T21:10:37Z unit (+200 room) presses **Lv.30 first, then Lv.24**, as the coordinator ordered, so the outcomes are:

| Outcome | Lv.30 press | Lv.24 press |
|---|---|---|
| A, a ramp | collects 200 (+329,400, '200 Lv. 10 units are ready') and leaves 593 | refused, room used up |
| B, all or nothing | refused (793 is over 200) | refused (249 is over 200) |
| C, mixed | refused | collects 200 (+212,600): a batch-size rule, or the Lv.30 batch not counted as finished |

Record 'Unit Count X of Y' and the power before and after. If A, my Lv.24 prediction is not exercised. Any frame before then should show digits of about 249 beside Lv.24 and, after 11:18Z, about 793 beside Lv.30. The **11:18Z tap with room 0 is not informative** (both models refuse), and the coordinator has dropped it.

## Two smaller findings

The troop-training card holds a mislabel: its 2026-11-09 entry calls Lv.27 "idle and blocked" from the toast alone, which taught the wrong rule. My precedent scan (version 0) failed its own validation on this gap and is withdrawn until it checks the unit brief, not only the card.
