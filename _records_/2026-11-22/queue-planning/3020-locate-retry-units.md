---
title: Queue Planning The Tech Center And Builder's Hut Locate Retries 3020 2026-11-23
created: 2026-11-23T11:50:00-08:00
modified: 2026-11-23T11:50:00-08:00
level: L0
version: 1.0.0
description: Planner pass re-staging the two locate units that closed not found and partial, starting from the frames the earlier runs covered and panning only what was not seen
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1150-locate-retry
trigger: coordinator message 19:31Z, operator records 1541, 1547, 1553 and 1921
started_at: 2026-11-23T11:32:00-08:00
finished_at: 2026-11-23T11:50:00-08:00
verified: the four operator records read for the areas covered; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/resource-collection/1541-oil-well-locate.md, 1547-oil-well-locate-2.md and 1553-oil-well-found.md
  - source: _records_/2026-11-22/perception-scout/1921-queue-run.md
---

# The locate retries, 3020

`scout-midday-locate-retry-2026-11-23-001` (the Tech Center, serves PL-04) and `-002` (the Builder's Hut, serves PL-08), priority 3, 19:40Z to 2026-11-24T03:30Z, up to two runs of 8 steps each, one job each: read the tag and record the position in the tag index. The records show what is covered: record 1541 the south-east and the core base, 1547 the whole north-west, 1553 the north-east and the east edge (where the Oil Well was found), 1921 the south-west corner and the south edge. Not yet seen: the centre and the area around the HQ at about (565,405) and the clock tower for the Tech Center, which a lit research bubble should show while a lab runs (both labs run); the west, the middle and the centre for the Hut, a small building near the HQ whose name the HUD quest bar line carries (read for the name only, its Go is not pressed). The HQ radial menu or the Tech hub icon is allowed only if it stays in the game. The brief carries the SALE stall warning from record 1921 (never tap (135,525): it opens the Black Market panel), the idle-counter line (start only when it reads 300 s or more, since the owner may be at the Mac, and a foreground switch stops the run) and the standing-rule line.
