# Zombie Invasion — queue run 0832 (unit 012, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-012`, chain `zombie-2026-11-10` seq 12
- Executor: ticker-0804; token acquired 08:22 PT; claimed about 08:22 PT; finished about 08:32 PT
- Session: cc-579, Last War window 636402
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 09:33:53 at about 08:33; "Challenge begins in: 1d 09:33:54"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in 00:28:27 at the 08:33 read (about 09:01 local)
- Alliance Finding: Lv.85 Zombie Boss 335km 02:03:22 MesutCLK; Lv.85 236km 02:34:03 SAPPER1DOG; Lv.80 281km 02:35:50 YOUGO; Lv.85 252km 02:36:40 YOUGO
- Wave live at unit time; Search found a target at once

## Entry state (world map HUD, read live)

- Food 672.4M, iron 994.9M, coin **123.0M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,317
- Total Power 149,218,973; stamina **18**
- Entry screen was the world map, left open by the previous unit

## Dispatch — one squad (squads_parallel 1), stamina-bound

- Squad 1 → **X:463 Y:324** (Lv.10, Suggested Power 670,000); stamina 18 → 9 after the march (one +1 regen tick observed between reads); march 00:02:12; March Queues 1/4 verified on screen
- Dispatch method: Events → Zombie Invasion - Glacieradon page verified by title → Search at 402,949 → card read (Lv.10, Suggested Power 670,000) → crossed-swords at 497,753 → 1.5s wait → March at 499,755, batched. No second dispatch was attempted in parallel: stamina 9 after the first march is short of the 10 a second march costs.
- Stamina refill attempted and abandoned: Inventory → Special tab opened; its first screen shows Amethyst Crystal 4,882, a blue crystal 293,800, chests 260 / 1,899 / 387 / 1 / 3 and no stamina item — the 50/10-stamina items sit below the fold and were not reached. One channel `stale_observation` error during the Inventory look (recovered by re-selecting the window; the app never exited). The hunt was abandoned under the unit clock so the in-flight march's LOOT could be claimed in-unit; the inventory stamina count is therefore NOT verified this unit and no exhaustion conclusion is drawn.
- No "active on a different device" dialog; no access error.

## Claims — 1 LOOT row × 268,000 coins = 268,000

- Row read before claiming: Lv.10 Invading Zombies X:463 Y:324, medal x10, gold ticket x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.
- Gift box at the right end of the March Queues bar, badge 1, grounded fresh on the current map view at (316,233); Claim All plain blue, no price tag, at 499,765.
- Coin HUD verified: **123.0M → 123.3M** (+0.3M ≈ 268,000); food 672.4M → 672.7M; iron 994.9M → 995.1M (HUD rounding on the iron read).
- Squad 1 was still Returning (00:00:42) at claim time; the LOOT row is created on arrival, confirmed again.

## Store

- Not visited this unit. Medal balance was NOT re-read live; no derived total is reported (the card states +10 medals for this kill). The Coin Chest (SSR) row scroll/drag blocker from unit 008 stays open for the successor: try a drag from inside the Store list. No redemption made, no medals spent.
- Chests opened: 0 (no Coin Chests owned or redeemed).

## Notes

- squads_parallel 1: stamina-bound (18 at entry, one 10-cost march, 9 left), not the march cap of 4; the parallel attempt was the Inventory stamina-item hunt, which did not land in-unit.
- Successor should: open a 50-stamina item first (scroll the Special tab to find it), then run parallel dispatches while the wave lasts; visit the Store for the SSR row drag test and a live medal balance.

## Result stats

- zombies_killed: 1
- cleared: false
- coin_before: 123000000 (HUD-rounded)
- coin_after: 123300000 (HUD-rounded)
- coins_collected: 268000
- medals_before: unread
- medals_after: unread
- chests_opened: 0
- squads_parallel: 1
- target: 2 parallel kills plus LOOT claim
- achieved: 1 kill, 268000 coins claimed
- resources_gained: coin 268000, iron 268000, food 268000, medals 10 (card-stated), hero EXP 263000, gold ticket 1
- costs: stamina 10 spent (net 8 after regen), duration about 10 minutes
- verified: yes (dispatch and claim figures are same-unit live reads; coin_before and coin_after HUD-rounded)
- blocker_category: h (by-design partial, unit cap reached mid-chain, wave still live)
