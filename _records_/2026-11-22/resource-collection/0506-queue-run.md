---
title: Harvest queue run 0506
created: 2026-11-22T13:06:00Z
modified: 2026-11-22T13:23:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-22-0203, ticker-0504, partial
status: unverified
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-22 05:06-05:21 PT
---

# Harvest queue run 0506

- Executor: ticker-0504, unit harvest-2026-11-22-0203, 05:06-05:21 PT (15 minute cap).
- Status: partial. Food and coin bubbles collected and verified live; iron
  bubbles unverified; oil droplet bubbles unverified; Armed Truck unchecked.
- Live reads (top bar, same unit):
  - Food 760.8M at entry, 763.7M after the first food tap, 763.7M at close:
    plus 2.9M verified.
  - Coin 103.8M at entry, 103.8M after the first food tap, 107.6M at close:
    plus 3.8M verified.
  - Iron 1.1G at entry and at close (display rounds to 0.1G, so a small gain
    would not show); no iron total change verified.
  - Power 149,417,850, stamina 120, diamonds 6,436, all unchanged.
- What was tapped:
  - One farmland food bubble at grounded centre (306,455) collected food,
    plus 2.9M on the live panel. A first tap at (310,384) on a stale
    screenshot missed (food unchanged at 760.8M, bubbles still present) -
    the map view had shifted between screenshot and tap; re-ground on a
    fresh screenshot before tapping (R2).
  - One bubble at (239,554), grounded as food, moved coin 103.8M to 107.6M
    (plus 3.8M) with food unchanged - the visual grounding had mislabelled
    a gold coin bubble as food. Bubble colour at this scale is unreliable;
    verify by which total moves, as done here.
  - Four taps at the grounded oil droplet points (238,111), (348,156),
    (410,196), (470,223) dispatched in one batch, effect unverified: the
    map had scrolled again and an airport panel (plane + info icons) was
    open in the next screenshot, so the taps likely missed the droplets.
    Oil collection is unverified - no oil total is shown on the HUD.
- Window-close incident (own error, no game loss): after the oil batch, a
  compact observation listed element 1 as button 'close button' and it was
  clicked as if it were an in-game panel close - it was the macOS window
  close button. The LastWar window closed; the app relaunched cleanly
  (new pid 9479, window 642x951), base state intact, no game input lost.
  Lesson: in computer.observe compact view the first 'close button' is
  window chrome - never click_element on it; dismiss in-game panels by
  tapping empty ground or the in-game X only.
- Armed Truck: not checked - the unit cap was reached at the relaunch
  verification. The next harvest unit takes the truck check first (R7).
- No diamonds or money spent, no paid button tapped, no red line touched.
- Tracker: untouched (partial unit - the next tick re-produces the regular).
- Follow-up: none filed as an Issue; the window-close lesson is recorded
  here and in the pass note.
