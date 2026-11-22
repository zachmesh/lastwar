---
title: Harvest queue run 1133
created: 2026-11-22T19:33:00Z
modified: 2026-11-22T19:33:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-22-1003, ticker-1104, partial
status: unverified
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-22 11:23-11:33 PT
---

# Harvest queue run 1133

- Executor: ticker-1104, unit harvest-2026-11-22-1003, 11:23-11:33 PT (15 minute cap).
- Status: partial. Food panel pool collected and verified live; coin and iron panels not reached; Armed Truck unchecked (sixteenth deferral in the lineage).
- Live reads (top bar and panels, same unit):
  - Food 763.5M at entry, 765.4M at close: plus 1,842,030 verified.
  - Coin 109.2M at entry and at close, unchanged.
  - Iron 1.1G at entry and at close (display rounds to 0.1G).
  - Power 147,972,269, stamina 120, diamonds 6,436, all unchanged.
- What was collected:
  - Food panel: Owned 763,597,167, Available Resources 1,842,030, Collect tapped once; Owned after 765.4M on the panel, Available 0 re-read. Exact panel figures, HUD delta matches.
  - Building Acquisition rate read live: 674.9K/H. Resource Items 4.1G, Optional resource items 3.0G.
- Exit blocker, resolved in-unit (the finding of this unit):
  - The game was left on the Secret Command Post screen by the ticker-1050 secrets unit. The pass called open_app LastWar, which opened a SECOND window (127250) showing the same screen while the original window (127196) kept keyboard focus.
  - Every canvas input sent to 127250 was a no-op: back-arrow exact-pointer click, back-arrow snapped click, back-arrow double-click, left_click on the arrow, dimmed-area tap, and two background drags for the swipe-back - all no-change on screenshot. Menu (Last War > Quit Last War) and Cmd+Q also failed, naming the other window as the front/focus holder.
  - Activating the ORIGINAL window 127196 with raise=true restored input at once: the same back-arrow tap at (132,968) exited to the base screen on the first try.
  - This explains the standing Secret Command Post back-arrow blocker (2026-11-11 0909 unit: back arrow did not respond to two background clicks) - the input was going to a dead duplicate window, not to a dead control.
  - Rule for the next pass: never open_app when the game is already running - list_windows first, and if a LastWar window exists, activate THAT window with raise=true and work in it. If two LastWar windows exist, the one holding keyboard focus is the live one; the newer duplicate is a dead input target. Filed as tooling Issue #822.
- Armed Truck: not checked, sixteenth deferral. The unit closed on the base screen with the parked vehicles (red jeep, blue truck, green tank) visible bottom-left, so the next harvest unit starts ON the base screen with a working entry route and the trade-screen method is finally reachable without an exit fight. Commented on Issue #566. Retro A-2026-11-11-05 verification (truck located or unlocatable with surfaces checked) is still unmet.
- No diamonds or money spent, no paid button tapped, no red line touched.
- Tracker: untouched (partial unit - the next tick re-produces the regular).
- Follow-up: Issue #822 filed (tooling, open_app duplicate window); Issue #566 commented (sixteenth deferral, base reached at close).
