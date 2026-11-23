---
title: Oil Well found 1553
created: 2026-11-23T15:58:00Z
modified: 2026-11-23T15:58:00Z
version: 1.0.0
description: Third read-only locate run - the Oil Well is Lv.20 at the north-east wall; its Lv.20 to 21 preview costs only 8.5M iron (time 19:50:38 original, 09:20:18 effective), gives output 1,200 to 1,260 an hour and power +4,200, storage 10:40:00 to 10:48:00; the quest-bar line no longer reads Build Oil Well
status: done
grounded_in:
  - source: cu_bridge run 20261123T155317Z-884a03, frames step-0000, step-0004 and step-0005, 2026-11-23T15:53Z to 15:54Z
  - source: coordinator and Steer A answers of 15:55Z (branch 3b: the line changed, pan north-east and east; Details never pressed)
---

# Oil Well found

Rows in [1553-oil-well-found.csv](1553-oil-well-found.csv); parts one and two are [1541](1541-oil-well-locate.md) and [1547](1547-oil-well-locate-2.md). An assignment, not a queue unit; no ledger row (no state changed). The desktop lock was free; no different-device dialog.

- **Quest-bar line.** At **15:53:18.233Z** it reads "Upgrade Builder's Hut to Lv.26 (0/1)", no longer "Build: Oil Well (0/1)", so the well exists and the one approved tap on that line was not used.
- **Found.** After WORLD then BASE, two pans (drag (400,580) to (150,830), then (660,470) to (390,620)) brought the north-east edge into view; the tag over the pumpjack beside the grey tanks reads **Oil Well Lv.20**. Position about **(1090,340)** on the restored fresh frame (derived from the two drag offsets, approximate; off-screen right of the window), at the wall just left of the Alliance button on the pan-2 frame. No storage line on the tag.
- **Upgrade preview, Lv.20 to 21** (the green up-arrow only; Details, Collect, Upgrade and Finish Now never pressed): Hero EXP 660.0K; **Oil Output 1,200 to 1,260 an hour**; **Power 23,200 to 27,400 (+4,200)**; **Max Production Time 10:40:00 to 10:48:00**; cost **iron 8.5M only** (1.0G held, green check); prerequisites **Lv.30 Headquarters** and **Lv.1 Unlock Oil Well**, both green; **Original Time 19:50:38**, the Upgrade button clock **09:20:18**, Finish Now **456 diamonds** (read, not pressed).
- **Reading for the builder unit.** The well is already Lv.20, not Lv.1, so tomorrow's 09:21Z builder unit starts from Lv.20 to 21, not Lv.1 to 2. The storage 10:40:00 at Lv.20 matches the model of 8h08m at Lv.1 plus 8 minutes a level (19 levels), so a collect every 8 hours loses nothing. At about 4,200 power for 8.5M iron it is the cheapest power read today.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 7 steps, 0.112332 USD against a stated cap of 0.5; 0 refused.
- **Closing state.** The base at the north-east edge, no panel or selection; LastWar frontmost; token released.
