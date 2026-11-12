---
title: Resource collection queue run 0126
created: 2026-11-12T09:26:27Z
modified: 2026-11-12T09:26:27Z
version: 1.0.0
executor: ticker-0100
unit: harvest-2026-11-11-2203
status: partial
---

# Resource collection queue run 0126

Session 01:17-01:26 PST (ticker-0100, unit harvest-2026-11-11-2203).
Panel Collect route (standing method, Issue #585).

## What was done

- Entry HUD: food 698.4M, iron 1.0G, coin 143.7M (coin already
  143.7M from the zombie unit's LOOT claim in this same pass).
  Base view recentered with the BASE/WORLD toggle (was drifted
  onto empty map after the zombie unit).
- Coin panel: Available 1,999,342, Collect tapped, Owned 143.7M
  to 145.7M (exact Owned after 145,704,804), Available re-read 0.
- Food panel: first tap on the food icon (233,52) opened nothing;
  retry with an exact unsnapped tap opened it. Available
  3,078,487, Collect tapped, Owned 698.4M to 701.5M, Available
  re-read 0.
- Iron panel: first tap (390,53) opened nothing, second identical
  tap no change, third tap at re-grounded (397,53) opened it
  (R2 pivot - re-grounded point, third attempt). Available
  7,117,257, Collect tapped, Owned exact 1,023,418,672 after,
  Available re-read 0.
- Total collected by panel: coin 1,999,342, food 3,078,487, iron
  7,117,257 - 12,195,086 combined, all three panels re-read
  Available 0.
- Panel close: the iron panel X did not respond; the slow
  swipe-back (20,500) to (200,500) closed it (X responsiveness
  varies per panel and session, as recorded).
- MAP BUBBLES STILL STANDING after all three panels read
  Available 0: the closing base view shows the same bubbles as
  the pre-Collect view - blue triangle bubbles over the top row,
  yellow coin bubbles over the left buildings, green food bubbles
  over the wheat field (843.9K labels, same values as before the
  Collects). Second datapoint for the 0909 open question (the
  1531 unit reported no bubbles after its Collects): the panel
  pools do not drain the map bubbles, or the bubbles are a
  separate accumulation. A crop-grounded single bubble tap with a
  HUD re-read (the Issue #502 next-test) was attempted via the
  visual grounding tool, which timed out after 3 minutes, so the
  test stays owed - the bubbles' collectibility is still
  unverified. Do NOT assume the icons are decorative or that
  they were collected.
- Armed Truck: NOT checked this unit - twelfth deferral in the
  lineage (Issue #566). The parked vehicles (red jeep, blue
  truck, green tank) showed no collect bubble over them in the
  closing view; the trade-screen method is still untried. R7
  promotes this to the first action of the next harvest unit.
- No bubbles were tapped this unit; no map-bubble collection
  is claimed.

## Result stats

- target: 3 panel pools collected to Available 0
- achieved: 3 of 3 panels collected to Available 0
- resources_gained: coin 1999342, food 3078487, iron 7117257
- costs: about 9 minutes
- verified: yes (panel Available reads and Owned deltas, same unit)
- blocker_category: h (by-design partial - Armed Truck unchecked, map-bubble test owed)
