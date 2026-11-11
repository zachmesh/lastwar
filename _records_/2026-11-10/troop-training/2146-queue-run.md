---
title: Troop training queue run 2146
created: 2026-11-11T05:46:00Z
modified: 2026-11-11T05:46:00Z
version: 1.0.0
description: Ticker-2122 training unit - Lv.27 barracks finished batch of 313 Lv.9 collected (+423,176 power), requeue blocked by Drill Ground Full toast, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 21:37-21:46 PT
---

# Troop training queue run 2146 (ticker-2122)

Unit: training-2026-11-10-1803. Status: partial.
Activity: troop-training. Computer session cc-512.

## Entry - tents located from a fresh grounding, no pans

- The game was left on the Alliance Techs screen by the
  donations unit of this pass. Closed the Techs panel (X)
  to the Alliance menu, then the back arrow to the base
  screen.
- Base screen at entry: food 644.3M, iron 967.4M, coin
  105.9M, gold 13.22K, Total Power 148,787,578, stamina
  46, diamonds 6,267. VS timer 20:23:46, Season II
  2d 20:33:46.
- The 1649 unit retired the blind-pan method and the 1229
  grounding (tent at norm 374,526) no longer matches this
  camera framing. Two tents were re-grounded fresh from
  the current screenshot (visual grounding): lower-middle
  tent bbox 549-688, 533-614 and lower-right tent bbox
  653-814, 580-675. No pan was needed.
- Tapping the lower-middle tent at its centre (618,573)
  selected it: "Barracks Lv.27" label with the button row
  (blue paw, orange pistol, green up arrow - the upgrade
  shortcut, never tapped).

## Lv.27 barracks - finished batch collected

- Tapping the orange pistol button (619,648; bbox
  568-670, 615-682) raised the toast "Training complete:
  313 Lv.9 units are ready" and the button row closed
  without opening TRAIN UNITS.
- Total Power moved 148,787,578 to 149,210,754 on the
  tap: +423,176, exactly 313 times 1,352 (the T9 unit
  power), so the finished batch counted into power on
  the tap, with no Drill Ground visit needed - the same
  mechanism the 1229 unit verified for the Lv.24
  barracks (666 x 1,063).
- The Lv.24 barracks batch (T8 x666, queued 12:29 for
  1d 04:19:43) is still running and is not due for
  requeue until about 16:49 on 2026-11-11. The Lv.30
  and fourth barracks were not checked in this unit.

## Requeue blocked - Drill Ground Full (live toast)

- The Lv.27 barracks is now idle. Re-tapping the tent
  and then the pistol to open TRAIN UNITS instead
  raised the toast "Drill Ground Full: Unable to add
  more units." and no panel opened.
- The Drill Ground Full blocker is therefore live in
  this unit, not inferred: the drill ground cap
  (39,460 of 39,460 per the retro) blocks the requeue
  even though the finished batch was collected without
  a Drill Ground visit. Collection and requeue are
  decoupled - collecting never needed the Drill Ground,
  requeueing does.
- The Drill Ground screen itself was not read live in
  this unit: the pass budget ended at the toast. The
  next training unit's first action is to read the
  Drill Ground screen live - locate the Drill Ground
  building on the base, open it, and record what
  controls it actually shows (what a full drill ground
  offers: deploy, dispatch, dismiss or collect) - and
  to spend itself on the nearest allowed preparatory
  action toward clearing it. How a full Drill Ground
  is cleared is still not known from a live read.

## Close

- Partial. One barracks checked, its finished batch of
  313 Lv.9 collected and verified by the exact power
  delta; its requeue blocked by Drill Ground Full; the
  other three barracks unchecked (Lv.24 known running
  from 1229). The tracker stays untouched, so the next
  tick re-produces the training regular and the work
  resumes as a fresh unit.
- No diamonds or money spent. No Finish Now button and
  no upgrade shortcut tapped. No login or verification
  demanded. No "active on a different device" dialog
  appeared.

## Result stats

- target check all 4 barracks, requeue any idle one at
  its highest tier
- achieved 1 of 4 barracks checked (Lv.27); finished
  batch of 313 Lv.9 collected; requeue blocked by Drill
  Ground Full; 3 unchecked
- resources_gained 313 Lv.9 units counted (+423,176
  Total Power)
- points 0
- costs about 9 minutes, no items spent, no food or
  iron spent (no batch queued)
- verified yes (power delta 313 x 1352 read live
  in-unit)
- blocker_category e
- barracks_checked 1, batches_collected 1,
  units_collected 313, batches_requeued 0,
  drill_ground_full yes (live toast), power_before
  148787578, power_after 149210754
