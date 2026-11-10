---
title: trucks 2026-11-10 ticker-1343 queue run
created: 2026-11-10T22:11:00Z
modified: 2026-11-10T22:11:00Z
level: L0
version: 1.0.0
description: Trucks unit trucks-2026-11-10-1057 executed by ticker-1343, partial - all 4 returned UR trucks settled, 5th dispatch and plunders resume next unit
status: unverified
grounded_in:
  - source: game screens observed live on the owner Mac mini, 2026-11-10 about 13:59 to 14:11 PT
---

# trucks 2026-11-10 ticker-1343 queue run

- Unit: trucks-2026-11-10-1057 (regular trucks, activity truck-plunder)
- Executor: ticker-1343
- Session window: about 13:59 to 14:11 PT, 2026-11-10 (device session cc-465)
- Status: partial

## Duel posture

- Duel day 2, theme Base Expansion, from tools/duel.py
  --json: day ends 18:00 local, 4.0 hours left at the
  read. UR truck dispatches score 100,000 each
  (Handbook rate). Window: duel day 2 - UR trucks,
  Mega UR only. Radar posture stack (not this unit).

## Counters, read live on the trade screen

- Entry: Today's Trade Count 4/5, read live.
- Close: Today's Trade Count 4/5, read live - no new
  dispatch this unit, so the count is unchanged.
- Plunder Count was NOT re-read in this unit: the
  Others' Trucks tab was never opened. Last live read
  2/4 at 05:13. The next trucks unit must re-read it
  live before plundering.

## Settlement - all four returned UR trucks paid out

- Entry: base-screen left column, the blue speech-bubble
  icon carrying a truck glyph with red badge 2, grounded
  at norm (55,573) - the same slot that held badge 4 at
  the 02:36 entry. The enlarged crop confirmed the glyph
  is a truck, not mail. Trade screen opened on Your
  Truck: four gold UR trucks on the road, two
  flame-marked (plundered en route).
- Truck 1 settled by opening its Truck Details (tap on
  the truck body at norm (366,452); a first tap at
  (366,410) hit the chest icon and did nothing):
  CONGRATULATIONS overlay, Squad 4 escort, iron 2.8M,
  food 2.8M, coin 1.8M - looted en route from
  3.8/3.8/2.4.
- Truck 2 settled by paging right once (norm (981,515)):
  intact UR, iron 3.8M, food 3.8M, coin 2.4M, puzzle
  x1, red gem 100 x1, puzzle x1, gold chest x10,
  badge 500 x3, x3, x3.
- A second right-arrow tap at the same point produced no
  change (R2 pivot): instead of a third identical tap,
  the unit backed out to the road view - and the yard
  showed four empty slots with green + signs. No
  returned truck remained to tap.
- History Dispatch tab confirms the four 02:42:47 UR
  trucks and their final cargo: two intact at
  3.8/3.8/2.4, two looted at 2.8/2.8/1.8 with crossed
  items.
- HUD reconciliation proves all four cargoes landed:
  base HUD before the unit read food 615.9M, iron
  938.8M, coin 84.1M; after the unit food 629.2M,
  iron 952.1M, coin 92.6M - deltas +13.3M, +13.3M,
  +8.5M, matching the four-truck total of 13.2M /
  13.2M / 8.4M within HUD rounding. Had only two
  trucks settled, the delta would have been about
  +6.6M / +6.6M / +4.2M.

## Open observation - how trucks 3 and 4 cleared

- Only trucks 1 and 2 were settled by an explicit
  Truck Details view in this unit, yet the yard was
  empty afterwards and the HUD proves all four
  cargoes landed. The mechanism is unverified: either
  opening one details view settles every returned
  truck at once, or the second right-arrow tap did
  page and settle truck 3 while its screenshot looked
  identical to truck 2 (both intact UR trucks share
  the same cargo template), and the road view then
  cleared the last one - or the yard clears on view.
  Next trucks unit: watch whether a single details
  view clears the whole yard, and record the yard
  state after each settlement instead of assuming
  one truck per view.

## Not done - resumes next trucks unit

- 5th dispatch (Mega Mode, UR only) not done: the yard
  is empty with four free slots, so the dispatch is
  available now. Trade Count 4/5.
- Plunder not done: Plunder Count not re-read this
  unit, last live 2/4 at 05:13. Two plunders remain
  against the quota.
- Reward Recovery not opened this unit: the 2026-11-6
  18:00 record verification from the 05:13 follow-up
  is still open. The Recover button showed no red dot
  in the road screenshots, but that was not verified
  by opening the panel.

## Live reads

- Base screen after the check: Total Power 148,765,970,
  coin 92.6M, food 629.2M, iron 952.1M, diamonds 6,207,
  stamina 120. The trade icon badge now reads 1 (was 2
  at entry).

## Red lines

- No diamonds or money spent. No Trade Contracts spent.
  No login or verification was demanded, and no
  different-device dialog appeared.

## Outcome

Partial. Settlement complete for the whole returned
wave (HUD-verified), but the 5th UR dispatch and the
remaining plunders are undone inside this unit's
15 minutes. Trade Count 4/5, Plunder Count last live
2/4 at 05:13, both resume in the next trucks unit.

## Result stats

- target: dispatch 5, plunder 4
- achieved: dispatch 4, plunder 2 (plunder 2 is the
  last live read at 05:13, not re-read in this unit)
- resources_gained: iron 13.3M, food 13.3M, coin 8.5M
  (HUD delta across the four settlements)
- points: 0 (no new dispatch this unit)
- costs: no contracts, no stamina, no diamonds, about
  12 minutes
- verified: yes (counters, cargo and HUD delta read
  live in-unit)
- blocker_category: h (by-design partial - the 15
  minute unit cap closed the quota mid-way)
- trucks_settled: 4 (2 by explicit details view,
  4 cargoes HUD-verified landed)
- trade_count: 4
- plunder_count: 2 (last live read 05:13, not re-read)
- follow_up: re-read Plunder Count live and plunder
  to 4/4; dispatch the 5th UR truck by Mega Mode;
  verify the 2026-11-6 recovery record; watch whether
  one details view settles the whole yard
