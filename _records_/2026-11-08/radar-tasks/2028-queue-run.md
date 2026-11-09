---
title: Radar queue run 2028
created: 2026-11-09T04:24:00Z
modified: 2026-11-09T04:24:00Z
level: L0
version: 1.0.0
description: Ticker-2002 radar unit, partial - release day, radar screen never entered, dish grounding failed twice, game left on research tree
status: unverified
---

# 2028 queue run - Radar tasks

Executor: ticker-2002. Unit: radar-2026-11-08-1803 (window
"duel day 7 - radar stack", stamped at production before the
rollover). Session window about 20:15 to 20:24
America/Los_Angeles.

## Posture

- Live duel posture from tools/duel.py at entry: duel day 1,
  Radar Training, radar_posture RELEASE, day ends
  2026-11-09 18:00 local. The unit window stamp (day 7
  stack) is stale - the duel week rolled at about 18:00
  local today. The live posture governs, so this unit ran
  as a RELEASE unit: claim everything claimable, pins
  included. The roughly 5 minute dead window after the
  roll is long past (entry 20:15). The delta test (VS
  panel duel score before and after) is still owed - no
  VS read was taken in this unit.
- Opening state carried from the 1355 unit (13:53 local):
  Lv.13, radar points 267, stored 16 of 40, stamina 92,
  full restore 11-8 22:32:10 local, 10 rewards pending
  behind a Claim All only bar, 6 pins inventoried
  untapped. No live radar read was obtained in this unit,
  so every figure here is carried, not re-measured.

## Performed

- Nothing executed, nothing claimed, no map pin tapped.
  The radar screen was never entered.
- Entry failure, first attempt: the satellite dish icon
  was grounded at norm (54,583) from a visual-grounding
  call on the 20:17 base screenshot. The tap opened the
  Intercity Trade (trucks) panel instead - "Today's
  Trade Count: 0/5", four trucks standing, Mega Mode
  button. Backed out untouched with the back arrow at
  (55,931), which returned to the base at once. The
  grounding tool mislabelled the truck slot as the dish
  - the same mislabel the profile records for the 0636
  unit. Incidental read only: trade count 0/5 today
  (the trucks regular owns it; nothing dispatched or
  plundered from this unit).
- Entry failure, second attempt (R2 pivot - re-grounded
  fresh from an enlarged crop of the left column, switched
  to a crop-measured point): the tap at norm (54,780)
  opened the BUILD menu (Economy tab: Oil Well, Drone
  Parts Workshop, Farmland, Iron Mine, Food Warehouse).
  The crop measurement put the dish lower than the
  control that actually sits there - the build/hammer
  icon. Nothing built, nothing tapped in the menu.
- Recovery failure: the tap at (113,888) on the Build
  screen's bottom-left list icon opened THE AGE OF OIL
  research tree instead of closing the menu (all nodes
  0/10, queue timers 20:13:57:39 and 08:47:50 - read
  only, no research started, nothing spent). Two taps
  on the tree's back arrow at (109,894) and at the
  re-grounded centre (131,898) produced no change; the
  control channel returned explicit guidance that
  background clicks do not reach some controls and to
  use click_element with the control's visible label, or
  the keyboard, instead. Return and Esc are never used
  on this app. Per R2 the tap method ended there.
- Game left on THE AGE OF OIL research tree at the
  unit's close. No state changed, nothing spent, no
  research started, no claim made - the 10 pending
  rewards and the 16 stored tasks are still waiting
  for the next radar unit, and no claim leaked onto a
  non-scoring day (today IS the scoring day; the
  rewards are simply still unclaimed).

## Closing reads

- No live radar reads in this unit: stored, pending
  rewards, radar points, stamina and restore line are
  all unverified carries from the 1355 unit (16 of 40,
  10 pending, 267 points, stamina 92, full restore
  22:32:10 local). The next radar unit must re-read
  them live on the radar screen itself.
- Base HUD read live about 20:17 local: power
  149,209,253, food 499.1M, iron 821.2M, coin 15.9M,
  diamonds 13.22K, cart 4,467, stamina 120, VS timer
  21:43:24, Season II 6d 21:43:23. Wanted Boss badge 1,
  timer 00:00:53 at 20:07; badge 2, timer 00:00:49 at
  20:19.

## Outcome

Partial. Release-day radar work not started: the screen
was never entered, so the Claim All bar, the stored
tasks and the pins all stand unworked. The next radar
unit opens with (a) the release-day claim still pending
(10 rewards plus 16 stored tasks, duel day 1, claims
score +30,000 each as displayed), (b) the dish entry
still ungrounded - the (50,740) point that opened the
radar first try at 13:53 today is the next point to try,
NOT the (54,583) or (54,780) points used here, and (c)
the game sitting on THE AGE OF OIL research tree with
its back arrow unresponsive to background clicks -
  back out with click_element on the arrow if the
  catalog names it, or relaunch the app (state is
  server-side; prior units relaunched after crashes
  with no loss), then re-ground the dish from a fresh
  full-HUD base screenshot. Tracker untouched for
  partial, per the queue rules.

## Delivery note - method finding for the next unit

- The visual-grounding tool mislabelled the dish slot
  twice in one unit (truck slot as dish at 20:17; the
  crop-measured dish point landing on Build at 20:24),
  and the research-tree back arrow does not respond to
  background clicks at all. Both are method findings,
  not game state; the radar profile already documents
  the grounding mislabel (0636, 1913, 0226 units) and
  the back-arrow guidance is new in this unit. No
  diamonds, money, speedups or other spending. No
  alliance diplomacy, no assembly, no teleport.
