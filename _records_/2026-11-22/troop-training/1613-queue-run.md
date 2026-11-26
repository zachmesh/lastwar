---
title: Promotion press: Lv.8 to Lv.9 dialog read and cancelled 1613
created: 2026-11-26T16:18:58Z
modified: 2026-11-26T16:18:58Z
version: 1.0.0
description: Unit training-promotion-read-2026-11-26-003 (Steer A 16:04Z press approved; version 1.0.366(908); front LastWar throughout; owner idle 15,744 s; the different-device dialog never on screen; no UserNotificationCenter; one run; game actions ended 16:17:36Z, before the 16:23Z harvest deadline) - FIRST FRAME (16:13:59.4Z): HUD food 46.6M, iron 643.2M, coin 11.5M, oil 678.2K; Total Power 151,689,455; WORLD then BASE; the Lv.27 barracks (462,585) tapped once at 16:14:20.5Z: the tag 'Barracks Lv.27'; the pistol (459,631) pressed once at 16:14:33.8Z: Train Units (Lv.9 selected by default: Power 1352, 4.1M food and 4.1M iron); the green up-arrow badge on the Lv.8 tile (333,474) tapped once at 16:14:47.2Z (it only selects the tier); THE BEFORE FRAME (16:14:56.9Z): food 46.6M, iron 643.2M, coin 11.5M; Total Power 151,689,455; troop counts Lv.7 1,116, Lv.8 2,415, Lv.9 2,604, Lv.10 34.3K (locked); quantity 726 (max 726, untouched); cost row 3.2M food and 3.2M iron; Train and Finish Now 1d 06:53:38; the up-arrow beside the cost row (572,684) GREEN; THE ONE PRESS: that green arrow pressed ONCE at 16:15:17.0Z: a UNIT UPGRADING dialog opened (16:15:30.0Z): Lv.8 (Own 2.4K): Power 1063, Morale 531.25, Squad Load Capacity 1800, Unit HP 3566.74; Lv.9 (Own 2.6K): Power 1352, Morale 625.0, Squad Load Capacity 2000, Unit HP 4167.45; quantity 726 (the slider at its max); COST 887.6K food and 887.6K iron: NO coin, no gem, diamond or price icon; buttons FINISH NOW 03:25:58 and PROMOTE 03:25:58; the power gain per troop 289 (1352 minus 1063): about 209,800 for 726 (computed, not seen applied); DECISION: the dialog carries a Finish Now button, which the unit's Confirm rule excludes: CANCELLED by its X (616,206) at 16:15:38.5Z (Promote never pressed); AFTER THE CANCEL: +10 s (16:15:49.0Z) the panel back to Lv.8 selected: the HUD, Total Power, the four counts, quantity 726, cost and Train and Finish Now 1d 06:53:38 UNCHANGED; the reads at about +40 s (16:15:58Z) and +73 s (16:16:29.9Z) the same (the Lv.7 to Lv.10 counts 1,116, 2,415, 2,604, 34.3K); nothing promoted, nothing spent; the Train Units panel closed by its X (611,281) at 16:16:38.5Z; the base: HUD food 46.6M, iron 643.2M, coin 11.5M, Total Power 151,689,455; Train, Finish Now, Promote, the quantity controls and the building's green upgrade shortcut never pressed; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261126T161353Z-5fb618, final report read by the operator, 2026-11-26T16:13Z to 16:17Z
  - source: unit brief training-promotion-read-2026-11-26-003 and the troop-training rule digest
---

# Promotion press: Lv.8 to Lv.9 dialog read and cancelled 1613

Rows in [1613-queue-run.csv](1613-queue-run.csv). Claimed 16:13:52Z; no different-device dialog.

- **The green arrow opens the UNIT UPGRADING dialog** (Lv.8 to Lv.9, 726 troops): cost 887.6K food and 887.6K iron, no coin; time 03:25:58; Power 1063 to 1352 per troop (+289, about 209,800 for 726); buttons Finish Now and Promote.
- **Cancelled by the X** (16:15:38.5Z): the dialog carries a Finish Now button, which the unit's Confirm rule excludes: Promote never pressed.
- **Nothing moved:** HUD (food 46.6M, iron 643.2M, coin 11.5M), Total Power 151,689,455 and the counts (Lv.7 1,116, Lv.8 2,415, Lv.9 2,604, Lv.10 34.3K) unchanged at +10 s and +73 s.
- **Counts.** The press was the arrow once; the dialog never showed; drags 0.
- **Run.** One run, 20 steps, 8 actions, 0.269367 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 16:17:36Z.
