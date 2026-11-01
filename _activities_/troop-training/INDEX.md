---
title: Troop Training
created: 2026-10-25T20:12:00Z
modified: 2026-11-01T05:24:00Z
level: L1
version: 1.1.0
description: Training new troops in the barracks, tier by tier, one activity folder for training knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming a train task, 2026-10-25
  - source: web guides on barracks and troop tiers, read 2026-10-25
---

# Troop training

## What this activity is

Training new troops in the four base Barracks. Each barracks trains one
batch at a time, up to its Training Count, at the highest tier its own
level unlocks. This folder accumulates training knowledge - entry,
costs, timers and tier rules. Executions are recorded in
`_records_/<date>/troop-training/`, one file per execution.

Naming note - the owner named this the train task on 2026-10-25. In
game there is also a separate alliance train at the station, registered
on its own as [`alliance-train`](../alliance-train/INDEX.md). Training
troops and riding the train are different systems and are kept apart.

## How to enter

- On the base screen, tap a Barracks tent. The four tents stand in the
  lower middle of the base in this layout.
- A row of round buttons appears under the selected tent. The pistol
  icon button opens the TRAIN UNITS panel. The paw icon opens Building
  Details, and the green up arrow is the upgrade shortcut - do not tap
  it.
- In TRAIN UNITS, the tier cards run left to right with the highest
  unlocked tier preselected, the count slider sits at the Training
  Count cap, and the blue Train button starts the batch. The yellow
  Finish Now button is never used, under the recording rules on
  spending.

## How it is done

- Keep every barracks busy. One batch per barracks at its highest
  unlocked tier, count left at the cap, then press Train.
- Queueing a batch costs food and iron only, paid up front. No diamond
  use, no instant finish.
- Training finishing also feeds VS Unit Progression and Arms Race
  points, per the web guides - unverified on this account.

## Cadence

- Continuous. A batch runs from about 23 hours to about 1 day 17 hours
  at this account, so in practice requeue each barracks as its batch
  finishes - check once per daily round and requeue any idle barracks.

## Scope and availability

- Always available, not season specific.
- Four barracks, one batch each. Barracks level gates the tier -
  observed Lv.24 trains up to T8, Lv.27 up to T9, Lv.30 up to T10.
  Guide tables agree (T8 at Lv.24 to 26, T9 at Lv.27 to 29, T10 at
  Lv.30 with Special Forces research), unverified beyond the observed
  three.
- Promotion of lower tier troops exists from Barracks Lv.10 per the
  guides. The promote arrow in the panel did nothing on the observed
  barracks, so its exact conditions are unconfirmed.

## What is known from 2026-10-25

Observed in game on this account, first execution 2026-10-25.

- Lv.30 barracks - T10, count 793, cost 5.5M food and 5.5M iron, time
  1 day 17 hours 14 minutes. T10 panel stats - power 1647, morale
  720.01, load 2200, HP 4726.34, attack 38.03, defense 7.55.
- Lv.27 barracks - T9, count 726, cost 4.1M food and 4.1M iron, time
  1 day 10 hours 19 minutes. T9 stats - power 1352, morale 600.01,
  load 2000, HP 4121.49, attack 33.13, defense 6.6.
- Lv.24 barracks - T8, count 666, cost 2.9M food and 2.9M iron, time
  1 day 4 hours 20 minutes. T8 stats - power 1063 in game (one web
  table says 800 - the in-game figure governs), morale 510.01, load
  1800, HP 3527.4, attack 28.37, defense 5.65.
- Fourth barracks - highest tier T7, count 613, cost 2.0M food and
  2.0M iron, time 23 hours 11 minutes. T7 stats - power 779, morale
  444.01, load 1600, HP 2942.73, attack 23.75, defense 4.7. Its own
  level was not read this round.
- Instructor survivors are assigned per barracks in Building Details.
  Quick Dispatch was not used.
- Guide strategies noted but not adopted - staggered barracks levels
  (the waterfall) and training T1 then promoting up to save resources.
  This account already runs staggered barracks levels by accident of
  its upgrade history.

## Limits

- Never tap Finish Now or the green upgrade shortcut while training.
- Training spends food and iron from stock. The 2026-10-25 round spent
  14.5M of each across four batches, small against roughly 290M stocks.

## Standing blocker recorded by the retro of 2026-10-31

- Queue era 2026-10-28 to 2026-10-31 - 21 of 22 training units
  closed non-done, 19 partial and 2 failed, 1 done. The dominant
  late-window blocker is Drill Ground Full, reading 39,460 of
  39,460, which blocked both collection and requeue in every
  2026-10-31 unit that reached a barracks.
- How a full Drill Ground is cleared is not yet known from a
  live read, and no clearing method is claimed here. The next
  unit reads the Drill Ground screen live first, records what
  controls it actually shows, and spends itself on the nearest
  allowed preparatory action instead of closing as a bare
  blocked read. This is a third-strike blocker under queue
  rule R2.

## Open questions

- The fourth barracks level, and whether raising it to Lv.27 or Lv.30
  is worth a build slot.
- How promotion actually engages, and its cost against training fresh.
- Whether the Lv.30 barracks button row differs - its pistol position
  opened Details twice before the panel opened from another button.
