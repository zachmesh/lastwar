---
title: Truck queue run 2052
created: 2026-10-30T21:02:00-07:00
modified: 2026-11-01T07:00:34Z
version: 1.0.1
description: Owner-requested plunder unit, partial - trade screen entry failed, left column in the no-trade-slot set, plunder untouched at 0 of 4
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner direct request to plunder trucks, 2026-10-30 20:35 local
---

# Truck queue run, 2052

Session window: about 20:50-21:02 PDT, executor
owner-req-2050 (owner direct request in the main
chat, unit trucks-2026-10-31-0350, priority 1),
Mac mini session cc-578, game account
[redacted-character-name]. Duel day 6, Enemy Buster
(non-UR day). Objective: plunder only, from the
2017 unit's close - Trade Count 2 of 5, Plunder
Count not re-read that unit, presumed 0 of 4 on
the new trade day until a unit reads it on the
trade screen itself.

Performed: entry only, failed. No plunder.

- Waited out ticker-2034 (device token held to
  20:49) before taking the token; ticker-2034's
  commit b38f0f7 closed treasures, vip and the
  zombie chain.
- Entry: game sat on the Events page (Desert
  Storm tab). Title-bar tap at 200,17, then the
  back arrow at 139,900 returned to base.
- The left icon column on the base read, top to
  bottom: green season face, blue train-front
  icon, white pickup, satellite dish, hammer.
  No blue truck-front (Intercity Trade) slot was
  identifiable in this set - the same no-trade
  set shape recorded on 2026-10-26.
- Taps tried: the blue train-front icon at
  54,582 panned the camera to the train station
  on the first tap and did nothing on the
  second; the 2017 unit's proven point 53,555
  also did nothing. Between the first base
  screenshot and the later ones the column
  shifted - the white pickup moved from about
  norm y 610 to about y 650 - consistent with
  the first tap flipping the shortcut set, as
  the metadata describes for the route icon.
  Next executor: flip the set back first (tap
  the same train/route icon and re-ground the
  column) before concluding the slot is absent.
- The trade screen was never opened, so neither
  counter was re-read. Plunder stands untouched;
  on the 2017 close the day was Trade 2 of 5,
  plunder presumed 0 of 4. Dispatch was not in
  this unit's scope (owner asked for plunder),
  and the two trucks dispatched at 20:17 arrive
  in about 4 hours regardless.
- Nothing spent, nothing tapped with a price
  tag, no Assemble or Teleport.

Outcome: partial. Entry failed on the shortcut
set; plunder still owed 4 of 4 for this trade
day. Tracker untouched, so the next tick
re-produces trucks, and the staged 2257 unit
also remains. Follow-up on the unit carries the
set-flip note above.
