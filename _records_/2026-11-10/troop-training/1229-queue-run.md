---
title: Training queue run 1229
created: 2026-11-10T20:29:00Z
modified: 2026-11-10T20:33:00Z
version: 1.0.0
description: Ticker pass ticker-1204 training unit - Lv.24 barracks requeued with T8 batch, verified running
status: unverified
---

# Training - ticker-1204, 12:29 to 12:33 PST

Unit training-2026-11-10-1003, executor ticker-1204. Status
partial: one barracks requeued and verified running; the
other three were not all checked.

## Lv.24 barracks - finished batch collected, new batch queued

- Tapping the tent (gold face bubble, norm 374,526) raised
  the toast "Training complete: 666 Lv.8 units are ready".
  Total power moved 148,058,020 to 148,765,978, +707,958,
  which is exactly 666 times 1,063 (the T8 unit power), so
  the finished batch counted into power on the tap, with no
  Drill Ground visit needed. The Drill Ground Full blocker
  (39,460 of 39,460) did not block this requeue.
- Its TRAIN UNITS panel: Lv.8 preselected as highest
  unlocked (Lv.9 and Lv.10 padlocked), count slider at the
  666 cap, cost 2.9M food and 2.9M iron, duration
  1d 04:20:26. Stats read live: Power 1063, Morale 531.25,
  Squad Load Capacity 1800, Unit HP 3527.4, Unit Attack
  28.69, Unit Defense 5.84. Owned counts: Lv.7 715, Lv.8
  1,998, Lv.9 1,152, Lv.10 35.8K.
- Train tapped (blue button, never Finish Now): food
  618.9M to 615.9M and iron 941.8M to 938.8M, the 2.9M each
  charged. Reopened panel reads "Training in progress
  1d 04:19:43", counting down, so the batch is running.

## Not checked this unit

- The Lv.30 barracks (white-bubble tent) panel read during
  the survivors unit showed T10 selected with 1d 17:14:37
  on the buttons. That figure is the prospective batch
  duration, not a remaining timer, so whether that barracks
  is busy or idle is still unverified; the next training
  unit must read its "Training in progress" line, not the
  button time.
- Two further barracks unchecked. The four-barracks sweep
  did not finish inside this unit's window.

## Result stats

- target: keep all four barracks busy, requeue any idle one
  at highest tier and cap count
- achieved: 1 of 4 barracks requeued (Lv.24, T8 x666,
  verified running); 1 known panel read but state
  unverified; 2 unchecked
- resources_gained: 666 Lv.8 units counted (+707,958 power)
- points: 0
- costs: about 4 minutes, 2.9M food and 2.9M iron for the
  new batch, no items spent
- verified: yes (power delta, cost delta and running timer
  all read live in-unit)
- blocker_category: h (by-design partial - unit window
  ended mid-sweep)
