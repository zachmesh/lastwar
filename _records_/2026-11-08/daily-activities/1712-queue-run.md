---
title: Pre-reset zero sweep first pass 1712
created: 2026-11-09T01:12:00Z
modified: 2026-11-09T01:12:00Z
level: L0
version: 1.0.0
description: Zero sweep unit zero-sweep-2026-11-08-1630, partial - first pre-reset ledger walk, 11 lines not at zero, fix-ups already queued
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 17:06-17:12 America/Los_Angeles
  - source: execution records of 2026-11-08 in _records_/2026-11-08
---

# 1712 queue run - pre-reset zero sweep, first pass (partial)

Zero sweep unit zero-sweep-2026-11-08-1630 by ticker-1646,
session cc-142, window mode 642x951 after a relaunch. This is
a verification-only unit: no bubble was collected, no truck
dispatched or plundered, no donation made, no chest claimed,
no secret task tapped, no pass button tapped inside this unit.
Line statuses below cite the live base read of this unit plus
the same-day execution records named per line.

## Live reads in this unit

- Base screen about 17:12 local, after a server disconnect
  and relaunch (see below): power reads 149,209,253 as
  displayed, against 149,850,353 at the 16:58 and 16:12
  reads - a 641,100 step down with no fight, dispatch or
  claim in between in this pass. Recorded as displayed,
  cause unexplained, not asserted as a loss; the next unit
  that reads power should confirm whether the figure holds.
  Food 490.8M, iron 813.3M, coin 12.3M; second row 25.0M,
  922.2K; diamonds 13.22K; cart 4,417; stamina 120.
  Season II 7d 00:50:41. Wanted Boss badge 1, timer
  00:00:57 (was 00:00:32 at 16:58 - a new cycle, recorded
  as displayed).
- Harvest bubbles still standing over the central building
  cluster at 17:12 - gold, food and iron bubbles with
  values in the hundreds of K. Resource totals unchanged
  from 16:58.
- Badges about 17:12: Events icon red x2, Mail icon red
  dot, Inventory icon red dot, Alliance icon red dot,
  radio badge 4, white truck red dot 1, survivor portrait
  badge 10, megaphone badge 4. No train icon in the left
  column; no "Boarding closes in" banner under the
  resource bar - the banner area shows the "Upgrade
  Builder's Hut to Lv.26 [0/1]" quest line and a Breaking
  News line instead. Fourteenth same-day no-train
  confirmation (thirteenth in this pass's scout unit).
- Server disconnect: at about 17:06 the game showed
  "Server disconnected. Please restart the game." with a
  Confirm button. The Confirm tap closed the app (target
  app exited); the app was relaunched with open_app and
  returned to the base screen with state intact - no login
  demanded, no different-device dialog. Same class as the
  earlier Esc/Return crashes: state is server-side.

## All 23 ledger lines

1. Food bubbles - not at zero (bubbles standing, 17:12).
   Fix-up harvest-2026-11-08-1803 already in inbox.
2. Iron bubbles - not at zero (same view; split not read
   per line). Same fix-up.
3. Coin bubbles - not at zero (same view; split not read
   per line). Same fix-up.
4. EXP bubbles - not at zero (same view; split not read
   per line). Same fix-up.
5. Titanium bubbles - unreadable (no full-base pan in
   this unit). Same harvest fix-up.
6. Armed Truck - unreadable (no fully-loaded notice or
   timer read in this unit). Same harvest fix-up.
7. Drone components - unreadable as a zero line (no
   drone-component zero read taken in this unit).
   Fix-up passes-2026-11-08-1857 already in inbox.
8. Upgrade ore - unreadable (no reward popup transcribed
   in this unit). No dedicated fix-up type.
9. Screws - unreadable (same as ore). No dedicated
   fix-up type.
10. Shop Daily Pickup and Free Supply - at zero per the
    1455 passes unit read (claimed earlier today, none
    outstanding); not re-read in this unit.
11. Pass daily pickups - at zero per the 1455 passes unit
    read (tiers 1-6 already Claimed, no owned pickup
    outstanding); not re-read in this unit.
12. VIP Daily Freebie - not at zero: no vip-rewards record
    exists today at all, and vip-2026-11-07-1900 sits
    stalled in inbox (priority 1, about 22 hours old);
    the 0512 observation read the Freebie still claimable
    at about 05:11. Fix-up vip-2026-11-08-1800 already in
    inbox.
13. VIP login chest - not at zero, same fix-up (never
    attempted today).
14. Daily activity chests - not at zero: 1628 record,
    activity 70, 80-point chest 10 points short, tab
    badge 1 remaining. Fix-up daily-missions-2026-11-08-1800
    already in inbox.
15. Mail, six categories - not at zero: Mail badge red dot
    at 17:12; last mail unit 1423. Fix-up
    mail-2026-11-08-1830 already in inbox.
16. Alliance gifts - not at zero: the 1406 unit claimed
    both tabs in full, but the 1615 scout read the
    Alliance Gifts panel dot again at 16:14, so new gifts
    have arrived since; fix-up gifts-2026-11-08-1830
    already in inbox.
17. Alliance donations, 30 of 30 - not at zero and
    unverified: no closing count exists today (0937 scout
    read Donation Count 2/30, and the count replenishes
    during the day); donations-2026-11-08-1803 already in
    inbox.
18. Trucks, dispatch 5 of 5 and plunder 4 of 4 - not at
    zero and unverified: no live trade-counter read exists
    today (the 0415 "Plunder Others 0/5" note is not a
    trade-counter close); trucks-2026-11-08-1857 already
    in inbox.
19. Alliance train, per service - at zero per last live
    read (no train in preparation, fourteenth same-day
    confirmation); train-2026-11-08-1830 still in inbox
    for the evening check.
20. Radar, by duel posture - stack posture per the 1355
    record (stack-day check complete, stack locked until
    the release day); a stack posture is not a miss;
    radar-2026-11-08-1803 already in inbox.
21. Alliance Duel daily total against 3,600,000 -
    unverified (1441 record: total unmeasured, verified
    no for that line); fix-ups duel-score-2026-11-08-1830
    and star-ceremony-2026-11-08-1830 already in inbox.
22. Crystal - not located, age 14 days from 2026-10-25
    (rule R5 owner-named item). Closes on the daily named
    status per the ledger; no standing unit in inbox, no
    duplicate enqueued by this sweep.
23. Glittering Market - not located, age 8 days from
    2026-10-31 (rule R5 owner-named item). Same standing
    as line 22.

## Fix-up units enqueued by this sweep

None. Every not-at-zero line already had a fix-up unit in
inbox at sweep time, so enqueuing more would have
duplicated units. The risk this sweep surfaces is the
same as the 2026-11-01 final sweep: those fix-up units
were still unrun at about 17:10, about 50 minutes before
the 18:00 reset, so several lines are likely to expire
unclaimed at the reset. That is a scheduling shortfall,
not a sweep finding to fix by duplication. The second
sweep, zero-sweep-2026-11-08-1730, is still in inbox and
repeats this walk before the reset.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  research or building started, no player attacked, no
  assemble or teleport. The server-disconnect Confirm tap
  and the app relaunch were recovery only.
