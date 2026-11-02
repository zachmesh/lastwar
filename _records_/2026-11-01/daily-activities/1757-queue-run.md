---
title: Pre-reset zero sweep first pass 1757
created: 2026-11-02T01:57:00Z
modified: 2026-11-02T01:57:00Z
version: 1.0.0
description: Zero sweep unit zero-sweep-pre-reset-sweep-2026-11-01-001 by ticker-1738, first pass before the 19:00 reset
status: partial
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-01
  - source: day unit records in _records_/2026-11-01, cited per line
---

# 1757 queue run - pre-reset zero sweep, first pass (partial)

Zero sweep unit zero-sweep-pre-reset-sweep-2026-11-01-001
by ticker-1738, session cc-72 then cc-75 (the control
session dropped once and was restarted), window mode
642x951, no different-device dialog. Session window
about 17:46 to 17:57 local. This is the first zero sweep
ever run, so it is recorded as partial: not all 23 ledger
lines were live-read inside this unit. Lines rest either
on a live read in this unit, on the day last live read
named below, or as unreadable, and every not-at-zero
line names its fix-up unit. The final sweep at 18:30
re-walks the list. No other task type was worked inside
this unit: no bubble was collected, no truck dispatched
or plundered, no donation made, no chest claimed, no
secret task tapped.

## Lines read live in this unit

- Base screen at about 17:55: harvest bubbles standing
  over the central building cluster (lines 1-4 not at
  zero as a group; the per-resource split was not read,
  so the split is not claimed per line). Resource bar
  read food 344.7M, iron 532.2M, coin 25.4M. Events icon
  carried a red x2 badge, so the Events surface is not
  at zero; fix-up events-2026-11-01-1857.
- Secret Command Post panel, reached by a wrong-entry
  tap on the left rail: Secret Mobile Squad reads
  Assist Allies 2/3, Plunder Others 0/3, with UR and SSR
  tasks standing. No task was tapped. Fix-up
  secrets-2026-11-01-1857.
- Duel total line: read in this pass star-ceremony
  unit, not in this sweep unit itself - League S38
  calculating, Weekly Ranking Bears Lair rank 190 with
  17,240,439 weekly points, personal daily total
  unverified. Re-read fix-up
  star-ceremony-2026-11-01-1830.

## All 23 ledger lines

1. Food bubbles - not at zero (bubbles standing, 17:55
   base view). Fix-up harvest-2026-11-01-1803.
2. Iron bubbles - not at zero (same view; split not
   read per line). Fix-up harvest-2026-11-01-1803.
3. Coin bubbles - not at zero (same view; split not
   read per line). Fix-up harvest-2026-11-01-1803.
4. EXP bubbles - not at zero (same view; split not
   read per line). Fix-up harvest-2026-11-01-1803.
5. Titanium bubbles - unreadable (titanium cluster not
   in this view; no full-base pan done). Fix-up
   harvest-2026-11-01-1803.
6. Armed Truck - unreadable (no fully-loaded notice or
   timer read in this unit). Fix-up
   harvest-2026-11-01-1803.
7. Drone components - unreadable (no shop or pass
   screen read in this unit). Fix-up
   passes-2026-11-01-1857.
8. Upgrade ore - unreadable (no reward popup
   transcribed in this unit). No dedicated fix-up type;
   radar, shop and event units transcribe on their runs.
9. Screws - unreadable (same as ore). No dedicated
   fix-up type; same transcription route.
10. Shop Daily Pickup and Free Supply - unreadable (no
    shop screen read in this unit). Fix-up
    passes-2026-11-01-1857.
11. Pass daily pickups - at zero per last live read
    10:40 (all daily pickups already claimed), to be
    re-verified by passes-2026-11-01-1857.
12. VIP Daily Freebie - not at zero: never attempted
    today, tracker has no vip entry for 2026-11-01, and
    no pre-reset vip unit existed. NEW fix-up
    vip-2026-11-02-0151, priority 1, expires at the
    19:00 reset.
13. VIP login chest - not at zero, same as line 12.
    Same NEW fix-up vip-2026-11-02-0151.
14. Daily activity chests - not at zero: activity 150
    at 14:49, chests 160 and 200 still ahead. No
    pre-reset missions unit existed. NEW fix-up
    daily-missions-2026-11-02-0151, priority 1, expires
    at the 19:00 reset.
15. Mail, six categories - not at zero: the previous
    pass mail unit closed partial 17:23-17:31 with
    categories unread and nothing claimed. Fix-up
    mail-2026-11-01-1830.
16. Alliance gifts - at zero per last live read 17:19
    (Regular 4 claimed, Premium 0 new), to be
    re-verified by gifts-2026-11-01-1830.
17. Alliance donations, 30 of 30 - not at zero and
    unverified: the 11:32 tracker note says 9 coin
    donations, but the 16:06 unit read Donation Count
    1 of 30 and its final count hid behind the
    cooldown timer, so no closing count exists.
    Fix-up donations-2026-11-01-1803.
18. Trucks, dispatch 5 of 5 and plunder 4 of 4 - not
    at zero: last live read 13:52 was Trade Count 4
    of 5 and Plunder Count 1 of 4, a dispatch gap of
    1 and a plunder gap of 3. This sweep own trade
    panel read failed on a wrong left-rail entry (see
    blocker below). Fix-ups trucks-2026-11-01-1457
    (already eligible) and trucks-2026-11-01-1857.
19. Alliance train, per service - at zero per last
    live read 13:23 (no train in preparation), to be
    re-checked by train-2026-11-01-1830.
20. Radar, by duel posture - stack posture per last
    live read 11:20 (5 tasks executed unclaimed, 11
    pending rewards); a stack posture is not a miss.
    Re-check radar-2026-11-01-1803.
21. Alliance Duel daily total against 3,600,000 -
    unverified (this pass star-ceremony unit, League
    S38 calculating state). Re-read
    star-ceremony-2026-11-01-1830.
22. Crystal - not located, age 7 days from 2026-10-25
    (rule R5 owner-named item). Standing unit
    crystal-shop-2026-11-01-0500 already in inbox,
    priority 1.
23. Glittering Market - not located, age 1 day from
    2026-10-31 (rule R5 owner-named item). Standing
    unit glittering-market-2026-11-01-0501 already in
    inbox, priority 1.

## Fix-up units enqueued by this sweep

- vip-2026-11-02-0151 (priority 1, expires 19:00 reset)
- daily-missions-2026-11-02-0151 (priority 1, expires
  19:00 reset)

All other not-at-zero lines already had a unit eligible
before the reset in inbox, so no duplicate was enqueued;
those units are named per line above.

## Blocker, named for the next unit

- The Secret Command Post back arrow resisted three
  background-click variants (two at norm 42,940, one
  at the re-measured button centre 66,957); the panel
  was left open at sweep close. The next unit must exit
  this panel with a fresh method (foreground click or
  another route) before reaching the base screen. The
  panel back control is the only control in this pass
  that resisted background clicks; back arrows from
  Mail and Duel League worked normally earlier in the
  pass.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  research or building started, no player attacked, no
  assemble or teleport. No secret task, truck, donation
  or claim was executed inside this sweep unit.
