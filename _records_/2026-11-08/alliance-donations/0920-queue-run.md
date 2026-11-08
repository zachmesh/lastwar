---
title: Queue Run 0920 Alliance Donations Re-read
created: 2026-11-08T17:21:00Z
modified: 2026-11-08T17:21:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1318, re-read after cooldown, partial - one coin donation dispatched from a live-read 1/30, proven not landed after its 00:07:01 timer cleared, plus a long-press variant that did nothing
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 09:06-09:20 America/Los_Angeles
---

# 0920 queue run - alliance donations re-read (donations-2026-11-08-1318)

- Unit: donations-2026-11-08-1318, executor ticker-0904.
  Status: partial - one coin donation dispatched from a
  live-read 1/30, proven NOT landed by a live re-read
  after its timer cleared, and a long-press variant
  that dispatched nothing. The unit closes unverified
  per the hard closing rule in the alliance-donations
  metadata (rule R1). Tracker untouched; the re-read
  for this tap is the already-queued
  donations-2026-11-08-1621 (not-before passed), which
  runs on a later tick. No duplicate re-read unit is
  enqueued.
- Session: computer session cc-101 on the owner Mac
  mini (1c817413-83e2-0545-cb90-36d5e096a6bd), then
  cc-102 after cc-101 closed itself during the 7.5
  minute timer wait - reopened without issue, game
  still on the donation panel. No device-access error,
  no different-device dialog, no login demanded.
- Entry route: game found on the base screen.
  Alliance button tapped at the fresh grounded centre
  (934,720), Alliance Techs tile at (674,681),
  Development tab, Quick Construction 8/10 carrying
  the recommended marker, node tapped at its grounded
  centre (284,529). All three points measured fresh
  on this unit's screenshots, none carried.
  Base resources at entry: food 478.8M, iron 802.1M,
  coin 6.9M, badge 303.0K, diamonds 4,397.

## What was read and done, live in this unit

- Quick Construction panel (Development tab, 8/10,
  "Increased Building Speed for Allies", Donation
  Reward +20%, Tech EXP Required 1.4M/6.0M, Current
  +20%, Next Level +22.5%, Donation Reward EXP 50 +
  badge 50): Donation Count read live at entry:
  **1/30**. This proves the 0841 unit's tap did NOT
  land - its 00:16:27 timer had cleared and the count
  still showed 1 remaining. The green coin Donate 900
  button was live, not greyed. Tech Donation Today
  read 4700 at entry, unchanged from the 0841 close.
- One tap (green Donate 900, grounded centre 648,782,
  single tap): the coin button greyed with a **00:07:01**
  cooldown timer and the badge moved 303.0K to 303.1K,
  but the count label is hidden behind the timer.
  The timer is notably shorter than the 00:16:27 and
  00:17:33 timers seen after taps from 1/30 by the
  0841 and 0804 units.
- Timer waited out inside the unit (7.5 minutes):
  after it cleared, Donation Count read live again:
  **still 1/30**, button green again. This tap did
  NOT land. That is the fifth eaten-tap confirmation
  in the series (0704 fourth tap, 0804 second tap,
  0804 third tap confirmed by 0841, 0841 tap confirmed
  by this unit's entry read, this unit's tap confirmed
  by this unit's post-timer re-read).
- Changed-method variant per queue rule R2 (second
  consecutive partial with this blocker must arrive
  with a changed method): a 2-second long-press on
  the green Donate button at the same grounded centre
  (648,782). Result: no change - no grey-out, no
  timer, no badge move, count still 1/30. Long-press
  is a no-op on this button, not a landing variant.
- Footer at close not re-read (panel left open, unit
  budget ended); entry footer 4700 recorded only.

## Findings

- The 1/30 stickiness is now the third consecutive
  donations unit closing partial on this same blocker
  (1523, 1146, this unit - 1523 also verified a 2 to 1
  landing before its 1/30 taps failed, so taps land
  fine at count 2 and fail at count 1). Per queue rule
  R2 the third consecutive partial writes the blocker
  into the activity metadata, changes the entry route
  before any further unit of that type runs, and is
  named in the day round summary. The blocker is
  already documented in the activity metadata (hard
  closing rule and burst-cap sections), so no tier-2
  metadata edit is swept into this records commit -
  the new measurements go to Issue 450, the
  established carrier for this blocker, and the
  changed route is stated below and in that issue
  comment for the next executor to read.
- Changed route for the next donations unit: do NOT
  tap from 1/30 on Quick Construction again. If the
  count reads 1/30, first check whether it has
  replenished above 1 (the count replenishes over
  time - 1/30 to 4/30 seen at 1346, 1/30 to 2/30 at
  1523), or try the War-tab node (Rallied Attack /
  Rallied Defense) as the changed entry route.
- Replenishment caveat on the "proven eaten" claim:
  because the count replenishes, "count unchanged
  after the timer" cannot strictly distinguish eaten
  from landed-plus-replenished inside one window.
  The repeated 1/30 stickiness across three
  consecutive units still stands as the blocker, but
  the proof is pattern-level, not per-tap.
- The 00:07:01 timer after this tap breaks the
  roughly-17-minute pattern of the two previous taps
  from 1/30. Timer length varies; it is recorded,
  not explained.

## Follow-up

- Re-read owed to the already-queued
  donations-2026-11-08-1621: it reads the Donation
  Count live and applies the changed route above -
  tap only if the count has replenished above 1, or
  try the War-tab node. No new re-read unit was
  enqueued from this unit.
- Measurements added to Issue 450 (comment from this
  unit): 00:07:01 timer, post-timer count still 1/30,
  long-press no-op, third consecutive partial, changed
  route stated. No new issue is filed from this unit.
- Tracker untouched (partial/unverified unit).
- No diamonds spent, no purchase tapped, no red line
  crossed. Coins spent: 900 dispatched, unverified.

## Session note

- Computer session cc-101 closed itself during the
  7.5 minute timer wait (observe returned
  observation_unavailable, no session open). Reopened
  as cc-102 with no device-access error and the game
  exactly where it was left. A session that idles
  through a wait does not survive the wait - future
  units that wait out a timer should expect to
  reopen the session.
