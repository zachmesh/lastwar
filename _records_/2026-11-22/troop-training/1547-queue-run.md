---
title: Promotion read: no Promote tab, Train Units panel read 1547
created: 2026-11-26T15:51:58Z
modified: 2026-11-26T15:51:58Z
version: 1.0.0
description: Unit training-promotion-read-2026-11-26-001 (read only; the Coordinator's 15:50Z restriction: tap a control named Promote only if it is a tab or view selector; version 1.0.366(908); front LastWar throughout; owner idle 14,181 s; the different-device dialog never on screen; no UserNotificationCenter; two runs: 0.112 and 0.228 USD of the 0.80 cap) - HUD BEFORE (15:47:53.7Z and 15:49:28Z): food 46.6M, iron 643.2M, coin 11.5M, oil 678.2K; the Warzone Duel timer 10:12:07; RUN 1 (15:47:48Z): WORLD then BASE, the Lv.30 barracks (530,637) tapped once at 15:48:15.0Z: the tag 'Barracks Lv.30'; the button row: left a blue circle with a group-of-people glyph (about (456,652)), middle an orange circle with a PISTOL (about (527,679)), right a green circle with an up arrow (about (599,652): never pressed); the pistol pressed ONCE at 15:48:27.5Z: no panel and no toast in the next frames (the toast had faded); RUN 2 (15:49:22Z): the same route: the Lv.30 barracks tag again, the pistol pressed ONCE at 15:50:05.1Z: only a toast 'Drill Ground Full: Unable to add more units.' (gone by the first read): no Train panel: the Lv.30 barracks holds a finished batch (the Full state) and its Train Units does not open; then WORLD then BASE (15:50:30Z), the Lv.27 barracks (462,585) tapped once at 15:50:44.8Z: the tag 'Barracks Lv.27' with the same three buttons (the pistol about (459,631)); the pistol pressed ONCE at 15:51:04.1Z: THE TRAIN UNITS PANEL OPENED (so the view opens on the Lv.27 barracks while the Lv.30 barracks is Full: H13): Power 1352, Morale 625.0, Squad Load Capacity 2000, Unit HP 4167.45, Unit Attack 33.87, Unit Defense 7.04; the troop row: Lv.6 (partly visible), Lv.7 1,116 and Lv.8 2,415 (each with a GREEN UP-ARROW BADGE), Lv.9 2,604 (selected), Lv.10 LOCKED with 34.3K; the quantity row: a minus button, a green slider with its handle at the far right (the maximum), a plus button and 726; the cost row: 4.1M food and 4.1M iron for 726 troops (no coin row; every row visible: no drag needed); a GREY UP-ARROW BUTTON at the right of the cost row (about (572,684)): UNNAMED and NOT pressed; buttons 'Finish Now 1d 10:19:35' and 'Train 1d 10:19:35' (both never pressed); NO TAB named Promote and no control named Promote anywhere: the panel's text is the result (the Coordinator's rule: stop); no busy or slot line besides the toast; the panel closed by its X (611,281) at 15:51:37.8Z; HUD AFTER (15:51:56Z): food 46.6M, iron 643.2M, coin 11.5M, oil 678.2K: unchanged; no Promote, Train, Finish Now, Heal, Collect, Speed Up, Upgrade or buy button and no green up arrow pressed; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261126T154921Z-8456e8, final report read by the operator, 2026-11-26T15:47Z to 15:52Z
  - source: unit brief training-promotion-read-2026-11-26-001 and the troop-training rule digest
---

# Promotion read: no Promote tab, Train Units panel read 1547

Rows in [1547-queue-run.csv](1547-queue-run.csv). Claimed 15:47:46Z; no different-device dialog.

- **Lv.30 barracks:** the pistol only toasted 'Drill Ground Full: Unable to add more units.' (no panel) twice (the first toast faded unread).
- **Lv.27 barracks Train Units opened** while the Lv.30 barracks is Full: troop row Lv.7 1,116 and Lv.8 2,415 (green up-arrow badges), Lv.9 2,604, Lv.10 locked 34.3K; 726 troops max cost 4.1M food and 4.1M iron (no coin); Train and Finish Now 1d 10:19:35; Power 1352, Unit HP 4167.45.
- **No Promote tab or named control:** the only candidate is an unnamed grey up-arrow button beside the cost row (not pressed): per the Coordinator's rule the panel's text is the result.
- **HUD unmoved** (food 46.6M, iron 643.2M, coin 11.5M); nothing pressed but taps to open and close; drags 0.
- **Run.** One run, 24 steps, 11 actions, 0.33975 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 15:51:56Z.
