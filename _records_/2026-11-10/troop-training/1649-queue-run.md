---
title: Training queue run 1649
created: 2026-11-11T00:49:00Z
modified: 2026-11-11T00:49:00Z
version: 1.0.0
description: Ticker-1634 training unit - barracks tents not located after three camera pans, no batch requeued, pan method retired
status: unverified
---

# Training - ticker-1634, 16:45 to 16:49 PST

Unit training-2026-11-10-1403, executor ticker-1634. Status
partial, unverified: no barracks tent was located in this unit,
so no barracks state was read and no batch was requeued.
Computer session cc-483, windowed 642x951 play throughout.
No device dialog, no login demand, no Touch ID, no password
typed.

## Live reads at entry

- Base screen: power 148,787,578; food 631.3M; iron 954.1M;
  coin 97.8M; diamonds 6,267; stamina 120; level 30.
- VS timer 01:13:28 at entry, 01:10:39 at close; Season II
  3d 01:23:28; third timer 5d 01:13:28 (meaning unverified).
- Left column: hammer 1/4 (red dot), flask 1/2 (red dot),
  truck icon with a question marker, radio/broadcast icon
  badge 11, hero portrait, gift chest. Right column: Events
  badge 2, VS, Season II, radar-side icon, skull badge
  moving 1 to 4 to 2 with a 00:00:24 to 00:00:52 countdown,
  Alliance (red dot), Mail (red dot), Inventory (red dot).
- Task: "Build: Oil Well [0/1]". Toasts seen during the
  unit: "Violet's Gift received!" (the gifts regular owns
  it) and "Important: President HawksMav appointed..."
  (truncated, unread).

## What was tried

- The base view at entry shows only the top-left corner of
  the base; the four barracks tents (lower middle of the
  base per the activity metadata) are not in frame, and the
  lower two thirds of the screen are fog.
- Pan 1, down: drag norm 320,700 to 320,250 (the 1615
  survivors grounding). The view overshot into full fog;
  no base, no tents.
- Pan 2, right: drag norm 500,500 to 200,500. The view
  moved only slightly; the top edge of the base stayed in
  frame and no tent appeared.
- Pan 3, right long: drag norm 550,450 to 100,450. The view
  overshot past the right edge of the base into fog with a
  mountain peak at the top; no tents.
- Restore: drag norm 200,450 to 500,450 returned the view
  to the base's top edge, where the game was left. The base
  screen is the closing state, not deep fog.
- No TRAIN UNITS panel was opened and no batch was queued.
  No Finish Now button and no upgrade shortcut were tapped.

## Known state, not re-verified in this unit

- Lv.24 barracks: a fresh T8 batch x666 was queued at 12:29
  for 1d 04:19:43, so it is still running and is not due for
  requeue until about 16:49 on 2026-11-11. The 12:29 unit
  also showed Drill Ground Full did not block that requeue.
- Lv.30, Lv.27 and the fourth barracks: states unverified;
  the Lv.30 "1d 17:14:37" seen at 12:24 is a batch duration,
  not a remaining timer.

## Method change under rule R2

- The blind-pan method is retired inside this unit after
  three no-locate pans: the drags either barely move the
  view or overshoot the base edge into fog, and they never
  land on the tents. The next training unit must re-ground
  from the 12:29 record's successful entry - read
  troop-training/1229-queue-run.md for the measured tent
  point that opened TRAIN UNITS that day - and go straight
  to that point before any pan. If the tents still cannot
  be located from that grounding, the blocker is filed as
  a GitHub issue instead of a third identical partial.

## Red lines

- No diamonds or money spent, no price tag or paid button
  tapped, no Delete All, no assembly or teleport. Nothing
  trained, nothing finished, nothing queued.

## Result stats

- target: check all 4 barracks, requeue any finished batch
  at its highest tier
- achieved: 0 barracks checked, 0 batches requeued
- resources_gained: none
- points: 0
- costs: 5min-device-session
- verified: no (no barracks state read live in this unit)
- blocker_category: e (repeated blocker - barracks tents
  not located; training units have closed partial on
  location since the 2026-10-28 to 2026-10-31 queue era)
