---
title: Radar tasks queue run 2108
created: 2026-11-22T05:21:00Z
modified: 2026-11-22T05:21:00Z
version: 1.0.0
description: Queue unit radar-2026-11-21-1803, ticker-2104 - 3 stored tasks executed via Quick Execute on a stack day; bar then flipped to Claim All (8 pending) with stored still 2/40, the 2026-10-31 trap state
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 21:08-21:21 PT
  - source: unit radar-2026-11-21-1803 in _queue_/done
  - source: tools/duel.py --json, run live this unit
---

# Radar tasks queue run 2108 (ticker-2104)

Unit radar-2026-11-21-1803, regular radar, activity
radar-tasks, priority 2, est 6 minutes, expires
2026-11-22T06:03:00Z (22:03 PT). Executor ticker-2104.
Session window about 21:08 to 21:16 PT. Token held 21:08
to 21:16 PT (released 21:16; lease ran to 21:23); unit claimed 21:08 PT, lease to
21:28 PT. Computer session cc-43.

## Outcome

Partial - 3 stored tasks executed via Quick Execute on a
stack day (stamina 112 to 82 proves the 3 marches), then
the bottom bar flipped to Claim All with 8 task rewards
pending and no Quick Execute offer, while stored still
reads 2/40. That is the 2026-10-31 Claim All trap state:
whether the 2 stored tasks are executable cannot be
settled without claiming, which the stack posture
forbids. No claims made, no pins tapped, no diamonds or
money spent, no stamina items used. The tracker is
untouched (partial re-produces next tick).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-43.
- LastWar window 105986 in windowed mode (763x1050),
  activated and raised on entry; no different-device
  dialog, no login demanded, no Touch ID, no password
  typed. The Issue #648 fullscreen block is cleared -
  the window is windowed and pointer input works, as in
  the ticker-1804, 1834, 1934 and 2034 passes.

## What happened

- Duel posture read live before entry: tools/duel.py
  reports duel day 7 (off day, settlement), radar
  posture stack. The unit window label says "duel day
  6 - radar stack"; the live posture agrees it is a
  stack day, so no claims.
- Entry read, verified live on the radar screen: Lv.13,
  radar points 533, stored 2/40, stamina 112, restore
  line "12 Radar Task(s) will be restored in about
  03:26:00", "Fully restore at 11-22 18:38:08 local
  time". Entry icon grounded fresh: the dish with its
  red badge sat at norm 52,708 on the current base
  screenshot and opened the radar on the first tap
  (the 2026-10-29 estimate was 62,727; the live point
  is 10 left of it).
- Bottom bar at entry: "You can complete 3 tasks,
  requires 30 Stamina." with Quick Execute. One tap
  on Quick Execute at norm 498,941 dispatched the
  batch. Verified by stamina: 112 to 82, exactly 3
  tasks at 10 stamina each.
- After the batch the bar reads "8 task rewards can
  be claimed" with a green Claim All button - not
  tapped, stack posture. Before this unit the pending
  count was therefore 5 (8 minus the 3 just executed).
- Stored-count anomaly, verified twice: stored read
  2/40 at entry (enlarged crop confirms the glyph)
  and still reads 2/40 after the 3 executions, on a
  re-entry after leaving to the base and coming back
  (second radar entry, stamina 83 by then from
  regeneration). The executed tasks did not move the
  stored counter. Either the counter counts a pool
  Quick Execute does not draw from, or it updates on
  a longer delay than one re-entry. Open question for
  the profile; the next radar unit should re-read
  stored at entry before assuming it.
- Pin inventory, stack posture - inventoried, none
  tapped (a finished-task pin pays instantly on tap
  and would leak the claim onto a non-scoring day):
  top-centre blue person pin and purple skull pin
  with red dot; right blue mine/cart pin with a small
  red dot; middle-left portrait pin (man's face in a
  frame); bottom-left cluster of orange axe pin,
  green skull pin with red dot, blue axe pin; a small
  round animal icon at the bottom-left edge, likely a
  world-map creature rather than a radar pin. The
  purple and green skull pins with red dots are the
  likely finished-task pins; the portrait, axe and
  mine pins stay unidentified, as before.

## Closing reads

- Stored 2/40, radar points 533, stamina 83
  (regenerating), restore 12 tasks in 03:24:32,
  pending rewards 8 (Claim All, untapped).
- Base totals at entry (top bar): food 755.0M, iron
  1.1G, coin 103.9M, diamonds 5,246, gold 17.72K,
  power 149,653,371 - identical to ticker-2034's
  close.

## Remaining work

- The 2 stored tasks may still be executable behind
  the Claim All trap; the next radar unit inherits
  this as its opening read (stored 2/40, pending 8,
  bar Claim All only). On the next release day the
  8 pending rewards claim and score.
- Open question: why stored stayed 2/40 after 3 Quick
  Execute marches - re-read at the next entry and,
  if it repeats, fold into the radar-tasks profile.

## Result stats

- target: execute stored radar tasks, stack posture, duel day 7 off day
- achieved: 3 tasks executed via Quick Execute; bar flipped to Claim All (8 pending), stored 2/40 unchanged
- resources_gained: none claimed (stack day; 8 rewards pending for the release day)
- points: 0 (no claims; radar points 533 unchanged)
- costs: about 8 minutes device time, 30 stamina, no items
- verified: yes (stamina, stored, bar and pins all read live in this unit)
- blocker_category: e (repeated blocker - Claim All trap, 2026-10-31 pattern, with 2 stored tasks possibly behind it)
- tasks_executed: 3
- stamina_before: 112
- stamina_after: 83
- stored_before: 2
- stored_after: 2
- pending_rewards: 8
- pins_inventoried: 7
- duel_day: 7
- duel_posture: stack

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #793 already open for the
  branch, no new PR owed.
