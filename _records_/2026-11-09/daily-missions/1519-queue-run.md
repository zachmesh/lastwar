---
title: Queue Run 1519 Daily Missions Claim
created: 2026-11-09T23:19:00Z
modified: 2026-11-09T23:38:00Z
level: L0
version: 1.0.0
description: Unit daily-missions-2026-11-08-1800, done - four completed rows and three activity chests claimed, full daily list re-checked live, activity 140
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-09 about 15:19-15:38 America/Los_Angeles
---

# 1519 queue run - daily missions claim (daily-missions-2026-11-08-1800)

- Unit: daily-missions-2026-11-08-1800, executor ticker-1518.
  Status: done - the full daily task list was re-checked live
  top to bottom, every completed row was claimed, and the
  40, 80 and 120 activity chests were all claimed. Activity
  star reads 140 at close; the 160 and 200 chests are
  unreached. Next Refresh read 02:38:33 at entry falling to
  02:24:03 at close, pointing at the 18:00 local reset.
- Session: computer sessions cc-300 then cc-303 on the owner
  Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd). Session
  cc-300 closed mid-unit (observe returned
  observation_unavailable); cc-303 was started, LastWar
  re-selected, no game state lost. No device-access error,
  no different-device dialog, no login demanded. One control
  call failed first on a missing observation_id
  (stale_observation); retried with the screenshot
  observation_id, no input lost. LastWar was already running
  on the Events screen (Desert Storm Battlefield,
  registration ends in 2d 02:40:17, battle day 2026-11-13);
  returned to base with the back arrow before opening
  Mission. The first click at normalized 100,875 missed
  the arrow; the grounded point 156,920 worked - coordinate
  inputs are normalized 0-1000, not window pixels.
- Evidence: this file; the Mission panel reads below are all
  live in this unit.

## What was read and claimed, live in this unit

- Entry, read live about 15:21 local: base screen, power
  149,217,331; food 553.9M, iron 879.2M, coin 51.8M;
  diamonds 6,077. Mission opened from the orange terminal
  on the base screen, grounded fresh at norm 44,836 in
  this unit's base view. The panel opened directly on the
  Daily Tasks tab.
- At entry the Daily Tasks tab badge read 9 and four rows
  stood green with Claim buttons: Daily Login (1/1),
  Defeat any Doom Elite 1 time(s) (1/1), Complete 1 Radar
  Task(s) (1/1), Donate to Alliance Tech 5 times (5/5).
  The activity star read 0 and the progress bar was grey
  through all five chests.
- One tap on Daily Login's Claim (norm 782,423) claimed
  all four green rows at once - the list reordered
  immediately to unclaimed rows, the badge fell 9 to 3,
  the star jumped to 140 and the bar went gold through
  120. This is the fourth observation of the
  one-tap-multi-claim mechanism (see Issue #171, #208):
  a single Claim tap claims every completed row in view,
  not just its own row. It is now verified by this unit's
  before/after reads, not merely observed.
- Full list, re-checked top to bottom in seven slow-drag
  scrolled views. Completed and claimed (green check at
  the bottom of the list): Daily Login (1/1), Defeat any
  Doom Elite (1/1), Complete 1 Radar Task(s) (1/1),
  Donate to Alliance Tech 5 times (5/5), Help Allies 5
  Times (5/5). Help Allies was not in the entry view; it
  stands claimed with a green check, either claimed by
  the same multi-claim tap or by an earlier pass this
  reset day - not distinguished in this unit.
- Incomplete, all with blue Go buttons, none tapped:
  Recruit Heroes 1 Time(s) (0/1); Kill 5 zombie(s) on
  World Map (0/5); Attack a Commander 1 time(s) (0/1);
  Gather Food x10,000 at resource tile (0/10000); Gather
  Iron x10,000 at resource tile (0/10000, seen only as
  the cut-off row between views); Gather Coin x10,000 at
  resource tile (0/10000); Train 100 units of any level
  (0/100); Upgrade a Building 1 time(s) (0/1); Research a
  tech 1 time(s) (0/1); Obtain 1 Gear at SSR and/or
  better rarity (0/1); Recruit Survivors 1 time(s) in the
  Tavern (0/1); Make any paid purchase once (0/1) - never
  to be tapped, red line; Dispatch Trade Trucks 3 time(s)
  (not seen in this unit's views - likely skipped between
  scroll steps, belongs to the trucks regular); Plunder
  others' Secret Task reward 1 time(s) (0/1); Perform Data
  Training on Drone 1 time(s) (0/1).
- Activity chests: a before/after crop of the chest row
  proves the change - at entry all five chests were
  closed with the star at 0; at close the 40, 80 and 120
  chests stand open (lids up) and the 160 and 200 chests
  closed. The 40 tap produced a CONGRATULATIONS banner:
  gear part x10, red gem x40, wrench x1, blue crate x20,
  food crate x20, gold coins x12, crystal 2.8K, 5m
  speedup x8, with the line "You've scored double rewards
  2 times this round!" The 80 tap showed its contents
  list: 5m Construction Speed-up x2, Iron Chest (SR) x4,
  Food Chest (SR) x4, Construction Part x1, Drone Parts
  x2, Crystal Ore 1.0K. The 120 chest already stood open
  before its tap, so it was claimed by the same cascade;
  tapping it showed its contents list: 5m Construction
  Speed-up x2, Iron Chest (SR) x6, Food Chest (SR) x6,
  Diamond x20, Drone Parts x2, Crystal Ore 1.2K. The
  chest cascade matches the row cascade - one tap claims
  every claimable chest, not just its own. Tapping an
  already-open chest shows its contents list and spends
  nothing.
- Scroll method, rule R2 pivot: the scroll action and a
  fast drag both produced no list movement (two no-change
  attempts, method ended); the slow drag - mouse down,
  three stepped moves with 0.5s waits, mouse up - moved
  the list every time and is now the working scroll method
  for this panel. Downward drags to return to the top did
  not move the list; the chest row is fixed at the top of
  the panel, so chests were tapped from the bottom view.

## Open questions

- Activity star composition: five claimed rows at 10 points
  each account for 50 of the 140 the star reads; the other
  90 are unexplained by this unit's reads. The star read 0
  at entry even though the four green rows were already
  complete, so the header may render stale until a claim
  refreshes it - or the star counts Main Tasks activity as
  well. The Main Tasks tab was not opened in this unit.
  A later unit should read the Main Tasks tab and the
  star in the same pass to pin this down.
- The one-tap-multi-claim mechanism is now verified for
  rows (fourth observation, with before/after reads) and
  for chests (this unit's 40/80/120 cascade). Issue #171
  and #208 carry the earlier observations; the retro may
  close them on this evidence.

## Follow-up

- The next tick re-checks the list in the same reset day;
  the remaining rows belong to their owning regulars
  (trucks, help, training, donations, radar) or later
  ticks, not to this unit.
- The 160 chest needs 20 more activity points and the 200
  chest 60 more; the only in-list paths before the 18:00
  reset are Recruit Survivors (20), Plunder (30) and
  Drone Training (10) plus the gather/train rows, all
  incomplete and owned elsewhere.

## Red lines

- No diamonds spent, no money spent, no Go button tapped,
  no PvP task attempted, no paid-purchase row touched, no
  research or building started. Game left on the base
  screen, power 149,317,331 at close.
