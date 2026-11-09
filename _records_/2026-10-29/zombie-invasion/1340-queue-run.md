---
title: Zombie Invasion Execution 2026-10-29 1340 Queue Run
created: 2026-10-29T21:09:00Z
unit: zombie-invasion-zombie-2026-10-28-047
executor: ticker-1334
status: partial
---

# Zombie Invasion - execution, 2026-10-29 1340 queue unit 047

A single task unit, executed by executor ticker-1334 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-047,
chain zombie-2026-10-28, chain sequence 47, priority 4.
Session window about 13:40 to 14:09 America/Los_Angeles.
Status - partial; the unit ran past the 15 minute cap because
the Store redemption investigation ran long, and the chain
continues while the event is available and zombies remain
nearby, so the tracker is left untouched. All three kills
dispatched in this unit were resolved and claimed inside it,
and the march queue was empty at the close.

## What was observed

- Open - the game was on the base screen, no
  different-device dialog at any point. Computer sessions
  cc-295, cc-304 and cc-306 were used in turn; the session
  dropped twice mid-unit (after a 60 second wait and again
  during the Store check) and was restarted each time with
  state intact. No login or verification was demanded.
- Coin HUD - 106.2M at this unit's start, 107.0M after the
  LOOT claim, consistent with the 804,000 claimed.
- Stamina - 69 at the base-screen sighting, 71 at the first
  deploy panel, 61 after kill 1, 62 at the third deploy
  panel, 42 after kills 2 and 3 marched, 43 at the close.
  No stamina item was opened; stamina never bound.
- Event timer - 1d 05:19:31 left at the Zombie page
  sighting. The next-wave countdown hit 00:00:53, then
  reset to 01:00:00 as a fresh wave arrived mid-unit.
- Kill 1 - batched Events, Search, crossed-swords at
  500,735 and March at 500,750 dispatched first try after
  the wave refresh. Lv.10 Invading Zombies, Suggested
  Power 670,000, stamina cost 10, Squad 1 25.05M Easy
  Win, Unit Count 2,231 of 2,231, march time 00:00:03.
  The first Search tap before the refresh did nothing
  visible; the second, after the refresh, jumped to the
  target card at once.
- Kill 2, first attempt failed - the batched
  swords at 500,735 plus March at 500,750 sequence after
  the second Search left stamina unchanged at 61 and the
  march queue at 0 of 4 with only one LOOT row, so the
  March tap in that batch missed and no march was
  charged. A batched March tap is not self-verifying.
- Kill 2, second attempt succeeded - a fresh Search
  found a third Lv.10 target (despawn 11:52:53); the
  deploy panel was verified on sight (Squad 1, Easy
  Win, march time 00:00:30, stamina 62) and the
  grounded March point 502,750 dispatched it.
- Kill 3, parallel - while kill 2's 30 second march
  was still out, a batched Events, tab, Search,
  swords, March sequence dispatched a fourth Lv.10
  target about 13 to 18 seconds after kill 2's March,
  inside kill 2's outbound window. Stamina 62 to 42
  proves two marches were charged. squads_parallel
  is 2, the first parallel result above 1 since unit
  013's four-squad run; the binding limit here was
  the 30 second march window, not the queue cap of 4.
- Claim - after a 60 second wait the march queue read
  0 of 4 and the gift badge read 3. The gift tap at
  317,233 opened the LOOT panel with exactly three
  rows, all Lv.10 Invading Zombies, each reading coin
  268.0K and medal x10 - X:951 Y:938, X:962 Y:942
  and X:990 Y:957. Claim All at 499,765, blue button
  with no price tag, claimed all three rows in-unit
  for 804,000 coins and 30 medals. The badge cleared
  and the coin HUD moved 106.2M to 107.0M.
- Store, medal balance live - the Store header read
  3260 medals. Only this figure is live-measured;
  every derived medal total carried across units
  (including this unit's 3230 start figure, 3260
  minus the 30 earned here) is a derivation, not a
  measurement, and must be labelled as such.
- Store, Coin Chest (UR) verified - the gold chest
  row, Limit 20, is Coin Chest (UR) by tooltip:
  Owned 25, yield 2.43M coins at Base Lv.30, price
  480 medals by the row and by the BUY ITEMS dialog
  (Unit Price 480, Total Price 480, quantity 1).
  That is 5,062 coins per medal, essentially tied
  with the SSR chest's 5,076. This resolves the open
  question of what the 480 chest is and pays.
- Store, Coin Chest (SSR) row not found - a full
  top-to-bottom scan of the Store list (17 rows)
  found no 160-medal, Limit-98 Coin Chest (SSR)
  row of the kind unit 043 read this morning. The
  160-medal purple-gold row in the first screen is
  Food Chest (SSR) by tooltip (Owned 925), not a
  coin chest, and must not be redeemed by mistake.
  The SSR row's absence is recorded as an open
  question for the next unit to re-check; no medal
  was spent on any wrong row.
- Store, Redeem bottleneck refined - single taps on
  Redeem still do nothing (this unit's grounded
  centre tap at 741,287 included). A long-press
  (mouse down, 1 second hold, mouse up) on Redeem
  opened the BUY ITEMS dialog for the first time in
  this chain, so the dialog step is reachable. The
  Buy confirmation inside the dialog did NOT
  register by single tap, long-press or double-click
  in background input: the dialog stayed open and
  the balance stayed 3260 through all three tries.
  No medals were spent, no chest was redeemed, and
  the redemption stays deferred. The next unit
  should try the Buy step with a different input
  route and must re-verify balance and Owned count
  before assuming any exchange happened.
- Store, other rows re-confirmed - the 50 stamina
  item reads greyed Redeem, Limit 0 (sold out).
  The event still has over a day left.
- Cleared - false. Search found targets on demand
  in a live wave, and the event still has over a
  day left. Successor unit 048 enqueued to start now.
- Red lines - no diamonds or money spent, no price
  tag or paid button tapped (the BUY ITEMS dialog's
  Buy button is medal-denominated and was not
  completed), no speedup burned, no assembly, no
  teleport, no player attacked outside the standing
  rules.

## Result statistics

- zombies_killed: 3
- cleared: false
- coin_before: 106.2M HUD rounded
- coin_after: 107.0M HUD rounded
- coins_collected: 804000
- medals_before: 3230 derived
- medals_after: 3260 store-measured
- chests_opened: 0
- chests_redeemed: 0
- squads_parallel: 2
- tasks_badge: 3
- stamina_end: 43
