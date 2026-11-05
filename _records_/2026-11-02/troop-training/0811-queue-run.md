---
title: Training queue run 0811
created: 2026-11-02T16:11:00Z
modified: 2026-11-02T16:11:00Z
version: 1.0.0
description: Ticker training unit, Barracks Lv.24 selected but TRAIN UNITS panel not reached
status: partial
grounded_in:
  - source: game screen on the owner Mac mini 2026-11-02 08:05 to 08:11 PST
---

# Training queue run 0811

Unit: training-2026-11-02-0603, executor ticker-0804, status
partial. Session window 08:05 to 08:11 PST on the owner Mac mini.
No batch was queued, no training state was verified, nothing was
claimed, and the tracker is left untouched, so the next tick
re-produces the regular and the work resumes as a fresh unit.

## What was done

- Base screen read live at unit start: food 388.3M, iron 578.2M,
  coin 51.6M, diamonds 2,336, total power 149,311,528.
- One different-device takeover, handled under the owner rule:
  the "active on a different device" dialog appeared at unit
  start, Confirm was tapped once, the app exited as expected,
  and it was relaunched and back at the base screen with no
  login or verification demanded. No second dialog appeared.
- Barracks located in this unit's camera view, by visual
  inspection of a cropped lower band: three tents in the
  lower-middle base area. Tapping the upper-right tent at
  norm (825,578) selected Barracks Lv.24, with the three-button
  action row under its label: blue paw circle at about norm
  (623,499), orange pistol circle at about norm (763,510),
  green up-arrow circle at about norm (903,494). The green
  arrow was not tapped, per the red lines.
- Tapping the pistol circle at norm (763,510) did not open
  TRAIN UNITS and did not open an upgrade panel: the game
  switched to the world map (radar fan, Radar Task restore
  countdown). Home at norm (903,941) returned to base.
- Changed method, per queue rule R2: re-selected Barracks
  Lv.24 at norm (825,578), then tapped the paw circle at
  norm (623,499). The result was the same world-map switch,
  not Building Details. Home returned to base again.
- Second changed method: re-selected the barracks, then
  tapped the tent body again at norm (825,578). That only
  re-showed the same action row; no panel opened.

## Why partial, not done

- The TRAIN UNITS panel was not reached, so no barracks queue
  state was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were not
  inspected. The activity doc's action-row mapping (paw to
  Details, pistol to TRAIN UNITS) did not hold on either tap
  in this unit: both taps switched to the world map instead
  of opening a panel. This differs from the 0322 unit, where
  the pistol tap opened the upgrade panel, so the mapping is
  not merely stale in one direction - it is unstable across
  camera positions, and the action row must not be tapped
  again as the entry route until a fresh, verified mapping
  is established.
- The 2026-10-31 Drill Ground Full blocker was neither
  confirmed nor cleared in this unit: no barracks panel was
  reached, so no Drill Ground figure is claimed here.

## Follow-up

- Commented on issue #150 with this unit's measured tent
  coordinate, action-row coordinates, and the world-map
  result for both the pistol and paw taps, so the next unit
  does not repeat the action-row route.
- Next unit: try a different entry route (for example a
  building-list or label entry, or a long-press variant on
  the selected tent), never the action-row taps used here,
  and record the Drill Ground screen live first if a panel
  is reached.

## Closing figures

- Batches queued: 0, read live as no panel opened.
- Barracks checked: 1 of 4 (Lv.24 selected only, panel not
  opened). Drill Ground count: not read.
- Device takeovers in this unit: 1, completed, no contest.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No upgrade shortcut tapped, no building
  started, no base move, no Assemble, no teleport.
