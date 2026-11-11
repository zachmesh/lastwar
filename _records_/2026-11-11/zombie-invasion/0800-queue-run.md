# Zombie Invasion — queue run 0800 (unit 011, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-011`, chain `zombie-2026-11-10` seq 11
- Executor: ticker-0741; token acquired 07:47 PT; claimed about 07:45 PT; finished about 08:00 PT
- Session: cc-577 (started), then cc-578 (re-started after ending cc-577 for the LOOT wait), Last War window 636402
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 10:12:58 at about 07:52; "Challenge begins in: 1d 10:12:59"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in 00:07:32 at the 07:52 read (about 07:59 local) — this disagrees with unit 010's derived wave time of about 07:54 (its 00:41:08 read at 07:13); the discrepancy is unresolved, only the two live reads are reported
- Wave live throughout the unit; zombies remained nearby at unit end (three Searches each found a target)
- Alliance Finding: Lv.80 Zombie Boss 139km EmberSteel 02:16:22; Lv.80 98km SAPPER1DOG 02:17:44; Lv.85 02:34:26 MesutCLK Apex; Lv.85 335km 02:42:27 MesutCLK Apex

## Entry state (base HUD, read live)

- Food 671.6M, iron 994.0M, coin **122.2M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,317
- Total Power 149,218,973; stamina **41**
- Entry screen was the world map, left open by the previous unit

## Dispatches — two squads in parallel (squads_parallel 2), then a third

- Squad 1 → **X:484 Y:329** (Lv.10, Suggested Power 670,000); stamina 41 → 31; march 00:02:06; deploy panel Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231
- Squad 2 → **X:540 Y:350** (Lv.10); stamina 31 → 22 (one +1 regen tick observed between reads); march 00:01:25 on the deploy panel; deploy panel auto-selected Squad 2 (2,175/2,175, Easy Win), no squad-tab tap needed
- Both squads were marching at once (March Queues 2/4 verified on screen) — parallel dispatch achieved; the third dispatch came after both had returned, so the unit's maximum simultaneous squads is 2
- Squad 1 (third dispatch) → **X:486 Y:427** (Lv.10, home-cluster target beside [AP3x]Bears Lair); stamina 22 → 13 (one more +1 regen tick observed); short march, Victory banner seen on screen
- Dispatch method: Events → title verified (Zombie Invasion - Glacieradon) → Search → screen read → crossed-swords at 496,753 → March at 499,755. The Events tab bar stayed on the Zombie Invasion tab on every re-open. Search at 370,941 held this unit.
- First March tap failed with a channel `stale_observation` ("target app exited or restarted") — no input was sent, the deploy panel stayed open, and the retry at the same point dispatched at once. The app never actually left the panel; same class as unit 001's restart report.
- Stamina at unit end: **13** (30 spent on three marches, +2 regen ticks observed)

## Claims — 3 LOOT rows × 268,000 coins = 804,000

Each row read before claiming: medal x10, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.

| Row | Coords | Potential rewards | Claimed |
| --- | --- | --- | --- |
| Squad 1 | X:484 Y:329 | green crate x1, green box x4 | yes, about 07:54 |
| Squad 2 | X:540 Y:350 | green crate x1, green box x4 | yes, about 07:54 |
| Squad 1 | X:486 Y:427 | green box x4, no green crate | yes, about 07:59 |

- Potential rewards vary per kill: the third row carried no green crate, only green box x4. The crate is not guaranteed.
- Gift box at the right end of the March Queues bar, re-grounded fresh on the current map view at (308,233); badge read 2 before the first claim and 1 before the second, cleared after each claim.
- Claim All is plain blue, no price tag, at 499,765.
- Coin HUD verified: **122.2M → 123.0M** (+0.8M ≈ 804,000, HUD rounds to 0.1M); food 671.6M → 672.4M, iron 994.0M → 994.9M (each +804,000).
- LOOT rows are created on arrival, confirmed again: Squad 2's row was claimable while Squad 2 was still Returning.

## Store

- Not visited this unit. Medal balance was NOT re-read live: +30 medals by card (10 per kill) against unit 010's live 4130 close, so no derived total is reported. The Coin Chest (SSR) row scroll/drag blocker from unit 008 stays open for the successor: try a drag from inside the Store list. No redemption made, no medals spent.
- Stamina 13 at close is not exhausted, so no refill was needed; the inventory stamina count was NOT checked this unit and no refill conclusion is drawn.

## Notes

- No "active on a different device" dialog; no access error.
- Chests opened: 0 (no Coin Chests owned or redeemed).
- Next wave was due about 07:59 local by this unit's live countdown; cleared is false, successor enqueued to start now.

## Result stats

- zombies_killed: 3
- cleared: false
- coin_before: 122200000 (HUD-rounded)
- coin_after: 123000000 (HUD-rounded)
- coins_collected: 804000
- medals_before: 4130 (unit 010 live close, carried)
- medals_after: unread
- chests_opened: 0
- squads_parallel: 2
- target: 3 parallel kills plus LOOT claim
- achieved: 3 kills, 804000 coins claimed
- resources_gained: coin 804000, iron 804000, food 804000, medals 30 (card-stated), hero EXP 789000, green crate x2, green box x12
- costs: stamina 30 spent (net 28 after regen), duration about 15 minutes
- verified: yes (dispatch and claim figures are same-unit live reads; coin_before and coin_after HUD-rounded)
- blocker_category: h (by-design partial, unit cap reached mid-chain, wave still live)
