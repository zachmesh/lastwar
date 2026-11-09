---
title: Alliance donations queue run 0547
created: 2026-11-02T13:47:00Z
modified: 2026-11-02T13:47:00Z
version: 1.0.0
description: Ticker unit donations-2026-11-02-0748, re-read of Rallied HP panel, node found upgrading with no donation count offered
status: partial
---

# Alliance donations queue run 0547

- Unit: donations-2026-11-02-0748, executor ticker-0534,
  session cc-157 on the Mac mini (cc-155 dropped mid-pass
  and was replaced; no game state lost).
- Window instruction: re-read after the ticker-2334
  cooldown - open the Rallied HP panel and read the
  Donation Count live, do not close on arithmetic.
- Navigation correction: the War tree's top tier is
  above the first view - the tree must be scrolled up
  (drag down) to reach it. The first view shows Expert
  Nurse and the Garrison row; scrolling down shows
  Drill Ground below; scrolling up reveals Troop
  Movement at the top with the Rallied row beneath it:
  Rallied HP 5/10, Rallied Attack 7/10, Rallied
  Defense 7/10. The Development tab (Auto Rally Max
  Level, Quick Construction 8/10, Great Helper Max
  Level, one node 2/10 below) holds no Rallied node.
- Finding, read live: the Rallied HP panel (5/10,
  Current +5%, Next Level +6%, matching the 2348
  record) offers NO donation interface at all - no
  Tech EXP bar, no Donation Reward row, no Donation
  Count, no Donate buttons. Instead it shows
  "Upgrade Countdown 07:28:29" and a blue Confirm
  button. The node is upgrading: between the 2348
  record (Tech EXP 1.9M/2.0M at 23:35) and this read
  it filled and entered its upgrade countdown, which
  runs to about 13:20 local. The Confirm button was
  NOT tapped - its function while a countdown runs is
  unverified, and confirming an upgrade is not a
  routine donation act.
- Consequence for this unit: the re-read it was
  created for cannot be satisfied on this node - there
  is no count to read here. Status partial, tracker
  untouched, no donations made in this unit, no
  diamonds or money spent.
- No new re-read unit is enqueued from this unit: the
  global count was already read live in the previous
  unit of this pass (0545 record: 8/30 down to 1/30,
  then greyed on a 00:09:54 timer), and its re-read
  unit (donations-2026-11-02-1344, not-before
  2026-11-02T13:55:00Z) already covers the post-timer
  check. Rallied HP's own upgrade completes about
  13:20 local; whether donations to it reopen then
  is for a later donations unit to discover, not a
  unit to pre-enqueue.
- Note for the metadata (not edited here, tier-2):
  the War tree's Rallied tier sits above Expert Nurse
  and is only reachable by scrolling the tree up;
  units that name a Rallied node must scroll up first
  instead of reporting it missing. The replenishment
  question this unit's window rested on is already
  tracked as GitHub Issue #160 (filed from the 2348
  record); this unit adds the upgrading-node state
  as a second reason a named panel may offer no count.
- Result stats: target 30, achieved unverified,
  verified no, blocker_category d (no count offered on
  an upgrading node). Donations landed in this unit: 0.
