---
title: Oil Well locate 1547
created: 2026-11-23T15:53:00Z
modified: 2026-11-23T15:53:00Z
version: 1.0.0
description: Second read-only search for the Oil Well - three pans toward the upper left and 7 building taps found Material Workshop, Component Factory, Ginkgo Tree, Food Warehouse and Secret Command Post but no Oil Well; with 1541 the south-east and the north-west are covered, the north-east and east edge are not; no preview read
status: partial
grounded_in:
  - source: cu_bridge run 20261123T154712Z-c7387c, events and the final report, 2026-11-23T15:47Z to 15:50Z
  - source: coordinator 'GO' of 15:46Z (pan the other way, same read-only rules, record a grid if not found)
---

# Oil Well locate, second run

Rows in [1547-oil-well-locate-2.csv](1547-oil-well-locate-2.csv); part two of [1541-oil-well-locate.md](1541-oil-well-locate.md). An assignment, not a queue unit; no ledger row. The desktop lock was free; no different-device dialog; nothing pressed except the WORLD and BASE restore, map pans and tag taps.

- **Result: not found.** Tags read: **Material Workshop Lv.20**, **Component Factory Lv.20**, **Ginkgo Tree Lv.1** (a decoration; its recycle button was not touched), **Food Warehouse Lv.24** (tapped twice, aimed at its orange crates), **Secret Command Post Lv.1**, and yellow fuel barrels with no tag. None is the Oil Well; the green arrow was never pressed and no preview was read.
- **Grid of what was seen.** Restored frame: the whole base at the centre. Pan 1 (toward the upper left): the upper-left fence and grey tanks, a diagonal row of Material Workshops, the smelter furnaces, the ICU tower, pyramid, airfield, statues and an orange pipe at the top, a fountain and the Component Factory at the left. Pan 2: only snow, railway, a station and the fence. Pan 3: the far-left corner with a station, an outpost, landing pads, helicopters and a fenced strip of barracks-type buildings and barrels. Pan 3 went up and to the right, not strictly upper left, to reach that corner.
- **Not seen in either run (1541 and 1547).** The **north-east** (top right), the **east edge** and the right of the tents: no pan went that way. The south-east and the whole north-west are covered.
- **Reading.** The well is probably in the unseen east or north-east, or it carries no selectable tag (the grey tanks and barrels showed none). The planner's 02:05Z fallback unit covers it; a third pass would drag from about (540,450) to (290,700).
- **Run.** `claude-gateway/claude-sonnet-5-5`, 14 steps, 0.277562 USD against a stated cap of 0.5; 0 refused.
- **Closing state.** The base at the far-left corner after pan 3, no panel or selection; LastWar frontmost; token released. The next run starts with WORLD then BASE.
