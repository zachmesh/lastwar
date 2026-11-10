---
title: Alliance train queue run 0413
created: 2026-11-10T12:13:00Z
modified: 2026-11-10T12:13:00Z
level: L0
version: 1.0.0
description: Train unit train-2026-11-10-0230, boarded carriage 2 of Missile Apex train, 3-contract gift missed (repeat of the 0147 deviation)
status: unverified
---

# Alliance train 04:04 to 04:13 - ticker-0404

Unit train-2026-11-10-0230 (planned for the 02:30 cycle,
expires 06:30). Executor ticker-0404. Sessions cc-395 then
cc-396 on the owner Mac mini (cc-395 dropped mid-unit;
cc-396 started, LastWar re-selected, no game state lost).

## Live reads

- Base screen: no "Boarding closes in" banner under the
  resource bar. The left icon column carries a locomotive
  train icon (verified by enlarged crop).
- Two taps at normalized (55, 608) produced no change; the
  point was about 39 px off the icon centre. Re-grounded
  centre (40, 568) panned the camera to the station at once
  (R2 pivot: fresh measurement, same method retried once
  with the corrected point).
- Station view: a yellow train stands at the platform,
  conductor Missile Apex, countdown 02:31:54 to departure
  at first sight, Train Rating 68,350.
- Tapped the train body: a train cinematic opened ("Tap the
  screen twice to skip"). Double-tapped to skip; the second
  tap landed at the platform screen centre and opened the
  THANK THE CONDUCTOR dialog (Trade Contracts owned 146,
  quantity slider at 1, Like & Thank and Gift Contract
  buttons).
- The dialog had opened on an unverified carriage, so it
  was closed via X without gifting, to read the platform
  first (standing rule: verify the carriage before tapping
  its plus).
- Platform read after the close: countdown 02:30:10, Train
  Rating 68,350, conductor Lv.30 [AP3x]Missile Apex
  (verified by tapping the conductor avatar to its profile).
  Carriages top to bottom: 1 at 3/7 with "+", 2 at 9/7 with
  the own avatar in place of "+", 3 at 4/7 with "+", 4 at
  17/7 with "+". Carriage 2 reward set: badge 2.5K x1, blue
  chest x1 + x1, gold chest x20, triangle 2.5K, triangle
  2.0K.
- The own avatar (night-sky profile picture) sitting in
  carriage 2 proves the account is aboard carriage 2: the
  blind second tap of the skip double-tap had landed on
  carriage 2's "+" (the platform centre), which is the
  standing-rule carriage, and the "+" tap itself takes the
  seat. Confirmed by tapping the carriage 2 avatar, which
  opened MY PROFILE (Lv.30 [AP3x]Bears Lair) - the seat is
  held. A "You're very popular!" overlay (1,815 +4 likes)
  was dismissed with Awesome! on the way back.
- Final station read on leaving: countdown 02:26:53, so
  departure is about 06:41 local. Returned from the
  platform to the station view.

## Deviation - gift missed, second identical occurrence today

- The seat was taken by the "+" tap, but the THANK THE
  CONDUCTOR dialog was closed without gifting, so the
  standing 3 Trade Contract ticket was NOT given. The
  dialog does not reopen once closed (learned 2026-10-27),
  so the gift step cannot be redone for this ride. Trade
  Contracts remain 146; none spent. The seat is held and
  the carriage 2 reward will still arrive as an Event mail
  ("Train arrival reward") after departure.
- This is the same deviation, same cause, as unit
  train-2026-11-09-2230 (ticker-0134, 01:47, Abyss Apex
  train, record 0147-queue-run.md), which had already
  written the lesson: skip the cinematic with a single tap
  plus a fresh observation, never a blind double-tap. This
  unit repeated the blind double-tap anyway - the record-only
  lesson did not change the next executor's behaviour.
  Filed as GitHub issue #570 (label play) so the fix -
  writing the skip method into the alliance-train activity
  metadata as a hard step - is tracked instead of living
  only in a past record. Per R2, a third identical
  deviation writes the blocker into the activity metadata.
- Unexplained delta, recorded not attributed: Trade
  Contracts read 158 in the 01:47 dialog and 146 in this
  unit's dialog, a drop of 12 with no spend by either
  unit. No cause established from this unit's reads.

## Outcome

- Boarded carriage 2 of the Missile Apex train (departure
  in about 2 hours 27 minutes from the final read). 0 of 3
  Trade Contracts gifted - deviation recorded above, issue
  #570 filed. No other game input dispatched.
