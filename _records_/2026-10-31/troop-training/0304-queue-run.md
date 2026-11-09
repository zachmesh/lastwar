---
title: Troop Training Execution 2026-10-31 0304 Queue Run
created: 2026-10-31T10:14:00Z
modified: 2026-10-31T10:14:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-0203 - partial, Lv.30 batch collected and requeued, Lv.24 batch collected, Lv.20 blocked by Drill Ground Full, Lv.27 not located
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-31 0304 queue unit

A single task unit, executed by executor ticker-0304 under the
task unit queue. Unit training-2026-10-31-0203, priority 3.
Session window 03:04 to about 03:14 America/Los_Angeles.
Status — performed in part: two finished batches were
collected and one was requeued, but not every barracks was
verified, so the tracker is untouched and the next tick
re-produces this regular.

## What was done

- Barracks tent row pinned down in this camera position,
  breaking the blind-search run that ended the 2026-10-30
  training units: the Lv.30 tent grounds at norm 708,602
  (its gun button at 710,638), and neighbouring tents on
  the right edge of the same view are further barracks.
- Barracks Lv.30 — finished batch collected, then
  requeued. First gun-button tap showed the toast
  "Training complete, 793 Lv.10 units" and total power
  rose 146,857,078 to 148,163,149, a rise of exactly
  793 x 1647, so the collected batch is verified. The
  TRAIN UNITS panel then read Lv.10 preselected, count
  793 at cap, cost 5.5M food and 5.5M iron, time
  1 day 17:14:37; Train was tapped, food fell 328.1M
  to 322.6M, and a re-opened panel read "Training in
  progress 1d 17:14:20". No Finish Now, no green
  upgrade shortcut.
- Barracks Lv.24 — finished batch collected, requeue
  NOT completed in this unit. Gun-button tap showed
  "Training complete, 666 Lv.8 units" and total power
  rose to 148,939,659. The rise from the Lv.30 close
  (776,510) does not equal 666 x 1063 (707,958), so
  the Lv.24 yield is NOT stated as a verified per-unit
  figure — the power readings are recorded as observed
  and the 68,552 gap is an open item. The tent
  selection was then lost in the camera position and
  the requeue tap sequence did not reopen its panel
  before the unit closed; its food and iron stocks
  were unchanged, so no new Lv.24 batch was paid for.
- Barracks Lv.20 — blocked by game state. Gun-button
  tap answered the toast "Drill Ground Full: Unable
  to add more units" and total power was unchanged
  at 148,939,659, so its finished troops could not be
  collected. No troops were deployed or dismissed to
  free drill-ground space — that is an owner-side
  decision, outside this unit. Its batch stays
  uncollected until space is freed.
- Barracks Lv.27 — not located or checked in this
  unit. It remains open for the next training unit,
  together with the Lv.24 requeue.
- No different-device dialog, no login or verification
  demanded. Nothing bought, no diamond spent, no
  speedup item burned, no assembly or teleport. No
  other regular was merged into this unit.

## Result statistics

- barracks_checked: 3
- batches_collected: 2
- batches_started: 1
- barracks_blocked_drill_ground_full: 1

## Close

- Next training unit should start from the pinned
  positions in this record: Lv.30 at 708,602 (already
  training, verify only), Lv.24 requeue first, then
  locate Lv.27, and re-check Lv.20 only after drill
  ground space is freed.
