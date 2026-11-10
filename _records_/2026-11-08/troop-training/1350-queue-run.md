---
title: Queue Run 1350 Troop Training Partial
created: 2026-11-08T21:50:00Z
modified: 2026-11-08T21:50:00Z
level: L0
version: 1.0.0
description: Training unit training-2026-11-08-1003, Lv.30 barracks re-verified busy, no batch queued, partial
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 13:37-13:40 America/Los_Angeles
---

# 1350 queue run - troop training (training-2026-11-08-1003)

- Unit: training-2026-11-08-1003, executor ticker-1317.
  Status: partial - 1 of 4 barracks verified (Lv.30 busy),
  0 batches queued, the other three barracks not reached
  inside the unit cap. Tracker untouched.
- Session: computer session cc-126 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd); session cc-125
  had dropped between units and was restarted. No
  device-access error, no different-device dialog, no
  login demanded. Nothing bought, no speedup used, no
  Finish Now tapped.
- Session window: 13:37-13:40 local, about 3 minutes.

## What was read and done

- Base HUD at entry: food 489.5M, wood 811.9M, iron 25.0M,
  stone 922.2K, coin 12.3M, power 149,850,353, diamonds
  4,397, gold 13.22K. Stamina 88 at the lightning icon.
- Tent tap 1 at norm (564, 510), on the second white-blue
  chevron tent in the middle of the base: no change, no
  selection label, no action row. A miss, not a tent
  selection (rule R2: that point ends here).
- Tent tap 2 at norm (459, 457), on the first white-blue
  chevron tent: opened TRAIN UNITS directly, with no
  action row seen in this framing. Panel read live:
  Power 1647, Morale 750.0, Squad Load Capacity 2200,
  Unit HP 4726.34, Unit Attack 38.45, Unit Defense 7.7,
  Lv.10 selected at 36.5K, a Lv.10 batch of 793 already
  training with 20:47:28 left. This is the same Lv.30
  barracks the arms-race unit read at 21:01:06 left
  about 13:27 - busy, cannot queue more. No Train was
  tapped and no Speed Up was tapped; the panel was
  closed with its X, returning to the base.
- The other three barracks (Lv.27, Lv.24, fourth T7)
  were not reached in this unit. The Drill Ground Full
  state was not re-read live, and Quick Dispatch was
  not tapped (unverified effect, left for an owner
  decision per the activity metadata).
- Arms Race implication: no Lv.10 batch was queued in
  this unit, so the Unit Progression phase score stays
  at 0. The priority-1 successor
  arms-race-2026-11-08-2127 follows in this pass to
  re-read the score and close the phase verdict before
  the 14:03 phase end.
- Observed, not acted on: a top banner reading "5000
  Diamonds from Alliance Star Thank You Gift. The rumor
  turns out to be true!" - a system/chat banner, not a
  claim by this unit; any gift claim belongs to the
  gifts regular, not this unit.

## Tracker and follow-up

- Tracker untouched (partial). The next training unit
  resumes the barracks check from the two unchecked
  tents: re-ground fresh in its own view, and note that
  a single tap on a verified tent can open TRAIN UNITS
  directly in this framing, while a neighbouring tent
  point missed outright.
- Result stats: target 4 barracks, achieved 0 batches
  queued (1 barracks state verified live), verified yes
  for the Lv.30 busy read.
