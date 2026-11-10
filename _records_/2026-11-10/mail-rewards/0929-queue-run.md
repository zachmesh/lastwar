---
title: Mail rewards 2026-11-10 0929 queue run
created: 2026-11-10T17:29:00Z
modified: 2026-11-10T17:29:00Z
version: 1.0.0
description: Mail unit partial by ticker-0904, entry blocked by camera framing, Mail panel never opened
status: partial
grounded_in:
  - source: in-game base screen observed live on the owner Mac mini, 2026-11-10 about 09:25 to 09:29 PT
---

# Mail rewards 2026-11-10 0934 queue run

- Executor: ticker-0904. Computer session cc-429 on the owner Mac
  mini (cc-428 dropped between units, recovered).
- Session window: about 09:25 to 09:29 PT. Status: partial.
- Unit: mail-2026-11-10-0630.

## What happened

- Entry attempt 1: Mail envelope tap at the fresh measured centre
  (931,757) on the standard base framing delivered as a camera
  pan, not a button tap - the Mail panel never opened, and the
  view jumped to a panned framing (Drill Ground Lv.25, "15:26"
  timer) with the right rail (Mail, Alliance, Inventory, WORLD)
  off-frame. This is the background-input tap-delivers-as-drag
  failure mode the 0304 pass named the same morning.
- Recovery attempt 1: drag from (200,500) to (450,500) moved the
  camera back toward the standard framing (top HUD and HQ back
  in view) but still panned down-left, right rail still
  off-frame.
- Recovery attempt 2: reverse drag from (450,500) to (200,500)
  moved the camera back to the panned-right framing (Drill
  Ground Lv.25, "15:27"). The two drags oscillate between two
  panned framings; neither restores the right rail.
- Per queue rule R2, the entry attempts stop here: no further
  blind taps or drags inside this unit. The Mail panel was
  never opened, no category was swept, nothing was claimed,
  nothing was deleted.

## Blocker

- Camera framing (audit class c/e - tap method / repeated
  blocker): background-input taps intermittently deliver as
  map drags, and the base camera then sits in a panned state
  where the fixed right-rail shortcut column is off-frame.
  This is the fourth unit this reset day with the same
  blocker (the 0304 pass's radar, survivors and donations
  units), so it is a repeated failure mode, not a one-off.
  The next mail unit must reset the camera framing first
  (the standard framing WAS present at 09:14 this pass, so
  the framing changes between passes) or find a Mail entry
  that does not depend on the right rail. Filed as GitHub
  issue #580 (play) from this record.

## Safety and red lines

- No different-device dialog, no login or verification demanded,
  no password or Touch ID step used.
- No diamonds or money spent, no mail claimed or deleted
  (Delete All never pressed, Claim All never reached), no
  building or research started. The trucks screen was not
  re-entered in this unit.

## Result stats

- target: all mail categories swept, claimable rewards claimed
- achieved: 0 categories swept, Mail panel never opened
- resources_gained: none
- costs: about 8 minutes, no items spent
- verified: yes (the non-entry is observed live in this unit)
- blocker_category: e (repeated blocker - camera framing, fourth unit this reset day)
