---
title: Zombie Invasion
created: 2026-10-28T09:47:00Z
modified: 2026-11-11T09:32:17Z
level: L1
version: 1.27.0
description: Zombie Invasion event - sweeping zombies near the base for coins, one activity folder for zombie invasion knowledge
status: unverified
grounded_in:
  - source: owner instruction in main chat on 2026-10-28 - a Zombie Invasion task is going on, it is a source of coins, play as much as possible and record knowledge as you go
  - source: owner instruction in main chat on 2026-10-28 - do not stop playing Zombie Invasion until the nearby zombies are exhausted
  - source: owner standing rule on 2026-10-28 - stamina may be refilled from the Free Claim or from stamina resource items of 10 or 50
  - source: owner standing rule in main chat on 2026-10-28 - a session may run for a few hours and that is fine, keep playing until the nearby zombies are exhausted
  - source: owner correction in side chat on 2026-10-28 - do not limit zombie invasion tasks per day and no hour budget, superseding an earlier same-day instruction to also stop once 3 hours had been played
  - source: owner instruction in side chat on 2026-10-28 - pause one hour only if no zombies are nearby, otherwise keep running zombie invasion continuously during the entire activity period
  - source: owner instruction in side chat on 2026-10-28 - dispatch multiple teams in parallel during zombie invasion so rewards accumulate faster
  - source: owner instruction in main chat on 2026-10-28 - play proceeds in rounds so other tasks get their time, and rounds keep cycling while the event is available
  - source: owner decision in main chat on 2026-10-28 - execute maximize coin, redeem medals for Coin Chests in the event Store and open the 2 owned Coin Chest (SR) in inventory
  - source: ticker-1134 scout-discovery execution record 2026-11-09 1152 queue run (done, Zombie Invasion tab still absent from the Events hub tab bar, event still ended, no chain seeded; record commit d2df49670 on records/2026-11-09)
  - source: ticker-1345 arms-race execution record 2026-11-09 1345 queue run (partial, Zombie Invasion tab still absent from the Events hub, Arms Race, Winter Battlefield and Desert Battlefield visible, event still ended, no chain seeded; record commit 63eccdb92 on records/2026-11-09)
  - source: ticker-1806 alliance-gifts execution record 2026-11-10 1810 queue run (done, Zombie Invasion tab seen live in the Events hub tab bar about 18:11, beside Desert Battlefield and a partially visible "...f Oil" tab, after absence re-confirmed about 17:56 the same day; chain head zombie-2026-11-10-001 seeded for the next unit to verify the event page; record commit 20a62ff0 on records/2026-11-10)
  - source: ticker-1952 zombie-invasion execution record 2026-11-10 2008 queue run (partial, event page VERIFIED live - new variant Zombie Invasion - Glacieradon, 1 Lv.10 kill with LOOT claimed, wave still live at the unit cap, successor enqueued; record commit d29bc658c on records/2026-11-10)
  - source: ticker-2154 zombie-invasion execution record 2026-11-10 2219 queue run (partial, Glacieradon chain 002, 1 Lv.10 kill X:516 Y:394 with its LOOT row read before Claim All - coin 268,000 verified, boss clue counter 40/40 with the challenge opening 2026-11-12 18:00, parallel dispatch missed on two mistaps, Lv.28 Ironhead sighted, successor 003 enqueued; record commit b11294e7f on records/2026-11-10)
  - source: ticker-2334 zombie-invasion execution record 2026-11-10 2340 queue run (partial, Glacieradon chain 003, server maintenance blocked the first half - disconnect dialog, update restart, maintenance dialog, login retry recovered - 1 Lv.10 kill X:471 Y:355 with its LOOT row read before Claim All - coin 268,000 verified, event timer 2d 18:12:18, boss clue counter 40/40, challenge opens 2026-11-12 18:00, successor 004 enqueued; record commit 5c07e8d40 on records/2026-11-10)
  - source: ticker-0004 zombie-invasion execution record 2026-11-11 0030 queue run (partial, Glacieradon chain 004, first parallel dispatch squads_parallel 2, 2 Lv.10 kills with both LOOT rows read before Claim All - 536,000 coins, Store medal balance 4000 confirming +10 medals per Lv.10 kill, 120-medal row identified as Universal Exclusive Weapon Shard, successor 005 enqueued; record commit 9ba46aa1 on records/2026-11-11)
---

# Zombie invasion

## What this activity is

An event the owner flagged as live on 2026-10-28. Zombies near the
base can be swept or attacked, and the event pays coins - coin is
one of the most precious resources on this account and a standing
bottleneck (donations and upgrades compete for it). The owner
instruction of 2026-10-28 is to discover the event, play it as much
as possible, spend stamina on it including refills, and maximise
the coin yield, recording knowledge as it is learned. Executions
are recorded in `_records_/<date>/zombie-invasion/`, one file per
execution.

## How to enter

- Open the Events screen from the base and tap the Zombie
  Invasion tab (it carried a red badge at first sight). The page
  offers Store, Ranking and Rewards buttons, Alliance Finding and
  My Findings tabs, a next-wave countdown, and Search and Boss
  Search buttons at the bottom.
- Search jumps to the world map centred on an Invading Zombies
  target and opens its card - tap the crossed-swords button, pick
  a squad, and tap March.

## Cadence

- While the event is live, play it as much as possible - the owner
  wants the maximum coin yield, not a single token attempt.
- Coin measurement (added 2026-10-28 after the owner asked for
  the collected total) - every zombie unit records the exact
  coin panel reading at its start and at its end in its result
  stats (coin_before, coin_after). The activity's yield is
  judged on those deltas, never on HUD-rounded figures. As of
  the first two executions the verified yield is zero - the
  Lv.10 target card carries no coin line, and coins appear only
  as a possible drop in the reward pools.
