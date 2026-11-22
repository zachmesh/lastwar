---
title: Troop Training 0958 Queue Run
created: 2026-11-22T18:00:00Z
modified: 2026-11-22T18:00:00Z
version: 1.0.0
description: Troop-training queue unit 0958 run - Lv.30 barracks requeued T10 x793, verified by exact food delta
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-22 09:58-10:13 PT
---

# Troop training 0958 queue run

- Unit: training-2026-11-22-0603, executor ticker-0957, session cc-128.
- Session window: about 09:58 to 10:05 PT. Status: partial.
- Result: 1 of 4 barracks checked and requeued - Barracks Lv.30, T10 x793,
  5.5M food plus 5.5M iron, 1d 17:14:37. Lv.27, Lv.24 and the fourth
  barracks unchecked; the Drill Ground screen still not read live.
- Tracker untouched, so the next tick re-produces this regular.

## Entry

- The game opened on the ALLIANCE TECHS detail panel (Rallied Attack 7/10,
  Donation Count 6/30) - leftover state from a donations unit, not this
  unit's work. No donation was made.
- The inner panel X at norm (826,237) produced no change on the first tap.
  A second tap at norm (826,158) closed the inner panel and revealed the
  Alliance Techs tree (Troop Movement 5/10, Tech Donation Today 6900).
  A third tap at the same point closed the tree to the Alliance main
  screen ([AP3x] The Apex, Members 100/100). The back arrow at norm
  (156,946) returned to the base screen. Red dots on Help, Alliance Gifts,
  Alliance Store and Alliance Techs were left untouched - other units'
  work.
- Base HUD at open: food 766.1M, iron 1.1G, coin 109.2M, diamonds 6,436,
  total power 149,417,850. Task line: "Build: Oil Well (0/1)".

## Grounding and the Lv.30 requeue

- Fresh visual grounding on the base screenshot returned four beige-tent
  boxes; the second box centre, norm (712,632), was tapped and selected
  Barracks Lv.30, raising the action row (blue paw, orange pistol,
  green up arrow). No green upgrade arrow was tapped.
- The pistol tap opened TRAIN UNITS for Lv.30: T10 preselected, count
  slider at the 793 cap, cost 5.5M food plus 5.5M iron, duration
  1d 17:14:37. Live stats: Power 1647, Morale 750.0, Squad Load Capacity
  2200, Unit HP 4726.34, Unit Attack 38.87, Unit Defense 7.87.
  Attack and defense moved since the profile's 38.45 / 7.79 - a
  knowledge-organizer fold item, not edited here (tier-2 change stays
  out of this record commit).
- No "Training in progress" line was visible on the panel; the Train
  button showed only the prospective 1d 17:14:37 duration, so the
  barracks read as idle, not state-verified-busy.
- Train tapped at norm (654,794). The panel closed and food read
  760.6M at close - exactly 5.5M down from 766.1M, the T10 batch cost.
  Iron still reads 1.1G (rounded, the 5.5M drop is invisible at that
  precision). No Drill Ground Full toast appeared at any point.
- The Lv.30 requeue is VERIFIED by the exact food delta, live in this
  unit. The Drill Ground Full block did NOT stop this requeue - the
  second live case after the 1229 Lv.24 requeue, against the 2146
  Lv.27 toast case. Collection and requeue stay decoupled as recorded
  in 2146; whether the Drill Ground refilled or the block is
  per-barracks is still unverified, since its screen was not read live.

## Open questions (not claims)

- A red-circle X timer bubble reading 00:09:16 appeared at the right
  edge of the base screen immediately after the Train tap (image about
  (590,630)); it was not present in the pre-train screenshot and was
  not read further before the unit cap. Its meaning is unknown.
- A second LastWar window (window_id 127250, 642x919) exists beside the
  selected window 127196 (642x951); input stayed on 127196 throughout
  and the second window was not touched.
- The Drill Ground screen remains unread live since 2026-11-07 (Lv.25
  read) and 2026-11-09 (Lv.30 read); Quick Dispatch stays untapped
  (owner decision). The next training unit's first action remains the
  live Drill Ground read, and the remaining three barracks still need
  their state checked - the Lv.24 T8 x666 batch queued 2026-11-10
  12:29 and the Lv.27 idle state are both long stale by now.

## Red lines

- No Finish Now, no green upgrade shortcut, no diamond or money spend,
  no speedup item burned, no purchase, no assemble or teleport.
- Nothing else was claimed, donated, dispatched or collected in this
  unit; the Alliance Techs screens were exited without action.
