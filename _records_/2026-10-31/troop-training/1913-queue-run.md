---
title: Troop Training Execution 2026-10-31 1913 Queue Run
created: 2026-11-01T02:13:00Z
modified: 2026-11-01T02:13:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-1803 - partial, Barracks Lv.27 checked and blocked by Drill Ground Full, no batch collected or started, other barracks not checked
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-31 1913 queue unit

A single task unit, executed by executor ticker-1904 under the
task unit queue. Unit training-2026-10-31-1803, priority 3.
Session window 19:05 to about 19:13 America/Los_Angeles.
Status — performed in part: one barracks was checked and
found blocked, no batch was collected or started, and the
other barracks were not checked, so the tracker is untouched
and the next tick re-produces this regular.

## What was done

- Sync — ticker sync reaped 0, expired 0, produced 0 new
  units: all 16 due regulars were already queued by the
  planner. No zombie chain was seeded: the Zombie
  Invasion event ended at about the 19:00 reset on
  2026-10-30 (chain unit 066 closed the chain, metadata
  forbids re-seeding until a Zombie Invasion tab is seen
  live in the Events hub again) and no zombie-invasion
  unit sits in inbox or claimed.
- Open — the game was already on the base screen, no
  different-device dialog appeared, no login or
  verification was demanded. HUD at the open — food
  342.5M, iron 530.4M, coin 177.0M, total power
  148,947,193, unchanged from the 1544 unit close.
- Window state — Google Chrome stayed frontmost
  throughout, as in earlier 2026-10-31 units, but
  background input DID reach the game: the barracks
  selection and the toast below both registered, so the
  foreground blocker is intermittent, not absolute.
  The computer session dropped once between the
  screenshot read and the pistol tap (cc-696 to cc-697
  resume, no state lost), matching the session-drop
  pattern seen in earlier units.
- Barracks Lv.27 — selected by a tap at norm 617,570
  on a tent in the lower-middle base view, the same
  point as the 1544 unit; the label read Barracks
  Lv.27 and the button row appeared (paw, pistol,
  green up arrow). The pistol button was re-grounded
  on this unit's own screenshot (visual-grounding box
  552 to 652 in x, 601 to 667 in y, centre 602,634)
  and tapped at 602,634.
- Blocked — the pistol tap answered with the toast
  "Drill Ground Full: Unable to add more units" (read
  in the post-action observation). No TRAIN UNITS panel
  opened, no batch was collected, no batch was
  started, and total power was unchanged at
  148,947,193. This is the same block the 0304, 0704
  and 1544 units recorded: finished batches cannot be
  collected until drill-ground space is freed, and
  no new batch can be added while it is full. No
  troops were deployed or dismissed to free space —
  that is an owner-side decision, outside this unit.
- Nothing bought, no diamond spent, no speedup item
  burned, no Finish Now, no green upgrade shortcut
  tapped, no assembly or teleport. No other regular
  was merged into this unit. The game was left on
  the base screen with the Lv.27 barracks selected.

## Result statistics

- barracks_checked: 1
- batches_collected: 0
- batches_started: 0
- barracks_blocked_drill_ground_full: 1

## Close

- Next training unit should not expect a collection
  to succeed while the drill ground is full; the
  owner-side space decision is the gate. Lv.27's
  pistol point in this camera view is 602,634 by
  fresh grounding (602,616 also triggered the same
  toast in the 1544 unit), but the camera drifts
  between views, so re-ground it on the unit's own
  screenshot before tapping.
