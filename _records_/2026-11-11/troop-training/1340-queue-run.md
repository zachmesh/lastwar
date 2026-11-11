---
title: Troop training queue run 1340
created: 2026-11-11T21:40:00Z
modified: 2026-11-11T21:53:00Z
version: 1.0.0
description: Ticker-1332 training unit - no barracks checked, tent grounding missed again, Iron Mine selected instead, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 13:36-13:46 PT
---

# Troop training queue run 1340 (ticker-1332)

Unit: training-2026-11-11-1003. Status: partial.
Activity: troop-training. Computer session cc-620.

## What happened

- Entry: the game was left on the radar world map by the 1204 radar
  unit (Lv.13, points 427, stored 0/40, stamina 70, "Fully restore
  at 11-12 17:39:11 local time" - matches the 1233 close). Two
  taps on the Home button failed with no change: an estimated
  point (688,958) and the visually grounded point (645,950).
  The back arrow, visually grounded at (326,948) and tapped with
  snap_to_control=false, returned to the base screen. Lesson: in
  this fullscreen framing the Home button does not respond to
  these taps; the back arrow is the working exit from the radar
  map. The snap variant is not the difference - the first two
  Home taps used the default snap and the back-arrow tap used
  snap_to_control=false, but the tent tap below also used
  snap_to_control=false and still missed, so the point, not the
  variant, decides.
- Base HUD at entry: food 687.5M, iron 1.0G, coin 134.7M,
  diamonds 6,717, total power 149,218,973. "Build: Oil Well
  (0/1)" task line at the bottom.
- Tent grounding missed again: visual grounding on the base
  screenshot returned four "beige barracks tent" boxes
  (500-550, 520-575; 538-592, 590-665; 575-628, 540-615;
  608-663, 492-562). A tap at the centre of the third box
  (602,578) selected nothing - no label, no action row, no
  change on the next screenshot. The boxes sit on the road /
  empty ground between the parked vehicles, not on verified
  tents, repeating the 0548 unit's warning that grounding
  boxes must be verified against the live screenshot, not
  trusted blindly. One no-change tap only; the point was not
  re-tapped.
- Drill Ground read did NOT happen: the grounding box for the
  "drill ground training field" (305-485, 300-610) was tapped
  at its centre (395,455) and produced no change on the
  receipt. The closing screenshot, however, shows the camera
  re-framed and "Iron Mine Lv.27" selected with its action row
  (blue paw and green up arrow at about image (390,370) and
  (430,370)) - the tap landed on the Iron Mine, not on the
  Drill Ground. Nothing on the Iron Mine was tapped (no paw,
  no green upgrade arrow). The Drill Ground screen was not
  opened and its Full state was not read live in this unit.
- New grounding for the next unit, from the closing screenshot:
  Iron Mine Lv.27 selects at norm (395,455) in this framing;
  the red troop formation (Drill Ground candidate) is visible
  at the bottom-right edge of the closing view, image about
  (850-980, 560-660). The next unit should start from this
  closing framing and tap the red formation directly, not
  re-ground from the opening view.

## Not done - stated plainly

- 0 of 4 barracks checked. No TRAIN UNITS panel opened, no batch
  collected or queued, no barracks busy/idle state verified.
- Carried, not re-read: Lv.24 T8 x666 batch queued 2026-11-10
  12:29, expected running until about 16:49 today (0548 unit
  read "Training in progress 11:01:26" at 05:48); Lv.27 idle
  and requeue-blocked by Drill Ground Full at 21:46 yesterday
  (2146 unit); Lv.30 and the fourth barracks unchecked.
- The Drill Ground live read that unit 2146 assigned as this
  unit's first action did NOT happen. How a full Drill Ground
  is cleared is still unknown from a live read; Quick Dispatch
  stays untapped (owner decision).
- This is another same-blocker partial for open Issue #150
  (barracks tents not located / Drill Ground never re-read);
  the recurrence is commented onto #150, not filed as a new
  issue.

## Close

- Game left on the base screen with Iron Mine Lv.27 selected,
  no panel open, no purchase, no diamond spend, no Finish Now,
  no upgrade shortcut, no speedup burned. No different-device
  dialog, no login or verification demanded. Tracker untouched;
  the next tick re-produces the regular.
- Unit time: claimed 13:36, game work 13:36-13:46, closed
  partial after 9 minutes 23 seconds, inside the 15-minute cap.
  (The record's first draft overstated the session as ending
  13:53; the queue tool's own timestamps govern: started
  21:36:19Z, finished 21:45:42Z.)
