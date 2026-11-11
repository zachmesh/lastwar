---
title: trucks 2026-11-09 ticker-2230 queue run
created: 2026-11-10T06:51:00Z
modified: 2026-11-10T06:51:00Z
level: L0
version: 1.0.0
description: Trucks unit trucks-2026-11-09-1857 executed by ticker-2230
status: unverified
grounded_in:
  - source: game screens observed live on the owner Mac mini, 2026-11-09 about 22:31 to 22:50 PT
---

# trucks 2026-11-09 ticker-2230 queue run

- Unit: trucks-2026-11-09-1857 (regular trucks, activity truck-plunder)
- Executor: ticker-2230
- Session window: about 22:31 to 22:50 PT, 2026-11-09 (device session cc-354)
- Status: partial

## Performed

- Entry: the trade icon (blue circle, white truck glyph, red badge 4)
  grounded fresh at norm (55,575) in the base left column; Intercity
  Trade opened on the Your Truck tab. HUD at base entry: food 582.7M,
  iron 906.5M, coin 70.1M, diamonds 13.22K, stamina 118, power
  146,751,949.
- Duel posture (tools/duel.py --json): duel day 2, Base Expansion, day
  ends 2026-11-10 18:00 PT; UR truck dispatches score 100,000 each;
  radar posture stack. Today is a UR dispatch day: UR only through
  Mega Mode.
- Trade Count 0/5 (new trade day after the about-18:00 reset; the
  2232 knowledge-organization record corroborates the about-18:00
  trade reset, superseding the "19:00 reset" wording). Plunder Count
  was not read; the Others' Trucks tab was not reached.
- Reward Recovery: the 2026-11-9 18:00 record claimed (1 unstarted
  transport, the old day's 5th dispatch shortfall): badge 500 x3,
  chest x2, gold chest x10, iron 1.5M, food 1.5M, coin 972.5K, plus
  5m speed-up tiles; CONGRATULATIONS verified. The 2026-11-8 record
  was not expanded (two taps on its header and toggle produced no
  change); its claim state is unverified.
- Settled 4 returned trucks by opening their Truck Details (each open
  pays the reward; all four read "The vehicle is safe and secure",
  none plundered):
  1. First truck, UR-scale cargo, rarity label unread behind the
     CONGRATULATIONS banner: iron 3.8M, food 3.8M, coin 2.4M, badge
     500 x1, red gems, 5m speed-ups x20 across tiles, chest x20.
  2. SR: iron 2.5M, food 2.5M, coin 1.6M, chest x20 x3, red gem 50 x2.
  3. UR: iron 3.8M, food 3.8M, coin 2.4M, badge 500 x3, blue chest x1,
     purple chest x25, gold chest x10, red gem 100 x1.
  4. SR: iron 2.5M, food 2.5M, coin 1.6M, chest x20, badge 500 x1,
     red gem 50 x2, green chest x1.
  Settlement totals: iron 12.6M, food 12.6M, coin 8.0M.
- Paging note: the details panel pages with the side "<" / ">" arrows
  and the bottom-left blue arrow (previous); the control receipt's
  no_change_observed flag is unreliable for this panel - the SR to UR
  page reported no change yet the screenshot proved the page.
  Tapping outside the panel does not close it; the unit ended with
  the panel open on the 4th truck, which is harmless - the next unit
  re-reads the trade screen fresh.

## Not done

- Dispatch: 0 of 5 new UR trucks dispatched (Mega Mode, duel day 2).
  The yard is clear after the 4 settlements; no slot was used.
- Plunder: 0 of 4; Plunder Count unread, Others' Trucks tab not opened.
- 2026-11-8 Reward Recovery record claim state unverified.

## Red lines

- No diamonds or money spent. No Trade Contracts spent. No paid button
  tapped. No login or verification demanded, and no different-device
  dialog appeared.

## Outcome

Partial. The 15 minute unit cap was reached with dispatch and plunder
unstarted (wall time ran to about 19 minutes against the claim, the
overrun being screenshot and observation latency); the next trucks
unit resumes from the cleared yard (Trade Count 0/5, Plunder Count to
be read live). The old trade day closed 4/5 dispatched with the 1
unstarted transport recovered above.

## Result stats

- target settle 4, dispatch 5, plunder 4, achieved settled 4,
  dispatched 0, plundered 0, resources_gained iron 14.1M, food
  14.1M, coin 8.97M (settlements 12.6/12.6/8.0 plus recovery
  1.5/1.5/0.9725), badge 500 x8, chest x20 x5 plus x25 plus x2,
  gold chest x10, red gems, 5m speed-ups x20, costs 19m wall, no
  stamina, no diamonds, no contracts, verified yes, blocker_category
  h, trucks_settled 4, recovery_claimed 1, trade_count 0,
  plunder_count unread, device_takeovers 0, follow_up next trucks
  unit dispatches 5 UR via Mega Mode and plunders 4; re-check
  2026-11-8 recovery record
