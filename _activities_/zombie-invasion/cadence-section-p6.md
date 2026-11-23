---
title: Cadence part 6
created: 2026-11-23T06:53:20Z
modified: 2026-11-23T06:53:20Z
version: 0.1.0
sequence: 10
description: Coin collection, owner instruction 2026-10-28 - the coins this event pays collect behind the task collection
---
- Coin collection, owner instruction 2026-10-28 - the coins
  this event pays collect behind the task collection icon and
  are received only when it is tapped. Every zombie unit shall
  collect from it. The icon shows as a gift box with a red
  dot carrying a number - the count of task rewards waiting
  to be claimed (owner word 2026-10-28; at the owner's
  reading the dot showed 4, four task rewards to claim). The
  number is live - it grows as more tasks are performed
  (owner word 2026-10-28), so record the number seen before
  tapping as the stat tasks_badge, and confirm it clears
  after claiming. VERIFIED by chain unit 003 on 2026-10-28 -
  the icon is the gift box at the right end of the March
  queue bar at the bottom of the screen (not on the event
  page), its badge counting loot entries waiting (3 at first
  sight, 5 at tap time). Tapping it opens the LOOT panel, one
  row per kill, whose single Claim All button is plain blue
  with NO price tag - that is the free claim to use; the
  price-tagged Claim All purchase stays banned as always.
  Kills pay nothing directly - the coin sits in the LOOT
  panel until claimed. Unit 003 claimed 5 rows for 1,072,000
  coins (about 214,400 per Lv.10 row), coin 34,416,573 to
  35,488,573. Record the collected amount as coins_collected
  alongside coin_before and coin_after, every unit. Row
  values vary - the two rows claimed in units 006 and 007
  on 2026-10-28 each read coin 268.0K on the row and each
  moved the exact panel by exactly 268,000 (35,488,573 to
  35,756,573, then 35,756,573 to 36,024,573), so later-wave
  Lv.10 rows pay more than the round 1 average; read each
  row's coin line rather than assuming the average.
- Stop condition, owner instruction 2026-10-28 - do not stop
  while zombies remain nearby. Keep sweeping or attacking the
  zombies near the base until none remain nearby, refilling
  stamina as needed. The campaign itself ends only when the
  event ends or continuing would cross a red line.
- The one hour pause, owner correction 2026-10-28 - pause for
  1 hour ONLY when no zombies are nearby - the next check is
  scheduled 1 hour later because new zombies may appear (waves
  arrive about hourly). A pause never ends the campaign; when
  the hour is up, play resumes and continues.
