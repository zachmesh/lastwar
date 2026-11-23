---
title: Oil Routine Sheet For The Base Expansion Path 2650 2026-11-23
created: 2026-11-23T05:00:00-08:00
modified: 2026-11-23T05:00:00-08:00
level: L0
version: 1.0.0
description: The reference the oil units point at - Steer A's oil model, the Oil Well collection every eight hours, the Oil Depot secret once a day, and what each routine unit reads and records
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0500-oil-sheet
trigger: coordinator message with Steer A's decisions on the Base Expansion path
started_at: 2026-11-23T04:58:00-08:00
finished_at: 2026-11-23T05:00:00-08:00
verified: figures copied from the coordinator message; none read on screen yet
grounded_in:
  - source: coordinator message 12:57Z relaying Steer A, analyst reports in /tmp/oilres/ and /tmp/lw/base-expansion-detail.md
---

# Oil routine, 2650

## Model [G], from Steer A's analysts

Lab time binds the Base Expansion path, not oil, but oil gates each research start. The Oil Depot secret pays 30K oil ONCE a day. Wells: one now, a second from the More Oil Wells research, a third at HQ 31. Storage is 8h08m at level 1 plus 8 minutes a level, so COLLECT THE WELL EVERY 8 HOURS or output is lost. The oil counter read 434K at the earlier read and 647.0K at 12:51Z (operator); whether it includes the 180K barrels is open (survey item).

## Routine units

- **Well collection** (`harvest-oil-well-2026-11-23-001` to `-003`): read the Oil Well panel (tag text and level, Output per hour, storage, stored oil) and the oil counter, press Collect, read the counter again, write the minutes since the last collection. Windows are about eight hours apart (the first from 13:15Z); the next one is due eight hours after the real collection time, so a late first run moves the rest.
- **Oil Depot secret** (`secrets-oil-depot-*`): the start right after the 02:00Z reset, the claim four hours later. Read whether it is available and whether today's 30K is already paid.
- **Radar and Bingo**: radar quests that pay oil and Bingo lines are taken when seen.
- **Before every research start** read the oil counter and write it.

## Limits

Collect and claim only; no purchase, no speed-up, no diamonds. A TIPS dialog about another device means stop and report, never Confirm. Tag text beside every number; none means [G].
