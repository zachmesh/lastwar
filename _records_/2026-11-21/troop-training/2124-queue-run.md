---
title: Troop training queue run 2124
created: 2026-11-22T05:30:00Z
modified: 2026-11-22T05:30:00Z
version: 1.0.0
description: Queue unit training-2026-11-21-1803, ticker-2104 - Lv.27 barracks selected live, Drill Ground yard identified by building, formation-flag tap selects a squad instead of opening a Drill Ground screen; no requeue, Issue #678 blocker stands
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 21:24-21:30 PT
  - source: unit training-2026-11-21-1803 in _queue_/done
  - source: GitHub Issue #678 (Drill Ground Full), as recorded in _activities_/troop-training/INDEX.md
---

# Troop training queue run 2124 (ticker-2104)

Unit training-2026-11-21-1803, regular training,
activity troop-training, priority 3, est 4 minutes,
expires 2026-11-22T06:03:00Z (22:03 PT). Executor
ticker-2104. Session window about 21:24 to 21:28 PT.
Token held 21:24 to 21:28 PT (released 21:28; lease
ran to 21:38); unit claimed 21:24 PT, lease to
21:43 PT. Computer session cc-43 (shared with the
radar and survivors units of the same pass).

## Outcome

Partial - no barracks requeued. The Lv.27 barracks
was selected live and its button row confirmed, but
its pistol tap was NOT repeated (ruled-out route
under Issue #678: it reproduces the "Drill Ground
Full: Unable to add more units." toast). One fresh
entry route was tried for the Drill Ground search -
the formation flag in the bottom yard - and it
selects a deployed squad instead of opening any
Drill Ground screen. The other three barracks were
not checked inside the unit cap. No diamonds or
money spent, no stamina spent, no items used. The
tracker is untouched (partial re-produces next
tick).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-43.
- LastWar window 105986 in windowed mode (763x1050),
  frontmost on entry; no different-device dialog, no
  login demanded, no Touch ID, no password typed.

## What happened

- Fresh base screenshot grounded five tent-like
  structures; the first tapped at norm 603,578
  selected Barracks Lv.27 (label read live) with its
  button row: paw (Building Details) at norm
  493,608, pistol (TRAIN UNITS) at norm 595,635,
  green up arrow (upgrade - not tapped) at norm
  700,605. This is the barracks idle since
  2026-11-10 21:46 per Issue #678.
- The pistol was deliberately not tapped: the
  activity metadata rules it out as a repeat route
  (toast only, no state change), and re-proving it
  is what the 2026-11-11 blocker update tells the
  queue to stop paying for.
- Fresh Drill Ground identification, from the same
  fresh screenshots: the bottom strip of the base is
  the squad formation ground - parked vehicles in
  marked slots, a "FORMATION 2" label, and the
  massed red troops standing at the bottom-right.
  A tap on the formation flag at norm 216,833
  selected the "2nd Squad Lv.20" vehicle (label read
  live) and showed a tank button plus the green
  upgrade arrow - it selects a deployed squad, it
  does not open a Drill Ground management screen.
  The Drill Ground screen and its controls (deploy,
  dispatch, dismiss, collect) are still unread, and
  no clearing method for the 39,460 of 39,460 full
  reading is known from a live read.
- The other three barracks (Lv.30, Lv.24, fourth)
  were not opened in this unit; their batch states
  are unread. Food ticked 755.0M to 755.4M across
  the pass (production), iron 1.1G, coin 103.9M,
  diamonds 5,246, power 149,653,371 throughout.

## Blocker accounting (R2)

- This is the fifth consecutive training partial on
  the Drill Ground Full cause (2146 on 2026-11-10;
  0213, 0548, 2136 on 2026-11-11; this unit). The
  activity metadata already carries it as a
  fourth-consecutive partial under Issue #678
  (knowledge class); this unit's new datum - the
  formation-flag tap selects a squad - is owed as a
  comment on #678 and is named here because the pass
  budget ran out before it could be posted.
- Per R2 a fourth identical partial is a process
  failure to be reported to the owner, not a result.
  The failure is structural (no known Drill Ground
  entry), not an executor error: the queue should
  not keep spending units re-proving it. What is
  needed is a web-researched Drill Ground location
  or an owner steer, tracked on #678.

## Remaining work

- Locate the Drill Ground screen (web research or a
  fresh route - not the tent pistol, Details, yard
  tap or formation flag, all ruled out or tried)
  and clear the 39,460 of 39,460 full state so the
  Lv.27 barracks can requeue.
- Check the other three barracks' batch states.

## Result stats

- target: requeue any idle barracks; locate the Drill Ground screen
- achieved: Lv.27 barracks selected live, button row confirmed, no requeue; formation-flag route tried and ruled out as a Drill Ground entry; other three barracks unchecked
- resources_gained: none
- points: 0
- costs: about 4 minutes device time, no stamina or items
- verified: yes (barracks label, button row, squad label all read live in this unit)
- blocker_category: e (repeated blocker - Drill Ground Full, Issue #678, fifth consecutive partial)
- barracks_checked: 1
- barracks_idle: 1
- drill_ground_located: no

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #793 already open for the
  branch, no new PR owed.
