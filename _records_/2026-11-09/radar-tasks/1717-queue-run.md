---
title: Radar tasks queue run 1717
created: 2026-11-10T01:17:00Z
modified: 2026-11-10T01:17:00Z
version: 1.0.0
description: Ticker-1704 radar unit, duel day 1 release - ordinary cycle already clear, 12:44 pin set absent, restore lands 12 tasks at about 17:40
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 17:07-17:17 PT
---

# Radar tasks queue run 1717 (ticker-1704)

Unit: radar-2026-11-09-1403. Status: partial.
Activity: radar-tasks. Posture: release (duel day 1, Radar
Training; duel.py confirms release, +30,000 per task as
displayed in game; day ends 18:00 PT, about 51 minutes left
at entry).

## Entry

- Radar entered first tap on the dish icon at norm 62,727
  (the same grounded point as the 12:44 unit). Entry
  verified: Lv.13, radar points 336, stored 0/40, stamina 93,
  restore line "12 Radar Task(s) will be restored in
  00:27:33" at first read, "Fully restore at 11-10 17:39:11
  local time".
- Ordinary cycle already clear from the 12:53 unit close:
  stored 0/40, no pending rewards, bottom bar gone. Nothing
  to execute or claim in the ordinary pool.

## What was done

- Pin sweep, per rule R7 (the 12:53 unit left at least 6 pins
  unworked, so this unit starts with the pins). Three map
  sectors swept by drag (west, east, north): no skull pin
  with a red dot stands anywhere in the swept sectors. The
  6-pin set inventoried at 12:44 (3 grey skull, 1 green skull,
  1 purple skull, 1 orange skull, 1 blue teardrop, 1 portrait
  pin) is absent about 4.5 hours later - presumably expired
  or despawned in the gap; the mechanism is unverified, and
  no expiry was observed live. No pin was tapped or claimed
  because no tappable pin stands.
- Brown animal-face circle: the only pin-like mark in the
  swept sectors, at the southwest edge at entry. Three
  grounded taps (norm 62,738, then 97,736, then the measured
  centre 132,762) produced no card and no screen change.
  It carries no red dot. Treated as a non-tappable map
  element, not a radar task pin - identified with reason,
  left alone. Per rule R2 the tap method ended after the
  second no-change tap; the third tap was the fresh-centre
  variant and also no-opped.
- "Violet's Gift received!" toast appeared after the first
  map tap, and an alliance toast ("Important: President
  HawksMav appointed Rage inferno as...") crossed the top
  at the same time. No reward was measured from the gift
  toast - radar points stayed 336, stamina moved only by
  regen (93 to 94) - so nothing is claimed as gained.
- The gold NEW! icon at the top of the radar screen (about
  norm 295,60) is still untouched and its function still
  unknown (also noted 2026-11-08 and 12:53).

## The restore gap (rule R6)

- The restore lands 12 tasks at about 17:40 PT, 20 minutes
  before the 18:00 duel-day roll. No radar unit is scheduled
  in that window: this unit's lease ends 17:27, the 17:30
  zero-sweep unit runs the ledger, and the next radar unit
  (radar-2026-11-09-1803) is not_before 18:03, after the
  roll, when the posture flips to stack.
- Per rule R6 a priority 1 radar successor is enqueued for
  the pre-roll claim window: not_before 17:40 PT, expires
  18:00 PT, window "duel day 1 - radar release, restored
  batch claim before 18:00 roll". If the 17:34 tick's pass
  finishes the sweep in time it can claim the restored
  batch (12 tasks, about 360,000 duel points at the
  displayed 30,000 each); if not, the batch stacks into
  duel day 3.

## Closing reads

- Stored 0 of 40, pending rewards 0, bottom bar gone, radar
  points 336, stamina 94, restore line at close 12 tasks in
  00:23:37, "Fully restore at 11-10 17:39:11 local time",
  tasks executed 0, tasks claimed 0, pins inventoried 1
  (brown circle, non-tappable), pins worked 0, pins absent
  6 (the 12:44 set), free stamina claims taken 0.

## Outcome

Partial. The ordinary-task release cycle is fully done
(stored 0/40, pending 0) but the release completion
standard also requires every map pin closed, and the pin
set that standard refers to is no longer standing - it
vanished in the gap between units, with the mechanism
unverified. The tracker is left untouched so radar stays
due; the 17:40 priority 1 successor carries the restored
batch.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  other activity's rewards touched. The Mission-screen radio
  icon was not opened. No pin was tapped blindly after the
  R2 method end.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0
  stamina plus about 10 minutes, verified yes,
  blocker_category f (the 12:44 pin set was no longer
  standing at entry - missing precondition), stored_tasks
  0, tasks_executed 0, tasks_claimed 0, pins_inventoried 1,
  pins_worked 0, pins_absent 6, stamina 94, radar_points
  336, restore_in_minutes 24, free_stamina_claims 0,
  device_takeovers 0
