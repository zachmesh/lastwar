---
title: Resource Collection
created: 2026-10-25T18:58:00Z
modified: 2026-11-01T20:40:00Z
level: L1
version: 1.4.0
description: Collecting building output bubbles and truck loot, one activity folder for collection knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: resource collection execution record 2026-11-01 1149 queue run
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

## Open questions

- The capacity cap per building, and how long until output stops
  accumulating when bubbles are left uncollected.

## Changelog

- 1.3.0 (2026-11-01): balloon-versus-bubble distinction, HUD
  button mis-tap point, base-view pan failure mode, and the
  2343 negative result, folded from the 2343 harvest unit and
  the 0016 survivors unit; no earlier claim superseded.
- 1.4.0 (2026-11-01): five-bubble inventory with the
  one-tap-clears-all farmland confirmation, the HUD
  rounding precision note, and the Armed Truck check
  deferred to the next harvest unit, folded from the 1149
  harvest unit; no earlier claim superseded.
