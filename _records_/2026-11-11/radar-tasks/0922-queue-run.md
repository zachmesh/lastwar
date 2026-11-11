# Radar Tasks — queue run 0922 (unit radar-2026-11-11-0603)

- Unit: `radar-2026-11-11-0603`, regular `radar`, activity `radar-tasks`
- Executor: ticker-0845; token held from the harvest unit; claimed about 09:09 PT; game work about 09:11 to 09:22 PT
- Session: cc-582, Last War window 636402
- Status: done — release-day bar work complete (stored 0/40, 12 claims, points 403 to 415)
- Duel posture (live, `duel.py --json`): duel day 3, Age of Science, radar_posture release; day ends 18:00 PT; radar claims score 10,000 each (Handbook rate)
- Note on times: the queue record stamps finished_at at the complete call; the game work for this unit ran about 09:11 to 09:22 PT (about 11 minutes).

## Entry state (radar screen, verified live)

- Lv.13, radar points 403, stored 1/40, stamina 18
- Restore line: "12 Radar Task(s) will be restored in 02:24:40" at the first read; "Fully restore at 11-12 05:39:11 local time" (later read 11-12 11:39:11 after the executions — the full-restore time moved with the restore cycle)
- Bottom bar at entry: "You can complete 6 tasks, requires 60 Stamina." with Quick Execute
- Entry: satellite dish grounded fresh from a 4x crop of the left icon column — the blue circle with the white dish and red badge 5, centre norm (43,724) — and opened the radar on the first tap with move-wait-click. The dish sits below the truck icon, as the 1754/1945 units found. The truck icon above it (with "?" bubbles) is the Secret Command Post slot, not the dish.

## Stamina — free claim exhausted, items used

- The first Quick Execute tap opened the Regain Stamina panel: stamina 18/120, "Restores 1 stamina every 300 seconds, fully replenished in 08:27:32".
- 75 Stamina free claim: Remaining Today 0/2 — both free claims already used today, button greyed with an 08:47:17 cooldown. No free claim available.
- 100 Stamina Buy for 300 rubies: NOT tapped (red line).
- The "x3" pill on the 50 Stamina row (Owned 669) is a quick-use control, not a quantity stepper: tapping it consumed 3x 50-stamina items at once ("you've acquired 150 Stamina", Owned 669 to 666). Stamina 18 to 168. The extra 2 items (100 stamina) were not needed for this unit's 70-stamina spend; the pill's quantity is the amount it uses, so a future unit needing one item must use the Use button with the pill read first, or accept the pill quantity. This is a scoring release day, so item use is within the standing stamina rules (Free Claim first — exhausted — then items, never rubies).
- 10 Stamina Owned 647 was not used.

## Executions and claims

- Quick Execute batch 1: 6 tasks, stamina 168 to 108 (60 spent). Bar flipped to "11 task rewards can be claimed" with Claim All.
- Claim All 1: 11 rewards claimed; radar points 403 to 414 (+11). CONGRATULATIONS popup read: radar item 110, EXP 17.7M, blue triangle 225, chest 3.2K, iron 3.2M, food 4.5M, coin 2.1M.
- The app exited/restarted once while dismissing the popup (tap at (100,200)); re-observed on the radar screen with state intact (points 414, Quick Execute offered). No input was replayed.
- Quick Execute batch 2: 1 task, stamina 108 to 98 (10 spent). Bar flipped to "1 task rewards can be claimed" with Claim All.
- Claim All 2: 1 reward claimed; radar points 414 to 415 (+1). CONGRATULATIONS popup read: radar item 10, EXP 1.7M, iron 348.0K, food 348.0K, coin 200.4K.
- Totals: 7 tasks executed, 12 rewards claimed, radar points 403 to 415 (+12), stamina 18 to 98 (net +80 after the +150 item refill and 70 spent).
- Combined claim rewards: radar item 120, EXP 19.4M, iron about 3.55M, food about 4.85M, coin about 2.30M, blue triangle 225, chest 3.2K. Base HUD after the unit: food 680.8M, iron 1.0G, coin 127.8M — deltas from the post-harvest 675.9M / 998.1M / 125.4M match the popup figures at HUD rounding (food +4.9M, iron +3.5M, coin +2.4M).
- Duel value: 12 claims at the Handbook 10,000 each implies 120,000 duel points; the VS duel panel was NOT read live, so no duel-score delta is claimed here (the duel-score unit reads it).
- The floating figures seen after the final claim (660,000 / 1,000,000 / 2,300,000) do not match the popup's per-claim read and are not reported as rewards; their meaning is unread.

## Map pins — present at entry, gone at close, mechanism unverified

- Pins visible at entry (9): 3 grey skull pins with red dots (right, left, bottom), 1 blue person pin with a red dot (right), 1 centre purple pin ([AP3x]Starfall), 4 green/ally portrait pins at the top (the 3 top-centre portraits may be alliance-member markers rather than task pins).
- Pins visible at close (after the second Claim All): 0. Only the home-base marker and one alliance member avatar ([AP3x]SAPPER1DOG) remain on the map.
- The pins vanished between the first CONGRATULATIONS screenshot (pins visible behind the popup) and the post-restart screenshot. Candidates, none verified: the Claim All pool included pin rewards; the pin tasks expired; the app restart re-rendered without them. The 0504 unit this morning also found pins that opened no card (1 pin, 3 tap variants, no card), so at least some pins in this cycle were non-interactive.
- Closing read per the release standard: 0 pins standing. No pin was tapped this unit, so no pin was individually completed or claimed by tap. This breaks the Issue #632 pattern (release units closing partial on unworked pins) in the sense that no pin remains standing, but the clearing mechanism is unverified and the next release unit should watch whether pins reappear with the 02:21:35 restore. Commented on Issue #632 by this pass.

## Closing state (radar screen, read live)

- Lv.13, radar points 415, stored 0/40, stamina 98
- Restore: "12 Radar Task(s) will be restored in 02:21:35"; fully restore 11-12 11:39:11 local time
- No bottom-bar offer remains (no Quick Execute, no Claim All); 0 pins standing
- No "active on a different device" dialog; no access error; no diamonds or money spent; the 300-ruby Buy was not tapped.

## Result stats

- target: release-day clear — execute stored tasks and claim all rewards on duel day 3
- achieved: 7 tasks executed, 12 rewards claimed, stored 0/40, points 403 to 415
- resources_gained: radar item 120, EXP 19400000, iron 3548000, food 4848000, coin 2300400
- costs: stamina 70 spent (18 to 98 after a 150 refill from 3x 50-stamina items); about 11 minutes of game work
- verified: yes (radar screen reads before/after; popup reward reads; base HUD deltas match)
- blocker_category: none
- tasks_claimed: 12
- tasks_executed: 7
- pins_inventoried: 9
- pins_worked: 0
- free_stamina_claims: 0
- radar_points_before: 403
- radar_points_after: 415
- stored_before: 1
- stored_after: 0
- stamina_before: 18
- stamina_after: 98
- duel_score_before: not-read
- duel_score_after: not-read
- entry_attempts: 1
- device_takeovers: 0
