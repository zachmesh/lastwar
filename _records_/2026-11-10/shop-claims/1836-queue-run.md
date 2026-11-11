---
title: Shop claims queue run 1836
created: 2026-11-11T02:36:00Z
modified: 2026-11-11T02:36:00Z
level: L0
version: 1.0.0
description: Passes unit passes-2026-11-10-1457, Hot Deals free pack claimed, Free Supply auto-claimed, Monthly Pass daily gift claimed, no weekly pass owned
status: unverified
---

# Shop claims 18:36 to 18:46 - ticker-1834

Unit passes-2026-11-10-1457 (planned for the 14:57 cycle,
expires 18:57). Executor ticker-1834. Session cc-490 on the owner
Mac mini, LastWar already open.

## What was claimed live

- HOT DEALS free pack: RESEARCH SPEED-UP PACK, timer 23:18:39,
  Availability 1 - 1h Research Speed-up x25 and Coin Chest
  (UR) x5. Free Claim tapped once; CONGRATULATIONS panel
  verified both items, then "Packs sold out" behind it.
- Free Supply auto-claim: on the same Hot Deals open, "Free
  rewards have been automatically claimed" - blue chest x1
  and ruby x10.
- Super Monthly Pass Daily Pickup: Monthly Pass, Squad 4
  Lv.20, Days Left 11, Rewards Left 11. Claim Reward tapped
  once; DAILY GIFT panel verified - gold bars x2, red
  diamonds x100, gold tickets x2, iron x200, 5-minute
  speedups x60 - and the button now reads Claimed (grey).
  The $24.99 Monthly Pass Extension was left untouched.

## What was checked and left alone

- Weekly Pass: rewards reset at 18:00:00 as displayed. All
  four pass cards verified in this unit - S2 Drone
  Components Weekly Pass (Legendary, Daily Pickup x2,
  Total x7), S1 Drone Parts Weekly Pass (Epic, Daily Pickup
  x15, Total 105), Iron Weekly Pass (Elite, Daily Pickup
  x3, Total x21), Coin Weekly Pass (Elite, Daily Pickup x3,
  Total x21) - every one carries a Get Now $4.99 button,
  none is owned, no Claim button anywhere. The Legendary
  Take All $19.99 row was left untouched.
- Weekly Deal (2026-11-9 00:00:00 to 2026-11-15 23:59:59):
  three paid bundles only - Valor Badge $99.99, Base Upgrade
  $19.99, UR Set $49.99. Nothing free.
- Entry state: the game opened on the Alliance screen with
  the HELP dialog showing - both help requests 30/30 full,
  "Today's points gained from Alliance Help: 40/1,000".
  That is the help unit's work, not this unit's; the dialog
  was closed untouched and no Help All was tapped.

## Calibration learned in this unit

- computer.control coordinates are normalized 0-1000 on BOTH
  axes. The back-arrow taps at (168,872) failed three times
  with no change because y 872 landed above the button in
  image pixels; the measured centre is (168,917) and that tap
  navigated at once. The HELP dialog X closed at (841,200).
  Future units: convert screenshot pixels as x/642*1000 and
  y/951*1000.
- Scroll: scroll_amount 5 at (500,600) did not move the
  Weekly Pass list; a press-drag from (500,750) to (500,300)
  scrolled it, confirming the 1335 unit's finding.

## Outcome

- Three claims done: free pack, Free Supply, Monthly Pass
  daily gift. No weekly pass owned, nothing else claimable.
  Returned to the base screen.

## Figures read live on screen

- Food 631.3M, iron 954.1M, coin 97.8M, power 148,787,578,
  diamonds 6,267 at entry.
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 3, achieved 3, resources_gained Coin Chest (UR) x5
  plus 1h Research Speed-up x25 plus Monthly Pass daily
  gift (gold bars x2, red diamonds x100, gold tickets x2,
  iron x200, 5-minute speedups x60) plus Free Supply (blue
  chest x1, ruby x10), costs about 10 minutes play, verified
  yes, blocker_category none, device_takeovers 0

No diamonds or money spent. No price button, Renew, paid
unlock or Legendary Take All tapped. No other task type was
executed in this unit.