- Parallel teams, owner instruction 2026-10-28 - dispatch
  multiple teams in parallel. Do not send one squad, wait for
  its return, then send the next - keep as many squads
  marching on nearby zombies simultaneously as the game
  allows, so kills and rewards accumulate faster inside each
  unit's 15 minutes. Record how many squads ran in parallel
  as the stat squads_parallel. Enforcement, owner check
  2026-10-28 - units 001 to 004 in fact ran with
  squads_parallel 1, which does not meet this instruction.
  From unit 005 onward parallel dispatch is mandatory where
  the game allows it - a unit that still records
  squads_parallel 1 must state in its summary why parallel
  dispatch was impossible, and any game-side cap found
  (march queue limit, stamina supply, march slots) is
  recorded here with the observed number. Unit 005
  (2026-10-28) also could not dispatch - the wave was
  exhausted and Search answered not found, so its
  squads_parallel is 0 for lack of targets, which is not a
  cap. MEASURED by unit 007 on 2026-10-28 - the March
  Queues bar reads 0/4 with no squad out and 1/4 with one
  out, so the march queue cap is 4 squads. The binding
  constraint in the 11:42Z wave was different (unit 006) -
  two extra marches failed at the March tap with the
  toast "The target location has changed. Please try
  again." and charged no stamina; Search targets in a
  fresh wave move or are taken within tens of seconds,
  so a dispatch that pauses to read screens loses its
  target. Batched click sequences (Events, Search,
  attack, March in one action batch, no screenshot reads
  in between) dispatched cleanly twice in units 006 and
  007 - that is now the standard dispatch method, and a
  parallel attempt should batch the second squad's whole
  sequence the same way immediately after the first
  March. (2026-11-10 2219 update: parallel dispatch missed again in the Glacieradon variant - while Squad 1 was out, a tap at 498,505 opened a Teleport/Profession tile menu instead (the map had shifted under the aim point) and the follow-up at 450,350 opened a Lv.28 Ironhead card; no second march, squads_parallel 1. The binding limit was the short round trip (about 80 seconds) plus the two mistaps, not the march cap of 4. Re-ground every map tap on the current screenshot - the map is dense with tappable tiles here.) (2026-11-10 2340 update: squads_parallel 1 again - the maintenance recovery consumed the first half of the unit window, leaving no time for a parallel second dispatch; the binding limit was the remaining unit time, not the march cap of 4. The successor should run parallel dispatches while the wave lasts.) (2026-11-11 0030 update: squads_parallel 2 ACHIEVED for the first time in this variant - while Squad 1 was out, Events back to the Glacieradon page and a second Search found another Lv.10 target; Squad 2 auto-selected in the deploy panel (no squad-tab tap needed, per unit 024); the second march dispatched inside Squad 1's outbound window. The binding limit was the short round trips, not the march cap of 4. The owner instruction (dispatch multiple teams in parallel) is now met in this variant; the successor keeps running parallel dispatches while the wave lasts.) Squad 2's deploy panel (unit 006) - 20.92M
  power, five Lv.150 heroes, Unit Count 2,175 of 2,175;
  its versus line read Unknown / Evenly Matched against
  the same Lv.10 card Squad 1 read as 670,000 / Easy
  Win, unexplained.
- Objective, owner instruction 2026-10-28 - maximize coin.
  Coin is one of the most needed resources on this account,
  and this activity exists to produce it. Units are judged on
  coins collected per hour (coins_collected over duration).
  Once the paying sources are pinned down, prefer them -
  the best coin per stamina across target levels, any reward
  crates the kills drop, and the event Rewards track when it
  pays coins - and record the yield per source in the unit
  stats so the preference is evidence, not habit.
- Coin chests, owner decision 2026-10-28 - execute the
  maximize-coin conversion without asking again. (a) Open
  Coin Chests already owned in inventory (2 Coin Chest (SR)
  at the decision, about 812.16K coins each by tooltip) and
  record the exact yield per chest. (b) Redeem medals for
  Coin Chests in the event Store - until both prices and
  yields are measured, redeem SR first; once the SR price
  and the SSR yield are known, follow the better coins per
  medal and record the comparison. Keep enough medals in
  reserve only for the stamina loop (a 50 stamina item costs
  10 medals) when stamina is the binding constraint. Record
  medal balance and chest counts in the unit stats. This
  authorization covers medal-denominated Store redemptions
  for Coin Chests and the opening of owned chests only - it
  does not extend to any diamond or money purchase.
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
- No limits, owner correction 2026-10-28 - there is no limit on
  zombie invasion tasks per day, no session length cap and no
  chain hour budget. This supersedes an earlier same-day
  instruction to also stop once 3 hours had been played - that
  cap no longer exists. Long sessions are fine by the owner's
  standing rule; do not cut play short because of how long it
  takes. Before any pause, claim all earned rewards.

## Scope and availability

- Stamina use is authorised for this activity, including refills -
  Free Claim first, then the 10 stamina and 50 stamina resource
  items, under the owner standing rule of 2026-10-28 (given for
  Arms Race and extended to this task by the owner in the task
  instruction). Stamina running out is not by itself a stop reason
  while refills remain.
- Open the stamina resources you already hold, owner reminder
  2026-10-28 - "For Stamina, you have Stamina Resource you can
  open." The stamina resource items sitting in the inventory are
  a refill source to be OPENED and used whenever stamina binds,
  not a reserve to sit on - the event Store being sold out of
  stamina items (Limit 0, unit 014) does not make stamina
  exhausted. Before any unit concludes that stamina and every
  refill source are exhausted (the only ground for delaying the
  successor by 1 hour), it must check the inventory stamina
  items and record their count in the unit stats.
- Red lines hold without exception - never spend diamonds or
  money, never tap a price tag, a paid button, Renew, Finish Now
  or the Legendary Claim All, and never assemble or teleport.
  Anything needing those is recorded as skipped-needs-owner.
- Mechanics as played in round 1 - a nearby Invading Zombies
  target costs 10 stamina charged on the march, one squad
  wins outright at Lv.10 (Suggested Power 670,000 against
  this account's 25.05M Squad 1), the battle resolves on
  arrival and the squad returns on its own. Supply is per
  wave; a cleared area answers Search with not found until
  the next wave (about hourly). The medal the kills pay is
  the event Store currency - see the Store entry under What
  is known, including the coin chests that are the event's
  confirmed coin source.
- Server maintenance windows (2026-11-10 2340) - a maintenance
  shutdown is announced by a server banner about 7 minutes
  ahead (seen 23:14 in the 2319 donations unit) and, once it
  lands, the game shows "Server disconnected. Please restart
  the game." - click_element on Confirm does nothing, a
  coordinate tap at 501,545 exits the app (the restart itself,
  not a crash). Relaunch shows a SYSTEM ANNOUNCEMENT "Update
  complete, please restart the game." (Confirm 502,568 -
  click_element no-change, coordinate tap dismisses and the
  game restarts). Then "The server is under maintenance.
  Please wait a moment, we'll be back with you shortly."
  with Cancel / Confirm, plus "Login failed. Please retry or
  contact Support" at the bottom - one Confirm tap at 634,568
  retries the login and the game loads to the base screen.
  The maintenance came back on its own; no "active on a
  different device" dialog appeared. Do not treat the
  disconnect as a crash - recover through the dialog
  sequence and keep the unit going.

## What is known from 2026-10-28

- Owner word 2026-10-28 - the event's coins are collected from
  the task collection icon (tap to collect) - it shows as a
  gift box with a red dot carrying a number, the count of
  task rewards waiting (4 at the owner's 2026-10-28 reading),
  along the top of the map screen toward the left. No executor had tapped it before
  this instruction; collecting from it is now part of every
  zombie unit.
- First sight, round 1 - the event page timer read 2 days 16
  hours 10 minutes left, tagline - Eliminate the invading
  zombies; defend our city. The next-wave countdown read about
  52 minutes, so waves arrive on a cycle of about an hour and
  the supply of nearby zombies is replenished per wave.
- Alliance Finding lists Zombie Bosses found by allies - Lv.80
  and Lv.85 seen - with despawn timers of about 2.5 hours and
  distances of hundreds of kilometres. Those read as rally-class
  targets far from home, a different thing from the nearby
  Invading Zombies that Search finds.
- The first Search found a Lv.10 Invading Zombies target beside
  an alliance member base (another commander), about 64 km from
  the home base. Its card read - Suggested Power 670,000,
  stamina cost 10, despawn timer about 11 hours 52 minutes.
  Guaranteed Reward - event medal x10, a book item 1.3K, hero
  EXP 263.0K, iron 268.0K, food 268.0K. Potential Reward -
  green crate x1, green box x4, gold ticket x1. No coin line on
  the Lv.10 card - where the coins come from is still open (the
  higher targets, the boss targets, the potential crates or the
  Rewards track are the candidates).
- Attack flow - crossed swords, Squad 1 (25.05M power against
  670.00K, read Easy Win), March. Stamina is charged on march -
  138 to 128 for the first kill. The march took about a minute
  each way at 64 km, the battle resolved on arrival with a
  Victory banner, and the squad returned on its own.
- Coin baseline for round 1 - the coin panel read 34,417,273
  owned at 02:48, immediately before the first march.
- The app crashed once (02:52) on the tap back toward the base
  screen right after the first kill and relaunched cleanly with
  state intact - stamina and march results are server-side.
- Round 1 totals (record 0246-round-1-run) - four distinct
  Lv.10 targets destroyed between 02:49 and about 04:10 (one
  march jointly dispatched with queue unit 001, which shared
  the Mac from 03:34), 40 stamina spent on marches, 40 medals
  earned. Coin panel owned read 34,417,273 at 02:48 and
  34,416,573 at the last read - the direct coin yield of
  Lv.10 kills is zero, and the 700 step down is segment
  activity, not zombie play. The collection icon was not
  verifiably tapped in round 1, so its yield is unmeasured.
- The event Store (read in full in round 1) - the medal is
  the currency. Coin Chests are the confirmed coin source -
  Coin Chest (SR) pays 812.16K coins at Base Lv.30 by its
  tooltip (medal price CONFIRMED 160 by chain unit 005 on
  2026-10-28; Limit 100; 2 already owned in inventory,
  unopened - their inventory location is still to be pinned
  down, the Special tab's purple gold chest is a Tactical
  Master Supply Box and not this chest), Coin Chest (SSR)
  costs 480 medals (Limit 20, yield unread). Medal balance
  read 70 in unit 005, below the 160 a first SR redemption
  needs. Other prices in medals - 50
  Stamina item 10 (Limit 3), Universal Exclusive Weapon
  Shard 120 (Limit 10), Hero Recruitment Ticket 80 (Limit
  10), Survivor Recruitment Ticket 80 (Limit 30), iron crate
  160 (Limit 50), badge item x10 200 (Limit 50), gear
  component 200 (Limit 50), Lv.3 chest 360 (Limit 3), blue
  chest 120 (Limit 3), purple chest 400 (Limit 1), 5 minute
  speedup 4 (Limits 100 and 50), 1 hour speedup 36 (Limit
  10). Round 1 redeemed 3 of the 50 Stamina items for 30
  medals under the owner's stamina authorization for this
  task - the medal loop is stamina-positive (one kill earns
  the 10 medals a 50 stamina item costs). Medal spending
  beyond stamina (chests versus saving) follows the owner's
  maximize-coin objective and is the chain's call. The owner
  confirmed the maximize-coin execution on 2026-10-28 -
  redeem medals for Coin Chests and open the owned chests
  (see Coin chests under Cadence).
- Battle reports - the owner's 2026-10-26 mail holds
  victories over Lv.16 to Lv.20 Zombie Horde targets (the
  Lv.20 at X990 Y954 took three squads in sequence), so
  higher-level zombie targets exist in this event family.
  Lv.10 Invading Zombies kills generate no battle report
  mail, and the reports list casualties only, no rewards.
- An unexplained plus 10 stamina read followed one kill in
  two independent records (round 1 and queue unit 001) -
  a stamina drop from the kill or chunked regeneration.

- Parallel dispatch ACHIEVED by unit 010 on 2026-10-28 —
  two batched sequences put Squad 1 and Squad 2 on the
  march at the same time (March Queues 2 of 4 in one
  screenshot, one Returning under a Victory banner, the
  other still going out). The second batch inserted one
  extra tap before March — the deploy panel's squad-2
  tab at about 397,920 in window coordinates (the second
  of the four squad tabs along the bottom of the deploy
  panel). It worked because the wave's targets were
  adjacent piles (X982 Y934 and X984 Y933) — the second
  Search found a distinct target, not the taken one.
  Both rows claimed together for 536,000 coins.
- A march left in flight at a unit's end does NOT always
  leave a LOOT row — unit 007's closing march toward
  about X871 Y458 produced no row in unit 009's LOOT
  panel (which held only unit 009's own kill), and the
  coin baseline never moved. Handovers are therefore
  evidence to check, not a guaranteed deferred kill.
- The Events page bottom buttons (Search, Boss Search,
  back) sit lower than their scaled-screenshot centre
  suggests (measured by unit 012 on 2026-10-28) — taps at
  normalized y 899 land on the next-wave text line and do
  nothing; y about 925 dispatches. The March Queues bar
  itself was seen on the world map at top-left under the
  resource bar (unit 012 closing screenshot, 1 of 4 with a
  march out to X891 Y845), with no gift badge visible at
  its right end while that march was out.
- The Events tab bar SHIFTS between openings in the same
  pass (measured by unit 011 on 2026-10-28) — a batched
  tap at the Zombie Invasion tab's earlier position
  landed on the Level Swap event page instead (left
  untouched, its Confirm never tapped). Batched dispatch
  sequences must re-verify the tab by its title on sight
  before the Search tap, or the sequence silently goes
  to the wrong event page. Unit 011's two kills (X985
  Y963, X992 Y963) were therefore sequential, not
  parallel — compounded by march times of only about
  10 seconds on home-cluster targets.
- Chest naming CORRECTED by unit 014 on 2026-10-28 —
  the 160-medal, Limit 100 chest's BUY ITEMS dialog and
  its tooltip both name it Coin Chest (SSR); the
  812.16K coin yield belongs to this chest. The round 1
  and unit 005 label Coin Chest (SR) for the 160-medal
  chest was a misread. The 480-medal, Limit 20 chest's
  name is still unread (its button reads Go To when the
  balance is short). Unit 014 redeemed 1 SSR chest for
  160 medals (balance verified 190 in the Store, 30
  after); the tooltip then read Owned 3 — the 2
  pre-owned chests plus the new one, 2,436,480 coins in
  total waiting to be opened, location in inventory
  still unknown, and the Store tooltip Owned count is a
  reliable tracker until then. The Store 50-stamina
  item (10 medals) reads Limit 0 with a greyed Redeem —
  round 1's 3 redemptions exhausted an event-total
  limit; that refill source is closed for this event.
  Unit 014's dispatch was stamina-bound (13 stamina,
  one 10-cost march, 3 left), squads_parallel 1 for
  that stated reason.

- Parallel dispatch at the cap ACHIEVED by unit 013 on
  2026-10-28 — four batched sequences put all four squads
  on the march at once (March Queues 4 of 4; X883 Y811,
  X895 Y771, X895 Y759, X799 Y760; stamina 46 to 7). The
  march queue cap of 4 is the binding parallel limit.
- Auto squad selection, unit 024 on 2026-10-28 — with
  Squad 1 out on march, the deploy panel for a second
  Lv.10 target had already auto-selected Squad 2
  (20.92M, 2,175 of 2,175, Easy Win; Squad 1's tab
  carried a red X), so no squad-tab tap was needed
  before March. Check the panel's power and unit count
  before March rather than tapping a squad tab
  blindly. Unit 024 also re-confirmed the gift-box tap
  at 317,233 (an image-estimated 314,210 tap failed)
  and Claim All at 499,765; its two parallel kills
  (X945 Y864, X938 Y845) claimed 536,000 coins
  together, medals 130 to 150, stamina 58 to 41.
  The gift box on the world map March Queues bar sits at
  normalized 317,233 — taps at 266,253 opened the ally
  base behind the bar instead. Unit 012's X891 Y845
  handover march DID produce its LOOT row (claimed by
  unit 013 for 268,000), so a march left in flight can
  land either way; check the badge, never assume.

- March button effective point, unit 043 on
  2026-10-29 — taps at normalized 498,726 and
  500,735 produced no change; March at 500,755
  dispatched at once. The button's active area
  sits at its lower edge, below its visual
  centre — ground March low, near 755, not at
  the centre estimate.
- Keyboard Return quits the app, unit 043 on
  2026-10-29 — a Return keypress while the
  deploy panel was open quit LastWar outright
  (same class as the Esc crash); relaunch
  recovered with state intact. Never use Return
  (or Esc) on this app.
- Medal balance resolved, unit 043 on
  2026-10-29 — the Store header read live at
  2900 medals, confirming unit 042 and proving
  unit 041's derived 1220 wrong (stale base).
  The Coin Chest (SSR) row stands at 160
  medals, Limit 98, and its Redeem tap at the
  grounded point 742,293 again produced no
  change — three unresponsive Redeems in two
  units, no medals spent, redemption still
  deferred.
- Sequential dispatch when round trips are
  short, unit 043 on 2026-10-29 — with 10 to
  15 second marches, the first squad returned
  during the Events and Search navigation for
  the second dispatch, so the unit ran
  squads_parallel 1 despite an immediate
  parallel attempt. Short round trips, not the
  march cap of 4, were the binding limit.

- Parallel dispatch again, unit 047 on
  2026-10-29 — a batched swords plus March
  sequence can silently miss: its March tap
  left stamina unchanged at 61 and the queue
  at 0 of 4, so verify stamina or queue state
  after a batched March, never assume it. A
  verified deploy panel (Squad 1, Easy Win,
  30 second march) plus the grounded March
  point 502,750 dispatched cleanly, and a
  second batched dispatch 13 to 18 seconds
  later, inside the 30 second outbound
  window, achieved squads_parallel 2 with
  stamina 62 to 42 proving both marches.
  Three LOOT rows claimed in-unit for
  804,000 coins (X:951 Y:938, X:962 Y:942,
  X:990 Y:957, each 268.0K).
- Store medal balance live, unit 047 on
  2026-10-29 — the Store header read 3260
  medals. Derived medal totals carried across
  units are repeatedly wrong (unit 043 proved
  1220 wrong against a live 2900); only a
  Store header read counts as a medal balance.
- Coin Chest (UR) verified, unit 047 on
  2026-10-29 — the gold chest row, Limit 20,
  is Coin Chest (UR) by tooltip: Owned 25,
  yield 2.43M coins at Base Lv.30, price 480
  medals by row and by BUY ITEMS dialog
  (Unit Price 480, Total Price 480, quantity
  1), that is 5,062 coins per medal against
  the SSR chest's 5,076. The 480 chest's name
  and yield open question is now answered.
- Coin Chest (SSR) row missing, unit 047 on
  2026-10-29 — a full top-to-bottom scan of
  the Store list (17 rows) found no
  160-medal, Limit-98 Coin Chest (SSR) row
  of the kind unit 043 read that morning.
  The 160-medal purple-gold row in the first
  screen is Food Chest (SSR) by tooltip
  (Owned 925), not a coin chest, and must
  never be redeemed by mistake. The SSR row
  needs a re-check by the next unit.
- Redeem bottleneck refined, unit 047 on
  2026-10-29 — single taps on Redeem still
  do nothing, including a visually grounded
  centre tap at 741,287. A long-press
  (mouse down, 1 second hold, mouse up) on
  Redeem opened the BUY ITEMS dialog for the
  first time in this chain. The Buy
  confirmation inside the dialog did NOT
  register by single tap, long-press or
  double-click in background input: the
  dialog stayed open and the balance stayed
  3260 through all three tries. No medals
  were spent and no chest was redeemed.
  The next unit must try the Buy step with
  a different input route and must re-verify
  balance and Owned count before assuming
  any exchange happened.
- 50 stamina item still sold out, unit 047
  on 2026-10-29 — greyed Redeem, Limit 0,
  re-confirmed. Stamina closed at 43 with no
  stamina item opened; stamina never bound
  this unit (kills cost 30 total).

- Events tab bar shifts between openings, unit 048
  on 2026-10-29 — a batched second dispatch that
  assumed the earlier tab position landed on the
  Desert Storm Battlefield tab instead of Zombie
  Invasion (no Confirm or entry button tapped there,
  nothing spent). Recovered by clicking the
  partially visible Zombie tab at the bar's right
  edge and verifying the page title before Search.
  Batched dispatch sequences must re-verify the tab
  by title, as unit 011 already warned.
- Missing LOOT row for a completed march, unit 048
  on 2026-10-29 — Squad 2 marched to X:980 Y:844
  (verified 1/4, stamina charged) and was home
  (0/4) before the LOOT panel opened, yet the panel
  held only Squad 1's row (X:906 Y:936, 268.0K
  coins, claimed in-unit). This is the second
  handover-style loss after unit 009's: a completed
  march whose row never materialized. The successor
  unit must re-check the gift badge — a late row
  gets claimed then, otherwise it is lost.
