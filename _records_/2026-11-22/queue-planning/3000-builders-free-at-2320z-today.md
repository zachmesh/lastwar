---
title: Queue Planning The Builders Are Free At 23:20Z Today 3000 2026-11-23
created: 2026-11-23T10:35:00-08:00
modified: 2026-11-23T10:35:00-08:00
level: L0
version: 1.0.0
description: Planner correction after the four builders were measured free at 23:20Z on 2026-11-23, not 09:20Z on 2026-11-24 - every builder unit re-timed, the speed-up unit moved to the Base Expansion duel day, the oil chain moved ten hours earlier, and the open items
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1035-builders-2320z
trigger: coordinator message 18:13Z, operator record 1806
started_at: 2026-11-23T10:10:00-08:00
finished_at: 2026-11-23T10:35:00-08:00
verified: the inbox searched for the old time in windows and in text before and after; the quiet windows retested on the new windows; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/building-queues/1806-queue-run.md (as relayed by the coordinator)
---

# The builders are free at 23:20Z today, 3000

## The error

Every builder unit, my sheets and the handover carried 'builders free 2026-11-24T09:20Z'. The Training Base Lv.25 timers read 05:13:04 to 05:13:15 at 18:07:08Z and 06:29:20 to 06:29:31 at 16:51Z, both giving 23:20Z today: '09:20' is the Oil Well upgrade's duration 09:20:18, not a clock time. I carried it forward without checking it against the timers.

## Re-timed

The Oil Well chain `building-queues-oil-well-2026-11-24-001` to `-010`: `-001` opens 23:21:00Z today and expires 23:45Z; `-002` to `-010` open at the earliest possible finish of the level before, 08:41Z, 18:01Z on 11-24, 03:21Z, 12:42Z and 22:02Z on 11-25, 07:22Z and 16:43Z on 11-26, 02:03Z and 11:23Z on 11-27, each running 40 hours. The ground units: `building-queues-growth-convert-2026-11-24-001` 23:22Z to 23:50Z, `-002` 23:22Z to 00:20Z, and `-003`, the speed-ups, to 02:05Z to 06:30Z on 11-24, because the speed-ups belong on the Base Expansion duel day (Tuesday, from 02:00Z) and 23:22Z today is still Monday. The five fills: 23:10Z to 23:21Z, 23:50Z to 00:05Z, 00:05Z to 00:20Z, 00:20Z to 00:35Z, 00:35Z to 00:50Z. The builder slot read text no longer says the upgrades end at 09:20Z. The sheets 2540, 2541, 2830 and 2900 carry the correction; my older notes keep the old time as they were written and this note supersedes them. No window or expiry falls inside a quiet window.

## Open

The Strategist's B2 to B4 pick is due before 22:30Z today, since I rewrite the ground units from it. The coin conversions for the first two grounds take operator time: if they wait for unit 001 at 23:22Z the builders idle during the conversion; a conversion unit at 22:50Z to 23:20Z, once the pick is known, shortens that. The unit ids keep the date 2026-11-24 in their names.
