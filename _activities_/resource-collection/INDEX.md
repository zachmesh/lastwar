---
title: Resource Collection
created: 2026-10-25T18:58:00Z
modified: 2026-11-05T13:35:09Z
level: L1
version: 1.27.0
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
- Food is special - tapping any one farmland bubble collects all
  farmland bubbles at once (observed the same evening, food rose
  about 0.4M in one tap and every farmland bubble cleared). Iron
  and coin bubbles collect one by one.
- Check the Armed Truck and claim it when it shows fully loaded.

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

## Changelog

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
