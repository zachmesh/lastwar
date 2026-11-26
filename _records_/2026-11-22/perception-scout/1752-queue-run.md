---
title: Hospital info button: instructions text, no tier printed 1752
created: 2026-11-26T17:54:57Z
modified: 2026-11-26T17:54:57Z
version: 1.0.0
description: PART TWO of unit scout-midday-hospital-completed-2026-11-26-001 (Steer A 17:51Z: the info button approved; record 1743 is part one; the queue unit is already closed; version 1.0.366(908); front LastWar throughout; owner idle 21,673 s; the different-device dialog never on screen; no UserNotificationCenter; the run ended at its cost cap with no report: I read the saved frames) - WORLD then BASE (17:53:04Z and 17:53:12.7Z); the Hospital tent (691,458) tapped once at 17:53:28.0Z: the tag 'Hospital' with its level (read 17:53:38Z; the panel title confirms HOSPITAL); the orange middle button (599,522) pressed ONCE at 17:53:44.5Z: THE HOSPITAL PANEL (17:53:56.7Z, digits from the saved frame): SEVERELY WOUNDED UNITS 1,364 of 7,999; one Lv.10 tile x1,364 (the wounded pool is Lv.10); COMPLETED 5,104 (a full bar); FREE ROOM = 7,999 - 1,364 - 5,104 = 1,531 (unchanged: expected); buttons: a green Collect (never pressed) and the round 'i'; THE INFO BUTTON (611,750) pressed ONCE at 17:54:09.1Z: a popup titled INSTRUCTIONS (read 17:54:19.0Z): '1. When you manually adjust the number of wounded units to treat some of them, the system will save the time needed as the default for the next treatment. 2. When you choose to treat all the wounded units, the system will reset the default and set the next treatment to treat all. 3. If you don't have enough resources to treat all the wounded, the system will adjust the number treated based on available resources.': IT PRINTS NO TIER OR COUNT OF THE COMPLETED TROOPS (it is the Heal instruction text); the info popup closed by its X (609,239) at 17:54:33.6Z; the Hospital panel closed by its X (605,257) at 17:54:43.7Z; the bare spot (300,670) at 17:54:59.2Z; HUD food 48.5M, iron 644.9M, coin 13.3M unchanged; the green Collect, Heal, Recover, Speed Up and Finish Now never pressed; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261126T175251Z-6e2dd2, final report read by the operator, 2026-11-26T17:52Z to 17:55Z
  - source: unit brief scout-midday-hospital-completed-2026-11-26-001 and the perception-scout rule digest
---

# Hospital info button: instructions text, no tier printed 1752

Rows in [1752-queue-run.csv](1752-queue-run.csv). Claimed 17:52:50Z; no different-device dialog.

- **Info button:** a popup titled INSTRUCTIONS with three points about treating wounded units (the manual number is saved as the next default; treating all resets it; short resources adjust the number): it does NOT print the tier or count of the Completed troops.
- **Panel again:** Severely Wounded 1,364 of 7,999 (Lv.10 x1,364); Completed 5,104; free room 7,999 - 1,364 - 5,104 = 1,531: unchanged.
- **Closed** by the two X buttons; Collect, Heal, Recover, Speed Up and Finish Now never pressed; HUD unmoved.
- **Counts.** The dialog never showed; drags 0.
- **Run.** One run, 13 steps, 7 actions, 0.159036 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 17:55:03Z.