- Store redemption deferred again, unit 048 on
  2026-10-29 — two sequential dispatches plus two
  full march round trips ran the unit past its cap,
  so the Store was not visited, no medal balance was
  re-measured live, and no derived medal total is
  reported. The SSR row re-check and the Buy-step
  retry from unit 047 stay open for the next unit.

- Grounded button points, unit 049 on 2026-10-29 —
  Search is at 358,941 (a tap at 901 hits the countdown
  text above the button and does nothing); the target
  card's crossed-swords button is at 499,753 (a tap at
  836 closes the card, as unit 008 also found); the
  deploy panel's March button is at 500,759; the
  squad-2 tab in the deploy panel is at 397,920.
  A batched sequence (Events, Search, crossed-swords,
  no screenshot read in between) opens the deploy
  panel where a single tap after a read closes the
  card.
- Short round trips again, unit 049 on 2026-10-29 —
  Squad 1 marched on an 8-second-class timer and had
  fully returned before the second batched dispatch
  landed, so squads_parallel was 1 despite an immediate
  parallel attempt, stamina 80 to 60 proving both
  marches. Both LOOT rows (X:982 Y:952, X:985 Y:963)
  claimed in-unit for 536,000 coins.
- Unit 048 missing row confirmed lost, unit 049 on
  2026-10-29 — the X:980 Y:844 row did not appear in
  unit 049's two-row LOOT panel, which held only
  unit 049's own two marches.
