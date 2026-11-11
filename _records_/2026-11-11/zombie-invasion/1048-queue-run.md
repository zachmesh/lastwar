# Zombie Invasion — queue run 1048 (unit 013, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-013`, chain `zombie-2026-11-10` seq 13
- Executor: ticker-1045; token acquired 10:48:55 PT; claimed about 10:49 PT; finished about 10:58 PT
- Session: cc-595, Last War window 636402, no drop, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, squad 2's kill still in flight at close

## Event state (Glacieradon variant, read live)

- Event timer 2d 07:08:39 at about 10:50; "Challenge begins in: 1d 07:08:40"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:03:14 at the 10:50 read (about 10:53:30 local)
- Alliance Finding: Lv.90 Zombie Boss 384km, Lv.90 249km, Lv.80 164km, Lv.85 171km (Niermeat, MegaLoki Apex)
- The event tab is live again under the Glacieradon variant; the INDEX.md chain-close note (event ended 2026-10-30) is stale — filed as Issue #642

## Entry state (base HUD, read live)

- Food 682.2M, iron 1.0G, coin **129.6M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **117**
- Skull icon on the right edge counted down 00:00:57 to 00:00:36 during the unit — unidentified timer, not the wave countdown; left alone

## Dispatches — two parallel squads (squads_parallel 2)

- Squad 1 → **X:404 Y:332** (Lv.10, Suggested Power 670,000); stamina 117 → 107; march 00:02:51; deploy panel Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231
- Squad 2 → **X:381 Y:319** (Lv.10); stamina 107 → 97; march 00:03:50; deploy panel auto-selected Squad 2 (2,175/2,175, Easy Win), no squad-tab tap needed
- Dispatch method: batched Events → wait 1 → Search (386,941) → wait 2 → crossed-swords (499,753) → wait 2 → read panel → March (500,755). Both batches landed cleanly; the Events tab stayed on Zombie Invasion and the title was verified before each Search.
- Third dispatch attempt: Search opened a **Lv.85 Zombie Boss** card instead (Found by [AP3x]MegaLoki Apex, Suggested Power 34,500,000, stamina 20, despawn 03:26:21). Rally-class, not a solo target — no march made; card closed by tapping empty ground. Whether Search fell through because no Lv.10 was nearby or the tap landed on Boss Search is unresolved; filed in Issue #642. No stamina spent on the attempt.

## Claims — 1 LOOT row × 268,000 coins = 268,000

Row read before claiming: medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.

| Row | Coords | Claimed |
| --- | --- | --- |
| Squad 1 | X:404 Y:332 | yes, about 10:57 |
| Squad 2 | X:381 Y:319 | no — still outbound at close (00:00:40 at last read), row lands for the successor |

- Gift box with red badge **1** at the right end of the March Queues bar, re-grounded fresh on the current map view at (308,237); badge cleared after claiming.
- Claim All is plain blue, no price tag, at 499,765.
- Coin HUD verified: **129.6M → 129.9M** (+0.3M ≈ 268,000, HUD rounds to 0.1M); food 682.2M → 682.5M (+268,000).
- Squad 1 Returning 00:01:30 at close; squad 2 Go X:381 Y:319 00:00:40 at close.

## Store

- Not visited this unit (token lease ended at the LOOT claim). No medal balance re-read, no redemption, no medals spent.
- Medals: before 4130 (unit 010 live Store header); after 4140 **derived** (+10 for the claimed kill), not live-read — flagged here, not a closing count.
- Chests opened: 0.
- Stamina 98 at close (117 − 20 spent + 1 regen); no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- The batched dispatch with a 2-second pause after Search held for both squads; the third Search landing on a boss card is the open question for the successor (Issue #642).
- Token lease expired 11:03:55 PT; the unit closed at the cap with squad 2 in flight rather than waiting out its return. Cleared is false, successor enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 129600000 (HUD-rounded)
- coin_after: 129900000 (HUD-rounded)
- coins_collected: 268000
- medals_before: 4130 (unit 010 live close, carried)
- medals_after: 4140 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, 1 LOOT row claimed (268,000 coins)
- resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
- costs: about 10 minutes, stamina 117 to 98
- verified: yes (coin and kill figures live-read; medals_after derived, flagged)
- blocker_category: h
