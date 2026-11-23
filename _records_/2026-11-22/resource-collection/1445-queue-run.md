---
title: Harvest run 1445
created: 2026-11-23T14:49:00Z
modified: 2026-11-23T14:49:00Z
version: 1.0.0
description: Unit harvest-2026-11-23-0603 - Collect pressed once on the coin, food and iron panels (coin +555,712, food +848,362, iron +781,908); output 444.5K, 674.9K and 622.7K per hour; no bubble or building tapped
status: done
grounded_in:
  - source: cu_bridge runs 20261123T144418Z-b35699 (stopped on the Alliance screen), 20261123T144502Z-3381ef (coin) and 20261123T144558Z-65ae31 (food and iron), frames read before and after each Collect, 2026-11-23T14:44Z to 14:47Z
  - source: unit brief harvest-2026-11-23-0603, rule digest rules 4, 5 and 10, and the measured panel method of 1330-queue-run
---

# Harvest run 1445

Rows in [1445-queue-run.csv](1445-queue-run.csv); three ledger rows (14:45 to 14:46Z). No different-device dialog at any no-click first frame.

- **Method.** The top-bar resource icon opens its panel (digest rule 5); one Collect tap each, Available 0 afterwards on every panel; no Use, Open All, bubble or building was pressed.
- **Coin:** available **553,348**, owned 12,575,037 to **13,130,749** (+555,712); output **444.5K per hour**, owned below its capacity bar (16,474,999).
- **Food:** available 847,427, owned 653,841,655 to 654,690,017 (+848,362); **674.9K per hour**, owned above the capacity bar (49,642,724), Collect still worked.
- **Iron:** available 781,045, owned 1,065,914,089 to 1,066,695,997 (+781,908); **622.7K per hour**, above its bar (59,840,549), Collect still worked.
- **Reading.** The last pass was 13:30Z; 553K coin is 1.245 hours of output at 444.5K an hour, which matches the 1.25 hours since the 13:30Z pass (one interval, so a fit, not a proof). Oil counter 647.0K, unchanged; Total Power 150,416,946, unchanged. Coin owned is 13.1M of the 16.47M bar: about 7.5 hours of output below it, so a pass every 3 to 4 hours stays under the bar.
- **Not done.** The Armed Truck loot check (rule 9) is not in this brief. Tag text: none read beside these numbers (panel numbers, no building tag), so [G].
- **Runs.** Three runs of 8 steps or fewer, because the donation dialogs left open needed closing and three panels need 11 turns: run A (4 steps) closed both Alliance dialogs and stopped on the full Alliance screen, as ordered; run B went back, did coin; run C did food and iron. 0.052380, 0.061145 and 0.083219 USD, 0.196744 in all, cap 0.5 each; 0 refused, no `local_input` pause.
- Closing state: the base, no panel open (frame step-0007 of run C), token released.
