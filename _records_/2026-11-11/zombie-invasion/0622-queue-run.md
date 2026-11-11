# Zombie Invasion — queue run 0622 (unit 009, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-009`, chain `zombie-2026-11-10` seq 9
- Executor: ticker-0604; claimed 06:12 PT; finished about 06:22 PT
- Sessions: cc-567 (dropped mid-unit at about 06:19, observation_unavailable; restarted as cc-568, no game state lost), Last War window 636402
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 11:43:40 at about 06:20; "Challenge begins in: 1d 11:43:41"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in 00:38:13 at the 06:20 read, 00:32:53 at the 06:25 Store read
- Wave live throughout the unit; both Searches found Lv.10 targets, zombies remained nearby at unit end

## Entry state (read live)

- Coin panel (exact): **120,927,972** owned (coin_before); HUD 120.9M; food 670.2M, iron 992.7M, gold 13.22K
- Total Power 149,218,973; stamina **73** (regen tick from 72 at first sight)
- Base screen at entry; no "active on a different device" dialog; no login demanded

## Dispatches — one parallel pair (squads_parallel 2)

- Squad 1 → Lv.10 Invading Zombies, Suggested Power 670,000, stamina cost 10, despawn 11:37:43; deploy panel Squad 1, Unit Count 2,231/2,231, Easy Win; March at 500,755; March Queues 1/4
- Squad 2 → Lv.10 Invading Zombies; deploy panel had auto-selected Squad 2 (2,175/2,175, Easy Win), no squad-tab tap needed; March Queues **2/4**
- Dispatch method: single-step taps with a screen read between steps (Search 379,946; crossed-swords 499,753; March 500,755). The Events hub re-opened directly on the Zombie Invasion tab both times; title "Zombie Invasion - Glacieradon" verified before each Search.
- Stamina: 73 → 53 after the two marches (20 spent), 54 at the LOOT read (regen tick)

## Claims — 2 LOOT rows × 268,000 coins = 536,000

Each row read before claiming: medal x10, green crate x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.

| Row | Coords | Claimed |
| --- | --- | --- |
| Squad 1 | X:560 Y:399 | yes, about 06:20 |
| Squad 2 | X:555 Y:389 | yes, about 06:20 |

- Gift box at the right end of the March Queues bar, re-grounded fresh on the current map view at (311,226); badge read 1 at the 06:19 map read (only Squad 1's row existed then — Squad 2 arrived seconds later); both rows present in the LOOT panel at claim, no loss this unit
- Coin panel (exact) after claiming: **121,463,972** (coin_after) — 120,927,972 + 536,000 exactly; HUD 120.9M → 121.4M; iron 992.7M → 993.2M, food 670.2M → 670.8M (HUD-rounded, consistent with +536,000 each)
- Claim All is plain blue, no price tag

## Store — medals live, Coin Chest (SSR) row still unverified

- Store header medal balance read live: **4100** (medals_after); medals_before 4080 is unit 008's live Store read at 04:12, +20 from this unit's two kills — exact
- First-screen rows read live: gold chest x1 for 120 medals Limit 10; gold bar x1 for 80 medals Limit 10; gold bar x1 for 80 medals Limit 30; 50 Stamina x1 for 10 medals Limit 3 (available in this variant — NOT sold out, unlike the October event); crate x1 for 160 medals Limit 50
- One scroll attempt on the Store list produced no change (same rows, same Limits) — same as unit 008. The Coin Chest (SSR) row below the fold stays unverified in this variant; no redemption made, no chest opened (chests_opened 0). Do not redeem on October prices: none of the rows seen is identified as a Coin Chest.
- The Store button responded to a single tap this unit (824,225), unlike units 057/058 in October.

## Notes

- Session cc-567 dropped mid-unit (observation_unavailable at about 06:19, during the wait for the marches); cc-568 restarted, Last War re-selected, no game state lost — same class as units 049/053/054.
- No red-line touches: no diamonds or money spent, no price tag tapped, no speedup burned, no assembly/teleport.
- Successor enqueued to start now (cleared false, wave live).
