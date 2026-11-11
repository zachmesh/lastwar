# Zombie Invasion — queue run 0238 (unit 005, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-005`, chain `zombie-2026-11-10` seq 5
- Executor: ticker-0212; claimed 10:25:21Z; finished about 02:38 PT
- Session: cc-540, Last War window 636402; token re-acquired 02:30:07 PT (until 10:45:07Z)
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 15:27:49 at about 02:36; "Challenge begins in: 1d 15:27:50"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in about 00:22:30 at the 02:36 read
- Wave live throughout the unit; zombies remained nearby at unit end

## Entry state (base HUD, read live)

- Food 666.0M, iron 988.7M, coin **117.4M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,307
- Total Power 149,218,973; stamina **32**

## Dispatches — two parallel pairs (squads_parallel 2)

Cycle 1 (about 02:26–02:27):
- Squad 1 → **X:455 Y:409** (Lv.10, Suggested Power 670,000); stamina 32 → 22; March Queues 1/4
- Squad 2 → **X:495 Y:356** (Lv.10); stamina 22 → 12; March Queues **2/4**

Cycle 2 (about 02:33–02:34):
- Squad 3 → **X:423 Y:386** (Lv.10); stamina 23 → 13; March Queues 1/4
- Squad 4 → **X:516 Y:358** (Lv.10); stamina 13 → 3; March Queues **2/4**

Stamina at unit end: **3** (+10 kill-drop and slow regen observed between dispatches: 12 → 22 after cycle 1, 3 → 4 at unit end).

## Claims — 3 LOOT rows × 268,000 coins = 804,000

Each row: medal x10, green box x4 (cycle 2) or gold ticket x1 (cycle 1), iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.

| Row | Coords | Claimed |
| --- | --- | --- |
| Squad 2 | X:495 Y:356 | yes, about 02:30 |
| Squad 3 | X:423 Y:386 | yes, about 02:35 |
| Squad 4 | X:516 Y:358 | yes, about 02:37 |

- Coin HUD verified: **117.4M → 118.2M** (+0.8M ≈ 804,000, HUD rounds to 0.1M)
- Food/iron verified after claims 1–2: food 666.0M → 666.6M, iron 988.7M → 989.3M (each +268,000); not re-read after claim 3
- Claim All is plain blue, no price tag; gift box at the right end of the March Queues bar, re-grounded fresh each time (321,230 then 323,227)

## Lost row — Squad 1 (X:455 Y:409)

- Squad 1 arrived, fought and returned home before the LOOT panel was first opened (~02:30); **no LOOT row for it ever appeared**
- Its medals are missing too: Store header read **4010** live, against 4020 expected from 004's 4000 + 2 kills × 10 — the missing kill's medal x10 never materialised
- Loss: 268,000 coins + medal x10 + iron/food 268.0K each
- Pattern confirmed (units 007/009, 048): a row is lost when its squad returns home before the LOOT panel is opened. Mitigation verified this unit: claim promptly after the first arrival, while a squad is still out or returning — all three rows claimed that way succeeded. The successor must re-check the gift badge for a late Squad 1 row.

## Store (read live, about 02:33)

- Medal balance: **4010** (Store header, live)
- **160-medal crate row = Iron Chest (SSR)**, Owned 1.1K, "At the current Base Level, you can obtain 1.35M Iron" — NOT a Coin Chest; no redemption made
- 120-medal row = Universal Exclusive Weapon Shard (unit 004); 50 Stamina (10 medals, Limit 3) available in this variant
- Two scroll attempts (scroll action, then drag) did not move the Store list, so the rows below the fold remain unidentified; no Coin Chest row established in this variant yet
- Store X needed a second tap (first tap only dismissed the tooltip); event page back arrow is at (159,947), not (73,936)

## Notes

- Inventory stamina count was NOT checked this unit — stamina (3) is not concluded exhausted. Successor must check the inventory (Free Claim first, then 10/50 stamina items; unit 058 recorded 50-stamina x609) before concluding refill sources are exhausted.
- A transient 66×20 LastWar window (642962, titled "Window") appeared during the Squad 4 dispatch batch; the main window (636402) was unaffected and the batch completed — harmless.
- Events icon tap coordinates vary slightly between openings (935,138 and 927,137 both worked); the Search card's crossed-swords button sat at (498,731) on the Squad 4 card.
- Chests opened: 0 (no Coin Chests owned or redeemed).

## Result stats

- zombies_killed: 4
- cleared: false
- coin_before: 117400000 (HUD-rounded)
- coin_after: 118200000 (HUD-rounded)
- coins_collected: 804000
- medals_before: 4000
- medals_after: 4010
- chests_opened: 0
- squads_parallel: 2
