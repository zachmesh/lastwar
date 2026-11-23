---
title: Quiet Window Margins For The Named Triggers 2830 2026-11-23
created: 2026-11-23T07:15:00-08:00
modified: 2026-11-23T10:45:00-08:00
level: L0
version: 1.3.0
description: The margin from each named trigger to the nearest cu quiet window, so no builder, lab or plunder session sits idle because of a window, with the rule for moving an action to the nearest edge
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0715-window-margins
trigger: coordinator message at 15:03Z relaying Steer A's approval of the cu windows
started_at: 2026-11-23T07:05:00-08:00
finished_at: 2026-11-23T07:15:00-08:00
verified: margins computed from the window rows in 2830-quiet-windows.csv with a script, not by eye
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2830-quiet-windows.csv
  - source: coordinator message 15:03Z
---

# Quiet window margins, 2830

The windows are provisional until the owner answers the cu coordinator: 2026-11-23 16:10Z to 16:35Z, 17:10Z to 17:25Z and 18:35Z to 18:50Z, and daily 08:00Z to 08:25Z from 2026-11-24 ([rows](2830-quiet-windows.csv)). The rule: a Complete, builder, lab or plunder session that falls inside a window moves to the nearest edge; if a node would sit finished for more than 15 minutes because of a window, the operator asks the cu coordinator, through the coordinator, for a one-line exception.

| Trigger | Time (Z) | Margin to the nearest window |
|---|---|---|
| Builders open (units 23:22Z; corrected from 09:20Z on 2026-11-24) | 2026-11-23 23:20 | 8 h 40 min before the 08:00Z start of 2026-11-24 |
| Complete lab 1, Food Output V | 2026-11-24 17:29:58 | 9 h 04 min after the 08:25Z end |
| Complete lab 2, Iron Output V, if not moved by the speed-up | 2026-11-25 02:38:53 | 5 h 21 min before the 08:00Z start |
| Donations pass 001 opens | 2026-11-23 17:44 | 19 min after the 17:25Z end, 51 min before the 18:35Z start |
| Plunder session -002 opens | 2026-11-23 18:00 | 35 min before the 18:35Z start: start by about 18:20Z or move to 18:50Z |
| Training collect opens | 2026-11-23 19:58 | 1 h 08 min after the 18:50Z end |
| Oil Output I level 1 ends, about | 2026-11-26 20:30 | 12 h 05 min after the 08:25Z end |

Reference times: the table uses the real finish times (09:20Z, 17:29:58Z); with the coordinator's triggers (09:21Z, 17:30:30Z, the Coach's reference) the margins are 56 min and 9 h 05 min. The Coach's rows QW1 to QW4 were checked against [2830-quiet-windows.csv](2830-quiet-windows.csv) and match on id, start, end, status and the daily recurrence. Oil Well chain margins (the Coach's check, trigger-window-margins.csv): level 2 opens 08:41Z, 16 minutes after the 08:25Z end, and must not be claimed earlier; level 7 opens 07:22Z on 11-26, 38 minutes before the 08:00Z start, so its Complete and next Upgrade press finish before 08:00Z or wait for 08:25Z; the other levels are hours from any window. If a level finishes earlier or later than the estimate, the new time goes to the Coach to recompute. No named trigger falls inside a window, so none is moved. The first Oil Well level finishes about 08:41Z on 2026-11-24, 16 minutes after the 08:25Z end. The Oil Well collection of 05:30Z to 09:00Z and the Oil Depot claim of 06:15Z to 09:00Z straddle the 08:00Z window and run before 08:00Z or after 08:25Z.
