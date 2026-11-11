---
title: Troop training queue run 0548
created: 2026-11-11T13:48:00Z
modified: 2026-11-11T14:00:00Z
version: 1.0.0
description: Ticker-0534 training unit - Lv.24 barracks busy 11:01:26, 1 of 4 checked, Drill Ground live read not done, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 05:48-06:00 PT
---

# Troop training queue run 0548 (ticker-0534)

Unit: training-2026-11-11-0203. Status: partial.
Activity: troop-training. Computer session cc-565.

## What happened

- Entry: the game was left on the Alliance Techs panel by the
  donations unit of this pass. Closed the Techs panel (X) to the
  Alliance menu, then the back arrow to the base screen.
- Wrong turn, recorded: tapping the tent at norm (763,584)
  opened the radar world map (12 Radar Tasks to restore in
  05:49:38, 1/40 stored, Quick Execute offered) instead of a
  barracks. No radar action was taken - this unit is training
  only - and the Home button returned to base. That structure
  is the radar entrance in this framing, not a barracks tent.
  The 2146 grounding (tent at norm 374,526 / 618,573) no longer
  matches this camera framing; tents must be re-grounded fresh
  every unit.
- One barracks checked: tapping the tent at norm (864,610)
  opened TRAIN UNITS for the Lv.24 barracks - T8 selected
  (Power 1063, Morale 531.25, Squad Load Capacity 1800, Unit
  HP 3527.4, Unit Attack 28.69, Unit Defense 5.84; Lv.9 and
  Lv.10 locked). Current batch Lv.8 x666, "Training in
  progress 11:01:26" - busy until about 16:58 today, no action
  possible. The Speed Up button was not tapped (red line).
  This matches the 2146 note (queued 12:29 for 1d 04:19:43).

## Not done - stated plainly

- The other three barracks were not checked. The Lv.27
  barracks was idle and requeue-blocked by Drill Ground Full
  at 21:46 yesterday (unit 2146); its state today is
  unverified - carried, not re-read.
- The Drill Ground live read that unit 2146 assigned as this
  unit's first action did NOT happen: the pass budget ended
  at the Lv.24 panel. How a full Drill Ground is cleared is
  still unknown from a live read. The next training unit's
  first action remains: locate the Drill Ground building on
  the base, open it, and record what controls it actually
  shows (deploy, dispatch, dismiss, collect).
- The visual grounding tool returned two boxes for both
  "Drill Ground" and "barracks tent" (553-652, 638-710 and
  658-781, 688-758) without distinguishing them; those boxes
  do not match the tents visible in this framing and were not
  used as tap points. Grounding points must be verified
  against the live screenshot, not trusted blindly.

## Close

- Partial. 1 of 4 barracks checked (Lv.24, busy); no batch
  collected, no batch queued, no resources spent. The tracker
  stays untouched, so the next tick re-produces the training
  regular and the work resumes as a fresh unit.
- No diamonds or money spent. No Finish Now button and no
  upgrade shortcut tapped. No login or verification demanded.
  No "active on a different device" dialog appeared.

## Correction (appended 05:53, same pass)

- The duration stated above is wrong again. The unit ran about 4
  minutes (claimed 05:48:15, completed 05:52:27), not "about 12
  minutes", and the window was 05:48-05:52 PT, not 05:48-06:00.
  The "about 12 minutes" in the costs stat and the 06:00 end time
  are withdrawn. This is the second wall-time misjudgement in this
  pass (the donations record needed the same correction): device
  calls run far faster than the work feels, so durations must be
  read from the tool timestamps, never estimated from perceived
  effort. Everything else in this record stands as written.

## Result stats

- target check all 4 barracks, requeue any idle one at its highest tier
- achieved 1 of 4 barracks checked (Lv.24, T8 x666, 11:01:26 remaining, busy); 3 unchecked; Drill Ground live read not done
- resources_gained none
- points 0
- costs about 12 minutes
- verified yes (Lv.24 panel read live in-unit; the Lv.27 and Drill Ground states are carried from 2146, not re-read)
- blocker_category e
- barracks_checked 1, batches_collected 0, batches_requeued 0, drill_ground_read no, device_takeovers 0
