---
title: Queue Run 2310 Harvest
created: 2026-11-09T07:28:00Z
modified: 2026-11-09T07:28:00Z
level: L0
version: 1.0.0
description: Unit harvest-2026-11-08-2203, partial - no bubbles collected, two mis-taps, bubble cluster not located in the views panned
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 23:10-23:26 America/Los_Angeles
---

# 2310 queue run - harvest (harvest-2026-11-08-2203)

- Unit: harvest-2026-11-08-2203, executor ticker-2308.
  Status: partial - no resource bubble was collected in
  this unit. Two taps hit non-bubble targets (a zombie
  NPC dialogue and the Recon Plane building panel) and
  three pans of the base view never revealed the
  farmland / iron-mine bubble cluster, so the sweep is
  unfinished. The tracker is untouched; the next
  harvest unit picks up the remainder.
- Session: computer session cc-187 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No
  device-access error, no different-device dialog, no
  login demanded. LastWar was already running
  (pid 1908, window 642x951) and was selected by
  list_windows and activate before any input.
- Issue filed this unit: #490, the unexplained HUD
  rise between harvest units (see below). Class
  records.

## What was read live in this unit

- Entry, read live about 23:12 local: base screen,
  power 149,209,253; food 501.9M, iron 824.0M, coin
  15.8M; gold 13.22K; diamonds 6,027; stamina 120.
  Against the 1935 unit closing read (food 499.1M,
  iron 821.2M, coin 15.9M at about 19:50) with no
  harvest record between: food +2.8M, iron +2.8M,
  coin -0.1M. Same unexplained pattern the 1935
  record flagged for 18:00-19:50, so per its
  instruction this is now Issue #490, not prose only.
- The game opened on the Secret Command Post screen
  (Hidden Treasure event, map pieces M1 x16, M2 x13,
  M3 x2, M4 x6, M5 x4, M6 x6, M7 x12, chest 8/15).
  One back-arrow tap returned to the base view. No
  event action was taken - this unit is harvest only.
  The Secret Command Post state (Hidden Treasure
  8/15) belongs to the secrets unit, not this one.

## Taps and pans, all live in this unit

- Wrong tap 1, about 23:13 local: a tap at norm
  701,468 on what looked like a gold diamond resource
  bubble opened the Area No.168 zombie NPC dialogue
  ("True dread struck me upon seeing the eyes of the
  zombies"). The gold diamond is the NPC marker, not
  a bubble. Dismissed by tapping empty ground; no
  button was touched.
- Wrong tap 2, about 23:17 local: a tap at norm
  565,636 on an orange sack icon above the purple
  crystal building selected the Recon Plane Lv.24
  building and showed its green upgrade arrow. The
  orange sack is that building's indicator, not a
  bubble. Dismissed by tapping empty ground; the
  upgrade arrow was not touched, nothing started.
- Pan 1, about 23:21 local: drag from norm 500,400
  to 500,700 moved the view to the foggy top edge of
  the base; no bubbles visible, only cloud cover.
- Pan 2, about 23:23 local: drag back from norm
  500,650 to 500,350 returned to the original base
  view; no green wheat, blue iron or yellow coin
  bubble readable in it.
- Pan 3, about 23:25 local: drag from norm 200,500
  to 450,500 revealed the left side of the base
  (clock tower, blue crystal, flower monument, golden
  statue, pink car, two glass domes); still no
  resource bubble readable. Two small circular
  portrait icons (about norm 285,505 and 110,595)
  are NPC markers, not bubbles.
- Closing state, read live about 23:26 local: food
  501.9M, iron 824.0M, coin 15.8M; power 149,209,253;
  diamonds 6,027. HUD unchanged across the unit -
  nothing was collected, nothing spent. Game left on
  the base screen.

## What was NOT verified - read this before the next harvest unit

- The bubble cluster itself: the coin bubbles the
  1935 unit left standing (left cluster, about norm
  132,436 and 234,452) and the further iron bubble
  were not re-found in any view this unit panned to.
  Per rule R2 the method must change again: recenter
  the base view first (the 1935 unit recentered after
  the map drifted; this unit only panned blind), then
  sweep systematically, and tap only a bubble whose
  icon and value label are both readable in the
  screenshot. Do not reuse the norm 701,468 or
  565,636 coordinates - both are verified non-bubbles.
- Armed Truck: the fully-loaded notice is still
  unverified and the truck loot unclaimed; it carries
  to the next harvest unit.
- Issue #490 (HUD rise with no intervening harvest
  record) is open; harvest gains measured as HUD
  deltas across units are not clean until it is
  resolved.

## Red lines

- No diamonds spent, no money spent, no upgrade or
  research started, no player attacked, no assemble
  or teleport. The Recon Plane upgrade arrow was
  visible and was not touched. The Secret Command
  Post screen was left without digging. Game left on
  the base screen.
