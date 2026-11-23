---
title: Age of Oil read
created: 2026-11-23T10:27:00Z
modified: 2026-11-23T10:27:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-022 - read-only look at the Age of Oil stage cards; stage 3 cards all done with green checks and no Claim button, stage 4 locked until 2026-11-29, no main timer, nothing claimed
status: done
grounded_in:
  - source: cu_bridge run 20261123T102201Z-ed63e6, events, final result and frames step-0004 and step-0006, 2026-11-23T10:22:01Z to 10:23:20Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-022 (baseline Age of Oil) and coordinator assignment A-20261123-1021-operator
---

# Age of Oil read

Rows in [1022-age-of-oil.csv](1022-age-of-oil.csv). The unit was claimed at 10:21:31Z (window end 10:29Z).

- **Stage track.** Four stages, stage 3 highlighted; the page has **no main timer** and no
  starts-in text. Each card carries its own timer.
- **Stage 3 (all done, no Claim).** Unlock Lv. 31-35 Zombies on World Map **3420/2000**, Rapid Rescue
  **689681/25000**, Major Construction **1636/500** (below the fold). Timers 6d 15:37:39 and
  6d 15:37:29 at 10:22Z, so they end **2026-11-30T02:00Z**. Each shows a green check, no green
  Claim button and no reward icon, so nothing could be claimed and no claim was pressed.
- **Stage 4 (read only).** Locked with the date **2026-11-29**: Unlock Lv.31-35 Doom Elite
  **0/1000** and Unit Training **0/50000**, each with a yellow chest icon, no quantity shown. No
  countdown.
- **Events tabs, not entered.** Black Market 20d 15:37:51 (the hub opened on it, matching the
  2026-12-14T02:00Z end), then Desert Battlefield, Winter Battlefield (PvP), Wanted Boss and
  Community; none shows a timer on its label.
- **HUD, before and after, unchanged:** food 648.5M, iron 1.0G, coin 14.4M, diamonds 11,136,
  Total Power 150,211,809; the snap command was run with those figures.
- **Reading, unverified.** The green checks probably mean the stage 3 rewards were already
  taken; the cards show no reward icons to confirm it.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 10 steps, 14 actions, 0 refused, no `local_input`
  pause, 0.143948 USD (stated cap 0.5 for 11 usable turns; the unit budget is 8 steps).
- Closing state: the base, no panel open, token released.
