---
title: Trucks queue run 0541
created: 2026-11-09T13:51:00Z
modified: 2026-11-09T13:51:00Z
version: 1.0.0
description: Trucks unit partial - trade screen could not be entered, no badge on the trade icon, counters not re-read, shortfall carried forward
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 05:41-05:50 PT
---

# Trucks queue run 0541 (ticker-0534)

Unit: trucks-2026-11-09-0257. Status: partial.
Activity: truck-plunder. Duel day 1, Radar Training (radar
release day) - non-UR day rules apply: dispatch SR or above
only, plunder UR or SSR trucks carrying UR shards with guard
below Squad 1 at 24.96M. Trade day ends 18:00 PT.

## Duel posture applied

- tools/duel.py --json at entry: duel day 1, theme Radar
  Training, day ends 2026-11-09T18:00:00-08:00, radar
  posture release. Truck dispatches do not score today, so
  the non-UR day rule governed. No Mega Mode dispatch was
  used or attempted.

## Entry - blocked, two methods failed

- Base screen (image read about 05:42 PT): food 540.1M, iron
  864.9M, coin 42.9M, gold 13.22K, diamonds 6,077, power
  149,217,331 (image read; the compact OCR variant
  149,117,331 is the same single-digit garble as in the
  arms-race unit of this pass and is not relied on). VS
  timer 12:18:35.
- Left column, re-grounded fresh on the live screenshot, top
  to bottom: hammer 1/4, flasks 1/2, light-blue train/bus
  front icon, white pickup, walkie-talkie with red badge 1,
  hammer, chest. The train-front icon carries NO red badge
  in this set.
- Method 1: title-bar tap at norm (180,15), then a tap on the
  freshly grounded train-front centre norm (55,594). The tap
  only panned the base map to the station area (golden train,
  Abŷss Apex, 00:27:31) - the trade screen did not open.
  This matches the 0242 no-badge pattern: a badgeless
  vehicle-front icon does not open trade.
- Method 2 (changed variant): a tap at norm (913,940) on the
  bottom-right WORLD corner, the 0242 WORLD-corner route.
  It opened the world map (alliance territory, [AP3x]Bears
  Lair base centre, March Queues 1/4), not Intercity Trade -
  the 0242 route did not reproduce in this framing.
- Returned to base with the BASE button. Per queue rule R2,
  both methods end inside this unit; the next trucks unit
  must arrive with a changed method (a foreground click
  variant on the icon, or the station-area route) rather
  than repeating either point.
- Reading the blocker: the icon carries no badge, and the
  1211/1846 precedent says the badgeless icon does not open
  trade - so this looks like a column-set availability
  issue (the trade slot is not surfaced in the current set),
  not a tap-accuracy issue. The set may rotate later in
  the day; the next unit re-grounds the column fresh before
  deciding.

## Counters - not re-read live

- Today's Trade Count and Your Plunder Count Today were NOT
  read live in this unit: the trade screen never opened.
  The standing shortfall is carried from the 0250 unit's
  close (02:50 PT, read live then): Trade Count 4/5,
  Plunder Count 1/4. No counter is overwritten here, and no
  tally is derived - the next trucks unit re-reads both
  counters live on the trade screen first.
- Dispatch shortfall 1: all four slots were occupied at the
  0250 close (dispatched about 02:40-02:50, arrivals about
  06:30-07:00), so the 5th dispatch awaits a return or a
  Mega Mode dispatch, still an open question - not attempted
  in this unit.
- Plunder shortfall 3: no plunder fought in this unit.
- Reward Recovery was not checked: the Recover button sits
  on the trade screen, which never opened.
- R3 quota checkpoint: the trade day ends 18:00 PT; the
  6-hour checkpoint falls at 12:00 PT and the 2-hour
  checkpoint at 16:00 PT, so no checkpoint is due in this
  unit and no priority escalation is raised now.

## Red lines

- No diamonds or money spent. No Trade Contract spent. No
  truck dispatched, no plunder fought, no alliance mate
  touched. No login or verification was demanded, no
  different-device dialog appeared, and no password or
  Touch ID step was used.
- Session cc-226: one open_app returned outcome_unknown and
  was not replayed; the window was verified open by
  observation instead.

## Stats

- target: dispatch 5, plunder 4
- achieved: dispatch 0, plunder 0 (nothing completed in this unit;
  the carried shortfall dispatch 4/5, plunder 1/4 is the 0250
  unit's live close, not a re-read here, so no trade_count or
  plunder_count is stated)
- points: 0
- resources_gained: none
- costs: none, about 9 minutes of unit time
- verified: no
- blocker_category: e
