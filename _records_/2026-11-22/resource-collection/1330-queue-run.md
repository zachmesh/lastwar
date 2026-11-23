---
title: Harvest run 1330
created: 2026-11-23T13:45:00Z
modified: 2026-11-23T13:45:00Z
version: 1.0.0
description: Unit harvest-2026-11-23-0203 - Collect pressed once on the coin, food and iron panels (coin 55,963 to 529,247, food +82K, iron +736K); output rates 441.9K, 674.9K and 622.7K per hour; no bubble or building tapped
status: done
grounded_in:
  - source: cu_bridge run 20261123T132957Z-621d1c, events and final result, 2026-11-23T13:29Z to 13:32Z
  - source: unit harvest-2026-11-23-0203 (resource-collection), rule digest rules 1, 4 and 5, coordinator assignment A-20261123-1329-operator
---

# Harvest run 1330

Rows in [1330-queue-run.csv](1330-queue-run.csv); three ledger rows (13:30 to 13:31Z). Claimed 13:29:56Z; no different-device dialog at the no-click first frame.

- **Method.** The top-bar resource icon opens its panel (digest rule 5); one Collect tap each; no bubble over a building and no building was tapped.
- **Coin (COIN panel):** available **465,123**, owned 55,963 to **529,247** (+473.3K, a little above the read because output kept accruing); output **441.9K per hour**.
- **Food (FOOD panel):** available 80,618, owned 654,676,950 to 654,759,440; **674.9K per hour**, owned above the capacity bar (49,642,724), Collect still worked.
- **Iron (IRON panel):** available 725,582, owned 1,066,095,808 to 1,066,831,874; **622.7K per hour**, above its capacity bar (59,840,549).
- **Reading.** The other device collected about an hour earlier, so a full hour of output is 442K coin: coin income is about 10.6M a day, against 433.5M for HQ 31 and 23.8M each for the Gold Mine and Farmland
  steps; unverified beyond one hour. Each panel also carries Use rows for stored items and the coin panel Open All rows: not pressed.
- **Not done.** The Armed Truck loot check (digest rule 9) was not run: the station view belongs to a truck unit. Oil was not opened.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 12 steps, 0 refused, no `local_input` pause, 0.144364 USD (stated cap 0.5). Total Power 150,413,046 before and after; coin 529.2K after.
- Closing state: the base, no panel, token released.
