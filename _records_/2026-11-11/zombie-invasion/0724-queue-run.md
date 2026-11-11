# Zombie Invasion — queue run 0724 (unit 010, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-010`, chain `zombie-2026-11-10` seq 10
- Executor: ticker-0707; token acquired 07:10:36 PT; claimed about 07:11 PT; finished about 07:24 PT
- Session: cc-574 (dropped mid-unit during the post-dispatch wait, cc-575 started, LastWar re-selected), Last War window 636402
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 10:46:34 at about 07:13; "Challenge begins in: 1d 10:46:35"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in about 00:41:08 at the 07:13 read (about 07:54 local)
- Wave live throughout the unit; zombies remained nearby at unit end (three Searches each found a target)
- Alliance Finding: Lv.80/85 Zombie Bosses at 207km, 90km, 115km, 139km, timers about 02:32-02:42

## Entry state (base HUD, read live)

- Food 670.8M, iron 993.2M, coin **121.4M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,317
- Total Power 149,218,973; stamina **64**
- Entry screen was Intercity Trade, left open by the ticker-0637 trucks unit (Today's Trade Count 1/5, one truck out, Recover red dot waiting) — returned to base with the back arrow; no truck work done, that is another unit's work

## Dispatches — three parallel squads (squads_parallel 3)

- Squad 1 → **X:475 Y:359** (Lv.10, Suggested Power 670,000); stamina 64 → 54; march 00:01:18; deploy panel Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231
- Squad 2 → **X:412 Y:402** (Lv.10); stamina 54 → 45; march 00:01:49; deploy panel auto-selected Squad 2 (2,175/2,175, Easy Win), no squad-tab tap needed
- Squad 3 → **X:483 Y:348** (Lv.10); stamina 45 → 35; march 00:00:56; deploy panel Easy Win, Unit Count 2,231/2,275 (OCR read)
- Dispatch method: batched Events → Search (2 second pause) → screen read → crossed-swords at 499,752 → March at 500,759. The Events tab bar stayed on the Zombie Invasion tab on every re-open; title verified before each Search. Search at 385,939; crossed-swords at 499,752/499,753; March at 500,759 — all three grounded points held this unit.
- All three squads arrived, fought and returned inside the unit; LOOT rows were created on arrival, as unit 054 established.
- Stamina at unit end: **36** (30 spent on marches, +2 regen observed between reads)

## Claims — 3 LOOT rows × 268,000 coins = 804,000

Each row read before claiming: medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.

| Row | Coords | Claimed |
| --- | --- | --- |
| Squad 1 | X:475 Y:359 | yes, about 07:21 |
| Squad 2 | X:412 Y:402 | yes, about 07:21 |
| Squad 3 | X:483 Y:348 | yes, about 07:21 |

- Gift box with red badge **3** at the right end of the March Queues bar, re-grounded fresh on the current map view at (323,224) via visual grounding; badge cleared after claiming.
- Claim All is plain blue, no price tag, at 499,765.
- Coin HUD verified: **121.4M → 122.2M** (+0.8M ≈ 804,000, HUD rounds to 0.1M); food 670.8M → 671.6M, iron 993.2M → 994.0M (each +804,000).

## Store (read live, about 07:21)

- Medal balance: **4130** (Store header, live)
- Rows on the first screen: 120 medals Limit 10; 80 medals Limit 10; 80 medals Limit 30; **50 Stamina 10 medals Limit 3 — available in this variant**; 160 medals Limit 50 (crate icon — the Iron Chest (SSR) row per unit 005, not a coin chest)
- The Coin Chest (SSR) row sits below the fold and was **not reached**: no drag attempt this unit (token budget ended at the balance read), no redemption made, no medals spent. The scroll/drag blocker from unit 008 stays open for the successor: try a drag from inside the list.
- Medal delta flag: unit 008 closed at 4080 (live, 04:14); this unit's three kills pay +30 medals, but the live header reads 4130, a +50 delta — **+20 medals unexplained**. The "Alliance Gifts received!" toast seen on the event page at about 07:21 is one candidate source; no derived total is reported, only the two live reads. Do not redeem the visible 160-medal Limit-50 row — it is the Iron Chest, not the coin chest.
- Stamina 36 at close is not exhausted, so no refill was needed; the inventory stamina count was NOT checked this unit and no refill conclusion is drawn.

## Notes

- Computer session cc-574 dropped during the 60-second post-dispatch wait; session cc-575 was started, LastWar re-selected, and no game state was lost (same class as units 049, 053, 054).
- No "active on a different device" dialog; no access error.
- Chests opened: 0 (no Coin Chests owned or redeemed).
- Next wave arrives about 07:54 local; cleared is false, successor enqueued to start now.

## Result stats

- zombies_killed: 3
- cleared: false
- coin_before: 121400000 (HUD-rounded)
- coin_after: 122200000 (HUD-rounded)
- coins_collected: 804000
- medals_before: 4080 (unit 008 live close, carried)
- medals_after: 4130 (Store header, live)
- chests_opened: 0
- squads_parallel: 3
