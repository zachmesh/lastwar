---
title: Events check 0706 queue run
created: 2026-11-09T15:06:15Z
modified: 2026-11-09T15:18:00Z
version: 1.0.0
description: Event claims check from the scout signals - Events icon badge 1 and Wanted Boss tab red dot
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 07:06-07:18 PT
---

# Events check - 0706 queue run

Unit events-2026-11-09-1450, executor ticker-0704. Window: claimable now -
scout 2026-11-09, base/hud Events icon badge 1; scout 2026-11-09,
events/wanted-boss Wanted Boss tab red dot.

## What was checked

- Base screen at entry: Events icon carried a red badge 1, coin 44.2M.
- Events hub opened on Arms Race (Tech Research phase, Contest Segment
  Lv.29-30, 02:51:08 left at first read). Score 0, point chests
  6,250 / 12,500 / 30,000 unreached, cumulative chest 6/8 (not full).
  Nothing claimable on this page; the phase itself belongs to the
  arms-race unit, not this one.
- Tab bar scrolled right: Wanted Boss tab carries a red dot (still
  present after visiting the tab - it is a persistent event marker,
  not a claim indicator). Survey Center and Community show no red
  dots; Community is the last tab, the bar does not scroll further.
- Wanted Boss (Code 87): boss appears at server time 00:00, Go button
  countdown 09:49:33 at first read (09:44:17 at close) - the boss is
  NOT out yet, so no attack is possible now.
- Rewards panel: Ranking Reward is a plain table (No.1 to No.4-10),
  no claim buttons. Individual Reward tiers (1 / 2 / 3 attacks) all
  greyed - 1 attack pays chests x6/x6/x6, 5-min speedup x5, red
  diamond x10; 2 attacks x8/x8/x8, x5, x20; 3 attacks x10/x10/x10,
  10-min speedup x10, x20. Nothing earned, nothing to claim.
- Goals panel: best single attack 899,542,636 against tiers 1.0B,
  1.5B, 2.0B, 2.5B, 3.0B - all unreached, all Claim buttons greyed.
  Nothing claimable.

## Result

Checked only, nothing claimed - both scout signals are explained
and neither hides a claimable reward. The Wanted Boss red dot stays
on the tab after the visit; the boss appears at server 00:00, about
9h44m after this unit, so the next events unit should re-check after
the boss is out.

## Method notes

- The Rewards panel X at (833, 156) did not close the panel on two
  taps (R2: method ended); the back arrow at (159, 952) closed it
  both times. Re-ground the panel X fresh next time instead of
  re-tapping the stale point.
- Session cc-232, LastWar window 489932, no device dialog, no
  contention, no login demand.

## Stats

- target: claimable event rewards behind the two scout signals
- achieved: 0 claimed (0 claimable found)
- resources_gained: none
- verified: yes (same-unit live reads)
- blocker_category: none
