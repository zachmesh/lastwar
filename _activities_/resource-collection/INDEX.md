---
title: Resource Collection
created: 2026-10-25T18:58:00Z
modified: 2026-11-02T17:05:00Z
level: L1
version: 1.9.0
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


## Open questions

- The capacity cap per building, and how long until output stops
  accumulating when bubbles are left uncollected.
- The drone component bubble's spot: still unidentified after
  the 1534 pass (the 164,116 top-left-corner candidate is
  unverified); the next harvest pass must locate it on screen
  rather than assuming the candidate.

## Changelog

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
