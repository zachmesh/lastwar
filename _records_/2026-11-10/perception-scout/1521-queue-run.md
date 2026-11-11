---
title: Scout pass 1521
created: 2026-11-10T23:21:00Z
modified: 2026-11-10T23:21:00Z
version: 1.0.0
description: Partial perception-scout pass by ticker-1503 - base re-read, Drill Ground level-up and upgrade panel
---

# Scout pass 1521 - perception-scout (partial)

- Unit: scout-2026-11-09-1800, executor ticker-1503
- Session: 15:12 to 15:21 local, Mac mini, LastWar window 642x951, computer session cc-474
- Status: partial - pass incomplete, unwalked surfaces named below
- Slot note: this unit's slot was the 2026-11-09 post-reset
  pass (18:00 local 2026-11-09); that reset day had already
  ended at the 19:00 reset. The pass was executed against the
  live game instead of being left to expire, and its
  observations were recorded in the current reset day file
  _records_/2026-11-10/perception-scout/observation.md, the
  second perception of reset day 2026-11-10. Nothing was
  attributed to 2026-11-09. Precedent: ticker-0604 on
  2026-11-09 and ticker-0604 on 2026-11-10 (0615 record) did
  the same with stale scout heads.

## What was walked

- Base screen and HUD, read live from screenshots at 15:12 -
  top-bar power 148,765,978, food 629.3M, iron 952.1M, coin
  92.6M, diamonds 6,267, stamina 120, level 30; building
  queue 1 of 4, research 1 of 2, task "Build: Oil Well
  [0/1]", truck icon with a question marker, radio/broadcast
  icon with a red badge 11 (new number since the 06:14 read).
  Events badge 2, VS 02:52:20, Season II 3d 03:02:20.
- Drill Ground level-up, observed 15:13 - "DRILL GROUND LEVEL
  UP!" celebration surfaced after the first Inventory tap;
  Power 118,600 to 140,200, Unit Count +7,200 to +7,400; the
  24.0M EXP reward card was not tapped. Power re-read live
  after dismissal at 148,787,578, confirming +21,600.
  Building now reads Drill Ground Lv.27.
- Drill Ground upgrade panel, inspected only - Lv.27 to 28,
  Hero EXP 26.0M, Unit Count +7,400 to +7,600, Power 140,200
  to 165,800; costs all met (Lv.28 Headquarters, iron
  952.1M/102.0M, food 629.3M/314.5M); Original Time 30d
  01:27:10, Upgrade button 14d 07:32:57. "Finish Now 33,887"
  diamonds and "Upgrade" both untouched (red lines). Panel
  closed via X.
- Alliance signal - toast "Alliance Gift (R) received!"
  about 15:15; the gifts regular owns the claim.

## Red dots - 8 seen, 5 explained, 3 unexplained

- Explained: hammer and flask queue indicators; Events badge 2
  (Age of Oil 1, Survey Center 1, carried from the 06:14
  read); Alliance dot (Wars, Help, Gifts, Techs, carried);
  Mail dot 1 (Alliance, In-app Purchases, carried).
- Unexplained: Inventory red dot (contents not opened - two
  taps at the stale point 880,841 failed, see below); skull
  icon badge 1 with a 00:00:47 countdown (carried from
  2026-11-09, badge moved 13 to 1); radio/broadcast icon
  badge 11 (new number since 06:14).

## Inventory point retired (rule R2)

Two taps at normalized 880,841 (grounded from the first base
screenshot) did not open Inventory: the first surfaced the
Drill Ground level-up modal; the second panned the base view
and exposed a three-button shortcut cluster at the bottom
right (blue people, blue cap, green up-arrow), whose green
button opened the Drill Ground upgrade panel instead of
collapsing the cluster. The point is retired inside this unit.
The successor must re-ground Inventory from a fresh full base
screenshot and must not reuse 880,841 blindly after a view
pan.

## Not walked in this pass

Store by section, VIP page, passes pages, daily missions panel,
duel page, radar panel, world map pins and loot box, Inventory
contents, hero screens, and the Age of Oil, Survey Center,
Wanted Boss, Arms Race and Community event pages. The staged scout-midday-2026-11-10-0700 unit (07:00
local) covers them; no duplicate successor was enqueued.

## Scout discipline

Observe only - no claim, fight, dispatch, donation or purchase
was made. No Upgrade, Finish Now, price tag or paid button was
tapped. Delete All in mail was never tapped.

## Diff and follow-up

- No scout_diff.py run in this pass: the unit hit its 15
  minute cap at 15:23 with the token lease ending 15:20:51,
  so the diff is left to the next scout pass.
- New observed item: Drill Ground Lv.27 to 28 upgrade
  available with all costs met (owning regular `new` - no
  building-upgrade regular in the roster; diff to route).
  No issue filed: building upgrades are owner-initiative
  work, not a queue gap or failure mode, and the perception
  design routes new items through the diff.
- Unwalked surfaces pass to the staged
  scout-midday-2026-11-10-0700 unit (07:00 local).
- Unexplained red dots (Inventory, skull badge 1,
  radio badge 11) carry to that pass; the skull signal is
  now on its fourth sighting with a moving badge and needs
  an owner-named read if it persists.

## Correction (appended same pass, C1)

- Session window: the 15:12 to 15:21 times above are estimates
  from the run clock; the computer session cc-474 ran inside
  the token lease taken 15:05:51 local. Do not cite the
  end minute as exact.
- VS timer: the first base screenshot read 02:52:20 and a
  later compact observe read 01:51:18. The wall time between
  the two reads was minutes, not 61 minutes, so the two
  reads conflict and the VS timer value is unverified - do
  not carry either figure forward as a live read. All other
  figures in this record are single live reads and stand.

- Resolution (from the harvest unit of the same pass): the VS
  timer read 02:39:31 at about 15:22 and 02:35:02 at about
  15:31, a consistent countdown from the 02:52:20 read at
  about 15:12. The "01:51:18" compact-OCR read was a misread
  of 02:51:18. The 02:52:20 figure stands as a live read.
