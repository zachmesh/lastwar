---
title: Troop Training Execution 2026-10-31 1544 Queue Run
created: 2026-10-31T22:44:00Z
modified: 2026-10-31T22:44:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-1403 - partial, Barracks Lv.27 checked and blocked by Drill Ground Full, no batch collected or started, other barracks not checked
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-31 1544 queue unit

A single task unit, executed by executor ticker-1534 under the
task unit queue. Unit training-2026-10-31-1403, priority 3.
Session window 15:34 to about 15:44 America/Los_Angeles.
Status — performed in part: one barracks was checked and
found blocked, no batch was collected or started, and the
other barracks were not checked, so the tracker is untouched
and the next tick re-produces this regular.

## What was done

- Sync — ticker sync reaped 0, expired 0, produced 0 new
  units: all 15 due regulars were already queued by the
  planner. No zombie chain was seeded: the Zombie
  Invasion event ended at about the 19:00 reset on
  2026-10-30 (chain unit 066 closed the chain, metadata
  forbids re-seeding until a Zombie Invasion tab is seen
  live in the Events hub again) and no zombie-invasion
  unit sits in inbox or claimed.
- Open — the game was already on the base screen, no
  different-device dialog appeared, no login or
  verification was demanded. HUD at the open — food
  337.1M, iron 523.2M, coin 177.1M, total power
  148,947,193.
- Window state — Google Chrome stayed frontmost
  throughout, as in the 1105 gifts, 1145 help, 1304
  trucks and 1335 secrets units, but background input
  DID reach the game this time: the barracks selection
  and the toast below both registered, so the
  foreground blocker is intermittent, not absolute,
  matching the 1409 treasures note. A title-bar tap
  at norm 120,16 was refused as covered by another
  window and was not retried, following the 1304
  lesson that norm x 120 on the title bar is unsafe.
- Barracks Lv.27 — selected by a tap at norm 617,570
  on a tent in the lower-middle base view; the label
  read Barracks Lv.27 and the button row appeared
  (paw, pistol, green up arrow). The pistol button
  grounds in this camera view at norm 602,616
  (visual-grounding box 552 to 653 in x, 580 to 652
  in y), distinct from the 1055 unit's failed
  623,615 tap, which opened Building Details instead.
  An earlier tap at norm 495,668 missed the button
  row below and deselected the barracks with no
  effect; the barracks was re-selected at 617,570
  before the pistol tap.
- Blocked — the pistol tap at 602,616 answered with
  the toast "Drill Ground Full: Unable to add more
  units" (read in the post-action observation; the
  toast had faded before the next screenshot, which
  shows the base screen with no TRAIN UNITS panel).
  No TRAIN UNITS panel opened, no batch was
  collected, no batch was started, and total power
  was unchanged at 148,947,193 in the close
  screenshot. This is the same block the 0304 unit
  recorded for Barracks Lv.20 and the 0704 unit
  confirmed from the Drill Ground panel itself
  (39460/39460): finished batches cannot be
  collected until drill-ground space is freed. No
  troops were deployed or dismissed to free space —
  that is an owner-side decision, outside this unit.
- Session drops — computer session cc-676 dropped
  between the barracks selection and the pistol tap,
  and cc-677 resumed with no state lost, matching
  the session-drop pattern seen in earlier units.
  No different-device dialog, no login or
  verification demanded. Nothing bought, no diamond
  spent, no speedup item burned, no Finish Now, no
  green upgrade shortcut tapped, no assembly or
  teleport. No other regular was merged into this
  unit.

## Result statistics

- barracks_checked: 1
- batches_collected: 0
- batches_started: 0
- barracks_blocked_drill_ground_full: 1

## Close

- Next training unit should not expect a collection
  to succeed while the drill ground is full; the
  owner-side space decision is the gate. Lv.27's
  pistol point in this camera view is 602,616, but
  the camera drifts between views, so re-ground it
  on the unit's own screenshot before tapping.
  Lv.24 requeue, Lv.30 verification and the Lv.20
  block remain open behind the same gate.
