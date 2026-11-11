---
title: Alliance train queue run 0209
created: 2026-11-11T10:09:00Z
modified: 2026-11-11T10:09:00Z
version: 1.0.0
description: Ticker-0155 train unit - boarding closed before the carriage-2 plus tap landed, account not aboard, train departs in about 4 minutes, failed
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 02:04-02:09 PT
---

# Alliance train queue run 0209 (ticker-0155)

Unit: train-2026-11-10-2230. Status: failed.
Activity: alliance-train. Computer session cc-536.

## Entry - banner tap opened the platform while boarding was still open

- The "Boarding closes in" banner was first seen during
  the training unit of this pass (00:02:51, then 00:02:38
  at the paw tap). On the Events screen at the arms-race
  interruption it read 00:01:13.
- This unit was claimed out of queue order: `next` had
  returned research-2026-11-10-2203, but the train
  boarding was the live expiring event (about 1 minute
  left), so the train unit train-2026-11-10-2230
  (planned 22:30, expires 02:30) was claimed instead.
- Tapping the banner opened the STATION PLATFORM at
  timer 00:05:19: Train Rating 108,350, carriages 5/7,
  7/7, 6/7, 7/7, plus buttons visible on all four
  carriages. Carriage 2 (standing rule) showed 7/7.

## Boarding missed - the plus tap landed after boarding closed

- Before tapping, the unit read the activity metadata in
  full. That read cost the boarding window: by the time
  the carriage-2 plus was tapped, the plus buttons were
  gone from all four carriages, the timer read 00:04:55,
  no THANK THE CONDUCTOR dialog opened, and occupancy
  was unchanged (5/7, 7/7, 6/7, 7/7). A second tap on
  the same spot changed nothing.
- The banner countdown and the platform timer agree on
  the close: the banner read 00:01:13 at about 02:03:20
  (close about 02:04:30), and the platform plus buttons
  were present at timer 00:05:19 and gone at 00:04:55 -
  boarding closes about 5 minutes before departure.
- Lesson for the next train unit: on a closing boarding
  window, tap the carriage-2 plus FIRST and read the
  metadata after - the standing rule (carriage 2, 3 Trade
  Contracts) is already known and the platform screen
  itself shows the occupancy. A metadata read must never
  sit between the platform open and the boarding tap
  while the banner is under about 2 minutes.

## Verification - account not aboard

- Carriage 3's passenger list was opened (6/7): [AP3x]
  Dogo, [AP3x]AshenRise, [AP3x]LAMP 1, [AP3x]Janet A,
  [AP3x]sebfin13, [AP3x]Raze Cromwell. [AP3x]Bears Lair
  is not among them. The account is not aboard this
  train. The train departs in about 4 minutes (timer
  00:03:37 at close) without this account.
- No Trade Contracts were spent, no dialog was opened,
  no other carriage was tapped for boarding. No diamonds
  or money spent. No login or verification demanded. No
  "active on a different device" dialog appeared.

## Close

- Failed. Boarding closed before the boarding tap landed;
  the account misses this train. The tracker is left
  untouched for a failed unit, and the next train unit
  (train-2026-11-11-0230, not_before 02:30) covers the
  next preparation. The game was left on the STATION
  PLATFORM screen.

## Result stats

- target board carriage 2 with 3 Trade Contracts
- achieved not boarded - boarding closed before the plus
  tap landed
- resources_gained none
- points 0
- costs about 5 minutes, no items spent, no contracts
  spent
- verified yes (platform, occupancies, passenger list
  and missing plus buttons all read live in-unit)
- blocker_category a
- boarded no, carriage_target 2, carriage_2_occupancy
  7/7, train_rating 108350, timer_at_entry 00:05:19,
  timer_at_close 00:03:37, boarding_close_about
  02:04:30, contracts_spent 0, device_takeovers 0
