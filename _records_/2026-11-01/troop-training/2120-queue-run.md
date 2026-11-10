---
title: Queue Run 2120 Troop Training Partial
created: 2026-11-01T21:20:00-08:00
modified: 2026-11-01T21:20:00-08:00
version: 1.0.0
description: Ticker pass ticker-2104 training unit, partial, device takeover handled, barracks tents still not located after north and south pans
status: partial
---

# 2120 queue run - troop training, partial

Session window: 2026-11-01 about 21:07 to 21:20 America/Los_Angeles.
Executor: ticker-2104. Unit: training-2026-11-01-1803 (regular
training, activity troop-training).

## Outcome

- Status: partial. No barracks panel was opened, no batch was
  queued, no Drill Ground screen was read, and nothing was
  claimed. The tracker is left untouched, so the next tick
  re-produces the regular and the work resumes as a fresh unit.
- One different-device takeover, handled under the owner rule:
  the "active on a different device" dialog appeared mid-unit,
  Confirm was tapped once, the app exited as expected, and it
  was relaunched and back at the base screen with no login or
  verification demanded. No second dialog appeared.
- No diamonds or money spent, no paid button tapped, no Finish
  Now, no upgrade shortcut, no other activity worked from this
  unit.

## Entry path measured fresh in this unit

1. Base screen at unit start, HUD read live: food 353.1M, iron
   543.9M, coin 30.1M, diamonds 2,396, power 149,288,895. After
   the relaunch the HUD read food 359.5M, iron 550.3M, coin
   34.2M, diamonds 2,416, same power - production ticks only,
   no claim made.
2. Visual grounding for a barracks tent timed out (3 minutes,
   no result) and was abandoned, not retried - do not repeat a
   grounding call inside a 15 minute unit after a timeout.
3. Scroll gestures did nothing to the game view; drag pans are
   the working move, and their mapping is now measured: drag
   from norm y 300 to y 700 moves the view south, the reverse
   moves it north. A full-length drag crosses most of the base.
4. South pan: reached the map south edge again - the Season 2
   house cluster, a tank, a STOP sign, formation lots 2 and 3
   at the top. This repeats the 1651 south route and adds
   nothing new; the houses there are not verified barracks.
5. North pan: reached the map north edge - the same house
   cluster at the top and empty snow below. No barracks tent
   in either edge view.
6. Half-length drag back south landed near the start view:
   house cluster top left, cannon and tank, empty snow below.
   The dense red-roofed formation of the very first screenshot
   was not in this view either, so it lies further east or
   north-east of the start view, unreached in this unit.

## What this rules out

- Barracks tents are not at the map south edge or the map
  north edge at this zoom level. The next unit must change the
  route again before repeating this work (rule R2): pan east
  from the start view toward the dense red-roofed formation
  seen in the first screenshot of this unit, and only tap a
  tent that is visually verified as a tent, never a point that
  sits on the gate road or the house cluster. Do not repeat
  the south or north pans, and do not spend a grounding call
  inside the unit budget after a timeout.
- The 2026-10-31 Drill Ground Full blocker was neither
  confirmed nor cleared in this unit: no barracks was reached,
  so no Drill Ground figure is claimed here.

## Closing figures

- Batches queued: 0, read live as no panel opened.
- Barracks checked: 0 of 4. Drill Ground count: not read.
- Device takeovers in this unit: 1, completed, no contest.
- Closing figures are unverified by design here: nothing was
  claimed, so there is no closing counter to read live.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No base move, no Assemble, no teleport.
