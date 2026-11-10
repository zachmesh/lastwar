---
title: Troop training queue run 0337
created: 2026-11-10T11:37:00Z
modified: 2026-11-10T11:37:00Z
level: L0
version: 1.0.0
description: Ticker-0334 training unit, partial - no barracks selected at wide zoom or panned-down view, Drill Ground not re-read, duel posture read live
status: unverified
---

# 0337 queue run - Troop Training

Executor: ticker-0334. Unit: training-2026-11-10-0203.
Session window about 03:37 to 03:42 America/Los_Angeles.
Computer session cc-390 on the owner Mac mini (started and
ended cleanly, no drops, no different-device dialog).

## What was done

- Changed method per queue rule R2 and the 0034 handover: instead
  of re-tapping the formation yard, the camera was zoomed out
  with a scroll to a wide base view and the beige tents with
  blue zigzag markings at the base right edge were tried fresh.
  Three fresh grounding taps on those tents selected nothing:
  - Tap at norm (890,500) on the upper tent body: no
    selection, no label, no button row. The truck bubble
    beside the yard changed to "Supplies are fully loaded,
    please claim them" during this step; the truck was left
    untouched (truck-type work for its own unit).
  - Tap at norm (903,468) on the upper tent: opened the
    world/radar map instead of selecting a building ("12
    Radar Task(s) will be restored in 01:59:55", "9 task
    rewards can be claimed", Claim All). The radar Claim All
    was NOT tapped: radar work belongs to its own unit. The
    home button returned to base.
  - Tap at norm (919,530) on the lower tent body: no
    selection, no label, no button row.
- The camera was then panned down with a drag to the formation
  yard view (Formation 2 and 3 signs, parked squads), the same
  framing the 0034 unit started from. Two more fresh points on
  the tents now at the top-right edge selected nothing:
  - Tap at norm (841,116) on the upper tent body: no change.
  - Tap at norm (903,198) on the lower tent: opened the
    Alliance Duel screen (the VS button hotspot sits at the
    same top-right corner). The back arrow returned to base.
- Alliance Duel read live on that screen (duel-type context,
  no duel action taken): Today's Theme Base Expansion,
  14:18:29 remaining, alliance target 1,650,000 points;
  reward chests 8,020 / 9,530 / 18,100 with progress bars
  40,000 / 150,000 / 540,000; scoring actions include
  Dispatch UR Trade Truck 1 time +300,000.0 and Perform 1 UR
  Secret Task +225,000.0. Today is a duel UR day for trucks.
- Power read live twice: 146,751,949 at entry, then
  148,058,020 from the wide view onward (+1,306,071 during
  the unit; no cause established - no training batch was
  observed completing and no claim was made in this unit).
  The rise is recorded as a live read, not attributed.
- No diamonds, money, speedups or paid buttons were used, and
  no other task type was executed in this unit. No squad was
  dispatched, no truck claimed, no radar reward claimed. The
  game was left on the base screen with nothing selected.

## What was not done

- No barracks was requeued: no barracks state was verified
  live in this unit, and the Drill Ground screen was NOT
  re-read live either. The Drill Ground Full toast (39,460
  of 39,460, last read live 2026-10-31) stays carried
  forward unverified. Carried-forward state (not
  re-verified): Lv.30 batch requeued 2026-11-07 about 17:08
  (1d 17h) was due about 10:22 on 2026-11-09; Lv.27 idle and
  blocked at the 1330 read on 2026-11-09; Lv.24 and the
  fourth barracks not checked. Tracker untouched, per the
  partial rule; the next tick re-produces the training
  regular.
- Quick Dispatch stays untapped: its effect is still
  unverified and it may march troops out, left for an owner
  decision or a learn-first exploration unit.
- R2 fourth-partial note: this is the fourth consecutive
  training partial with the same blocker (0039, 1330, 0034,
  this unit), each with a changed method and none requeuing
  a barracks. Per queue rule R2 a fourth identical partial
  is a process failure, not a result, and is reported to the
  owner as one. The blocker is commented on issue #150 in
  this pass. The next unit needs a new grounding route, not
  another tap on these tent points: the tents at the base
  right edge do not select at wide zoom or in the panned-down
  view, and the top-right corner hotspots belong to the VS
  and radar entries.

## Figures read live on screen

- Food 610.2M, iron 933.6M, coin 82.7M, power 146,751,949
  at entry rising to 148,058,020 during the unit, diamonds
  6,207, energy 117 at entry.
- Build slot in use: Oil Well (0/1), 1/4 hammer icon, 1/2
  flask icon.
- Radar: 12 task(s) restore in 01:59:55, 9 task rewards
  claimable (not claimed in this unit).
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 4, achieved 0, resources_gained none, costs
  about 5 minutes play, verified yes, blocker_category e,
  device_takeovers 0
