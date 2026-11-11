---
title: Zombie Invasion
created: 2026-10-28T09:47:00Z
modified: 2026-11-11T02:32:17Z
level: L1
version: 1.23.0
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
  March. Squad 2's deploy panel (unit 006) - 20.92M
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
  Invasion tab, no chain seeded. Re-confirmed 2026-11-09 about 13:47 PT by the ticker-1345 arms-race unit - the tab bar showed Arms Race, Winter Battlefield and Desert Battlefield, still no Zombie Invasion tab, no chain seeded. (2026-11-10 1810 UPDATE, supersedes the absence as the newest read: the ticker-1806 gifts unit saw a Zombie Invasion tab live in the Events hub tab bar at about 18:11, beside Desert Battlefield and a partially visible "...f Oil" tab - after the ticker-1734 arms-race unit's close scan at about 17:56 the same day found no Zombie tab in the Events strip. The tab reappeared between the two reads, around the 18:00 rollover (inference, not a measured time). The event page itself is NOT yet verified - the sighting is a tab-bar read only - so the chain head zombie-2026-11-10-001 is seeded for the next unit to open the tab and verify the event page. Until that verification lands, the standing rule holds: no sowing, no zombie chain beyond the verification unit.)

## Open questions

- What the collection icon pays per kill - partly answered
  2026-10-28 - two consecutive later-wave Lv.10 rows paid
  exactly 268,000 each while the 5 round 1 rows averaged
  214,400; what sets a row's coin line (wave, distance,
  target) is still open.
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
  rewards scale with level.
- Where the stamina Free Claim lives - not located in
  round 1.
- The plus 10 stamina read after a kill - drop or regen.
- Any daily attempt cap or diminishing returns (none seen).
- Failure conditions - what a loss costs, and whether stamina
  is refunded.
- What Boss Search does differently from Search (inspected
  in round 1 - rally-class targets, no coin line seen; no
  rally started).

## What the 2026-11-10 1810 sighting added - Zombie Invasion tab seen live again, event page verification owed

- Sighting, not a zombie unit: the ticker-1806 gifts unit (gifts-2026-11-10-1430, about 18:10 to 18:16 local) entered the Events hub and read the tab bar live: a Zombie Invasion tab beside Desert Battlefield and a partially visible "...f Oil" tab. Evidence in `_records_/2026-11-10/alliance-gifts/1810-queue-run.md` (commit 20a62ff0 on records/2026-11-10). No zombie unit was executed in this pass.
- Newest-read rule: this sighting supersedes the absence reads as the newest verified record - the 2026-11-09 absence re-confirmations (scout 1152, arms-race 1345) and the ticker-1734 arms-race unit's close scan at about 17:56 the same day, which found no Zombie Invasion tab in the Events strip. The tab reappeared between 17:56 and 18:11, around the 18:00 rollover (inference: the duel-day / Weekly Pass reset lands about 18:00 per Issue #242; the reappearance time itself was not measured).
- What is verified: the TAB is back in the Events hub tab bar. What is NOT verified: the event page itself (Store, Ranking, Rewards, Search, wave countdown), whether zombies are nearby, and whether the event runs on the old rules. The chain head zombie-2026-11-10-001 was seeded this pass for the next unit to open the tab and verify the event page.
- Standing rule, unchanged until that verification lands: do NOT seed a fresh zombie chain beyond the verification unit, and do NOT sow (the 2026-10-30 ban - no sowing until the page reappears - is satisfied only by a verified event page, not by a tab-bar sighting). If the next unit confirms the page live, the chain reopens under the 2026-10-28 owner rules (no daily limit, no hour budget, pause 1 hour only when no zombies are nearby) and this profile records the return as a new round.
- Result stats: no zombie unit ran; nothing claimed, nothing spent, verified yes for the tab sighting only (same-unit live read), blocker_category none.
