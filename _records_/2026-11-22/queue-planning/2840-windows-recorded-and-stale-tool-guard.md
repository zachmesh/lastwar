---
title: Queue Planning Windows Recorded And The Stale Tool Guard 2840 2026-11-23
created: 2026-11-23T07:20:00-08:00
modified: 2026-11-23T07:20:00-08:00
level: L0
version: 1.0.0
description: Planner pass recording the four cu quiet windows as rows for the Coach, the margins of the named triggers, the Researcher's grid phase addendum in the donation passes, and the stale tool guard that stopped the one unit that needed enqueue
status: partial
activity: queue-planning
run_id: queue-planning-2026-11-23-0720-windows-and-guard
trigger: coordinator message 15:03Z, Researcher addendum 15:05Z
started_at: 2026-11-23T07:03:00-08:00
finished_at: 2026-11-23T07:20:00-08:00
verified: window rows and margins computed by script; unit word counts under 450; the guard refusal read in full; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2830-quiet-windows.csv and 2830-quiet-window-margins.md
  - source: _records_/2026-11-22/research/donation-refill-addendum.md
---

# Windows recorded and the stale tool guard, 2840

## Done

[2830-quiet-windows.csv](2830-quiet-windows.csv) holds the four windows as rows of type quiet-window (id, start, end, recurrence, who, status provisional, approver, note): 2026-11-23 16:10Z to 16:35Z, 17:10Z to 17:25Z, 18:35Z to 18:50Z, and daily 08:00Z to 08:25Z from 2026-11-24. They are for the Coach to merge into the trigger table the slot-idle report reads, to subtract from idle minutes; I do not edit the Coach's files. The margins are in [2830-quiet-window-margins.md](2830-quiet-window-margins.md): no named trigger falls inside a window; the builders open 55 minutes after the daily window, the Food Output V Complete 9 h 04 min after it, the Iron Output V Complete 5 h 21 min before the next one, and the 18:00Z plunder session must start by about 18:20Z or move to 18:50Z. The margin is written into the three builder units and the 17:30Z Complete unit. The donation passes carry the Researcher's addendum: the grid phase of the first timer end is decisive, read within one minute of the last tap, and the 35-minute reading is withdrawn as favoured.

## Not done

`research-complete-2026-11-25-001`, the Complete of Iron Output V at 02:39Z on 2026-11-25 if the 17:30Z speed-up does not move it, could not be minted: `enqueue` refused because the live `queue.py` differs from main (PR 911, token-lease, merged) and is not ahead of it. No bypass was used and the unit file was not written by hand. The coordinator brings the live tool up to main; the unit is minted after that. The same guard blocks `plan` and `next` from this copy, so the 18:03Z wave needs the synced tool as well.
