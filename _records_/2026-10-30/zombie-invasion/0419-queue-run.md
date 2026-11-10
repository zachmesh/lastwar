---
title: Zombie invasion queue run
created: 2026-10-30T11:19:00Z
modified: 2026-10-30T11:19:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-056 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 04:04 to 04:19 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-056, executor
ticker-0404, chain zombie-2026-10-28 seq 56, computer
session cc-441. Status partial: the 15 minute unit cap
ran out during the Store redemption step. The kills and
the in-unit loot claim are complete; the redemption is
not, and no tracker change is made, so the next tick
re-produces the work as a fresh unit.

## Windowed-mode failure, fullscreen fix

- The game was found with the Zombie Invasion Store
  panel still open from unit 055, medals 3510 on the
  Store header, exactly unit 055's close.
- In the windowed 642x951 window, Search, Boss Search
  and the back arrow at the bottom bar did not respond
  to four coordinate clicks, while a mid-screen click
  (My Findings tab) and the Store close X did. The
  control channel reported background_window mode.
- Clicking the window zoom button (element 4) put the
  game into native fullscreen (1920x1080, screenshots
  downsampled to 1280x720). In fullscreen, Search,
  Events, March, the LOOT gift icon and Store all
  responded to image-fraction coordinates. The game
  is left in fullscreen with the Store panel open;
  the successor should keep working in fullscreen
  coordinates rather than reopening windowed, unless
  it deliberately exits fullscreen via View menu.
- Two intermittent keyboard_focus_unavailable blocks
  ("user is working in another window of this app",
  frontmost app Macky) were cleared by re-activating
  LastWar and retrying; no input was lost to them.

## Two Lv.10 kills, sequential, loot claimed in-unit

- Events page verified by title Zombie Invasion on
  opening (event timer 14:54:12 left, next wave in
  about 00:35 at entry). Coin HUD 134.1M at entry.
- First kill - Search found a Lv.10 Invading Zombies
  card (Guaranteed medal x10, EXP 263.0K, iron
  268.0K, food 268.0K, stamina cost 10). Crossed
  swords opened the deploy panel (Squad 1, 25.05M
  Vs 670.00K, Easy Win, Unit Count 2,231 of 2,231,
  march 00:00:09, stamina 54 in the bottom bar).
  March dispatched at once. Verified: March Queues
  1/4, Returning 00:00:01, stamina 54 to 44.
- Parallel attempt - Events was reopened at once and
  Search found a second Lv.10 card, but by the time
  its deploy panel opened it again showed Squad 1
  (25.05M, Easy Win, march 00:00:26), so the first
  squad was already home. squads_parallel is
  therefore 1, sequential, as in units 049, 053 and
  055: the round trips are only seconds long, so a
  second dispatch via Events and Search cannot land
  while the first squad is still out. No march-queue
  cap was hit (cap remains 4, measured by unit 007).
- Second kill - March dispatched from that panel.
  Verified: March Queues 1/4, Go X:964 Y:952,
  stamina 44 to 34 after the march.
- LOOT claim - after the second return (March
  Queues 0/4) the gift-box badge read 2. The grounded
  tap at 438,213 in fullscreen coordinates opened the
  LOOT panel with exactly this unit's 2 rows, each
  coin 268.0K, medal x10, iron 268.0K, food
  268.0K, hero EXP 263.0K: X:964 Y:952 and
  X:998 Y:958. Claim All (plain blue, no price tag)
  at 485,764 tapped in-unit; panel closed, badge
  cleared, 536,000 coins collected by row lines.
  Claim verification - HUD after the claim: coin
  134.6M (from 134.1M), food 271.9M (from 271.3M),
  iron 463.9M (from 463.4M), consistent with plus
  536,000 at HUD rounding. No exact coin-panel
  reading was taken, so no exact coin_before or
  coin_after is reported.

## Store redemption - NOT completed, Redeem bottleneck

- Store header read live at 3530 medals after the
  claims (prior close 3510, plus 20 from this unit's
  2 kills). No derived medal total is reported
  beyond that live reading.
- The SSR Coin Chest row was identified after a
  drag-scroll: gold coin-chest icon, 160 medals,
  Limit 95, exactly unit 055's post-redemption
  state. Its tooltip was not obtained (a tap on the
  chest icon produced no tooltip), but the row
  identity matches the prior unit's SSR row on all
  three visible fields.
- Five Redeem attempts on that row produced no BUY
  ITEMS dialog and no medal change: two coordinate
  taps at 609,410, one click_element on the Redeem
  text (which opened a Courage Medal tooltip,
  Owned 3.5K, instead of a dialog), one tap at
  576,397 which only closed that tooltip, and one
  final tap at 609,410 after the tooltip closed.
  Medals stayed 3530, Limit stayed 95. No diamonds
  and no money were spent, and no other Store row
  was redeemed.
- This is a further instance of the Redeem bottleneck
  recorded in units 054, 055 and in the alignment
  notes: a different tap approach was tried
  (click_element) and still did not open the dialog.
  The successor should try yet another approach
  (for example a fresh Store reopen, or a tap on a
  different point of the Redeem button) and must
  re-verify medal balance and Limit before assuming
  an exchange happened. The redemption remains open.
- Accidental Ranking open - one Store-aimed tap at
  613,229 landed on Ranking instead and opened the
  Zombie Boss Damage Ranking panel. It was closed
  untouched (X at the grounded 616,145, after two
  lower X taps missed); our row read Damage 0, no
  boss, rally or other task type was touched.

## Outcome

Partial (unit cap reached mid-redemption): 2 kills at
squads_parallel 1 (sequential, short round trips),
loot 536,000 coins claimed in-unit, 0 chests
redeemed, 0 chests opened (owned chests still not
located in inventory, as in units 048, 049, 052, 053,
054 and 055). Nearby zombies not cleared - Search
found targets twice in this wave and the next-wave
countdown read about 00:28 at the Store close, so
cleared is false and the successor starts now.
Stamina 34 at close; stamina inventory was not
re-checked because stamina never bound (34 left, no
refill needed), so no 1 hour delay applies.
