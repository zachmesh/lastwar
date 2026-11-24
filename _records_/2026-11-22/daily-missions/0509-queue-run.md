---
title: Daily missions after the reset 0509
created: 2026-11-24T05:12:30Z
modified: 2026-11-24T05:12:30Z
version: 1.0.0
description: Unit daily-missions-2026-11-23-1800 - the Oil Well Lv.22 side task Claim (5.0K food and 5.0K iron), one Daily Tasks Claim tap that claimed the four finished rows (activity points 0 to 90, gems +20) and the 40 and 80 chests opened; two further Claim rows (badge 2) stayed unclaimed because the second run's swipe was cancelled at 05:11:26Z by a foreground switch of an app outside the scope
status: partial
grounded_in:
  - source: cu_bridge run 20261124T050849Z-7d52d4, final report read by the operator, 2026-11-24T05:08Z to 05:11Z
  - source: unit brief daily-missions-2026-11-23-1800 and the daily-missions rule digest
---

# Daily missions after the reset 0509

Rows in [0509-queue-run.csv](0509-queue-run.csv). Claimed 05:08:49Z; no different-device dialog.

- **Main Tasks.** The Oil Well Lv.22 side task Claim paid 5.0K food and 5.0K iron (no popup seen); the list now starts with Upgrade Headquarters to Lv.31 (0/1), then Builder's Hut Lv.26, Hospital Lv.26, Training Base Lv.27, Gear Factory Lv.21.
- **Daily Tasks.** One Claim tap took the four finished rows (Daily Login, Radar Task, Donate to Alliance Tech, Help Allies): activity points **0 to 90**, gems **+20**; chests 40 and 80 opened (items in the CSV); 120, 160 and 200 locked.
- **Open.** Two more Claim rows (badge 2) below the fold unclaimed: the second run's swipe was cancelled at **05:11:26.2Z** by a foreground switch of an unnamed app outside the scope (out_of_scope); LastWar was frontmost again in the next frame.
- **Never pressed.** Any Go.
- **Run.** One run, 19 steps, 26 actions, 0.244 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 05:11:43Z.

- **Release point (CU-744 note).** The cancelled drag was released at its start (394,720) in the Mission panel: in the last good frame (step 5, Daily Tasks) that point is the blank gap between the Greet Visitors card (ends y 718) and the Kill 5 zombies card (starts y 726), midway across (x 394), well left of the Go buttons (x about 575): no Claim, Go or Buy under it. The next frame (05:11:29Z) shows the base: the Mission panel closed, no toast, no change in food 125.4M, iron 769.2M, coin 23.0M, gems 11,153 or Total Power 150,046,960 (energy 84 to 85).
