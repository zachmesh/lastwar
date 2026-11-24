---
title: Research queue already advanced by another actor 1734
created: 2026-11-24T17:36:05Z
modified: 2026-11-24T17:36:05Z
version: 1.0.0
description: Unit research-complete-2026-11-24-002 - nothing to Complete and nothing to start: the Research Queue (read twice, 17:35:05Z and 17:35:35Z) shows BOTH labs busy with other nodes than the brief expected: 'Lv.1 Food Output V upgrade in progress' (Time Left 1d 02:04:02 at 17:35:05.4Z, ends about 2026-11-25T19:39:07Z) and 'Lv.0 Oil Output I upgrade in progress' (1d 15:02:29, ends about 11-26T08:37:34Z); no Complete button, no idle lab, no Iron Output V row: the Complete of Food Output V, the Iron Output V and the start of Oil Output I were done by another actor on the account; nothing pressed except the flask icon and the panel X; HUD food 143.9M, iron 765.6M, coin 19.4M, Total Power 150,103,292; tram badge none; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T173531Z-833653, final report read by the operator, 2026-11-24T17:34Z to 17:36Z
  - source: unit brief research-complete-2026-11-24-002 and the research-queue rule digest
---

# Research queue already advanced by another actor 1734

Rows in [1734-queue-run.csv](1734-queue-run.csv). Claimed 17:34:53Z; no different-device dialog.

- **Queue.** Both labs busy with Lv.1 Food Output V (ends about **2026-11-25T19:39:07Z**) and Lv.0 Oil Output I (ends about **11-26T08:37:34Z**): **no Complete button, no idle lab, no Iron Output V row**.
- **Another actor.** The Food Output V Complete, the Iron Output V and the Oil Output I start were done on the account before 17:34Z (coin 19.4M).
- **Pressed.** Only the flask icon and the panel X; HUD and Total Power unchanged (150,103,292); tram badge none; drags 0.
- **Run.** One run, 10 steps, 4 actions, 0.128933 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 17:36:18Z.
