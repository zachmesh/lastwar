---
title: Troop training queue run 2136
created: 2026-11-12T05:57:00Z
modified: 2026-11-12T05:57:00Z
version: 1.0.0
description: Ticker-2133 training unit - Lv.27 idle, requeue blocked by Drill Ground Full toast; Building Details route tried, Drill Ground still not located live; Issue 678 filed
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 21:36-21:52 PT
---

# Troop training queue run 2136 (ticker-2133)

Unit: training-2026-11-11-1803. Status: partial.
Activity: troop-training. Computer session cc-671.

## Entry - base screen

- Base screen at entry: food 697.1M, iron 1.0G, coins 142.3M,
  diamonds 6,717, gold 13.22K, Total Power 149,118,973 (OCR
  at window activate and at close agree; the first screenshot
  appeared to read 149,218,973 - treated as a misread, no
  power-changing action occurred in this unit). VS timer
  20:22:40, Season II 3d 20:22:39.

## Lv.27 barracks - idle, requeue blocked by Drill Ground Full (live toast)

- Tapping the tent at norm (334,584) selected it: "Barracks
  Lv.27" label with the button row (blue paw, orange pistol,
  green up arrow - the upgrade shortcut, never tapped).
- Tapping the orange pistol at norm (343,631) raised the
  toast "Drill Ground Full: Unable to add more units." and
  no panel opened. The requeue block is live in this unit,
  the same toast unit 2146 recorded on 2026-11-10: the
  Lv.27 barracks has been idle since its 313 Lv.9 batch
  was collected that evening, and it still cannot requeue.

## Changed method - Building Details route (rule R2)

- Re-selected the Lv.27 tent and tapped the blue paw at
  norm (234,605). Building Details opened: BARRACKS Lv.27,
  Training Count +726, Survivors Karen, Javier, Jessica,
  Elizabeth (all Instructor), Quick Dispatch button.
- The Details panel carries NO Drill Ground link and NO
  troop-capacity figure. The barracks Details route does
  not reach the Drill Ground. The Drill Ground building
  itself is still not located live on the base screen,
  and its screen (deploy, dispatch, dismiss, collect)
  has still never been read.

## Wrong hypothesis - the massed-troops yard tap opens mail

- A tap at norm (841,799), on the massed red-troops area,
  opened Alliance mail instead of any Drill Ground
  screen. That spot is not the Drill Ground.
- Read "(President Mail) 2110 Honoring Our Veterans"
  (2026-11-11 16:34:14, 94 likes) and the mail list:
  three unread President Mail items (Y Espanol and two
  Veteran's Day), Maintenance Completed, Patch Notes.
  The Alliance and Event rows show gift icons - rewards
  unclaimed, noted here for the mail unit, nothing
  claimed in this unit. Delete All was NOT tapped;
  Claim All was NOT tapped. Mail closed back to the
  base screen.

## Not done - stated plainly

- The other three barracks were not checked. The Lv.24
  barracks was busy until about 16:58 today per unit
  0548 (carried, not re-read); the Lv.30 and fourth
  barracks are unchecked.
- The Drill Ground live read that units 2146, 0213 and
  0548 already assigned did NOT happen in this unit
  either. This is the fourth consecutive training
  partial on the same blocker. Per queue rule R2 the
  blocker is now written into the activity metadata
  (tier-2 edit, left uncommitted for the PR flow) and
  Issue #678 filed (knowledge): Drill Ground location
  and clearing mechanism still unknown; training
  requeue blocked four consecutive units.

## Close

- Partial. 1 of 4 barracks checked (Lv.27, idle);
  no batch collected, no batch queued, no resources
  spent. The tracker stays untouched, so the next tick
  re-produces the training regular and the work resumes
  as a fresh unit.
- The unit ran past the 15 minute cap (about 16 to 17
  minutes): the mail detour cost about 4 minutes.
  The mail screens are not this unit's work and must
  not be re-entered by the next training unit; the
  Drill Ground search needs a fresh entry route, not
  another yard tap.
- No diamonds or money spent. No Finish Now button and
  no upgrade shortcut tapped. No login or verification
  demanded. No "active on a different device" dialog
  appeared.

## Result stats

- target check all 4 barracks, requeue any idle one at its highest tier
- achieved 1 of 4 barracks checked (Lv.27, idle, requeue blocked by Drill Ground Full); 3 unchecked; Drill Ground live read not done
- resources_gained none
- points 0
- costs about 16 minutes, no items spent, no food or iron spent (no batch queued)
- verified yes (Lv.27 idle state and Drill Ground Full toast read live in-unit; the Lv.24 state is carried from 0548, not re-read)
- blocker_category e
- barracks_checked 1, batches_collected 0, batches_requeued 0, drill_ground_read no, drill_ground_full yes (live toast), device_takeovers 0, issue 678

## Correction (appended 21:47, same pass)

- The duration stated above is wrong. The unit ran 603 seconds
  (claimed 05:36:20Z, completed 05:46:23Z), i.e. about 10
  minutes, window 21:36-21:46 PT - NOT "about 16 minutes" and
  NOT "21:36-21:52". It did NOT breach the 15 minute cap.
  The "about 16 minutes" in the costs stat, the "past the
  15 minute cap" claim, the 21:52 end time and the "mail
  detour cost about 4 minutes" framing are all withdrawn.
  This repeats the exact wall-time misjudgement the 0548
  record already flagged in this same activity: durations
  must be read from the tool timestamps, never estimated
  from perceived effort. The frontmatter `created`
  05:57:00Z is likewise wrong (the file was written about
  05:45Z); it stands as written, corrected by this note.
  Everything else in this record stands as written.
