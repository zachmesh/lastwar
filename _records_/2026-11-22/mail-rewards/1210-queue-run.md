---
title: Mail Event list read whole: no claimable mail 1210
created: 2026-11-26T12:11:19Z
modified: 2026-11-26T12:11:19Z
version: 1.0.0
description: Unit mail-2026-11-26-0630 (the Event list with ONE composed pan, Steer A 12:01Z; version 1.0.366(908); front LastWar at the start 12:10:35Z; owner idle 1,178 s; the different-device dialog never on screen; no UserNotificationCenter) - FIRST FRAME (12:10:42.0Z; Warzone Duel timer 13:49:19): the Mail button WITHOUT a dot; HUD: food 51.8M, iron 686.0M, coin 14.6M, diamonds 10,673; the Mail envelope (670,787) tapped once, the category Event (400,378) tapped once; THE EVENT LIST BEFORE THE PAN (12:10:59.9Z): six rows, all greyed (read), no Claim button or gift icon: (1) an ally's 'Missile Mega Ex...' 1h ago, (2) an ally's 'train has ...' 1h ago, (3) an ally's 'train...' 4h ago, (4) an ally's 'Mega Exp...' 5h ago, (5) an ally's 'train...' 6h ago, (6) 'Code 87 Individual Reward' 6h ago (partly cut off); the buttons Search, Delete All, Claim All (NOT pressed), the back arrow; THE ONE COMPOSED PAN (12:11:07.1Z): start (670,720) on the list's right margin (a plain gap right of the rows), end (670,570), 1 s hold: not refused, not flung; it moved the list about 125 px (the second row's title y 359 to y 234); THE ROWS BELOW THE SIXTH (12:11:12.9Z): ONE new row: a second 'Code 87 Individual Reward' 6h ago (read); nothing else below: THE WHOLE LIST IS SEVEN ROWS, ALL READ; NO mail titled 'Train arrival reward!', 'UNCLAIMED ARMS RACE EVENT' or 'GLITTERING MARKET UNCLAIMED' exists in the Event list (so nothing to claim and no row to quote); no claim made; Claim All, Delete All, Read All never pressed; the Mail screen left by its back arrow twice (113,935); no TIPS popup; the Mail button without a dot at the end; the In-app Purchases category carries a red dot (not opened); NOTE: the Claim All pressed once on the Event list at 11:56:54.7Z (record 1150) came before the 12:01Z rule: it paid nothing (no popup, HUD unchanged) and the named mails were not in the list; the base; drags 1 (the composed pan, in the list margin, not on the base map)
status: done
grounded_in:
  - source: cu_bridge run 20261126T121036Z-9b52db, final report read by the operator, 2026-11-26T12:10Z to 12:12Z
  - source: unit brief mail-2026-11-26-0630 and the mail-rewards rule digest
---

# Mail Event list read whole: no claimable mail 1210

Rows in [1210-queue-run.csv](1210-queue-run.csv). Claimed 12:10:35Z; no different-device dialog.

- **Whole Event list read** (one composed pan inside the list margin): seven rows, all read: an ally's Mega Exp x2 and train mails x3, and two Code 87 Individual Reward rows (6h ago).
- **Rows below the sixth:** one, a second Code 87 Individual Reward; the list ends there.
- **The three named mails** ('Train arrival reward!', 'UNCLAIMED ARMS RACE EVENT', 'GLITTERING MARKET UNCLAIMED') are not in the list: nothing to claim or quote.
- **Counts.** No Claim All, Delete All or Claim pressed; the Mail button has no dot; the dialog never showed; the earlier 11:56:54.7Z Claim All (record 1150) paid nothing; drags 1 (the composed pan in the list margin).
- **Run.** One run, 9 steps, 5 actions, 0.119445 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 12:11:34Z.
