---
unit: building-queues-growth-convert-2026-11-24-002
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T08:27:07Z
expires_at: 2026-11-24T10:20:00Z
planned_for:
not_before: 2026-11-24T09:22:00Z
window: convert coin, start the lowest Drill Ground and apply bounded speed-ups when the builders free
est_minutes: 15
serves: capacity source: Drill Ground lowest first (builders at 2026-11-24T09:20Z)
chain_id: growth-convert-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: Drill Ground lowest first (builders at 2026-11-24T09:20Z)

## Brief (planner, conversion-and-spend for the builders, coordinator coin plan and F1 read)

serves: capacity source: Drill Ground lowest first (builders free at 2026-11-24T09:20Z)

Second unit: act only on the builders still idle after the first unit; read the builder queue first and skip any Drill Ground already upgrading.

Rules: conversion and speed-up in `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Never touch a builder running the owner's queue. Never press Obtain, Finish Now or any purchase.

F1 read (`_records_/2026-11-22/perception-scout/0035-queue-run.md`): Drill Ground Lv.28 to 29 costs coin 119.0M (the panel, not the guide), iron 144.5M (met), prerequisite Lv.29 Headquarters (met), no food row; time 18d 09:21:34, which is 26,481 minutes; +200 slots and +30,400 building power. Re-read the panel; if it differs, the panel governs.

1. Open the builder queue (hammer icon): press COMPLETE on any finished upgrade and note the idle builders. If none is idle, read the earliest time left, write it with the UTC time and stop.
2. Count the Drill Grounds by the Building Details route, never a blind pan (one is confirmed; a second may sit at the bottom right edge). Take the lowest not already upgrading, open its Upgrade preview and read cost and time.
3. Convert exactly its coin cost by the rules: for 119.0M that is 49 UR Coin Chests (119.07M), opened by quantity if offered; if not, open at most 10, record the taps and stop. Read coin before and after, press Upgrade once, read the new timer.
4. Speed-up, bounded: after the preview showed the gain, use general speed-up items only, up to 10,000 minutes and never above (the 26,481-minute upgrade then has about 11.4 days left), never Finish Now, diamonds or money, and none if the 35,000-minute weekly budget is spent. Log the minutes and Total Power before and after.
5. Builders left idle: barracks Lv.24 to 27, then Oil Well levels 1 to 9 (food and iron only).

15 minutes, 10 steps. Never convert hero levers. Do not enqueue a chain successor.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
