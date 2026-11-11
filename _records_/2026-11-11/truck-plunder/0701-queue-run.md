---
title: Truck plunder queue run
created: 2026-11-11T15:01:00Z
modified: 2026-11-11T15:01:00Z
version: 1.0.0
description: Ticker trucks unit - one UR truck dispatched, quota shortfall remains
status: unverified
---

# Truck plunder queue run - 2026-11-11 07:01 local

- Executor: ticker-0637
- Unit: trucks-2026-11-11-0257 (planned 10:57 UTC, expires 14:57 UTC)
- Session window: about 06:53-07:01 local (14:53-15:01 UTC)
- Status: partial - pass budget ended mid-quota
- Duel posture (tools/duel.py): Day 3, Age of Science. UR truck
  dispatches do NOT score today, so the non-UR day rule applied:
  dispatch SR or above only, free refresh first, then Trade
  Contracts until reached.

## What was done

- Entry: the trade slot is absent from the base left column in the
  current set (chat / white pickup / radar dish / magnifier). Tapping
  the top icon at norm (51,576) opened Intercity Trade directly on
  Others' Trucks - this is the route flip the metadata describes,
  verified live this unit. The white pickup at (51,641) is the Secret
  Command Post, not trade; the dish at (51,702) is radar.
- Counters read live on entry: Today's Trade Count 0/5, Your Plunder
  Count Today 0/4. No returned trucks to settle - Your Truck showed
  four empty slots.
- Recover button carries a red dot (a Reward Recovery record waits);
  not opened in this unit - the pass budget ended at the dispatch.
- Dispatch 1 (slot 1, Squad 1 escort): first roll N (iron 1.2M, food
  1.2M, coin 810.0K, arrives 03:45:11). Free refresh kept N (chest
  x20, arrives 03:30:00). Contract refresh (dice label read 148/1
  after the free refresh, 145/1 after this one - the label's exact
  meaning is unread, recorded as seen) rolled UR: iron 3.8M, food
  3.8M, coin 2.4M, chest x10 twice, plus items; arrives in 03:18:14.
  Dispatched with Let's Go (normal - Mega Mode is for UR duel days
  only). Trade Count moved 0/5 to 1/5 live.
- Plunder: not started - no plunder was attempted in this unit.

## Result statistics

- target: Trade Count 5/5, Plunder Count 4/4
- achieved: Trade Count 1/5, Plunder Count 0/4 (live reads)
- resources_gained: none yet (truck in transit, arrives in about
  03:18)
- points: none (truck dispatches do not score on Science day)
- costs: about 8 minutes; 1 free refresh + contract refresh(es) on
  the dice (label 148/1 to 145/1 as read)
- verified: yes - every figure above was read live on screen in this unit
- blocker_category: h (by-design partial - pass budget ended mid-quota)

## Next trucks unit must

- Read both counters live first (Trade 1/5, Plunder 0/4 at this
  unit's close), dispatch slots 2-4 to SR or above, then plunder
  0/4 to 4/4 by the shard rule (UR/SSR trucks carrying UR shards,
  guard below Squad 1, shards right-sided; refresh the list until
  a suitable target appears).
- Open the Recover panel (red dot) and claim any waiting Reward
  Recovery record.
- Entry: tap the top left-column icon at norm (51,576) to open
  Intercity Trade; do not hunt the column for a trade icon.

## Red lines

- No diamonds spent. No Mega Mode used (not a UR duel day).
  Trade Contract refresh spending is standing-authorized for the
  non-UR day SR-or-above rule. No plunder attempted, no alliance
  mate touched. No other task type was executed in this unit.
