---
title: Harvest queue run 2036
created: 2026-11-22T04:52:00Z
modified: 2026-11-22T04:52:00Z
version: 1.0.0
description: Queue unit harvest-2026-11-21-1803, ticker-2034 - three verified bubble collections (food +2.3M, iron bubbles cleared, coin +1.5M); Armed Truck unchecked
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 20:36-20:51 PT
  - source: unit harvest-2026-11-21-1803 in _queue_/done
---

# Harvest queue run 2036 (ticker-2034)

Unit harvest-2026-11-21-1803, regular harvest, activity
resource-collection, priority 3, est 9 minutes, expires
2026-11-22T06:03:00Z (22:03 PT). Executor ticker-2034.
Session window about 20:36 to 20:51 PT. Token held 20:34
to 20:51 PT; unit claimed 20:36 PT, lease to 20:56 PT.
Computer session cc-39.

## Outcome

Partial - three verified bubble collections (food +2.3M,
iron bubbles cleared, coin +1.5M), but the Armed Truck
was not checked inside this unit. No diamonds or money
spent, no stamina spent, no march sent. The tracker is
untouched (partial re-produces next tick).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-39.
- LastWar running and frontmost on entry; no
  different-device dialog, no login demanded, no Touch
  ID, no password typed.

## What happened

- Entry totals read live from the top bar: food 752.7M,
  iron 1.1G, coin 102.4M, diamonds 5,246, gold bars
  17.72K, power 149,653,371. Stamina 105, regenerating
  to 107 by close.
- The first BASE view showed no readable bubbles. A
  scroll down at the base centre re-rendered the view
  and the bubbles appeared: green food bubbles over the
  farmland, white iron bubbles over the upper mines,
  yellow coin bubbles over the mines. Visual grounding
  was not usable for bubble positions - it returned the
  top-bar HUD totals and scattered points instead - so
  bubble centres were read from fresh-screenshot crops
  and tapped directly. This is the R2 pivot for this
  unit: the no-bubble first view was not taken as an
  empty base; the scroll changed the view and revealed
  them.
- Tap 1 (20:44 PT) on the green food bubble labelled
  301.5K, grounded at 315,436 on a fresh screenshot:
  VERIFIED - food 752.7M to 755.0M (+2.3M). Every
  green food bubble in view cleared on this one tap
  (301.5K, 460.8K, 453.3K, 389.1K, 475.8K labels seen
  before the tap), so one tap collected the whole
  farmland set this time.
- Tap 2 (20:48 PT) on the white iron bubble labelled
  1.1M, grounded at 249,345 on a fresh screenshot:
  VERIFIED by disappearance - all five white iron
  bubbles in view (898.2K, 1.1M, 1.0M, 998.7K,
  998.7K, about +5.0M by label sum) cleared on this
  one tap, confirmed on the follow-up crop; the top
  bar still reads 1.1G because its 0.1G rounding hides
  a +5M move, so the iron amount is label-derived, not
  top-bar verified.
- Tap 3 (20:49 PT) on the yellow coin bubble labelled
  304.1K, grounded at 177,437 on a fresh screenshot:
  VERIFIED - coin 102.4M to 103.9M (+1.5M). Every
  yellow coin bubble in view cleared on this one tap
  (330.6K, 304.1K, 305.5K, 261.2K labels seen before
  the tap, plus one more below the crop edge).
- Close totals: food 755.0M, iron 1.1G, coin 103.9M,
  diamonds 5,246, gold 17.72K, power 149,653,371.
  Stamina 107 at close (regenerating, no spend).
- The Armed Truck was not located or checked; the red
  target icon at the right edge (badge 2, countdown
  00:00:45 falling to 00:00:27) was left untouched -
  it is not this unit's work. An alliance banner
  ("appointed BerLin as Secretary of Defense!") crossed
  the top of the screen during the unit; nothing was
  tapped there.

## Learning for the activity profile (not edited here)

- One tap collected the whole visible set for each
  resource in this unit (food, iron, coin each cleared
  on a single tap). This differs from the 2026-10-25
  note that iron and coin bubbles collect one by one,
  and from ticker-1704, where a food tap left a second
  plot's bubbles standing. Whether a tap clears one
  plot or the whole base is still open; the next unit
  should re-check for a second plot after each tap.
- Bubbles were invisible on the first BASE view and
  appeared only after a scroll re-rendered the base.
  A harvest unit that sees no bubbles must scroll once
  and re-read before concluding the base is empty.

## Remaining work

- The Armed Truck loot state is still unchecked. The
  next tick re-produces this regular as a fresh unit
  (partial: tracker untouched).

## Result stats

- target: collect every ready resource bubble and check
  the Armed Truck loot state
- achieved: 3 verified collections - food +2.3M, iron
  bubbles cleared (about +5.0M by label sum), coin
  +1.5M; truck unchecked
- resources_gained: food 2.3M, iron about 5.0M, coin 1.5M
- costs: about 15 minutes device time, no stamina or items
- verified: yes (food and coin totals read live from the
  top bar before and after each tap; iron verified by
  bubble disappearance, amount label-derived)
- blocker_category: h (by-design partial - Armed Truck
  unchecked inside the unit cap)
- coin_before: 102.4M
- coin_after: 103.9M
- food_before: 752.7M
- food_after: 755.0M
- iron_before: 1.1G
- iron_after: 1.1G
- bubbles_collected: 3 taps, all visible bubbles of all three resources cleared
- truck_checked: no

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #793 already open for the
  branch, no new PR owed.
