---
title: The forecast-refusal flip, 2026-11-24
created: 2026-11-24T02:52:00-08:00
modified: 2026-11-24T02:52:00-08:00
level: L3
version: 0.1.0
description: The queue now refuses a unit whose serves names no plan item with a ledger row, live from 2026-11-24T10:48:40Z; the conditions, the correction of the clock, the checks and the path
status: done
activity: team-operations
run_id: team-operations-2026-11-24-1048-flip
trigger: schedule-41383442-5556-406d-8f57-c6a113f3d673 (moved from 00:05Z to 10:05Z) and schedule-207a175a-c104-4bbd-94b8-cba7da79289b (10:25Z)
started_at: 2026-11-24T02:05:00-08:00
finished_at: 2026-11-24T02:52:00-08:00
duration_seconds: 2820
verified: the live TEAM.yaml reads version 0.7.5 and coordination.queue.require_forecast true; the queue scanner reads true; queue.py validate reads pool valid; a real upkeep enqueue was accepted and a PL-99 enqueue refused with the strict-rule text
---

# The forecast-refusal flip

- Gate rule (_records_/2026-11-22/strategy/0202-forecast-gate-rule.md): refusal only when the ledger columns have been unchanged for 24 hours, every plan item PL-01 to PL-14 except PL-12 has a row, the Coach's first calibration report landed, and the Strategist announces it.
- Clock correction: my 10:05Z wake used the 09:20Z authoring time; Steer A's check at 10:05Z used the landed time of the header commit, 2026-11-23T10:22:08Z, so the 24 hours completed at 10:22:08Z. The flip waited for the Strategist's fresh line (strategy-log-1124c.md, 10:23Z).
- Change: TEAM.yaml 0.7.4 to 0.7.5, `coordination.queue.require_forecast: true` (PR 959, merge b341250ac, 10:48:40Z), prepared on a branch in a throwaway worktree, landing check exit 0, scan 0.
- Live at 10:48:59Z (the live checkout rebased on the merge; tool_sync refreshes only the tools folder, so the checkout rebase is the live step).
- Checks: Steer A's scratch probe (PL-99 refused, no serves refused, upkeep and PL-17 accepted, the override accepted, the strict rule refusing 'PL-17 the Oil Well chain'); my live check: a real upkeep enqueue accepted, PL-99 refused from a linked worktree before anything queued (a linked worktree writes into the live pool by design, so it is safe only for a refusal); the Coach's independent read: 45 inbox units all strict-valid.
- Follow-ups: the Toolsmith's counter of uses of --no-require-forecast; the Coach's standing count of units created since the flip with other wording or no serves.
