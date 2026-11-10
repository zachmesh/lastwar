---
title: Alliance gifts 2026-11-10 0932 queue run
created: 2026-11-10T17:32:00Z
modified: 2026-11-10T17:32:00Z
version: 1.0.0
description: Gifts unit partial by ticker-0904, entry blocked by the same camera framing as the mail unit, Gifts panel never opened
status: partial
grounded_in:
  - source: in-game base screen observed live on the owner Mac mini, 2026-11-10 about 09:31 to 09:32 PT
---

# Alliance gifts 2026-11-10 0932 queue run

- Executor: ticker-0904. Computer session cc-429 on the owner Mac
  mini.
- Session window: about 09:31 to 09:32 PT. Status: partial.
- Unit: gifts-2026-11-10-0630.

## What happened

- Entry blocked before any gifts action: the base camera is still
  in the panned framing left by the mail unit this pass (Drill
  Ground Lv.25, "15:30" timer, read live on a fresh screenshot
  in this unit). The right rail - Alliance shield, Mail,
  Inventory, WORLD - is off-frame, so the Alliance Gifts entry
  cannot be reached.
- No blind tap or drag was attempted in this unit: the mail unit
  already proved two drags only oscillate between two panned
  framings without restoring the rail, and the pass budget was
  nearly out. Per queue rule R2 the unit stops here rather
  than repeating the failed method.
- The Gifts panel was never opened, no tab was claimed, Gift
  Level progress was not read. Nothing claimed, nothing spent.

## Blocker

- Camera framing (audit class c/e - tap method / repeated
  blocker), same as the mail unit this pass: GitHub issue #580
  (play), filed from the mail record. This is the fifth unit
  this reset day with the same blocker (the 0304 pass's radar,
  survivors and donations units, plus mail and gifts this
  pass). No new issue filed - #580 already carries it.
- The next gifts unit needs the camera framing reset first
  (the standard framing WAS present at 09:14 this pass), or
  a Gifts entry that does not depend on the right rail.

## Safety and red lines

- No different-device dialog, no login or verification demanded,
  no password or Touch ID step used.
- No diamonds or money spent, no gifts claimed, no building or
  research started.

## Result stats

- target: Claim All on both tabs (Regular and Premium), both verified empty
- achieved: 0 tabs claimed, Gifts panel never opened
- resources_gained: none
- costs: about 2 minutes, no items spent
- verified: yes (the blocked entry is observed live in this unit)
- blocker_category: e (repeated blocker - camera framing, fifth unit this reset day)
