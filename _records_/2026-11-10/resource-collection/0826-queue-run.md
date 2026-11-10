---
title: Resource collection queue run 0826
created: 2026-11-10T16:26:00Z
modified: 2026-11-10T16:26:00Z
version: 1.0.0
description: Ticker-0804 harvest unit, one tap collected iron plus 3.4M HUD-verified, bubble type misidentified, sweep incomplete at the token expiry
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-10 08:17 to 08:26 local
---

# Resource collection - ticker-0804 queue run

- Executor: ticker-0804
- Unit: harvest-2026-11-10-0603, claimed 08:17:28 local
- Session window: about 08:17 to 08:26 local
- Status: partial, verified yes for the iron gain, no for the sweep
- Tracker: untouched

## Entry

- The game was left on the Rallied Attack donation panel by the
  donations unit of this pass. The panel X, the Alliance Techs X
  and the Alliance menu back arrow returned the view to the base
  with no donation button touched. On the way out the Alliance
  Techs tree showed the War tab: World Interception, Rapid Siege,
  Quick Garrison, Troop Movement 5/10, Rallied HP / Attack /
  Defense 7/10, Tech Donation Today 6,600 (display only).
- Base HUD at unit start, live: food 612.5M, iron 935.9M, coin
  84.1M, second-row 13.22K, power 148,058,020, diamonds 6,207.

## The tap - iron, not food

- Visual grounding on the live base screenshot found 11 green
  circular bubbles with wheat icon and value label over the
  farmland cluster (about 949K each) and 4 blue triangular
  bubbles over the top-center furnace row.
- One tap on the grounded centre of the topmost green bubble at
  norm (167, 324). HUD after the tap, live: food 612.5M
  unchanged, iron 939.3M (plus 3.4M), coin 84.1M unchanged.
- The tap therefore collected iron, not food: the bubble at
  (167, 324) was an iron bubble misread as food, or the tap
  cleared iron bubbles of that type. This is the R2
  bubble-type identification failure again - the downscaled
  screenshot plus grounding labels cannot be trusted for the
  type, and the HUD delta is the only type evidence. The
  4 blue triangles are unchanged (4 before, 4 after), so they
  did not clear.
- Re-grounding after the tap counted 9 green bubbles, but two
  new points appeared further right that the first pass did
  not return, so the 11-to-9 count is detection variance, not
  a verified clear of two food bubbles - and food did not move,
  which rules out a two-bubble food clear of about 1.9M. No
  bubble-clear count is claimed beyond the iron gain.
- Iron one-tap test (Issue #502): inconclusive again. The tap
  paid iron plus 3.4M, but without a pre-tap iron bubble
  inventory the mode (one-by-one vs per-type clear) cannot be
  judged - the standing iron bubbles were never read. The
  next harvest unit must read the iron bubbles first, as the
  2326 unit already instructed.

## Sweep state, why partial

- The unit stopped at the token expiry (08:26:57): one tap only.
  No second type was tapped, the left and top edges were not
  dragged, the Armed Truck loot bubble was not checked, and
  the farmland bubbles were not re-tapped. All fall to the
  next harvest unit. The tracker is untouched, so the regular
  stays due.
- Not tapped, left alone: the white speech bubble over the
  central buildings (not a resource bubble), the "?" marker,
  the Help and Gifts red dots on the Alliance menu (other
  units' work), the blue truck icon, and the radar shortcut
  gold circle. No panel was opened by any tap in this unit.
