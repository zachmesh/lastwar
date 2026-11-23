---
title: Queue Planning Slot Plan Conversion Units And Bypass Close 2430 2026-11-23
created: 2026-11-23T00:28:00-08:00
modified: 2026-11-23T00:28:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the inventory read and the tool merge - slots ranked by power per slot-day, conversion-and-spend units staged for the 11:43Z lab and the 2026-11-24 09:20Z builders with bounded speed-ups, and the stale-tool bypass log closed at 12 uses
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0028-slots-and-conversion
trigger: coordinator coin plan, owner decisions 2425, PR 876 merge
started_at: 2026-11-23T00:20:00-08:00
finished_at: 2026-11-23T00:28:00-08:00
verified: inventory arithmetic recomputed; pick order simulated at four instants; word counts of every staged unit under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/growth/0009-inventory-read.md
  - source: _records_/2026-11-22/queue-planning/2430-sinks-by-slot-day.csv, 2430-conversion-rules.md, 2410-coin-supply.csv
  - source: coordinator messages on the coin plan, owner decisions and the merge
---

# Slots, conversion and the bypass close, 2430

## 1. Slots decide, not coin

Coin obtainable is 2,383,161,480, of which 405,976,800 is read and 1,972,712,880 is inferred from Resource Choice Chests. Planning uses only the read figure (owner decision). The first conversion units open the read Coin Chests (281M) and touch a choice chest only after one is opened and its popup read. [Sinks by slot-day](2430-sinks-by-slot-day.csv): Drill Ground L25 about 65.9K power per builder-day, L26 47.8K, L27 34.3K, against 5.1K for the Training Base, 2.4K for the Hut (measured) and about 1.2K to 1.4K for barracks L30, Tech Center L30 and HQ L30. Days are the guide's base days times 0.476, the one measured Hut ratio, which is an assumption. Drill Ground L21 to L24 and the Expansion node are unread. The ledger has `slot_days` and `power_per_slot_day`.

## 2. Slot plan

- **Lab, about 11:43Z:** `research-growth-convert-2026-11-23-001` (11:44Z to 12:04Z), backup `-002` (12:10Z to 12:40Z). Complete the finished research, read the Drill Ground Expansion node, convert exactly its coin, start it.
- **Builders, 2026-11-24T09:20Z:** `building-queues-growth-convert-2026-11-24-001` and `-002` (from 09:22Z). Lowest Drill Ground first, convert exactly its coin, then a bounded speed-up. I re-timed the five 2026-11-24 fills to 09:10 to 09:21 and 09:50 to 10:50Z by hand, so the conversion units outrank them; simulated, no slot waits more than one unit.
- **Speed-ups:** a full speed-up would use about 7,547 minutes at L25, 10,497 at L26 and 14,750 at L27, which is 22, 30 and 42 percent of the 35,000-minute weekly cap. My default cap is 10,000 minutes on one upgrade; the coordinator may change it. 2026-11-24 falls on the Base Expansion duel day by the knowledge table, to be confirmed on the Duel screen.
- **ST1** staged (09:05Z to 09:45Z). ST1b is in the scout table and not staged.
- Queue-less sinks (gear levels, skills, drone, weapons) wait for C1, D1 and the previews.

## 3. Bypass log, closed

`LASTWAR_QUEUE_ALLOW_STALE_TOOL=1`, 12 uses, all `enqueue`: seven snapshot units 08:08:25Z to 08:08:28Z; one collect unit about 08:09:05Z; BM1 and SC1 at 08:17:23Z to 08:17:24Z; the two lab conversion units at 08:25:37Z. The last two came about 50 seconds after the merge at 08:24:46Z, before the ping reached me, so the coordinator's count of 10 is two short. None for `next`, `sync`, `plan` or `sweep`. No flag since 08:26Z. After the merge my fetch of main still failed, so the currency check was skipped, not passed.
