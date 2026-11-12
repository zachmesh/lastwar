# Zombie Invasion — queue run 1834 (unit 018, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-018`, chain `zombie-2026-11-10` seq 18
- Executor: ticker-1822; token acquired 18:22 PT, released 18:36 PT; claimed about 18:22 PT; finished about 18:34 PT
- Session: cc-654; Last War window 676414 (windowed 642x951, not fullscreen); no drop, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, third kill claimed at close

## Event state (Glacieradon variant, read live)

- Event timer 1d 23:33:36 at about 18:26; "Challenge begins in: 23:33:37"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:28:13 at the 18:26 read (about 18:54 local), 00:26:15 at the 18:30 re-read
- Alliance Finding: Lv.80 Zombie Boss 342km, Lv.80 138km, Lv.80 294km, Lv.85 208km
- 40/40 bar on the event page (unchanged from unit 015)

## Entry state (base HUD, read live)

- Food 693.3M, iron 1.0G, coin **136.7M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **88**

## Dispatches — 3 Lv.10 kills, sequential

- Kill 1 — Squad 1 → X:502 Y:406. Events (942,115) → tab verified Zombie Invasion → Search (361,946) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:27:40. Crossed-swords grounded fresh at (490,736); deploy panel read Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231, march 00:00:35. March (500,760) dispatched; stamina 88 → 78, March Queues 1/4.
- Kill 2 — Squad 1 again → X:497 Y:396. By the time the second dispatch sequence landed, Squad 1 had already returned (deploy panel showed Squad 1, 25.20M, full unit count — not the auto-selected Squad 2 of unit 024), so the two squads were never out at once. March 00:00:43; stamina 78 → 68, March Queues 1/4.
- Kill 3 — Squad 1 → X:505 Y:394. Third Search found a target at once (despawn 11:22:28). Deploy panel Squad 1, Easy Win, march 00:00:51. March (500,760) dispatched; stamina 69 → 59 (68 + 1 regen before the march), March Queues 1/4, squad Returning 00:00:34 at the close read.

## Parallelism — squads_parallel 1, short round trips again

- The parallel attempt was real (second dispatch started immediately after the first March), but each round trip is only about 35–51 seconds outbound plus a short return, and the navigation plus screenshot reads between dispatches take minutes — Squad 1 was home before Squad 2's deploy panel opened. Same binding limit as units 043 and 049, not the march cap of 4 (never reached). A batched no-read dispatch sequence would be the only way to overlap squads on this wave, and unit 015 showed batching fails when the hub is still settling.

## Claims — 3 LOOT rows × 268,000 coins = 804,000

- Rows: X:502 Y:406, X:497 Y:396 (claimed together), X:505 Y:394 (claimed separately after its arrival).
- Gift-box icon at the right end of the March Queues bar, grounded fresh at (311,226) on this map view — badge read 2, then 1, and opened LOOT at once both times (no base under the icon on this view). Claim All at (499,780) is plain blue, no price tag; panel closed on the tap.
- Coin HUD verified: **136.7M → 137.2M** after the first two rows, **137.2M → 137.5M** after the third (+0.3M displayed, 268,000 by the row); food 693.3M → 693.8M → 694.1M (+268,000 per row). Gift badge gone after claiming.
- Medals: before 5070 (unit 017's live Store read, carried); after 5100 **derived** (+10 per kill), not live-read — Store not visited, flagged here, not a closing count.

## Store

- Not visited this unit (unit cap reached at the third claim). No medal balance re-read, no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up.
- Stamina 59 at close (88 − 30 spent + 1 regen); no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- First Events tap at (942,100) opened nothing but a Ghost Ops banner; the icon centre on this windowed view is (942,115) — ground it per view, never reuse the fullscreen y.
- The Events hub Search button grounds at (361,946) on this layout; the crossed-swords button at (490,736); March at (500,760) — all measured fresh this unit on the 642x951 windowed view.
- Cleared is false — the third Search found a target immediately and the next wave arrives about 18:54; successor 019 enqueued to start now.

## Result stats

- zombies_killed: 3
- cleared: false
- coin_before: 136700000 (HUD-rounded)
- coin_after: 137500000 (HUD-rounded)
- coins_collected: 804000
- medals_before: 5070 (unit 017 live Store read, carried)
- medals_after: 5100 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 1
- target: kill wave zombies and claim LOOT
- achieved: 3 Lv.10 kills dispatched, 3 LOOT rows claimed (804,000 coins)
- resources_gained: coins 804000, iron 804000, food 804000, medals 30, hero EXP 789000
- costs: about 12 minutes, stamina 88 to 59
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: h
