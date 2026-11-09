---
title: Resource Collection
created: 2026-10-25T18:58:00Z
modified: 2026-11-09T20:32:17Z
level: L1
version: 1.47.0
description: Collecting building output bubbles and truck loot, one activity folder for collection knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: resource collection execution record 2026-11-01 1149 queue run
  - source: resource collection execution record 2026-11-01 1534 queue run (same-unit screen reads and owner live corrections)
  - source: resource collection execution record 2026-11-01 2006 queue run
  - source: resource collection execution record 2026-11-02 0308 queue run (ticker-0308 unit, partial, edge drag unverified)
  - source: resource collection execution record 2026-11-02 0741 queue run (ticker-0734 unit, partial, fast regeneration over the left-side buildings)
  - source: resource collection execution record 2026-11-02 1052 queue run (ticker-1040 unit, partial, edges undragged)
  - source: resource collection execution record 2026-11-02 1520 queue run (ticker-1452 unit, partial, sweep barely started, campaign mis-tap)
  - source: resource collection execution record 2026-11-02 1945 queue run (ticker-1934 unit, partial, one farmland bubble, two new not-a-bubble points)
  - source: resource collection execution record 2026-11-02 2247 queue run
  - source: ticker-0234 resource-collection execution record 2026-11-03 0244 queue run (partial, four central bubbles, left edge undragged)
  - source: ticker-0634 resource-collection execution record 2026-11-03 0642 queue run (partial, central, left and top bubble-free, right edge unswept)
  - source: ticker-1034 resource-collection execution record 2026-11-03 1044 queue run (partial, central and right-bottom bubble-free, 0 collected, left and top unswept since 0642)
  - source: ticker-2034 resource-collection execution record 2026-11-03 2034 queue run (partial, one verified +1.6M second-row collection, factory-top grounding confusion filed as Issue #250)
  - source: ticker-0034 resource-collection execution record 2026-11-04 0034 queue run (failed, server maintenance blocked login, no base view reached)
  - source: ticker-0404 resource-collection execution record 2026-11-04 0413 queue run (partial, farmland +2.0M verified, factory-row marker confusion, Issue #250 evidence)
  - source: ticker-0734 resource-collection execution record 2026-11-04 0755 queue run (partial, farmland +2.6M verified, left-side +3.0M unattributed, Alliance back arrow corrected to (161,935), marker confusion repeats, Issue #250 already commented by the ticker pass)
  - source: ticker-1034 resource-collection execution record 2026-11-04 1101 queue run (partial, farmland +2.1M food and left-side +1.4M coin verified, entry corrections re-confirmed, sweep incomplete at unit cap)
  - source: ticker-1634 resource-collection execution record 2026-11-04 1634 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, ninth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-2104 resource-collection execution record 2026-11-04 2104 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, next ticker pass after 2034 known to fail identically, Issue 284)
  - source: ticker-0034 resource-collection execution record 2026-11-05 0034 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, twenty-fourth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0434 resource-collection execution record 2026-11-05 0434 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, thirty-second consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0904 resource-collection execution record 2026-11-05 0904 queue run (failed, Mac device invoke channel stall, zero responses to any invoke, fortieth consecutive ticker pass with a Mac device-access blocker, first recording of the worsened zero-response form, Issue 284)
  - source: ticker-1634 resource-collection execution record 2026-11-05 1634 queue run (failed, Mac device offline, fifty-fourth consecutive ticker pass with a Mac device-access blocker, fifteenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 9h04m, unchanged since the 1025 pass; five invokes, zero responses)
  - source: ticker-0504 resource-collection execution record 2026-11-06 0504 queue run (failed, Mac device offline, sixty-ninth consecutive ticker pass with a Mac device-access blocker, thirtieth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 21h30m, unchanged since the 0004 pass; five invokes, zero responses)
  - source: ticker-0704 resource-collection execution record 2026-11-06 0704 queue run (failed, Mac device offline, seventy-third consecutive ticker pass with a Mac device-access blocker, thirty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 23h36m, unchanged since the 0534 pass; four invokes, zero responses, no recovery-device attempts)
  - source: ticker-1904 resource-collection execution record 2026-11-06 1904 queue run (failed, Mac device offline, eighty-seventh consecutive ticker pass with a Mac device-access blocker, forty-eighth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 35h37m, unchanged since the 1827 pass; five invokes, zero responses, recovery-device health check and repair both timed out after 25s; pre-reset zero-sweep pair both expired unexecuted, no ledger line verified at zero for this reset day)
  - source: ticker-2257 resource-collection execution record 2026-11-06 2257 queue run (failed, Mac device offline, ninety-second consecutive ticker pass to fail this way, fifty-third in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 39h, unchanged since the ticker-1025 pass; six invokes, zero responses, recovery-device health check timed out after 25s; no queue-state divergence this pass)
  - source: ticker-0526 resource-collection execution record 2026-11-07 0526 queue run (failed, Mac device offline, one-hundredth consecutive ticker pass to fail this way, sixty-first in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 46h, unchanged since the ticker-0420 pass; seven invokes, zero responses, recovery-device health check and repair both timed out after 25s; no queue-state divergence this pass)
  - source: ticker-0704 resource-collection execution record 2026-11-07 0704 queue run (failed, Mac device offline, one-hundred-second consecutive ticker pass with a Mac device-access blocker, sixty-third in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 47.5h, unchanged since the ticker-0633 pass; four invokes, zero responses, recovery-device health check timed out after 25s; sync expired 6, produced duel-score-2026-11-07-0630; inbox 69, done 1049 at 15:06Z; pre-reset zero-sweep pair pending 2)
  - source: ticker-1655 resource-collection execution record 2026-11-07 1655 queue run (partial, farmland bubbles 40.9K/38.8K/37.7K/37.1K/32.0K cleared in one tap, about 186.5K food; purple crystal and beige square are static decorations, blue droplet over the truck opens the world-map task view; Armed Truck loot and full-map sweep unfinished; unit 466 seconds inside the 15-minute cap; record commit 514e333e5b on records/2026-11-07)
  - source: ticker-1940 resource-collection execution record 2026-11-07 1941 queue run (partial, farmland +1.9M food and +1.2M coin verified by HUD deltas, iron +1.7M observed unattributed, estimated bubble centres failed twice so ground-then-tap is now the rule, gold truck icon tap at norm 681,814 panned to the Drill Ground instead of opening a loot panel, Armed Truck loot and full-map sweep unfinished; unit 476 seconds inside the 15-minute cap; record commit c47e491fd on records/2026-11-07)
  - source: ticker-0934 resource-collection execution record 2026-11-08 0958 queue run (partial, food +8.2M coin +5.4M iron +7.5M verified by HUD deltas, one-tap farmland rule holds, grounded centres work, top-edge bubbles unreliable and batch opened Power Details, Power Details breakdown measured, sweep unfinished; record commit ac350b49c on records/2026-11-08)
  - source: ticker-1134 resource-collection execution record 2026-11-08 1211 queue run (partial, farmland food +1.6M HUD-verified, top-edge single tap collects nothing, iron +1.3M unattributed not claimed, coin bubbles about 0.8M remain, token expired 12:22:56); record commit ce3dcc4bf on records/2026-11-08
  - source: ticker-1724 resource-collection execution record 2026-11-08 1759 queue run (partial, iron +3.6M and coin +3.6M HUD-verified in two taps, food bubbles still standing, bubble-type identification unreliable per R2, identical +3.6M unexplained, reset arrived mid-sweep; record commit 5f3a904f4 on records/2026-11-08)
  - source: ticker-1935 resource-collection execution record 2026-11-08 1935 queue run (partial, food +5.1M one-tap all-at-once and iron +1.2M one-tap one-bubble HUD-verified, coin tap missed its bubble, pre-unit HUD rise food +3.2M iron +3.1M unexplained; record commit 5534be1e5 on records/2026-11-08; section and changelog folded in 1.42.0, this grounded_in line added by the 2332 run)
  - source: ticker-2308 resource-collection execution record 2026-11-08 2310 queue run (partial, 0 bubbles collected, two verified non-bubbles, HUD rise second occurrence, Issue #490 filed; record commit aac215e08 on records/2026-11-08)
  - source: ticker-0140 resource-collection execution record 2026-11-09 0202 queue run (partial, 0 collected, no resource bubbles in two base views, resource quarter not reached, Armed Truck entry unlocated, white truck (55,652) opens Secret Command Post; record commit 3d5dc8314 on records/2026-11-09)
  - source: ticker-0334 resource-collection execution record 2026-11-09 0340 queue run (partial, one tap per resource type cleared all visible bubbles of that type, iron +4.9M coin +4.3M food +5.4M EXP 4 bubbles, contradicting the 1935 iron one-by-one re-confirmation, Issue #502 filed, recenter-first sweep executed; record commit 063a5bde7f on records/2026-11-09)
  - source: ticker-0634 resource-collection execution record 2026-11-09 0636 queue run (partial, one tap per type cleared all bubbles of that type a second time - food +2.0M, coin +1.3M, iron +1.9M HUD-verified - blue-triangle 596 bubbles over the furnaces cleared on one tap with no HUD move, Issue #508 filed, EXP bubble and Armed Truck loot left for the next unit; record commit 04b12d13 on records/2026-11-09)
  - source: ticker-1204 resource-collection execution record 2026-11-09 1220 queue run (done, all visible bubbles collected - food +3.9M, iron +3.6M, coin +2.6M HUD-verified - one farmland tap collects all food a third time, panel swipe-close method measured, Armed Truck loot unchecked at the 15-minute cap; record commit 6f18bc3be on records/2026-11-09)
---


# Resource collection

## What this activity is

Collecting accumulated building output - the resource bubbles over
buildings and the Armed Truck loot. This folder accumulates collection
knowledge - bubble behaviour, capacity and truck timing.
Executions are recorded in
`_records_/<date>/resource-collection/`, one file per execution.

## How it is done

- Tap each output bubble over the base buildings - and tap the
  center of the bubble itself. The owner corrected this on the
  evening of 2026-10-25 after side taps missed; a tap on the edge
  can fall through to the building underneath and open its panel
  instead of collecting. Ground the bubble center visually before
  tapping, and verify the resource total moved afterwards.
- Estimated bubble centres are not reliable at this window size - measured 2026-11-07 (1941 unit): two estimated-centre taps failed to collect (one no HUD move, one no change at all); the pivot to grounding the bubble centre with the visual grounding tool on the live screenshot before tapping collected. Ground first, then tap - never tap an estimated centre.
- Food is special - tapping any one farmland bubble collects all
  farmland bubbles at once (observed the same evening, food rose
  about 0.4M in one tap and every farmland bubble cleared). Iron
  and coin bubbles collect one by one. (2026-11-08 1759 update:
  the one-by-one line was marked suspect - two taps aimed at
  supposed food bubbles collected iron +3.6M then coin +3.6M, the
  identical figure on both taps recorded as observed, not
  explained; one candidate mechanism, NOT verified, was a tap
  clearing all standing bubbles of one resource type at once.
  2026-11-08 1935 update: the test is now run for iron - one tap
  grounded fresh on a blue iron bubble centre collected exactly
  one iron bubble (+1.2M HUD-verified, food and coin unchanged),
  so iron one-by-one is RE-CONFIRMED and the 1759 identical
  +3.6M is explained in part as two different bubbles holding
  similar amounts, not a shared clear. Coin is still untested:
  the 1935 coin tap missed its bubble and hit the Iron Mine
  building underneath, so the coin one-by-one line stays suspect
  until a coin tap lands and is HUD-verified.) (2026-11-09 0340 update: the 1935 iron RE-CONFIRMATION is contradicted by the newest verified record - one tap grounded fresh on a 974.9K iron bubble centre cleared all four visible iron bubbles at once (iron +4.9M HUD-verified), one tap on a 952.4K coin bubble centre cleared all three visible coin bubbles (+4.3M), one tap on a 1.8M EXP bubble centre cleared all four EXP bubbles, and one tap on a 1.1M food bubble centre collected the food bubbles (+5.4M). Iron and coin one-by-one are therefore SUSPECT again, not settled; the 1935 one-tap-one-bubble read is not deleted, it stands as a single-bubble-remaining read or a different standing condition, tracked as knowledge Issue #502. The HUD deltas exceed the visible bubble sums (iron +4.9M vs 3.83M visible, coin +4.3M vs 2.71M, food +5.4M vs about 3.3M), so a candidate mechanism, NOT verified, is one tap collecting that type base-wide including off-frame bubbles. Until #502 is resolved, fold sections record per-type clears as observed and do not re-assert one-by-one for any type.) (2026-11-09 0636 update: second independent confirmation - one tap per type cleared all standing bubbles of that type again (food 5 bubbles +2.0M, coin 5 bubbles +1.3M, iron 4 read bubbles +1.9M HUD, all HUD-verified in-unit), and the same tap behaviour cleared the four blue-triangle 596 bubbles at once. One-tap-per-type is now the standing rule, grounded in two verified units (0340, 0636); the 1935 one-tap-one-bubble read stands as a single unexplained outlier, possibly only one bubble of that type standing at the time, not deleted. The HUD deltas again exceed the read bubble sums (iron +1.9M vs about 1.53M read), so the base-wide-collection candidate is still NOT verified. Issue #502 stays open pending the daily retro's closure decision.) (2026-11-09 1220 update: third confirmation - one tap on an 862.2K bread bubble collected all farmland at once, HUD food +3.9M, more than the two visible bread bubbles, so further farmland bubbles off the crop cleared too; iron 5 bubbles +3.6M and coin 4 bubbles +2.6M collected in-unit. One-tap-per-type stands, grounded in three verified units (0340, 0636, 1220); the base-wide-collection candidate is still NOT verified.)
- Verify the bubble's identity before tapping (rule R2, added
  2026-11-08 1759): bubble-type identification from the
  downscaled base screenshot is unreliable - both 1759 taps were
  aimed at food bubbles and collected a different resource (iron,
  then coin). Read the bubble's value label and icon at full
  resolution, or confirm the resource total that moves after the
  first tap before tapping a second bubble of the same supposed
  type. A tap point that looks like a wheat bubble can sit on an
  iron or coin bubble. (2026-11-08 1935 update: for coin bubbles, zoom the base view in
  before tapping, or tap only a bubble whose yellow coin icon and
  value label are both readable in the screenshot. The 1935 coin
  centre candidates around norm 132,436 and 234,452 are NOT
  verified - the 234,452 tap hit the Iron Mine building underneath
  - so do not reuse them blindly; re-ground fresh in the next
  unit. (2026-11-08 2310 update: recenter the base view FIRST
  before sweeping - the 1935 unit recentered only after the map
  drifted, and the 2310 unit panned blind three times and never
  found the bubble cluster. Two new verified non-bubbles, do not
  reuse: norm 701,468 (gold diamond) is the zombie NPC marker, it
  opens the Area No.168 dialogue; norm 565,636 (orange sack) is
  the Recon Plane Lv.24 building indicator, not a bubble.)
- Check the Armed Truck and claim it when it shows fully loaded.
- Close an accidentally opened building panel with the left-edge swipe-back gesture (drag from x 20 to 200 at y 500) - measured 2026-11-09 (1220 unit): the panel X does not respond to background clicks (single, double, 1s and 2s holds all no-change), while the swipe closes one level per drag. The same unresponsive-X class trapped the upgrade panel in the 1204 Builders Hut unit. Never batch-tap on after a tap opened a panel - tap bubbles one at a time with a screen read between taps, or the batch taps panel rows. Bubble centres must be re-grounded from an enlarged crop, never from the downscaled full screenshot - the 1220 unit's first tap at 210,589 hit a building, not a bubble, for exactly that reason.
- The gold truck icon is not a verified loot-panel entry - measured 2026-11-07 (1941 unit): tapping the gold truck icon at norm 681,814 panned the map down to the Drill Ground area instead of opening a loot panel. The loot panel entry remains unlocated and the Armed Truck loot state stays unverified.
- The gold circle with a blue gem above the blue truck vehicle is a radar shortcut, not the truck loot - measured 2026-11-09 (0636 unit): tapping it opened the world/radar map showing "6 task rewards can be claimed" with a Claim All button; the rewards belong to the radar unit and were left untouched, and the truck vehicle itself was not tapped, so the Armed Truck loot state stays unverified.

## Standing instruction from the owner

- Set on 2026-10-25 (evening), with the same standing autonomy as
  the alliance help icon - harvesting is collected directly
  whenever it is ready. Tap every ready output bubble - farm
  (food), iron, coin, and all other resources - in any session
  and at any moment, autonomously, without asking first. The
  Armed Truck loot is claimed the same way when fully loaded.
  Do not leave finished output sitting uncollected.

## What is known from 2026-10-25

- Five bubbles of 466.9K each were waiting at login, per the base
  snapshot in the day play record.
- After a collection, a bubble restarts from a small accumulating
  figure. That reset is normal, not a loss.
- The Armed Truck, level 1 with an 8 hour loot accumulation as
  displayed, was claimed once after it showed fully loaded, and then
  returned to a Collecting state.
- Bubbles regenerate fast - a fresh round of iron and coin bubbles
  was ready within minutes of the evening collection. Collect what
  is ready in a pass and move on; do not chase the regeneration.

## What the 2026-10-31 late unit and the 2026-11-01 early unit measured

- Not every round floating icon is a bubble - measured 2026-10-31
  (2343 unit): the orange confetti balloon over the central
  helicopter pad is not a resource bubble. The chat line in the
  same view mentions fireworks, and the balloon was left untapped.
  Confirm the point is an output bubble before tapping: visual
  grounding can return HUD buttons as bubbles - in the same unit
  a grounding-returned point at norm 694,860 opened the Chat
  panel instead (that point is the chat button; the chat back
  arrow at norm 85,953 returns to the base).
- Base-view panning failed in both units - measured 2026-10-31
  (2343) and 2026-11-01 (0016 survivors unit, same zoomed
  central-pad view): drags (500,600 to 200,600; 200,500 to
  600,500; 600,700 to 300,300; and 500,500 to 200,500) left the
  view unchanged, so building sectors beyond the zoomed view
  could not be inspected and the Armed Truck fully-loaded state
  went unchecked in the 2343 unit. A slow manual drag (mouse
  down, stepped move, mouse up) or a scroll zoom-out, starting
  from the wider relaunched view, stands as the untried next
  method from the 0016 record - proposed, not verified.
- Negative result, same units: three fresh base screenshots in
  2343 showed no verifiable bubble; HUD unchanged across the
  unit (food 289.2M, iron 477.2M, coin 10.6M); bubbles collected
  0; tracker untouched, so the regular stays due.

## What the 2026-11-01 1149 unit added

- Bubble inventory at entry, located by visual grounding
  on the base screen: five green bubbles at norm 371,413,
  279,466, 472,462, 372,503 and 472,571. A single tap on
  the 371,413 bubble cleared all five bubbles from the
  screen at once, consistent with the farmland rule that
  one farmland tap collects all farmland bubbles. No
  bubble remained on the closing screenshot.
- HUD precision note: food 289.2M, iron 477.2M and coin
  10.6M read the same rounded values before and after,
  while the second-row blue resource moved 18.1M to
  18.2M, confirming a collection landed. Gains below the
  0.1M display precision do not move the rounded food,
  iron and coin figures, so an unchanged rounded HUD is
  not proof that nothing was collected - read the
  second-row resource and the bubble clearance together.
- Armed Truck not checked in this unit: the pass time
  budget was already exceeded when the base screen was
  reached, so the truck check falls to the next harvest
  unit, and no claim is made about whether its loot is
  fully loaded. The unit closed partial and the tracker
  is left untouched, so the regular stays due.


## What the 2026-11-01 1534 urgent full sweep added

- Unit harvest-2026-11-01-1403 by ticker-urgent-harvest,
  session about 15:34 to 16:13, status done with one
  disclosed executor miss (the drone bubble, below).
  The unit was claimed out of the queue on the owner's
  urgent report at 15:33 that the production bubbles
  were full and sitting uncollected. Standing rule
  confirmed by this pass: a full bubble means production
  has stalled, so a harvest reported full is claimed
  urgently, not left to wait for its regular slot.
- Measured totals (same-unit screen reads): before
  collection food 323.9M, iron 512.1M, coin 29.8M,
  second-row blue ingots 18.7M, dark stone 265.5K,
  diamonds 11.72K, power 148,967,493; at the end food
  341.2M, iron 528.7M, coin 41.0M, the other figures
  unchanged at display rounding. The deltas combine
  the bubble collections below, the three truck
  returns, and three small regenerated rounds collected
  during the sweep.
- Full-base bubble location map. Coordinates are
  normalised 0-1000 within the 642x951 game window in
  the named screenshot's camera framing; the landmark
  and base area are the durable locator, the
  coordinates are the framing-specific tap point.
  Every entry was verified cleared on a follow-up
  screenshot unless marked otherwise:
  1. FOOD - wheat farms, center of the main base.
     One tap on any farmland bubble collects all
     farmland bubbles at once (tap used 364,554 in
     the center-north framing). Round 1 gain: food
     323.9M to 331.8M.
  2. IRON / STONE - iron mine row, left-center of the
     main base, beside the farms. Collected one by
     one. Round 1 gain: iron 512.1M to 519.3M.
  3. COIN - gold mines, bottom-left (southwest) of
     the main base, the flaming buildings. Collected;
     coin 29.8M to 35.0M. A stray extra tap after the
     last bubble opened the Gold Mine survivor panel;
     it was closed with no dispatch change.
  4. COIN - far-left blue coin buildings, west edge
     of the main base, partially cut off in the
     centered view; pan west to see them whole.
     Tapped and cleared.
  5. EXPERIENCE - green bubbles over the iron-mine /
     left-side production rows, same left-side area
     as entries 2-4. Collected in one batch; the
     owner confirmed on screen that the experience
     bubbles were collected.
  6. SCREWS - row of small blue workshops along the
     TOP-LEFT (northwest) edge of the main base,
     beside the coin and stone rows. In the centered
     view this row is half hidden under the top
     resource bar; pan north a bit to bring the
     bubbles fully into view. A single tap on the
     center bubble collected all five at once
     (gold circles with a wrench/screw icon). This
     was the last full bubble the owner flagged live
     at about 15:49.
  7. WEST COMPOUND WORKSHOPS - small white bubbles
     with a blue gem icon over the red-roof workshop
     buildings inside the walled compound at the far
     west of the base (tank/artillery yard). One tap
     collected all five at once.
  8. BLUE BUBBLES, FURNACE ROW BY HQ - three blue
     bubbles over the round furnace buildings in the
     top-center of the base, below Headquarters.
     Tapped in the first batch; no total moved at
     display rounding, type unverified.
  9. COIN - red/white building, center of the base.
     Seen at entry, gone in the closing views.
  10. TRUCK COMPLETION BUBBLES - Trade screen, Your
     Truck tab: a completed dispatched truck shows a
     speech bubble with a blue chest on top of the
     truck; collect it. Owner-stated rule from this
     pass: "a completed dispatched truck shows a
     bubble on top of the truck; collect it." Three
     finished trucks showed bubbles; the fourth had
     none (still en route). Tapping the first bubble
     ran one collection flow that collected all three
     finished trucks (the Your Truck tab badge dropped
     3 to 1). Rewards read on the Truck Details screen
     for the UR truck, Intercity Trade Reward, vehicle
     safe and secure: food 3.8M, iron 3.8M, coin 2.4M,
     plus a squad row of food 2.5M, iron 2.5M, coin
     1.6M, chest x80, red gem 50 x1, badge 500 x6
     total, gold tickets x2, puzzle piece x1,
     notebook x1, red gem 100 x1 and 5-minute
     speedups. The other two trucks' returns were
     collected in the same flow without a separate
     details read.
  11. DRONE COMPONENTS - MISSED BY THE EXECUTOR. The
     standing instruction names the drone component
     bubble as always-collect; this pass did not
     identify or collect it. The owner collected it
     himself at about 15:52 and reported so live. It
     is NOT claimed as collected here. Its spot was
     not identified in this pass's screenshots; the
     only unverified candidate seen is the blue
     diamond bubble at the top-left corner in the
     center-north framing (164,116, over the corner
     building by Headquarters) - unverified, marked
     owner-collected / missed-by-executor. Do not
     treat that candidate as the located drone spot.
  12. SEASON 2 AREA (NOT main base) - panning to the
     bottom of the map leaves the main base and
     reaches the Season 2 area (vehicle bays 2 and 3,
     drill grounds). The owner corrected this live:
     the bottom-area bubble belongs to the Season 2
     area and is a different thing from the main-base
     production bubbles; do not confuse the two areas
     in future passes. No production bubbles were
     found or collected in the Season 2 area in this
     pass.
- Bubble-versus-icon distinction, refined: the Gear
  Factory chip icon, the Decoration Gallery book icon
  and the green survivor-stationed markers are building
  entry or status icons, NOT collectible bubbles. A
  collectible bubble is a circle carrying a resource
  icon and an amount label. Bubble-edge taps can still
  fall through to the building underneath (this pass
  opened, and closed with nothing bought or changed:
  Emergency Center, Iron Mine upgrade panel twice
  with Finish Now never tapped, Gold Mine survivor
  list and building panel, Trade screen, Secret
  Command Post, Gear Factory, Decoration Gallery) -
  consistent with the 2026-10-25 center-tap rule.
- Pan correction, qualifying the 1.3.0 note: the whole
  base was panned in every direction to its edges and
  re-checked in this pass (north to Headquarters and
  the airport, west to the walled compound and the
  far-left coin buildings, southwest to the gold
  mines, south to the vehicle bays, east to the drill
  grounds and tents, and the center), and the closing
  verification found zero full or ready bubbles
  remaining in the main base. Panning failed in the
  zoomed central-pad view of the 2343 and 0016 units,
  but succeeded in this pass's framing, so the pan
  failure is framing-dependent, not universal.
- Armed Truck: checked in the base and south parking
  views during the sweep; no full / Collect bubble was
  seen over any vehicle, so there was no Armed Truck
  loot to claim in this pass.
- Regeneration rule reaffirmed: production regenerates
  continuously; three small regenerated rounds were
  collected during the sweep itself, and any
  micro-bubbles appearing after the closing screenshot
  belong to the next harvest pass by design (collect
  what is ready, do not chase regeneration).
- Session note, confirming the standing device rule:
  the game showed the "active on a different device"
  dialog at entry; Confirm was clicked once, the app
  exited and was reopened, and the pass continued on
  the Mac.

## What the 2026-11-01 2006 unit added

Unit harvest-2026-11-01-1803 by ticker-2006, status
partial. The game was already open on the Mac mini,
left on the Alliance Tech panel from an earlier unit.
The panels were closed without touching any donation
button, and the back arrow returned the view to the
base. Evidence in
`_records_/2026-11-01/resource-collection/2006-queue-run.md`.

- The first tap, on the centre bubble cluster,
  cleared the 5 visible base bubbles in one tap,
  matching the pattern of the 11:49 run the same day.
  HUD iron moved 18.7M to 19.1M, a plus 0.4M measured
  gain. Food stayed 353.1M, coin stayed 30.1M, stone
  stayed 543.9M at display rounding.
- A second tap at the one remaining centre bubble
  position selected the Titanium Alloy Factory No.3
  panel instead of collecting; no gain was verified
  from that tap, and the panel was closed by tapping
  empty ground. This is the same edge fall-through
  the center-tap rule guards against: a tap that
  misses a bubble centre can open the building
  underneath instead of collecting.
- Sweep state, why partial: the base was panned east
  and west. No further clear resource bubble was
  identified in either panned view. One partial bubble
  shape at the far left edge could not be
  distinguished from the left-column UI widgets and
  was deliberately not tapped. Rule from this unit:
  do not tap an ambiguous edge shape that cannot be
  distinguished from UI widgets.
- The bottom Season 2 area and the Armed Truck were
  not checked in this unit, so the full-map
  zero-remaining acceptance is not met. Both fall to
  the next harvest unit. The tracker is untouched, so
  the regular stays due.

## What the 2026-11-01 2356 unit added

Unit harvest-2026-11-01-2203 by ticker-2334, status
partial. The tracker is untouched, so the regular stays
due. Evidence in
`_records_/2026-11-01/resource-collection/2356-queue-run.md`.

- Entry: the game was left on the Rallied HP donation
  panel from the previous unit of the pass. The panel
  and the Alliance Techs tree were closed with their X
  buttons (no donation button touched), and the Alliance
  menu back arrow returned the view to the base.
- First base view (snowy northern strip): 4 green
  resource bubbles over the central buildings, visually
  grounded at norm 393,415, 293,466, 499,467 and
  394,518. One tap on the centre of the first bubble
  cleared all 4 at once - the third same-day instance
  of the centre-tap-clears-cluster pattern (11:49, 20:06
  and 23:56 runs). The white speech bubble near the
  central buildings is not a resource bubble and was
  not tapped.
- No gain figure is claimed: HUD totals read live
  before and after the tap (food 362.4M, iron 19.4M,
  stone 1.5M, coin 36.7M) did not move at the displayed
  0.1M precision, so the collected amount sits below
  the HUD display precision.
- Sweep state, why partial: the base was panned in one
  direction (drag norm 500,500 to 200,500). The panned
  strip showed no green resource bubble: only the white
  speech bubble and a red arrow marker over buildings.
  Not covered in this unit, so the 2026-11-01 full-map
  zero-remaining acceptance is not met: the opposite pan
  direction, the far-left edge partial bubble shape
  left unidentified by the 20:06 run, the Armed Truck
  loot state, and the bottom Season 2 area (whose
  bubbles do not count as main-base harvest under the
  2026-11-01 rule, but were still not inspected). All
  fall to the next harvest unit.

## What the 2026-11-02 0308 unit added

Unit harvest-2026-11-02-0203 by ticker-0308, session 03:08
to 03:17, status partial. The tracker is untouched, so the
regular stays due. Evidence in
`_records_/2026-11-02/resource-collection/0308-queue-run.md`.

- Entry: the game was left on the Alliance Techs panel from
  an earlier session. The panels were closed without
  donating (donations belong to their own unit) and the
  view returned to the base.
- Sweep: the visible main base bubbles were collected; one
  farmland tap collected all farmland at once, as
  documented. Iron, coin and food bubbles in the visible
  area were collected.
- HUD figures, rounded as displayed: food 366.2M before,
  373.3M after, plus about 7.1M; second top bar resource
  (iron) 558.8M before, 565.3M after, plus about 6.5M;
  coins 39.1M before, 43.7M after, plus about 4.6M.
  Figures are HUD-rounded millions, not exact panel
  readings.
- Why partial, not done: the full-map acceptance needs the
  base dragged to each edge with zero bubbles remaining.
  Remote drags barely panned the map (two attempts moved
  the view only slightly), so the extreme edges were not
  verified. The visible main base is bubble-free across
  two overlapping views, but the edge check is incomplete
  - a third instance of the remote-drag pan failure mode
  (see the 2343 and 0016 units). Next harvest unit: retry
  the edge drag with a longer drag on empty road, and
  re-check the armed truck loot bubble.
- Incidents, all closed without action: a bubble tap opened
  the Iron Mine upgrade panel (Lv.27 to 28 offer), closed
  with the panel X - no Upgrade, no Finish Now, no speedup
  used, no building started. A later tap opened the Store
  cosmetics Preview panel (Silverclaw Fighter), closed
  with the panel X and the Store back arrow - nothing
  bought, nothing equipped. A tap on the parked truck body
  produced no panel; the truck marker tap also produced
  no panel. The parked truck shows its marker but no
  collectable loot bubble, so it was left alone (not fully
  loaded, nothing claimed).
- The Season 2 area at the bottom was left out of the
  sweep, per the standing rule that it is not main base
  harvest.


## What the 2026-11-02 0741 unit added

- Unit harvest-2026-11-02-0603 by ticker-0734, session 07:35
  to 07:41, status partial. Tracker untouched, so the regular
  stays due. Evidence in
  `_records_/2026-11-02/resource-collection/0741-queue-run.md`.
- Entry: the game was left on the Alliance Techs panel from
  an earlier session, as in the 0308 unit. The panels were
  closed without donating (donations belong to their own
  unit); the Alliance screen back arrow needed three taps
  before it registered, the first two showing no change,
  the third returning to the base.
- Sweep: a visual grounding pass located 16 bubbles in the
  starting view, and bubble centres were tapped grounded on
  live screenshots. One tap selected the Iron Mine and one
  later tap selected the Coin Vault Lv.24; both were
  deselected with an empty-road tap, no panel action taken
  - fall-throughs on bubble taps, as documented, not
  collections.
- Pan: one long drag on empty road toward the right edge
  did move the view, and the panned right-side view showed
  no resource bubbles over its buildings - a longer drag
  succeeded where the 0308 unit's drags barely panned, so
  drag length, not the drag route, is the suspect in that
  failure mode. The view was dragged back to restore the
  starting view.
- HUD figures, rounded as displayed: food 383.9M before,
  387.0M after, plus about 3.1M (one farmland tap collected
  all farmland at once, as documented); second top bar
  resource 574.0M before, 576.9M after, plus about 2.9M;
  coins 48.7M before, 50.7M after, plus about 2.0M.
  Figures are HUD-rounded millions, not exact panel
  readings.
- Why partial, not done: the full-map acceptance needs zero
  bubbles remaining. The restored starting view still showed
  a few small bubbles over the left-side buildings,
  consistent with fast regeneration (bubbles regenerate
  within minutes of a collection), and the top and left
  edges were not dragged to their extremes. Next harvest
  unit: re-sweep the left-side buildings first, since
  regeneration lands there fastest, then drag to the top
  and left edges, and re-check the armed truck loot bubble.
- Armed truck: the parked truck shows its marker but no
  collectable loot bubble, so it was left alone (not fully
  loaded, nothing claimed), as in the 0308 unit.
- The Season 2 area at the bottom was left out of the sweep,
  per the standing rule that it is not main base harvest.

## What the 2026-11-02 1052 unit added

- Unit harvest-2026-11-02-1003 by ticker-1040, session 10:39
  to 10:52, status partial. Tracker untouched, so the regular
  stays due. Evidence in
  `_records_/2026-11-02/resource-collection/1052-queue-run.md`.
- Sweep: the visible main base was swept, tapping bubble
  centres grounded on live screenshots - one visual-grounding
  pass timed out without returning points, so the taps that
  followed were grounded on the screenshots themselves.
  First tap (left-side coin bubble, 50,405) collected coins;
  batched taps on a farmland bubble (325,470) and an iron
  bubble (140,300) collected food and iron with no panel
  opened.
- HUD figures, rounded as displayed: food 388.3M before,
  390.2M after, plus about 1.9M; second top-bar resource
  578.2M before, 580.0M after, plus about 1.8M; coins
  51.6M before, 52.8M after, plus about 1.2M. Figures are
  HUD-rounded millions, not exact panel readings.
- Armed truck: the parked armed truck area at the bottom of
  the base was checked; no collectable loot bubble over the
  parked vehicles, so nothing was claimed there (not fully
  loaded), as in the 0308 and 0741 units.
- Why partial, not done: the full-map acceptance needs zero
  bubbles remaining with the base dragged to each edge. The
  top and left edges were not dragged to their extremes, and
  small bubbles over the left-side buildings and the farmland
  were still present or regenerating at close (bubbles
  regenerate within minutes of a collection). The Season 2
  area at the bottom was left out of the sweep, per the
  standing rule that it is not main base harvest.
- Follow-up carried, not completed: the 0741 unit's
  next-unit instruction (re-sweep the left-side buildings
  first, then drag to the top and left edges, and re-check
  the armed truck loot bubble) is still open after this
  unit - the visible base was swept but the edges were
  again not dragged to their extremes, so the same
  instruction passes to the next harvest unit unchanged.

## What the 2026-11-02 1520 unit added

- Unit harvest-2026-11-02-1403 by ticker-1452, session
  about 15:11 to 15:20, status partial: the sweep
  barely started inside the pass budget, no bubble was
  collected, tracker untouched, so the next tick
  re-produces this regular. Evidence in
  `_records_/2026-11-02/resource-collection/1520-queue-run.md`.
- HUD figures measured at unit start: food 387.7M, iron
  577.5M, coins 54.0M, diamonds 2,536. Unchanged at
  close - no bubble was collected.
- Not-a-bubble lesson, new: the base-screen glow at
  norm 486,216 is the Operation Falcon campaign entry
  (Chapter 15), not a resource bubble. Tapping it
  opened the campaign map; no stage was entered, no
  battle started, nothing spent. Future sweeps must
  not tap this glow as a bubble.
- Return unverified: the campaign back arrow at norm
  62,988 was tapped and dispatched, but the control
  session dropped before a fresh screenshot could
  verify the return, so the final screen is recorded
  as unverified. The game was last seen on the
  Operation Falcon screen with the back-out tap
  dispatched and no action taken on that screen. The
  next unit screenshots first and navigates from
  wherever the game sits; no state was changed.
- What was not done: no resource bubble was collected,
  no edge drag was attempted, and the armed truck loot
  bubble was not checked. The full-map sweep (all
  bubbles to zero, Season 2 area excluded) is entirely
  outstanding for the next harvest unit.
- Session reliability note: computer-use sessions
  dropped repeatedly this pass (three restarts); each
  restart re-selected the Last War window without
  disturbing the game.
- Follow-up carried, not completed: the full-map sweep
  to zero bubbles, the armed truck loot bubble check,
  and screenshot-first navigation from an unverified
  screen all pass to the next harvest unit.

## What the 2026-11-02 1945 unit added

- Unit harvest-2026-11-02-1803 by ticker-1934, session
  about 19:34 to 19:45, status partial: one bubble
  collected, the full-map sweep not complete, tracker
  untouched, so the next tick re-produces this regular.
  Evidence in
  `_records_/2026-11-02/resource-collection/1945-queue-run.md`.
- Entry: the game was found on the Events screen (Unit
  Progression); the bottom-left back button at norm
  157,947 returned the game to the base view.
- HUD measured at unit start: food 226.5M, second
  top-bar resource 561.8M, coins 5.9M (HUD-rounded
  figures as displayed). A farmland bubble at norm
  280,535 collected: food 226.5M to 227.1M, about plus
  0.6M - one farmland tap collects all farmland bubbles
  at once, re-confirming the standing rule. These
  figures differ from the 1723 snapshot the same day
  (food 387.7M, iron 577.5M, coins 54.0M); the change
  is measured but its cause is not established by this
  record, so no spend is claimed here.
- Not-a-bubble lessons, two new: norm 215,465 in the
  pre-drag view selects an Iron Mine Lv.27 building
  (no HUD change); norm 145,265 in the post-drag view
  opens the Survivor List panel (Overview/All/Dispatch)
  and no survivor was dispatched or changed. With the
  1520 campaign entry at norm 486,216, three points
  are now known not to be bubbles. Future sweeps must
  ground bubble centres on a fresh screenshot and must
  not re-tap these three points as bubbles.
- Deselect note: an empty-ground tap at norm 600,700
  deselected with no building action. Drag note: the
  base dragged rightwards (norm 300,500 to 700,500)
  exposed the left/top edge.
- What was not done: the full-map sweep to zero
  bubbles was not completed; the left-side gold/stone
  building bubbles (experience, screw bubbles) and the
  armed truck loot bubble were not verified or
  collected; the Season 2 area at the bottom was left
  out of the sweep, per the standing rule that it is
  not main base harvest.
- Session reliability note: the computer-use session
  dropped once during the unit and was restarted
  without disturbing the game.
- Follow-up carried, not completed: the full-map
  sweep, the armed truck loot bubble check and the
  left-side bubbles pass to the next harvest unit.


## What the 2026-11-02 2247 unit added

- Unit harvest-2026-11-02-2203 by ticker-2234, session
  about 22:42 to 22:47, status partial. Evidence in
  `_records_/2026-11-02/resource-collection/2247-queue-run.md`.
- Base HUD at unit start, rounded as displayed: food
  230.0M, second top-bar resource 564.7M, coins 5.9M,
  second-row first resource 18.3M, second-row second
  resource 504.7K. A computer session drop mid-pass
  was restarted without disturbing the game, and the
  base view was intact.
- Four green bubbles grounded on the starting
  screenshot over the central building cluster, at
  norm (396,416), (292,468), (499,468) and (397,516).
  All four centres were tapped in one batch. No panel
  was opened except that the closing tap left a
  building highlighted (Titanium Alloy Factory No.1
  Lv.30 label); an empty-ground tap at norm
  (600,700) deselected it. No Upgrade, no Finish Now,
  no speedup, nothing bought.
- HUD after the batch, rounded: food 230.0M, second
  top-bar 564.7M, coins 5.9M, second-row first
  resource 18.7M (up about 0.4M from 18.3M),
  second-row second 504.7K. Food, iron and coin
  figures did not move at HUD rounding, so the
  collected amount is recorded only as the
  second-row movement plus the four bubbles cleared,
  not as an exact total.
- Sweep remainder, why partial: the right-panned view
  (drag 300,500 to 700,500) showed no bubbles, and
  the restored starting view again showed none, but
  the top and left extremes were not dragged to
  their limits, and bubbles regenerate within
  minutes of a collection, so a whole-map
  zero-remaining claim is not proven. Armed truck
  check: the parked vehicles at the top right showed
  no collectable loot bubble, so nothing was claimed
  there (not fully loaded). Season 2 area at the
  bottom was left out of the sweep, per the standing
  rule that it is not main base harvest.
- Follow-up for the next harvest unit, carried
  unchanged: re-sweep the left-side buildings first
  (regeneration lands there fastest), drag to the
  top and left edges, and re-check the armed truck
  loot bubble. Tracker untouched, so the next tick
  re-produces this regular.


## What the 2026-11-03 0244 unit added - four central bubbles, left edge still undragged

- Unit harvest-2026-11-03-0203 by ticker-0234, about 02:44
  local, status partial. Evidence in
  `_records_/2026-11-03/resource-collection/0244-queue-run.md`.
- Entered from the Alliance Techs panel left over from
  the donations unit: closed the tech panel, closed
  Alliance Techs, tapped the Alliance menu back arrow to
  reach the base view. Nothing else tapped on the way;
  no other activity's rewards claimed.
- Base HUD at unit start, rounded as displayed: food
  230.7M, second top-bar resource 565.3M, coins 5.9M,
  second-row first resource 18.7M, second-row second
  resource 505.1K. Power 149,940,141.
- Four green resource bubbles grounded on the starting
  screenshot over the central building cluster, at norm
  (396,399), (294,455), (497,458) and (397,510): the same
  four-position central cluster as the 2026-11-02 2247
  unit, with small coordinate drift by framing (2247
  read (396,416), (292,468), (499,468), (397,516)), so
  the cluster is near-identical, not exactly re-pinned.
  All four centres were tapped in one batch. No panel
  opened; the closing tap left a building highlighted
  (Titanium Alloy Factory No.1 Lv.30 label), deselected
  with an empty-ground tap at norm (600,700). No Upgrade,
  no Finish Now, no speedup, nothing bought.
- HUD after the batch, rounded: food 230.7M, second
  top-bar 565.3M, coins 5.9M, second-row first resource
  19.0M (up about 0.3M from 18.7M), second-row second
  505.1K. The food, iron and coin figures did not move
  at HUD rounding, so the collected amount is recorded
  only as the second-row movement plus the four bubbles
  cleared, not as an exact total.
- Sweep remainder, why partial: dragged the base
  (300,500 to 700,500) and the panned view showed the
  right-side buildings with no green resource bubbles;
  dragged back and then vertically (500,300 to 500,650)
  and the top-edge view showed the farmland plots and
  their small crop icons plus two question-mark figures,
  but no green collectible bubbles. The left edge was
  not dragged to its limit, and bubbles regenerate
  within minutes of a collection, so a zero-remaining
  claim for the whole map is not proven. The top edge
  is now checked (it was undragged in the 2247 unit), so
  the remainder narrows to the left edge.
- Armed truck check: the parked vehicles at the top
  right of the base showed no collectable loot bubble in
  the starting view, so nothing was claimed there (not
  fully loaded). Season 2 area at the bottom was left
  out of the sweep, per the standing rule that it is not
  main base harvest.
- Follow-up for the next harvest unit, carried with the
  left-edge-first order: drag to the left edge first,
  re-check the central cluster for regenerated bubbles,
  and re-check the armed truck loot bubble. Tracker
  untouched, per the rule for partial units; the next
  tick re-produces harvest and resumes the sweep.

## What the 2026-11-03 0642 unit added - central, left and top bubble-free, right edge unswept so partial

- Ticker-0634, unit harvest-2026-11-03-0603, about 06:42
  local, status partial. Evidence in
  `_records_/2026-11-03/resource-collection/0642-queue-run.md`.
- Entered from the radar screen (previous unit in this
  pass): the radar back arrow returned to the base view.
- Base HUD at unit start and close, rounded as displayed,
  unchanged: food 230.7M, second top-bar resource 565.3M,
  coins 5.9M, second-row first resource 19.0M, second-row
  second resource 505.1K. Power 149,940,141, stamina 120.
- Sweep: central cluster bubble-free at the four positions
  cleared by the 0244 unit, nothing tapped there.
  Left-edge follow-up from 0244 done: dragged (700,500
  to 300,500) to the neighbouring-base cluster west of
  the own base, no own-building resource bubble visible
  there; dragged back (300,500 to 700,500) to the central
  view. Top edge: dragged (500,300 to 500,650); the upper
  base area (farmland plots, upper buildings, parked
  helicopter) showed no green collectible bubble;
  dragged back (500,650 to 500,300) to the central view.
- Armed truck: no fully-loaded loot bubble was seen in
  any view swept, so nothing was claimed there, but the
  truck's loaded state was not separately verified with
  a dedicated tap and no vehicle panel was opened.
  Season 2 area at the bottom was left out of the sweep,
  per the standing rule that it is not main base harvest.
- Why partial, not done: the full-map acceptance needs
  zero bubbles remaining with the base dragged to each
  edge. Central, left-edge neighbouring cluster and top
  edge are bubble-free in this unit, but the right edge
  was not swept in this unit and the armed truck loot
  state was not separately verified, so a whole-map zero
  claim is not proven. Tracker untouched, per the rule
  for partial units; the next tick re-produces harvest
  and resumes the sweep.
- Follow-up for the next harvest unit, carried with the
  right-edge-first order: sweep the right edge first,
  re-check the central cluster for regenerated bubbles,
  and verify the armed truck loot bubble explicitly. The
  0244 left-edge-first carry is now closed.

## Open questions

- The capacity cap per building, and how long until output stops
  accumulating when bubbles are left uncollected.
- The drone component bubble's spot: still unidentified after
  the 1534 pass (the 164,116 top-left-corner candidate is
  unverified); the next harvest pass must locate it on screen
  rather than assuming the candidate.
- Why HUD food and iron totals rise between harvest units with no
  harvest record between: the 1935 unit flagged food +3.2M and
  iron +3.1M for 18:00-19:50, and the 2310 unit measured food
  +2.8M, iron +2.8M, coin -0.1M for 19:50-23:12 with no
  intervening harvest record. Tracked as GitHub Issue #490
  (labels records). Until resolved, HUD deltas across units are
  not clean harvest measurements. (Added 2026-11-08 2310.)

- Whether bubble collection is per-type (one tap clears every standing bubble of that resource type) or per-bubble, and under what standing conditions the 1935 one-tap-one-bubble read occurs: the 0340 unit cleared all visible bubbles of each type in one tap per type (iron 4, coin 3, EXP 4, food), contradicting the 1935 iron one-by-one re-confirmation, with HUD deltas exceeding the visible sums. Tracked as knowledge Issue #502 (labels knowledge). (Added 2026-11-09 0340. 2026-11-09 0636 update: second independent confirmation - one tap per type cleared all bubbles of each type again; the profile now treats one-tap-per-type as the standing rule with the 1935 read as the single outlier; Issue #502 stays open, closure belongs to the daily retro.)

- What the blue-triangle 596 bubbles over the furnace buildings are: four yellow-circle bubbles with a blue triangle icon, each labelled 596, stand over the orange-glowing furnace buildings; one tap cleared all four at once with no HUD total moving. Candidates, unverified: oil from the Age of Oil event (the oil total may live on the event page, not the HUD) or a furnace output that lands in inventory. Tracked as knowledge Issue #508 (labels knowledge). The next harvest unit reads the furnace building panel and, if it is oil, the Age of Oil event page, and states whether these bubbles belong in the zero sweep. (Added 2026-11-09 0636.)

## Changelog

- 1.46.0 (2026-11-09): 0636 harvest unit folded (partial, one tap per type cleared all bubbles of that type a second time - food 5 bubbles +2.0M, coin 5 bubbles +1.3M, iron 4 read bubbles +1.9M HUD, all HUD-verified in-unit - so one-tap-per-type is now the standing rule with the 1935 one-tap-one-bubble read as the single unexplained outlier; Issue #502 stays open pending the daily retro's closure decision; four blue-triangle 596 bubbles over the furnace buildings cleared on one tap with no HUD move, resource unidentified, filed as knowledge Issue #508; gold circle with blue gem above the blue truck is a radar shortcut showing 6 claimable task rewards, not the truck loot, cross-noted in radar-tasks 1.58.0; EXP bubble about 490K at the far left edge partly off-screen and the Armed Truck loot check are first actions of the next harvest unit; fresh coin bubbles about 8K each stood again within minutes, regeneration is not chased).

- 1.45.0 (2026-11-09): 0340 harvest unit folded (partial, one tap per resource type cleared all visible bubbles of that type - iron 4 bubbles +4.9M, coin 3 bubbles +4.3M, EXP 4 bubbles, food +5.4M, all HUD-verified in-unit; this CONTRADICTS the 1935 iron one-by-one re-confirmation, so iron and coin one-by-one are marked suspect again, not settled, and the mechanism question is filed as knowledge Issue #502 with a base-wide-collection candidate NOT verified; recenter-first sweep EXECUTED for the first time, discharging the 0202 owed item - centred view showed no bubbles, one long drag west reached the resource quarter, green ticks on iron-mine buildings are status markers not bubbles (3x crop); HUD deltas exceed visible bubble sums; Armed Truck loot-panel entry still unlocated, Season 2 excluded per rule; remainder to the next unit).

- 1.44.0 (2026-11-09): 0202 harvest unit folded (partial, 0 bubbles collected, no resource bubble with a value label in either of two base views, the resource quarter never reached - same wall as the 2310 unit; the recenter-first sweep ordered by the 2310 follow-up was NOT executed in this unit either, it swept troop areas again, so the method change is still owed; no HUD rise this unit, the Issue #490 phenomenon did not recur; white truck (55,652) opens the Secret Command Post, Armed Truck loot-panel entry still unlocated and its loot state unverified; skull timer re-seen with badge 4 and a 00:00:23 countdown rising to about 00:00:40, Issue #498).

- 1.43.0 (2026-11-08): 2310 harvest unit folded (partial, 0 bubbles collected, three blind pans never found the bubble cluster; two new verified non-bubbles - norm 701,468 gold diamond is the zombie NPC marker opening the Area No.168 dialogue, norm 565,636 orange sack is the Recon Plane Lv.24 indicator; method change under R2 - recenter the base view FIRST, then sweep systematically, tap only a bubble whose icon and value label are both readable; HUD rise second occurrence food +2.8M iron +2.8M coin -0.1M vs the 1935 close with no intervening harvest record, now GitHub Issue #490 and an open question; coin bubbles (132,436) and (234,452) plus one iron bubble still standing and not re-found; armed-truck loot still unverified, remainder to the next unit).

- 1.42.0 (2026-11-08): 1935 harvest unit folded (partial, food +5.1M one-tap all-at-once and iron +1.2M one-tap one-bubble HUD-verified; iron one-by-one RE-CONFIRMED so the 1759 suspect marking on iron is lifted and its identical +3.6M is explained in part as two different bubbles holding similar amounts; coin tap missed its bubble and hit the Iron Mine building, so coin one-by-one stays suspect and rule R2 now requires zooming in or a readable coin icon plus value label before tapping, with the 1935 coin centre candidates marked unverified; wrong tap at 490,352 opened a UR Trade Truck panel, closed untouched; pre-unit HUD rise food +3.2M iron +3.1M since 18:00 unexplained with no intervening harvest record; armed-truck toast fragment still unread; coin bubbles and at least one iron bubble still standing, remainder to the next unit).

- 1.41.0 (2026-11-08): 1759 harvest unit folded (partial, pre-reset sweep cut short by the 18:00 reset arriving mid-sweep; iron +3.6M and coin +3.6M HUD-verified in two taps, food bubbles still standing; both taps aimed at supposed food bubbles collected a different resource, so bubble-type identification from the downscaled screenshot is unreliable and rule R2 now requires verifying the bubble's identity before tapping; the identical +3.6M on both taps is recorded unexplained with an all-at-once per-type mechanism as unverified inference, and the 2026-10-25 one-by-one line for iron and coin is marked suspect, not deleted; armed-truck toast fragment still unread; remainder to the 1803 unit).

- 1.28.0 (2026-11-05): fortieth consecutive Mac device-access blocker (0904 harvest unit, invoke-channel stall, zero responses to eight invokes across two devices and five commands - a new worsened form, distinct from Issue 284's capture-failure-with-responses signature); the Correction 2026-11-05 unblock (owner Dock-icon click) is scoped to the window-stream fault only and does NOT address a stalled invoke channel, for which the Mac-side agent gateway likely needs a restart (unverified); the 1101 harvest close stands as the last live read, full edge-drag sweep still incomplete, Armed Truck state unknown; fortieth occurrence commented onto Issue #282 by this run.

- 1.37.0 (2026-11-07): channel rules carried (propagation follow-up from the 1732 run): the 1020 Mission Control lesson - open_app Mission Control wedged the channel (geometry_mismatch, input gated on observation_required, second launch restores) and background Ctrl+Right does not switch Spaces; the background-Space-keys half was already in this profile from its own 0034 unit, the open_app wedging is the new part; the Dock-icon unblock stands. (1.29.0 through 1.36.0 carry sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.38.0 (2026-11-07): 1941 harvest unit folded (partial, farmland +1.9M food and +1.2M coin verified by HUD deltas, iron +1.7M observed unattributed - possibly furnace overdrive production, recorded as an observed HUD change only, not a collection claim; estimated bubble centres failed twice so ground-then-tap is now the standing rule; gold truck icon tap at norm 681,814 panned to the Drill Ground instead of opening a loot panel, so the icon is not a verified loot entry and the Armed Truck loot stays unverified; blue top-of-base bubbles and gold star over the cannon untapped, Season 2 zone unchecked, full-map zero-remaining acceptance not met, next unit resumes from the panned-down Drill Ground view; HUD food 476.8M to 478.7M, iron 800.4M to 802.1M, coin 5.7M to 6.9M, stone 25.0M, 922.2K, power 149,850,353, stamina 105 to 106).

- 1.27.0 (2026-11-05): thirty-second consecutive capture failure (0434 harvest unit, 5 attempts across cc-518 and cc-519, probe OFF_SCREEN_WINDOW high confidence, Chrome observes normally in cc-520, View-menu probe step missing because describe is capture-blocked, recovery still the owner Dock-icon click or mac_lastwar_front.sh); the 1101 harvest close stands as the last live read, full edge-drag sweep still incomplete, Armed Truck state unknown; thirty-second occurrence commented onto Issue #282 by this run.

- 1.26.0 (2026-11-05): Correction from the 0134 survivors and 0204 gifts records - the game window is windowed 1920x1080 on an inactive Space, not in native fullscreen (View menu lists Enter Full Screen, read on-screen in session cc-505 and re-confirmed by a repeated probe in cc-508); the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission; the "running fullscreen" wording in the 1634, 2104 and 0034 sections is superseded, and the 0034 "menu path View -> Exit Full Screen" with it; the permission/pipeline-restart follow-up is replaced by the window-back-on-active-Space unblock (owner Dock-icon click); background Space keys do not switch Spaces, set_window_frame is stale-observation-gated, Cmd+Tab is blocked, list_windows needs the exact app name "LastWar"; the 1101 harvest close stands as the last live read; twenty-sixth and twenty-seventh occurrences commented onto Issue #282 by this run. (1.23.0, 1.24.0 and 1.25.0 carry the 1634, 2104 and 0034 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.22.0 (2026-11-04): farmland +2.1M food (417.9M to 420.0M) and left-side +1.4M coin (18.0M to 19.4M) verified by HUD deltas, farmland one-tap-clears-all and the 0755 left-side point (88,406) re-confirmed, Alliance back arrow (161,935) and panel X closures (848,213) and (848,150) re-confirmed, donations timer 00:11:45 corroborating the 1046 timer running, right side and top edge unswept and EXP, screw and drone-component bubbles unlocated so the full edge-drag sweep stays incomplete, marker confusion caution (Issue #250) carried with no new failure mode, folded from the 1101 harvest unit; no earlier claim superseded. (1.20.0 and 1.21.0 carry the 0413 and 0755 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.19.0 (2026-11-04): server maintenance blocking login (0034 unit failed, 0 bubbles, no base view reached), disconnected dialog distinguished from maintenance dialog (disconnected Confirm quits the app, maintenance Confirm safe to retry and login impossible only while maintenance is active), sweep now two units behind after the partial 2034 unit, folded from the 0034 harvest record with the 0110 survivors record as the clearing corroboration; no earlier claim superseded.

- 1.18.0 (2026-11-03): one verified teal-bubble collection
  (+1.6M second-row resource, name unclaimed), factory-top
  grounding confusion at (435,442) and (501,532) selecting
  Titanium Alloy Factory No.1 and No.3 Lv.30 (Issue #250),
  season-entry white bubble at (485,575) toast-only, entry
  Techs-panel closures and the donations-counter attribution
  caution, full edge sweep and armed-truck loot still
  outstanding, partial blocker category b, folded from the
  2034 harvest unit; no earlier claim superseded.

- 1.17.0 (2026-11-03): batch taps over left-side buildings
  and farmland mixed bubble centres with building panels
  (Gear Factory Lv.20 to 21 and Iron Mine Lv.27 panels
  opened and closed untouched, farmland bubbles still
  visible), so 0 collections verified and HUD unchanged at
  rounding (food 251.1M, iron 592.7M, coins 17.4M, power
  149,948,901); full edge sweep, Season 2 area and armed
  truck loot unchecked so partial, blocker category c;
  next unit must re-measure bubble centres fresh before
  tapping; the 1044 left/top-first follow-up carries
  forward, not closed; folded from the 1524 harvest unit;
  no earlier claim superseded.

- 1.12.0 (2026-11-02): one farmland bubble collected (food plus about 0.6M, one-tap-clears-all re-confirmed), two new not-a-bubble points (215,465 Iron Mine Lv.27 building, 145,265 Survivor List panel) joining the 1520 campaign entry, HUD measured food 226.5M, second resource 561.8M, coins 5.9M with the change since the 1723 snapshot unexplained in the record, full-map sweep and armed truck loot check outstanding, folded from the 1945 harvest unit; no earlier claim superseded.

- 1.11.0 (2026-11-02): sweep barely started so partial with no bubble collected, base-screen glow at norm 486,216 identified as the Operation Falcon campaign entry and not a bubble, campaign back-out dispatched but return unverified after a session drop so the next unit screenshots first, full-map sweep and armed truck loot check entirely outstanding, HUD measured food 387.7M, iron 577.5M, coins 54.0M, diamonds 2,536, folded from the 1520 harvest unit; no earlier claim superseded.

- 1.10.0 (2026-11-02): visible-base sweep with HUD-rounded gains (food +1.9M, second resource +1.8M, coins +1.2M), screenshot-grounded taps after a grounding timeout, parked truck with no loot bubble left alone, edges again undragged so partial with the 0741 follow-up carried unchanged, folded from the 1052 harvest unit; no earlier claim superseded.

- 1.9.0 (2026-11-02): visible-base sweep with HUD-rounded gains (food +3.1M, second resource +2.9M, coins +2.0M), 16 bubbles grounded in the starting view, long-drag right-edge pan succeeding where the 0308 drags barely moved, fast regeneration over the left-side buildings so partial, parked truck with marker but no loot bubble left alone, folded from the 0741 harvest unit; no earlier claim superseded.

- 1.6.0 (2026-11-01): centre-cluster one-tap five-bubble clearance with iron plus 0.4M measured, Titanium Alloy Factory No.3 panel fall-through on the second tap, ambiguous far-left edge shape deliberately untapped, Season 2 bottom area and Armed Truck checks deferred to the next harvest unit, folded from the 2006 harvest unit; no earlier claim superseded.

- 1.7.0 (2026-11-02): centre-tap four-bubble cluster clearance as the third same-day instance, no gain claimed at 0.1M HUD precision, and the carried sweep remainder (opposite pan, far-left edge shape, Armed Truck, Season 2 area), folded from the 2356 harvest unit.

- 1.8.0 (2026-11-02): visible-base sweep with HUD-rounded gains (food +7.1M, iron +6.5M, coins +4.6M), remote-drag edge check incomplete so partial, Iron Mine upgrade and Store cosmetics panels closed untouched, parked truck with marker but no loot bubble left alone, folded from the 0308 harvest unit; no earlier claim superseded.

- 1.3.0 (2026-11-01): balloon-versus-bubble distinction, HUD
  button mis-tap point, base-view pan failure mode, and the
  2343 negative result, folded from the 2343 harvest unit and
  the 0016 survivors unit; no earlier claim superseded.
- 1.4.0 (2026-11-01): five-bubble inventory with the
  one-tap-clears-all farmland confirmation, the HUD
  rounding precision note, and the Armed Truck check
  deferred to the next harvest unit, folded from the 1149
  harvest unit; no earlier claim superseded.
- 1.5.0 (2026-11-01): full-base bubble location map with
  batch-collection rules (farmland, screws row, west compound,
  truck completion flow), the full-bubble urgent-claim rule,
  the bubble-versus-icon distinction, the framing-dependent
  pan correction, the Season 2 area distinction, and the
  disclosed drone-bubble executor miss, folded from the 1534
  urgent harvest unit; the 1.3.0 pan-failure claim is
  qualified, not erased, and the drone spot stays an open
  question.

- 1.13.0 (2026-11-02): four central-cluster bubbles cleared in one batch at (396,416), (292,468), (499,468) and (397,516), second-row first resource up about 0.4M at HUD rounding with food, iron and coins unmoved at rounding, right-panned and restored views bubble-free but top and left extremes undragged so partial, armed truck with no loot bubble left alone, Season 2 area excluded per standing rule, left-side-first re-sweep carried to the next unit, folded from the 2247 harvest unit; no earlier claim superseded.

- 1.14.0 (2026-11-03): four central-cluster bubbles cleared in one batch at (396,399), (294,455), (497,458) and (397,510), second-row first resource up about 0.3M at HUD rounding with food, iron and coins unmoved at rounding, right-panned and top-edge views bubble-free but the left edge undragged so partial, armed truck with no loot bubble left alone, Season 2 area excluded per standing rule, left-edge-first re-sweep carried to the next unit, folded from the 0244 harvest unit; no earlier claim superseded.

- 1.15.0 (2026-11-03): central cluster bubble-free at the four positions cleared by the 0244 unit with nothing tapped, left-edge follow-up from 0244 done (drag 700,500 to 300,500 to the neighbouring-base cluster west of the own base, no own-building bubble), top edge bubble-free (drag 500,300 to 500,650, farmland plots, upper buildings, parked helicopter), HUD unchanged at rounding (food 230.7M, second top-bar resource 565.3M, coins 5.9M, second-row first resource 19.0M, second-row second resource 505.1K, power 149,940,141, stamina 120), right edge not swept and armed truck loot state not separately verified so partial with tracker untouched, Season 2 area excluded per standing rule, right-edge-first re-sweep with explicit armed-truck loot verification carried to the next unit (the 0244 left-edge carry is now closed), folded from the 0642 harvest unit; no earlier claim superseded.


## What the 2026-11-03 1044 unit added - central and right-bottom bubble-free, 0 collected, left and top unswept since 0642

- Ticker-1034, unit harvest-2026-11-03-1003, about
  10:36 to 10:44 local, status partial. Evidence in
  `_records_/2026-11-03/resource-collection/1044-queue-run.md`.
- Entry, left open by the previous pass: the game was
  NOT on the base view at unit start - the Alliance
  Tech detail panel for Rallied Defense (7/10) was
  left open by ticker-1004, coin Donate button greyed
  with its timer at 00:02:53. Nothing was donated
  here; that panel belongs to the donations unit.
  The panel X closed to the Alliance Techs list,
  whose X revealed the Alliance main panel ([AP3x]
  The Apex, 94/100 members, power 13,091,657,850),
  and its back arrow returned to base. Help and
  Alliance Gifts red dots were visible in that panel
  and were left untouched as other units work.
- HUD at unit start and close, rounded as displayed,
  unchanged: food 240.3M, second top-bar resource
  575.0M, coins 12.1M, second-row first resource
  19.0M, second-row second resource 505.1K, power
  149,948,901, stamina 120.
- Central cluster (starting view and restored view):
  no green resource bubble over any building, nothing
  tapped, nothing collected. Right-edge follow-up
  from the 0642 unit: a first drag (300,500 to
  700,500) produced no visible view change; the
  reverse drag (700,500 to 250,500) panned to the
  right-bottom base area (gold HQ, radar towers,
  troop tents, Season 2 structures at the bottom
  right). No green bubble in that view either.
  Dragged back (250,500 to 700,500) to central.
- Armed truck loot check: the parked trucks in the
  central view (red and blue trucks by the lower
  gate) and the blue truck by the gold HQ in the
  panned view showed no green loot bubble, so
  nothing was claimed there (not fully loaded). The
  loot state was verified visually only; no truck
  panel was opened. The Season 2 area at the bottom
  was left out of the sweep, per the standing rule
  that it is not main base harvest.
- Why partial, not done: the full-map acceptance
  needs zero bubbles with the base dragged to each
  edge. Central and right-bottom are bubble-free in
  this unit, but the left edge and top edge were last
  swept by the 0642 unit, not this one, and bubbles
  regenerate within minutes of a collection, so a
  whole-map zero claim is not proven. Tracker
  untouched, per the rule for partial units.
- Follow-up for the next harvest unit, order flipped
  from the 0642 carry: sweep the left edge and top
  edge first, re-check the central cluster for
  regenerated bubbles, and re-check the armed truck
  loot bubble. No earlier claim superseded.

## What the 2026-11-03 1524 unit added - batch taps mixed bubbles with building panels, 0 verified collections

- Ticker-1504, unit harvest-2026-11-03-1403, about
  15:05 to 15:24 local, status partial. Evidence in
  `_records_/2026-11-03/resource-collection/1524-queue-run.md`.
- Entry: the game was left on the Radar tasks screen from
  the previous unit; returned to base with the grounded
  home button.
- Base HUD read live at close: food 251.1M, iron 592.7M,
  coin 17.4M, diamonds 12.72K, total power 149,948,901.
  These figures are unchanged at displayed precision
  from the unit start, so no collection amount is
  verified for this unit. The power read matches the
  1044 HUD read exactly; it is a repeated measurement,
  not a correction.
- Bubbles tapped: one single tap, then a batch of eight
  taps, on the gold circles visible over the left-side
  buildings and farmland (measured centres in the unit,
  e.g. [234, 363], [164, 394], [304, 400], [382, 394]).
  No panel opened for the single tap, but the batch
  ended on a building panel, and the farmland bubbles
  were still visible afterwards, so the taps cannot be
  counted as verified collections. Lesson, stated as the
  next unit's method (R2 pivot): the batch-tap method
  used here mixed bubble centres with building panels;
  the next unit must re-measure bubble centres fresh
  from a new screenshot before tapping, and must not
  batch taps across bubble and building targets.
- Building panels opened by mistake and closed without
  action: Gear Factory Lv.20 to 21 (Upgrade and Finish
  Now NOT tapped, per the red lines) and Iron Mine Lv.27
  (Output/hr +115325, Max Production Time 11hr 36min,
  survivors Charles, Jolene, Alyssa, Harry, all Miner;
  Quick Dispatch NOT tapped). No building, research or
  assembly action was taken; no diamonds or money spent.
- Full sweep NOT completed: the base was not dragged to
  its edges in all directions, the Season 2 area bubbles
  and the armed truck loot were not checked, and no
  bubble count was closed live. This unit is partial,
  never done. Tracker untouched, per the partial rule.
- Blocker category: c (tap method - bubble centre versus
  building panel confusion at this zoom).
- Follow-up carried, not closed: the 1044 follow-up
  (sweep the left edge and top edge first, re-check the
  central cluster for regenerated bubbles, re-check the
  armed truck loot bubble) was NOT done by this unit and
  carries forward, now with the added fresh-measure
  requirement above and the full edge-to-edge sweep
  before closing. No earlier claim superseded.

## What the 2026-11-03 2034 unit added - one verified +1.6M second-row collection, factory-top grounding confusion, season icon not a bubble

- Ticker-2034, unit harvest-2026-11-03-1803, about
  20:50 to 21:05 local, status partial. Evidence in
  `_records_/2026-11-03/resource-collection/2034-queue-run.md`.
- Entry, left open by the previous pass: the Alliance
  Techs panel was open, left over from the 2004
  donations unit. The inner detail closed at (855,195),
  the Techs list at (854,146), the Alliance screen
  with its back arrow at (140,915). Nothing was
  donated here. The Donation Count 2/30 read at entry
  belongs to the donations unit, not this one - do not
  fold another unit's counter into a harvest read.
- HUD at entry, read live: food 275.0M, iron 612.5M,
  coin 34.2M, second-row resource 19.0M, second-row
  second resource 505.1K, total power 149,948,901.
  The power read matches the 1044 and 1524 reads
  exactly; it is a repeated measurement, not a
  correction.
- One verified collection: the first-view teal bubble
  tap at (397,413) moved the second-row resource from
  19.0M to 20.6M (+1.6M, HUD read live on the next
  screenshot). No resource name is claimed for that
  row; the record states only the row and the delta,
  so this profile claims only the row and the delta.
- Factory-top confusion, a new failure mode (Issue
  #250, tooling): grounding points (435,442) and
  (501,532) for "small circular resource bubble above
  a building" selected Titanium Alloy Factory No.1 and
  No.3 (both Lv.30) instead. Factory-top markers look
  like bubbles to the grounding pass. Both selections
  were cleared by tapping empty ground (200,780); no
  panel was opened, nothing was built or spent.
  Method, carried to the next unit: verify every tap
  against HUD movement, and treat grounding hits over
  factory rows as suspect.
- Season icon, not a bubble: the white bubble above
  the central house cluster, tapped at (485,575),
  produced only the toast "Game season event not yet
  started or has ended" and stayed on screen. It is a
  season entry icon, not a collectible bubble; do not
  re-tap it as harvest.
- Why partial, not done: the Nov 1 full edge-drag
  sweep was not completed - the left-side coin and
  stone buildings, the drone-component bubbles and
  the armed-truck loot check were not reached inside
  the unit cap. The pass opened with own-PR work
  (PR 207's branch-side conflict resolution), blocker
  category b. The "ready to depart again" tooltip near
  the top of the base view was not probed; truck work
  belongs to the trucks unit. Tracker untouched, per
  the rule for partial units.
- Follow-up for the next harvest unit, carried not
  closed: the 1044 and 1524 follow-ups (left edge and
  top edge first, central re-check, armed-truck loot
  verification, fresh-measure bubble centres before
  tapping) still outstanding, now with the factory-row
  caution from Issue #250 first. No earlier claim
  superseded.

## What the 2026-11-04 0034 unit added - server maintenance blocks login, two dialogs distinguished

- Failed, 0 bubbles: the ticker-0034 harvest pass never reached a base view. At entry the game showed a "Server disconnected. Please restart the game." dialog whose Confirm quit the app (the known crash path for that dialog, state intact), then on relaunch a SYSTEM ANNOUNCEMENT "Update complete, please restart the game." (Version 1.0.366 (908), Asset Version 2167.1512...), then the login screen behind a TIPS dialog "The server is under maintenance. Please wait a moment, we'll be back with you shortly!" with a "Login failed. Please retry or contact support." footer. Two Confirm retries about 4 minutes apart (second at the OCR-grounded point (634,568)) left the dialog unchanged: login is impossible while maintenance is active. This is a game-server state, not a device-access failure and not the different-device dialog.
- Do not conflate the two dialogs: the disconnected dialog's Confirm exits the app; the maintenance dialog's Confirm is safe to retry - the 0110 survivors pass later the same night shows it dismissing to the loading screen once maintenance lifted (by about 01:04), so the retry-next-tick handling already in the loop is the correct response, and re-attempting another unit inside the same blocked pass only repeats the wall.
- The full edge-drag sweep of the Nov 1 rule was not started (left-side coin and stone buildings, drone-component bubbles, EXP and screw bubbles, armed-truck loot check all unreached); with the 2034 unit already partial, the sweep is now two units behind. No HUD figure was read, no diamonds or money touched, tracker untouched. No earlier claim superseded; no new issue filed - maintenance is transient external state, not a queue failure mode.

## What the 2026-11-04 0413 unit added - farmland verified again, factory-row marker confusion repeated

- Partial, ticker-0404, unit harvest-2026-11-04-0203 (game work about 04:06 to 04:13 local). Base reached via the world-map back arrow after two home-icon taps did not switch views. HUD at entry (live reads): food 395.0M, iron 732.0M, coin 3.1M, second row 21.0M and 922.2K, total power 150,028,269, diamonds 12.72K.
- Verified again: one farmland bubble tap at (395,415) moved food 395.0M to 397.0M (+2.0M, HUD read live on the next screenshot), reaffirming that one farmland tap collects all farmland bubbles at once.
- Marker confusion, Issue #250 evidence (already commented on #250 by the ticker pass, so no duplicate comment here): the gold circles and small icons above the iron-mine and factory row are building markers, not collectible bubbles, at this screenshot resolution. Taps at (148,405) on a left-side marker and (86,315) on the small icon floating above the leftmost blue building moved no HUD figure; taps at (833,391), (369,273), (389,363) and (467,405) selected Headquarters Lv.30, Gear Factory, Component Factory Lv.20 and Iron Mine Lv.27 and were closed without spending (Craft at 495.0K coin was NOT tapped). The floating-icon tap at (86,315) is the closest miss and the next unit's first retry candidate.
- The full edge-drag sweep of the Nov 1 rule was NOT completed: the left-side coin and stone building bubbles, the drone-component bubbles, the EXP and screw bubbles and the armed-truck loot check were not reached or verified inside the unit cap, so the sweep falls further behind; the next harvest unit resumes from the sweep with the marker-confusion caution above as its first note. No truck top bubble was claimed (truck work belongs to the trucks unit). No diamonds, money, speedup or paid button was touched.
- No earlier claim superseded.

## What the 2026-11-04 0755 unit added - farmland +2.6M verified, left-side +3.0M unattributed, Alliance back arrow corrected to (161,935), partial

- Unit harvest-2026-11-04-0603 by ticker-0734, about 07:43 to 07:55 local, status partial. Session dropped between units (cc-430 to cc-431); the token was re-acquired at 07:51 after the first 15 minute lease expired, and no other executor held the token. No different-device dialog appeared. Evidence in `_records_/2026-11-04/resource-collection/0755-queue-run.md`.
- Entry route, corrected: the unit started on the Rallied Attack panel left open by the donations unit. Both panel X buttons closed cleanly (Alliance Tech panel, then Alliance Techs tree). The Alliance menu back arrow did NOT respond at (106,910) (two taps, no change) nor at (106,925) (one tap, no change). Visual grounding on the menu screenshot placed the arrow centre at (161,935); a tap there returned to the base on the first try. Next unit: use (161,935) for this back arrow, not the left-edge estimates (106,910) or (106,925).
- Verified gains, by HUD deltas only: base HUD at entry (live screenshot reads) first value 412.6M, second 745.8M, third 12.2M, total power 150,028,269. Farmland tap at (364,481): first HUD value 412.6M to 415.2M (+2.6M) on the next screenshot. Per the standing farmland rule one tap collects all farmland bubbles; the +2.6M is the verified gain, consistent with the 0413 unit's +2.0M farmland tap. Left-side tap at (88,406): third HUD value 12.2M to 15.2M (+3.0M) on the next screenshot, and the left-side buildings showed tall orange bars on that same screenshot (normal buildings again on the following screenshot). The +3.0M HUD delta is verified; the bubble identity behind it is NOT separately verified, so no bubble count is claimed for it.
- Marker confusion, Issue #250 evidence (already commented on #250 by the ticker pass, so no duplicate comment here): tap at (90,448) selected Gold Mine Lv.30 (label and info icons shown, HUD unchanged) - a building selection, not a bubble. This repeats the 0413 pattern - small icons above the left-side buildings are building markers at this screenshot resolution, not reliably collectible bubbles. An empty-ground tap at (500,700) deselected the Gold Mine; no panel was opened and nothing was spent.
- Sweep coverage: left edge viewed after a (300,500) to (600,500) drag (the two taps above are the only left-side attempts); right side (Capitol, VS, Season II header area) viewed after a (600,500) to (300,500) drag - no collectible bubbles seen, only building markers and red-dot badges; top edge (hero statues, Eiffel Tower, ferris wheel) viewed after a (500,300) to (500,600) drag - no collectible bubbles seen; bottom Season 2 zone NOT swept as main-base harvest, per the 2026-11-01 rule (its bubbles are not main-base harvest).
- Why partial, not done: the full edge-drag sweep of the 2026-11-01 rule was not completed to zero remaining - EXP, screw and drone-component bubbles were not located or verified, and the remaining left-side bubbles were not distinguished from building markers. The next harvest unit resumes from the sweep, with the back-arrow correction (161,935) and the marker-confusion caution above as its first notes. No truck top bubble was claimed; truck work belongs to the trucks unit under one-unit-one-type. No diamonds, money, speedup, or paid button was touched. Tracker untouched, per the rule for partial units.
- No earlier claim superseded.

## What the 2026-11-04 1101 unit added - farmland +2.1M food, left-side +1.4M coin, entry corrections re-confirmed, sweep still incomplete, partial

- Unit harvest-2026-11-04-1003 by ticker-1034, about 10:48 to 11:01 local, status partial. Session dropped between units (cc-446 to cc-448); the unit cap (15 minutes from claim) and the mid-pass session drop left only about 7 minutes of game time in this unit, blocker category b. No diamonds, money, speedup items or paid button touched. No building or research started, no assembly, no teleport. Evidence in `_records_/2026-11-04/resource-collection/1101-queue-run.md`.
- Entry route, corrections re-confirmed: the unit started on the Rallied Attack panel left open by the donations unit. Both panel X buttons closed cleanly (Alliance Tech panel at (848,213), then Alliance Techs tree at (848,150)). The Alliance menu back arrow responded at (161,935) on the first tap, confirming the 0755 correction; the left-edge estimate (106,910) was not used. Incidental donations state at entry: the coin button was still greyed with a 00:11:45 regen timer, down from 00:16:35 at the donations unit's close, consistent with the timer running (see the donations 1046 fold).
- Verified gains, by HUD deltas only: base HUD at entry (live screenshot reads) food 417.9M, iron 749.5M, coin 18.0M, second row 21.0M, 922.2K, diamonds 12.72K, total power 150,028,269. Farmland tap at (364,481): food 417.9M to 420.0M (+2.1M) on the next screenshot, and the farmland cluster's round value bubbles cleared. Per the standing farmland rule one tap collects all farmland bubbles; the +2.1M is the verified gain. Left-edge drag (300,500) to (600,500) shifted the camera to the left-side buildings. Left-side tap at (88,406): coin 18.0M to 19.4M (+1.4M) on the next screenshot, food and iron unchanged. The +1.4M HUD delta is verified; the bubble identity behind it is NOT separately verified, so no bubble count is claimed for it. This replicates the 0755 unit's left-side collection point. Total HUD-verified gain in this unit: food +2.1M, coin +1.4M.
- Sweep coverage: farmland cluster collected, bubbles cleared. Left edge viewed after the drag; one tap collected. Remaining small icons above the left-side buildings were not distinguished from building markers and were not tapped (the 0755 marker-confusion caution, Issue #250). Right side and top edge NOT swept in this unit. Bottom Season 2 zone NOT swept as main-base harvest, per the 2026-11-01 rule (its bubbles are not main-base harvest).
- Why partial, not done: the full edge-drag sweep of the 2026-11-01 rule was not completed to zero remaining - EXP, screw and drone-component bubbles were not located or verified, and the right side and top edge were not swept. The next harvest unit resumes from the sweep. No truck top bubble was claimed; truck work belongs to the trucks unit under one-unit-one-type. No new issue filed: Issue #250 already covers the bubble-grounding confusion, and this unit's left-side tap succeeded at the 0755 point rather than adding a new failure mode. No earlier claim superseded.

## What the 2026-11-04 1634 unit added - screen-capture failure, ninth consecutive pass, nothing read

- Unit harvest-2026-11-04-1403 by ticker-1634, about 16:34 to 16:48 local, status failed. Evidence in `_records_/2026-11-04/resource-collection/1634-queue-run.md`. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: computer.control activate LastWar (cc-469) selected the window for background input but captured no observation, computer.observe (cc-469, compact) failed, and after a 30 second wait computer.observe (cc-470, image) and computer.control describe LastWar (cc-470) failed, all with "Failed to start stream due to audio/video capture failure". The control channel itself was reachable (computer.control list_windows in cc-469 listed the LastWar window); the capture stream was not. The device connection health was healthy on both native and web transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The base, its resource bubbles and the HUD totals could not be read, and no bubble was tapped or verified. No harvest was collected.
- Recurrence, not a new failure class: this is the ninth consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434, ticker-1504 donations 1504, ticker-1534 radar 1534, ticker-1604 arms-race 1604, ticker-1634 harvest 1634), now across nine activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 instead of filing a duplicate, and this run comments the ninth and tenth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The inbox held 72 units at this pass, per the record.

## What the 2026-11-04 2104 unit added - screen-capture failure, next known pass after 2034, nothing read

- Unit harvest-2026-11-04-1803 by ticker-2104, about 21:04 to 21:12 local, status failed. Evidence in `_records_/2026-11-04/resource-collection/2104-queue-run.md`. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: session cc-486, computer.control list_windows succeeded and listed the LastWar window, so the control channel itself was reachable, but computer.observe (compact) failed with "Failed to start stream due to audio/video capture failure", computer.control activate selected the LastWar window for background input but captured no observation with the same error, and computer.observe (image view) failed with the same error; session cc-487, a fresh session after ending cc-486 and a connection-health check, computer.observe (compact) failed with the same error and computer.control describe for LastWar failed with the same error, so even the accessibility-tree route was unavailable. Total capture attempts: 4, meeting and exceeding the standing at-least-3-attempts retry rule. The device connection health was healthy on both native and web transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The base, its resource bubbles and the HUD totals could not be read, and no bubble was tapped or verified. No harvest was collected.
- Recurrence, not a new failure class: this is the next ticker pass after ticker-2034 known to fail on this exact blocker; the record does not assert an exact consecutive count beyond that. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments this occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The inbox held 72 units at this pass, per the record.

## What the 2026-11-05 0034 unit added - screen-capture failure, twenty-fourth consecutive pass, nothing read

- Unit harvest-2026-11-04-2203 by ticker-0034, about 00:34 to 00:41 local, status failed. Evidence in `_records_/2026-11-05/resource-collection/0034-queue-run.md`. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt: the executor subagent tried `computer.observe` (compact, image, full), `computer.control` screenshot and describe, and `screen.snap`, six or more attempts, all with "Failed to start stream due to audio/video capture failure"; the parent then tried once more in a fresh computer session (cc-502) with `computer.observe` view=image, same error. The capture pipeline itself works: a Chrome window observed and screenshotted normally in the same session, so the fault is specific to the LastWar window. LastWar (bundle com.lastwar.ios, pid 59735) is running, fullscreen 1920x1080 at (0,0) on an inactive Space; Google Chrome is frontmost. `activate` reports `window_on_screen: false`.
- Space-switch attempts failed: Ctrl+Right / Ctrl+Left dispatched but the Space did not switch; Cmd+Tab is blocked by the tool; the Dock icon could not be located from a window-relative observation, so no blind click was attempted. The menu path View -> Exit Full Screen needs a fresh observation of the game window, which is exactly what fails.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The base, its resource bubbles and the HUD totals could not be read, and no bubble was tapped or verified. No harvest was collected.
- Recurrence, not a new failure class: this is the twenty-fourth consecutive ticker pass to fail on this exact blocker (ticker-0004 at 00:04 was the twenty-third, per the recount in its correction file). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the twenty-fourth and twenty-fifth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed.
- The unit's 15 minute budget was spent on control-channel recovery attempts; game time was zero. No other unit was attempted in this pass: every unit needs the same game screen, so all would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh). The View menu lists "Enter Full Screen" (read from the menu-action error listing in session cc-505, repeated probe in cc-508 with the menu unchanged), so the app is NOT in native fullscreen: it is a windowed 1920x1080 window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission (Chrome windows observe normally in the same sessions).
- Superseded in this profile: the "running fullscreen" wording in the 1634, 2104 and 0034 sections above. The 0034 section's "menu path View -> Exit Full Screen" is superseded with it: the menu contains "Enter Full Screen", not "Exit Full Screen".
- Follow-up corrected: the standing "screen recording permission or capture pipeline restart" unblock is replaced - the unblock is getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step. Background-sent Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, Cmd+Tab is blocked by the tool, and list_windows needs the exact app name "LastWar" ("Last War" returns 0 windows). No control route available to the background channel moves the window across Spaces without a fresh observation of the window itself.
- This correction does not change the harvest state: the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) stands as the last live read. The twenty-sixth and twenty-seventh occurrences are commented onto Issue #282 by this run; Issue #284 already tracks the blocker.

## What the 2026-11-05 0434 unit added - screen-capture failure, thirty-second consecutive pass, nothing read

- Unit harvest-2026-11-05-0203 by ticker-0434, about 04:34 to 04:44 local, status failed. Evidence in `_records_/2026-11-05/resource-collection/0434-queue-run.md`. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on all five attempts across two computer sessions (cc-518, cc-519): computer.control activate selected the LastWar window for background input but captured no observation, computer.observe (compact, then image) failed, and in a fresh session (cc-519) computer.observe (compact) and computer.control describe for LastWar failed, all with "Failed to start stream due to audio/video capture failure". The capture pipeline itself works: a Chrome window observed normally in a fresh session (cc-520, Gmail inbox, 60 elements), so the fault is specific to the LastWar window. LastWar (bundle com.lastwar.ios, pid 59735) is running, a 1920x1080 window at (0,0) on an inactive Space, window_id 160366; Google Chrome is frontmost (Gmail inbox). `activate` reports `window_on_screen: false` and `brought_to_front: false`.
- Probe classification: `_tools_/mac_capture_probe.py` (tool version 1.0.0) classifies OFF_SCREEN_WINDOW (high confidence), stop_pass yes, exit code 10. One probe step is missing: the View-menu inspect (Enter/Exit Full Screen), because the describe route is itself capture-blocked.
- Recovery still needs the one owner step: click the LastWar Dock icon once on the Mac mini (or run `_tools_/mac_lastwar_front.sh` in Terminal), then re-probe. No background control route moves the window - Space keys sent in the background do not switch Spaces, open_app returns outcome_unknown, and set_window_frame needs a fresh observation, which is exactly what the failure prevents. Never use Control-Command-F or Escape on this app (both crash it).
- Recurrence, not a new failure class: this is the thirty-second consecutive ticker pass to fail on this exact blocker (ticker-0304 the twenty-ninth, ticker-0334 the thirtieth, ticker-0404 the thirty-first). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the thirty-second occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- The pass stopped after this one unit - every unit needs the same game screen, and the probe says to stop. The inbox held 72 units at this pass. No other unit was attempted.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 0904 unit added - invoke-channel stall, fortieth consecutive pass, nothing read

- Unit harvest-2026-11-05-0603 by ticker-0904, about 09:04 to 09:22 local, status failed. Evidence in `_records_/2026-11-05/resource-collection/0904-queue-run.md`, published on branch `ticker-0904-rec-2026-11-05` (commit 4545274268, pushed to GitHub) and landing on the records/2026-11-05 branch with the 11:00 batch. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. Every device invoke timed out with zero responses - eight attempts across two devices and five distinct commands: `computer.session` start twice (node_invoke_timeout after 120 seconds each), `computer.control` list_apps (120 seconds), `connection.health` on the Mac mini (25 seconds), `connection.repair` (target web) on the Mac mini (25 seconds), `connection.repair` (target native) on the recovery device ("timeout: Connection recovery could not complete"), `connection.health` on the recovery device (same timeout), `computer.session` end (120 seconds). Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd reported online by device.list but last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 1 hour 40 minutes at pass time; the recovery device reported online with the same stale last_seen. This meets and exceeds the standing at-least-3-attempts retry rule.
- New worsened form, distinct from Issue 284's signature: Issue 284 is a capture failure WITH responses - the 0804 pass got list_apps results, activate calls returning the stream error, and a working Chrome observation. This pass got no response to any invoke at all - the device gateway / transport itself is stalled, not just the LastWar window stream. The count keeps running (fortieth consecutive ticker pass with a Mac device-access blocker; thirty-ninth was ticker-0834, donations unit donations-2026-11-03-1241), but the form is new and is tracked as the worsened form of Issue 284, not as another capture-failure occurrence.
- Recovery, scoped correction: the Correction 2026-11-05 unblock - the owner clicking the LastWar Dock icon once (or running `_tools_/mac_lastwar_front.sh`) - addresses the window-stream fault, NOT a stalled invoke channel. If the next pass still times out on every invoke, the Mac-side agent gateway likely needs a restart. That gateway-restart step is the record's inference, not a verified fix: no pass has yet run it and confirmed recovery. The probe `_tools_/mac_capture_probe.py` 1.0.0 has no invoke-timeout field and cannot classify this evidence; the CHANNEL_STALL diagnosis that classifies exactly it (invoke_timeouts with invoke_responses 0, high confidence, stop_pass yes) lived in PR #321 at pass time and has since merged (2026-11-05, commit 18b8b6da29), so the next pass classifies with the probe in-tree.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed. The pass stopped after this one unit: a second unit would hit the same stalled channel.
- Recurrence: this is the fortieth consecutive ticker pass with a Mac device-access blocker. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fortieth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1634 unit added - Mac device offline, fifty-fourth consecutive pass, zero-response form

- Unit harvest-2026-11-05-1403 by ticker-1634, about 16:34 to 16:41 local, status failed. Evidence in `_records_/2026-11-05/resource-collection/1634-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses, across two devices and four distinct commands: connection.health on the Mac mini node_offline (device offline, no wake-up path), computer.session start on the Mac mini node_offline, screen.snap on the Mac mini node_offline, connection.health on the recovery device node_invoke_timeout after 25 seconds, connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 9 hours 4 minutes at pass time, unchanged since the ticker-1025 pass; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence, not a new failure class: this is the fifty-fourth consecutive ticker pass with a Mac device-access blocker, fifteenth in the worsened zero-response form after ticker-1604 (fifty-third, fourteenth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fifty-fourth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- The pass stopped after this one unit: a second unit would hit the same dead channel. Sync at pass start produced nothing new (21 due, all already queued). The Zombie Invasion chain stays closed: the event ended 2026-10-30 about 19:00 and no Zombie Invasion tab has been seen in the Events hub since, so no fresh chain was seeded. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-05) was already staged by ticker-1604.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 0504 unit added - Mac device offline, sixty-ninth consecutive pass, zero-response form

- Unit harvest-2026-11-06-0203 by ticker-0504, about 05:04 to 05:14 local, status failed. Evidence in `_records_/2026-11-06/resource-collection/0504-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted harvest check for this slot.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses, all node_offline (device offline, no wake-up path): connection.health (attempts 1 and 5), computer.session start (attempts 2 and 4), connection.repair (web) (attempt 3). device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 21 hours 30 minutes at the 05:05 re-check, unchanged since the ticker-0004 pass. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen 15:36:52Z, and its attempts in the ticker-2041 pass timed out after 25 seconds each, so nothing new would be learned by repeating them. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the sixty-ninth consecutive ticker pass with a Mac device-access blocker, thirtieth in the worsened zero-response form after ticker-0434 (sixty-eighth, twenty-ninth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate (its first comment carried the stale ticker-0004 counts, 64th/25th, then posted a correction to 69th/30th), and this run comments the sixty-ninth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 0, due 20, produced nothing new, all 20 regulars already queued; the inbox held 74 units at this pass close (74 at sync).

## What the 2026-11-06 0704 unit added - Mac device offline, seventy-third consecutive pass, zero-response form

- Unit harvest-2026-11-06-0603 by ticker-0704, about 07:04 to 07:14 local, status failed. Evidence in `_records_/2026-11-06/resource-collection/0704-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted harvest check for this slot (planned 06:03 local 2026-11-06, expires 10:03 local 2026-11-06).
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses, all node_offline (device offline, no wake-up path): connection.health (attempts 1 and 4), connection.repair (web) (attempt 2), computer.session start (attempt 3). device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 23 hours 36 minutes at the 07:12 re-check, unchanged since the ticker-0534 pass and re-verified unchanged by the ticker-0604 and ticker-0634 passes. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen 15:36:52Z, and its attempts in the ticker-0234 pass timed out after 25 seconds each, so nothing new would be learned by repeating them. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the seventy-third consecutive ticker pass with a Mac device-access blocker, thirty-fourth in the worsened zero-response form after ticker-0634 (seventy-second, thirty-third). No executed pass is recorded between 0634 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the seventy-third occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 5, due 22, produced no new unit, 22 regulars already queued; the inbox held 54 units at this pass close (55 counting the claimed harvest unit, after 5 expired units were reaped).

## What the 2026-11-06 1904 unit added - Mac device offline, eighty-seventh consecutive pass, zero-response form

- Unit harvest-2026-11-06-1803 by ticker-1904, about 19:04 to 19:15 local, status failed. Evidence in `_records_/2026-11-06/resource-collection/1904-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted resource-collection sweep for this slot (planned 18:03 local 2026-11-06, expires 2026-11-07 06:03 UTC). The full-map zero-remaining acceptance is still unmet since the 2026-11-01 15:34 close, and the Armed Truck state is unknown since then.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) twice; connection.health on the Mac mini node_offline; connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds; connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 35 hours 37 minutes at the 19:14 re-check, unchanged since the ticker-1827 pass. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the eighty-seventh consecutive ticker pass with a Mac device-access blocker, forty-eighth in the worsened zero-response form after ticker-1827 (eighty-sixth, forty-seventh). No executed pass is recorded between 1827 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eighty-seventh occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- Pre-reset zero sweep missed: both pre-reset zero-sweep units for the 2026-11-06 reset day expired unexecuted in this pass's sync - zero-sweep-pre-reset-sweep-2026-11-06-001 (17:30 slot) and -002 (18:30 slot). The 19:00 reset has now passed with no zero sweep of the daily collection ledger, so no ledger line was verified at zero for this reset day. The other six units expired in the same sync were duel-score-2026-11-06-1430, events-2026-11-06-1457, passes-2026-11-06-1457, secrets-2026-11-06-1457, treasures-2026-11-06-1457 and trucks-2026-11-06-1457.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 8, due 22, produced 4 new units (vip-2026-11-06-1800, daily-missions-2026-11-06-1800, duel-score-2026-11-06-1830, scout-2026-11-06-1800); the other 18 due regulars were already queued. The inbox held 67 units at this pass's close.

## What the 2026-11-06 2257 unit added - Mac device offline, ninety-second consecutive pass, zero-response form

- Unit harvest-2026-11-06-2203 by ticker-2257, about 22:57 to 23:04 local, status failed. Evidence in `_records_/2026-11-06/resource-collection/2257-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted resource-collection sweep for this slot (planned 22:03 local 2026-11-06, expires 2026-11-07 10:03 UTC). The full-map zero-remaining acceptance is still unmet since the 2026-11-01 15:34 close, and the Armed Truck state is unknown since then.
- No game screen was ever read and no game input was dispatched. Six device invokes, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) three times; connection.health on the Mac mini node_offline; connection.repair (web) on the Mac mini node_offline; connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 39 hours at the 23:02 re-check, unchanged since the ticker-1025 pass on 2026-11-05. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the ninety-second consecutive ticker pass with a Mac device-access blocker, fifty-third in the worsened zero-response form after ticker-2134 (ninety-first, fifty-second). No executed pass is recorded between 2134 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented the ninety-second occurrence onto #284, and this run comments it onto #282.
- Nothing new was learned about the recovery route: the recovery-device health check timed out after 25 seconds, the same signature as the 0934, 1544, 2034 and 2134 passes - the recovery channel still accepts the invoke and never answers within 25 seconds.
- Queue-state note, carried from the record: no working-tree divergence this pass. The pass fetched the remote tip first and worked in a fresh detached worktree of github/records/2026-11-06 at f5a85928e0 (planner-2240 tip), verified identical on the VPS and on github - the fetch-first discipline that the 2034 pass lacked, so the divergence class the 2034 record named did not recur here. Sync reaped 0, expired 6, due 22, produced 1 (duel-score-2026-11-06-2230; the other 21 regulars were already queued). No zombie seeding: the Zombie Invasion chain closed 2026-10-30 when the event ended, and no Zombie Invasion tab is to be seeded until one is seen live in the Events hub again. The 22:04 tick executed no unit: the newest executed closing before this pass was the 21:53 ticker-2134 close, and the day INDEX already carries ticker-2204 as a pass with no record on either branch - this pass does not resolve that gap, which stays tracked by the organizer and pr-catchall jobs.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the harvest unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically.

## What the 2026-11-07 0526 unit added - Mac device offline, one-hundredth consecutive pass, zero-response form

- Unit harvest-2026-11-07-0203 by ticker-0526, about 05:26 to 05:33 local, status failed. Evidence in `_records_/2026-11-07/resource-collection/0526-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted resource-collection sweep for this slot (planned 02:03 local 2026-11-07, expires 06:03 local 2026-11-07). The full-map zero-remaining acceptance is still unmet since the 2026-11-01 15:34 close, and the Armed Truck state is unknown since then.
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) three times; connection.health on the Mac mini node_offline; connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds; connection.health on the recovery device node_invoke_timeout after 25 seconds; connection.repair (web) on the Mac mini node_offline. device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 46 hours at the 05:30 re-check, unchanged since the ticker-0420 pass about 70 minutes earlier. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the one-hundredth consecutive ticker pass with a Mac device-access blocker, sixty-first in the worsened zero-response form after ticker-0420 (ninety-ninth, sixtieth). No executed pass is recorded between 0420 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented the one-hundredth occurrence onto #284, and this run comments it onto #282.
- Nothing new was learned about the recovery route: the recovery-device health check and repair both timed out after 25 seconds, the same signature as the 0420, 0345, 0304, 0234 and 0204 passes - the recovery channel still accepts the invoke and never answers within 25 seconds.
- Queue-state note, carried from the record: sync reaped 0, expired 0, due 20, produced nothing new, all 20 regulars already queued. Queue stats at 13:27Z: inbox 74, claimed 0, done 1097. No zombie seeding: the Zombie Invasion chain closed 2026-10-30 when the event ended, and no Zombie Invasion tab is to be seeded until one is seen live in the Events hub again. The pre-reset zero-sweep pair for the 2026-11-07 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. Tracker untouched, per the failed-unit rule; the next tick re-produces the harvest unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.

## What the 2026-11-07 0704 unit added - Mac device offline, one-hundred-second consecutive pass, zero-response form

- Unit harvest-2026-11-07-0603 by ticker-0704, about 07:04 to 07:15 local, status failed. Evidence in `_records_/2026-11-07/resource-collection/0704-queue-run.md`. No bubble count was read, no bubble was collected, and the Armed Truck state is unread. No resource collected, no diamonds, money, speedup items or paid button touched. The loss is the unexecuted resource-collection sweep for this slot (planned 06:03 local 2026-11-07, expires 10:03 local 2026-11-07). The full-map zero-remaining acceptance is still unmet since the 2026-11-01 15:34 close, and the Armed Truck state is unknown since then.
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses: computer.session start on the Mac mini node_offline (attempt 1), connection.health on the Mac mini node_offline (attempt 2), computer.session start on the Mac mini node_offline (attempt 3), connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 4). device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 47.5 hours at the 07:14 re-check, unchanged since the ticker-0633 pass about 30 minutes earlier. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the one-hundred-second consecutive ticker pass with a Mac device-access blocker, sixty-third in the worsened zero-response form after ticker-0633 (one-hundred-first, sixty-second). No executed pass is recorded between 0633 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the one-hundred-second occurrence onto #282.
- Nothing new was learned about the recovery route: the recovery-device health check timed out after 25 seconds, the same signature as the 0633, 0526, 0420, 0345, 0304 and 0234 passes - the recovery channel still accepts the invoke and never answers within 25 seconds.
- Queue-state note, carried from the record: sync reaped 0, expired 6, due 22, produced one new unit (duel-score-2026-11-07-0630), all other due regulars already queued. Queue stats at 15:06Z: inbox 69, claimed 0, done 1049. No zombie seeding: the Zombie Invasion chain closed 2026-10-30 when the event ended, and no Zombie Invasion tab is to be seeded until one is seen live in the Events hub again. The pre-reset zero-sweep pair for the 2026-11-07 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. Tracker untouched, per the failed-unit rule; the next tick re-produces the harvest unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Reading warning: this failed unit gives zero evidence about the harvest state. It must NOT be read as "nothing collectible" or as a bubble state - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The full edge-drag sweep of the 2026-11-01 rule remains incomplete from the 1101 unit and is carried forward, not closed. The Armed Truck state is unknown.

## What the 2026-11-07 1655 unit added - farmland bubbles cleared in one tap, three new not-a-bubble points, sweep unfinished, partial

- Unit harvest-2026-11-07-1403 by ticker-1655, about 16:56 to 17:04 local, status partial. Evidence in `_records_/2026-11-07/resource-collection/1655-queue-run.md` (commit 514e333e5b on records/2026-11-07). Mac mini online and controllable again after the outage that failed the 0526 pass this morning; computer session cc-14, LastWar already running and selected. Unit duration 466 seconds (about 8 minutes) by the tool stamps - inside the 15-minute cap; the record frontmatter's "3 minutes past the cap" is corrected by the record body itself, so no overrun is claimed here.
- Farmland bubbles, one tap collected all five: after panning the base view left (drag from norm 450,500 to 750,500), five gold food bubbles stood over the wheat fields at the left edge, labelled 40.9K, 38.8K, 37.7K, 37.1K and 32.0K (norm about 64,297 / 124,281 / 172,301 / 124,324 / 59,363). One tap on the 38.8K bubble at norm 124,281 cleared all five at once, as the activity metadata records. Food HUD moved 485.3M to 485.5M (about 0.2M, matching the 186.5K sum of the five labels at the 0.1M display rounding). Iron 808.9M, coin 5.0M, stone 25.0M and 922.2K unchanged.
- Not-a-bubble points, three new: (1) purple crystal icon over the purple crystal building at norm 596,547 - one tap, no change observed, icon still present in the next screenshot; building decoration, not a collectible bubble; not retried. (2) beige square with a green symbol at norm 806,686, right of the troop field - one tap, no change observed, still present; a static sign, not a bubble. (3) blue droplet bubble over the blue truck at norm 150,293 - one tap did NOT collect; it jumped to the world-map task view ("2 task rewards can be claimed", green Claim All button, no price tag). That is radar-task work, not harvest, so the Claim All was left untouched and the home button returned the view to the base. The droplet is a locator, not a loot bubble; the Armed Truck loot state itself was not verified in this unit.
- Sweep state, why partial: the base was panned left only. Iron, coin, stone, EXP, screws and drone-component bubbles were not swept, the Armed Truck loot was not verified or claimed, and the bottom Season 2 zone was not checked, so the 2026-11-01 full-map zero-remaining acceptance is not met. The next harvest unit resumes from the panned-left view state and the findings above.
- Figures read live: food 484.6M at entry, 485.3M before the farmland tap, 485.5M after; iron 808.9M before and after, coin 5.0M, stone 25.0M, 922.2K; power 149,850,353; stamina 72 at entry, 73 at close (regeneration). No diamonds, money, speedups or paid buttons were used. No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.
- Lesson, standing: image-observe round trips are still the bulk of the unit time (each screenshot plus read about a minute) - verify with the compact observe where the HUD figure is enough, and keep image screenshots for bubble grounding only.
- Reading warning: this partial unit is not a full-map close - the 1101 close (farmland +2.1M food, left-side +1.4M coin verified, sweep incomplete) stands as the last live read of the wider sweep, and the full edge-drag sweep of the 2026-11-01 rule remains incomplete, carried forward not closed. The Armed Truck state is unknown.
- Tracker untouched, per the partial rule; the next tick re-produces the harvest regular.

## What the 2026-11-07 1941 unit added - farmland +1.9M food, +1.2M coin, estimated centres fail so ground first, truck icon pans instead of opening loot, sweep unfinished, partial

- Unit harvest-2026-11-07-1803 by ticker-1940, about 19:41 to 19:49 local, status partial. Evidence in `_records_/2026-11-07/resource-collection/1941-queue-run.md` (commit c47e491fd on records/2026-11-07). Computer session cc-39, LastWar already running on the Events screen (Drone Boost contest, Arms Race phase, not this unit's work); back arrow returned to base. Unit duration 476 seconds inside the 15-minute cap; the session window was corrected against the queue tool stamps.
- Food collected, verified by HUD: 476.8M at entry, 478.7M at close, plus about 1.9M. Three taps on the left farmland cluster: the first tap (norm 155,286, estimated from the screenshot) cleared the upper bubble row with no HUD move; the second tap (norm 301,357, estimated) produced no change and the bubble stayed; the third tap (norm 344,383, centre from visual grounding on the live screenshot) cleared the middle cluster and food moved 476.8M to 478.7M. A fourth tap (norm 98,357) on the leftmost bubble cleared the remaining visible farmland bubbles - the wheat fields show no bubbles in the closing views.
- Coin collected, verified by HUD: 5.7M at entry, 6.9M at close, plus about 1.2M, collected during the same farmland sweep (the gold bubbles in the cluster include coin; the labels at this resolution do not separate food from coin, so the split is by HUD movement, not by label).
- Iron, observed not claimed: HUD 800.4M at entry, 802.1M after the first tap, plus about 1.7M, attribution unverified - no iron bubble was deliberately tapped, so this may be furnace overdrive production (the "High-temp Furnace total overdrive time [in sec] [22/60]" toast ran through the unit) rather than a collection. Recorded as an observed HUD change only.
- Method lesson, standing (rule R2): two estimated-centre taps failed to collect. The pivot was to ground the bubble centre with the visual grounding tool on the live screenshot before tapping; the grounded tap collected. Estimated bubble centres are not reliable at this window size - ground first, then tap.
- Armed Truck loot, still unverified: the gold truck icon tapped at norm 681,814 near the end panned the map down to the Drill Ground area instead of opening a loot panel. The truck icon is not a verified loot-panel entry; the loot panel entry remains unlocated.
- Sweep state, why partial: iron, stone, EXP, screw and drone-component bubbles in other map areas were not individually swept; the blue bubbles at the top of the base and the gold star bubble over the cannon were not tapped; the bottom Season 2 zone was not checked, and the map was not dragged to every edge, so the 2026-11-01 full-map zero-remaining acceptance is not met. The next harvest unit resumes from the panned-down Drill Ground view.
- Left untouched, other task types' work: the blue droplet over the blue truck (radar-task locator, per the 1655 record) and the "?" survivor markers.
- Figures read live: food 476.8M at entry, 478.7M at close; iron 800.4M at entry, 802.1M at close; coin 5.7M at entry, 6.9M at close; stone 25.0M before and after, 922.2K before and after. Power 149,850,353. Stamina 105 at entry, 106 at close (regeneration). No diamonds, money, speedups or paid buttons were used. No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.
- Reading warning: this partial unit is not a full-map close - the 1101 close stands as the last live read of the wider sweep, and the full edge-drag sweep of the 2026-11-01 rule remains incomplete, carried forward not closed. The Armed Truck state is unknown.
- Tracker untouched, per the partial rule; the next tick re-produces the harvest regular.


## What the 2026-11-08 0958 unit added - food +8.2M, coin +5.4M, iron +7.5M, one-tap farmland rule holds, top-edge bubbles unreliable, Power Details measured

- Unit harvest-2026-11-08-0603 by ticker-0934, about 09:47 to 10:02
  local, status partial - food, coin and iron collected in bulk; the
  full-map zero-remaining acceptance of 2026-11-01 is NOT met
  (top-edge bubbles and the armed truck loot are unverified). Evidence
  in `_records_/2026-11-08/resource-collection/0958-queue-run.md`
  (commit ac350b49c on records/2026-11-08). Sessions cc-104 (dropped
  mid-unit, observation_unavailable, same class as the 0808 unit's
  cc-97) and cc-105 on the owner Mac mini. One visual-grounding call
  timed out after 180 seconds; the sweep continued from the last live
  screenshot. No device-access error, no different-device dialog, no
  login demanded. About 14 minutes, inside the 15-minute cap.
- Collected, HUD-verified: Coin - one tap on a grounded gold bubble
  centre (norm 180,452) collected the left coin cluster, coin 6.9M
  to 12.3M, plus about 5.4M. Food - one tap on a grounded wheat
  bubble centre (norm 304,430) collected ALL farmland bubbles, food
  478.8M to 487.0M, plus about 8.2M; the wheat fields show no bubbles
  afterwards. The one-tap farmland rule holds (third confirmation:
  1655, 1941, this unit). Iron - one tap on a grounded iron bubble
  centre (norm 242,343) collected the iron-mine cluster, iron 802.1M
  to 809.6M, plus about 7.5M; the mine bubbles restart as small green
  6.1M bubbles.
- Method notes: grounded centres work. An estimated centre (norm
  247,483) selected the Iron Mine building instead and opened its
  panel (dismissed by tapping empty road; the green up-arrow upgrade
  button was NOT tapped) - ground first, then tap (rule R2 from the
  1941 unit, confirmed again).
- Top-edge bubbles unreliable, standing: a 4-tap batch on the
  top-edge bubbles collected nothing; the third tap (norm 380,124)
  landed on the HUD power figure and opened the POWER DETAILS panel
  instead of a bubble. The panel was closed unread for action (Power
  Up button NOT tapped). Never batch-tap near the HUD power figure.
  Bubble centres near the top edge of the window sit partly
  off-screen and their grounding points map onto HUD elements.
- Power Details panel read, for the record only (measured
  2026-11-08): Hero Power 65,282,351 (Hero Level 41,841,684;
  Decorations and Building Stats 7,264,676; Gear 5,647,815; Hero
  Skill 4,267,150; Hero Tier 3,971,468; Exclusive Weapon 2,182,608;
  Wall of Honor 106,950), Drone Power 5,807,288 (Drone Level
  3,459,213; Drone Component 1,639,876; Skill Chip 708,200), Building
  Power 10,292,275 (Buildings 7,170,500). Total account power
  149,850,353 unchanged.
- Sweep state, why partial: top-edge bubbles over the top buildings
  (gold coin and blue iron/stone bubbles, partly off-screen) were not
  collected; EXP, screw and drone-component bubbles were not
  individually swept or verified; the Armed Truck loot was not
  verified or claimed (the blue droplet over the blue truck is the
  radar-task locator per the 1655 record, not truck loot); the bottom
  Season 2 zone was not checked, and the map was not dragged to every
  edge, so the 2026-11-01 full-map zero-remaining acceptance is not
  met. The next harvest unit resumes the sweep.
- Left untouched, other task types' work: the "?" survivor markers and
  the blue truck droplet.
- Figures read live: entry food 478.8M, iron 802.1M, coin 6.9M,
  diamonds 4,397, badge 13.22K, power 149,850,353, stamina 120, stone
  25.0M, 922.2K; close food 487.0M, iron 809.6M, coin 12.3M, the rest
  unchanged. Furnace overdrive toast [22/60] recurring through the
  unit; 99+ chat badge recurring.
- Reading warning: this partial unit is not a full-map close - the
  1101 close stands as the last live read of the wider sweep, and the
  full edge-drag sweep of the 2026-11-01 rule remains incomplete,
  carried forward not closed. The Armed Truck state is unknown.
- Tracker untouched, per the partial rule; the next tick re-produces
  the harvest regular.

## What the 2026-11-08 1211 unit added - farmland food +1.6M verified, top-edge single tap collects nothing, iron +1.3M unattributed, coin sweep cut off by token expiry, partial

- Unit harvest-2026-11-08-1003 by ticker-1134, about 12:11 to 12:21
  local, status partial - the farmland food bubbles are collected
  and the field is clear; the coin bubbles, the iron bubbles, the
  top-edge bubbles and the armed truck loot are NOT verified
  collected and carry to the next harvest unit. Evidence in
  `_records_/2026-11-08/resource-collection/1211-queue-run.md`
  (commit ce3dcc4bf on records/2026-11-08). Tracker untouched.
- Session: computer session cc-118 on the owner Mac mini. The game
  was on the Events hub Ranking Reward panel at entry (leftover from
  the ticker-1134 scout unit); the panel was closed and the base
  screen reached with the back arrow. No device-access error, no
  different-device dialog, no login demanded. Nothing bought, no
  speedup used. The pass token expired at 12:22:56, so the unit
  closed before the coin sweep.
- Base HUD at entry (12:11): food 487.9M, iron 810.6M, coin 12.3M,
  stone 25.0M, gold 922.2K, power 149,850,353, diamonds 13.22K,
  stamina 120, cart 4,397, Season II 7d 05:51:17.
- Food collected, HUD-verified: a double-tap on a wheat-field bubble
  cleared the farmland bubbles and food moved 487.9M to 489.5M
  (+1.6M). The second tap of the double-tap landed on the farmland
  building after the bubble vanished and raised a "Production in
  progress. Please wait..." toast - no panel opened, no state
  changed. Do NOT double-tap: one grounded tap suffices (one-tap
  farmland rule, fourth confirmation: 1655, 1941, 0958, this unit).
- Top-edge bubbles, still unreliable: a single tap on a bubble at the
  top edge of the wheat field cleared no food bubble and food did not
  move (further confirmation of top-edge unreliability after the 0958
  4-tap batch, which also collected nothing).
- Iron, observed not claimed: iron moved 810.6M to 811.9M (+1.3M)
  with no bubble tap confirmed as its cause - NOT claimed as a
  collection. The likely cause is furnace overdrive production (the
  "High-temp Furnace total overdrive time [22/60]" toast was
  showing), but that is inference, not a verified read. Same class
  as the 1941 unit's +1.7M unattributed iron move.
- Not done (carries to the next harvest unit): coin bubbles, about
  four visible, uncollected (about 200-230K each, roughly 0.8M
  total; coin HUD still 12.3M); iron bubbles, no iron bubble tapped
  and verified; top-edge bubbles, the small bubbles cut off at the
  very top edge of the base view remain unverified (same open item as
  the 0934 harvest unit); armed truck loot, the blue truck at the
  bottom of the base was not tapped and its loot state is unverified
  (same open item as the 0934 harvest unit).
- Method note (R2): the compact OCR coordinates run about 30 units
  off the image-derived positions, so bubble centres must be
  re-grounded from the image in each unit. Ground first, then tap.
- Figures read live: entry food 487.9M, iron 810.6M, coin 12.3M;
  close food 489.5M, iron 811.9M, coin 12.3M; the rest unchanged.
- Reading warning: this partial unit is not a full-map close - the
  1101 close stands as the last live read of the wider sweep, and the
  full edge-drag sweep of the 2026-11-01 rule remains incomplete,
  carried forward not closed. The Armed Truck state is unknown.
- Tracker untouched, per the partial rule; the next tick re-produces
  the harvest regular. The next harvest unit resumes with the coin
  bubbles first, then the iron bubbles, the top-edge bubbles and the
  armed truck loot (R7 - the starved subtasks lead).

## What the 2026-11-08 1759 unit added - iron +3.6M and coin +3.6M, bubble-type identification unreliable, reset mid-sweep, partial

- Unit harvest-2026-11-08-1403 by ticker-1724, about 17:56 to
  18:00 local, status partial - two bubble taps collected verified
  gains (iron +3.6M, coin +3.6M), but the food bubbles are still
  standing and the 18:00 reset arrived mid-sweep, so the sweep is
  unfinished. Evidence in
  `_records_/2026-11-08/resource-collection/1759-queue-run.md`
  (commit 5f3a904f4 on records/2026-11-08). The tracker is
  untouched and the harvest-2026-11-08-1803 unit, queued with
  not_before 18:03, picks up the remainder in the new reset day.
  This unit is the overdue 1403-slot harvest unit; it was picked by
  the loop after the sweep and missions units because it expires
  18:03 and its bubbles were the last collectible value before the
  reset.
- Session: computer session cc-146 on the owner Mac mini. Sessions
  cc-143 and cc-144 closed between units of this pass without an
  error; each unit re-opened its session, no device-access error,
  no different-device dialog, no login demanded. No control call
  failed in this unit. LastWar was already running and selected,
  verified by list_apps and observe before any input.
- Entry, read live about 17:56 local: base screen, power
  149,209,253 (unchanged all day since 17:12); food 490.8M, iron
  813.3M, coin 12.3M; diamonds 13.22K; cart 4,417; stamina 120;
  Season II 7d 00:03:54. Bubbles standing over the central building
  cluster - food, iron and coin, values in the hundreds of K.
- Tap 1, about 17:58 local: one tap grounded fresh at norm 249,355
  on a bubble centre in the central cluster. After: iron 813.3M to
  816.9M (+3.6M, HUD-verified), food unchanged 490.8M, coin
  unchanged 12.3M.
- Tap 2, about 17:59 local: one tap grounded fresh at norm 179,468
  on a bubble centre over the farmland. After: coin 12.3M to 15.9M
  (+3.6M, HUD-verified), food unchanged 490.8M, iron unchanged
  816.9M.
- Closing state, read live about 17:59-18:00 local: food 490.8M,
  iron 816.9M, coin 15.9M; power 149,209,253. Wheat (food) bubbles
  are still standing over the farmland in the closing screenshot.
  Season II 7d 00:01:22 at the last read, reset about 18:00.
- What was NOT verified - read this before the next harvest unit:
  both taps were aimed at food bubbles and both collected a
  different resource (iron, then coin). The bubble-type
  identification from the downscaled base screenshot is unreliable:
  a tap point that looks like a wheat bubble can sit on an iron or
  coin bubble. Per rule R2 the method must change before the next
  unit of this type taps again: verify the bubble's identity before
  tapping - read its value label and icon at full resolution, or
  confirm the resource total that moves after the first tap before
  tapping a second bubble of the same supposed type. Measurements
  on Issue #250 (already commented there by the ticker pass, no
  duplicate comment here).
- The identical +3.6M on both taps is recorded as observed, not
  explained. One candidate mechanism, NOT verified: a tap clears
  all standing bubbles of one resource type at once (the food
  all-at-once behaviour is already recorded; iron and coin may
  share it). The activity metadata still says iron and coin collect
  one by one (2026-10-25); that line is now marked suspect above
  and the next harvest unit should test it with one tap and a HUD
  re-read, not assume it.
- Armed Truck: the bottom-left toast fragment ("...ies ... loaded,")
  was visible again in this unit's screenshots, still cut off at
  the screen edge and not transcribed, so the fully-loaded notice
  is still unverified and the truck loot unclaimed. The 1803 unit
  should read the notice in full before deciding.
- Titanium bubbles, EXP bubbles: no separate read taken in this
  unit; they carry to the 1803 unit with the food bubbles.
- The 1803 unit should also re-ground every bubble centre fresh in
  its own screenshots; no point from this unit carries over.
- No diamonds spent, no money spent, no Go button tapped, no
  research or building started, no player attacked, no assemble or
  teleport. Game left on the base screen.

## Channel rules, carried 2026-11-07 - Mission Control and background Ctrl+Right lessons (propagation from the 1020 help unit)

- Channel rules, now carried in this profile (propagation follow-up from the 1732 run, resource-collection done - joining alliance-help, alliance-gifts, radar-tasks, arms-race, alliance-donations and shop-claims): Mission Control was not opened as a recovery step, per the 1020 lessons folded into alliance-help 1.27.0 - open_app Mission Control wedged the channel in that pass (first launch opened the overview; every later activate and observe then failed with geometry_mismatch origin_delta 256+, agent_display false, and all key input gated on observation_required; a second launch closed it and restored observation; the overview itself cannot be observed or clicked through this channel). Background Ctrl+Right was not tried: it does not switch Spaces through this channel (in the 1020 pass the key went to the Finder column view instead). The known reliable unblock stands: the owner clicking the LastWar Dock icon once. This profile already records the background-Space-keys half from its own 0034 unit (Ctrl+Right / Ctrl+Left dispatched but the Space did not switch); the new part carried here is the open_app Mission Control wedging (a launch, not a keypress).

## What the 2026-11-08 1935 unit added - food all-at-once re-confirmed, iron one-by-one re-confirmed, coin tap missed, remainder carries

- Unit harvest-2026-11-08-1803 by ticker-1935, about 19:35-19:51
  local, status partial. Evidence in
  `_records_/2026-11-08/resource-collection/1935-queue-run.md`
  (commit 5534be1e on records/2026-11-08). Two bubble taps
  collected verified gains (food +5.1M, iron +1.2M), but coin
  bubbles are still standing and the token window ran out, so the
  sweep is unfinished. The tracker is untouched; the next harvest
  unit picks up the remainder.
- Entry, read live about 19:37 local: base screen, power
  149,209,253; food 494.0M, iron 820.0M, coin 15.9M; diamonds
  13.22K; cart 4,467; stamina 120. Note: food is +3.2M and iron
  +3.1M against the 1759 unit closing read (food 490.8M, iron
  816.9M at about 18:00), with coin unchanged at 15.9M. No
  harvest record exists between 1759 and this unit, so the rise
  is unexplained - possibly collected by another session or at
  the reset. Recorded as observed, not explained; if a later unit
  finds the same pattern, file it as an Issue rather than leaving
  it in prose.
- Wrong tap, about 19:38 local: a tap at norm 490,352 on what
  looked like an orange resource bubble opened a UR Trade Truck
  panel instead ([BI0d]Whodat34, Times plundered 0/2, Next
  Station 04:58:41, Your Plunder Count Today 0/4). Closed at
  once with the panel X. No plunder, no dispatch - truck work
  belongs to the trucks unit. A bubble-shaped orange target at
  the map edge can be a truck, not a bubble; ground the target
  before tapping.
- Tap 1, about 19:44 local: one tap grounded fresh at norm
  335,489 on a green wheat bubble centre in the base interior
  (BASE view, after the map had drifted to a neighbour and was
  recentered). After: food 494.0M to 499.1M (+5.1M, HUD-verified),
  iron unchanged 820.0M, coin unchanged 15.9M. The green wheat
  bubbles cleared from the cluster in the same screenshot. This
  confirms the food all-at-once behaviour: one tap clears the
  standing food bubbles.
- Tap 2, about 19:47 local: one tap grounded fresh at norm
  156,352 on a blue iron bubble centre. After: iron 820.0M to
  821.2M (+1.2M, HUD-verified), food unchanged 499.1M, coin
  unchanged 15.9M. One tap, one iron bubble - iron still collects
  one by one, as the activity metadata says. This also resolves
  the 1759 open question in part: the identical +3.6M on its two
  taps was two different bubbles holding similar amounts, not a
  shared clear.
- Tap 3 (miss), about 19:49 local: a tap at norm 234,452 aimed
  at a yellow coin bubble landed on the Iron Mine building
  underneath and opened its action panel (Iron Mine Lv.27, paw
  and upgrade buttons). Dismissed by tapping empty ground; no
  button was touched, nothing spent, nothing started. HUD
  unchanged (food 499.1M, iron 821.2M, coin 15.9M). The coin
  bubbles were still standing at close. Per rule R2 the method
  must change: zoom the base view in before tapping coin
  bubbles, or tap only a bubble whose yellow coin icon and value
  label are both readable in the screenshot. The coin centre
  coordinates above are NOT verified - re-ground fresh in the
  next unit; do not reuse them blindly. Measurements on Issue
  #250 (commented there by this run).
- Armed Truck: the bottom-left toast fragment was visible again
  in this unit's screenshots, still cut off at the screen edge
  and not transcribed, so the fully-loaded notice is still
  unverified and the truck loot unclaimed. It carries to the next
  harvest unit - read the notice in full before deciding.
- Closing state, read live about 19:50 local: food 499.1M, iron
  821.2M, coin 15.9M; power 149,209,253; diamonds 13.22K. Game
  left on the base screen. One transient observe error ("target
  app exited or restarted") self-resolved on re-list - the app
  never left the frontmost list (pid 1908 throughout).
- No diamonds spent, no money spent, no Go button tapped, no
  research or building started, no player attacked, no assemble
  or teleport. The Iron Mine panel's upgrade button was visible
  and was not touched. The UR truck panel was closed without
  plundering.

## What the 2026-11-08 2310 unit added - partial, 0 bubbles, two verified non-bubbles, HUD rise second occurrence (Issue #490)

- Unit harvest-2026-11-08-2203 by ticker-2308, about 23:10 to 23:26 local, status partial - no resource bubble was collected in this unit. Evidence in `_records_/2026-11-08/resource-collection/2310-queue-run.md` (commit aac215e08 on records/2026-11-08). The tracker is untouched; the next harvest unit picks up the remainder.
- Entry, read live about 23:12 local: base screen, power 149,209,253; food 501.9M, iron 824.0M, coin 15.8M; gold 13.22K; diamonds 6,027; stamina 120. Against the 1935 unit closing read (food 499.1M, iron 821.2M, coin 15.9M at about 19:50) with no harvest record between: food +2.8M, iron +2.8M, coin -0.1M. Same unexplained pattern the 1935 record flagged for 18:00-19:50 (food +3.2M, iron +3.1M), so per its instruction this is now GitHub Issue #490 (labels records), not prose only. Harvest gains measured as HUD deltas across units are not clean until it is resolved.
- The game opened on the Secret Command Post screen (Hidden Treasure event, map pieces M1 x16, M2 x13, M3 x2, M4 x6, M5 x4, M6 x6, M7 x12, chest 8/15) - the 2255 treasures unit's closing state. One back-arrow tap returned to the base view. No event action was taken - this unit is harvest only.
- Wrong tap 1, about 23:13 local: a tap at norm 701,468 on what looked like a gold diamond resource bubble opened the Area No.168 zombie NPC dialogue ("True dread struck me upon seeing the eyes of the zombies"). The gold diamond is the NPC marker, not a bubble. Dismissed by tapping empty ground; no button was touched. Note: this is the same Area No.168 dialogue the 2227 survivors unit opened from the lone figure at the gate - the NPC marker and the dialogue are the same object.
- Wrong tap 2, about 23:17 local: a tap at norm 565,636 on an orange sack icon above the purple crystal building selected the Recon Plane Lv.24 building and showed its green upgrade arrow. The orange sack is that building's indicator, not a bubble. Dismissed by tapping empty ground; the upgrade arrow was not touched, nothing started.
- Pans, all live: pan 1 (drag norm 500,400 to 500,700) moved the view to the foggy top edge of the base; no bubbles visible, only cloud cover. Pan 2 (drag back 500,650 to 500,350) returned to the original base view; no green wheat, blue iron or yellow coin bubble readable in it. Pan 3 (drag 200,500 to 450,500) revealed the left side of the base (clock tower, blue crystal, flower monument, golden statue, pink car, two glass domes); still no resource bubble readable. Two small circular portrait icons (about norm 285,505 and 110,595) are NPC markers, not bubbles.
- METHOD CHANGE under rule R2: recenter the base view FIRST (the 1935 unit recentered after the map drifted; this unit only panned blind), then sweep systematically, and tap only a bubble whose icon and value label are both readable in the screenshot. Do not reuse the norm 701,468 or 565,636 coordinates - both are verified non-bubbles. The bubble cluster itself was not re-found: the coin bubbles the 1935 unit left standing (left cluster, about norm 132,436 and 234,452) and the further iron bubble were not re-found in any view this unit panned to.
- Armed Truck: the fully-loaded notice is still unverified and the truck loot unclaimed; it carries to the next harvest unit.
- Closing state, read live about 23:26 local: food 501.9M, iron 824.0M, coin 15.8M; power 149,209,253; diamonds 6,027. HUD unchanged across the unit - nothing was collected, nothing spent. Game left on the base screen.
- Red lines held: no diamonds spent, no money spent, no upgrade or research started, no player attacked, no assemble or teleport. The Recon Plane upgrade arrow was visible and was not touched. The Secret Command Post screen was left without digging.
- Result stats: target not stated, achieved 0 bubbles, resources_gained none, costs about 16 minutes, verified no, blocker_category c, follow_up recenter-first sweep.

## What the 2026-11-09 0202 unit added - partial, 0 bubbles, resource quarter not reached again, Armed Truck entry still unlocated, skull timer re-seen (Issue #498)

- Unit harvest-2026-11-08-2203 by ticker-0140, about 01:52 to 01:55 local, status partial. Evidence in `_records_/2026-11-09/resource-collection/0202-queue-run.md` (commit 3d5dc8314 on records/2026-11-09). Computer session cc-207. Observe and collect only.
- Base HUD at entry (01:53) and at close (02:02), unchanged: food 513.8M, iron 838.3M, coin 25.2M, diamonds 6,027, power 149,209,253; stamina 61 rising to 62. No HUD rise this unit - the Issue #490 rise (second occurrence at 2310) did not recur.
- View 1, south snow area (entry view): barracks and tanks at the top, empty snow below with a cannon. No resource bubbles visible over any building. View 2, north area (after one drag down from (320,300) to (320,600)): tents with survivor smiley markers, blue dome buildings, purple crystal, gift-box decoration, barracks. Building status markers seen (tent smileys, a blue helmet, a red face, a green icon over the orange building) - none is a resource bubble. No gold, wheat or iron bubble with a value label anywhere in either view.
- The resource buildings (farms, iron, stone, gold) sit in a part of the base neither view reached. The 2310 unit on 2026-11-08 hit the same wall (three blind pans, cluster never found). Correction to the 2310 follow-up: the recenter-first sweep was NOT executed in this unit either - it swept the troop areas again. The standing rule (bubbles full equals production stalled) makes this a carry, not a close: the next harvest unit must pan the view to the resource quarter first instead of sweeping the troop areas again.
- Left-column map re-confirmed in the 642x951 window: the blue bus icon at (55,573) opens the Trucks screen (already read by the 0150 scout unit this pass: Today's Trade Count 0/5); the white truck icon at (55,652) opens the Secret Command Post, not the Armed Truck - matching the 2026-11-03 measured column map ((52,626) Secret Command Post), the point rotated with the column set. The Armed Truck loot-panel entry stays unlocated, as the activity metadata records; its loot state stays unverified.
- Carried observation, skull timer: the skull icon at the right edge mid-screen reappeared during this unit with a red badge 4 and a 00:00:23 countdown (the 0150 scout unit saw badge 1 with 00:00:24 about 01:57, then the icon vanished). At close it read about 00:00:40. The badge count and the timer do not behave like a single countdown; meaning still unverified, not opened. Filed as knowledge Issue #498 by this run - do not tap it blind.
- No bubble collected (0). No view reached the resource quarter. Armed Truck not checked (entry unlocated). Tracker untouched: the regular stays due and the next tick re-produces it. No diamonds or money spent.
- Result stats: target unknown (bubble count not established in the views swept), achieved 0, resources_gained none, costs about 9 minutes of unit time, no items spent, verified yes, blocker_category c.

## What the 2026-11-09 0340 unit added - one tap per type clears all bubbles of that type, contradicting the 1935 iron one-by-one re-confirmation (Issue #502)

- Unit harvest-2026-11-09-0203 by ticker-0334, about 03:40 to 03:52 local, status partial - the resource quarter was swept; the full-map zero-remaining acceptance is not met (other pans and the Armed Truck loot state unchecked). Evidence in `_records_/2026-11-09/resource-collection/0340-queue-run.md` (commit 063a5bde7f on records/2026-11-09).
- Entry: the game was on the world map after the radar unit's Iron Mine gathering dispatch (March Queues 1/4, Gathering 00:05:48 remaining at unit start). BASE returned to the base view. HUD at unit start, rounded as displayed: food 534.7M, iron 859.3M, coin 38.6M, second-row first resource 13.22K, power 149,217,331, stamina 83.
- RECENTER-FIRST EXECUTED, discharging the 0202 follow-up: the centred base view showed no collectible bubble with a readable value label - the small green ticks on the iron-mine buildings are building status markers, not bubbles (verified on a 3x magnified crop). One long drag on empty road (norm 300,500 to 700,500) panned the view west to the resource quarter, where the bubble cluster stood with readable labels. This is the first unit to actually execute the recenter-first sweep the 2310 follow-up ordered and the 0202 unit failed to execute.
- Bubble identification, read at full resolution before tapping: yellow circles with an EXP book icon and "1.8M" (experience), green circles with a blue iron ingot icon "876.8K", "1.0M", "974.9K", "974.9K" (iron), green circles with a gold coin icon "952.4K", "876.0K", "880.1K" (coin), yellow circles with a bread icon "1.1M" (food).
- Collections, each one tap on a freshly grounded bubble centre, HUD-verified in the same unit:
  - Iron: one tap on the 974.9K iron bubble centre (norm 671,397) cleared all four visible iron bubbles at once. Iron 859.3M to 864.2M, plus 4.9M.
  - Coin: one tap on the 952.4K coin bubble centre (norm 510,423) cleared all three visible coin bubbles at once. Coin 38.6M to 42.9M, plus 4.3M.
  - EXP: one tap on a 1.8M EXP bubble centre (norm 343,442) cleared all four EXP bubbles at once. No HUD resource measures EXP; clearance is verified visually on the follow-up screenshot.
  - Food: one tap on a 1.1M food bubble centre (norm 670,457) collected the food bubbles (bread icons seen flying in the collection animation). Food 534.7M to 540.1M, plus 5.4M.
- CONTRADICTION, recorded as observed: one tap on a bubble of a resource type cleared every standing bubble of that type, not one bubble. This contradicts the 2026-11-08 1935 unit's iron one-by-one re-confirmation (one tap, exactly one iron bubble, +1.2M) and the profile line built on it. The iron and coin one-by-one lines are SUSPECT again, not settled; the 1935 read stands as a single-bubble-remaining read or a different standing condition, not deleted. The HUD deltas also exceed the sums of the visible bubbles of each type (iron +4.9M against 3.83M visible, coin +4.3M against 2.71M visible, food +5.4M against about 3.3M visible), which suggests the tap collects that type base-wide, including bubbles off-frame - a candidate mechanism, NOT verified. Filed as knowledge Issue #502 by this unit; the knowledge organizer comments the fold onto #502. Until #502 is resolved, fold sections record per-type clears as observed and do not re-assert one-by-one for any type.
- Not done in this unit: the remaining base pans (farmland area, top and far-left edges) were not re-swept after the quarter clear; the Armed Truck loot state was not checked (its loot-panel entry is still unlocated); the Season 2 area at the bottom was left out of the sweep, per the standing rule that it is not main-base harvest. Bubbles regenerate within minutes, so the quarter will need re-sweeping by the next harvest unit.
- No diamonds or money spent, no Buy tapped, no building panel actioned, no other activity worked from this unit. Tracker untouched for partial, per the queue rules.
- Result stats: target unknown (bubble count not established before the sweep), achieved 4 types swept, resources_gained iron +4.9M coin +4.3M food +5.4M EXP 4 bubbles, costs about 12 minutes, verified yes for the per-type clears, blocker_category none stated in the record.

## What the 2026-11-09 0636 unit added - one tap per type clears all a second time, blue-triangle 596 bubbles unidentified (Issue #508)

- Unit harvest-2026-11-09-0603 by ticker-0634, about 06:36 to 06:53 local, status partial - the 15-minute cap was reached mid-work; the EXP bubble and the Armed Truck loot check remain. Evidence in `_records_/2026-11-09/resource-collection/0636-queue-run.md` (commit 04b12d13 on records/2026-11-09). Computer session cc-228; every tap needed the fresh observation_id from the last observe.
- HUD, read live from screenshots: before (06:37) food 540.1M, iron 864.9M, coin 42.9M, diamonds 6077, stamina 118, total power 149,217,331, second-row figure 13.22K. After (06:49): food 542.1M, iron 866.8M, coin 44.2M, diamonds 6077, stamina 120, total power 149,217,331, second-row figure 13.22K unchanged. (OCR in the control channel misreads the food total 542.1M as 541.1M; HUD figures in this record are from the screenshots, not the OCR text.)
- Collections, each one tap on a freshly grounded bubble centre, HUD-verified in the same unit:
  - Coin: one tap on a gold coin bubble cleared all five standing coin bubbles (287.3K, 264.3K, 265.5K, 228.6K, 249.3K read live) - coin 42.9M to 44.2M, about +1.3M, matching the summed bubble values.
  - Food: one tap on a bread bubble cleared all five standing bread bubbles (413.6K, 433.9K, 380.0K, 394.2K, 338.4K read live) - food 540.1M to 542.1M, about +2.0M, matching the sum.
  - Iron: one tap on a grey-blue ingot bubble cleared all four standing iron bubbles read live in the farm crop (407.5K, 385.4K, 368.9K, 366.9K, sum about 1.53M) - iron 864.9M to 866.8M, about +1.9M. The HUD rise exceeds the four read bubbles by about 0.37M, unattributed - likely further iron bubbles elsewhere on the base that the same tap cleared; the four-bubble sum and the HUD delta are both recorded as read.
  - Blue-triangle bubbles: one tap cleared all four yellow-circle blue-triangle bubbles over the orange furnace buildings, each labelled 596 - no HUD total moved. Resource unidentified; filed as knowledge Issue #508 by this unit. Candidates, unverified: oil from the Age of Oil event or a furnace output landing in inventory.
- RESOLUTION of the #502 contradiction, in favour of the newest verified records: this is the second independent one-tap-per-type confirmation (0340, 0636), against the single 1935 one-tap-one-bubble read. One-tap-per-type is now the standing rule in the profile; the 1935 read stands as a single unexplained outlier, not deleted. The base-wide-collection candidate (HUD deltas exceeding read bubble sums) is still NOT verified. Issue #502 stays open; closure belongs to the daily retro.
- Method learning: bubbles regenerate fast - fresh coin bubbles of about 8K each were standing again within minutes of the collection. Not chased, per the activity rule - collect what is ready in a pass and move on.
- Not done in this unit: EXP bubble - a light-blue EXP bubble of about 490K stands at the far left edge of the base, partly off-screen (centre near x 15, y 432); not tapped, the unit cap was reached; first action of the next harvest unit. Armed Truck loot: not checked - the gold circle with a blue gem above the blue truck vehicle turned out to be a radar shortcut, not the truck loot; tapping it opened the world/radar map, which showed "6 task rewards can be claimed" with a Claim All button. Those rewards belong to the radar unit and were left untouched; the game was returned to base with the Home button. The truck vehicle itself was not tapped, so whether the Armed Truck loot is ready is unverified. Fresh coin bubbles (about 8K each, five standing at 06:49) left standing.
- No diamonds or money spent, no speedup used, no purchase tapped. Tracker untouched for partial, per the queue rules.
- Result stats: target collect all standing bubbles to zero, achieved 3 types (food, iron, coin), resources_gained food +2.0M iron +1.9M coin +1.3M blue-triangle 4x596 unidentified, costs about 17 minutes of unit time, no items spent, verified yes, blocker_category h, issue 508.

## What the 2026-11-09 1220 unit added - third one-tap-per-type confirmation, panel swipe-close method, Armed Truck loot unchecked

- Unit harvest-2026-11-09-1003 by ticker-1204, about 12:06 to 12:20 local, status done. Evidence in `_records_/2026-11-09/resource-collection/1220-queue-run.md` (commit 6f18bc3be on records/2026-11-09). All visible bubbles collected; closing screenshot verified no iron, coin or food bubble remains anywhere on the base screen.
- HUD, read live: before - food 544.5M, iron 871.8M, coin 46.2M, diamonds 6,077, total power 149,217,331, stamina 120, building queue 1/4, research 1/2. After - food 548.4M (+3.9M), iron 875.4M (+3.6M), coin 48.8M (+2.6M), the rest unchanged.
- Collections, HUD-verified in-unit: iron 5 bubbles (630.7K, 719.9K, 739.5K, 701.3K, 703.9K read on the enlarged crop); coin 4 bubbles (569.4K, 523.9K, 526.2K, 453.0K re-read just before the taps); food one tap on the 862.2K bread bubble collected all farmland at once - the second bread bubble (669.0K) cleared with it and the HUD rose 3.9M, more than the two visible bread bubbles, so further farmland bubbles off the crop cleared too. One-tap-per-type is now grounded in three verified units (0340, 0636, 1220); the base-wide-collection candidate is still NOT verified. Issue #502 stays open; closure belongs to the daily retro.
- Panel incidents (no harm, nothing spent): the iron batch's last tap opened the Iron Mine Building Details panel (Lv.27, Output/hr +110,681, Max Production Time 11hr 36min, Survivors Charles, Jolene, Alyssa as Miners) and then its Survivor List (Alyssa already assigned, Harry's row highlighted by a batch tap) - the Select button was never tapped, no survivor assigned or changed. The coin batch's third tap opened the Gold Mine Building Details panel (Lv.30, Output/hr +98,064, Max Production Time 12hr, Survivors Madison, William, Amanda, Rebecca as Gold Miners) - Quick Dispatch never tapped. Both panels were left by the left-edge swipe-back gesture (drag from x 20 to 200 at y 500), which closes one level per drag; the panel X does not respond to background clicks. The swipe is now the working panel close method for this input route, and it is also the answer to the 1204 Builders Hut unit's stuck upgrade panel.
- Method learning: tap bubbles one at a time with a screen read between taps when a batch tap has just opened a panel - a batch that continues into an open panel taps panel rows. Bubble centres must be re-grounded from an enlarged crop, never from the downscaled full screenshot (the first tap of this unit at 210,589 hit a building, not a bubble, for exactly that reason).
- Not done in this unit: Armed Truck loot NOT checked - the unit hit its 15-minute cap at the food verification; the truck check is the follow-up for the next harvest unit, together with the EXP bubble (about 490K at the far left edge, partly off-screen). The yellow question-mark chest bubble near the truck is not a resource bubble and was left for the treasures unit. Issue #508 gets no new evidence from this unit - no furnace panel was read and no 596 bubble was seen.
- No diamonds or money spent, no speedup used, no purchase tapped. Tracker untouched for done, per the queue rules.
- Result stats: target collect-all-visible-resource-bubbles, achieved 1, resources_gained food +3.9M iron +3.6M coin +2.6M, costs about 14 minutes of unit time, no items spent, verified yes, blocker_category none, points 0, surfaces_walked base-screen-resource-bubbles-iron-mine-panel-gold-mine-panel, items_observed 11.