- Computer session drop, unit 049 on 2026-10-29 —
  session cc-347 closed mid-unit (observe returned
  observation_unavailable with no session open);
  session cc-351 was started, LastWar re-selected,
  and no game state was lost.
- Store redemption deferred again, unit 049 on
  2026-10-29 — the unit cap was reached at the loot
  claim, so the Store was not visited, no medal
  balance was re-measured live, and no derived medal
  total is reported (only plus 20 medals by row
  evidence). The SSR row re-check and the Buy-step
  retry from unit 047 stay open for the next unit.

- Parallel dispatch at the cap, unit 052 on
  2026-10-30 — four batched dispatches put all four
  squads on the march at once (March Queues 4/4;
  X:887 Y:926, X:877 Y:910, X:874 Y:915, X:892 Y:880;
  stamina 56 to 16 proving all four marches), the
  first cap-4 run in this chain. All four LOOT rows
  claimed in-unit for 1,072,000 coins (each 268.0K),
  coin HUD 122.5M to 123.6M.
- Store redemption breakthrough, unit 052 on
  2026-10-30 — the Store header read live at 3370
  medals. The 160-medal Coin Chest (SSR) row was
  found again after scrolling (Limit 98), answering
  unit 047's missing-row question: the row exists
  and its position shifts with scroll, so a
  first-screen scan alone misses it. Its tooltip
  read Owned 4, yield 812.16K coins. A 1-second
  long-press on Redeem did nothing this time, while
  a plain single click opened the BUY ITEMS dialog
  (SSR x1, Unit Price 160, Total Price 160) and a
  plain single click on Buy succeeded — the Buy-step
  bottleneck from unit 047 is broken in this
  session by plain single clicks, though input-route
  behaviour varies between sessions, so the next
  redemption must still verify balance and Owned
  count rather than assume success. Verified live:
  CONGRATULATIONS, balance 3370 to 3210, Limit 98
  to 97. Owned count after the redemption was not
  re-read in a tooltip, and the owned chests'
  inventory location is still unknown, so no chest
  was opened. A fresh wave arrived during the unit,
  so cleared is false.

- Batched dispatch too fast, unit 053 on
  2026-10-30 — a 3-click batch (Search,
  crossed-swords, March) dispatched in 1.5 seconds
  failed silently, stamina unchanged and March
  Queues 0/4: the later clicks landed before the
  Search jump animation produced the card. A batch
  needs a pause after Search, or single-step
  dispatch with a screen read between steps, as
  both kills in unit 053 used.
- Gift-box point moves with the map, unit 053 on
  2026-10-30 — taps at 317,233 and 312,225 opened
  ally another commander's base profile instead of LOOT,
  because the map was centred on that base and the
  base sat under the gift icon. After a map drag
  moved the base clear, a tap at 319,247 opened
  LOOT. Re-ground the gift point on the current
  screenshot whenever the map view has moved;
  never re-tap a stale point blindly.
- Computer session drop, unit 053 on
  2026-10-30 — session cc-421 dropped mid-unit
  (observe returned observation_unavailable);
  session cc-422 was started, LastWar re-selected,
  and no game state was lost.

