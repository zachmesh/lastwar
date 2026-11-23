---
title: How to enter - hardened against the rotating shortcut part 7
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 10
description: 2026-11-11 2105 - entry RECOVERED by the changed method the 1805 unit prescribed - the dish
---
- 2026-11-11 2105: entry RECOVERED by the changed method the 1805 unit prescribed - the dish icon was re-grounded from a fresh base screenshot (two visual grounding calls - the full window screenshot, then the cropped left column), landing at norm (55,702), close to the 0141 unit's (53,707) - the column shifts with the camera, so fresh grounding every unit is confirmed again. The tap was sent as an exact-pointer tap (snap_to_control false) so no accessibility snap could redirect it onto a neighbour - the record names the exact-pointer tap as a lesson for the entry section alongside fresh grounding, the default snap may have contributed to the 1805 mis-taps. Result: the radar screen opened on the first tap. Entry verified on the radar screen itself: Lv.13, radar points 427, stored 1/40, stamina 60/120, restore "12 Radar Task(s) will be restored in 02:29:47". Posture note from the same unit: tools/duel.py at 21:05 read duel day 4, theme Train Heroes, radar_posture stack - but the unit file's window text still reads "duel day 3 - radar release", stale against the live day-4 stack posture, the same staleness the 1805 unit noted; the live duel.py read governs.
- 2026-11-09 0636: another entry point, found by a harvest unit, not the dish - the gold circle with a blue gem above the blue truck vehicle on the base opens the world/radar map, which showed "6 task rewards can be claimed" with a Claim All button at 06:49. It is a radar shortcut, not the Armed Truck loot; the rewards were left untouched for the radar unit. A radar unit arriving through this shortcut still verifies the radar screen (level, points, stored count, stamina) before any work, same as the dish entry.
- Entry precondition, binding from the 1026 and 1439
  units: when the camera is panned onto the Drill Ground
  cluster, restore the full base view first - if a
  building panel is open, close it first (foreground the
  LastWar window and re-tap the X, click_element, or
  relaunch the app; a background-click X may not reach
  the control, and Esc is never used) - then ground the
  dish fresh from that screenshot. (2026-11-09 0852 refinement: a merely panned camera does not block the dish tap - the dish is a HUD icon and the tap at (51,726) landed cleanly with the camera still panned on the Drill Ground cluster; the restore-first rule still binds when a building panel is open.)
