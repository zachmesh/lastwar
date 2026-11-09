---
title: Queue Run 0841 Alliance Donations Re-read
created: 2026-11-08T16:41:00Z
modified: 2026-11-08T16:41:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1146, re-read after cooldown, partial - one coin donation dispatched from a live-read 1/30, landing unverified behind a 00:16:27 timer
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 08:38-08:41 America/Los_Angeles
---

# 0841 queue run - alliance donations re-read (donations-2026-11-08-1146)

- Unit: donations-2026-11-08-1146, executor ticker-0834.
  Status: partial - one coin donation dispatched from a
  live-read 1/30, landing UNVERIFIED behind a 00:16:27
  timer that hides the count. The unit closes unverified
  per the hard closing rule in the alliance-donations
  metadata (rule R1). Tracker untouched; the re-read
  for this tap is the already-queued
  donations-2026-11-08-1621 (not-before 16:40:00Z),
  which the 09:04 tick will pick up after this timer
  clears at about 08:57 local. No duplicate re-read
  unit is enqueued.
- Session: computer session cc-99 on the owner Mac
  mini (1c817413-83e2-0545-cb90-36d5e096a6bd).
  No device-access error, no different-device dialog,
  no login demanded. Session ended cleanly at the
  unit close.
- Entry route: the game was found already on the
  ALLIANCE TECHS screen (left there by the 0804 pass),
  Development tab, Quick Construction 8/10 carrying
  the recommended marker. The node was tapped at its
  grounded centre (283,518) and the donation panel
  opened first try. Base resources at entry: food
  478.8M, iron 802.1M, coin 6.9M, badge 302.9K,
  diamonds 4,397.

## What was read and done, live in this unit

- Quick Construction panel (Development tab, 8/10,
  "Increased Building Speed for Allies", Donation
  Reward +20%, Tech EXP Required 1.4M/6.0M, Current
  +20%, Next Level +22.5%, Donation Reward EXP 50 +
  badge 50): Donation Count read live at entry:
  **1/30**. This proves the 0804 unit's third tap did
  NOT land - its 00:17:33 timer had cleared and the
  count still showed 1 remaining. The green coin
  Donate 900 button was live, not greyed.
- One tap (green Donate 900, grounded centre 647,779,
  single tap): the coin button greyed with a **00:16:27**
  cooldown timer and the badge moved 302.9K to 303.0K,
  but the count label is hidden behind the timer, so
  whether this tap landed is UNVERIFIED. No arithmetic
  final is claimed as the closing count. The grey-plus-
  badge signature is confirmed NOT to be landing
  evidence for a third unit in a row (0704, 0804, this
  unit).
- Footer re-read live at close (panel closed back to
  the tree screen): Tech Donation Today **4700**
  (entry 4600, delta +100). The delta does not
  reconcile with 50 points per coin donation over
  this unit's one dispatched donation, so the footer
  is NOT used as a count proxy - it is recorded only
  as an observed figure. The 0804 unit saw +200 for
  one verified donation; this unit saw +100 for one
  dispatched donation. The footer moves independently
  of verified donations.

## Findings

- The 0804 unit's third tap is now proven eaten: count
  1/30 at this unit's entry, after its timer cleared.
  The burst-cap eaten-tap signature (grey button, badge
  move, count unchanged after the timer) now has three
  consecutive confirmations (0704 fourth tap, 0804
  second tap, 0804 third tap confirmed here).
- Cooldown timers inside a burst stay long: 00:16:27
  after this unit's single tap from 1/30 (0804 saw
  00:17:33 after its third tap). A tap from 1/30
  therefore always costs a re-read unit after a
  roughly 17 minute timer.
- This unit (1146) was a stale re-read enqueued at
  03:46 local whose window described an older count
  state; it was executed as a live re-read of the
  current count, which is what the queue needed, and
  its result supersedes its window text.

## Follow-up

- Re-read owed after this unit's 00:16:27 timer clears
  at about 08:57 local: the already-queued
  donations-2026-11-08-1621 (not-before 2026-11-08
  16:40:00Z) is designated the re-read for this tap -
  it reads the Donation Count live and, if it still
  shows 1 remaining, donates once more; if 0, the day
  is done and the tracker is marked. No new re-read
  unit was enqueued from this unit.
- Issue 450 already carries the replenishment, burst-cap
  and timer measurements; no new issue is filed from
  this unit.
- Tracker untouched (partial/unverified unit).
- No diamonds spent, no purchase tapped, no red line
  crossed. Coins spent: 900 dispatched, unverified.
