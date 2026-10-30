---
title: Zombie invasion queue run
created: 2026-10-30T15:45:00Z
modified: 2026-10-30T15:45:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-060 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 08:34 to 08:45 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-060, executor
ticker-0834, chain zombie-2026-10-28 seq 60, computer
sessions cc-466 and cc-467 (cc-466 dropped during a
50 second wait, cc-467 recovered with no state lost,
as in earlier units).
Status partial: two kills and the in-unit loot claim
are complete, but the Store redemption step was not
executed (Redeem unresponsive, see below), so the
work continues in successor unit 061. No tracker
change is made for a partial unit.

## Entry state

- The game was found on the Secret Command Post
  Hidden Treasure screen in windowed mode (642 by
  951). The first back-arrow tap at 95,885 did
  nothing; the grounded back arrow at 160,948
  returned to the base screen. Windowed mode kept
  throughout, and clicks responded throughout.
- Coin HUD at base entry 142.5M (gold coin icon,
  third resource). Food 286.3M, iron 472.6M.
  No "active on a different device" dialog appeared.
- Zombie Invasion Events page verified by title:
  event timer 10:21:54, next wave in 00:03:25.
  The Events tab bar needed a rightward drag to
  reveal the Zombie Invasion tab (492,131).

## Two Lv.10 kills in parallel, loot claimed in-unit

- Dispatch method: single-step with a screen read
  between steps for kill 1, then an immediate
  second dispatch while squad 1 was still out.
  Grounded windowed points used: Events icon
  935,160; Search 376,940; crossed-swords 501,753;
  March 499,774 (grounded by visual grounding;
  the button's active area sits low).
- Kill 1: Lv.10 Invading Zombies, X:998 Y:913,
  Squad 1 (25.05M vs 670,000, Easy Win, Unit Count
  2,231 of 2,231), stamina 93 to 83, March Queues
  1 of 4, 41 km, 00:00:37 timer.
- Kill 2: Lv.10, X:990 Y:909, Squad 2 auto-selected
  (Unit Count 2,175 of 2,175, Easy Win), stamina 83
  to 73, March Queues 2 of 4 - parallel dispatch
  ACHIEVED, the first unit in this chain to record
  squads_parallel 2 since unit 047 (units 043, 049,
  058 and 059 all recorded 1 for short round trips).
  At the 2 of 4 screenshot squad 1 was already
  Returning (00:00:38) while squad 2 was outbound
  (00:00:41).
- After a 50 second wait both squads were home
  (March Queues 0 of 4) and the gift badge read 2.
  Gift box at 304,258 on that map view opened
  LOOT at once. The panel held exactly the two
  rows: X:990 Y:909 and X:998 Y:913, each coin
  268.0K, iron 268.0K, food 268.0K, medal 10,
  EXP 263.0K.
- Both rows claimed in-unit via the plain blue
  Claim All at 499,765 (no price tag). Total
  coins_collected 536,000. Coin HUD moved 142.5M
  to 143.0M, food 286.3M to 286.8M, iron 472.6M
  to 473.2M, each consistent with 2 x 268K.
- squads_parallel 2. Stamina 93 to 73, 20 spent,
  no refill needed, no stamina item opened.

## Store redemption deferred - Redeem bottleneck again

- Store opened at once in windowed mode at
  823,178 (the windowed-vs-fullscreen difference
  from unit 059 holds). Store header read live at
  4010 medals. No medal balance is derived: the
  4010 figure stands well above unit 059's close
  of 3440 plus this unit's 20 earned medals, and
  derived totals have repeatedly proved wrong, so
  the gap is recorded, not explained.
- After one scroll the 160-medal row was found at
  Limit 94, matching unit 059's close (95 to 94).
  Its item tooltip read Coin Chest (SSR), yield
  812.16K coins at Base Lv.30 - the verified coin
  chest, not the Food Chest (SSR). The tooltip's
  Owned line read 28, against unit 059's Owned 7
  reading; that discrepancy is unresolved and is
  recorded here, not reconciled by derivation.
  Redemption verification below therefore rests
  on balance and Limit, not on Owned.
- Redeem for the Limit 94 row tried three input
  routes, all with no change: a plain single tap
  at 740,335, a 1 second long-press at the same
  point, and a double-click at 740,333. Balance
  stayed 4010 and Limit stayed 94 through all
  three, so no medals were spent and no chest was
  redeemed. This is the same Redeem bottleneck
  seen in units 043 and 047; the next unit must
  try a different input route and must re-verify
  balance and Limit before assuming any exchange.
- No Coin Chest was opened in this unit; the owned
  chests' inventory location is still unknown.

## Close

- Cleared is false: both Searches found a target
  at once, and a fresh wave arrived during the
  unit (next-wave countdown 00:58:34 at Store
  time, 00:57:18 at close, after 00:03:25 at
  entry). Successor unit 061 is enqueued to start
  now in the same chain.
- No diamonds or money spent, no price tag tapped
  except the medal-denominated Redeem attempts
  above (no purchase completed, no medals spent),
  no speedup burned, no assembly or teleport.
