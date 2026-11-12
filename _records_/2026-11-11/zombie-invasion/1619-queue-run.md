# Zombie Invasion — queue run 1619 (unit 017, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-017`, chain `zombie-2026-11-10` seq 17
- Executor: ticker-1547; token acquired about 16:02 PT; claimed about 16:03 PT; finished about 16:19 PT
- Session: cc-635, Last War window 676414, no drop, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, wave still live at close

## Event state (Glacieradon variant, read live)

- Event timer 2d 01:54:24 at about 16:08, 2d 01:47:12 at close; "Challenge begins in: 1d 01:54:25"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:49:00 at the 16:08 read, 00:43:08 at the 16:17 read
- Counter 40/40 (green bar); Alliance Finding: Lv.85 Zombie Boss 226km, Lv.80 302km, Lv.80 248km, Lv.95 (Skinner Box, MegaLoki Apex) — rally-class, far away, not attacked
- The Events hub opened directly on the Zombie Invasion tab both times (tab persisted across openings this pass)

## Entry state (base HUD, read live)

- Food 688.3M, iron 1.0G, coin **135.6M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **79** (80 after a regen tick at the first LOOT read)
- March Queues 0/4; gift badge **2** (handover rows from unit 016)

## Handover claims — 2 LOOT rows × 268,000 coins = 536,000

Rows read before claiming (unit 016's kills):

| Row | Coords | Contents (row-read) |
| --- | --- | --- |
| 1 | X:454 Y:281 | medal x10, green crate x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K |
| 2 | X:586 Y:340 | medal x10, green crate x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K |

- Gift box re-grounded fresh on the current map view at (315,225); badge cleared after claiming.
- Claim All plain blue, no price tag, at 499,765.
- Coin HUD verified: **135.6M → 136.2M**; food 688.3M → 688.8M (+536,000).

## Dispatches — two parallel squads (squads_parallel 2)

- Squad 1 → **X:500 Y:417** (Lv.10, Suggested Power 670,000, stamina cost 10, despawn 11:48:22, near [AP3x]War Palace); deploy panel Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231; march about 10 seconds
- Squad 2 → **X:436 Y:435** (Lv.10); march 00:01:10 outbound; deploy panel auto-selected Squad 2, no squad-tab tap needed
- Dispatch method: Squad 1 single-step (Search 380,940 → read card → crossed-swords 499,753 → read panel → March 499,757). Squad 2 batched (Events → wait 2 → Search → wait 2 → swords → wait 1.5 → March) in one 7-step batch; the batch receipt read March Queues 2/4, proving both squads out at once.
- Method note: the first March tap at (500,755) returned outcome_unknown — the deploy panel had re-rendered and the tap did not dispatch (stamina still 80, panel still open on re-snap). Re-tapped at the re-grounded button centre (499,757) and it dispatched at once. The March button's active area sits at its lower edge; ground it low and verify after any outcome_unknown instead of re-tapping blind.
- Stamina 80 → 60 for the two marches (+1 regen tick during the waits → 61 at the second LOOT read).

## Own claims — 2 LOOT rows × 268,000 coins = 536,000

Rows read before claiming (this unit's kills, both resolved on arrival):

| Row | Coords | Contents (row-read) |
| --- | --- | --- |
| 1 | X:436 Y:435 | medal x10, green crate x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K |
| 2 | X:500 Y:417 | medal x10, gold ticket x1, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K |

- Gift badge 2 at the second claim (rows exist on arrival, before squads return home); badge cleared after claiming.
- Coin HUD verified: **136.2M → 136.7M**; food 688.8M → 689.4M (+536,000); iron 1.0G display unchanged.
- Total coins claimed this unit: 1,072,000 (4 rows × 268,000).

## Store (Glacieradon variant, read live)

- Store button worked on a single tap this pass (829,205) — no unresponsive-button repeat of units 057/058.
- Medal balance (Store header, live): **5070**.
- First-screen rows, top to bottom: gold chest x1 120 medals Limit 10; gold bar x1 80 medals Limit 10; gold bar x1 80 medals Limit 30; **50 Stamina x1 10 medals Limit 3** (available in this variant — not sold out); crate x1 160 medals Limit 50; a sixth row is cut off below the fold.
- No Coin Chest row on the first screen — the October Coin Chest (SSR) 160 / (UR) 480 rows are not this variant's Store list. No redemption made, no chest opened.
- Below-fold rows still unread: one scroll attempt (down 3 at 500,500) produced no change in the list — the scroll did not move it. The successor must retry with a drag or a different scroll point. Medals_before was not read this unit (Store visited only at the end); medals_after 5070 is the live close, not a derived figure.
- Stamina 61 at close; no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- Seeding correction: this pass first enqueued a duplicate successor (018) after reading the worktree snapshot, which showed no pending zombie unit; the live pool already held 017 (minted 22:56:16Z by the 016 completion). The duplicate 018 was removed from the live pool the same minute. Seeding must read the live pool, not the worktree snapshot.
- The skull-icon timer on the right edge (00:00:58 countdown, badge 1) is still unidentified; left alone.
- Toasts seen: "Signed in as HidingAnt504" (Game Center); alliance appointment notice; no device-conflict dialog.
- Cleared is false — Search found Lv.10 targets immediately and the wave countdown still had 43 minutes at close. Successor enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 135600000 (HUD-rounded)
- coin_after: 136700000 (HUD-rounded)
- coins_collected: 1072000
- medals_before: unverified (Store not visited at entry)
- medals_after: 5070 (Store header, live-read)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, 4 LOOT rows claimed (1072000 coins)
- resources_gained: coins 1072000, iron 1072000, food 1072000, medals 40, hero EXP 1052000
- costs: about 15 minutes, stamina 80 to 61
- verified: yes (coin, kill and Store figures live-read; medals_before not read, stated as unverified)
- blocker_category: h
