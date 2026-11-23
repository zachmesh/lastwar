---
title: Oil counter and research queue read
created: 2026-11-23T13:40:00Z
modified: 2026-11-23T13:40:00Z
version: 1.0.0
description: Unit research-age-of-oil-survey-2026-11-23-002 - the oil counter (647.0K) includes the used barrels; the research queue rows read twice (Food Output V and Coin Output V); no research speed percent shown and no node panel reachable, so M is not derivable
status: partial
grounded_in:
  - source: cu_bridge run 20261123T132645Z-156e23 (frame step-0002) and run 20261123T130851Z-d2a82d (Backpack oil tiles), 2026-11-23T13:09Z to 13:28Z
  - source: unit brief research-age-of-oil-survey-2026-11-23-002 (planner, survey item 5) and the 1308 record
---

# Oil counter and research queue read

Rows in [1327-oil-counter-queue.csv](1327-oil-counter-queue.csv). Claimed 13:26:45Z; no different-device dialog at the no-click first frame; nothing pressed.

- **Oil counter:** 647.0K on the HUD (oil counter beside the blue barrel icon) at 13:26:47Z, as in the Backpack header at 13:09Z and the HUD at 12:51Z; 434.1K at 11:18Z. The 3.0K x6 and 6.0K x32
  oil barrel tiles are gone from the Resources tab, so the **counter includes the 210K barrels** the other device used. The Oil Well has no panel: it is researched, not built.
- **Queue rows (13:26:58Z and 13:27:09Z):** "Lv.0 **Food Output V** upgrade in progress", Time Left **1d 04:02:56** then 1d 04:02:45 (ends about 2026-11-24T17:29:54Z), bar about 28 percent filled;
  "Lv.0 **Coin Output V** upgrade in progress", Time Left **1d 01:32:07** then 1d 01:31:57 (ends about 2026-11-24T14:59:05Z), bar about 30 percent filled. Each row has only a Speed Up button.
- **Research speed percent:** not shown on the queue panel. **Coin Output V node panel:** not reachable (a running node shows a timer only; no route to the trees while both labs are busy), so its base time, effective
  time and costs stay unread.
- **M, not derivable.** The bar fractions imply totals near 131,000 s (Coin) and 140,000 s (Food), so M = 485,100 divided by the total is near 3.7 and 3.5, but the speed-up minutes used on the blue-disc items
  (3,960) shift both the remaining time and the bar: unverified, about plus or minus 5 percent from the bar edge alone.
- **Next.** The Coin Output V panel (cost, base and effective time) needs an idle lab or the Tech Center route; the first lab idles about 2026-11-24T14:59Z.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 8 steps, 0 refused, no `local_input` pause, 0.088009 USD (stated cap 0.4). HUD: coin 55.9K, food 654.6M, Total Power 150,413,046.
- Closing state: the base, no panel, token released.
