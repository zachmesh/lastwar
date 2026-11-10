---
title: Alliance donations queue run 0634
created: 2026-11-10T14:57:00Z
modified: 2026-11-10T14:57:00Z
version: 1.0.0
description: Ticker-0634 donations unit - failed, game canvas ignored all taps, Donation Count never read, no donation made
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 06:39-06:57 PT
---

# Alliance donations queue run 0634 (ticker-0634)

Unit: donations-2026-11-10-1343. Status: failed.
Activity: alliance-donations.

## Entry state

- The game was open on the MAIL screen at entry (left there by
  an earlier pass; mail-2026-11-10-0630 sits unexecuted in the
  inbox). Two LastWar windows existed, both on the same pid
  1908: window 489932 (642x951 at 73,31, titled "Last War",
  the frontmost/main window) and window 508052 (642x919 at
  73,63, untitled). The 0534 unit had left the game at the
  Alliance Techs panel; something since had opened Mail.
- Mac mini online, last_seen 14:31:58Z fresh. Computer
  session cc-407. No different-device dialog, no login
  demand, no Touch ID prompt at any point.

## What was tried - input failure, not a game-state failure

Nine dispatched taps across two windows, two display modes
and five methods produced exactly one game change:

1. Mail back arrow, window 489932, single click at norm
   (62,907) - no change.
2. Same point, snap_to_control false plus 1.5 s wait - no
   change. The channel advised background clicks do not
   reach some controls.
3. Mail back arrow, window 508052, single click at norm
   (62,938) - no change.
4. System mail row, window 508052, single click at norm
   (320,484) - no change. The pointer visibly moved to
   each tap point in the returned images, but the game
   never responded.
5. Mail back arrow, window 489932, mouse down, 1 s hold,
   mouse up - the receipt reported change_observed, but
   the image showed the MAIL screen unchanged; the only
   change was the title-bar buttons dropping out of the
   OCR read. No game change.
6. View menu Enter Full Screen (sanctioned route, green
   zoom button equivalent; never Ctrl-Cmd-F or Esc) -
   engaged, 1920x1080 downsampled to 1280x720 in
   observations. MAIL still showing.
7. Mail back arrow in fullscreen, single click at norm
   (383,928) - no change. The pointer in the next image
   sat about 70 normalized units right of the requested
   point (image 580,655 vs expected 490,668), the first
   sighting of the fullscreen tap offset.
8. Same point compensated 70 left, (313,928) - the MAIL
   screen exited to the base screen. The only tap in
   this unit that changed the game.
9. Alliance shield on the base screen in fullscreen,
   single click compensated (602,701), label-area tap
   (602,736), double-click (602,701), and a single click
   on window 508052 (602,701) - all no change. The
   pointer in each following image sat on the shield
   centre, so the taps landed where aimed (the +70x
   offset confirmed on all three), and the game ignored
   them.

## New measurements

- Fullscreen tap offset: in native fullscreen 1920x1080,
  a requested tap lands about 70 normalized units right
  and about 14 up of the requested point (three
  independent cursor reads agree). Aim 70 left to hit a
  target. In the windowed 642x951 mode no such offset
  was seen (the System-row tap landed exactly).
- The two-window state survives fullscreen: both windows
  became 1920x1080 at (0,0). The app menu belongs to the
  main window 489932 only; a menu call while 508052 was
  selected failed with "The app menu belongs to a
  different window."
- open_app LastWar returned outcome_unknown, the same
  signature the probe tool associates with the
  off-screen-window state, but the pixel stream here is
  live (notification banners animate, the pointer moves),
  so this is NOT the issue #284 capture failure: it is
  input not reaching the game canvas while capture
  works. Filed as GitHub Issue #575 (tooling class)
  from this record.
- The window was returned to its found state before
  close: View menu Exit Full Screen, both windows back
  to 642x919 / 642x951 at 73,63 / 73,31, base screen
  showing. No diamonds or money spent, no priced button
  tapped, no mail opened or deleted.

## Closing reads

- Alliance Techs entered: no. Donation Count: never read
  in this unit (no live read exists for the final 1/30).
  Donations made: 0. Coins spent: 0.
- Base-screen reads at 06:52 PT (display only, not
  closing figures): coin 612.5M, iron 935.9M, food
  84.1M, Total Power 148,058,020, diamonds 13.22K.
- The final 1/30 donation is still owed. The re-read
  unit donations-2026-11-10-0603 already sits in the
  inbox; no second re-read unit was enqueued, because
  the blocker is the input route, not the count. The
  next unit that finds taps working again should read
  the Rallied Attack Donation Count live first, per
  this unit's window, and donate the final 1/30 there.

## Outcome

Failed. Execution was impossible: the game canvas ignored
every tap except one mail back-button tap, so the unit
never reached Alliance Techs and never read the Donation
Count. The tracker is left untouched. The owner recovery
step for this state is the issue #284 step: click the
LastWar Dock icon once on the Mac mini (or run
_tools_/mac_lastwar_front.sh in Terminal), then re-probe;
no background route fixed it inside this unit, including
the fullscreen escalation. This is the first pass to fail
this way; the previous pass (ticker-0534) completed 7
donations with working taps about 45 minutes earlier.

## Red lines

- No diamonds or money spent. No priced button tapped.
  No mail row opened. No other activity's rewards
  touched. The diamond Donate button was never reached,
  let alone tapped. Fullscreen was entered and exited
  only through the View menu, never Ctrl-Cmd-F or Esc.
  The app was never quit or relaunched.

## Result stats

- target 1, achieved 0, resources_gained none, costs
  about 19 minutes, verified no, blocker_category c,
  donations_made 0, donation_count_before unknown,
  donation_count_after unknown, coin_spent 0,
  device_takeovers 0, entry_attempts 9
