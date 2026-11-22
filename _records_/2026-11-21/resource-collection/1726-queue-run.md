---
title: Harvest queue run 1726
created: 2026-11-22T01:26:00Z
modified: 2026-11-22T01:26:00Z
version: 1.0.0
description: Queue unit harvest-2026-11-21-1403, ticker-1704 - two verified bubble collections (food +3.2M, coin +2.1M), one tap misfired into a battle-deployment screen and was backed out of untouched, bubbles remain and the Armed Truck unchecked
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 17:17-17:26 PT
  - source: unit harvest-2026-11-21-1403 in _queue_/done
---

# Harvest queue run 1726 (ticker-1704)

Unit harvest-2026-11-21-1403, regular harvest, activity
resource-collection, priority 3, est 9 minutes, expires
2026-11-22T02:03:00Z (18:03 PT). Executor ticker-1704.
Session window about 17:17 to 17:26 PT. Token held 17:04
to 17:20 PT; unit claimed 17:17 PT, lease to 17:37 PT.
Computer session cc-27.

## Outcome

Partial - two bubble collections verified live on the
top-bar totals (food +3.2M, coin +2.1M), but bubbles
remain over the farmland and the Armed Truck was not
checked inside this unit. No diamonds or money spent, no
stamina spent, no march sent. The tracker is untouched
(partial re-produces next tick).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-27.
- LastWar window 105986 (pid 5136, 763x1050) raised to the
  front with activate raise=true on the first attempt -
  the Issue #648 window precondition stays cleared.
- No different-device dialog, no login demanded, no Touch
  ID, no password typed.

## What happened

- Entry totals read live from the top bar: food 730.5M,
  iron 1.1G, coin 88.2M, diamonds 5,236, gold bars
  17.72K, power 149,653,371. Stamina 65.
- Tap 1 (17:19 PT) at 452,405 on the zoomed-in base view
  MISFIRED: the yellow shape there was not a bubble - the
  tap opened a battle-deployment screen (road view, five
  Lv.150 heroes staged, flag "35", 18.4M vs 25.4M, Battle
  button). Battle was NOT tapped; backed out with the
  back arrow at once. No march sent, no stamina spent,
  totals unchanged on return. This is the same tap-method
  failure class as ticker-0048 (taps landing on the wrong
  affordance) - the pivot is the same: re-ground on a
  fresh screenshot and verify totals per tap.
- The back-out re-centred the camera on the farm district
  (zoomed-out view), where the bubbles were clearly
  readable for the first time: green food bubbles
  (453.0K to 943.9K), yellow coin bubbles, white iron
  bubbles over the upper buildings.
- Tap 2 (17:23 PT) on the green food bubble labelled
  700.0K, grounded by visual grounding at 308,455 on a
  fresh screenshot: VERIFIED - food 730.5M to 733.7M
  (+3.2M). The middle-field green bubbles cleared; other
  green bubbles remain, so one tap did NOT collect all
  farmland bubbles this time (the 2026-10-25 all-at-once
  observation does not hold for this field state - the
  remaining bubbles sit on a second plot).
- Tap 3 (17:25 PT) on a yellow coin bubble, grounded by
  visual grounding at 176,514 on a fresh screenshot:
  VERIFIED - coin 88.2M to 90.3M (+2.1M). Iron unchanged
  at 1.1G.
- Close totals: food 733.7M, iron 1.1G, coin 90.3M,
  diamonds 5,236, gold 17.72K, power 149,653,371.
  Stamina 67 at close (regenerating, no spend).
- The Armed Truck was not located or checked; the red
  target icon at the right edge (countdown 00:00:39 at
  entry, 00:00:56 at close) was left untouched - it is
  not this unit's work.

## Remaining work

- Green food bubbles remain (about 610.2K, 581.0K,
  564.2K, 429.9K readable), white iron bubbles over the
  upper buildings remain, and at least one yellow coin
  bubble remains. The Armed Truck loot state is still
  unchecked. The next tick re-produces this regular as a
  fresh unit (partial: tracker untouched).

## Result stats

- target: collect every ready resource bubble and check
  the Armed Truck loot state
- achieved: 2 verified collections - food +3.2M, coin
  +2.1M; bubbles remain, truck unchecked
- resources_gained: food 3.2M, coin 2.1M
- costs: about 9 minutes device time, no stamina or items
- verified: yes (both totals read live from the top bar
  before and after each tap)
- blocker_category: h (by-design partial - pass budget
  reached with bubbles remaining; the tap-1 misfire is
  recorded above as the same tap-method class as
  ticker-0048, pivoted successfully by fresh-screenshot
  visual grounding)
- coin_before: 88.2M
- coin_after: 90.3M
- food_before: 730.5M
- food_after: 733.7M
- iron_before: 1.1G
- iron_after: 1.1G
- bubbles_collected: 2
- bubbles_remaining: many
- truck_checked: no

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #762 already open for the
  branch, no new PR owed.

## Delivery status (amended 17:31 PT)

- Commit 207229c6bb is on branch ticker-1704-delivery in
  worktree ~/workspace/lastwar-wt-1704-ticker, parented on
  the remote tip 0dd1c94871 (fast-forward). The push was
  NOT completed: the bundle file created for the VPS route
  failed an execution-risk check, so it was not copied to
  the VPS, fetched, or pushed. The commit awaits the
  owner's go-ahead to proceed with the bundle route (or
  an alternative push route). PR #762 is already open for
  records/2026-11-21; no new PR is owed once the push
  lands.
