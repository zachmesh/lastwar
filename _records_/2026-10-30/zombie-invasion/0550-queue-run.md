---
title: Zombie invasion queue run
created: 2026-10-30T12:50:00Z
modified: 2026-10-30T12:50:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-059 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 05:40 to 05:50 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-059, executor
ticker-0534, chain zombie-2026-10-28 seq 59, computer
sessions cc-449 and cc-450 (cc-449 dropped, cc-450
recovered with no state lost, as in earlier units).
Status partial: three kills and one SSR redemption are
complete, but the chain is not exhausted, so the work
continues in successor unit 060. No tracker change is
made for a partial unit.

## Entry state

- The game was left on the base screen in windowed mode
  (642 by 951) by the trucks unit in the same pass.
  Coin HUD 136.0M at entry. No "active on a different
  device" dialog appeared.
- Windowed mode matters in this pass: in the trucks
  unit, fullscreen clicks reached nothing until View
  then Exit Full Screen restored windowed clicks.
  This zombie unit ran entirely windowed, and its
  clicks responded throughout.

## Three Lv.10 kills, sequential, loot claimed in-unit

- Dispatch method: single-step with a screen read
  between steps (Search, crossed-swords, March), not
  a blind batch. Grounded windowed points used:
  Events icon 935,140; Search 376,948; crossed-swords
  496,763 then 498,754 (re-grounded on the new card);
  March 478,767. A first attempt at the third kill
  missed the swords button and closed the card with
  no march and no stamina charged; the retry with a
  freshly grounded swords point dispatched cleanly.
- Kill 1: Lv.10, X:994 Y:954, row coin 268.0K,
  iron 268.0K, food 268.0K, medal 10.
- Kill 2: Lv.10, X:984 Y:949, row coin 268.0K,
  same resource lines, medal 10.
- Kill 3: Lv.10, X:994 Y:974, row coin 268.0K,
  same resource lines, medal 10. Its LOOT row was
  claimed while the squad was still Returning, per
  the unit 054 lesson that a row is created on
  arrival, not on homecoming.
- All three rows claimed in-unit via Claim All at
  499,765, gift box at 288,263 on the map view
  (March Queues bar right end, windowed). Total
  coins_collected 804,000. Coin HUD moved 136.0M
  to 136.8M (food 273.2M to 274.0M, iron 465.3M
  to 466.1M, consistent with 3 x 268K per resource).
- squads_parallel is 1, for the same reason as
  units 043 and 049: round trips of seconds (the
  first squad was Returning within seconds and home
  before the next dispatch landed), not the march
  cap of 4. Each next dispatch was attempted
  immediately after the previous claim.
- Stamina: 3 marches cost 30 total (10 each). No
  Regain Stamina panel appeared and no stamina item
  was opened, so stamina never bound this unit and
  no inventory stamina count was needed for a
  delay decision. Stamina totals at entry and close
  were not read live, so none is reported here.

## Store redemption breakthrough

- Store button on the Zombie Invasion Events page
  opened at once in windowed mode at 823,178. This
  is the first successful Store opening after three
  units in a row (056, 057, 058) with an
  unresponsive Store button in fullscreen. The
  fullscreen-vs-windowed difference, already seen
  with the Events back arrow in the trucks unit
  of this pass, is the likely explanation: in
  fullscreen, background clicks did not reach the
  game; in windowed mode they did. Successors
  should keep the game windowed for Store work.
- Store header read live at 3600 medals before
  redemption (entry medals before the kills were
  not read live, so no entry balance is reported
  and none is derived from the 3600 figure).
- The 160-medal row was found after one scroll:
  its item tooltip read Coin Chest (SSR), Owned 7,
  yield 812.16K coins at Base Lv.30. This is the
  verified coin chest, not the Food Chest (SSR)
  that unit 047 warned about.
- Redeem: a plain single tap on Redeem at 740,305
  did nothing; a 1-second long-press opened the
  BUY ITEMS dialog (Coin Chest (SSR) x1, Unit
  Price 160, Total Price 160). Buy at the grounded
  centre 497,691 succeeded at once.
  Verified live: CONGRATULATIONS banner, balance
  3600 to 3440 (exactly minus 160), Limit 95 to 94.
  Owned count after the redemption was not re-read
  in a tooltip, so no post-redemption Owned total
  is reported here.
- No Coin Chest was opened in this unit; the owned
  chests' inventory location is still unknown, so
  the 812.16K per chest remains pending, now for
  the 7 pre-owned plus this 1 redeemed chest by
  count evidence only for the pre-owned figure.

## Close

- Cleared is false: the third Search found a target
  at once, the next-wave countdown read about
  00:54 at Store time, and the event timer read
  about 13:09 at close. Successor unit 060 is
  enqueued to start now in the same chain.
- No diamonds or money spent, no price tag tapped
  except the medal-denominated Redeem/Buy above
  (authorized maximize-coin conversion, no money),
  no speedup burned, no assembly or teleport.
