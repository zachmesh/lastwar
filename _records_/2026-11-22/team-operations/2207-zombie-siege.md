---
title: Zombie Siege time settled - 2026-11-22 22:07 PT
created: 2026-11-22T22:07:00-08:00
modified: 2026-11-22T22:09:00-08:00
level: L3
version: 0.1.0
description: The server clock is UTC-2, so Zombie Siege is 01:15Z on 2026-11-24, not 23:15 PT tonight; the coordinator's earlier assumption was wrong
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2207-zombie-siege
trigger: issue 814; planner note 2205-zombie-siege; operator To-do List read 2205
started_at: 2026-11-22T21:58:00-08:00
finished_at: 2026-11-22T22:09:00-08:00
duration_seconds: 660
verified: two live reads of Server Time against UTC stamps; the planner's three archived readings; both notes within the 500-word limit
---

# Zombie Siege time settled

## Answer

- Server time is UTC-2, exact to the second: 04:05:26 on a capture stamped 06:05:26.78Z, and 04:05:34 at 06:05:34.78Z (`_records_/2026-11-22/perception-scout/2205-queue-run.md`). The planner found the same offset in three archived readings (`_records_/2026-11-22/queue-planning/2205-zombie-siege.md`).
- The To-do List lists Zombie Siege at 23:15 server time on 2026-11-23, which is **2026-11-24T01:15Z**, 17:15 PT on 11-23, 45 minutes before the 18:00 PT reset. Nothing is due tonight.
- The same list: Alliance Train 04:08 server (06:08Z, matching the boarding banner seen at 06:01Z), Winter Battlefield 09:00 server (11:00Z), Alliance Exercise 21:00 server (23:00Z).

## The error

From issue 814 I had assumed "23:15 PT" (07:15Z) and repeated it in several messages and notes, with the label unverified. No reading supported it. The planner's note ruled it out, and a three-step read-only run confirmed it. Cost: one planner assignment and one observation run, no unit was staged on the wrong time.

## Actions

- The planner mints one read-only watch unit for 2026-11-24T01:10Z to 02:00Z, with both `not_before` and `expires_at`, and checks coverage of Alliance Exercise (23:00Z today) and Winter Battlefield (11:00Z).
- The scribe folds the offset into `_knowledge_/events-and-cycles` (a verified fact with two readings).
- The Steward posts the offset and the siege time on issue 814.