- Cap-4 again, stamina refill, and Buy centre,
  unit 054 on 2026-10-30 — stamina 8 at entry, so
  one 50 Stamina item was opened before dispatch
  (Inventory Special live: 50-stamina x611,
  10-stamina x624; Inventory opens at 900,870,
  taps at 875,825 and 880,840 did not open it).
  A slow single-step dispatch lost its target to
  the stale-target toast ("The target location has
  changed", no stamina charged), while batched
  dispatches with a 2 second pause after Search
  succeeded four times at the cap (X:913 Y:944,
  X:894 Y:953, X:894 Y:934, X:862 Y:942, stamina
  59 to 19). A LOOT row is created on arrival, not
  on homecoming — the gift badge read 3 while two
  squads were still Returning and 4 after the
  fourth arrival, so rows can be claimed before
  squads return home. All four rows claimed
  in-unit for 1,072,000 coins. Store header read
  live at 3270 medals (again above a derived
  3250, so derived totals stay untrusted); one
  SSR Coin Chest redeemed (3270 to 3110, Limit
  97 to 96, CONGRATULATIONS verified). A Buy tap
  at 500,640 missed (button top edge) while the
  grounded Buy centre 499,689 succeeded — ground
  the Buy centre, never reuse 640. Session
  cc-423 dropped during a wait, cc-424 recovered
  with no state lost. A fresh wave arrived during
  the unit, so cleared is false.

- Search point corrected, Store button
  unresponsive, unit 057 on 2026-10-30 — taps
  at 358,941 hit the back arrow, not Search
  (back arrow grounds at 349,950; real Search
  is at 441,940 by OCR); both mis-taps jumped
  to the map with no target card, and the "The
  event has ended" toast on the map belongs to
  a Lv.10 Marshal's Guard notification, not to
  Zombie Invasion. Events icon grounds at
  683,150 (a tap at 645,153 opened Halloween
  Check-In instead). Two sequential Lv.10 kills
  (X:960 Y:950, X:910 Y:965, stamina 40 to 20),
  both LOOT rows claimed in-unit for 536,000
  coins, gift box grounded at 424,251 on that
  map view, Claim All at 499,765. Session
  cc-445 dropped during a wait, cc-446
  recovered with no state lost. Store button
  grounded twice at 618,222 and 625,220
  produced no change to background clicks, so
  the SSR redemption is deferred again; medals
  after the kills were not re-measured live
  and no derived balance is reported. The
  successor must try a different input route
  for the Store button. Cleared is false.

- Gift point moves with the map view, Store button
  still unresponsive, unit 058 on 2026-10-30 — taps
  at 319,247, 328,240, 340,250 and 340,257 only
  highlighted the March Queues bar; a single tap at
  428,240 opened LOOT at once (icon active area
  about 406 to 438 in x, 200 to 250 in y on this
  view). The gift badge read 1 yet the panel held
  3 rows, so the badge is not the row count here.
  Three Lv.10 kills (X:992 Y:943, X:993 Y:937,
  X:995 Y:932) claimed in-unit for 804,000 coins,
  HUD 135.2M to 136.0M, squads_parallel 1 (short
  round trips, plus a stamina refill before the
  third march). Stamina 5/120 at the third
  dispatch, one 50 Stamina item used (Owned 610
  to 609, 10 Stamina Owned 628 in the same panel),
  stamina 46 at close. Store button unresponsive
  to a single tap and a 1 second long-press at
  609,221, third unit in a row, so the SSR
  redemption and medal re-measurement stay open.

- Gift tap radius is small, base tap radius is
  large, unit 063 on 2026-10-30 — the gift icon
  sits immediately right of the March Queues bar
  with a red badge (2 for this unit's two kills),
  but three taps at its cropped positions
  (275,235, 420,275 and 335,278 on successive
  map views) each opened an ally base profile
  instead of LOOT, and a map drag from a target
  tile opened a Lv.75 Zombie Boss card (closed
  untouched, no attack, no rally). Re-ground the
  gift point on the current screenshot before
  tapping, and if a tap opens a base profile,
  reset with BASE and re-ground rather than
  dragging blindly. The two LOOT rows from unit
  063 stayed unclaimed at its close and are at
  risk of the handover-style loss.

- Chain close, unit 066 on 2026-10-30 — the Zombie
  Invasion event ended at about the 19:00 reset on
  2026-10-30: unit 064 read 05:08 left at 13:46 and
  unit 065 read 01:16 left at 17:42, and unit 066
  found the Events hub tab bar (Arms Race, Desert
  Storm Battlefield, Winter Battlefield, Level Swap,
  Wanted Boss, Community — six tabs) with no Zombie
  Invasion tab. No successor unit was enqueued; the
  chain zombie-2026-10-28 is closed. Do NOT seed a
  fresh zombie chain until a Zombie Invasion tab is
  seen live in the Events hub again. Re-confirmed
  2026-11-09 11:38 PT by scout-discovery unit 016
  (ticker-1134) - the tab bar still carries no Zombie
  Invasion tab, no chain seeded. Re-confirmed 2026-11-09 about 13:47 PT by the ticker-1345 arms-race unit - the tab bar showed Arms Race, Winter Battlefield and Desert Battlefield, still no Zombie Invasion tab, no chain seeded. (2026-11-10 1810 UPDATE, supersedes the absence as the newest read: the ticker-1806 gifts unit saw a Zombie Invasion tab live in the Events hub tab bar at about 18:11, beside Desert Battlefield and a partially visible "...f Oil" tab - after the ticker-1734 arms-race unit's close scan at about 17:56 the same day found no Zombie tab in the Events strip. The tab reappeared between the two reads, around the 18:00 rollover (inference, not a measured time). The event page itself is NOT yet verified - the sighting is a tab-bar read only - so the chain head zombie-2026-11-10-001 is seeded for the next unit to open the tab and verify the event page. Until that verification lands, the standing rule holds: no sowing, no zombie chain beyond the verification unit.) (2026-11-10 2008 UPDATE, supersedes the verification-owed state: the ticker-1952 unit verified the event page live - Zombie Invasion - Glacieradon - so the verification precondition is met; the chain is live and the 2026-10-28 owner rules apply again. See the 2008 section below.)

## Open questions

- What the collection icon pays per kill - partly answered
  2026-10-28 - two consecutive later-wave Lv.10 rows paid
  exactly 268,000 each while the 5 round 1 rows averaged
  214,400; what sets a row's coin line (wave, distance,
  target) is still open. (2026-11-10 2219 update: VERIFIED for this variant - the 2219 LOOT row was read before Claim All: medal x10, green crate x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K, and the HUD moved +0.3M on each resource. A later-wave Lv.10 row pays exactly 268,000 coins, third confirmation (units 006/007, 2008 HUD-inferred, 2219 row-read). What sets a row's coin line is still open; the Lv.28 Ironhead LOOT coin line is unmeasured.) (2026-11-10 2340 update: fourth confirmation - the 2340 LOOT row was read before Claim All: Lv.10 X:471 Y:355, medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K, HUD coin 109.9M to 110.2M. A later-wave Lv.10 row pays exactly 268,000 coins.) (2026-11-11 0030 update: fifth and sixth confirmations - the 0030 unit read two LOOT rows before Claim All (Lv.10 X:525 Y:356 and X:534 Y:376, each medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K) and claimed 536,000 coins in one Claim All; HUD coin 110.2M to 110.7M, food +0.5M, iron +0.6M, each displayed move consistent with 2 x 268,000.)
- The 480-medal, Limit 20 chest's name and yield -
  answered by unit 047 on 2026-10-29 - it is Coin
  Chest (UR), yield 2.43M coins at Base Lv.30.
- Why the 160-medal Coin Chest (SSR) row that unit
  043 read at Limit 98 on 2026-10-29 was absent from
  unit 047's full Store scan the same afternoon -
  answered by unit 052 on 2026-10-30: the row exists
  and its position shifts with scroll, so a
  first-screen scan alone misses it; it was found at
  Limit 98 (now 97 after unit 052's redemption).
- Where the 3 owned Coin Chest (SSR) sit in the inventory -
  not found in the Special tab or the first Resources pages
  in unit 005.
- Whether zombie levels rise above Lv.10 in later waves or
  days (Lv.16 to Lv.20 Zombie Hordes in the owner's
  2026-10-26 reports), and how stamina cost, medals and
  rewards scale with level. (2026-11-10 2219 update: YES in this variant - a Lv.28 Ironhead was sighted (not attacked): Suggested Power 2,396,500, stamina cost 10, despawn 19:35:38; Guaranteed Reward drone data 780, hero EXP 105.0K, iron obscured by the cursor; Potential Reward green crate x1, green box x4, gold ticket x1. How medals and rewards scale with level is unmeasured - the Lv.28 LOOT coin line is the next read.)
- Where the stamina Free Claim lives - not located in
  round 1.
- The plus 10 stamina read after a kill - drop or regen. (2026-11-10 2219 update: one more datapoint - stamina 44 at the march, 45 at the LOOT read, a regen tick; still open whether the plus-stamina read is a drop or regen.) (2026-11-10 2340 update: stamina 127 to 117, exactly the 10 cost, no plus-stamina read this unit.)
- Any daily attempt cap or diminishing returns (none seen).
- Failure conditions - what a loss costs, and whether stamina
  is refunded.
- What Boss Search does differently from Search (inspected
  in round 1 - rally-class targets, no coin line seen; no
  rally started).
- Glacieradon variant (2026-11-10 2008): the 0/40 counter's label is unread (likely boss clue progress); which Store rows are Coin Chests in this variant is NOT established; whether the gift-box claim is named Alliance Gifts by the game (toast wording) is an open read; Boss Search is untested in this variant. (2026-11-10 2219 update: the counter now reads 40/40 (was 0/40 in 2008) with 'Challenge begins in: 1d 19:46:34. Your Timezone: 2026-11-12 18:00' - the boss challenge opens 2026-11-12 18:00 local; the counter's label is still unread. Store Coin Chest rows in this variant are still NOT established - Store not visited in 2219, medal balance not re-read (unit 001's live read was 3950; this kill adds a card-stated medal x10, unverified as a balance). The 'Alliance Gifts received!' toast appeared again in 2219, this time immediately after the March tap and before any LOOT claim - cause still unknown, quoted verbatim. Boss Search still untested in this variant.) (2026-11-10 2340 update: event timer 2d 18:12:18 remaining, boss clue counter still 40/40, 'Challenge begins in: 1d 18:12:15. Your Timezone: 2026-11-12 18:00' re-confirmed; next wave arrives about 23:57. Store Coin Chest rows in this variant are still NOT established - Store not visited in 2340, medal balance not re-read (unit 001's live read was 3950; this kill adds a card-stated medal x10, unverified as a balance). Boss Search still untested in this variant.) (2026-11-11 0030 update: Store visited - medal balance 4000 read live in the Store header; unit 001 read 3950 before its kill, and five Lv.10 kills since (001, 2219, 2340, plus these two) at medal x10 each reconcile exactly to 4000, so +10 medals per Lv.10 kill is CONFIRMED across five kills. The 120-medal row is 'Universal Exclusive Weapon Shard', Owned 417 - it is NOT a Coin Chest, correcting unit 001's appearance-based 'gold chest' label. The 50 Stamina x1 10-medal row (Limit 3) is available in this variant, NOT sold out (unlike the October event). No Coin Chest row is established in this variant yet: the 160-medal crate row and the below-fold rows are still unidentified, and no redemption was made. Event page re-read: timer 2d 17:26:24, boss clue 40/40, challenge opens 2026-11-12 18:00, next wave in 00:20:58 at the read (current wave arrived about 23:57). Boss Search still untested in this variant.)

## What the 2026-11-10 1810 sighting added - Zombie Invasion tab seen live again, event page verification owed

- Sighting, not a zombie unit: the ticker-1806 gifts unit (gifts-2026-11-10-1430, about 18:10 to 18:16 local) entered the Events hub and read the tab bar live: a Zombie Invasion tab beside Desert Battlefield and a partially visible "...f Oil" tab. Evidence in `_records_/2026-11-10/alliance-gifts/1810-queue-run.md` (commit 20a62ff0 on records/2026-11-10). No zombie unit was executed in this pass.
- Newest-read rule: this sighting supersedes the absence reads as the newest verified record - the 2026-11-09 absence re-confirmations (scout 1152, arms-race 1345) and the ticker-1734 arms-race unit's close scan at about 17:56 the same day, which found no Zombie Invasion tab in the Events strip. The tab reappeared between 17:56 and 18:11, around the 18:00 rollover (inference: the duel-day / Weekly Pass reset lands about 18:00 per Issue #242; the reappearance time itself was not measured).
- What is verified: the TAB is back in the Events hub tab bar. What is NOT verified: the event page itself (Store, Ranking, Rewards, Search, wave countdown), whether zombies are nearby, and whether the event runs on the old rules. The chain head zombie-2026-11-10-001 was seeded this pass for the next unit to open the tab and verify the event page. (2026-11-10 1834 update: the chain head was restored to the live pool; the verification unit is next - see the 1834 section below.)
- Standing rule, unchanged until that verification lands: do NOT seed a fresh zombie chain beyond the verification unit, and do NOT sow (the 2026-10-30 ban - no sowing until the page reappears - is satisfied only by a verified event page, not by a tab-bar sighting). If the next unit confirms the page live, the chain reopens under the 2026-10-28 owner rules (no daily limit, no hour budget, pause 1 hour only when no zombies are nearby) and this profile records the return as a new round.
- Result stats: no zombie unit ran; nothing claimed, nothing spent, verified yes for the tab sighting only (same-unit live read), blocker_category none.

## What the 2026-11-10 1834 ticker pass added - chain head restored to the live pool, event-page verification still owed

- Queue-state change, not a zombie unit: the ticker-1834 batch (commit af56d36ec on records/2026-11-10) restored chain head zombie-2026-11-10-001 to the live pool after the 18:11 live tab sighting - the unit had stranded on the branch inbox only. Evidence in the commit's queue-file move and `_records_/2026-11-10/INDEX.md`.
- Standing rule, unchanged: the next tick verifies the event page; do NOT seed a fresh chain beyond the verification unit, and do NOT sow until the event page itself is verified live. The tab sighting alone does not lift the ban. (2026-11-10 2008 update: the verification has now landed - see the 2008 section below; the ban is lifted and the chain is live.)

## What the 2026-11-10 2008 ticker-1952 run added - Glacieradon event page VERIFIED live, 1 Lv.10 kill, LOOT claimed

- Event page VERIFIED live, unit zombie-invasion-zombie-2026-11-10-001 by ticker-1952, about 19:52 to 20:08 local, status partial - the chain head's purpose is met and one Lv.10 kill was made with its LOOT claimed, but the unit ran to its time cap mid-chain with the wave still live, so the chain continues and a successor is enqueued to start now. Evidence in `_records_/2026-11-10/zombie-invasion/2008-queue-run.md` (commit d29bc658c on records/2026-11-10). Computer sessions cc-501 and cc-502 on the owner Mac mini, LastWar already open on the base screen. No "active on a different device" dialog appeared.
- NEW VARIANT, supersedes the October "event ended" claim: the event page title reads "Zombie Invasion - Glacieradon". This is a DIFFERENT event from the October one (which ended 2026-10-30, unit 066): this variant is boss-clue oriented. The October mechanics that still hold: Search finds Lv.10 Invading Zombies, Suggested Power 670,000, stamina cost 10, same Guaranteed Reward line.
- Page layout, read live: at entry the page showed a pre-wave countdown 00:06:15 with "Zombies are coming." and a Rewards row (gold bar x10, medal x500, crates x50, x50). Store, Rewards and Record buttons present. At 20:01, after the countdown expired, the page changed to the live-wave layout: event timer 2d 21:58:23 remaining (event runs about 3 days, ends about 2026-11-13), "Zombies are invading! Protect our City! Challenge the fearsome Beast Glacieradon!", Store / Ranking / Rewards buttons, tabs Alliance Finding / My Findings, text "No Zombie Boss found yet. Killing Invading Zombies on world map might reveal their clues.", a 0/40 counter (label unread - likely boss clue progress), and "The next wave of Invading Zombies will arrive in 00:31:08." Buttons: Search, Boss Search, Record. Entry: Events icon at 934,135 opened the Events hub; the tab bar showed a Zombie Invasion tab live (red badge), confirming the ticker-1806 18:11 sighting.
- Entry state, read live: food 631.4M, iron 954.2M, coin 97.8M (HUD-rounded), gold 13.22K, stamina 120, Total Power 148,787,578, March Queues 0/4. The gift badge at the right end of the March Queues bar read 5 at entry. The app reported "exited or restarted" once on a back-arrow tap (no input dispatched) and was found intact on the same page on re-observe. Session cc-502 started after a 4 minute wait for the wave countdown.
- The kill: Search at 379,946 (this page's Search button, bottom centre-left) jumped to the world map with a Lv.10 Invading Zombies card: Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000; stamina cost 10; despawn timer 11:57:53. Target beside [AP3x]Lost Boys / [AP3x]Tigers bases, home cluster. Crossed-swords button at 496,736 opened the deploy panel: Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win, march 00:00:06, stamina 120 with -10 shown. March at 499,755 dispatched at once. Stamina 120 to 110, March Queues 1/4, Victory banner on screen, squad Returning 00:00:04, then 0/4. squads_parallel 1: only one dispatch was attempted in this unit (time cap, single target chased); the parallel-dispatch rule was NOT exercised. The successor should run parallel dispatches while the wave lasts (batched sequences, pause after Search). No second Search was attempted: the unit cap was reached at the LOOT claim.
- Store, Glacieradon variant, read live: Store header medal balance 3950. No redemption made, no chest opened. Store rows seen (first screen): gold chest x1 for 120 medals Limit 10; gold bar x1 for 80 medals Limit 10; gold bar x1 for 80 medals Limit 30; 50 Stamina x1 for 10 medals Limit 3 (in the October event this item was sold out at Limit 0); crate x1 for 160 medals Limit 50; more rows below the fold, unscrolled. Which rows are Coin Chests in THIS event is NOT established - the successor must scroll the Store, read the chest rows by tooltip, and re-read the medal balance before any redemption. Do NOT redeem on October prices: the October Store list (Coin Chest (SSR) 160, Coin Chest (UR) 480) is the old variant's list, not this one's. (2026-11-11 0030 CORRECTION: the 120-medal 'gold chest' row is Universal Exclusive Weapon Shard, Owned 417 - NOT a Coin Chest. The appearance-based label is superseded; see the 0030 section.)
- Rewards panel is a reference table, not a claimable track: zombie boss rewards by Level Range 5-75, 80-100, 105-135 ("The discoverer and the team leader may possibly earn the following rewards upon defeating the zombie boss"), including medals, stamina 10, drone data, EXP, iron, food, coins and chests. Nothing claimed there.
- LOOT claim: gift badge read 5 at entry, 6 after the kill (one new row from this kill). The gift box grounds at the right end of the March Queues bar and MOVES with the map view: a tap at 268,229 did nothing; re-grounded on the current screenshot at 304,226 it opened the LOOT panel at once. The LOOT panel was NOT read before Claim All (unit cap): its rows' coin lines are unread, so the exact coins collected are NOT verified. Claim All at 499,765 tapped once; toast "Alliance Gifts received!" and the panel closed. HUD deltas across the claim, read live: coin 97.8M to 98.1M, food 631.4M to 631.7M, iron 954.2M to 954.4M. The +0.3M displayed coin move is consistent with one October-style Lv.10 row (268,000), but the exact row value is unverified and the badge count (5 pre-existing) leaves open whether older rows were also claimed - the HUD move covers about one row's worth, not six. The toast wording ("Alliance Gifts") is quoted verbatim; whether the gift-box claim is named Alliance Gifts by the game is an open read for the successor.
- Medal balance after the kill was NOT re-read live: the card states medal x10 per kill, but no Store re-read was made, so medals_after is not verified. No stamina item was opened (stamina 110 at close, no refill needed).
- Standing rule, updated: the verification precondition is met - event page verified live 2026-11-10 about 19:52 to 20:08; chain zombie-2026-11-10 is live, successor enqueued; the 2026-10-28 owner rules apply again (no daily limit, no hour budget, pause 1 hour only when no zombies are nearby). The October "event ended" claim is superseded for this variant. The variant is boss-clue oriented (0/40 counter, Boss Search untested) and the wave cadence read about 31 minutes between waves (next wave 00:31:08 at 20:01; the next wave arrives about 20:32, zombies remain on the map, cleared is false).
- Result stats: zombies_killed 1 (verified: Victory banner, stamina 120 to 110, March Queues 1/4 to 0/4). coins_collected about 0.3M by HUD delta, exact value unverified. medals_before 3950 live, medals_after not re-read. chests_opened 0. squads_parallel 1 (single dispatch only).
- Follow-up for the successor (from the record): scroll the Store and identify this event's Coin Chest rows by tooltip before any redemption; re-read the medal balance; run parallel dispatches (batched sequences, pause after Search); read the LOOT rows before Claim All; check Boss Search and the 0/40 clue counter; note the "Alliance Gifts received!" toast wording. (2026-11-10 2219 update: Store scroll, medal re-read and parallel dispatch still owed - 2219 attempted parallel dispatch and missed on two mistaps, Store not visited, medal balance not re-read; the LOOT row WAS read before Claim All this time (coin 268,000 verified); the 0/40 counter is now 40/40 with the challenge opening 2026-11-12 18:00. Successor 003 carries the owed items.)

## What the 2026-11-10 2219 ticker-2154 run added - Glacieradon chain 002, 1 Lv.10 kill, LOOT 268,000 coins claimed

- Unit zombie-invasion-zombie-2026-11-10-002 by ticker-2154, chain zombie-2026-11-10 seq 2, about 22:12 to 22:19 local, status partial - the pass budget ended mid-chain with the wave still live, so the chain continues. Evidence in `_records_/2026-11-10/zombie-invasion/2219-queue-run.md` (commit b11294e7f on records/2026-11-10). Session cc-516.
- Entry state: Zombie Invasion - Glacieradon page verified live again, event timer 2d 19:46:33, "Zombies are invading! Protect our City! Challenge the fearsome Beast Glacieradon!", Store / Ranking / Rewards buttons, Alliance Finding / My Findings tabs. Boss clue counter now reads 40/40 (was 0/40 in unit 001): "Challenge begins in: 1d 19:46:34. Your Timezone: 2026-11-12 18:00" - the boss challenge opens 2026-11-12 18:00 local. Alliance Finding lists Lv.85 and Lv.80 Zombie Bosses at 395km, 423km, 405km, 573km, despawn timers about 02:17-02:40. Next wave of Invading Zombies arrives in 00:39:19 at entry (about 22:54) - the current wave is part-spent but targets remain. HUD at entry (world map read): food 644.3M, iron 967.4M, coin 105.9M (HUD-rounded), gold 13.22K. Stamina 54 at the deploy panel. March Queues 0/4.
- The kill: Search at 382,936 (fresh-grounded on the event page screenshot) found a Lv.10 Invading Zombies target: Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000; stamina cost 10; despawn 11:38:27. Crossed-swords at 496,736 opened the deploy panel: Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win, march 00:01:01, stamina 54 with -10 shown. March at 500,760 dispatched at once. Stamina 54 to 44, March Queues 1/4, target X:516 Y:394, ETA 00:00:34. Squad 1 was Returning 00:00:46 on the next read and home (0/4) by the LOOT claim.
- Unexplained toast: "Alliance Gifts received!" appeared in the observation immediately after the March tap, before any LOOT claim in this unit (the row was still unclaimed then). Quoted verbatim; cause unknown - possibly a delayed toast. The LOOT row itself was verified unclaimed until this unit claimed it below. See the updated Glacieradon open question.
- Parallel dispatch not achieved: squads_parallel 1. While Squad 1 was out, a second dispatch was attempted on a nearby Lv.10 pile, but the tap at 498,505 opened a Teleport/Profession tile menu instead (the map view had shifted under the aim point), and the follow-up tap at 450,350 opened a Lv.28 Ironhead card instead of dismissing the menu. No second march was dispatched, and Squad 1's round trip was about 80 seconds, so the parallel window closed before a re-grounded second attempt could land. Short round trips plus the two mistaps, not the march cap of 4, were the binding limit. Re-ground every map tap on the current screenshot; the map is dense with tappable tiles here. See the updated parallel-dispatch entry.
- Lv.28 Ironhead sighted (not attacked): Suggested Power 2,396,500, stamina cost 10, despawn 19:35:38; Guaranteed Reward drone data 780, hero EXP 105.0K, iron (value obscured by the cursor); Potential Reward green crate x1, green box x4, gold ticket x1. Higher-level zombies exist in this event variant; their LOOT coin line is still unmeasured. See the updated levels open question.
- LOOT claim: gift badge read 1 at the right end of the March Queues bar after Squad 1's return; the gift box re-grounded fresh on the current screenshot at 288,216 opened the LOOT panel at once. One row, read before claiming: Lv.10 Invading Zombies X:516 Y:394, medal x10, green crate x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K. Claim All (plain blue, no price tag) at 498,765 tapped once; panel closed. Coin HUD 105.9M to 106.1M, food 644.3M to 644.6M, iron 967.4M to 967.7M - each +0.3M displayed move consistent with the single 268,000 row (HUD rounds to 0.1M). Gift badge gone after the claim. This is the first row-read (not HUD-inferred) coin verification in this variant - see the updated coin-per-kill open question.
- Stamina 44 at the march, 45 at the LOOT read (regen tick) - one more plus-stamina read for the open question in the activity metadata. Store not visited in this unit (pass budget): the medal balance was not re-read live and no Coin Chest redemption was attempted. Unit 001's live Store read was 3950 medals; this unit's kill adds a card-stated medal x10, unverified as a balance. The Store coin-chest identification from unit 001's follow-up stays open for the successor.
- Result stats: zombies_killed 1 (verified: Victory implied by Returning march, stamina 54 to 44, March Queues 1/4 to 0/4, LOOT row X:516 Y:394 claimed). cleared false: the wave is live, more Lv.10 piles visible on the map, next wave arrives about 22:54. coin_before 105.9M HUD, coin_after 106.1M HUD, coins_collected 268,000 (row read before Claim All). medals_before not re-read, medals_after not re-read. chests_opened 0. squads_parallel 1. Target: kill wave zombies and claim LOOT; achieved: 1 Lv.10 kill and its LOOT row claimed. Verified yes (same-unit live reads: row coin line, HUD deltas, stamina, queue state). Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule, cleared false). It should run parallel dispatches with freshly grounded map taps, visit the Store to identify this event's Coin Chest rows by tooltip and re-read the medal balance, and check the Lv.28 Ironhead LOOT coin line if it dispatches on one.

## What the 2026-11-10 2340 ticker-2334 run added - Glacieradon chain 003, maintenance recovery, 1 Lv.10 kill, LOOT 268,000 coins claimed

- Unit zombie-invasion-zombie-2026-11-10-003 by ticker-2334, chain zombie-2026-11-10 seq 3, about 23:40 to 23:53 local, status partial - the wave is still live and the chain continues. Evidence in `_records_/2026-11-10/zombie-invasion/2340-queue-run.md` (commit 5c07e8d40 on records/2026-11-10). Computer sessions cc-521 and cc-524 on the owner Mac mini; cc-521 dropped once mid-unit (wait returned no active session), cc-524 was started and the game state was intact on recovery - no game input was replayed.
- Server maintenance ate the first half of the unit: at entry LastWar showed "Server disconnected. Please restart the game." with a Confirm button - click_element on Confirm produced no change, a coordinate tap at 501,545 exited the app (the restart itself, not a crash). Relaunch showed a SYSTEM ANNOUNCEMENT "Update complete, please restart the game." with Confirm at 502,568 - click_element no-change, a coordinate tap dismissed the dialog and the game restarted. After the restart a second dialog: "The server is under maintenance. Please wait a moment, we'll be back with you shortly." with Cancel / Confirm, plus "Login failed. Please retry or contact Support" at the bottom - one Confirm tap at 634,568 retried the login and the game loaded to the base screen. This matches the 2319 donations record, which saw a server banner warning of a maintenance shutdown in 7 minutes at its entry - the maintenance was announced and the game came back on its own. No "active on a different device" dialog appeared at any point. See the new maintenance entry under Scope and availability.
- Entry state, read live about 23:47: food 655.4M, iron 978.5M, coin 109.9M (HUD-rounded), gold 13.22K, stamina 127. Total Power 149,218,973.
- Event page re-verified live: Events icon at 927,131 opened the Events hub; the tab bar read The Age of Oil (red 1 badge), Arms Race, Desert Battlefield and a partially visible "Zon..." tab at the right edge - tapping it at 860,131 opened the Zombie Invasion - Glacieradon page. Page read live: event timer 2d 18:12:18 remaining, "Zombies are invading! Protect our City! Challenge the fearsome Beast Glacieradon!", Store / Ranking / Rewards buttons, Alliance Finding / My Findings tabs, boss clue counter 40/40 with "Challenge begins in: 1d 18:12:15. Your Timezone: 2026-11-12 18:00". Alliance Finding lists Lv.80 and Lv.85 Zombie Bosses at 546km, 487km, 486km, 506km. "The next wave of Invading Zombies will arrive in 00:06:50" at the read (about 23:57).
- The kill: Search at 379,936 found a Lv.10 Invading Zombies target: Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000; stamina cost 10; despawn 11:04:34. Crossed-swords at 496,736 opened the deploy panel: Squad 1, Unit Count 2,231/2,231, Easy Win, march 00:01:38. March at 500,755 dispatched at once. Stamina 127 to 117, March Queues 1/4, squad Returning 00:00:57 on the next read and home by the LOOT claim.
- Parallel dispatch not achieved: squads_parallel 1 - only one dispatch was attempted in this unit. The maintenance recovery consumed the first half of the unit window, leaving no time for a parallel second dispatch - the binding limit was the remaining unit time, not the march cap of 4. The successor should run parallel dispatches while the wave lasts. See the updated parallel-dispatch entry.
- LOOT claim: gift badge read 1 at the right end of the March Queues bar after the squad's return; the gift box re-grounded fresh on the current screenshot at 308,237 opened the LOOT panel. One row, read before claiming: Lv.10 Invading Zombies X:471 Y:355, medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K. Claim All (plain blue, no price tag) at 499,765 tapped once; panel closed. Coin HUD 109.9M to 110.2M, food 655.4M to 655.7M, iron 978.5M to 978.7M - each displayed move consistent with the single 268,000 row (HUD rounds to 0.1M). Gift badge gone after the claim. March Queues 0/4. This is the fourth row-read coin verification in this variant - see the updated coin-per-kill open question.
- Stamina 117 at close, no refill needed. Store not visited in this unit (unit time): the medal balance was not re-read live and no Coin Chest redemption was attempted. The Store coin-chest identification from unit 001's follow-up stays open for the successor.
- Result stats: zombies_killed 1 (verified: Victory implied by Returning march, stamina 127 to 117, March Queues 1/4 to 0/4, LOOT row X:471 Y:355 claimed). cleared false: the wave is live, next wave arrives about 23:57, more targets may appear. coin_before 109.9M HUD, coin_after 110.2M HUD, coins_collected 268,000 (row read before Claim All). medals_before not re-read, medals_after not re-read. chests_opened 0. squads_parallel 1. Target: kill wave zombies and claim LOOT; achieved: 1 Lv.10 kill and its LOOT row claimed. Verified yes (same-unit live reads: row coin line, HUD deltas, stamina, queue state). Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule, cleared false). It should run parallel dispatches with freshly grounded map taps, visit the Store to identify this event's Coin Chest rows by tooltip and re-read the medal balance, and check the next wave's targets after 23:57. (2026-11-11 0030 update: Store visited, medal balance re-read 4000, 120-medal row identified as Universal Exclusive Weapon Shard - see the 0030 section; the 160-medal crate row and below-fold rows still unidentified, and the parallel dispatch owed here was achieved in 0030.)

## What the 2026-11-11 0030 ticker-0004 run added - Glacieradon chain 004, first parallel dispatch, 2 Lv.10 kills, LOOT 536,000 coins claimed

- Unit zombie-invasion-zombie-2026-11-10-004 by ticker-0004, chain zombie-2026-11-10 seq 4, about 00:30 to 00:42 local, status partial - the wave is still live and the chain continues. Evidence in `_records_/2026-11-11/zombie-invasion/0030-queue-run.md` (commit 9ba46aa1 on records/2026-11-11). Computer sessions cc-525 and cc-526 on the owner Mac mini; cc-525 dropped mid-unit (observe returned observation_unavailable with no session open), cc-526 was started, LastWar re-selected, and no game state was lost. No "active on a different device" dialog appeared.
- Entry state: the game was on the ALLIANCE TECHS panel at unit start (the donations unit left it there): closed the tech panel and the tree, back arrow to the base screen. Base HUD at entry: food 655.7M, iron 978.7M, coin 110.2M (HUD-rounded), badge 13.22K, gold 6,287, stamina 120, Total Power 149,218,973.
- Event page re-verified live: Events icon at 935,138 opened the Events hub on the Zombie Invasion - Glacieradon page (the hub remembered the tab). Page read live: event timer 2d 17:26:24 remaining, "Zombies are invading! Protect our City! Challenge the fearsome Beast Glacieradon!", Store / Ranking / Rewards buttons, Alliance Finding / My Findings tabs, boss clue counter 40/40 with "Challenge begins in: 1d 17:26:25. Your Timezone: 2026-11-12 18:00". Alliance Finding lists Lv.80 and Lv.85 Zombie Bosses at 546km, 487km, 486km, 506km. "The next wave of Invading Zombies will arrive in 00:20:58" at the read - the current wave (arrived about 23:57) is live. A system ticker read "...ed 1000 from Zombie Boss Loot!" at the top during the first Search - quoted verbatim; a ticker line, not this account's gain, and not claimed as one.
- Kill 1: Search at 379,946 found a Lv.10 Invading Zombies target: Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000; stamina cost 10; despawn 11:20:17. The first crossed-swords tap failed with stale_observation (the target app's process identity was unavailable, input NOT dispatched, side effect none); the window was re-selected, the card re-observed still open, and the tap re-sent - no input was replayed. Crossed-swords at 496,736 opened the deploy panel: Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win, march 00:01:37, stamina 120 with -10 shown. March at 500,755 dispatched at once. Stamina 120 to 110, March Queues 1/4, Go X:534 Y:376 00:01:20.
- Kill 2 - parallel dispatch, FIRST in this variant: while Squad 1 was out, Events (935,138) back to the Glacieradon page and Search at 379,946 found a second Lv.10 target with the same card values. Crossed-swords at 496,736 opened the deploy panel with Squad 2 auto-selected (Unit Count 2,175/2,175, Easy Win - no squad-tab tap needed, per unit 024). March at 500,755 dispatched at once. Stamina 110 to 100, March Queues 2/4, Go X:525 Y:356 00:01:54. squads_parallel 2 - the first parallel run in the Glacieradon chain (units 001-003 all ran 1). The binding limit was the short round trips, not the march cap of 4; the second dispatch landed inside Squad 1's outbound window. See the updated parallel-dispatch entry.
- LOOT claim: gift badge read 2 at the right end of the March Queues bar after both arrivals; the gift box re-grounded fresh on the current screenshot at 322,226 opened the LOOT panel at once. Two rows, read before claiming: Lv.10 Invading Zombies X:525 Y:356, medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K; Lv.10 Invading Zombies X:534 Y:376, same values. Each row pays exactly 268,000 coins, the fifth and sixth row-read confirmations for this variant. Claim All (plain blue, no price tag) at 499,765 tapped once; toast "Alliance Gifts received!" and the panel closed. Coin HUD 110.2M to 110.7M, food 655.7M to 656.2M, iron 978.7M to 979.3M - each displayed move consistent with 2 x 268,000 (HUD rounds to 0.1M). Gift badge gone after the claim. Squad 2 was still Returning 00:00:17 at the claim - rows are claimable before homecoming, per unit 054.
- Store - medal balance and chest-row identification: Store opened from the event page at 846,210 on the first try. Medal balance read live in the header: 4000. Unit 001 read 3950 before its kill; five Lv.10 kills since (001, 2219, 2340, plus these two) at medal x10 each reconcile exactly to 4000 - the +10 medals per Lv.10 kill is confirmed across five kills. First-screen rows: gold chest x1 120 medals Limit 10; gold bar x1 80 medals Limit 10; gold bar x1 80 medals Limit 30; 50 Stamina x1 10 medals Limit 3 (available - NOT sold out in this variant, unlike the October event); crate x1 160 medals Limit 50; one more row below the fold, unscrolled. Tooltip on the 120-medal row (icon tap at 230,300): the row is "Universal Exclusive Weapon Shard", Owned 417 - it is NOT a Coin Chest, correcting unit 001's appearance-based "gold chest" label. No Coin Chest row is established in this variant yet: the 160-medal crate row and the below-fold rows are still unidentified, and no redemption was made. The Store X tap to close left no change (tooltip still up); the game was left on the Store screen - harmless state for the successor.
- Stamina 100 at close, no refill needed. No stamina item was opened and the inventory stamina count was not read (stamina never bound this unit).
- Result stats: zombies_killed 2 (verified: stamina 120 to 110 to 100, March Queues 0/4 to 1/4 to 2/4 to 0/4, two LOOT rows X:534 Y:376 and X:525 Y:356 claimed). cleared false: the wave is live, next wave arrives in about 00:13:47 at the Store read, more targets may appear. coin_before 110.2M HUD, coin_after 110.7M HUD, coins_collected 536,000 (two rows read before Claim All). medals_before not re-read live at unit start, medals_after 4000 (Store header read live after the kills). chests_opened 0. squads_parallel 2 (see above). Target: kill wave zombies and claim LOOT; achieved: 2 Lv.10 kills in parallel and both LOOT rows claimed. Verified yes (same-unit live reads: row coin lines, HUD deltas, stamina, queue state, Store header). Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule, cleared false). It should run parallel dispatches while the wave lasts, finish identifying the Store chest rows (the 160-medal crate tooltip and the below-fold rows) and, once a Coin Chest row is established, redeem per the maximize-coin rule, and check the Lv.28 Ironhead LOOT coin line if it dispatches on one.
