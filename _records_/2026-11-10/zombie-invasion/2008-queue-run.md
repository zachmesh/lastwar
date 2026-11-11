---
title: Zombie invasion queue run
created: 2026-11-11T04:09:00Z
modified: 2026-11-11T04:09:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-11-10-001 execution
status: partial
---

# Zombie invasion - 2026-11-10 about 19:52 to 20:08 PST queue run

Unit: zombie-invasion-zombie-2026-11-10-001, executor
ticker-1952, chain zombie-2026-11-10 seq 1, computer
sessions cc-501 and cc-502. Status partial - the chain
head's purpose is met (the event page is VERIFIED live
for the new event variant) and one Lv.10 kill was made
with its LOOT claimed, but the unit ran to its time cap
mid-chain with the wave still live, so the chain
continues. Successor enqueued to start now.

## Entry state

- LastWar already open on the base screen. HUD at unit
  entry, read live: food 631.4M, iron 954.2M, coin
  97.8M (HUD-rounded), gold 13.22K, stamina 120,
  Total Power 148,787,578. March Queues 0/4. The gift
  badge at the right end of the March Queues bar read
  5 at entry (unexplained pre-existing rows - see
  LOOT note below).
- No "active on a different device" dialog appeared.
- Computer session cc-501 started 19:52; the app
  reported "exited or restarted" once on a back-arrow
  tap (no input dispatched) and was found intact on
  the same page on re-observe. Session cc-502 started
  after a 4 minute wait for the wave countdown.

## Event page VERIFIED - new variant Zombie Invasion - Glacieradon

- Events icon at 934,135 opened the Events hub. The
  tab bar showed a Zombie Invasion tab live (red badge),
  confirming the ticker-1806 18:11 sighting.
- The event page title reads "Zombie Invasion -
  Glacieradon". At entry the page showed a pre-wave
  countdown 00:06:15 with "Zombies are coming." and
  Rewards row (gold bar x10, medal x500, crates x50,
  x50). Store, Rewards and Record buttons present.
- At 20:01, after the countdown expired, the page
  changed to the live-wave layout: event timer
  2d 21:58:23 remaining (event runs about 3 days),
  "Zombies are invading! Protect our City! Challenge
  the fearsome Beast Glacieradon!", Store / Ranking /
  Rewards buttons, tabs Alliance Finding / My
  Findings, text "No Zombie Boss found yet. Killing
  Invading Zombies on world map might reveal their
  clues.", a 0/40 counter (label unread - likely boss
  clue progress), and "The next wave of Invading
  Zombies will arrive in 00:31:08." Buttons: Search,
  Boss Search, Record.
- This is a DIFFERENT event from the October one: the
  October event ended 2026-10-30 (unit 066) and this
  Glacieradon variant is boss-clue oriented. The
  October mechanics that still hold: Search finds
  Lv.10 Invading Zombies, Suggested Power 670,000,
  stamina cost 10, same Guaranteed Reward line.
- The activity metadata still says "do NOT seed until
  a tab is seen live" and describes the ended October
  event; it is tier-2 and left for the knowledge flow
  to update with this variant (page layout, boss
  clues, 0/40 counter, wave cadence about 31 minutes
  between waves as read, event timer about 3 days).

## Store read live

- Store header read live at entry to the Store:
  medal balance 3950. No redemption made, no chest
  opened. Store rows seen (first screen): gold chest
  x1 for 120 medals Limit 10; gold bar x1 for 80
  medals Limit 10; gold bar x1 for 80 medals Limit
  30; 50 Stamina x1 for 10 medals Limit 3 (in the
  October event this item was sold out at Limit 0);
  crate x1 for 160 medals Limit 50; more rows below
  the fold, unscrolled. Which rows are Coin Chests in
  THIS event is NOT established - the successor must
  scroll the Store, read the chest rows by tooltip,
  and re-read the medal balance before any redemption.
- Rewards panel is a reference table, not a claimable
  track: zombie boss rewards by Level Range 5-75,
  80-100, 105-135 ("The discoverer and the team
  leader may possibly earn the following rewards upon
  defeating the zombie boss"), including medals,
  stamina 10, drone data, EXP, iron, food, coins and
  chests. Nothing claimed there.

## The kill

- Search at 379,946 (this page's Search button, bottom
  centre-left) jumped to the world map with a Lv.10
  Invading Zombies card: Guaranteed Reward medal x10,
  drone data 1.3K, hero EXP 263.0K, iron 268.0K, food
  268.0K; Potential Reward green crate x1, green box
  x4, gold ticket x1; Suggested Power 670,000;
  stamina cost 10; despawn timer 11:57:53. Target
  beside [AP3x]Lost Boys / [AP3x]Tigers bases, home
  cluster.
- Crossed-swords button at 496,736 opened the deploy
  panel: Squad 1, five Lv.150 heroes, Unit Count
  2,231/2,231, 25.20M vs 670.00K, Easy Win, march
  00:00:06, stamina 120 with -10 shown.
- March at 499,755 dispatched at once. Stamina
  120 to 110, March Queues 1/4, Victory banner on
  screen, squad Returning 00:00:04, then 0/4.
  squads_parallel 1: only one dispatch was attempted
  in this unit (time cap, single target chased); the
  parallel-dispatch rule was not exercised. The
  successor should run parallel dispatches while the
  wave lasts.
- No second Search was attempted: the unit cap was
  reached at the LOOT claim.

## LOOT claim

- Gift badge read 5 at entry, 6 after the kill (one
  new row from this kill). The gift box grounds at
  the right end of the March Queues bar and MOVES
  with the map view: a tap at 268,229 did nothing;
  re-grounded on the current screenshot at 304,226
  it opened the LOOT panel at once.
- The LOOT panel was NOT read before Claim All (unit
  cap): its rows' coin lines are unread, so the
  exact coins collected are NOT verified. Claim All
  at 499,765 tapped once; toast "Alliance Gifts
  received!" and the panel closed.
- HUD deltas across the claim, read live: coin
  97.8M to 98.1M, food 631.4M to 631.7M, iron
  954.2M to 954.4M. The +0.3M displayed coin move is
  consistent with one October-style Lv.10 row
  (268,000), but the exact row value is unverified
  and the badge count (5 pre-existing) leaves open
  whether older rows were also claimed - the HUD
  move covers about one row's worth, not six. The
  toast wording ("Alliance Gifts") is quoted verbatim;
  whether the gift-box claim is named Alliance Gifts
  by the game is an open read for the successor.
- Medal balance after the kill was NOT re-read live:
  the card states medal x10 per kill, but no Store
  re-read was made, so medals_after is not verified.
  No stamina item was opened (stamina 110 at close,
  no refill needed).

## Result

- zombies_killed 1 (verified: Victory banner,
  stamina 120 to 110, March Queues 1/4 to 0/4).
- cleared false: the wave is live, the next wave
  arrives about 20:32, zombies remain on the map.
- coin_before 97.8M HUD, coin_after 98.1M HUD,
  coins_collected about 0.3M by HUD delta, exact
  value unverified.
- medals_before 3950 live, medals_after not re-read.
- chests_opened 0. squads_parallel 1 (single
  dispatch only).
- Follow-up for the successor: scroll the Store and
  identify this event's Coin Chest rows by tooltip
  before any redemption; re-read the medal balance;
  run parallel dispatches (batched sequences, pause
  after Search); read the LOOT rows before Claim All;
  check Boss Search and the 0/40 clue counter; note
  the "Alliance Gifts received!" toast wording.
