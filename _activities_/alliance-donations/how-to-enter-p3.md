---
title: How to enter part 3
created: 2026-11-23T06:11:49Z
modified: 2026-11-23T06:11:49Z
version: 0.1.0
sequence: 5
description: Entry, 2026-11-10 0634 - the game was left on the MAIL screen at entry (two LastWar
---
- Entry, 2026-11-10 0634: the game was left on the MAIL screen at entry (two LastWar windows on the same pid 1908) and the unit never reached Alliance Techs. Nine taps across two windows, two display modes and five methods produced exactly one game change: the mail back arrow in fullscreen, compensated 70 left, exited Mail to the base screen. The Alliance shield taps on the base screen were ignored even with the pointer sitting on the shield centre. The blocker is the input route, not the entry point - no entry-point change is indicated. Fullscreen tap offset measured in this unit: in native fullscreen 1920x1080 a requested tap lands about 70 normalized units right and about 14 up of the requested point (three independent cursor reads agree), so aim 70 left; in the windowed 642x951 mode no such offset was seen. Recovery for this state is the Issue #284 step: click the LastWar Dock icon once on the Mac mini (or run _tools_/mac_lastwar_front.sh in Terminal), then re-probe; no background route fixed it inside this unit, including the fullscreen escalation. Filed as GitHub Issue #575 (tooling), distinct from the #284 capture failure.

- Entry, 2026-11-10 0734: taps working again - the 0634 input-blocked state did not recur. The game was left on the Events hub Drone Boost screen by the ticker-0704 pass; the back arrow returned to the base screen (Total Power 148,058,020 live). Alliance shield grounded fresh from the current base screenshot at norm (931,714); the tap opened the Alliance menu on the first try. Alliance Techs tile grounded fresh at (686,674); opened on the first try. The (903,787) centre stays withdrawn.

- Entry, 2026-11-10 1133: Alliance shield at the fresh measured centre (930,715) on the current base screenshot opened the Alliance menu on the first try. Alliance Techs tile at (689,683) opened ALLIANCE TECHS on the first try. Both points re-grounded from the current screenshots, nothing inherited. Base framing full at entry, Total Power 148,058,020 live.

