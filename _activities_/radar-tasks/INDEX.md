---
title: Radar Tasks
created: 2026-10-25T18:58:00Z
modified: 2026-11-10T01:46:47Z
level: L1
version: 1.62.0
proficiency: learning
description: Radar stored tasks, Quick Execute coverage and exceptions, map pin handling, stack and release completion standards and duel scoring
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25 to 2026-10-31
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1904 radar release unit)
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner live guidance during the evening radar clear, 2026-10-25
  - source: Last War Wiki Radar Tasks page on Fandom, accessed 2026-11-01
  - source: LDShop radar and secret tasks guide, accessed 2026-11-01
  - source: GrindnStrat radar tasks guide, accessed 2026-11-01
  - source: Last War Handbook VS schedule guide, accessed 2026-11-01
  - source: lastwar.wiki Alliance Duel page, accessed 2026-11-01
  - source: radar tasks execution record 2026-11-01 1122 queue run
  - source: radar tasks execution record 2026-11-01 1629 queue run
  - source: ticker-2304 radar execution record 2026-11-01 2319 queue run
  - source: ticker-0204 radar execution record 2026-11-02 0226 queue run
  - source: radar tasks execution record 2026-11-02 0636 queue run
  - source: ticker-1004 radar-tasks execution record 2026-11-02 1026 queue run (partial, radar screen never entered)
  - source: radar tasks execution record 2026-11-02 2242 queue run
  - source: ticker-0204 radar-tasks execution record 2026-11-03 0212 queue run (partial by design, single-offer trap in at-entry form)
  - source: ticker-0634 radar-tasks execution record 2026-11-03 0636 queue run (partial by design, dish centre re-grounded, Claim All-only bar again)
  - source: ticker-1004 radar-tasks execution record 2026-11-03 1010 queue run (partial by design, third consecutive Claim All-only bar, stored 25 of 40, three skull pins inventoried)
  - source: PR 237 merged 2026-11-03 16:38 local (duel.py timezone fix, Refs #235) settling the 1450 live-dialog contradiction
  - source: ticker-1904 radar-tasks execution record 2026-11-03 1913 queue run (partial, release day, 17 claims, no TIPS dialog on any Claim All, 4 pins carried, Issue #235 evidence)
  - source: ticker-2304 radar-tasks execution record 2026-11-03 2317 queue run (partial, release day, story pin completed, March centre 500,751, 11 claims, no TIPS dialog, Issue #235 evidence)
  - source: ticker-0334 radar-tasks execution record 2026-11-04 0334 queue run (partial, Doom Elite pin identified, rally blocked Issue #268, stamina 156 over the old 120 cap, Rare Farmland pin identified)
  - source: ticker-0706 radar-tasks execution record 2026-11-04 0720 queue run (partial, release day, Doom Legion base claimed, Rare Farmland gathering dispatched, blue skull pin opens no card)
  - source: ticker-1004 radar-tasks execution record 2026-11-04 1005 queue run (partial, duel day 3 release, 13 claims, points 206 to 219, stored 0 of 40, stamina 131 to 81, Doom Elite pin march left for the next unit per rule R7)
  - source: ticker-1534 radar-tasks execution record 2026-11-04 1534 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, seventh consecutive ticker pass to fail this way, Issue 284; PT-corrected duel posture day 3 release)
  - source: ticker-1904 radar-tasks execution record 2026-11-04 1904 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, fourteenth consecutive ticker pass to fail this way, blocker continuing past the 19-00 reset, Issue 284; live posture day 4 Train Heroes stack, not the stale unit-window day 3 release wording)
  - source: ticker-2334 radar-tasks execution record 2026-11-04 2334 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, twenty-second consecutive ticker pass to fail this way, Issue 284; stack-posture unit, duel day 4)
  - source: ticker-1504 radar-tasks execution record 2026-11-05 1504 queue run (failed, Mac device offline, fifty-first consecutive ticker pass to fail this way, twelfth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 7h30m, unchanged since the 1025 pass; four invokes, zero responses; stack-posture unit, duel day 4)
  - source: ticker-1933 radar-tasks execution record 2026-11-05 1933 queue run (failed, Mac device offline, fifty-ninth consecutive ticker pass to fail this way, twentieth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 12h, unchanged since the 1025 pass; five invokes, zero responses; stack-window unit, live posture release, duel day 5 Total Mobilization)
  - source: ticker-0004 radar-tasks execution record 2026-11-06 0004 queue run (failed, Mac device offline, sixty-third consecutive ticker pass to fail this way, twenty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 16h50m, unchanged since the 1025 pass and identical to the 2303 reading; five invokes, zero responses; release-day unit, duel day 5)
  - source: ticker-0342 radar-tasks execution record 2026-11-06 0342 queue run (failed, Mac device offline, sixty-sixth consecutive ticker pass to fail this way, twenty-seventh in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 20h10m, unchanged since the 0234 pass; five invokes, zero responses; release-day unit, duel day 5)
  - source: ticker-0741 radar-tasks execution record 2026-11-06 0741 queue run (failed, Mac device offline, seventy-fourth consecutive ticker pass to fail this way, thirty-fifth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 24h10m, unchanged since the 0704 pass; five invokes, zero responses, recovery-device health check and native repair both timed out after 25s; release-day unit, duel day 5)
  - source: ticker-1104 radar-tasks execution record 2026-11-06 1104 queue run (failed, Mac device offline, seventy-seventh consecutive ticker pass to fail this way, thirty-eighth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 27h45m, unchanged since the 0934 pass; five invokes, zero responses, recovery-device health check timed out after 25s, matching the 0741/0832/0934 signature; release-day unit, duel day 5)
  - source: ticker-1235 radar-tasks execution record 2026-11-06 1235 queue run (failed, Mac device offline, seventy-eighth consecutive ticker pass to fail this way, thirty-ninth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 29h, unchanged since the 1104 pass; five invokes, zero responses, recovery-device health check timed out after 25s, matching the 0741/0832/0934/1104 signature; release-day unit, duel day 5)
  - source: ticker-1507 radar-tasks execution record 2026-11-06 1512 queue run (failed, Mac device offline, eightieth consecutive ticker pass to fail this way, forty-first in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 31h36m, unchanged since the 1235 pass; five invokes, zero responses, recovery-device repair and health check both timed out after 25s, matching the 1235/1349 signature; release-day unit, duel day 5)
  - source: ticker-1934 radar-tasks execution record 2026-11-06 1934 queue run (failed, Mac device offline, eighty-eighth consecutive ticker pass to fail this way, forty-ninth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 36h, unchanged since the ticker-1025 pass; seven invokes, zero responses, recovery-device health check and repair both timed out after 25s; duel rolled to day 6 Enemy Buster, radar posture stack, at about 18:00 local)
  - source: ticker-0011 radar-tasks execution record 2026-11-07 0011 queue run (failed, Mac device offline, ninety-third consecutive ticker pass to fail this way, fifty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 40h45m, unchanged since the ticker-1025 pass; four invokes, zero responses, recovery-device health check and native repair both timed out after 25s; five records-PR action-log conflicts resolved first)
  - source: ticker-0127 radar-tasks execution record 2026-11-07 0132 queue run (failed, Mac device offline, ninety-fourth consecutive ticker pass to fail this way, fifty-fifth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 41h57m, unchanged since the ticker-0011 pass; six invokes, zero responses, recovery-device repair with target "web" rejected as invalid_command_params, corrected native repair and health check both timed out after 25s; pre-reset zero-sweep pair staged for tonight's 19:00 reset)
  - source: ticker-0304 radar-tasks execution record 2026-11-07 0304 queue run (failed, Mac device offline, ninety-seventh consecutive ticker pass to fail this way, fifty-eighth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 43h30m, unchanged since the ticker-0234 pass; five invokes, zero responses, recovery-device health check timed out after 25s; stack-day unit, duel day 6; PR 382 action-log conflict resolved first by union-merge of main)
  - source: ticker-0734 radar-tasks execution record 2026-11-07 0734 queue run (failed, Mac device offline, one-hundred-third consecutive ticker pass to fail this way, sixty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 48h, unchanged since the ticker-0704 pass; seven invokes, zero responses, recovery-device health check and repair both timed out after 25s; stack-day unit, duel day 6)
  - source: ticker-1104 radar-tasks execution record 2026-11-07 1104 queue run (failed, Mac device online, window off-Space, one-hundred-eighth consecutive ticker pass to fail this way, second in the new capture-failure form, Issue 282; last_seen 2026-11-07T18:41:20Z fresh; eleven invokes, zero game screens, four capture attempts failed identically, open_app outcome_unknown with no relaunch or move, set_window_frame refused observation_required; stack-day unit, duel day 6)
  - source: ticker-1608 radar-tasks execution record 2026-11-07 1616 queue run (failed, Mac device online, window off-Space, one-hundred-twelfth consecutive ticker pass to fail this way, sixth in the new capture-failure form, Issue 282; last_seen 2026-11-07T23:44:36Z about 32 minutes stale; four invokes, zero game screens, four capture attempts failed identically; stack-day unit, duel day 6)
  - source: ticker-1633 alliance-donations execution record 2026-11-07 1633 queue run (incidental radar reads during the navigation detour - BASE tap 920,975 opened the radar map, Lv.13, points 237 to 259, stored 19/40 to 0/40, stamina 100 to 35, 19 tasks completed between screenshots with no executor tap; record commit a85cfdafa8 on records/2026-11-07)
  - source: ticker-1655 harvest, survivors and training execution records 2026-11-07 1655 queue runs (capture channel working again on live game screens after the 1020-1608 capture-failure run, Issue 282; record commit 514e333e5b on records/2026-11-07)
  - source: ticker-1904 radar execution record 2026-11-07 1912 queue run (done, stack empty, dish re-grounded for the windowed layout, capture channel recovered)
  - source: ticker-1249 radar execution record 2026-11-08 1256 queue run (done, stack-day Quick Execute 4 tasks, stamina 120 to 80, radar points 267 unchanged, bar flipped to Claim All only with 10 rewards pending, pins inventoried untapped; record commit 6d4ec6287 on records/2026-11-08)
  - source: ticker-1352 radar execution record 2026-11-08 1355 queue run (partial, Claim All bar lockout, 16 stored tasks unexecuted, 10 rewards pending, 6 pins inventoried, duplicate-unit Issue #466; record commit bf20e1a48 on records/2026-11-08)
  - source: 2026-11-08 daily retro, execution-knowledge action A-2026-11-08-01 (Issue #484): prefer the (50,740) dish point as the first tap; (54,583) and (54,780) failed 2026-11-08; record commit 90c3fa64e on records/2026-11-08
  - source: ticker-2334 radar-tasks execution record 2026-11-08 2335 queue run (partial, release day 1, 16 tasks executed, 44 rewards claimed, stored 39/40 to 0/40, points 267 to 311, dish re-grounded to norm 37,736 in the 642x951 window, 6 pins left untapped; record commit 86b26f5ce0 on records/2026-11-08)
  - source: ticker-0140 radar-tasks execution record 2026-11-09 0159 queue run (done, stack empty 0 of 40, points 311, restore 12 tasks in 03:41:39, 6 pins inventoried untapped, dish grounded (54,707) first tap, NEW! badge re-seen; record commit 3d5dc8314 on records/2026-11-09)
  - source: ticker-0334 radar-tasks execution record 2026-11-09 0335 queue run (partial, release day, dish re-grounded (51,718) first try after (55,689) missed, Rare Iron Mine gathering dispatched 720K 00:06:57, 5 pins inventoried unattempted, points 311, restore 12 tasks in 02:01:04; record commit 063a5bde7f on records/2026-11-09)
  - source: ticker-0634 resource-collection execution record 2026-11-09 0636 queue run (partial, gold circle with blue gem above the blue truck opens the world/radar map with 6 task rewards claimable - a radar entry point, not the truck loot; record commit 04b12d13 on records/2026-11-09)
  - source: ticker-0842 radar-tasks execution record 2026-11-09 0852 queue run (partial, release day, 3 tasks executed, 11 claims, points 311 to 322, stored 2/40 to 0/40, dish grounded (51,726) first tap, 12-task restore did NOT land as a batch, Iron Mine gathering pin claim first next unit; record commit ec55aa585 on records/2026-11-09)
  - source: ticker-1234 radar-tasks execution record 2026-11-09 1253 queue run (partial, release day, 6 tasks executed, 14 claims, points 322 to 336, stored 3/40 to 0/40, dish grounded (62,727) first tap, 6 pins inventoried unworked; record commit da81e137e on records/2026-11-09)
  - source: ticker-1704 radar-tasks execution record 2026-11-09 1717 queue run (partial, release day 1, ordinary cycle clear, 1244 pin set absent, restore lands 12 tasks about 1740, R6 successor enqueued; record commit 9806b8352 on records/2026-11-09)
---


# Radar tasks

## What this activity is

Working the radar - executing stored ordinary tasks with Quick
Execute, claiming their rewards on the days claims score, and
handling the map pin tasks that Quick Execute does not cover.
This profile was hardened on 2026-11-01 under the learning and
knowledge hardening protocol (perception-driven queue design,
section 10), as the first retrospective hardening target. Every
field below carries its evidence basis - measured in game,
dual-source web agreement, single source, or still open - and
the profile stays at proficiency learning until the open fields
in the proficiency table close.

Executions are recorded in `_records_/<date>/radar-tasks/`, one file per execution.

## Knowledge sources

- In-game execution records, 2026-10-25 to 2026-10-31 (this
  repo, `_records_` radar folders) - the primary source; where
  web sources disagree with a live in-game read, the in-game
  read governs and the disagreement is noted.
- Last War Wiki (Fandom), Radar Tasks page, accessed
  2026-11-01 - level table (refresh quantity, storage,
  maximum concurrent tasks), task type probabilities, quality
  distribution.
- LDShop, Last War Trucks and Secret Tasks guide, accessed
  2026-11-01 - refresh cycle, storage cap behaviour, stacking
  strategy for duel days 1, 3 and 5.
- GrindnStrat, Last War Radar Tasks guide, accessed
  2026-11-01 - refresh cycle, per-task expiry timers,
  cap-stops-refresh behaviour.
- Last War Handbook, VS schedule guide, and lastwar.wiki,
  Alliance Duel page, both accessed 2026-11-01 - radar task
  duel value of 10,000 points per task (base, before research
  bonuses).
- One dissenting source was rejected - a GeekVibesNation
  guide claims an 8 hour refresh; the Fandom table, LDShop
  and GrindnStrat agree on 6 hours, and the in-game restore
  line (12 tasks per restore at this level) matches the
  Fandom row for levels 12 and 13, so 6 hours stands.

## How to enter - hardened against the rotating shortcut

- The radar opens from the satellite dish icon in the base
  left icon column. That slot is a ROTATING shortcut - the
  same slot can open Secret Command Post or Intercity Trade
  instead (see `_activities_/secret-missions`). A tap on the
  slot is never proof of entry.
- Ground the icon fresh from a current screenshot in every
  unit. On a fresh 2026-10-29 screenshot the dish with its
  red badge sat at norm 62,727 and opened the radar on the
  first tap. The earlier estimate norm 54,667 opened Secret
  Command Post in the 06:44 and 11:19 units of 2026-10-29 -
  two whole units lost to a stale coordinate.
- 2026-11-02 0636: three fresh groundings in one unit
  disagreed - (55,677) did nothing, (53,575) opened Trucks,
  (53,708) opened the radar. The grounding tool twice
  mislabelled the truck icon as the dish. Ground the dish
  below the truck icon and verify the radar screen (level,
  stored count, stamina) before any work.
- PREFERRED FIRST TAP, retro action A-2026-11-08-01 (2026-11-08
  daily retro, Issue #484): norm (50,740), which opened the radar
  on the first tap at 13:53 on 2026-11-08 (1355 unit). The (54,583)
  and (54,780) points failed at 20:15 the same day (2028 unit) -
  (54,583) opened Intercity Trade, (54,780) opened BUILD - and are
  not dish points; never reuse them. If the preferred point fails,
  re-ground the dish from a fresh base screenshot.
- 2026-11-08 2335: first tap at norm (59,687), estimated from the
  fresh screenshot, missed the dish and only showed a transient
  "Achievements 8/16 Completed" tooltip. Re-grounded from a
  magnified crop of the left icon column: the satellite dish icon
  with the red "10" badge sits at pixel about 24,700 in the
  642x951 window, i.e. norm (37,736), and the second tap opened
  the radar on the first try. The profile coordinate (62,727,
  measured 2026-10-29 in a 763x1050 window) was judged stale in this
  window geometry by the 2335 unit. (CORRECTED 2026-11-09 1253: the (62,727) point opened the radar on the first tap again in the current window, so it is not stale after all; the dish still drifts per session.) The (50,740) retro preference was not tested
  in this unit; the dish drifts per session, so re-ground fresh
  from a magnified crop in every unit.
- 2026-11-09 0335: first tap at norm (55,689), estimated from the magnified crop, missed (top edge of the dish circle). Re-grounded centre norm (51,718) opened the radar on the first try. The (50,740) retro preference was not tested in this unit either; the dish drifts per session, so re-ground fresh from a magnified crop in every unit. Commented on Issue #484 by this run.
- 2026-11-09 0852: dish grounded fresh from the current base screenshot at norm (51,726) (red badge 6 on the dish) and opened the radar on the first tap - the (50,740) retro preference was not needed this unit. The camera was still panned on the Drill Ground cluster from the previous unit; the dish is a HUD icon and the tap landed cleanly without a view restore. A merely panned camera does not block the dish tap; the restore-first rule still binds when a building panel is open (see the entry precondition).
- 2026-11-09 1253: dish grounded fresh at norm (62,727) (red badge 1) and opened the radar on the first tap - the 2026-10-29 measured point works again in this window, so (62,727) is not stale after all; the dish still drifts per session, so every unit still re-grounds fresh. Commented on Issue #484 by this run: (62,727) is the newest verified first-tap point, joining (51,718) and (51,726); the (50,740) retro preference remains untested as a direct tap.
- 2026-11-09 1717: dish grounded fresh at norm (62,727) and opened the radar on the first tap again - the same point as the 1253 unit, so (62,727) is re-confirmed in this window; the dish still drifts per session, so every unit still re-grounds fresh. Commented on Issue #484 by this run.
- 2026-11-09 0636: another entry point, found by a harvest unit, not the dish - the gold circle with a blue gem above the blue truck vehicle on the base opens the world/radar map, which showed "6 task rewards can be claimed" with a Claim All button at 06:49. It is a radar shortcut, not the Armed Truck loot; the rewards were left untouched for the radar unit. A radar unit arriving through this shortcut still verifies the radar screen (level, points, stored count, stamina) before any work, same as the dish entry.
- Entry precondition, binding from the 1026 and 1439
  units: when the camera is panned onto the Drill Ground
  cluster, restore the full base view first - if a
  building panel is open, close it first (foreground the
  LastWar window and re-tap the X, click_element, or
  relaunch the app; a background-click X may not reach
  the control, and Esc is never used) - then ground the
  dish fresh from that screenshot. (2026-11-09 0852 refinement: a merely panned camera does not block the dish tap - the dish is a HUD icon and the tap at (51,726) landed cleanly with the camera still panned on the Drill Ground cluster; the restore-first rule still binds when a building panel is open.)
- ENTRY VERIFICATION, mandatory before any work - the radar
  screen is confirmed only when the screen shows radar level
  and points top left, stored tasks out of 40, and the
  stamina figure top right. If Secret Command Post, Intercity
  Trade or anything else opens, back out untouched, re-ground
  and retry; never do another activity's work from a radar
  unit (one unit, one type). Neighbouring icons that are NOT
  radar, both hit on 2026-10-29 - the magnifier (world search
  panel) and the yellow radio device (Mission screen; its
  Claim buttons belong to daily-missions).
- The radar screen shows the restore line ("N Radar Task(s)
  will be restored in HH:MM:SS"), the full restore time, the
  bottom action bar, and the task pins on the map itself.
- 2026-11-03 1913 unit: a visual-grounding point at norm
  (55,560) opened the Your Truck panel (Today's Trade Count
  3/5), not the radar - nothing was tapped there, and its
  back arrow at (56,939) returned to the base untouched. A
  tap at norm (57,715), inside the proven 52-62, 704-727
  cluster from the 0636, 1010 and 1450 units, opened the
  radar on the first tap. Entry verified by its own reads:
  Lv.13, radar points 166, stored 10/40, stamina 120.

- 2026-11-08 2028: two fresh groundings in one unit both missed
  the dish - norm (54,583) opened Intercity Trade (Today's Trade
  Count 0/5, four trucks standing, Mega Mode) and norm (54,780)
  opened the BUILD menu (Economy tab). The grounding tool
  mislabelled the truck slot as the dish at 20:17 and the
  crop-measured point landed on the Build/hammer icon at 20:24.
  Neither point is a dish point. The next point to try is norm
  (50,740), which opened the radar on the first tap at 13:53
  the same day (1355 unit).
- 2026-11-08 2028: the Age of Oil research tree back arrow does
  not respond to background clicks at all - two taps on the
  arrow at (109,894) and the re-grounded centre (131,898)
  produced no change, and the control channel returned explicit
  guidance that background clicks do not reach some controls and
  to use click_element with the control's visible label, or the
  keyboard, instead. Return and Esc are never used on this app.
  Back out of the tree with click_element on the arrow if the
  catalog names it, or relaunch the app (state is server-side;
  prior units relaunched after crashes with no loss).
## Mechanism

- Radar level - Lv.13 since the level-up in the 2026-10-30
  06:23 unit (Lv.12 before). Storage cap 40 at both levels
  (measured; Fandom agrees).
- Refresh - the restore line restores 12 tasks per cycle at
  this level (measured repeatedly, e.g. "12 Radar Task(s)
  will be restored in 04:05:40" at the 2026-10-29 18:47
  close). Cycle length about 6 hours (dual source - Fandom
  level table and LDShop; consistent with stored counts
  rising between units). Whether the restore lands as one
  batch or trickles is not yet settled - see open questions.
- Cap behaviour - when storage hits the cap, the refresh
  timer stops and no new tasks generate (dual source -
  LDShop and GrindnStrat). Stack discipline therefore keeps
  headroom - leave stored at or below 39 of 40 whenever a
  restore cycle will land before the next unit.
- Task expiry - uncompleted tasks carry their own timers
  and disappear when the timer runs out (GrindnStrat; the
  in-game pin cards show countdowns, e.g. about 7 hours 56
  minutes on the 2026-10-25 story pin). Completed but
  unclaimed tasks also expire if never claimed (GrindnStrat)
  - on release days, claim before expiry, do not admire the
  stack.
- Task types (Fandom, single source, not yet verified
  in game) - guaranteed daily one Eliminate Rebels and one
  Defeat Doom Elites; the random pool is Ally Assistance
  30 percent, Zombie Sampling 30 percent, Geological
  Sampling 20 percent, Rare Resource Mining 20 percent,
  each with a 0.25 percent chance to upgrade to a Treasure
  Digging task. Qualities run Common to Legendary with
  type-specific distributions.
- Radar points counter - claiming a task adds 1 radar point
  (measured many times, e.g. 39 claims moved 2,950 to 2,989
  on 2026-10-29). (2026-11-09 1253 re-confirmation: 14 claims moved 322 to 336, one per claim.) After the Lv.13 level-up the counter
  displayed small numbers again (29 on 2026-10-31 morning
  against 2,989 the day before) - an apparent per-level
  progress reset, observed once, mechanism unverified. The
  radar points counter is NOT the duel score; see Scoring.

## Stamina

- Cap 120 (measured to 2026-11-03) SUPERSEDED 2026-11-04: the 0334 unit entered reading stamina 156 and spent to 136 on Quick Execute alone, so the cap is at least 156 and the old 120 figure is not a cap. No new cap value is claimed - the mechanism is unverified, so do not quote 156 as the cap. Regenerating 1 point every 300 seconds (measured, not re-measured here).
- Ordinary task through Quick Execute - 10 stamina each
  (measured across dozens of batches).
- Pin task march costs vary by type (measured) - story pin
  march 5, Doom Walker rally 20, gathering pins 0.
- Free stamina claim - the Regain Stamina panel offers 75
  stamina free, cooldown 4 hours, twice a day (measured -
  Remaining Today reads 2 of 2 down to 0 of 2; taken in the
  2026-10-29 02:24 and 18:47 units). Always take the free
  claim first when stamina blocks execution.
- Paid option - Buy 100 stamina for 300 rubies. NEVER use
  it (red line).
- Stamina items (10 and 50) exist in inventory in the
  hundreds (measured counts in the Regain panel; 2026-11-08 2335:
  10-stamina x641, 50-stamina x665). Use only
  under the standing stamina rules for scoring pushes -
  Free Claim first, then items, never rubies.

## Quick Execute - coverage and exceptions

Coverage (measured in game; web sources do not document
Quick Execute's exact scope, so this section rests on the
execution records):

- COVERS - ordinary stored tasks, executed in batches. The
  bottom bar states how many tasks can be completed and the
  stamina required. After the marches, the bar flips to
  Claim All with the count of rewards waiting.
- DOES NOT COVER - every map pin task (story pins, Doom
  Legion base, Doom Walker, gathering mines), finished-task
  pins waiting on the map, and anything resolved on the
  world map. A radar clear is never proven by the bottom bar
  alone; the pin scan decides.
- Behaviour trap, measured across 2026-10-31 - the bottom
  bar presents ONE offer at a time. In the 06:12, 14:15,
  18:38 and 22:06 units it presented Claim All (rewards
  waiting) and no Quick Execute, so the stored tasks could
  not be executed at all; that is the structural reason the
  stack day stalled - the 02:39 unit executed 6 tasks, and
  most later units were locked out, with stored tasks
  sitting at 21 of 40 unexecuted by 14:15. But the block is
  not absolute - the 10:40 unit was presented a Quick
  Execute offer (1 task) despite 7 rewards pending from the
  06:12 close, and ran it. What selects which offer the bar
  presents is not understood (open question); never assume
  either way - read the bar that is actually shown.
- Bottom-bar hitbox, measured 2026-11-03 1450: taps at norm y
  890, 905, 910 and 912 on the Claim All button did NOTHING
  (five taps across two attempts, including a double-click);
  the taps landed on the map/label area above the button's
  true hitbox. A tap at norm (498,925) opened the button.
  Next units: tap the bottom-bar buttons at y 925, not at
  their visual centre (~910). CORRECTION 2026-11-03 1913:
  the y-925 lesson does NOT transfer to every window
  geometry - in the 1913 window the bottom-bar buttons
  responded at norm (500,952), confirmed by three Quick
  Execute and three Claim All taps at that point. The
  grounded point governs in each window; never carry a
  y value across windows unverified.
- With too little stamina, tapping Quick Execute opens the
  Regain Stamina panel instead of failing - use the free
  claim there and continue.

## Map pins - taxonomy and handling protocol

Pins are not one thing. Classes proven in game:

- Finished-task pins - a completed ordinary task standing on
  the map with a red dot. Tapping it claims INSTANTLY - a
  CONGRATULATIONS popup, no card, no chance to back out
  (measured twice on 2026-10-29, a blue person pin at 02:24
  and a purple skull pin at 14:52; each paid at once and
  added 1 radar point). This is how part of the stacked
  rewards present on the map.
- Story pins - a purple question mark pin, NOT covered by
  Quick Execute. Full verified flow under Special pin tasks
  below (A Distressed Survivor, 2026-10-25).
- Doom Legion base pin - jumps to a legion base on the world
  map; attacking destroyed it outright (loot about food
  1.4M, iron 1.4M, coin 0.9M to 1.7M as read).
- Doom Walker pin - a world boss rally (cost 20 stamina,
  rally about 7 minutes here). A launch is real only when
  stamina drops by 20 AND the march timer appears - the
  first launch on 2026-10-25 was a silent no-op.
- Gathering pins - purple mine pins (Diamond Mine, Rare Gold
  Mine, 2026-10-26). Card names the spot, rewards and a
  despawn timer of about 3 hours; Go, advance any story
  dialog, tap the pickaxe button, a full squad gathers at
  no stamina cost. The pin reward is claimed at the radar
  afterwards (Claim All or tapping the finished pin); the
  gathered yield itself lands in the HUD on squad return.
- Unidentified standing pins - an orange arrow pin, a purple
  axe pin and an orange axe pin stood on the map through the
  2026-10-29 release units, plus a portrait pin on 2026-10-29
  22:21, none ever tapped, type unknown. Do not guess their
  class from colour; they head the open questions.

Handling by posture (binding):

- RELEASE posture - every pin is worked to a closing read
  in the unit: tapped and completed, claimed, or identified
  with the reason it is left. "Pins left unattempted" is a
  partial, never a done - the 2026-10-29 18:47 and 22:21
  units both closed partial on exactly this, and the pins
  were still standing the next day.
- STACK posture - do NOT tap pins. A finished-task pin pays
  instantly on tap and leaks the claim onto a non-scoring
  day. Instead the unit records a pin inventory (class if
  known, position, red dot or not) as part of its closing
  read, so the release-day unit inherits a checklist rather
  than a surprise.
- Either posture - the pin scan is part of the closing read
  of every radar unit. No scan, no done.

## Special pin tasks - verified flow (A Distressed Survivor)

1. Tap the pin on the radar map. A bottom card opens with
   the task title, a countdown (about 7 hours 56 minutes
   remaining), the reward area and a Go button. Rewards may
   be hidden behind a state line - here "Break the ice to
   view rewards".
2. Tap Go. The view jumps to the task location on the world
   map and the card shows the situation state - here Thawing
   Soon with a timer, a snowflake bar at 1,000 of 1,000, and
   one large round contextual action button (a hammer here).
3. Tap the contextual button. A march panel opens - squad,
   power versus Unknown, a match rating, march time and a
   stamina cost (5 here). Tap March. The squad marches
   (March Queues 1 of 4, back to 0 of 4 on arrival) and the
   situation resolves.
4. Go back to the radar screen and tap the same pin again.
   The card has changed - the reward list is now revealed
   (here a survivor times 1, a paw print item times 200 and
   black rock times 207.3K).
5. Tap Go again. On the world map the card is simplified and
   the round button is now a green magnifier.
6. Tap the magnifier. A story conversation opens with a
   large character portrait. Keep tapping the bottom of the
   dialog to advance it to the end - complete the
   conversation with clicks only. If a chat screen opens by
   an extra tap, the Back Arrow at the bottom left exits it.
7. Return to the radar screen. The bottom bar reads "1 task
   rewards can be claimed" with a Claim All button. Claim
   All pays the revealed rewards and adds 1 radar point.
   The pin and its red dot disappear.

## Scoring - duel days

- Posture follows the duel day (_tools_/duel.py) - stack on
  even days (complete, do not claim), release on odd days
  1, 3 and 5 (claims score). Radar claims score at the
  moment of claiming, not at completion - the whole stack
  and release rhythm rests on this (owner-taught rule,
  corroborated by LDShop and the tkw FAQ page, both accessed
  2026-11-01 - save radar tasks for days 1, 3 and 5).
- Per-task duel value - the Handbook and lastwar.wiki both
  list Complete 1 Radar Task at 10,000 points (base, before
  Alliance Duel research bonuses). The in-game VS panel on
  this account displays plus 30,000 per task (recorded in
  _tools_/duel_schedule.json). The in-game value governs
  planning; the gap is presumed to be duel research bonus
  but is NOT verified - the delta test (read duel score,
  claim one batch, read again) is still owed and heads the
  open questions.
- Do not read the radar points counter as duel score - it
  moves 1 point per claim and says nothing about the duel.
- Live-dialog contradiction, 2026-11-03 1450, RESOLVED
  2026-11-03 by PR 237 (Issue #235, tooling): the 1450 unit
  ran on duel day 2, Base Expansion, radar posture stack -
  not day 3 release. The tool's day-3 reading was a clock
  bug, not a stale schedule: duel.py read a naive UTC
  clock, which had already crossed the 19:00 boundary at
  14:03 PT and rolled to day 3 eight hours early. The
  corrected tool returns day 2 stack for the 1450 instant,
  matching the live TIPS dialog verbatim, and the schedule
  in tools/duel_schedule.json is NOT stale - that
  hypothesis is retired. The unit's window stamp (duel day
  2, radar stack) was right and the live tool reading was
  wrong, reversing the 1532 lesson that the live posture
  governs over the stamp: when tool and stamp disagree,
  check the tool's clock basis and the VS panel before
  trusting either. Tapping Claim All opened
  a TIPS dialog reading verbatim: "Completing Radar Tasks
  today will not grant Alliance Duel points, and you are about
  to claim 10 radar task rewards at once. Continue?" This
  contradicts the tool's gate text that radar claims score
  again today. The unit claimed anyway (resources certain,
  holding the stack risks task expiry, release standard
  governs). That either/or is now settled by PR 237 (see
  the head of this bullet): the schedule was NOT stale,
  the tool's clock was wrong, and the dialog meant what
  it said. The next radar release
  decision needs the settled reading, ideally from the VS
  panel itself. No duel score read was taken in the 1450
  unit, so the delta test is still owed. Verification still
  owed after the merge: the next radar unit that consults
  duel.py must report the PT day. ANSWERED IN PART
  2026-11-03 1913 (first radar unit after the PR 243
  merge): the unit consulted duel.py at entry (day 3,
  Age of Science, release) and NO TIPS dialog appeared
  on any of its three post-rollover Claim All taps, so
  tool, day and dialog agree after the fix - but no VS
  panel read was taken, so no duel-points figure is
  claimed and the delta test is still owed. The 19:00 PT
  boundary in this bullet is superseded by PR 243: the
  boundary is absolute 02:00 UTC, about 18:00 PST now
  (19:00 PDT before the DST end), and day 3 release runs
  from the about-18:00 rollover, not from 19:00 PT.
  Issue #235 closure belongs to the daily retro, not
  to this fold.

## Stack day completion standard

A stack-day radar unit is done only when ALL of these hold:

- The radar screen was entered and verified (level, stored
  count, stamina read on the radar screen itself).
- Every executable ordinary task was executed - Quick
  Execute batches run until no offer remains or the stamina
  floor under the standing rules is hit, free claim taken
  first when stamina blocks.
- Closing reads are recorded - stored count, pending reward
  count on the Claim All bar, stamina, and the pin
  inventory (untapped, per the stack handling rule).
- If the bar presents Claim All and no Quick Execute (the
  2026-10-31 trap - rewards left pending by an earlier unit
  can lock later units out of execution), the unit records
  that blocker by name with the pending count - not a
  generic partial - and the block is carried into the next
  unit's opening read, so the stack is planned around it
  instead of rediscovered hourly.

## Release day completion standard

A release-day radar unit is done only when ALL of these hold:

- Claim All worked until the bar disappears; Quick Execute
  batches interleaved until stored reads 0 of 40 or only
  restoring tasks remain (the 2026-10-29 18:47 shape - 39
  claimed, 12 executed, stored 0 of 40).
- Every map pin has a closing read per the release handling
  rule - completed, claimed, or identified with a reason.
- Closing reads recorded - stored count, radar points,
  stamina, restore line - and, on a scoring day, the duel
  score before and after where the panel allows the read
  (this is also how the pending delta test gets done).

## Red lines

- Never tap Buy in the Regain Stamina panel (100 stamina
  for 300 rubies).
- Never tap map pins and never tap Claim All on a stack
  posture day.
- Never claim another activity's rewards from a radar unit
  (the Mission screen belongs to daily-missions).

## Red dots and red badges - the owner rule

- A red badge number on a tab or icon means that many tasks
  or claims are ready to do there (owner, 2026-10-25).
- A red dot on a radar map pin means that pin is clickable
  and its task can be done now (owner, 2026-10-25). Do not
  treat a pin with a red dot as decoration - open it (on a
  release day; on a stack day, inventory it instead - see
  the pin handling protocol).

## Failure history this profile is hardened against

- 2026-10-29 06:44 and 11:19 - two stack-day units never
  entered the radar screen; the stale dish coordinate opened
  Secret Command Post both times and the units closed
  without a single radar read.
- 2026-10-29 18:47 and 22:21 - release-day units claimed 39
  tasks and cleared ordinary tasks to 0 of 40, then left
  three standing pins (orange arrow, purple axe, orange
  axe) untapped with "falls to the next tick"; the pins
  were never closed by any later unit.
- 2026-10-25 - the special story pin (A Distressed
  Survivor) was invisible to Quick Execute and surfaced
  only when the owner pointed at the still-standing pin;
  it had no completion standard until its flow was worked
  and written down the same evening.
- 2026-10-31 - stack day closed with stored tasks at
  21 of 40 unexecuted; the bottom bar presented Claim All
  instead of Quick Execute in four units, locking out
  execution, and the block was treated as weather instead
  of a named blocker with a plan.

## Proficiency by field

- Entry and entry verification - proficient (measured,
  including the failure and its correction on 2026-10-29).
- Storage cap 40 - proficient (measured; Fandom agrees).
- Ordinary task stamina cost 10 - proficient (measured).
- Free stamina claim terms - proficient (measured).
- Refresh quantity 12 per cycle - proficient (measured).
- Refresh cycle length 6 hours - supported (dual source;
  no direct in-game timing measurement yet).
- Cap stops refresh - supported (dual source; not yet
  measured in game on this account).
- Quick Execute coverage of ordinary tasks - supported
  (measured repeatedly; web sources silent on exact scope).
- Bottom bar single-offer behaviour (Claim All presented
  instead of Quick Execute) - supported as behaviour
  (measured four times on 2026-10-31, with one counter-
  observation the same day); the rule that selects the
  offer is open.
- Pin taxonomy - learning (four classes measured; the
  standing arrow and axe pins are unidentified).
- Task types and probabilities - learning (single source,
  Fandom; guaranteed daily pair unverified in game).
- Duel scoring per task - learning (dual source base value
  10,000 against an in-game display of 30,000; delta test
  owed).
- Radar points counter behaviour across level-up - learning
  (one observation).

Profile level stays learning - the weakest key fields
(scoring value, pin taxonomy, Quick Execute re-offer rule)
are still open, per the protocol.

## What the 2026-11-01 1122 unit added

- Stack posture held throughout, status done
  (ticker-1114, session about 11:16 to 11:22, duel day 7
  off-day settlement, radar posture stack per
  tools/duel.py): tasks executed, nothing claimed, no
  map pin tapped. This unit was missed by the 1132
  organizer run's input list and is folded here, so the
  watermark gap is closed, not carried.
- Entry verified on the radar screen itself: satellite
  dish icon at norm 62,727 opened the radar on the first
  tap. Lv.13, radar points 45, stored 33 of 40, stamina
  135, restore line 12 tasks in 03:29:29.
- Quick Execute: the bottom bar offered 5 tasks for 50
  stamina and no Claim All at entry, so the batch ran.
  Stamina 135 to 85, exactly 5 tasks at 10 stamina each.
  Radar points stayed 45, confirming nothing was
  claimed.
- Closing reads: stored 33 of 40 (unchanged by execution;
  the executed tasks moved to the pending-reward count),
  restore 12 tasks in 03:28:04, stamina 85, radar points
  45.
- Named blocker carried forward: after the batch the bar
  flipped to Claim All only, 11 task rewards pending (6
  already pending at entry plus the 5 just executed),
  with no further Quick Execute offer. Claim All was NOT
  tapped, per the stack-day red line. The next radar unit
  inherits this blocker and the pending count of 11, per
  the stack-day completion standard's named-blocker rule.
- Pin inventory, untapped per the stack handling rule,
  all red-dotted: grey handshake pin, green handshake
  pin, and orange skull pin on the radar map. No pin was
  tapped, so no claim leaked onto this non-scoring day.
- Headroom warning with a deadline: stored 33 of 40 sits
  below the 39 cap guard, but the 12-task restore landing
  in about 3.5 hours - about 14:50 - would overshoot the
  40 cap if no unit executes or claims before then. A
  later unit must act before the restore lands; on a
  stack day that action is execution, not a claim, and
  execution is currently locked behind the Claim All
  only bar above, so the next radar unit faces the
  blocker and the deadline together.


## What the 2026-11-01 1629 unit added

- Unit radar-2026-11-01-1403 by ticker-1604, session
  about 16:19 to 16:29, status partial. Duel day 7,
  off-day settlement, radar posture stack. Nothing was
  executed and nothing was claimed. The tracker is
  untouched, so the next tick re-produces this regular.
- Entry failure mode: radar entry was attempted from
  a fresh base screenshot. The dish icon was grounded
  at 53,688 on that screenshot and tapped. The
  resulting screen was not the radar screen - it showed
  base buildings and production bubbles in a panned
  view, with no radar level, no stored count, no
  stamina figure and no bottom action bar. Entry
  verification therefore failed. No Secret Command
  Post and no Intercity Trade opened, and no other
  activity was worked from this unit. A dish tap that
  lands on a panned base view is a failed entry, not a
  radar read; the entry must be re-grounded from a
  verified base view, not retried blind.
- Recovery cut short, and correctly stopped: the
  computer session dropped twice during this pass and
  had to be restarted, and a visual grounding call for
  the recovery controls timed out after three minutes.
  With the pass budget nearly spent, no further
  navigation tap was attempted, because a blind tap on
  an ungrounded control risked opening another
  activity. No map pin was tapped and no Claim All was
  tapped, so the stack posture held with no claim
  leaked onto this non-scoring day.
- First read owed by the next radar unit: the stored
  count. The opening state carried in (1122 unit,
  11:22 local) was entry verified Lv.13, radar points
  45, stored 33 of 40, stamina 85, restore 12 tasks in
  03:29:29, with the bar flipped to Claim All only and
  11 task rewards pending. The 12-task restore landing
  about 14:45 local would have pushed stored toward
  the 40 cap. This unit obtained no fresh stored count,
  so whether stored now sits at the cap is unverified
  and is the first read the next unit must make.

## What the 2026-11-01 1904 unit added

- Unit radar-2026-11-01-1803 by ticker-1904, session about
  19:05 to 19:35, status partial. The unit window text still
  read "duel day 7 - radar stack" (stamped at production
  before the 19:00 reset); the live posture from
  tools/duel.py governs, so this unit ran as a release
  unit: duel day 1, Radar Training, radar posture release,
  day ends 2026-11-02 19:00 local, more than 5 minutes
  after the 19:00 roll, past the dead window named in the
  duel gate.
- Entry verified on the first tap at norm 62,727 (the
  2026-10-29 measured dish point): Lv.13, radar points 66,
  stored 19 of 40, stamina 145, restore line "Fully
  restore at 11-2 03:31:43 local time" at entry. Later
  reads in the same unit showed 15:31:43; the hour figure
  is recorded as displayed and is unverified - neither
  figure is adopted over the other here.
- Batch 1: Quick Execute 4 tasks, stamina 145 to 105. Bar
  flipped to Claim All, 10 task rewards. Claim All claimed
  10, radar points 66 to 76. Rewards: chest times 25, radar
  item 100, EXP 14.1M, drone item 3.2K, blue triangle 450,
  iron 3.9M, food 2.3M, coin 2.0M.
- Batch 2: Quick Execute 3 tasks, stamina 105 to 75,
  stored 9 of 40. Bar flipped to Claim All, 8 task rewards.
  Claim All claimed 8, radar points 76 to 84. Rewards:
  radar item 70, EXP 14.2M, drone item 3.2K, speedup 5m
  times 7, speedup 1m times 85, iron 4.4M, food 3.6M, coin
  1.3M.
- Batch 3: Quick Execute 4 tasks, stamina 75 to 35, stored
  1 of 40. Bar flipped to Claim All, 7 task rewards. Claim
  All claimed 7, radar points 84 to 91. Rewards: radar item
  70, EXP 13.2M, drone item 2.4K, iron 3.3M, food 2.4M, coin
  1.3M.
- Totals in this unit: 11 tasks executed, 25 rewards
  claimed, radar points 66 to 91, stamina 145 to 35, coin
  claimed across the three popups 2.0M plus 1.3M plus 1.3M
  equals 4.6M (popup figures, not HUD totals).
- Contradiction resolved in favour of the newest live
  read: the prior radar unit 1629 never entered the radar
  screen, so its reads were carried from unit 1122 (stored
  33 of 40, stamina 85, 11 task rewards pending). Those
  carried figures are superseded by this unit's live
  re-read (stored 19 of 40 at entry, 0 of 40 at close,
  stamina 145 to 35). The stored-count first read the 1629
  unit owed is now answered: 19 of 40 at entry.
- Closing state (live reads, same unit): Radar Lv.13,
  radar points 91, stored 0 of 40, stamina 35, restore line
  "12 Radar Task(s) will be restored in 02:16:05", fully
  restore 11-2 15:31:43 local time as displayed.
- Offer-versus-stored mismatch, carried as an open rule:
  the bottom bar offers 1 more task for 10 stamina while
  stored reads 0 of 40, so the offer count and the stored
  count do not move together. The next unit must read the
  bar it is actually shown, not infer it from stored.
- Pin inventory, untapped in this unit: purple
  question-mark story pin top centre, purple skull pin
  centre, orange axe pin lower left, blue skull pin lower
  centre, plus one alliance portrait pin ([AP3x]Black
  Death) that is not a task. The green and blue skull pins
  with red dots seen at entry are gone after the claims.
  Per the release standard, pins left unattempted make
  this unit partial, never done; the next radar unit must
  work the pins to a closing read (completed, claimed, or
  identified with a reason) and run the remaining 1-task
  offer.
- Duel delta test still owed: the VS panel was not opened
  in this unit, so no duel score before and after was
  read. The 25 claims on a scoring day are the batch the
  delta test should measure against (see alliance-duel
  1.8.0).
- Entry method note: a visual grounding call during entry
  timed out after 3 minutes; entry then succeeded on the
  documented coordinate, so no method change was needed.
- No diamonds or money spent, no Buy tapped, no map pin
  tapped, no other activity worked from this unit. Tracker
  untouched for partial, per the queue rules.



## What the 2026-11-01 2319 unit added

- Unit radar-2026-11-01-2203 by ticker-2304, session about
  23:06 to 23:19, status partial. Live duel posture from
  tools/duel.py at entry: duel day 1, Radar Training, radar
  posture release, day ends 2026-11-02 19:00 local. Release
  posture governs, so this unit claimed everything claimable
  and worked pins toward a closing read.
- Entry lesson, rotating-shortcut trap again: the app opened
  on Secret Command Post, not the radar. It was backed out
  untouched with two back-arrow taps, then the dish icon
  grounded fresh on the base screenshot at norm 55,699
  entered radar on the first tap: Lv.13, radar points 91,
  stored 6 of 40, stamina 82, restore line "12 Radar
  Task(s) will be restored in 04:22:08".
- Live re-read supersedes the 1904 close: the 1904 unit
  closed at stored 0 of 40 and stamina 35, but this unit's
  live entry read is stored 6 of 40 and stamina 82
  (restore accumulation between the units, not a
  correction of the 1904 close). The standing rule holds:
  re-read live, never trust a carried figure.
- Batch 1: Quick Execute 3 tasks, stamina 82 to 52. Bar
  flipped to Claim All, 5 task rewards. Claim All claimed
  5, radar points 91 to 96. Rewards: radar item 50, EXP
  5.6M, blue triangle 540, iron 1.1M, food 1.1M, coin
  1.3M, Lv1 chest 1.
- Batch 2: Quick Execute 1 task, stamina 52 to 42. Bar
  flipped to Claim All, 4 task rewards. Claim All claimed
  4, radar points 96 to 100. Rewards: radar item 40, EXP
  7.2M, drone item 2.4K, iron 2.2M, food 1.2M, coin
  668.4K. One control-channel error mid-popup ("target
  app exited") proved transient: the app was still open
  with the popup intact, and the dismiss re-sent on a
  fresh observation succeeded with no state lost.
- Batch 3: Claim All 1 task reward, radar points 100 to
  101. Rewards: radar item 10, EXP 1.5M, drone item 800,
  iron 789.6K, coin 127.2K. Bottom bar then offered
  nothing further.
- Totals in this unit: 4 tasks executed, 10 rewards
  claimed, radar points 91 to 101, coin claimed across
  the three popups 1.3M plus 668.4K plus 127.2K equals
  about 2.10M (popup figures, not HUD totals).
- Pin work, Doom Walker rally launched: the purple skull
  pin with a red dot opened a "Kill a Doom Walker" card
  (Kill 1 Doom Walker regardless of level, rewards food
  975.6K, iron 975.6K, coin 622.8K, radar item 300, plus
  a gold ticket item, pin timer 00:19:45). Go jumped to
  a Lv.160 Doom Walker on the world map (Suggested Power
  21,454,000, stamina cost 20). Rally panel: Squad 1 at
  25.12M versus 21.45M, Evenly Matched, Unit Count 2,231
  of 2,231, Rally Time 1min checked. Rally tapped and
  verified real: stamina 23 at launch, March Queues 1
  of 4, Rallying 00:00:55 remaining at the closing
  screenshot. The rally departs after its 1 minute
  assembly and then marches 340 km; its kill and claim
  fall to the next radar unit, not this one.
- Pin inventory at close (radar screen, after the
  claims): purple question-mark story pin top centre,
  orange axe pin right, orange axe pin lower left (two
  axe pins lower left in total), portrait pin left
  middle, blue skull pin lower centre without a red
  dot. The blue skull and grey skull pins with red dots
  seen at entry are no longer standing after the claims;
  the Doom Walker pin is replaced by the live rally on
  the world map. Per the release standard, pins left
  unattempted make this unit partial, never done.
- Closing state (live reads, same unit): Radar Lv.13,
  radar points 101, stored 0 of 40, stamina 23 at rally
  launch, restore line "12 Radar Task(s) will be
  restored in 04:19:37" at the last radar-screen read.
- Next radar unit, first actions in order: check the
  Doom Walker rally result and claim its pin reward if
  the kill landed; then work the story pin, the orange
  axe pins, the portrait pin and the blue skull pin to a
  closing read each; then run any new Quick Execute or
  Claim All offer the bar shows. Duel delta test still
  owed: the VS panel was not opened in this unit.
- No diamonds or money spent, no Buy tapped, no other
  activity worked from this unit. No map pin was tapped
  except the Doom Walker pin above. Tracker untouched
  for partial, per the queue rules.

## What the 2026-11-02 0226 unit added - entry corrections, 2 claims, Doom Walker rally still unverified, pins unattempted

- Unit radar-2026-11-02-0203 by ticker-0204, session
  about 02:08 to 02:26, status partial. Live duel posture
  from tools/duel.py at entry: duel day 1, Radar
  Training, radar posture release, day ends 2026-11-02
  19:00 local. Release posture governs.
- Entry, three corrections, all recorded for the next
  unit: the game was open at the Secret Command Post
  from the preceding treasures unit. The back arrow's
  true centre, measured on an enlarged crop, is norm
  (132,948); the first two taps at (94,944) hit the small
  avatar badge overlapping the button's left edge and
  changed nothing - do not repeat the 94,944 point
  (R2 pivot: re-ground, then switch variant). The tap
  at (132,948) exited the post to the base.
- The base view first rendered without the HUD (no top
  resource bar, no right column) and showed no shortcut
  column; a tap on the in-base dish structure restored
  the full HUD. The shortcut column is only groundable
  on the full-HUD base view - the no-HUD frame is not a
  usable grounding screenshot. The dish icon was then
  grounded fresh on the full-HUD strip: white satellite
  dish on a dark circle with a red badge 2, at norm
  (58,736) on the left edge. One tap opened the radar
  on the first try. Visual-grounding points offered
  earlier in this unit were wrong - one landed on the
  train icon, one on the in-base dish structure - and
  were not used blindly; re-ground from the live
  screenshot before tapping a suggested point.
- Opening state (live, radar screen verified): Radar
  Lv.13, radar points 101, stored 0/40, stamina 60.
  Restore line: 12 Radar Task(s) will be restored in
  01:09:44 at the claim popup read, about 03:35 local
  for the next restore. Bottom bar at entry: 2 task
  rewards can be claimed, with a Claim All button. No
  Quick Execute offer: stored reads 0/40, so no
  ordinary task was executable.
- Pin inventory at entry (from the entry screenshot):
  purple skull pin with red dot (top left), purple
  question-mark story pin with red dot (top centre),
  orange axe pin (right), portrait pin (left middle),
  orange axe pin (lower left), orange axe pin (lower
  centre-left), blue skull pin with red dot (lower
  centre). Seven pins standing.
- Claim All claimed the 2 pending rewards. Radar points
  101 to 103. CONGRATULATIONS popup read live: gold paw
  item x3, radar item x600, drone item x1.6K, iron 1.8M,
  food 1.8M, coin 1.2M (item names for the first three
  tiles by icon; the last three tiles are the labelled
  resource rows). Popup dismissed by a tap at norm
  (500,850). No stamina was spent; stamina read 61 at
  the popup (regeneration tick during the unit).
- Non-verification, stated plainly: the 2 claimed
  rewards do NOT match the Doom Walker rally card
  figures from the 2026-11-01 2319 unit (food 975.6K,
  iron 975.6K, coin 622.8K, radar item 300, gold ticket),
  so the rally kill/claim is NOT verified by this claim
  and remains open. Do not read this claim as the rally
  reward.
- Closing state (live reads, same unit): Radar Lv.13,
  radar points 103, stored 0/40, stamina 61, restore
  line 01:09:44 remaining at the popup read. No pin was
  tapped in this unit; all seven entry pins stand
  unattempted. Per the release standard, pins left
  unattempted make this unit partial, never done.
  Tracker untouched for partial, per the queue rules.
- Next radar unit, first actions in order, from the unit
  record: check the Doom Walker rally result from the
  2026-11-01 2319 launch and claim its pin reward if
  the kill landed (still unverified); work each standing
  pin to a closing read (the story pin, the purple skull
  pin, the three orange axe pins, the portrait pin and
  the blue skull pin); run any new Quick Execute or
  Claim All offer the bar shows (the next 12-task
  restore lands about 03:35); duel delta test still
  owed - read the VS panel duel score before and after
  one claim batch.
- The computer-use session dropped twice mid-unit
  (cc-130, then cc-131); each time a new session was
  started and work resumed with no state lost.
- No diamonds or money spent, no Buy tapped, no other
  activity worked from this unit.
  Evidence in `_records_/2026-11-02/radar-tasks/0226-queue-run.md`.

## What the 2026-11-02 0636 unit added - 12 claims, Doom Legion pin left on an ambiguous card, duel delta still owed

- Unit radar-2026-11-02-0603 by ticker-0634, session about
  06:35 to 06:43, status partial. Live duel posture from
  tools/duel.py at entry: duel day 1, Radar Training,
  radar posture release. Release posture governs.
- Entry struggle, recorded for the next unit: the dish icon
  was grounded fresh three times with disagreeing points. A
  tap at norm 55,677 did nothing. A tap at norm 53,575
  opened the Trucks screen instead (plunder count read 2/4
  in passing, NOT acted on - one unit, one type). Backed out
  untouched via the bottom-left back arrow. The tap that
  opened the radar was norm 53,708 on the current
  screenshot. The grounding tool twice mislabelled the truck
  icon as the dish. Next unit: ground the dish below the
  truck icon and verify the radar screen (level, stored
  count, stamina) before any work, as the profile requires.
  Prior dish points (62,727 on 2026-10-29, 58,736 on
  2026-11-02 0226) do not transfer across framings.
- Entry reads, live on the verified radar screen: Lv.13,
  radar points 103, stored 4/40, stamina 112. Restore line
  at entry: fully restore at 11-2 21:31:43 local time.
- Quick Execute offered 5 tasks for 50 stamina. Executed:
  stamina 112 to 62. Bar then offered Claim All for 8
  rewards. Claim All batch 1 popup: spiral icon 80, EXP
  9.7M, triangle 855, iron 1.9M, food 1.9M, coin 2.2M, Lv.1
  chest x2. Radar points 103 to 111.
- Bar then offered 1 more task for 10 stamina. Executed:
  stamina 62 to 52. Bar then offered Claim All for 4
  rewards. Claim All batch 2 popup: spiral icon 40, EXP
  5.3M, chip item 1.6K, triangle 183, iron 316.8K, food
  2.2M, coin 717.6K. Radar points 111 to 115.
- Closing reads: stored 0/40, radar points 115, stamina 53
  (one point regenerated), restore line "12 Radar Task(s)
  will be restored in 02:50:07", no bottom-bar offer left.
  Ordinary work is complete; 12 claims total (8 plus 4).
  The entry full-restore time (21:31:43) and the closing
  next-12 restore line (02:50:07) are different quantities
  and are not conflated here; the restore-shape question
  below stays open.
- Map pins, closing inventory, all red-dotted: portrait pin,
  left-mid, norm about 304,468 - TAPPED. Card: "Eliminate
  the Doom Legion - Destroy Doom Legion's base!", rewards
  food 11.2M, iron 11.2M, coin 7.4M, radar points 300, one
  chip item, countdown 00:27:23 at tap time (expiry about
  07:09 local). Go jumped to the world map and opened a
  card showing Power 6,937,000, Kills 0, Alliance [AP3x]The
  Apex, rewards 21.3M, 21.3M, 13.6M. The alliance tag on
  the card made the target ambiguous, so the attack button
  was NOT tapped. Closing the card produced the toast
  "Other commanders are currently conducting radar tasks
  here. Please wait or change location." The pin is
  therefore identified but left for a contested location
  plus an ambiguous card - the next unit must re-read the
  card before any attack, and must not attack an alliance
  member's base. The about 07:09 expiry has passed by the
  next unit's window, so the next unit verifies whether
  the pin still stands rather than assuming it does.
- Orange arrow pin, right side, norm about 810,410 -
  unattempted, class unknown (one of the standing arrow
  pins open since 2026-10-29). Orange arrow pin, lower
  left, norm about 296,673 - unattempted, class unknown.
  Per the release standard, pins left unattempted make
  this unit partial, never done. Tracker untouched.
- Duel score before and after was NOT read (VS panel not
  visited); the radar delta test is still owed.
- No diamonds or money spent, no price tag tapped, no Buy
  in any panel, no other activity's rewards claimed. The
  Trucks screen was entered by a mis-grounded tap and left
  untouched.
  Evidence in `_records_/2026-11-02/radar-tasks/0636-queue-run.md`.

## What the 2026-11-02 1026 unit added

- Unit radar-2026-11-02-1003 by ticker-1004, session about
  10:20 to 10:25, status partial, tracker untouched.
  Duel day 1, Radar Training, release posture confirmed
  by tools/duel.py (radar_posture release) before the unit
  started, but the radar screen was never entered, so
  this unit executed and claimed nothing. Evidence in
  `_records_/2026-11-02/radar-tasks/1026-queue-run.md`.
- Entry state: the game was left by the donations unit
  with the base camera panned onto the Drill Ground
  cluster (Drill Ground Lv.27, three floating round
  buttons at the bottom right). The left icon column with
  the radar dish is not visible in this framing. A fresh
  screenshot was taken and a visual grounding call for
  the satellite dish icon was attempted, but the call
  timed out after 180 seconds, consuming the rest of the
  pass budget. No tap was made on any ungrounded icon,
  and no other activity's work was done from this unit.
- Entry precondition added: when the camera is panned
  (here, by the previous unit's failed entry taps),
  restore the full base view first - re-centre the camera
  away from the Drill Ground cluster - then ground the
  dish fresh from that screenshot. The 0636 unit's
  working point was norm (53,708), and the profile's
  measured point is (62,727); neither transfers across
  framings - verify the radar screen (Lv.13, stored
  count, stamina) before any work.
- Release posture still applies: execute and claim
  everything stored, then scan the map pins to a closing
  read each. The 0636 unit's pin inventory is still open
  (two standing orange arrow pins, classes unknown), and
  the Doom Legion pin from that unit expired about 07:09.
- Result stats: target unverified, achieved 0, verified
  no, blocker_category c (entry-route: dish icon not
  locatable in the panned camera framing, plus a
  grounding tool timeout). Lesson: a grounding-tool
  timeout can consume the whole pass budget - treat a
  timed-out grounding as the unit's blocker and stop,
  rather than tapping ungrounded points.

## What the 2026-11-02 1439 unit added

- Unit radar-2026-11-02-1403 by ticker-1412, session
  about 14:27 to 14:39, status partial, tracker
  untouched. Duel day 1, Radar Training, release
  posture confirmed by tools/duel.py (radar_posture
  release, day ends 19:00, 4.5 hours left) before the
  unit started, but the radar screen was never entered,
  so this unit executed and claimed nothing. Evidence
  in `_records_/2026-11-02/radar-tasks/1439-queue-run.md`.
- Entry state: the game was left by the donations unit
  (1427) with the base camera panned onto the Drill
  Ground cluster (Drill Ground Lv.25, three floating
  round buttons at the bottom right). The left icon
  column with the radar dish is not visible in this
  framing. This is the second consecutive radar unit
  with this entry blocker, after 1026 the same day.
- Changed method per rule R2 (the 1026 unit burned its
  budget on a grounding timeout): instead of grounding
  the dish, this unit tried to restore the base view
  through the building panel. Tapping the Drill Ground
  area at (810,778) opened the DRILL GROUND panel
  (Unit Count 39460 of 39460, In Base Lv.7 x701, Lv.8
  x1332, Lv.10 x37.4K, Outside no units outside) -
  figures consistent with the 1020 donations unit's
  Drill Ground panel read. No Promote button was
  tapped and nothing was spent.
- Panel close failure, two no-change taps, method
  retired in this unit: the panel X at (799,203) and
  again at (802,200) produced no change. The control
  channel noted background clicks do not reach some
  controls and suggested click_element with a visible
  label or the keyboard instead; neither was tried in
  this unit, and Esc was not used (standing rule: Esc
  has crashed this app before). The game is left safe
  with the DRILL GROUND panel open, no purchase, no
  dispatch, no march, no pin tapped, no other
  activity's rewards claimed.
- Handover for the next radar unit: the panel must be
  closed first (candidates: foreground the LastWar
  window and re-tap the X, click_element, or relaunch
  the app to restore the base overview), then restore
  the full base view, then ground the dish fresh from
  that screenshot (the 0636 unit working point was
  norm 53,708; the profile measured point is 62,727)
  and verify the radar screen (Lv.13, stored count,
  stamina) before any work. Release posture still
  applies: execute and claim everything stored, then
  scan the map pins to a closing read each. The 0636
  unit pin inventory (two standing orange arrow pins,
  classes unknown) is still open. If the next radar
  unit also fails on entry, it is the third consecutive
  unit with this blocker and must write the blocker
  into the radar-tasks activity metadata per rule R2.
- Cross-unit note, binding on donations units: a
  donations unit that pans the camera should restore
  the base framing before it closes, or the following
  unit inherits a panned view with no icon column.
- Result stats: target unverified, achieved 0,
  verified no, blocker_category c (entry-route: base
  camera panned onto Drill Ground with no icon column,
  and the Drill Ground panel X unresponsive to
  background clicks; second consecutive radar unit
  with this blocker).

## Open questions

- Duel delta test - on the next release day, read the duel
  score, claim exactly one batch, read again; settle whether
  a radar claim pays 10,000, 30,000 or another figure on
  this account, and what the bonus source is. (2026-11-09 0852: still owed - the VS panel was not opened in this unit.) (2026-11-09 1253: still owed - the VS panel was not opened; 14 claims on a scoring day would be about 420,000 at 30,000 each, inference only, not a measurement.) (2026-11-09 1717: still owed - the VS panel was not opened; the restored batch of 12 tasks at about 17:40 would be about 360,000 at 30,000 each, inference only, not a measurement.)
- Bottom bar offer selection - the bar presents one offer
  at a time; why did the 2026-10-31 10:40 unit get Quick
  Execute despite 7 pending rewards, when the 06:12, 14:15,
  18:38 and 22:06 units got Claim All and no Quick Execute?
  Candidate factors to test - completable task count at
  entry, pending count, restore timer state.
- Standing pin types - identify the orange arrow, purple
  axe, orange axe and portrait pins (class, cost, reward)
  on the next release day, by tapping them under the
  release handling rule. (2026-11-08 2335 update: the standing
  inventory now also includes blue arrow pins (one with a red
  dot), purple arrow pins and orange skull pins, none yet
  identified - the blue arrow, purple arrow and orange skull
  classes join the orange arrow, purple axe, orange axe and
  portrait pins awaiting identification under the release
  handling rule.) (2026-11-09 0852 update: pin inventory at close - portrait pin top left, blue skull pin top left, blue skull pin top centre, green skull pin right middle, two grey skull pins bottom, gold/pink pin cluster left centre (the 0335 Rare Iron Mine gathering pin, claim NOT checked this unit); per rule R7 the Iron Mine gathering claim is the first action of the next radar unit, then the skull pins and the portrait pin, each to a closing read.) (2026-11-09 1253 update: pin inventory at close - 3 grey skull pins with red dots, 1 green skull, 1 purple skull, 1 blue teardrop, 1 brown animal-face pin, 1 orange skull, 1 portrait pin, at least 6 distinct pins unworked; per the record the same standing set deferred from the 2026-11-08 2335 unit; the 0335 Rare Iron Mine gathering claim is still unchecked after two units (0852, 1253), so the next unit checks whether that pin still stands and claims it if it does, then works the pins per R7.) (2026-11-09 1717 update: the 1244 pin set is ABSENT about 4.5 hours later - 3 grey skull, 1 green skull, 1 purple skull, 1 blue teardrop and 1 portrait pin in the first view, 1 orange skull in the second view, at least 6 distinct pins, none standing in the three swept sectors; the mechanism is unverified (expiry or despawn) - pins do not persist across a half-day gap, new open question; the 0335 Rare Iron Mine gathering claim is now UNCHECKABLE - its pin is gone, so the R7 first-action carry closes as unverifiable, not as done; the brown animal-face circle is NOT a pin - three grounded taps produced no card and no screen change, non-tappable map element, left alone.)
- Doom Legion pin card ambiguity - 0636: the portrait pin
  card named a Doom Legion base, but the world-map card
  carried the own-alliance tag [AP3x]The Apex and closing
  it produced the contested-location toast; when a pin card
  names an alliance base, and whether the toast blocks only
  that location, is unmeasured. Never attack on an ambiguous
  card.
  (2026-11-04 0720 update: the tag alone is NOT a proven block - the 0720 unit attacked an [AP3x]-tagged legion base card, destroyed the base and was paid exactly the card preview. The 0636 contested-toast case is still unexplained and is not reproduced here; the tag must not be read as a no-attack rule by itself, but the card text still has to be read before any attack, and the 0636 toast mechanism stays open.)
- Restore shape - does the 12-task restore land as a batch
  at the 6 hour mark or trickle? Compare stored counts
  against the restore line across one full cycle.
  (2026-11-02 2242 update: the 1913 close predicted 12
  tasks by about 21:32, but the 2242 entry read only 1
  stored at 22:34, so the restore line as written does
  not predict the stored count; semantics unverified.) (2026-11-09 0852 update: the 12-task restore the 0335 unit expected around 05:36 PT did NOT land as a batch - stored read 2/40 at 08:52, not 12/40; a second datapoint that the restore line as written does not predict the stored count.) (2026-11-09 1253 update: the restore line's full-restore time disagreed within the unit - entry read 'Fully restore at 11-10 11:39:11 local time', close read '11-10 17:39:11 local time', six hours apart; the close read is the live one. Do not quote a restore time from an entry read without a closing re-read.) (2026-11-09 1717 update: the restore lands 12 tasks at about 17:40 PT per the close read 'Fully restore at 11-10 17:39:11 local time' with 00:23:37 remaining - a third datapoint that the restore line as written does not predict the stored count in advance; a priority 1 successor is enqueued for the pre-roll claim window 17:40-18:00.)
- Where a survivor gained from a special radar task reports
  to - base gate queue or straight onto the roster.
- How often special pins appear, and whether the skull and
  handshake pins seen on 2026-10-25 follow the story flow.
- Skull pin that opens no card (2026-11-04 0720): a blue skull pin, centre right, took 3 taps (centre twice, tip once) plus 1 long-press and opened no card - only a radar sweep animation and a small circular badge at the pin's lower left. Its identity against the 0334 Doom Elite skull pin (top centre, red dot, card opened, rally blocked, Issue #268) is UNRESOLVED: position and behaviour differ, so it is not recorded as the same pin, and the #268 rally retry that the 0334 R7 order put first was not executed in the 0720 unit and remains owed. The next radar unit must re-ground every pin on its own screenshot, identify the skull pin's class first, and only then attempt a #268 rally retry with a changed method if the Doom Elite pin is present.
- Whether manual per-task execution ever beats Quick
  Execute (cost or reward difference), untested.
- Stored versus completable versus pending (2242): stored
  1 of 40 at entry, 6 tasks completable by Quick Execute,
  11 rewards pending after execution. The top-left stored
  figure is not an inventory of the Quick Execute offer;
  do not infer completable tasks from it. (2026-11-03 1450 update: after Quick Execute 3 tasks
  the bar offered Claim All 8 rewards, and after Quick Execute
  2 tasks it again offered Claim All 8 rewards; the pending
  count after a Quick Execute batch exceeds the batch size.
  Marches returning from earlier batches are the leading
  hypothesis, recorded in the unit, not verified.) (2026-11-09 0852 update: after Claim All emptied stored to 0/40, the bar offered Quick Execute again for 1 task at 10 stamina - a restore landing mid-unit or a stale count, left for the next radar unit, not chased.) (2026-11-09 1253 update: the bar offered Quick Execute 5 tasks for 50 stamina while stored read 3/40, then 1 task for 10 stamina while stored read 0/40; the second Claim All paid 3 rewards for 1 executed task. Consistent reading: pending rewards hide behind the bar's single offer - after the execute the bar flips to Claim All and shows executed plus hidden pending together (1 executed plus 2 hidden equals 3). The bar's Quick Execute count itself exceeding stored (5 versus 3, 1 versus 0) is still unexplained - possibly tasks restore in a trickle the stored counter does not show, or the bar counts a different pool. Left open for the next unit.)
- Dish badge meaning: the dish badge read "10" at entry on
  2026-11-08 2335 while stored was 39 of 40 and only 1 task was
  Quick Executable - the badge number does not equal the stored
  count. What it counts is not established. (Added 2026-11-08 2335.)
- Gold NEW! icon on the radar screen: a gold icon with a NEW!
  badge sits at the top of the radar screen (about norm 295,60),
  seen 2026-11-08 2335, function unknown, never tapped.
  (Added 2026-11-08 2335.) (2026-11-09 1253: re-seen, still untouched, function still unknown.)
- Blue-triangle item identity - radar Claim All rewards repeatedly include a blue-triangle item (366 on 2026-11-09 0852, 726 on 2026-11-09 1253, 450 and 540 on earlier units), unidentified, likely drone parts, unverified. Whether it is the same item as the blue-triangle 596 bubbles over furnace buildings (Issue #508) is unverified - the 1253 unit gives #508 no direct evidence beyond the shared shape, and the item is recorded here as a candidate link only.

## What the 2026-11-02 1508 unit closed for radar

- The Drill Ground panel-close handover written in the
  1532 run is completed, not by a radar unit but by the
  1508 arms-race unit, which found the game on the
  panel the 1412 radar unit left open and closed it to
  the base on the first tap of its X at norm 869,139
  (measured). The panel is no longer left open.
- Entry-blocker counting is unchanged: closing a left
  open panel is not a radar entry attempt, so the
  consecutive entry-failure count from the 1026 and
  1439 units does not advance on this unit, and the
  rule R2 third-failure write-up is not triggered.
  Evidence in
  `_records_/2026-11-02/arms-race/1508-queue-run.md`.

## What the 2026-11-02 1913 unit added - new trade day stack day, done, pin scan empty

- Unit radar-2026-11-02-1803 by ticker-1904, session
  about 19:13, status done. New trade day, stack day
  (duel day 2, Base Expansion): complete tasks but do
  NOT claim - claims score on odd days only. Nothing was
  claimed in this unit, and no map pin was tapped.
  Evidence in
  `_records_/2026-11-02/radar-tasks/1913-queue-run.md`.
- Entry: the left-column dish icon at norm 62,727 opened
  the radar on the first tap. This resolves the 1439
  entry blocker (panned camera, unresponsive panel X):
  the base view was restored and the profile measured
  point worked. The consecutive entry-failure count
  resets to 0 on this successful entry.
- Entry verification (radar screen itself): Radar Lv.13,
  radar points 139, stored tasks 0 of 40, restore line
  12 Radar Task(s) will be restored in 02:18:56 (landing
  about 21:32 PST, before the 22:03 radar slot), stamina
  56 top right.
- No bottom Quick Execute / Claim All bar was presented:
  with 0 stored and 0 rewards pending there is no offer,
  which is consistent, not the 2026-10-31 Claim All
  lockout.
- Work done: no ordinary task was executable (stored
  reads 0 of 40), so there was nothing for Quick Execute
  to run. No stamina was spent and no free stamina claim
  was needed.
- Pin scan: the radar map showed no standing pins at all
  - no finished-task pins, no story pins, no gathering
  pins, and none of the unidentified arrow/axe pins from
  earlier units. Pin inventory is empty as of this unit,
  so nothing was left unattempted; the 0636 pin items
  are long expired and are superseded by this empty
  scan, not carried.
- Device: one "active on a different device" dialog on
  entry, Confirm tapped once (first takeover this pass);
  the app exited as the owner rule predicts, was
  reopened, and the dialog did not return, so the pass
  continued (not contested - the dialog appeared once,
  not three times as in the contested 1834 pass).
- Closing reads: stored 0 of 40, radar points 139,
  stamina 56, restore 12 tasks in about 02:19. Returned
  to the base view at close. Stack-day standard met with
  zero executable tasks.

## What the 2026-11-02 2242 unit added - stack day, single-offer trap in post-execution form, restore line still unverified

- Unit radar-2026-11-02-2203 by ticker-2234, session
  about 22:34 to 22:42, status partial by design under
  the stack posture (duel day 2, Base Expansion).
  Nothing was claimed, and no map pin was tapped.
  Evidence in
  `_records_/2026-11-02/radar-tasks/2242-queue-run.md`.
- Entry: the game was left open on the Alliance Tech
  panel, a donations-screen leftover. Its inner X and
  the Alliance Techs X were closed untouched, no
  donation was tapped, and the Alliance back arrow at
  norm 120,920 returned to the base view. The
  left-column dish icon grounded fresh at norm 53,710
  opened the radar on the first tap, close to the
  profile measured point 62,727 and to the 0636
  working point 53,708, so the dish point stays a
  fresh-grounding point, not a fixed hit.
- Entry verification: Radar Lv.13, radar points 139
  unchanged from the 1913 close, confirming nothing
  was claimed since; stored tasks 1 of 40; stamina 97.
  Restore line: "Fully restore at 11-3 21:31:43 local
  time". Against the 1913 close, which read 12 tasks
  restoring in 02:18:56 and landing about 21:32, only
  1 stored task was present by 22:34, not 12, so the
  restore-line semantics stay unverified, not assumed.
  The restore-shape open question below carries this
  data point.
- Work done: Quick Execute ran the sole offer, 6 tasks
  for 60 stamina (97 to 37). After the batch the bar
  flipped to "11 task rewards can be claimed" with a
  Claim All button and no Quick Execute offer
  remained. The 11 pending rewards were deliberately
  NOT claimed under the stack posture, so radar
  points stayed at 139. A second Quick Execute offer
  never appeared while the Claim All bar stood: this
  is the single-offer trap measured on 2026-10-31, in
  its post-execution form.
- Closing reads: stored 1 of 40, radar points 139,
  stamina 38 at close (37 at the post-batch read,
  plus 1 regenerated during the closing wait),
  pending rewards 11 unclaimed, restore line
  unchanged. Returned to base via the radar home
  button.
- Pin scan, inventory only, nothing tapped: green
  skull upper left near an ally base, purple skull
  mid left, green skull mid right, all red-dotted.
  No orange arrow, orange axe or portrait pins were
  visible in this map framing. These three pins are
  the release-day unit's checklist, not a surprise.
- Completion standard, carried to the next unit: the
  stored-count versus Quick Execute-count gap (stored
  1 at entry, 6 completable, 11 pending after) is an
  open measurement question - the top-left 1 of 40
  figure does not behave as a simple inventory of the
  Quick Execute offer, and the next unit must not
  infer completable tasks from it. Its opening read
  must check whether the stored 1 becomes executable
  and whether the pending count is still 11, before
  any other radar work. Tracker untouched, so the
  next tick re-produces this regular.

## What the 2026-11-03 0212 unit added - stack day, single-offer trap in at-entry form

- Ticker-0204, unit radar-2026-11-03-0203, about 02:12
  local, partial by design under the stack posture, not
  a miss. Duel day 2, theme Base Expansion: radar_posture
  stack, day ends 2026-11-03T19:00:00 local. Complete
  tasks but do NOT claim - claims score on odd days
  only. Nothing was claimed in this unit, and no map
  pin was tapped.
- Entry: the game was left open on the Alliance Techs
  panel (a donations-screen leftover, not this unit's
  work). The panel X was closed untouched - no donation
  was tapped - and the Alliance screen back arrow
  returned to the base view. Entry correction, measured:
  an early coordinate estimate for the Alliance back
  arrow was wrong in x (104 instead of the grounded
  162); the grounded point worked at once. Ground the
  back arrow fresh; do not trust the 104 estimate.
- Dish icon grounded fresh at norm 53,711 (visual
  grounding on the current screenshot; close to the
  2242 unit's 53,710 and to the profile measured point
  62,727) opened the radar on the first tap. The
  re-ground-fresh rule stands: the fresh point, not
  the carried point, is what opened the screen.
- Entry verification, read live: Radar Lv.13, radar
  points 139 (unchanged from the 2242 unit close,
  confirming nothing was claimed since). Stored tasks
  1 of 40. Stamina 79 top right. Bottom bar at entry:
  "11 task rewards can be claimed" with a Claim All
  button. No Quick Execute offer was shown at entry.
- Single-offer trap, second form measured: the trap
  measured on 2026-10-31 and in post-execution form at
  2242 (Quick Execute at entry, 6 tasks run, then the
  bar flipped to Claim All only) appears here in
  at-entry form - the bar presented Claim All only
  from the start, so no Quick Execute offer existed to
  run, and the stored 1 of 40 sits behind the Claim All
  bar, which the stack posture forbids clearing. No
  task was executed and nothing was claimed. The next
  unit's opening read must check whether a Quick
  Execute offer returns, and whether the pending count
  is still 11, before any other radar work.
- Restore line, semantics still unverified: "12 Radar
  Task(s) will be restored in 01:22:23" at entry. This
  differs in form from the 2242 close ("Fully restore
  at 11-3 21:31:43 local time"); neither form is assumed
  to mean the other, and the restore-line semantics
  stay unverified, not assumed.
- No free stamina claim was needed and none was taken;
  no stamina items were opened; no Buy was tapped.
  Returned to the base view at close via the radar
  home button (grounded at norm 907,952).
- Closing reads: stored 1 of 40, radar points 139,
  stamina 79, pending rewards on the Claim All bar 11,
  unclaimed. Restore line unchanged in form at close.
- Pin scan (stack posture - inventory only, nothing
  tapped): three standing pins on the closing radar
  map, all with red dots, all left untapped per the
  stack handling rule - the same three as the 2242
  inventory: green skull pin upper left near an ally
  base, purple skull pin mid left, green skull pin mid
  right. No orange arrow, orange axe or portrait pins
  were visible in this map framing. The three pins are
  the release-day unit's checklist, not a surprise.
- Result stats: stored_count 1, radar_points 139,
  stamina_before 79, stamina_after 79, tasks_executed
  0, tasks_claimed 0, pending_rewards 11, pins_found 3,
  device_takeovers 0, blocker single-offer Claim All
  standing at entry.

## What the 2026-11-03 0636 unit added - stack day, dish centre re-grounded, Claim All-only bar again

- Ticker-0634, unit radar-2026-11-03-0603, about 06:36
  local, partial by design under the stack posture, not
  a miss. Duel day 2: stack, claims score on release
  days only. Nothing was claimed in this unit, no map
  pin was tapped, no stamina was spent.
- Entry: the game was left open on the Alliance Techs
  panel by the previous donations unit (Donation Count
  read live 1/30 at entry, not this unit's work, nothing
  donated). The Alliance back arrow stalled twice at
  norm 98,919 and 100,920, then the visually grounded
  centre norm 164,931 returned to the base screen - the
  same proven point as the 2026-11-02 mail unit, and
  consistent with the 0212 x correction from 104 to
  grounded 162.
- Dish correction, measured: a first tap at norm 53,682
  opened an ally base profile ([AP3x]Amarky257) instead
  of the radar; the profile was dismissed by tapping
  empty ground. A second tap at the bounding-box centre
  norm 57,704 opened the radar, verified by its own
  reads. Lesson: the dish icon's effective centre is
  57,704 on this framing, not the 53,682 point. The
  0212 point 53,711 was not tested in this unit and is
  not claimed wrong; the re-ground-fresh rule stands,
  and the fresh point, not the carried point, is what
  opened the screen.
- Radar screen, read live: Lv.13, radar points 139
  unchanged, stored 13 of 40, stamina 120, restore line
  "12 Radar Task(s) will be restored in 02:50:41",
  full restore at 11-3 21:31:43 local time. Stored rose
  from 1 of 40 at 0212 to 13 of 40 here, consistent with
  one 12-task restore landing between the two units;
  headroom to the 40 cap is not a concern. Restore-line
  semantics stay unverified, not assumed.
- Single-offer trap, at-entry form again: the bottom
  bar read "11 task rewards can be claimed" with a
  Claim All button only, no Quick Execute offer, so
  stack-day execution is locked out while the pending
  rewards stand. This is the named blocker carried into
  the next unit's opening read, per the stack-day
  completion standard; the next unit reads the bar
  offer first and plans around it before any other
  radar work.
- Pin inventory (stack posture - inventory only,
  nothing tapped): three skull pins standing on the
  radar map - a green skull pin top-centre-left, a
  purple skull pin mid-left, and a blue skull pin
  mid-right. No other radar pin was visible on the map
  shown. The portrait squares on the map are alliance
  member markers, not radar pins - a new distinction
  for the inventory rule.
- Closing reads: points 139, stored 13 of 40, pending
  rewards on the Claim All bar 11, stamina 120, tasks
  executed 0, rewards claimed 0, pins tapped 0.
  Blocker category e (repeated blocker - Claim
  All-only bar).

## What the 2026-11-03 1450 unit added - release day, 27 claims, duel-dialog contradiction

- Ticker-1434, unit radar-2026-11-03-1403, about 14:35 to
  14:50 local, status partial. Evidence in
  `_records_/2026-11-03/radar-tasks/1450-queue-run.md`.
- Posture note, read live at entry: tools/duel.py reported
  duel day 3, Age of Science, radar posture release, day
  ends 2026-11-04 19:00 local. The unit window text still
  read "duel day 2 - radar stack" (stamped at production
  before the posture flipped); the live posture governs,
  so this unit ran as a release unit. Lesson: stamped unit
  text can lag a posture flip; re-read the live posture
  at entry, never trust the stamp.
- Entry: the game was left on the Alliance panel by the
  1404 pass; the back arrow at norm (148,907) exited to
  the base on the first try. The dish tap at the
  documented norm (62,727) opened the radar on the first
  try, confirming the 1913 dish point again. Entry reads:
  Lv.13, stored 25/40, stamina 120, restore line "12
  Radar Task(s) will be restored in 00:53:xx", full
  restore 11-4 03:31:43 local time.
- Pin claim first: a green skull pin with a red dot (top
  left of the entry map) tapped at norm (312,300) claimed
  instantly, as the finished-task pin rule predicts.
  CONGRATULATIONS popup: radar item x10, EXP 1.5M, drone
  item 800, food 789.6K, coin 127.2K. Radar points 139 to
  140, stored 25/40 to 24/40, pending rewards 11 to 10.
  The finished-task instant-claim rule is confirmed again.
- Claim All hitbox correction, measured: taps at norm y
  890, 905, 910 and 912 on the Claim All button did
  NOTHING (five taps across two attempts, including a
  double-click); a tap at norm (498,925) opened the
  button. Standing rule updated in the Quick Execute
  section: tap bottom-bar buttons at y 925, not at their
  visual centre (~910).
- Claim All opened a TIPS dialog, verbatim: "Completing
  Radar Tasks today will not grant Alliance Duel points,
  and you are about to claim 10 radar task rewards at
  once. Continue?" This contradicts tools/duel.py, which
  said radar claims score again today. The unit claimed
  anyway: the resources are certain, holding the stack
  for a later scoring day risks task expiry, and the
  release standard governs. The contradiction is filed
  as Issue #235 (tooling) for the planner/retro to settle
  against a live VS panel read; it is NOT closed here,
  and the scoring section is NOT rewritten on this
  evidence alone. Confirm tapped at norm (638,702).
- Claim All 1: 10 rewards claimed. Popup: radar item
  100, EXP 19.4M, drone item 2.4K, blue triangle 225,
  iron 2.8M, food 5.6M, coin 2.3M. Radar points 140 to
  150, stored 24/40 to 14/40. Bar flipped to Quick
  Execute: "You can complete 3 tasks, requires 30
  Stamina."
- Quick Execute 1: 3 tasks, stamina 120 to 90, stored
  stayed 14/40. Bar flipped to Claim All: "8 task rewards
  can be claimed". The pending count after a Quick
  Execute batch exceeds the batch size; the mechanism is
  not settled - marches returning from earlier batches
  are the leading hypothesis, recorded here, not
  verified. This instance is appended to the stored
  versus completable open question.
- Claim All 2: 8 rewards claimed (same TIPS dialog,
  Confirm at (638,702)). Popup: radar item 80, EXP
  13.5M, blue triangle 183, drone item 3.2K, iron 5.1M,
  food 1.1M, coin 1.4M. Radar points 150 to 158, stored
  14/40 to 6/40. Bar flipped to Quick Execute: "You can
  complete 2 tasks, requires 20 Stamina."
- Quick Execute 2: 2 tasks, stamina 90 to 70, stored
  stayed 6/40. Bar flipped to Claim All: "8 task rewards
  can be claimed" again.
- Claim All 3: 8 rewards claimed (same dialog, same
  Confirm). Popup: radar item 80, EXP 11.5M, drone item
  4.0K, blue triangle 225, iron 2.2M, coin 1.3M, food
  3.2M. Radar points 158 to 166, stored 6/40 to 0/40.
  Bar flipped to Quick Execute: "You can complete 4
  tasks, requires 40 Stamina" - left for the next unit.
- Totals in this unit: rewards claimed 27 (1 pin + 10 +
  8 + 8). Radar points 139 to 166 (+27, exactly the
  claim count). Tasks executed 5 via Quick Execute (3 +
  2), 50 stamina. Popup resources summed: coin 5.127M,
  EXP 45.9M, iron 10.1M, food 10.69M, drone items 10.4K,
  radar items 270, blue triangles 633. No diamonds or
  money spent, no Buy tapped, no stamina item used,
  no free stamina claim taken (not needed).
- Closing state, live reads: Lv.13, radar points 166,
  stored 0/40, stamina 70, restore line "12 Radar Task(s)
  will be restored in 00:42:21" at close, full restore
  11-4 03:31:43 local (unchanged from entry). Bottom bar
  at close: Quick Execute, 4 tasks, 40 stamina -
  carried to the next radar unit. Restore-line semantics
  stay unverified, not assumed.
- Pin inventory at close (untapped, visible frame only,
  not a whole-map census): orange skull pin with red dot
  (top centre), purple axe pin (top right), green pin
  (left middle, partly behind a portrait), portrait pins
  (left middle), purple axe pin (centre), blue axe pin
  (lower centre). All pins left unattempted, so per the
  release handling rule this unit is partial, never done.
  Pin types stay unidentified; they head the open
  questions, not a guessed taxonomy.
- Duel-points note: per the live TIPS dialog, none of
  today's radar claims granted Alliance Duel points; the
  duel-score delta test remains open and is now Issue
  #235. No duel score read was taken in this unit.
  No earlier claim superseded; the 0636 pin inventory is
  superseded in place by this close inventory, not erased.

## Changelog

- 1.62.0, 2026-11-09 - 1717 unit folded (partial, release day 1): dish grounded fresh (62,727) first tap again, re-confirmed in this window, commented on Issue #484; ordinary cycle already clear (stored 0/40, pending 0, bar gone); the 1244 pin set (at least 6 distinct pins) is ABSENT about 4.5 hours later, mechanism unverified - pins expire or despawn, new open question; the 0335 Rare Iron Mine gathering claim carry closes as UNVERIFIABLE, not done (pin gone, 720K landing never attributed); brown animal-face circle is NOT a pin - three grounded taps, no card, non-tappable map element; Violet's Gift toast unmeasured (points 336 unchanged); gold NEW! icon fourth sighting, still untouched; restore lands 12 tasks about 17:40 PT, R6 successor radar-2026-11-10-0118 enqueued for the pre-roll claim window 17:40-18:00 (12 tasks about 360,000 duel points at 30,000 each, inference only); points 336, stamina 93 to 94, restore 12 tasks in 00:23:37 at close; duel delta test still owed.

- 1.61.0, 2026-11-09 - 1253 unit folded (partial, release day): dish grounded fresh (62,727) first tap, red badge 1 - the 2026-10-29 point works again, commented on Issue #484, and the 2335 'stale in this window geometry' judgement is corrected; ordinary cycle fully done (Quick Execute 5 plus 1 tasks, Claim All 11 plus 3 rewards, points 322 to 336, stored 3/40 to 0/40, stamina 120 to 61, restore 12 tasks in 04:48:41 at close); bar-vs-stored refined - the bar offered 5 tasks against stored 3 and 1 task against stored 0, and the second Claim All paid 3 rewards for 1 executed task, so pending rewards hide behind the bar's single offer and surface with the executed batch, while the Quick Execute count exceeding stored stays unexplained; restore full-time disagreed within the unit (entry 11-10 11:39:11, close 11-10 17:39:11, close read is live); points 322 at entry against 311 at last night's close with no unit between, unverified, possibly the owner's own play; 6 pins inventoried unworked (grey skulls, green skull, purple skull, blue teardrop, brown animal-face, orange skull, portrait), same standing set deferred from the 2026-11-08 2335 unit per the record, R7 next unit starts with the pins; gold NEW! icon re-seen, still untouched; blue-triangle item 726 in the rewards, unidentified, likely drone parts, unverified, candidate link to Issue #508 only; duel delta test still owed (14 claims would be about 420,000 at 30,000 each, inference only).

- 1.60.0, 2026-11-09 - Frontmatter repair flagged by the integrator on PR #518 (post-merge note, 0945 pass): the 2026-11-07 1633 grounded_in line carried a colon inside an unquoted value ('...navigation detour: BASE tap 920,975...') and failed a strict YAML parse on main; reworded to a dash so the frontmatter parses. No new radar unit ran this hour; no other change.

- 1.59.0, 2026-11-09 - 0852 unit folded (partial, release day): dish grounded fresh (51,726) first tap with the camera still panned on the Drill Ground cluster - a merely panned camera does not block the dish tap, restore-first still binds for an open building panel; entry Lv.13, points 311, stored 2/40, stamina 120, restore 12 tasks in 02:46:23, Fully restore at 11-10 05:39:11; the 12-task restore expected around 05:36 did NOT land as a batch (stored 2/40 at 08:52, second datapoint against the batch hypothesis); Quick Execute 3 tasks / 30 stamina, Claim All 11 rewards (radar item x110, EXP 15.9M, blue item 4.0K, blue triangle 366, iron 5.0M, food 2.3M, coin 2.0M), points 311 to 322, stored 0/40; bar then offered Quick Execute again for 1 task at 10 stamina with stored 0/40, unexplained, left for the next unit; 7 pins inventoried unattempted (portrait, 2 blue skull, green skull, 2 grey skull, gold/pink Iron Mine cluster - its claim NOT checked), R7 puts the Iron Mine gathering claim first next unit; duel delta test still owed.

- 1.58.0, 2026-11-09 - cross-unit entry note from the 0636 harvest unit (partial): the gold circle with a blue gem above the blue truck vehicle opens the world/radar map with 6 task rewards claimable at 06:49 - a verified radar entry point, not the truck loot; the rewards were left untouched for the radar unit; entry verification still applies. Sourced to the harvest record 04b12d13, folded here, not as a radar unit.

- 1.57.0, 2026-11-09 - 0335 unit folded (partial, release day): dish re-grounded fresh, (55,689) missed the top edge of the dish circle, (51,718) opened on the first try - newest verified first-try point, (50,740) preference still untested as a direct tap, commented on Issue #484; blue axe pin dispatched a Rare Iron Mine gathering (Lv.15 mine, 720K, 00:06:57, finish 03:45, March Queues 1/4, 0 stamina, reward iron 105.6K + radar item 10 lands on the next unit); pin inventory 5 unattempted (blue axe centre, 2 orange skulls top right, purple axe centre, portrait left middle) with the record listing the blue axe both worked and unattempted - persistence after dispatch unresolved, next unit verifies; points 311, stored 0/40, stamina 82 to 83, restore 12 tasks in 02:01:04, Fully restore at 11-9 23:39:11; duel delta test still owed.

- 1.56.0, 2026-11-09 - 0159 unit folded (done): stack empty, 0 stored of 40, no Quick Execute work and no Claim All bar, points 311, restore 12 tasks in 03:41:39, stamina 62, green gauge 100%, Lv.13; the 1355 stack (16 stored, Claim All lockout, 10 pending) has since emptied, how it emptied not determined and recorded as observed, not asserted; 6 pins inventoried untapped (2 blue arrow, 2 orange skull, 1 purple arrow, 1 portrait); dish grounded fresh at (54,707) and opened on the first tap - the retro-preferred (50,740) point and this grounded point agree within the same slot, the slot rotates so every unit still re-grounds fresh, (50,740) itself still untested as a direct tap; NEW! badge on the yellow icon at the top of the radar screen re-seen, function still unknown; orange skull pins may be the same skull signal as the timed base-edge badge (Issue #498), hypothesis only, next radar unit checks whether tapping an orange skull pin matches that timer.

- 1.55.0, 2026-11-09 - 2335 release-day unit folded: 16 tasks executed in 6 batches, 44 rewards claimed in 7 Claim All taps, points 267 to 311 (+44, one per claim), stored 39 of 40 to 0 of 40, free stamina claim once (75, Remaining Today 2 of 2 to 1 of 2), stamina items 10-stamina x641 and 50-stamina x665 read live; dish re-grounded fresh to norm (37,736) in the 642x951 window after (59,687) missed - the (62,727) 2026-10-29 point is stale in this geometry and the (50,740) retro preference was not tested this unit, so the dish still drifts per session and is re-grounded fresh every unit; dish badge "10" does not equal the stored count (39 of 40), meaning unknown; gold NEW! icon at the top of the radar screen (about 295,60) function unknown; 6 pins left untapped (2 blue arrow, 2 orange skull, 1 portrait, 1 purple arrow) so partial, token expired 23:50:29; HUD cross-check consistent (food +11.9M, iron +14.3M, coin +9.4M); duel delta test still owed (44 claims would be about 1.32M at 30,000 each, inference only); brown animal-face pin not seen, may be off-screen.

- 1.54.0, 2026-11-08 - retro action A-2026-11-08-01 applied (Issue #484): the dish entry rule now prefers norm (50,740) as the first tap (opened the radar on the first tap at 13:53 on 2026-11-08, 1355 unit); the (54,583) and (54,780) points failed at 20:15 the same day (2028 unit, opened Intercity Trade and BUILD) and are never to be reused; if the preferred point fails, re-ground from a fresh base screenshot. No new radar unit ran this hour; no other change.

- 1.53.0, 2026-11-08 - 2028 release-day unit folded: duel week rolled about 18:00 to day 1 Radar Training RELEASE (day ends 2026-11-09 18:00), unit window stamp day 7 stale, live posture governs; radar screen never entered - dish groundings (54,583) opened Intercity Trade and (54,780) opened BUILD, grounding tool mislabelled the dish slot twice, next point to try is (50,740) from the 1355 unit; recovery tap opened the Age of Oil research tree (all nodes 0/10, queue timers 20:13:57:39 and 08:47:50, read only) whose back arrow does not respond to background clicks - control channel guidance is click_element with the visible label or the keyboard, Return/Esc never used, relaunch is a verified exit; game left on the research tree; 10 pending rewards plus 16 stored tasks still waiting, claims score +30,000 each as displayed; carried figures from 1355 unverified; duel delta test still owed.

- 1.21.0, 2026-11-03 - 1450 release-day unit folded: dish
  62,727 first-tap entry confirmed again; green skull pin
  instant claim (+1 point) re-confirms the finished-task
  rule; bottom-bar hitbox corrected to y 925 (y 890-912
  no-change); 27 rewards claimed, points 139 to 166, stored
  0 of 40, stamina 70, Quick Execute 4 tasks / 40 stamina
  carried; live TIPS dialog says today's radar claims grant
  no duel points, contradicting duel.py - filed as Issue
  #235 (tooling), scoring section NOT rewritten, delta test
  still owed; 6 pins inventoried unattempted so partial.

- 1.16.0, 2026-11-02 - 1913 new-trade-day stack-day unit folded: dish 62,727 first-tap entry resolves the 1439 entry blocker, entry-failure count resets to 0; Lv.13, points 139, stored 0 of 40, stamina 56, 12 tasks restoring about 21:32; no Quick Execute / Claim All bar with 0 stored and 0 pending (consistent, not the 2026-10-31 lockout); pin scan empty, nothing left unattempted; one takeover, dialog did not return, not contested.

- 1.15.0, 2026-11-02 - 1508 arms-race unit closed the Drill Ground panel-close handover from the 1532 run: panel X at norm 869,139 closed to base on the first tap, panel no longer left open; entry-blocker count unchanged (a close is not an entry attempt, rule R2 third-failure write-up not triggered); 0636 pin inventory still open, release posture still applies, duel delta test still owed.


- 1.14.0, 2026-11-02 - 1439 duel day 1 release unit folded: radar screen never entered (camera panned to Drill Ground by the donations unit's failed taps, dish column not visible); Drill Ground panel opened at (810,778) with figures matching the 1020 read, but its X was unresponsive to background clicks twice and the game was left with the panel open; handover is close panel, restore full base view, ground dish fresh; a third consecutive entry failure writes the blocker into this metadata per rule R2; 0636 pin inventory still open, release posture still applies, duel delta test still owed.

- 1.13.0, 2026-11-02 - 1026 duel day 1 release unit folded: radar screen never entered (camera panned to Drill Ground by the donations unit's failed taps, dish column not visible, dish grounding timed out after 180s consuming the pass budget); entry precondition added (restore full base view before grounding dish); 0636 pin inventory still open, Doom Legion pin expired about 07:09; release posture still applies; duel delta test still owed.

- 1.12.0, 2026-11-02 - 0636 duel day 1 release unit folded: dish groundings disagreed in one unit (55,677 nothing, 53,575 Trucks, 53,708 radar; tool twice mislabelled truck as dish); entry Lv.13, points 103, stored 4 of 40, stamina 112; 12 claims over two batches, points 103 to 115, stored 0 of 40, stamina 53; portrait Doom Legion pin left on an ambiguous alliance-tagged card plus contested toast, expiry about 07:09; two orange arrow pins unattempted so the unit stays partial; duel delta test still owed.

- 1.11.0, 2026-11-02 - 0226 duel day 1 release unit folded: entry corrections (back arrow true centre 132,948; no-HUD base frame unusable; dish fresh at 58,736, badge 2); points 101 to 103 over 2 claims, stored 0 of 40, stamina 60 to 61; claimed rewards do not match the 2319 Doom Walker rally card, so the rally kill/claim stays unverified; seven pins left unattempted so the unit stays partial; duel delta test still owed.

- 1.10.0, 2026-11-01 - 2319 duel day 1 release unit folded: live re-read supersedes the 1904 close (stored 6 of 40 at entry, 0 of 40 at close; points 91 to 101 over 4 tasks and 10 claims); Doom Walker rally launched (Lv.160, Squad 1 25.12M, rally cost 20, kill and claim fall to the next unit); pins left unattempted so the unit stays partial; duel delta test still owed.

- 1.9.0, 2026-11-01 - 1904 duel day 1 release unit folded:
  live re-read supersedes the 1629 carried figures (stored 19
  of 40 at entry, 0 of 40 at close; stamina 145 to 35; points
  66 to 91 over 11 tasks and 25 claims); offer-versus-stored
  mismatch recorded; pins left unattempted so the unit stays
  partial; duel delta test still owed.
- 1.8.0, 2026-11-01 - 1629 entry-failure unit folded:
  dish tap at 53,688 landing on a panned base view is a
  failed entry, not a radar read; recovery correctly stopped
  rather than blind-tapped; stack posture held on duel day 7
  off-day settlement; the next unit's first read is the stored
  count against the 40 cap after the about 14:45 restore.
- 1.6.0, 2026-11-01 - first retrospective hardening pass,
  worked as the knowledge organizer's first work order under
  the learning and knowledge hardening protocol. Entry
  section rewritten around the rotating shortcut with
  mandatory screen verification; mechanism table completed
  from the 2026-10-25 to 2026-10-31 records (refresh
  quantity, cap behaviour, expiry, task types); Quick
  Execute coverage and exceptions made explicit, including
  the Claim All bar trap measured on 2026-10-31; pin
  taxonomy and posture-dependent handling protocol added;
  stack and release completion standards stated as checkable
  closing reads; scoring section records the 10,000 dual
  source base against the in-game 30,000 display with the
  delta test owed; proficiency table added per field.
  Web research accessed 2026-11-01 - Fandom Radar Tasks,
  LDShop guide, GrindnStrat guide, Last War Handbook VS
  schedule, lastwar.wiki Alliance Duel; one dissenting
  8 hour refresh claim rejected against dual source and the
  in-game restore quantity. Registration note - the retro
  improvements backlog (_records_/retro/improvements.md)
  does not exist yet at the time of this pass; it is to be
  created by the first retro run, so this work order is
  registered here rather than in a backlog file, and the
  first retro should lift it into the backlog as a
  knowledge-organization task pending closure by field
  verification in later execution units.
- 1.5.0 and earlier - incremental field notes from the
  2026-10-25 to 2026-10-29 executions (entry grounding,
  pin tap caution, special pin flow, doom pins, gathering
  pins), preserved in git history.
- 1.7.0, 2026-11-01 - stack-day 1122 unit folded (missed
  by the 1132 run's input list, gap closed here): 5-task
  Quick Execute batch at 10 stamina each, points held at
  45, bar flipped to Claim All only with 11 rewards
  pending, handshake and skull pins inventoried untapped,
  and the 12-task restore landing about 14:50 that would
  overshoot the 40 cap. (1.6.1 was a minor bump without
  a changelog line; the numbering is preserved, not
  rewritten.)

- 1.17.0, 2026-11-02 - 2242 stack-day unit folded: dish fresh at 53,710 first-tap entry; Lv.13, points 139, stored 1 of 40, stamina 97 to 38; Quick Execute 6 tasks for 60 stamina, then Claim All for 11 rewards with no second Quick Execute offer (single-offer trap, post-execution form); 11 rewards left unclaimed per stack posture; restore line predicting 12 tasks by about 21:32 against only 1 stored at 22:34, so restore semantics stay unverified; three red-dotted pins inventoried, none tapped; stored-versus-completable gap recorded as an open measurement question.

- 1.18.0, 2026-11-03 - 0212 stack-day unit folded: dish fresh at 53,711 first-tap entry; Lv.13, points 139 unchanged, stored 1 of 40, stamina 79; single-offer trap in at-entry form (Claim All only at entry, no Quick Execute offer, contrast 2242 post-execution form); 11 rewards left unclaimed per stack posture; restore line in a second form ("12 Radar Task(s) will be restored in 01:22:23"), semantics still unverified; three red-dotted pins inventoried, same as 2242; Alliance back-arrow x corrected 104 to grounded 162; radar home button 907,952.

- 1.19.0, 2026-11-03 - 0636 stack-day unit folded: dish centre re-grounded at 57,704 after the 53,682 tap opened an ally base profile (0212 point 53,711 untested here, not claimed wrong); Lv.13, points 139 unchanged, stored 13 of 40 (one 12-task restore since 0212), stamina 120, restore line "12 tasks in 02:50:41" with full restore 11-3 21:31:43, semantics still unverified; Claim All-only bar with 11 pending again in at-entry form, stack-day lockout carried as the named blocker; three skull pins inventoried (green top-centre-left, purple mid-left, blue mid-right), portrait squares distinguished as member markers, not pins; Alliance back arrow stalls at 98,919 and 100,920 with grounded 164,931 working.


- 1.20.0, 2026-11-03 - 1010 stack-day unit folded: dish
  grounded fresh at 52,711 first-tap entry (consistent
  with the proven 57,704 centre from 0636, not claimed
  against the untested 0212 point); Lv.13, points 139
  unchanged, stored 25 of 40 (one 12-task restore since
  the 0636 read of 13 of 40), stamina 120, restore line
  "12 tasks in 05:21:27" with full restore 11-3 21:31:43
  (same full-restore clock as 0636), semantics still
  unverified; Claim All-only bar with 11 pending for
  the third consecutive radar unit (0203, 0636, now
  1010), stack-day lockout carried as the named
  blocker, the next unit must read the bar offer first
  and plan around it; three skull pins inventoried
  (green top-centre-left, blue mid-right, purple
  mid-left), portrait squares distinguished as member
  markers, not pins; Commendation Notice popup
  navigated past via its View button to the Exercise
  panel (Preparing 04:51:29, Offline Participation
  checked, untouched), then backed out untouched to
  base; headroom to the 40 cap is not a concern
  (25/40, below 39).
- 1.22.0 (2026-11-03): PR 237 merge settles the 1450 live-dialog contradiction - duel.py naive-UTC clock bug (day 3 eight hours early), corrected tool returns day 2 stack matching the dialog verbatim, stale-schedule hypothesis retired, 1450 re-read as a stack-day unit misread as release (window stamp was right, tool reading wrong), retro verification (next radar unit reports the PT day) still owed, Issue #235 commented by this run and left open for the retro.

- 1.23.0 (2026-11-03): 1913 release-day unit folded: entry
  misfire (55,560) opens Your Truck, radar at (57,715) in
  the proven cluster; bottom-bar hitbox corrected per-window
  (500,952) in this geometry, y-925 does not transfer;
  17 rewards claimed, points 166 to 183, stored 0 of 40,
  stamina 21, full restore 11-4 15:31:43; NO TIPS dialog on
  any of the three post-rollover Claim All taps, new Issue
  #235 evidence, not a settlement, delta test still owed;
  4 pins inventoried unattempted so partial, second
  consecutive partial carrying the same pin blocker, R7
  pins-first for the next unit; trade-counter reset
  correction cross-referenced from the 1846 trucks unit.

- 1.24.0 (2026-11-03): 2317 release-day unit folded: story pin completed through the verified flow (revealed rewards survivor x1, paw print 200, black rock 207.3K, dialog to the treasure-map banner, pin gone at close); March true centre (500,751) in this window geometry, estimates above the active area all dead, matching the zombie-invasion March lesson (500,755); ground contextual buttons, never estimate them (hammer 490,600, magnifier 499,599, estimates dead); radar stamina read did NOT move with the story march (shown -5, read stayed 120) - unresolved discrepancy, dispatch proven by the pin-card reward reveal, not by stamina; 11 rewards claimed, points 183 to 194, stored 0 of 40, stamina 91, full restore 11-5 03:31:43; NO TIPS dialog on either Claim All tap, further Issue #235 evidence commented by this run, delta test still owed; third consecutive partial carrying the same pin blocker, R7 next-unit order is the red-dotted blue skull pin first, then the axe pins, every pin point re-grounded on the unit's own screenshot.

- 1.31.0 (2026-11-05): Correction from the 0134 survivors and 0204 gifts records - the game window is windowed 1920x1080 on an inactive Space, not in native fullscreen (View menu lists Enter Full Screen, read on-screen in session cc-505 and re-confirmed by a repeated probe in cc-508); the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission; the "running fullscreen" wording in the 1534, 1904 and 2334 sections is superseded; the permission/pipeline-restart follow-up is replaced by the window-back-on-active-Space unblock (owner Dock-icon click); background Space keys do not switch Spaces, set_window_frame is stale-observation-gated, Cmd+Tab is blocked, list_windows needs the exact app name "LastWar"; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; twenty-sixth and twenty-seventh occurrences commented onto Issue #282 by this run. (1.25.0 through 1.30.0 carry the 2317, 0720, 1005, 1534, 1904 and 2334 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.32.0 (2026-11-05): 0304 radar unit folded - twenty-ninth consecutive capture failure, first fail-fast probe classification OFF_SCREEN_WINDOW (high confidence) from _tools_/mac_capture_probe.py 1.0.0 (PR 307); the View-menu inspect step could not run, gated on a fresh observation of the window; Chrome observes normally in the same session (Gmail inbox, full accessibility tree); the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; twenty-eighth and twenty-ninth occurrences commented onto Issue #282 by this run.

- 1.33.0 (2026-11-05): 0704 radar unit folded - thirty-sixth consecutive capture failure, probe classification OFF_SCREEN_WINDOW (high confidence) from _tools_/mac_capture_probe.py 1.0.0 (PR 307); the probe's missing Chrome control-observation step was closed in the same pass (cc-529, full accessibility tree); five 0257-cycle units expired by sync; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; thirty-sixth occurrence commented onto Issue #282 by this run (the thirty-fifth, ticker-0634, has no record on the records branch at this run's cutoff).

- 1.34.0 (2026-11-05): 1104 radar unit folded - forty-third consecutive pass with a Mac device-access blocker, fourth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 3h30m, unchanged since the 1025 pass, four invokes zero responses, no probe run since last_seen unrefreshed); stack-day unit (duel day 4), loss is unexecuted ordinary tasks and missing closing reads, not leaked claims; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; forty-third occurrence commented onto Issue #282 by this run.

- 1.35.0 (2026-11-05): 1504 radar unit folded - fifty-first consecutive pass with a Mac device-access blocker, twelfth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 7h30m, unchanged since the 1025 pass, four invokes zero responses, one of them the pass's own connection.repair parameter error, no probe run since last_seen unrefreshed); stack-day unit (duel day 4), loss is unexecuted ordinary tasks and missing closing reads, not leaked claims; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; fifty-first occurrence commented onto Issue #282 by this run.

- 1.36.0 (2026-11-05): 1933 radar unit folded - fifty-ninth consecutive pass with a Mac device-access blocker, twentieth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 12h, unchanged since the 1025 pass, five invokes zero responses, no probe run since last_seen unrefreshed); stack-window unit whose live entry posture is release, not stack (tools/duel.py 19:35 reads duel day 5, Total Mobilization, radar_posture release, day ends 2026-11-06 18:00 local) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; fifty-ninth occurrence commented onto Issue #282 by this run.

- 1.37.0 (2026-11-06): 0004 radar unit folded - sixty-third consecutive pass with a Mac device-access blocker, twenty-fourth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 16h50m, unchanged since the 1025 pass and identical to the 2303 reading, five invokes zero responses, no probe run since last_seen unrefreshed, no recovery-device attempts); release-day check for the slot unexecuted (duel day 5) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; sixty-third occurrence commented onto Issue #282 by this run.
- 1.38.0 (2026-11-06): 0342 radar unit folded - sixty-sixth consecutive pass with a Mac device-access blocker, twenty-seventh in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 20h10m, unchanged since the 0234 pass, five invokes zero responses, no probe run since last_seen unrefreshed, no recovery-device attempts - the 0234 pass recovery-channel attempt timed out after 25s); release-day check for the slot unexecuted (duel day 5, planned 02:03 local, expires 06:03 local) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; sixty-sixth occurrence commented onto Issue #282 by this run.
- 1.39.0 (2026-11-06): 0741 radar unit folded - seventy-fourth consecutive pass with a Mac device-access blocker, thirty-fifth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 24h10m, unchanged since the 0704 pass, five invokes zero responses, no probe run since last_seen unrefreshed, recovery-device health check and native repair both timed out after 25s - new against the 0342/0634/0704 passes, which made no recovery-device attempts, matching the 0234 signature); release-day check for the slot unexecuted (duel day 5, planned 06:03 local, expires 10:03 local) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; seventy-fourth occurrence commented onto Issue #282 by this run.

- 1.40.0 (2026-11-06): 1104 radar unit folded - seventy-seventh consecutive pass with a Mac device-access blocker, thirty-eighth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 27h45m, unchanged since the 0934 pass, five invokes zero responses, no probe run since last_seen unrefreshed, recovery-device health check timed out after 25s, matching the 0741/0832/0934 signature); release-day check for the slot unexecuted (duel day 5, planned 10:03 local, expires 14:03 local) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; seventy-seventh occurrence commented onto Issue #282 by the 1132 run.

- 1.41.0 (2026-11-06): 1235 radar unit folded - seventy-eighth consecutive pass with a Mac device-access blocker, thirty-ninth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 29h, unchanged since the 1104 pass, five invokes zero responses, no probe run since last_seen unrefreshed, recovery-device health check timed out after 25s, matching the 0741/0832/0934/1104 signature); release-day check for the slot unexecuted (duel day 5, planned 10:03 local, expires 14:03 local) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; seventy-eighth occurrence commented onto Issue #282 by this run.

- 1.42.0 (2026-11-06): 1507 radar unit folded - eightieth consecutive pass with a Mac device-access blocker, forty-first in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 31h36m, unchanged since the 1235 pass, five invokes zero responses, no probe run since last_seen unrefreshed, recovery-device repair and health check both timed out after 25s, matching the 1235/1349 signature); release-day check for the slot unexecuted (duel day 5, planned 14:03 local, expires 2026-11-07 02:03 UTC) - the day 4 stack sits unclaimed and the release window runs until 2026-11-06 18:00 local; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; eightieth occurrence commented onto Issue #282 by this run.

- 1.44.0 (2026-11-07): 0011 radar unit folded - ninety-third consecutive pass with a Mac device-access blocker, fifty-fourth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 40h45m, unchanged since the 1025 pass, four invokes zero responses, no probe recorded since last_seen unrefreshed, recovery-device health check and native repair both timed out after 25s, matching the 0741/1235/1349/1507/1934 signature); stack-day unit (duel day 6, Enemy Buster) whose window stamp agrees with the live posture this time - the 1934 stamp-staleness class did not recur; correction: the record's "unread since the 2317 close" dating is superseded by the 1005 on-screen read (stored 0 of 40, stamina 81, points 219) which stands as the last live read; the pass first resolved five records-PR action-log conflicts (PRs 351, 350, 301, 265, 256, union merge, no lines dropped, all re-checked MERGEABLE/CLEAN); ninety-third occurrence commented onto Issue #282 by this run. (1.43.0 carries the 1934 section without a changelog line; the numbering is preserved, not rewritten.)

- 1.45.0 (2026-11-07): 0132 radar unit folded - ninety-fourth consecutive pass with a Mac device-access blocker, fifty-fifth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 41h57m, unchanged since the 0011 pass, six invokes zero responses, no probe recorded since last_seen unrefreshed, recovery-device repair with target "web" rejected as invalid_command_params - the recovery device's schema takes only "native" - corrected native repair and health check both timed out after 25s, matching the 0011/2257/2134 signature); stack-day unit (duel day 6, Enemy Buster) whose window stamp agrees with the live posture - the 1934 stamp-staleness class did not recur; the pass staged the pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07, 001 not_before 17:30 local, 002 not_before 18:30 local); the branch already held this unit failed by ticker-0011, so the 0011 done file is kept and this record is the re-attempt evidence; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; ninety-fourth occurrence commented onto Issue #282 by this run.
- 1.46.0 (2026-11-07): 0304 radar unit folded - ninety-seventh consecutive pass with a Mac device-access blocker, fifty-eighth in the worsened zero-response form (Mac mini offline, last_seen 15:36:52Z stale about 43h30m, unchanged since the 0234 pass, five invokes zero responses, no probe recorded since last_seen unrefreshed, recovery-device health check timed out after 25s, matching the 0234/0204/0127 signature, no repair attempt this pass); stack-day unit (duel day 6, Enemy Buster) whose window stamp agrees with the live posture - the 1934 stamp-staleness class did not recur; the pass first resolved the PR 382 action-log conflict by union-merging main (commit 87ef39a4c4, no lines dropped); the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; ninety-seventh occurrence commented onto Issue #282 by this run.
- 1.48.0 (2026-11-07): 1104 radar unit folded - one-hundred-eighth consecutive pass with a Mac device-access blocker, second in the new form (Mac mini back online, last_seen 2026-11-07T18:41:20Z fresh, both transports healthy; Last War window 1920x1080, pid 59735, still at (0, -360) off-Space, unchanged from the 1020 pass; eleven invokes, zero game screens, four capture attempts failed with the identical capture failure); new: open_app returns outcome_unknown and produces no relaunch or move, and set_window_frame is gated on an observation that cannot be produced, so neither is a live route while capture is down; Mission Control and Ctrl+Right deliberately not retried per the 1020 lessons folded into alliance-help 1.27.0 - the pass applied them instead of re-learning them; the Dock-icon unblock stands and still needs the owner at the Mac; stack-day unit (duel day 6, Enemy Buster) whose window stamp agrees with the live posture; queue stats reconcile with the planner-1040 read (done 1122 to 1127, inbox 79 to 74, exactly the 5 expired 0657-slot units); the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; one-hundred-eighth occurrence commented onto Issue #282 by this run. (1.47.0 carries the 0734 section without a changelog line; the numbering is preserved, not rewritten.)
- 1.49.0 (2026-11-07): 1608 radar unit folded - one-hundred-twelfth consecutive pass with a Mac device-access blocker, sixth in the new form (Mac mini back online, last_seen 2026-11-07T23:44:36Z about 32 minutes stale, both transports healthy; Last War window 1920x1080, pid 59735, still at (0, -360) off-Space, unchanged from the 1020/1104/1204/1452 passes; four invokes, zero game screens, four capture attempts failed with the identical capture failure); recovery routes deliberately not retried per the 1020 lessons, the Dock-icon unblock stands and still needs the owner at the Mac; the pass itself commented the one-hundred-twelfth occurrence onto Issue #282, so this run posts no duplicate comment; stack-day unit (duel day 6, Enemy Buster) whose window stamp agrees with the live posture; queue stats inbox 79 done 1143 at 00:08Z; the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read.

- 1.50.0 (2026-11-07): 1633 and 1655 units folded - capture channel working again in the 1633 arms-race and 1655 harvest/survivors/training units after the 1020-1608 capture-failure run (Issue 282, no new occurrence, no new comment, issue stays open; window read 788x1083 in the 1633 pass vs 1920x1080 in the failure passes); incidental radar reads during the 1633 donations detour (BASE tap 920,975 landing on the radar map, Lv.13, points 237 to 259, stored 19/40 to 0/40, stamina 100 to 35, 19 tasks completed between screenshots with no executor tap - owner play or mis-tap, unverified, the next radar unit re-reads; the 1005 close stands as the last live read by a radar unit); blue droplet over the blue truck is a radar-task locator, not a loot bubble (Claim All left untouched).

## What the PR 237 merge settled - 1450 re-read as a stack-day unit

- PR 237 (lastwar-tool-developer, Refs #235) merged
  2026-11-03 16:38 local, during this organizer run,
  after the run's first three folds were already
  committed. It changes only _tools_/duel.py: the duel
  day is now computed in the timezone the schedule
  declares (America/Los_Angeles), with day boundaries
  at 19:00 local wall times, instead of a naive
  datetime.now().
- Re-read of the 1450 unit: the unit ran on duel day 2
  (Base Expansion, stack), not day 3 (Age of Science,
  release). The 1532 fold's classification of 1450 as
  a release-day unit is corrected here, not left
  standing. The claims themselves are unaffected as
  resources: 27 rewards claimed, radar points 139 to
  166 (radar points, not duel points - consistent
  with the dialog that no duel points were granted
  that day). The claim-anyway rationale (resources
  certain, holding the stack risks task expiry) still
  stands; the "release standard governs" justification
  is superseded, since the unit was a stack-day unit.
  Its partial status stands on the same grounds as
  before (6 pins left unattempted, Quick Execute 4
  tasks left for the next unit).
- Standing rule going forward: the next radar release
  decision uses the corrected tool, and any future
  tool-versus-stamp disagreement is settled against
  the VS panel itself plus the tool's clock basis,
  never by assuming the schedule is stale or the
  stamp lags. The stored-versus-completable open
  question (Claim All 8 after Quick Execute batches
  of 3 and of 2, returning marches the leading
  hypothesis) is untouched by this resolution.
- Issue #235 commented by this run with this
  resolution; the issue is NOT closed here - closure
  belongs to the daily retro once the next radar unit
  after merge reports the PT day.


## What the 2026-11-03 1913 unit added - release day, 17 claims, no TIPS dialog, pins carried

- Ticker-1904, unit radar-2026-11-03-1803, about 19:05 to
  19:13 local, status partial. Evidence in
  `_records_/2026-11-03/radar-tasks/1913-queue-run.md`.
  Posture: release (live duel.py at entry: duel day 3, Age
  of Science, radar posture release; the unit window text
  still read "duel day 2 - radar stack", stamped at
  production before the posture flipped, and the live
  posture governs).
- Entry: the game was left on the Others' Trucks panel by
  the previous trucks unit (Plunder Count Today 2/4, not
  this unit's work, nothing plundered); its back arrow at
  norm (56,939) returned to the base on the first tap.
  First radar attempt wrong: a visual-grounding point at
  norm (55,560) opened the Your Truck panel (Today's Trade
  Count 3/5), not the radar - nothing tapped there, backed
  out untouched. Second attempt: a tap at norm (57,715),
  inside the proven 52-62, 704-727 cluster from the 0636,
  1010 and 1450 units, opened the radar on the first tap.
  Entry verified by its own reads: Lv.13, radar points
  166, stored 10/40, stamina 120, restore line "12 Radar
  Task(s) will be restored in 02:22:02" at entry (later
  frames 02:21:58 down to 02:20:34, and the full-restore line
  "Fully restore at 11-4 15:31:43 local time" once stored
  hit 0/40).
- Bottom-bar geometry, this window: the buttons respond at
  norm (500,952) (visual-grounding point for the Quick
  Execute button, confirmed by three successful Quick
  Execute taps and three successful Claim All taps at the
  same point). The 1450 unit's y-925 lesson does not
  transfer to this window geometry; the grounded point
  governs.
- What was done: Quick Execute 1: 4 tasks, stamina 120 to
  80, stored stayed 10/40, bar flipped to Claim All ("8
  task rewards can be claimed"). Claim All 1: 8 rewards
  claimed, NO TIPS dialog appeared (contrast the 1450 unit,
  where every Claim All opened the "will not grant
  Alliance Duel points" TIPS dialog). Popup: chest-like
  icon 25 (icon identity not resolved from the popup alone,
  recorded as seen), radar item 80, EXP 12.0M, drone item
  1.6K, blue triangle 450, food 4.0M, coin 1.7M, iron 1.3M.
  Radar points 166 to 174, stored 10/40 to 2/40. Quick
  Execute 2: 4 tasks, stamina 80 to 40, stored stayed 2/40.
  Claim All 2: 7 rewards claimed, again no TIPS dialog.
  Popup: radar item 70, EXP 10.0M, blue triangle 450, drone
  item 800, iron 1.5M, food 2.8M, coin 1.6M. Points 174 to
  181, stored 2/40 to 0/40. Quick Execute 3: 2 tasks,
  stamina 41 to 21 (one stamina regenerated between the
  reads), stored stayed 0/40. Claim All 3: 2 rewards
  claimed, again no TIPS dialog. Popup: radar item 20, EXP
  4.8M, iron 980.4K, food 980.4K, coin 565.2K. The bottom bar
  then showed no offer at all: no Quick Execute, no Claim
  All.
- Totals: rewards claimed 17 (8 + 7 + 2); radar points 166
  to 183 (+17, exactly the claim count); tasks executed 10
  via Quick Execute (4 + 4 + 2), 100 stamina spent, 1
  regenerated, 120 to 21. Popup resources summed: radar
  items 170, EXP 26.8M, drone items 2.4K, blue triangles
  900, iron 3.7804M, food 7.7804M, coin 3.8652M, plus the
  unresolved chest-like icon 25 from Claim All 1.
- Duel-points note, NOT a settlement: no TIPS dialog on
  any of the three post-18:00-rollover Claim All taps is
  new evidence for Issue #235 (duel.py said radar claims
  score on day 3; the 1450 unit's pre-rollover TIPS dialog
  said they do not). No VS panel read was taken and no
  duel-points figure is claimed. The delta test (read duel
  score, claim one batch, read again) is still owed, and
  Issue #235 closure belongs to the daily retro.
- Closing state, live reads: radar Lv.13, points 183,
  stored 0/40, stamina 21, restore line "Fully restore at
  11-4 15:31:43 local time", bottom bar with no offer.
- Pin inventory at close (visible frame only, not a
  whole-map census): a purple question-mark story pin top
  left, a purple axe pin top right, a purple axe pin
  centre, a blue axe pin lower centre. No red dot was
  visible on any of them in this frame. The portrait
  squares on the map are alliance member markers, not
  radar pins. All four pins were left unattempted.
- Per the release standard, pins left unattempted make
  this unit partial, never done. The pins are the same
  standing pins the 1450 unit left (its frame showed the
  same axe pins plus skull pins since claimed through
  Claim All), so this is the second consecutive partial
  carrying the same pin blocker. Under rule R7 the pins
  become the FIRST action of the next radar unit, starting
  with the question-mark story pin whose flow is verified
  in the activity metadata, before any Quick Execute
  batch. Tracker untouched for partial, per the queue
  rules.


## What the 2026-11-03 2317 unit added - release day, story pin completed, March centre 500,751, 11 claims, pins carried third time

- Ticker-2304, unit radar-2026-11-03-2203, about 23:05
  to 23:17 local, status partial. Evidence in
  `_records_/2026-11-03/radar-tasks/2317-queue-run.md`.
  Posture: release (live duel.py at entry: duel day 3,
  Age of Science, radar posture release; the unit window
  text reads "duel day 3 - radar release", matching the
  live posture).
- Entry: radar entry on the first tap at norm (57,715),
  the proven dish cluster from the 0636, 1010, 1450 and
  1913 units. Entry verified by its own reads: Lv.13,
  radar points 183, stored 2/40, stamina 120, restore
  line "12 Radar Task(s) will be restored in 04:24:25"
  at entry (later frames 04:23:18 down to 04:15:18, and
  the full-restore line "Fully restore at 11-5 03:31:43
  local time" once stored hit 0/40). Bottom-bar buttons
  in this window respond at norm (500,952), confirmed
  by two successful Quick Execute taps and two
  successful Claim All taps at that point.
- Pins first (rule R7, from the 1913 unit): the 1913
  unit's first-action pin was the purple question-mark
  story pin top left. This unit worked it first, before
  any Quick Execute batch. Pin tap at norm (231,323)
  opened the card: "A Distressed Survivor", "Look for
  survivors after the cold wave...", "Break the ice to
  view rewards", countdown 04:03:28. Go at norm
  (500,946) jumped to the world map task location:
  "Thawing Soon 00:02:51", snowflake bar 1,000/1,000.
- Ground contextual buttons, never estimate them: a
  hammer tap at the estimate (449,548) did nothing; a
  visually grounded tap at (490,600) opened the deploy
  panel (Squad 1, 25.17M vs Unknown, Evenly Matched,
  Unit Count 2,231/2,231, march 8 seconds, stamina cost
  shown as -5). March button: taps at (500,691),
  (500,715) and (500,730), a 1 second long-press at
  (500,700) and a double-click at (500,691) all left
  the panel open with stamina unchanged. A visually
  grounded tap at (500,751) closed the panel. The March
  button's true centre is (500,751) in this window
  geometry, matching the zombie-invasion March lesson
  (500,755) - the visual centre estimate sits above
  the button's active area.
- Story completion, verified step by step: march
  verification came from the pin itself, not from
  stamina - back on the radar, the same pin's card now
  showed the revealed rewards (survivor x1, paw print
  x200, black rock 207.3K), exactly the verified story
  flow's step 4. Go again at (500,946) returned to the
  task location with the simplified card; the green
  magnifier button grounded at (499,599) (an estimate
  tap at (449,553) did nothing) opened the story dialog
  ("Are you Violet?"). Tapping the bottom of the dialog
  advanced it through "...and helped delay CL-7." to
  the closing line "Take me to your base. I'll prove it
  through my actions!" and the top banner "...th the
  treasure map - congrats!". One more bottom tap closed
  the dialog. Back on the radar, the story pin is gone
  in the closing frames: the pin completed and its
  reward was paid through the Claim All below. This is
  the first story-pin completion recorded since the
  2026-10-25 pin.
- Stamina discrepancy, unresolved and recorded, not
  smoothed over: the radar stamina read stayed 120
  through the story march despite the shown -5 cost,
  and the panel close plus March Queues 0/4 did not by
  themselves prove dispatch. Dispatch is proven by the
  pin-card reward reveal above. The story march's shown
  -5 never moved the radar stamina read in this unit.
- What was done: Quick Execute 1: 2 tasks, stamina 120
  to 100, stored stayed 2/40. Bar flipped to Claim All:
  "9 task rewards can be claimed". Claim All 1: 9
  rewards claimed, no TIPS dialog (as in the 1913 unit;
  contrast the 1450 unit's pre-rollover TIPS dialog).
  Popup: radar item 80, paw print 200, blue triangle
  948, EXP 7.6M, drone item 1.6K, black rock 207.3K,
  coin 1.9M, iron 2.0M, food 1.5M, Lv.1 chest 1,
  survivor portrait 1. Radar points 183 to 192 (plus 9,
  exactly the claim count), stored 2/40 to 0/40. Bar
  flipped to Quick Execute: "You can complete 1 tasks,
  requires 10 Stamina." Quick Execute 2: 1 task, stamina
  100 to 91 (10 spent, 1 regenerated), stored stayed
  0/40. Bar flipped to Claim All: "2 task rewards can
  be claimed". Claim All 2: 2 rewards claimed, again
  with no TIPS dialog. Popup: radar item 20, EXP 3.3M,
  drone item 800, food 1.2M, coin 319.2K, iron 316.8K.
  Radar points 192 to 194 (plus 2, exactly the claim
  count), stored 0/40. The bottom bar then showed no
  offer at all: no Quick Execute, no Claim All.
- Totals in this unit: rewards claimed 11 (9 + 2);
  radar points 183 to 194 (plus 11, exactly the claim
  count); tasks executed 3 via Quick Execute (2 + 1),
  plus the story pin task completed through its full
  flow. Popup resources summed: radar items 100, EXP
  10.9M, drone items 2.4K, blue triangles 948, coin
  2.2192M, iron 2.3168M, food 2.7M, plus paw prints 200,
  black rock 207.3K, Lv.1 chest 1, survivor 1. Stamina
  120 to 91 net (minus 29: 30 spent on Quick Execute, 1
  regenerated; the story march's shown -5 never moved
  the radar stamina read, see above).
- Duel-points note, NOT a settlement: no TIPS dialog
  on either Claim All tap, matching the 1913
  post-rollover unit and continuing the evidence for
  Issue #235 (duel.py says radar claims score on day 3;
  the 1450 unit's pre-rollover TIPS dialog said they do
  not). No VS panel read was taken and no duel-points
  figure is claimed. The delta test (read duel score,
  claim one batch, read again) is still owed, and Issue
  #235 closure belongs to the daily retro.
- Closing state (live reads, same unit): radar Lv.13,
  radar points 194, stored 0/40, stamina 91, restore
  line "Fully restore at 11-5 03:31:43 local time",
  bottom bar with no offer.
- Pin inventory at close (visible frames only, not a
  whole-map census): a blue axe pin top left, a purple
  arrow pin centre, and a blue skull pin top centre
  carrying a red dot (seen in the frame before Claim
  All 2; the closing frame's map view had shifted and
  showed only the axe and arrow pins, both with no red
  dot visible). The story question-mark pin is gone,
  completed in-unit.
- Per the release standard, pins left unattempted make
  this unit partial, never done. The axe and skull pins
  are the same standing pins carried since the 1450 and
  1913 units, so this is the third consecutive partial
  carrying the same pin blocker. Under rule R7 the pins
  become the FIRST action of the next radar unit,
  starting with the red-dotted blue skull pin (a
  finished-task pin pays instantly on tap, per the
  activity metadata) and then the axe pins, whose class
  is still unidentified - the next unit must tap them
  under the release handling rule rather than inventory
  them again. The map-view shift between the pre-claim
  and closing frames means the next unit must re-ground
  every pin point on its own current screenshot, never
  reuse the positions recorded here blindly.
- Tracker untouched for partial, per the queue rules.
  No earlier claim superseded.

- 1.25.0 (2026-11-04): 0334 unit folded: Esc crash route repeated - the Alliance panel back arrow stalled on two taps and an Esc press exited the app outright (standing rule reaffirmed: Esc is never used); relaunch restored the session with no observed state loss. Dish entry on the first tap at norm (53,708) with badge 6, verified by Lv.13, points 194, stored 3/40, stamina 156. STAMINA CAP CORRECTED: the 156 entry read supersedes the old cap 120 - the cap is at least 156, the old 120 figure is not a cap, and no new cap value is claimed (mechanism unverified); Quick Execute spent 20 (156 to 136) for 2 tasks, consistent with 10 per task. Five finished-task pins claimed instantly, +1 point each (points 194 to 199, stored 3/40 to 0/40). Doom Elite pin identified: the red-dotted blue skull pin (552,360) is Defeat Doom Elite 1 times (food 920.4K, iron 920.4K, coin 588.0K, radar item 300, drone item, countdown 07:56:50); the rally is BLOCKED - the Rally button did not launch on two clicks and one long-press at grounded (501,735), no march, no stamina change, filed as Issue #268; per rule R2 the next unit must change method (different squad, different rally time, or a fresh entry route) before retrying. Rare Farmland gathering pin identified: purple axe pin bottom centre (433,720), food 132.0K, radar item 10, countdown 07:52:38, NOT started (a march near unit end would leave its reward unclaimed) - left first for the next unit via Go, the pickaxe step and the radar claim. R7 next-unit order is now: Doom Elite rally retry with changed method first, then the Rare Farmland pin, then remaining pins re-grounded on the unit's own screenshot. Bottom-bar buttons respond at norm (500,952). Claim All: 6 rewards, points 199 to 205 (+6, exactly the claim count), no TIPS dialog (consistent with the post-rollover units; the duel delta test is still owed, no VS panel read was taken). Unit totals: 11 rewards claimed, 2 tasks executed, popup resources radar items 390, EXP 6.1M, blue triangles 906, coin 2.4948M, iron 2.5076M, food 3.1028M, drone items 800, paw prints 3, 5-minute speedups 6, 1-minute speedups 65, Lv.1 chest 1. Closing state: Lv.13, points 205, stored 0/40, stamina 136, restore line Fully restore at 11-5 03:xx partly obscured by a toast (not quoted as an exact figure). Base-view harvest bubbles seen on return were not touched (one unit, one type). No earlier claim superseded except the stamina cap above.

## What the 2026-11-04 0720 unit added - release day, Doom Legion claimed, Farmland gathering dispatched, skull pin opens no card

- Unit radar-2026-11-04-0603 by ticker-0706, about 07:07 to 07:20 local, status partial. Evidence in `_records_/2026-11-04/radar-tasks/0720-queue-run.md`. Duel day 3, radar release posture, day ends 2026-11-04 19:00 local.
- Entry, re-confirmed: base left icon column dish icon grounded fresh this unit at norm (53,710) - first tap opened the radar screen, not Secret Command Post or Intercity Trade. The centre matches the 0334 read (53,708) within grounding tolerance.
- Entry reads match the 0334 close exactly, so nothing moved between units: Radar Lv.13, radar points 205, stored 0/40, stamina 136. The Day 2 stack was already empty at entry - no bottom action bar, no Quick Execute offer and no Claim All. Restore line at entry: 12 tasks restored in 02:21:22; fully restore at 11-5 03:31:43 local time at close. That exact full-restore figure replaces the 0334 close's partly obscured 03:xx read and matches the 2317 unit's exact figure.
- Portrait pin (upper right at entry), DONE: card "Eliminate the Doom Legion - Destroy Doom Legion's base!", countdown 04:24:21, rewards food 11.2M, iron 11.2M, coin 7.4M, 300 (purple swirl item), 1.6K card item. Go jumped to the world map legion base card (Power 6,937,000, Kills 0, Alliance [AP3x]The Apex). Attack panel: squad 1, Unit Count 2,231/2,231, power 25.18M vs Unknown, "Evenly Matched", march 00:00:30, stamina cost 5. Marched, base destroyed, returned to radar: bottom bar read "1 task rewards can be claimed". Claim All paid exactly the card preview: iron 11.2M, food 11.2M, coin 7.4M, 300, 1.6K; radar points 205 to 206 (+1, exactly the claim count, consistent with the prior points-per-claim pattern). Portrait pin gone after the claim.
- Doom Legion tag qualification, recorded not smoothed over: the world-map base card carried the own-alliance tag [AP3x]The Apex, the same tag pattern as the 0636 ambiguous pin, yet the attack proceeded, the base was destroyed and the claim paid exactly. The tag alone is therefore not a proven block, and the 0636 "Never attack on an ambiguous card" note is qualified in the open questions accordingly. The 0636 contested-location toast mechanism itself is still unexplained and is not reproduced here - card text must still be read before any attack.
- Purple axe pin (bottom centre at entry), IN PROGRESS: card "Rare Farmland - Allow Troops to gather incredibly fast!", rewards food 132.0K + 10 (purple swirl item), countdown 04:20:23. Go jumped to Lv.28 Farmland (1,800,000/1,800,000, Gathering Speed +20000%, despawns in 04:19:55). Green pickaxe button opened the gather panel: Unit Count 2,231/2,231, gathering amount 1.8M/1.8M, gathering time 00:08:41, expected finish 2026-11-04 07:25, march 00:00:08, stamina cost 0. Marched. Pin faded on the radar map (gathering in progress). Reward claim falls to a later unit after the squad returns (about 07:25 plus return march). Handling change from the 0334 unit, which deliberately did NOT start this pin (a march near unit end would leave its reward unclaimed): the 0720 unit started it mid-morning with the finish inside the next tick window, so the claim is now pending rather than deferred by choice.
- Blue skull pin (centre right), UNRESOLVED, named blocker carried forward: tapped three times (pin centre twice, pin tip once) and long-pressed once as the changed method - no card opened in any attempt. Observed effects only: a radar sweep animation from the base toward the pin and a small circular badge appearing at the pin's lower left. The two other pins opened their cards on the first tap each, so the skull pin's taps are believed to have landed but the pin does not respond with a card. This is a different blocker from Issue #268 (Doom Elite rally button inert after the card opened): here no card opens at all.
- Skull identity tension, unresolved: the 0334 R7 order put the Doom Elite rally retry with a changed method FIRST for the next unit, then the Rare Farmland pin. The 0720 unit did the Farmland pin but no Doom Elite rally retry, and its entry pin inventory (portrait, purple axe, blue skull centre right) contains no identified Doom Elite pin. The centre-right skull is not recorded as the 0334 Doom Elite pin: its position (centre right vs top centre), its red-dot state (none mentioned vs red dot) and its behaviour (no card vs card opened) all differ. The #268 rally retry therefore remains owed, and the next unit must re-ground every pin on its own screenshot and identify the skull pin's class before any rally attempt - it must not assume the skull pin is Doom Elite, and must not retry the rally on an unidentified pin.
- Closing reads: radar points 206, stored 0/40, stamina 131 (136 minus the 5-point legion march; gathering cost 0). The legion march cost DID move the stamina read exactly, which contrasts with the 2317 story-march anomaly (shown -5, read stayed 120): the anomaly is specific to that story flow, not a general stamina-read rule. Restore line at close: 12 tasks restored in about 02:13, fully restore at 11-5 03:31:43 local time. Bottom bar at close: none (no pending claims). No diamonds, rubies or money spent; no paid button tapped; no Buy in any stamina panel (no stamina panel was opened).
- Duel scoring, still owed: the VS panel was not opened in this unit, so duel score before/after was not read. The Issue #235 delta test (read duel score, claim one batch, read again) is still owed, and no duel-points figure is claimed from this unit. No TIPS dialog is reported in this unit.
- Tracker untouched for partial, per the queue rules; the next tick re-produces this regular. No earlier claim superseded except the restore-figure confirmation and the Doom Legion tag qualification above.

## What the 2026-11-04 1005 unit added - release day, 13 claims, points 206 to 219, Doom Elite pin march left open per rule R7

- Unit radar-2026-11-04-1003 by ticker-1004, about 10:05 to 10:20 local, status partial. Duel day 3, release posture. Evidence in `_records_/2026-11-04/radar-tasks/1005-queue-run.md`. No diamonds spent, no paid button tapped.
- Entry, continuity exact: radar entered from the base left icon column, dish icon re-grounded fresh on the current screenshot at norm about 53,705 before the tap; the tap opened the radar on the first try. Entry reads match the 0720 close exactly except for stored tasks: Lv.13, radar points 206, stored 3 of 40 (was 0 of 40 at the 0720 close), stamina 131. Restore line at entry: "12 Radar Task(s) will be restored in 05:23:45". The stored 3 of 40 at entry is the restore's movement since 0720, not a new stack.
- Work done, both batches verified: Quick Execute batch 1 - 4 tasks, 40 stamina, stamina 131 to 91. Claim All batch 1 - 10 task rewards claimed, radar points 206 to 216. Popup rewards read: radar discs 100, EXP 10.7M, drone parts 726, blue item 1.6K, iron 2.4M, food 2.3M, coin 2.0M, Lv.1 chests 2. Quick Execute batch 2 - 1 task, 10 stamina, stamina 91 to 81; the bar offered this batch only after the first Claim All cleared, repeating the one-offer-at-a-time behaviour. Claim All batch 2 - 3 task rewards claimed, radar points 216 to 219; the second popup contents were not read before dismissal, so only the count (3) and the points delta are recorded for this batch. Totals: 13 claims, points +13 (exactly 1 per claim, as in every prior unit), stored closed at 0 of 40, bottom bar offer gone, stamina 131 to 81 (50 spent, exactly the two Quick Execute batches).
- Restore line, recorded as read with an unexplained step: at close it read "12 Radar Task(s) will be restored in 05:21:57", a drop of only 01:48 against about 15 minutes of unit elapsed time. No mechanism is claimed for the small step; the two restore reads are kept as read and the discrepancy is not smoothed over.
- Pin scan, finished-task pins confirmed as a class: the pins standing at entry (purple skull, purple handshake, grey skull, purple arrow, alliance portraits) cleared during the two Claim All batches - they were finished-task pins paying through Claim All, not separate pin tasks. A radar clear is therefore still never proven by the bottom bar alone, and a pin inventory at entry that later clears through Claim All is a finished-task pin inventory, not leftover work.
- Remaining pin, identified: blue skull pin, tapped and identified as "Defeat Doom Elite 1 times" ("Traces of Doom Elites found. Please send Heroes for investigation ASAP."), countdown 01:26:27 at tap, rewards food 920.4K, iron 920.4K, coin 588.0K, radar discs 300, one blue item. Go opened the world map card: Lv.1 Doom Elite, stamina cost 20, suggested power 1,096,500, despawn timer 23:59:53. The pin countdown (01:26:27) and the world-card despawn timer (23:59:53) are different timers and are not merged here.
- Remaining work, rule R7: the march was NOT started - the unit 15 minute cap was reached with the card open on the target. No stamina was spent on the pin and no attack was launched. Per rule R7, the Doom Elite march is the first action of the next radar unit: the card is already open on the target, cost 20 stamina, suggested power 1,096,500, countdown about 01:26 at 10:19 local.
- Qualification against the 0720 section, stated not smoothed over: the 1005 record does not record the remaining pin's map position, so this section does NOT assert it is the 0720 centre-right blue skull pin (which opened no card on three taps and a long-press). Cross-check, not an assertion: the 1005 pin reward set (food 920.4K, iron 920.4K, coin 588.0K, radar discs 300, one blue item) is identical to the 0334 Doom Elite pin reward set, and its countdown decay is roughly consistent (07:56:50 at about 03:34 falling to 01:26:27 at about 10:19, about 6:30 of drop over about 6:45 elapsed), so the 1005 pin may be that same 0334 pin still standing - but with no position recorded in the 1005 record this is not asserted. The 0720 no-card skull question therefore stays open, and the 1005 identification does not close Issue #268 either: #268 is the Doom Elite rally button inert after the card opened in the 0334 unit, and this unit never reached a rally or march button - the march was deferred by the time cap, not blocked by a button. No comment was posted on #268: no rally attempt was made, so there is no new evidence for it.
- Tracker untouched for partial, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-04 1534 unit added - screen-capture failure, seventh consecutive pass, nothing read

- Unit radar-2026-11-04-1403 by ticker-1534, about 15:34 to 15:47 local, status failed. Evidence in `_records_/2026-11-04/radar-tasks/1534-queue-run.md`. No diamonds spent, no paid button tapped.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: computer.observe (compact) failed twice in session cc-466 with "Failed to start stream due to audio/video capture failure"; in fresh session cc-467 computer.control activate selected the LastWar window for background input but captured no observation, computer.observe (compact) failed with the same error, computer.control screenshot failed with the same error, and a final computer.observe after the connection health check failed with the same error. The device connection health was healthy on both native and web transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The radar screen was never entered or verified, no stored task count, stamina figure, restore line or pin scan was read, and no Quick Execute, Claim All or pin march was run.
- Recurrence, not a new failure class: this is the seventh consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434, ticker-1504 donations 1504, ticker-1534 radar 1534), now across seven activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 instead of filing a duplicate, and this run comments the seventh and eighth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Posture check, PT-corrected: the unit window reads duel day 3, radar release. A naive run of tools/duel.py on this UTC VM printed day 4, Train Heroes, stack - but the duel anchor (2026-10-25T19:00 local) is America/Los_Angeles time, and recomputed in PT today is still day 3, Age of Science, release posture, matching the unit window and the 1005 unit. The next radar unit must use the PT-corrected posture, not a raw duel.py print from this UTC VM.
- Remaining work, carried forward and time-bounded: the 1005 unit left a Doom Elite pin march as the first action of the next radar unit per rule R7 (cost 20 stamina, suggested power 1,096,500); its countdown read 01:26:27 at 10:19 local, so it expired about 11:46 local and is almost certainly gone - the next unit must re-check the pin live rather than assume it. The restore line at the 1005 close pointed to 12 tasks restoring about 15:42 local, right inside this pass's window, so the next unit should expect a fresh stored batch. Both expectations are superseded by the next live read.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-04 1904 unit added - screen-capture failure, fourteenth consecutive pass, nothing read

- Unit radar-2026-11-04-1803 by ticker-1904, about 19:04 to 19:15 local, status failed. Evidence in `_records_/2026-11-04/radar-tasks/1904-queue-run.md`. No diamonds spent, no paid button tapped.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: computer.session cc-479 started, list_apps confirmed LastWar as target, computer.observe (compact) failed with "Failed to start stream due to audio/video capture failure"; computer.control activate selected the LastWar window for background input but captured no observation, same error; computer.observe (compact) failed again with the same error while connection.health at the same time reported both transports connected and healthy; session cc-479 ended, fresh session cc-480 started, computer.control activate again selected the window with no observation, same error, and computer.observe (image view) in cc-480 failed with the same error. Three observation attempts across two sessions, two views, plus two activates, all the identical signature. LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080 and Google Chrome was frontmost.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The radar screen was never entered or verified, no stored task count, stamina figure, restore line or pin scan was read, and no Quick Execute, Claim All or pin march was run. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence, not a new failure class: this is the fourteenth consecutive ticker pass to fail on this exact blocker (the 12:35, 13:33, 13:44, 14:34, 14:39, 15:04, 15:34, 16:34, 17:07, 17:34, 18:04, 18:34 and now 19:04 passes of 2026-11-04), and the first to continue past the 19:00 reset - the blocker is not reset-bound. The blocker is filed as Issue #284 (tooling, 11 comments); this pass commented on #284 instead of filing a duplicate, and this run comments the thirteenth and fourteenth occurrences onto the knowledge Issue #282.
- Posture check: the unit window reads duel day 3, radar release, but that slot (18:03 local) predates the 19:00 reset. Live posture at this pass, recomputed with tools/duel.py under America/Los_Angeles time, is duel day 4, Train Heroes, radar STACK: complete ordinary tasks but do not claim, do not tap pins. The unit's work, when the screen returns, is the stack execution, not the stale release wording.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as a stored-count or claim state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Remaining work, carried forward and time-bounded: this unit's stack work (enter and verify the radar screen, run Quick Execute batches until no offer remains, record stored count, pending reward count, stamina, restore line and the pin inventory untapped) is still owed. The 1005 unit's Doom Elite pin expired about 11:46 local and is gone; the restore line at the 1005 close pointed to 12 tasks restoring about 15:42 local, so the next live unit should expect a fresh stored batch. Both expectations are superseded by the next live read.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this one unit rather than claiming further units: every further unit would fail on the same capture error and burn attempts, so the inbox is left for the first pass after capture recovers.

## What the 2026-11-04 2334 unit added - screen-capture failure, twenty-second consecutive pass, nothing read

- Unit radar-2026-11-04-2203 by ticker-2334, about 23:34 to 23:47 local, status failed. Evidence in `_records_/2026-11-04/radar-tasks/2334-queue-run.md`. No diamonds spent, no paid button tapped.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: session cc-497, computer.control activate selected the LastWar window for background input but captured no observation, "Failed to start stream due to audio/video capture failure", and computer.observe failed twice with the same error; session cc-498, computer.control activate again selected the window with the same capture failure and computer.observe failed again with the same error. Five capture attempts in total, all with the identical error. The device connection health was healthy on both transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The radar screen was never entered or verified, no stored task count, stamina figure, restore line or pin scan was read, and no Quick Execute, Claim All or pin march was run.
- Stack posture, no leaked claims: this was a stack-posture unit (duel day 4, window "duel day 4 - radar stack"): on a stack day nothing is claimed in any case, so the loss is the unexecuted ordinary tasks and the missing closing reads, not leaked claims.
- Recurrence, not a new failure class: this is the twenty-second consecutive ticker pass to fail on this exact blocker (the 16th through 21st were ticker-2034 donations, ticker-2104 harvest, ticker-2134 survivors, ticker-2204 gifts, ticker-2234 shop-claims and ticker-2304 donations; the 22nd is this radar unit), now across nine activities, and the inbox held 69 units at this pass. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 instead of filing a duplicate, and this run comments the twenty-second and twenty-third occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Remaining work, carried forward: the 1904 section's stack work is still owed (enter and verify the radar screen, run Quick Execute batches until no offer remains, record stored count, pending reward count, stamina, restore line and the pin inventory untapped). The 1005 unit's Doom Elite pin expired about 11:46 local and is gone; the restore line at the 1005 close pointed to 12 tasks restoring about 15:42 local, so the next live unit should expect a fresh stored batch. Both expectations are superseded by the next live read.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh). The View menu lists "Enter Full Screen" (read from the menu-action error listing in session cc-505, repeated probe in cc-508 with the menu unchanged), so the app is NOT in native fullscreen: it is a windowed 1920x1080 window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission (Chrome windows observe normally in the same sessions).
- Superseded in this profile: the "running fullscreen" wording in the 1534, 1904 and 2334 sections above.
- Follow-up corrected: the standing "screen recording permission or capture pipeline restart" unblock is replaced - the unblock is getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step. Background-sent Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, Cmd+Tab is blocked by the tool, and list_windows needs the exact app name "LastWar" ("Last War" returns 0 windows). No control route available to the background channel moves the window across Spaces without a fresh observation of the window itself.
- This correction does not change the radar state: the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read. The twenty-sixth and twenty-seventh occurrences are commented onto Issue #282 by this run; Issue #284 already tracks the blocker.

## What the 2026-11-05 0304 unit added - screen-capture failure, twenty-ninth consecutive pass, nothing read

- Unit radar-2026-11-05-0203 by ticker-0304, about 03:04 to 03:12 local, status failed. Evidence in `_records_/2026-11-05/radar-tasks/0304-queue-run.md`. This was a stack-day unit (duel day 4): on a working screen it would have run Quick Execute batches and recorded the pin inventory without claiming anything.
- No radar screen was ever read and no task was executed or claimed. The Mac screen-capture stream failed on every attempt: session cc-512 `computer.control` activate selected the window for background input but captured no observation, `computer.observe` compact failed, `computer.observe` image failed, `computer.control` open_app returned outcome_unknown; fresh session cc-513 `computer.control` activate again reported `window_on_screen: false` and `brought_to_front: false`, `computer.observe` compact failed, `screen.snap` failed - four capture attempts across two computer sessions, all with "Failed to start stream due to audio/video capture failure". LastWar (bundle com.lastwar.ios, pid 59735) is running, window 1920x1080 at (0,0); Google Chrome is frontmost. `computer.control` list_windows with app LastWar confirms the window exists: 1 window, 1920x1080 at (0,0), window_id 160366, pid 59735. Device connection health at the same time: both native and web transports connected and healthy - this is not a connectivity problem.
- First probe classification: this is the first pass to run the fail-fast probe landed by PR 307. `_tools_/mac_capture_probe.py` 1.0.0 classifies the evidence above OFF_SCREEN_WINDOW (high confidence), stop_pass yes. The View-menu inspect step could not run this pass: it is gated on a fresh observation of the LastWar window, which is exactly what the capture failure prevents - the classification stands on the activate evidence alone, as the probe tool allows (on_screen false plus brought_to_front false is high confidence).
- Narrowing, first-hand this pass: control observation of a Chrome window in the same session (cc-513) succeeds with a full accessibility tree (Gmail inbox), so the capture channel works for on-screen windows and the fault is specific to the LastWar window stream, consistent with the windowed-on-inactive-Space diagnosis in the Correction 2026-11-05 section above.
- Recurrence, not a new failure class: this is the twenty-ninth consecutive ticker pass to fail on this exact blocker (ticker-0234 at 02:34 was the twenty-eighth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the twenty-eighth and twenty-ninth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this unit: with no observation channel a second unit would fail identically, so the remaining inbox units were left queued.

## What the 2026-11-05 0704 unit added - screen-capture failure, thirty-sixth consecutive pass, nothing read

- Unit radar-2026-11-05-0603 by ticker-0704, about 07:19 to 07:23 local,
  status failed. Evidence in
  `_records_/2026-11-05/radar-tasks/0704-queue-run.md`. This was a
  stack-day unit (duel day 4, radar posture stack per tools/duel.py):
  on a working screen it would have run Quick Execute batches and
  recorded the pin inventory without claiming anything.
- No radar screen was ever read and no task was executed or claimed.
  The Mac screen-capture stream failed on every attempt across four
  computer sessions: session cc-526 `computer.control` activate
  selected the window for background input but captured no
  observation (`window_on_screen: false`, `brought_to_front: false`),
  `computer.observe` compact failed; fresh session cc-527
  `computer.control` open_app returned outcome_unknown and
  `computer.observe` compact failed, while connection.health reported
  both transports healthy; session cc-528 `computer.control`
  frontmost_app returned Google Chrome frontmost with the LastWar
  target present and `computer.observe` image failed; session cc-529
  `computer.control` list_windows with app LastWar confirms the
  window exists: 1 window, 1920x1080 at (0,0), window_id 160366,
  pid 59735. Four capture attempts across four sessions, all with
  "Failed to start stream due to audio/video capture failure", plus
  one open_app outcome_unknown - this meets the standing
  at-least-3-attempts retry rule.
- Probe classification: `_tools_/mac_capture_probe.py` 1.0.0
  classifies the evidence above OFF_SCREEN_WINDOW (high confidence),
  stop_pass yes. The View-menu inspect step could not run this pass:
  it is gated on a fresh observation of the LastWar window, which is
  exactly what the capture failure prevents. The Chrome
  control-observation step the probe lists as missing was closed in
  session cc-529: a control observation of the Google Chrome window
  in the same session succeeded with a full accessibility tree, so
  the capture channel works for on-screen windows and the fault is
  specific to the LastWar window stream, consistent with the
  windowed-on-inactive-Space diagnosis in the Correction 2026-11-05
  section above.
- Recurrence, not a new failure class: this is the thirty-sixth
  consecutive ticker pass to fail on this exact blocker. The blocker
  is filed as Issue #284 (tooling) alongside the knowledge Issue
  #282; this pass commented on #284 instead of filing a duplicate,
  and this run comments the thirty-sixth occurrence onto #282.
  Coverage note: the thirty-fifth occurrence (ticker-0634) has no
  record on the records branch at this run's cutoff, so the count
  from 34 to 36 is attested only by the 0704 record's own count.
- Sync and expiry: the pass reaped 0, expired 5 (five 0257-cycle
  units), due 21, produced nothing new, 21 regulars already queued.
  No zombie seeding: no zombie-invasion unit in inbox or claimed;
  the chain closed with unit 066 on 2026-10-30 and the activity
  metadata forbids seeding a fresh chain until a Zombie Invasion tab
  is seen live again.
- Reading warning: this failed unit gives zero evidence about the
  radar claim state. It must NOT be read as "nothing claimable" or
  as a stored-count state - the 1005 close (Lv.13, points 219,
  stored 0 of 40, stamina 81) rests on a live read and stands as the
  last live read; this unit rests on no read at all.
- Tracker untouched for failed, per the queue rules; the next tick
  re-produces this regular. The pass stopped after this unit: with
  no observation channel a second unit would fail identically, so
  the remaining inbox units were left queued.

## What the 2026-11-05 1104 unit added - Mac device offline, forty-third consecutive pass, zero-response form

- Unit radar-2026-11-05-1003 by ticker-1104, about 11:04 to 11:15 local, status failed. Evidence in `_records_/2026-11-05/radar-tasks/1104-queue-run.md`. No radar screen was ever read and no task was executed or claimed. This was a stack-posture unit (duel day 4, window "duel day 4 - radar stack"): on a stack day nothing is claimed in any case, so the loss is the unexecuted ordinary tasks and the missing closing reads, not leaked claims.
- Attempts, four, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path) twice; connection.health and connection.repair (native) on the recovery device both node_invoke_timeout after 25s. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 3 hours 30 minutes at pass time, unchanged since the ticker-1025 pass. This meets the standing at-least-3-attempts retry rule.
- Recurrence, not a new failure class: the forty-third consecutive ticker pass with a Mac device-access blocker, fourth in the worsened zero-response form after ticker-0904 (fortieth), ticker-0941 (forty-first) and ticker-1025 (forty-second). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-third occurrence onto #282. No probe was run this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Sync and expiry: the pass reaped 0, expired 5 (events, passes, secrets, treasures, trucks 0657), due 21, produced nothing new, 21 regulars already queued; inbox held 73 units at this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this unit: with no observation channel a second unit would fail identically, so the remaining inbox units were left queued.

## What the 2026-11-05 1504 unit added - Mac device offline, fifty-first consecutive pass, zero-response form

- Unit radar-2026-11-05-1403 by ticker-1504, about 15:04 to 15:15 local, status failed. Evidence in `_records_/2026-11-05/radar-tasks/1504-queue-run.md`. No radar screen was ever read and no task was executed or claimed. This was a stack-posture unit (duel day 4, window "duel day 4 - radar stack", radar_posture stack confirmed by tools/duel.py at 15:06): on a stack day nothing is claimed in any case, so the loss is the unexecuted ordinary tasks and the missing closing reads, not leaked claims.
- Attempts, four, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path) (attempt 1); connection.health on the recovery device node_invoke_timeout after 25s (attempt 2); connection.repair on the recovery device first rejected client-side (invalid_command_params, target "web" not accepted, expected "native" - the pass's own parameter error, no channel response), retried with target "native": node_invoke_timeout after 25s (attempt 3); connection.health on the Mac mini again node_offline (attempt 4). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 7 hours 30 minutes at pass time, unchanged since the ticker-1025 pass. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: the fifty-first consecutive ticker pass with a Mac device-access blocker, twelfth in the worsened zero-response form after ticker-1434 (fiftieth, eleventh). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fifty-first occurrence onto #282.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Sync: reaped 0, expired 4, due 21, produced nothing new, all 21 regulars already queued; inbox held 73 units at this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this unit: with no observation channel a second unit would fail identically, so the remaining inbox units were left queued.

## What the 2026-11-05 1933 unit added - Mac device offline, fifty-ninth consecutive pass, zero-response form

- Unit radar-2026-11-05-1803 by ticker-1933, about 19:34 to 19:40 local, status failed. Evidence in `_records_/2026-11-05/radar-tasks/1933-queue-run.md`. No radar screen was ever read and no task was executed or claimed. This was a stack-window unit (window text "duel day 4 - radar stack", planned_for 2026-11-06T02:03:00Z, expires 2026-11-06T06:03:00Z), but the live posture at entry governs and it is release, not stack: tools/duel.py at 19:35 local reads duel day 5, Total Mobilization, radar_posture release, day ends 2026-11-06 18:00 local. On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) twice; connection.repair (web) on the Mac mini node_offline; connection.health on the Mac mini node_offline; connection.health on the recovery device node_invoke_timeout after 25s. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 12 hours at pass time, unchanged since the ticker-1025 pass; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the fifty-ninth consecutive ticker pass with a Mac device-access blocker, twentieth in the worsened zero-response form (fifty-eighth was ticker-1834, scout). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fifty-ninth occurrence onto #282.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 0004 unit added - Mac device offline, sixty-third consecutive pass, zero-response form

- Unit radar-2026-11-05-2203 by ticker-0004, session window about 00:17 to 00:30 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/0004-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path) twice (attempts 1 and 5); computer.session start on the Mac mini node_offline twice (attempts 2 and 4); connection.repair (web) on the Mac mini node_offline (attempt 3). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 16 hours 50 minutes at the 00:20 re-check, unchanged since the ticker-1025 pass and identical to the ticker-2303 reading. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen, and its attempts in the ticker-2041 pass timed out after 25 seconds each, so nothing new would be learned by repeating them. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the sixty-third consecutive ticker pass with a Mac device-access blocker, twenty-fourth in the worsened zero-response form (sixty-second was ticker-2303, ghost-ops). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the sixty-third occurrence onto #282.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: the inbox held 76 units at this pass close (77 at sync); the pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06), restored to the live pool inbox by the ticker-2303 pass (not_before 01:30Z and 02:30Z), was not yet due and was untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 0342 unit added - Mac device offline, sixty-sixth consecutive pass, zero-response form

- Unit radar-2026-11-06-0203 by ticker-0342, session window about 03:42 to 03:47 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/0342-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5, planned 02:03 local, expires 06:03 local). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path) twice (attempts 1 and 4); connection.repair (web) on the Mac mini node_offline (attempt 2); computer.session start on the Mac mini node_offline twice (attempts 3 and 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 20 hours 10 minutes at the 03:47 re-check, unchanged since the ticker-0234 pass. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen, and the ticker-0234 pass about an hour earlier attempted its recovery channel and timed out after 25 seconds, so nothing new would be learned by repeating them. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the sixty-sixth consecutive ticker pass with a Mac device-access blocker, twenty-seventh in the worsened zero-response form (sixty-fifth was ticker-0234, shop-claims). No executed pass is recorded between 0234 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the sixty-sixth occurrence onto #282.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: the inbox held 76 units at this pass close (77 at sync); four 2257-slot units (events, secrets, treasures, trucks, all 2026-11-05) sat in done with status expired and finished_at 2026-11-06T11:41:17Z (03:41:17 local), already reaped before this pass started. The pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (not_before 01:30Z and 02:30Z on 2026-11-07, expires 03:00Z), not yet due and untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 0741 unit added - Mac device offline, seventy-fourth consecutive pass, zero-response form

- Unit radar-2026-11-06-0603 by ticker-0741, session window about 07:41 to 07:52 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/0741-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5, planned 06:03 local, expires 10:03 local). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (attempts 1 and 2); connection.health on the Mac mini node_offline (attempt 3); connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 4); connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 24 hours 10 minutes at the 07:47 re-check, unchanged since the ticker-0704 pass. New against the 0342, 0634 and 0704 passes, which made no recovery-device attempts: this pass DID attempt the recovery device, and both the health check and the native repair timed out after 25 seconds - the recovery channel accepts the invoke and never answers within 25 seconds, matching the ticker-0234 signature. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the seventy-fourth consecutive ticker pass with a Mac device-access blocker, thirty-fifth in the worsened zero-response form (seventy-third was ticker-0704, harvest). No executed pass is recorded between 0704 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the seventy-fourth occurrence onto #282.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: sync reaped 0, expired 6, due 20, produced nothing new, all 20 regulars already queued. Queue stats at 15:43Z: inbox 79, claimed 0, done 1009, upcoming 53. The pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (not_before 01:30Z and 02:30Z on 2026-11-07, expires 03:00Z), not yet due and untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1104 unit added - Mac device offline, seventy-seventh consecutive pass, zero-response form

- Unit radar-2026-11-06-1003 by ticker-1104, session window about 11:04 to 11:23 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/1104-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5, planned 10:03 local, expires 14:03 local). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (attempt 1); connection.health on the Mac mini node_offline (attempt 2); connection.repair (web) on the Mac mini node_offline (attempt 3); computer.session start on the Mac mini node_offline (attempt 4, retry); connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 27 hours 45 minutes at the 11:23 re-check, unchanged since the ticker-0934 pass. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the seventy-seventh consecutive ticker pass with a Mac device-access blocker, thirty-eighth in the worsened zero-response form (seventy-sixth was ticker-0934, donations, thirty-seventh). No executed pass is recorded between 0934 and this one: the newest executed closing in the pool is 2026-11-06T17:56:17Z (the 0934 unit). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the seventy-seventh occurrence onto #282.
- New against the 0741 pass, which attempted both a recovery health check and a native repair (both timed out): this pass attempted the recovery channel once, health check only, and it timed out after 25 seconds - the same signature as the 0741, 0832 and 0934 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: sync reaped 0, expired 6, due 22, produced 12 new units, 9 regulars already queued. Queue stats at 19:18Z: inbox 68, claimed 1, done 956, upcoming 48. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due and untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1235 unit added - Mac device offline, seventy-eighth consecutive pass, zero-response form

- Unit radar-2026-11-06-1003 by ticker-1235, session window about 12:35 to 12:45 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/1235-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5, planned 10:03 local, expires 14:03 local). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (attempt 1); connection.health on the Mac mini node_offline (attempt 2); connection.repair (web) on the Mac mini node_offline (attempt 3); computer.session start on the Mac mini node_offline (attempt 4, retry); connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 29 hours at the 12:44 re-check, unchanged since the ticker-1104 pass. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the seventy-eighth consecutive ticker pass with a Mac device-access blocker, thirty-ninth in the worsened zero-response form (seventy-seventh was ticker-1104, radar, thirty-eighth). No executed pass is recorded between 1104 and this one: the newest executed closing in the pool is 2026-11-06T17:56:17Z (the 0934 unit). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the seventy-eighth occurrence onto #282.
- New against the 1104 pass: nothing new about the recovery route. This pass attempted the recovery channel once, health check only, and it timed out after 25 seconds - the same signature as the 0741, 0832, 0934 and 1104 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: sync reaped 0, expired 0, due 20, produced nothing new, all 20 regulars already queued. Queue stats at 20:30Z: inbox 79, claimed 0, done 1025, upcoming 53. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due and untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1507 unit added - Mac device offline, eightieth consecutive pass, zero-response form

- Unit radar-2026-11-06-1403 by ticker-1507, session window about 15:07 to 15:13 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/1512-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar release-day check for this slot (duel day 5, planned 14:03 local, expires 2026-11-07 02:03 UTC, 18:03 local). On a working screen this unit would have entered the radar, run Quick Execute batches and claimed the stack built on day 4, then worked the map pins to a closing read each, per the release standard. None of that happened; the day 4 stack sits unclaimed and the release window still runs until 2026-11-06 18:00 local, so a later pass with a live Mac can still claim it.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (attempt 1); connection.repair on the recovery device node_invoke_timeout after 25 seconds (attempt 2); connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 3); computer.session start on the Mac mini node_offline (attempt 4, retry); computer.session start on the Mac mini node_offline (attempt 5, retry). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 31 hours 36 minutes at the 15:12 re-check, unchanged since the ticker-1235 pass. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the eightieth consecutive ticker pass with a Mac device-access blocker, forty-first in the worsened zero-response form (seventy-ninth was ticker-1349, arms-race, fortieth). No executed pass is recorded between 1349 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eightieth occurrence onto #282.
- New against the 1235 pass, which attempted the recovery channel once (health check only): this pass attempted the recovery channel twice, repair and then health check, and both timed out after 25 seconds - the same signature as the 0741, 0832, 0934, 1104, 1235 and 1349 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day 4 stack sits unclaimed until a live pass claims it in the release window (until 2026-11-06 18:00 local).
- Pass context: sync reaped 0, expired 5, due 20, produced nothing new, all 20 regulars already queued. Queue stats at 23:08Z: inbox 74, claimed 0, done 1041, upcoming 48. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pre-reset zero-sweep pair for the 2026-11-06 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due and untouched by this pass. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1934 unit added - Mac device offline, eighty-eighth consecutive pass, zero-response form

- Unit radar-2026-11-06-1803 by ticker-1934, session window about 19:34 to 19:45 local, status failed. Evidence in `_records_/2026-11-06/radar-tasks/1934-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The unit window stamp reads "duel day 5 - radar release", but the live posture at entry governs and it is stack, not release: tools/duel.py at 19:38 local reads duel day 6, Enemy Buster, radar_posture stack, day ends 2026-11-07 18:00 local. The duel rolled over at about 18:00 local (02:00 UTC). Had the device been reachable, this unit would have run as a stack unit (complete, do not claim, keep headroom), not a release unit; the stamp staleness is a production-window artefact, not a schedule error. The day-5 release window closed at 18:00 local 2026-11-06 with the day-4 stack never claimed in it.
- Attempts, seven, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path); connection.repair (web) on the Mac mini node_offline; computer.session start on the Mac mini node_offline; computer.control activate LastWar on the Mac mini node_offline; computer.observe compact on the Mac mini node_offline; connection.health on the recovery device node_invoke_timeout after 25 seconds; connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 36 hours at the 19:38 re-check, unchanged since the ticker-1025 pass; the last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the eighty-eighth consecutive ticker pass with a Mac device-access blocker, forty-ninth in the worsened zero-response form (eighty-seventh was ticker-1904, harvest, forty-eighth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eighty-eighth occurrence onto #282.
- New against the 1507 pass, which attempted the recovery channel twice (repair and then health check, both timed out): this pass also attempted the recovery channel twice, health check and repair (native), and both timed out after 25 seconds - the same signature as the 1235, 1349, 1507, 1534, 1604, 1634 and 1704 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Pre-reset zero sweep: both pre-reset zero-sweep units for the 2026-11-06 reset day expired unexecuted in the ticker-1904 pass's sync, and the 19:00 reset passed with no zero sweep of the daily collection ledger. Nothing new to add this pass; the miss stands (already recorded in the 1904 fold, resource-collection 1.32.0).
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: sync reaped 0, expired 0, due 22, produced nothing new, all 22 regulars already queued. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass stopped after this one unit: with the device fully offline, further units would fail identically. The inbox held 65 units at this pass's close.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 0011 unit added - Mac device offline, ninety-third consecutive pass, zero-response form

- Unit radar-2026-11-06-2203 by ticker-0011, session window about 00:11 to 00:22 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/0011-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack slot for this cycle (duel day 6, Enemy Buster, radar posture stack per tools/duel.py at 00:17 local - complete, do not claim, keep headroom; day 6 ends 2026-11-07 18:00 local). The unit window stamp reads "duel day 6 - radar stack" and AGREES with the live posture this time - unlike the 1934 unit, whose stamp was stale day-5 release wording; the stamp-staleness class did not recur here. The day-5 release window closed at 18:00 local 2026-11-06 with the day-4 stack never claimed in it (already recorded in the 1934 fold).
- Attempts, four, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path); connection.health on the recovery device node_invoke_timeout after 25 seconds; connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds; connection.health on the Mac mini node_offline. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 40 hours 45 minutes at the 00:20 re-check, unchanged since the ticker-1025 pass. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the ninety-third consecutive ticker pass with a Mac device-access blocker, fifty-fourth in the worsened zero-response form (ninety-second was ticker-2257, harvest, fifty-third). No executed pass is recorded between 2257 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the ninety-third occurrence onto #282.
- New against the 1934 pass, which attempted the recovery channel twice (health check and repair, both timed out): this pass also attempted the recovery channel twice, health check and then repair (native), and both timed out after 25 seconds - the same signature as the 0741, 1235, 1349, 1507 and 1934 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Correction, 0011 record dating: the record states the stored count, the pending-reward count on the Claim All bar and the pin inventory are "all unread since the 2026-11-03 2317 close". That dating is corrected here, not adopted: the 1005 unit on 2026-11-04 read all three live (entry stored 3 of 40, closed 0 of 40; 13 rewards claimed through Claim All in two batches; pins scanned at entry and the blue skull Doom Elite pin identified). The 0011 pass performed no game read, so its "since 2317" phrasing cannot supersede the 1005 on-screen read. The 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read; the next radar unit that reaches the game must still re-read stored count, pending-reward count, stamina, restore line and pin inventory live first, per the standing rule.
- Scope note: the Correction 2026-11-05 unblock (owner Dock-icon click, window back on the active Space) holds for the window-stream (capture-failure) form only; it does not address a stalled invoke channel or an offline device. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing - unverified.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: before any game work, this pass resolved five open records PRs sitting in conflict on the single file _logs_/repo-actions/action-log.jsonl (append-append): PR 351 (records/2026-11-05), PR 350 (records/2026-11-01), PR 301 (records/2026-11-04), PR 265 (records/2026-11-02), PR 256 (records/2026-11-03) - each resolved on the branch side in a scratch worktree on the VPS by merging main into the branch and unioning both sides' appended lines (942/945 ours + 1003 theirs to 1004/1007 merged, no lines dropped), commit, push, no force push; all five re-checked MERGEABLE / CLEAN afterwards. PR 381 (records/2026-11-06) was already clean. The integrator merges records PRs in 4-hour batches; the next batch is 03:00 local. Queue sync at pass start: 22 due, all already queued, 0 produced, 0 reaped. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. No sweep-pair claim is made in this fold: the 0011 record is silent on the pre-reset-sweep-2026-11-07 pair's state, so its state is not asserted here. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 0132 unit added - Mac device offline, ninety-fourth consecutive pass, zero-response form

- Unit radar-2026-11-06-2203 by ticker-0127, session window about 01:27 to 01:33 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/0132-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack slot for this cycle (duel day 6, Enemy Buster, radar posture stack - complete, do not claim, keep headroom; day 6 ends 2026-11-07 18:00 local). The unit window stamp reads "duel day 6 - radar stack" and AGREES with the live posture this time - the record cites the tools/duel.py read (duel day 6, Enemy Buster, radar posture stack); the 1934 stamp-staleness class did not recur here. The day-5 release window closed at 18:00 local 2026-11-06 with the day-4 stack never claimed in it (already recorded in the 1934 fold).
- Attempts, six, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) on attempts 1, 4 and 5; connection.repair on the recovery device with target "web" rejected as invalid_command_params (expected one of native - the recovery device's schema differs from the Mac mini's own, which lists "web"); connection.repair corrected to target "native" on the recovery device node_invoke_timeout after 25 seconds; connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 41 hours 57 minutes at the 01:32 re-check, unchanged since the ticker-0011 pass. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the ninety-fourth consecutive ticker pass with a Mac device-access blocker, fifty-fifth in the worsened zero-response form (ninety-third was ticker-0011, fifty-fourth). No executed pass is recorded between 0011 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the ninety-fourth occurrence onto #282.
- New against the 0011 pass, which went straight to a native repair: this pass first attempted the recovery-device repair with target "web" and was rejected as invalid_command_params - the recovery device's schema takes only "native", unlike the Mac mini's own, which lists "web". The corrected native repair and the health check both timed out after 25 seconds - the same signature as the 0011, 2257 and 2134 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route beyond the schema detail.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: this pass staged the pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07, priority 1, est 15 minutes): unit 001 not_before 2026-11-08T01:30:00Z (17:30 local), unit 002 not_before 2026-11-08T02:30:00Z (18:30 local), both expiring at the 2026-11-08T03:00:00Z reset - no chain existed in the pool before this pass. Queue sync at pass start: 22 due, all already queued, 0 produced, 0 reaped, 0 expired. Queue stats at 09:29:51Z: inbox 75, claimed 0, done 1078, upcoming 49 (77 after the sweep pair was staged, 76 after this unit was claimed). No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Branch note: the records/2026-11-07 branch already carries this same unit completed as failed by ticker-0011 (evidence 0011-queue-run.md, 4 invokes, 93rd consecutive pass), so this pass's re-attempt does not overwrite that completion: the branch keeps the 0011 done file, and this record file is the evidence of the re-attempt. The stale-mirror divergence is the known working-tree divergence already named in the 2026-11-06 retro; the integrator's merge reconciliation keeps the branch's true failed outcomes over main's stale re-creations.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 0304 unit added - Mac device offline, ninety-seventh consecutive pass, zero-response form

- Unit radar-2026-11-07-0203 by ticker-0304, session window about 03:04 to 03:13 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/0304-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack check for this slot (duel day 6, Enemy Buster, radar posture stack - complete, do not claim, keep headroom; planned 02:03 local 2026-11-07, expires 06:03 local 2026-11-07). The unit window stamp reads "duel day 6 - radar stack" and agrees with the live posture - the 1934 stamp-staleness class did not recur.
- Attempts, five, zero responses: connection.health on the Mac mini node_offline (attempt 1), connection.repair (web) on the Mac mini node_offline (attempt 2), computer.session start on the Mac mini node_offline (attempts 3 and 4, retry), connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 43 hours 30 minutes at the 03:10 re-check, unchanged since the ticker-0234 pass 30 minutes earlier. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the ninety-seventh consecutive ticker pass with a Mac device-access blocker, fifty-eighth in the worsened zero-response form (ninety-sixth was ticker-0234, fifty-seventh, 30 minutes earlier). No executed pass is recorded between 0234 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the ninety-seventh occurrence onto #282.
- Nothing new was learned about the recovery route: the recovery-device health check timed out after 25 seconds, the same signature as the 0234, 0204 and 0127 passes - the recovery channel accepts the invoke and never answers within 25 seconds. No repair attempt was made this pass.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: sync reaped 0, expired 4 (events, secrets, treasures, trucks, all 2026-11-06-2257 slot), due 20, produced nothing new, all 20 regulars already queued. Queue stats at 11:08Z: inbox 72, claimed 0, done 1094. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Branch note: before any game work this pass resolved a conflict on PR 382 (records/2026-11-07) with main 2d36115cd4 after the 0300 batch merged records PRs 350 and 381 - a single conflicting file, _logs_/repo-actions/action-log.jsonl (append-append collision), resolved by union-merging main into the branch (commit 87ef39a4c4): main's version kept whole including its line-join fix, the branch-only 9 lines appended, no line dropped (1016 lines, set-wise verified). The PR carries to the 07:00 batch.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 0734 unit added - Mac device offline, one-hundred-third consecutive pass, zero-response form

- Unit radar-2026-11-07-0603 by ticker-0734, session window about 07:34 to 07:42 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/0734-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack slot for this cycle (duel day 6, Enemy Buster, radar posture stack - complete, do not claim, keep headroom; planned 06:03 local 2026-11-07, expires 10:03 local 2026-11-07). The unit window stamp reads "duel day 6 - radar stack" and agrees with the live posture - the 1934 stamp-staleness class did not recur.
- Attempts, seven, zero responses: computer.session start on the Mac mini node_offline (attempts 1, 5 and 7); connection.health on the Mac mini node_offline (attempt 2); connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds (attempt 3); connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 4); connection.repair (web) on the Mac mini node_offline (attempt 6). A device.list re-check between attempts confirmed the Mac mini still offline with last_seen unchanged. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 48 hours at the 07:42 re-check, unchanged since the ticker-0704 pass about 30 minutes earlier. The last_seen value is known-stale (it did not move while ticker passes played the game on 2026-11-05), so it is reported as the listed value only, not as the outage start. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the one-hundred-third consecutive ticker pass with a Mac device-access blocker, sixty-fourth in the worsened zero-response form (one-hundred-second was ticker-0704, sixty-third, 30 minutes earlier). No executed pass is recorded between 0704 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the one-hundred-third occurrence onto #282.
- Recovery-device attempts were made, as in recent passes: the native repair and the health check both timed out after 25 seconds - the same signature as the 0704, 0633, 0526, 0420, 0345, 0304 and 0234 passes, so the recovery channel still accepts the invoke and never answers within 25 seconds. Nothing new was learned about the recovery route.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: sync reaped 0, expired 5, due 20, produced nothing new, all 20 regulars already queued. The 5 expired units are the unexecuted 0257 slot units (events, secrets, treasures, trucks 2026-11-07-0257; scout-midday 2026-11-06-0700), moved to done as expired in the live pool - the records branch already held these same 5 units as expired from the ticker-0704 sync, so this pass delivers no duplicate copies of them. Queue stats at 15:34Z: inbox 76, claimed 0, done 1106 (71 after this unit was claimed and the 5 expired units were reaped). The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass stopped after this one unit: with the device fully offline, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1104 unit added - Mac back online, window off-Space, one-hundred-eighth consecutive pass, capture-failure form

- Unit radar-2026-11-07-1003 by ticker-1104, session window about 11:19 to 11:27 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/1104-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack slot for this cycle (duel day 6, Enemy Buster, radar posture stack - complete, do not claim, keep headroom; planned 10:03 local 2026-11-07, expires 14:03 local 2026-11-07). The unit window stamp reads "duel day 6 - radar stack" and agrees with the live posture - the 1934 stamp-staleness class did not recur.
- Attempts, eleven, zero game screens: computer.session start (cc-4) on the Mac mini started; list_windows LastWar: 1 window, (0, -360), 1920x1080; activate LastWar: selected for background input, brought_to_front false, window_on_screen false, evidence_error "Failed to start stream due to audio/video capture failure"; computer.observe (attempt 1): screen_failed, same capture failure; open_app LastWar: outcome_unknown - "The launch request was sent before its result could be verified", no retained evidence, retryable false, required_next observe; computer.observe (attempt 2): screen_failed, same capture failure; list_windows LastWar again: unchanged - same pid 59735, still (0, -360), the open_app launch produced no relaunch and no move; set_window_frame LastWar to (0, 0): refused with observation_required - an earlier input result needs fresh observation, and no capture exists to satisfy it, so the move could not be attempted; connection.health on the Mac mini: both transports connected and healthy (native lastResponseAgeSeconds 0, web 9); computer.observe (attempt 3): screen_failed, same capture failure; computer.session end (cc-4): ended. Four capture attempts failed (activate evidence plus three observes), all with the identical "Failed to start stream due to audio/video capture failure". This meets the standing at-least-3-attempts retry rule, and the extra attempts added no new route.
- New against the 1020 pass: open_app does not relaunch or move the window when it sits off-Space - the launch returned outcome_unknown and list_windows afterwards showed the same pid 59735 at the same (0, -360). set_window_frame is not a live route while capture is down: it is gated on a fresh observation that cannot be produced. Recovery routes NOT retried, deliberately, per the ticker-1020 lessons folded into alliance-help 1.27.0: Mission Control was not opened (it wedged the channel in 1020) and background Ctrl+Right was not tried (it does not switch Spaces through this channel) - this pass applied the folded lessons instead of re-learning them. The known reliable unblock stands (2026-11-05 correction): the owner clicking the LastWar Dock icon once brings the window to the active Space; that step needs the owner at the Mac. No "active on a different device" dialog appeared, so no takeover was needed or made.
- Recurrence, not a new failure class: this is the one-hundred-eighth consecutive ticker pass with a Mac device-access blocker, second in the new form (device online, capture failing) after the 106-pass offline streak ended with ticker-1003 (one-hundred-seventh was ticker-1020, about 40 minutes earlier). No executed pass is recorded between 1020 and this one. The blocker is filed as Issue #282 (knowledge, still open); this pass commented on #282 instead of filing a duplicate, and this run comments the one-hundred-eighth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: sync reaped 0, expired 5, due 20, produced nothing new, all 20 regulars already queued. The 5 expired units are the unexecuted 0657 slot units (events, passes, secrets, treasures, trucks 2026-11-07-0657), moved to done as expired in the live pool. Queue stats at 19:19Z: inbox 74, claimed 0, done 1127 - read after the sync reaped the 5 expired units but before this unit was claimed (73 after), so done 1122 to 1127 (+5) and inbox 79 to 74 (-5) against the planner-1040 read at 10:44 local are exactly the 5 expired units. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass stopped after this one unit: with the capture channel down, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1616 unit added - Mac back online, window off-Space, one-hundred-twelfth consecutive pass, capture-failure form

- Unit radar-2026-11-07-1403 by ticker-1608, session window about 16:16 to 16:18 local, status failed. Evidence in `_records_/2026-11-07/radar-tasks/1616-queue-run.md`. No radar screen was ever read and no task was executed or claimed. The loss is the unexecuted radar stack slot for this cycle (duel day 6, Enemy Buster, radar posture stack - complete, do not claim, keep headroom; planned 14:03 local 2026-11-07, expires 02:03 local 2026-11-08). The unit window stamp reads "duel day 6 - radar stack" and agrees with the live posture - the 1934 stamp-staleness class did not recur.
- Attempts, four, zero game screens: computer.session start (cc-9) on the Mac mini started; list_windows LastWar: 1 window, (0, -360), 1920x1080; activate LastWar: selected for background input, brought_to_front false, window_on_screen false, evidence_error "Failed to start stream due to audio/video capture failure"; computer.observe (attempt 1): screen_failed, same capture failure; computer.observe (attempt 2): screen_failed, same capture failure; connection.health on the Mac mini: both transports connected and healthy (native lastResponseAgeSeconds 0, web 8); computer.observe (attempt 3): screen_failed, same capture failure; computer.session end (cc-9): ended. Four capture attempts failed (activate evidence plus three observes), all with the identical "Failed to start stream due to audio/video capture failure". This meets the standing at-least-3-attempts retry rule, and the extra attempts added no new route.
- No new route tried, deliberately, per the ticker-1020 lessons folded into alliance-help 1.27.0 and confirmed by the 1104, 1204 and 1452 passes: Mission Control was not opened (it wedged the channel in 1020), background Ctrl+Right was not tried (it does not switch Spaces through this channel), open_app was not retried (1104: outcome_unknown, no relaunch and no move), and set_window_frame was not tried (1204: refused with observation_required - an observation that cannot be produced while capture is down). The known reliable unblock stands (2026-11-05 correction): the owner clicking the LastWar Dock icon once brings the window to the active Space; that step needs the owner at the Mac. No "active on a different device" dialog appeared, so no takeover was needed or made.
- Recurrence, not a new failure class: this is the one-hundred-twelfth consecutive ticker pass with a Mac device-access blocker, sixth in the new form (device online, capture failing) after the 106-pass offline streak ended with ticker-1003 (one-hundred-eleventh was ticker-1452, about 1 hour 25 minutes earlier). No ticker pass is recorded between 1452 and this one, and no executed pass is recorded between them. The blocker is filed as Issue #282 (knowledge, still open); the pass itself commented the one-hundred-twelfth occurrence onto #282 at 2026-11-08T00:20:14Z, so this run posts no duplicate comment.
- Reading warning: this failed unit gives zero evidence about the radar claim state. It must NOT be read as "nothing claimable" or as a stored-count state - the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) rests on a live read and stands as the last live read; this unit rests on no read at all. The day-4 stack was never claimed in the release window (closed 2026-11-06 18:00 local); the current duel day is a stack day (day 6, Enemy Buster), so a live pass now completes tasks without claiming.
- Pass context: sync reaped 0, expired 0, due 20, produced nothing new, all 20 regulars already queued. Queue stats at 00:08Z: inbox 79, claimed 0, done 1143. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the activity metadata forbids seeding a fresh chain until a Zombie Invasion tab is seen live again. The pass first reconciled all four open records PRs with main dfc3e08b by union-merging the action log (records/2026-11-07 at d230406be2, records/2026-11-05 at f9e1fff83d, records/2026-11-04 at 602566d905, records/2026-11-03 at d44b93bac2), all pushed and commented; the pr-integration 1615 run confirms the four PRs now clean. The pass stopped after this one unit: with the capture channel down, further units would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1633 and 1655 units added - capture channel working again, radar state read incidentally during the donations detour

- Capture channel working again: the ticker-1633 arms-race unit (about 16:35 to 16:48 local) and the ticker-1655 harvest, survivors and training units (about 16:56 to 17:12 local) all ran on live game screens with working capture, after the 1020/1104/1204/1452/1608 passes failed identically on "Failed to start stream due to audio/video capture failure" (Issue 282). The 1633 pass read the Last War window as 788x1083 (vs 1920x1080 at (0, -360) in the 1020-1608 passes; the size change is recorded as observed, not explained). No new capture-failure occurrence was recorded in these passes, so no new comment was posted onto Issue 282; the issue stays open and the Dock-icon unblock stands if the failure recurs.
- Incidental radar reads during the ticker-1633 donations unit's navigation detour (evidence in `_records_/2026-11-07/alliance-donations/1633-queue-run.md`, commit a85cfdafa8): a BASE tap at 920,975 opened the radar map instead of the base - Lv.13, 237 points, 19/40 radar tasks, "12 Radar Task(s) will be restored in 05:48:31", stamina 100. A home-icon tap at 918,941 did not return to base; the next screenshot showed a radar CONGRATULATIONS rewards screen: radar tasks 0/40, points 259, stamina 35, "You can complete 2 tasks, requires 20 Stamina", Quick Execute button. Between the two radar screenshots 19 tasks completed and 65 stamina was spent. The executor did NOT tap Quick Execute and did NOT tap any radar pin; the tap coordinates used were the home icon's. The owner is at the Mac this run and may have executed the radar tasks himself, or a tap mis-landed.
- Reading discipline for these figures: they are incidental live observations, not a radar-unit close. They are the newest observed radar state (points 259, stored 0/40, stamina 35), but the 1005 close (Lv.13, points 219, stored 0 of 40, stamina 81) stands as the last live read BY A RADAR UNIT, and the next radar unit re-reads the stored count, points and stamina from its own entry and confirms whether the 19 tasks were owner-executed. The detour also shows the BASE button at 920,975 can land on the radar map - a navigation hazard for units leaving the Arms Race page.
- The blue droplet over the blue truck (norm 150,293) opens the world-map task view ("2 task rewards can be claimed", green Claim All button, no price tag) - radar-task work, not harvest; the harvest unit left the Claim All untouched (see resource-collection 1.36.0). The droplet is a locator, not a loot bubble.
- Tracker untouched for the radar regular; the next tick re-produces the radar unit, which re-reads the state.

## What the 2026-11-07 1912 unit added - stack empty, dish re-grounded for the windowed layout, capture channel recovered

- Unit radar-2026-11-07-1803 by ticker-1904, about 19:07 to 19:12 local, status done. Evidence in `_records_/2026-11-07/radar-tasks/1912-queue-run.md` (commit 6baaa831b9 on records/2026-11-07). Live duel posture at 19:06 is duel day 7, off day settlement, radar_posture stack per tools/duel.py. First unit of the new trade day (post-19:00 reset) and the first successful live game read after the access-failed streak recorded through ticker-1608.
- Radar screen entered and verified live: Lv.13, radar points 267, stored tasks 0 of 40, stamina 99 (top right), restore line "12 Radar Task(s) will be restored in 03:22:08". No bottom action bar is shown - no Quick Execute offer and no Claim All offer, consistent with zero stored and zero pending rewards.
- Stack posture held throughout: nothing executed, nothing claimed, no pin tapped. The stack is empty - there were zero executable ordinary tasks, so the execute step is vacuously complete and no stamina was spent. The next radar restore lands in about 3 hours 22 minutes (12 tasks); the next radar unit will have work again then.
- Pin inventory (stack rule, untapped): one pin standing on the radar map, southwest near the map edge at about norm 85,738 - a brown circular pin showing what looks like an animal face, no red dot visible, class unknown. No other pins are visible on the map. Left for the next release-day unit to identify under the release handling rule. This is a new unidentified pin type for the "Standing pin types" open question, alongside the orange arrow, purple axe, orange axe and portrait pins.
- Entry correction, layout-dependent: the first tap at norm 50,690 (estimated from the fresh screenshot) missed the dish and opened a base visitor dialog, "POLAR GUEST - Amazing! This place feels just like home." / "Can I stay here forever?" - advanced twice with dialog taps only and the dialog closed by itself. No reward was offered or claimed; no radar-unrelated work was done. Re-grounded from a magnified crop of the left icon column: the satellite dish icon sits at pixel about 38,757 in the 763x1050 window, i.e. norm 52,721 - slightly left of the 2026-10-29 measured norm 62,727 recorded in this profile. The second tap at norm 52,721 opened the radar on the first try. CORRECTION: the 62,727 point is a fullscreen-layout point and does not transfer to the windowed layout - in the 763x1050 windowed layout the dish grounds at norm 52,721. Units must re-ground the dish from a magnified crop of the left column in the current layout (rule R2), never carry 62,727 across layouts. A missed dish tap can open a visitor dialog; advance it with dialog taps only and take nothing from it.
- UI note, untouched: a gold icon with a NEW! badge at the top of the radar screen (about norm 295,60). Its function is unknown; it is not part of this unit's stack work. The next radar unit reads it before tapping anything.
- Capture channel recovered: the device channel that failed the last twelve-plus passes (Issue 282, screen-capture failure, Last War window off-Space) is working again in this pass: the Last War window is on-screen at 763x1050, global (73,30), and screenshots and OCR read normally. Recovery noted in the record and commented on Issue #282 by this pass. The Dock-icon unblock is no longer the only route: the window returned to the active Space on its own (the Mac mini came back online about 10:20 PT after about 50h offline; the pid changed 59735 to 98156, so the app relaunched - the relaunch is inferred from the pid change, not observed). If the capture fails again, the recovery question is what moved the window back, not the login. The 1853 passes record is a second independent live read on the same recovered channel (window 372131, 788x1083, pid 98156); see shop-claims 1.29.0.
- Returned to the base screen afterwards (power 149,850,353). No diamonds, money, speedups or other spending. No alliance diplomacy, no assembly, no teleport.

## What the 2026-11-08 1256 and 1355 units added - stack-day Quick Execute 4 tasks, Claim All bar lockout carried, 16 stored, 10 pending, pins re-inventoried

- Unit radar-2026-11-08-1003 by ticker-1249, about 12:54 to 12:56
  local, status done - the stack-day completion standard is met:
  radar entered and verified, every executable ordinary task
  executed, closing reads recorded, pin inventory recorded untapped.
  Evidence in `_records_/2026-11-08/radar-tasks/1256-queue-run.md`
  (commit 6d4ec6287 on records/2026-11-08). Tracker marked done.
- Session: computer session cc-122 on the owner Mac mini. No
  device-access error, no different-device dialog, no login demanded.
  Nothing bought, no speedup used. One earlier click attempt failed
  without dispatch (stale observation, missing observation_id) and
  was retried with the fresh observation id; no input was sent by
  the failed attempt.
- Live duel posture from _tools_/duel.py at entry: duel day 7, Off
  day - settlement, radar posture stack (day ends 2026-11-08 18:00
  local). The unit window stamp (duel day 7 - radar stack) agrees
  with the live tool; no contradiction to resolve. This is a further
  live confirmation of the 18:00 reset (Issue #242); commented on
  Issue #242 by this run.
- Entry: base screen full HUD at entry (food 489.5M, iron 811.9M,
  coin 12.3M, stone 25.0M, gold 922.2K, power 149,850,353, diamonds
  13.22K, stamina 120, cart 4,397, Season II 7d 05:05:28). The dish
  icon was grounded fresh by visual grounding at norm (48, 710),
  inside the proven 52-62, 704-727 cluster, and opened the radar on
  the first tap.
- Entry verified on the radar screen itself: Lv.13, radar points
  267, stored 16/40, stamina 120, restore line "12 Radar Task(s)
  will be restored in 03:36:42". Bottom bar at entry offered Quick
  Execute: "You can complete 4 tasks, requires 40 Stamina." No Claim
  All was offered at entry.
- Quick Execute: one tap at the grounded button centre norm (491,
  945). Stamina 120 to 80, exactly 4 tasks at 10 stamina each. Radar
  points stayed 267, confirming nothing was claimed.
- Closing reads (live, same unit): Radar Lv.13, radar points 267,
  stored 16/40, stamina 80, restore line "12 Radar Task(s) will be
  restored in 03:36:12". Stored 16/40 plus the 12-task restore
  landing in about 3.6 hours reaches 28/40, below the 40 cap, so no
  cap pressure before the next unit.
- Named blocker carried forward: after the batch the bar flipped to
  Claim All only, "10 task rewards can be claimed", with no further
  Quick Execute offer. 6 of the 10 were already pending at entry
  (the entry bar showed Quick Execute despite them, the known
  single-offer behaviour). Claim All was NOT tapped, per the
  stack-day red line. The next radar unit inherits this blocker and
  the pending count of 10, per the stack-day completion standard's
  named-blocker rule.
- Pin inventory (untapped, per the stack handling rule): grey skull
  pin with red dot, top centre; blue skull pin with red dot, right;
  blue helmet pin, lower centre-left; grey skull pin with red dot,
  lower centre; portrait pins (alliance members, not tasks):
  [AP3x]Texan Apex, [AP3x]TheGoldenEclipse, [AP3x]papillon707,
  [AP3x]Cinmor. No purple question-mark story pin visible in this
  view. No pin was tapped, so no claim leaked onto this non-scoring
  day.
- Duel delta test still owed (VS panel not opened in this unit).
- Unit radar-2026-11-08-1003 by ticker-1352, about 13:53 to 13:57
  local, status partial. Evidence in
  `_records_/2026-11-08/radar-tasks/1355-queue-run.md` (commit
  bf20e1a48 on records/2026-11-08). Same unit id as the 1256 unit:
  the delivery-time check found this unit id had already been
  executed by ticker-1249 (done, record 1256) and its done unit file
  was already on the live records/2026-11-08 branch. The local sync
  re-produced it because the local tree never received the branch's
  done records. This pass left the branch head's done unit file
  intact; this partial lives in this record file and the day INDEX
  only. Filed as Issue #466 (tooling), related to #465.
- Entry via the satellite dish icon at norm 50,740 (fresh screenshot
  ground); the dish opened the radar on the first tap.
- Radar screen entered and verified live: Lv.13, radar points 267,
  stored tasks 16 of 40, stamina 92 (top right), restore line
  "Fully restore at 11-8 22:32:10 local time".
- Stack posture held throughout: nothing executed, nothing claimed,
  no pin tapped.
- BLOCKER (named, carried from the 2026-10-31 trap): the bottom bar
  presents ONLY "10 task rewards can be claimed" with a Claim All
  button - no Quick Execute offer. The 16 stored ordinary tasks
  therefore could not be executed in this unit. Claiming on a stack
  day is forbidden (claims leak onto a non-scoring day), so the bar
  was left untouched. This is the same Claim All bar lockout measured
  in four units on 2026-10-31; the block is carried into the next
  radar unit's opening read, so the stack is planned around it
  instead of rediscovered hourly. Pending reward count at close: 10.
- No cap pressure: stored 16 of 40, full restore at 22:32 local
  (about 8 hours 38 minutes away); even a 12-task restore lands at
  28 of 40, below the cap.
- Pin inventory (stack rule, untapped): six pins standing on the
  radar map - grey animal/skull pin, about norm 573,314, red dot;
  portrait pin (man's face), about norm 718,314, red dot; blue skull
  pin, about norm 718,395, red dot; blue helmet pin, about norm
  415,646, no red dot seen; grey handshake pin, about norm 501,646,
  red dot; brown animal-face pin at the southwest map edge, about
  norm 79,762, no red dot (same pin inventoried in the 2026-11-07
  1912 unit at norm 85,738 - the position drifts per view). All left
  for the next release-day unit to identify under the release
  handling rule.
- Restore-line note: the 1256 "12 Radar Task(s) will be restored in
  03:36:42" countdown and the 1355 "Fully restore at 11-8 22:32:10"
  clock line are different counters (task-restore countdown vs
  full-restore time), both recorded as read, not reconciled into one
  figure.
- Returned to the base screen afterwards (power 149,850,353). No
  diamonds, money, speedups or other spending. No alliance
  diplomacy, no assembly, no teleport.
- Follow-up: the next radar unit opens with this blocker already
  known: if the bar still offers only Claim All, the stack stays
  locked until the release day (Day 1, 2026-11-09) claims the pending
  rewards and frees the offer. The pending count of 10 is carried,
  not trusted - the next unit re-reads the bar live.

## What the 2026-11-08 2028 unit added - duel rolled to day 1 Radar Training RELEASE, radar screen never entered, dish grounding failed twice, game left on the Age of Oil research tree

- Unit radar-2026-11-08-1803 by ticker-2002, about 20:15-20:24
  local, status partial. Evidence in
  `_records_/2026-11-08/radar-tasks/2028-queue-run.md` (commit
  eee08287 on records/2026-11-08). Nothing executed, nothing
  claimed, no map pin tapped. The radar screen was never entered.
- Posture: live duel posture from tools/duel.py at entry: duel
  day 1, Radar Training, radar_posture RELEASE, day ends
  2026-11-09 18:00 local. The unit window stamp (day 7 stack)
  is stale - the duel week rolled at about 18:00 local today.
  The live posture governs, so this unit ran as a RELEASE unit:
  claim everything claimable, pins included. The roughly 5
  minute dead window after the roll is long past (entry 20:15).
  The delta test (VS panel duel score before and after) is still
  owed - no VS read was taken in this unit.
- Opening state carried from the 1355 unit (13:53 local): Lv.13,
  radar points 267, stored 16 of 40, stamina 92, full restore
  11-8 22:32:10 local, 10 rewards pending behind a Claim All only
  bar, 6 pins inventoried untapped. No live radar read was
  obtained in this unit, so every figure here is carried, not
  re-measured.
- Entry failure, first attempt: the satellite dish icon was
  grounded at norm (54,583) from a visual-grounding call on the
  20:17 base screenshot. The tap opened the Intercity Trade
  (trucks) panel instead - "Today's Trade Count: 0/5", four
  trucks standing, Mega Mode button. Backed out untouched with
  the back arrow at (55,931), which returned to the base at once.
  The grounding tool mislabelled the truck slot as the dish -
  the same mislabel the profile records for the 0636 unit.
  Incidental read only: trade count 0/5 today (the trucks
  regular owns it; nothing dispatched or plundered from this
  unit).
- Entry failure, second attempt (R2 pivot - re-grounded fresh
  from an enlarged crop of the left column, switched to a
  crop-measured point): the tap at norm (54,780) opened the
  BUILD menu (Economy tab: Oil Well, Drone Parts Workshop,
  Farmland, Iron Mine, Food Warehouse). The crop measurement put
  the dish lower than the control that actually sits there - the
  build/hammer icon. Nothing built, nothing tapped in the menu.
- Recovery failure: the tap at (113,888) on the Build screen's
  bottom-left list icon opened THE AGE OF OIL research tree
  instead of closing the menu (all nodes 0/10, queue timers
  20:13:57:39 and 08:47:50 - read only, no research started,
  nothing spent). Two taps on the tree's back arrow at (109,894)
  and at the re-grounded centre (131,898) produced no change;
  the control channel returned explicit guidance that background
  clicks do not reach some controls and to use click_element with
  the control's visible label, or the keyboard, instead. Return
  and Esc are never used on this app. Per R2 the tap method ended
  there.
- Game left on THE AGE OF OIL research tree at the unit's close.
  No state changed, nothing spent, no research started, no claim
  made - the 10 pending rewards and the 16 stored tasks are still
  waiting for the next radar unit, and no claim leaked onto a
  non-scoring day (today IS the scoring day; the rewards are
  simply still unclaimed).
- Closing reads: no live radar reads in this unit: stored,
  pending rewards, radar points, stamina and restore line are all
  unverified carries from the 1355 unit (16 of 40, 10 pending,
  267 points, stamina 92, full restore 22:32:10 local). The next
  radar unit must re-read them live on the radar screen itself.
- Base HUD read live about 20:17 local: power 149,209,253, food
  499.1M, iron 821.2M, coin 15.9M, diamonds 13.22K, cart 4,467,
  stamina 120, VS timer 21:43:24, Season II 6d 21:43:23. Wanted
  Boss badge 1, timer 00:00:53 at 20:07; badge 2, timer 00:00:49
  at 20:19.
- Outcome: partial. Release-day radar work not started: the
  screen was never entered, so the Claim All bar, the stored
  tasks and the pins all stand unworked. The next radar unit
  opens with (a) the release-day claim still pending (10 rewards
  plus 16 stored tasks, duel day 1, claims score +30,000 each as
  displayed), (b) the dish entry still ungrounded - the (50,740)
  point that opened the radar first try at 13:53 today is the
  next point to try, NOT the (54,583) or (54,780) points used
  here, and (c) the game sitting on THE AGE OF OIL research tree
  with its back arrow unresponsive to background clicks - back
  out with click_element on the arrow if the catalog names it, or
  relaunch the app (state is server-side; prior units relaunched
  after crashes with no loss), then re-ground the dish from a
  fresh full-HUD base screenshot. Tracker untouched for partial,
  per the queue rules.
- Method finding for the next unit: the visual-grounding tool
  mislabelled the dish slot twice in one unit (truck slot as
  dish at 20:17; the crop-measured dish point landing on Build
  at 20:24), and the research-tree back arrow does not respond to
  background clicks at all. Both are method findings, not game
  state; the radar profile already documents the grounding
  mislabel (0636, 1913, 0226 units) and the back-arrow guidance
  is new in this unit. No diamonds, money, speedups or other
  spending. No alliance diplomacy, no assembly, no teleport.

## What the 2026-11-08 2335 unit added - release day 1, 16 tasks executed, 44 claims, stored 0 of 40, dish re-grounded to (37,736), 6 pins left untapped

- Unit radar-2026-11-08-2203 by ticker-2334, about 23:35 to 23:50 local, status partial - the ordinary-task release cycle is fully done (stored 0 of 40, pending 0, bar gone, 44 claims, 16 executions) but the release completion standard also requires every map pin closed, and 6 pins stand untapped. Evidence in `_records_/2026-11-08/radar-tasks/2335-queue-run.md` (commit 86b26f5ce0 on records/2026-11-08). Tracker untouched, so radar stays due.
- Entry: first tap at norm 59,687 (estimated from the fresh screenshot) missed the dish and only showed a transient "Achievements 8/16 Completed" tooltip; the radar did not open. Re-grounded from a magnified crop of the left icon column: the satellite dish icon with the red "10" badge sits at pixel about 24,700 in the 642x951 window, i.e. norm 37,736. The second tap at norm 37,736 opened the radar on the first try. The profile coordinate (norm 62,727, measured 2026-10-29 in a 763x1050 window) is stale in this window geometry. The (50,740) retro preference (Issue #484) was NOT tested in this unit - it stands as the first try, and the dish drifts per session, so re-ground fresh from a magnified crop of the left icon column in every unit.
- Entry state, read live: Lv.13, radar points 267, stored tasks 39 of 40, stamina 120 (top right), restore line "12 Radar Task(s) will be restored in 05:59:54". Bottom bar at entry offered Quick Execute for 1 task (10 stamina).
- Release cycle, alternating Quick Execute and Claim All until the bar disappeared: executed 16 tasks in 6 batches (1, 5, 3, 2, 3, 2) for 160 stamina; claimed 44 task rewards in 7 Claim All taps (11, 9, 8, 5, 5, 5, 1). Radar points 267 to 311 (+44, one per claim, as measured). Stored 39 of 40 to 0 of 40; pending rewards 0; no bottom action bar at close.
- Free stamina claim taken once in the Regain Stamina panel (Remaining Today read 2 of 2 at entry, 75 stamina claimed; stamina 11 to 86 at that point). The 100 stamina for 300 rubies Buy button was never touched. Stamina items were not used (inventory counts read in the panel: 10-stamina x641, 50-stamina x665). Stamina at close 36.
- Claimed rewards, summed from the seven CONGRATULATIONS popups: orange chest x50, radar coil x370, EXP 58.4M, blue triangle 2,496, blue card 8.0K, 5m speedup x8, 1m speedup x50, iron 14.0M, food about 11.7M, coin about 9.2M, Lv.1 chest x1.
- HUD cross-check on return to base: power 149,209,253 unchanged; food 501.9M to 513.8M (+11.9M), iron 824.0M to 838.3M (+14.3M), coin 15.8M to 25.2M (+9.4M) - consistent with the radar claim totals above plus march yields shown during Quick Execute (floating 660,000 / 1,000,000 / 2,300,000 lines).
- Pin inventory (release rule, untapped): at close, 6 pins standing, none tapped - 2 blue arrow pins (one with a red dot), 2 orange skull pins (no red dots visible), 1 portrait pin (a man's portrait in a blue frame, no red dot visible), 1 purple arrow pin (red dot not clearly visible). The brown circular animal-face pin inventoried on 2026-11-07 (norm about 85,738) was not seen in this unit's map views; the map panned away from the southwest edge and it may be off-screen rather than gone. The pins were not worked because the unit's 15 minutes were spent on the ordinary-task release cycle and the device token expired at 23:50:29. They fall to the next radar unit under the release handling rule.
- Dish badge note: the dish badge read "10" at entry while stored was 39 of 40 and only 1 task was Quick Executable - the badge number does not equal the stored count. What it counts is not established; added as an open question.
- One UI element noted but not touched: the gold icon with a NEW! badge at the top of the radar screen (about norm 295,60). Its function is still unknown; added as an open question. It is not part of this unit's work.
- Duel note: the duel-score delta test is still owed - this unit did not visit the VS panel. If the in-game displayed value of 30,000 per task held, 44 claims would be about 1.32M duel points - stated here as an inference only, not a measurement. The duel-score unit in the inbox (duel-score-2026-11-08-2230) reads the VS panel separately.
- Restore-line note: the closing toast read "Fully restore at 11-9 23:39:11 local time", meaning unverified; it is a different counter from the entry "12 Radar Task(s) will be restored in 05:59:54" countdown, recorded as read, not reconciled.
- Result stats: target 1, achieved 0, resources_gained coin about 9.2M plus iron 14.0M food about 11.7M EXP 58.4M, costs 160 stamina plus 1 free claim, verified yes, blocker_category time (unit cap reached with pins unworked), stored_tasks 0, tasks_executed 16, tasks_claimed 44, pins_inventoried 6, pins_worked 0, stamina 36, radar_points 311, restore_in_minutes 360, free_stamina_claims 1, device_takeovers 0.
- Commented on Issue #484 by this run with the fold.
- Game left safe: base screen, no purchase, no diamond spent. No alliance diplomacy, no assembly, no teleport.
- Follow-up: the next radar unit works the 6 standing pins under the release handling rule and re-grounds the dish fresh per session (newest verified first-try point (37,736) in the 642x951 window; the (50,740) preference untested this unit). It falls to the next run.

## What the 2026-11-09 0159 unit added - stack empty 0 of 40 done, dish grounded (54,707) first tap, 6 pins inventoried untapped, NEW! badge re-seen

- Unit radar-2026-11-08-2203 by ticker-0140, about 01:56 to 01:59 local, status done. Evidence in `_records_/2026-11-09/radar-tasks/0159-queue-run.md` (commit 3d5dc8314 on records/2026-11-09). Computer session cc-207.
- Radar screen, entry verified by its own reads: Lv.13, radar points 311, stored 0/40, stamina 62, the green gauge at 100%. Restore line: "12 Radar Task(s) will be restored in 03:41:39." Stack EMPTY: 0 stored tasks, so Quick Execute has nothing to execute. No Claim All bar is shown, so no rewards are pending. The stack-day completion standard from the 1256 unit is met (closing reads recorded, pin inventory recorded untapped) and the tracker is marked done.
- The 1355 unit on 2026-11-08 reported 16 stored tasks unexecuted with a Claim All bar lockout and 10 rewards pending; the stack has since emptied (executed, claimed or expired - not determined in this unit, recorded as observed, not asserted). No lockout state remains on this screen.
- Pin inventory, untapped per the stack handling rule: 2 blue arrow pins (ordinary tasks, left and centre); 2 orange skull pins (top-right); 1 purple arrow pin (lower centre); 1 portrait pin (hero face, left-centre). No pin was tapped, so no claim or task was started. Hypothesis, NOT verified: the orange skull pins may be the same skull signal that appears as a timed badge on the base right edge (seen badge 1, 4 and 2 with about 00:00:24-00:00:28 timers in this pass) - the next radar unit should check whether tapping an orange skull pin matches that timer. The skull signal itself is filed as knowledge Issue #498 by this run.
- NEW! badge on a yellow icon at the top of the radar screen (next to the 311 points) - observed only, not opened. This re-confirms the gold NEW! icon the 2335 unit saw (about 295,60); its function is still unknown.
- Entry: the dish grounded fresh on the live screenshot at (54,707) and opened the radar on the first tap - the retro-preferred point (50,740) from Issue #484 and this grounded point agree within the same slot. The radio-looking icon at that position IS the dish slot in this rotation; the slot rotates, so every unit still re-grounds fresh. Commented on Issue #484 by this run: (54,707) is a new verified first-tap point in this rotation, (50,740) itself still untested as a direct tap.
- No diamonds or money spent. Nothing claimed, fought, dispatched, donated, dug or bought. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 0, achieved 0, resources_gained none, costs about 4 minutes of unit time, no items spent, verified yes, blocker_category none.

## What the 2026-11-09 0335 unit added - release day, Rare Iron Mine gathering dispatched, dish re-grounded (51,718) first try, 5 pins inventoried unattempted

- Unit radar-2026-11-09-0203 by ticker-0334, session 03:35:38 to 03:39:33 local (235 seconds; the record's own "about 03:36-03:49" and "about 14 min" figures are corrected in the record's appended correction - the unit file's duration_seconds 235 governs, nothing else in the record changes), status partial. Evidence in `_records_/2026-11-09/radar-tasks/0335-queue-run.md` (commit 063a5bde7f on records/2026-11-09). Live duel posture from _tools_/duel.py at entry: duel day 1, Radar Training, radar posture release, day ends 2026-11-09 18:00 PT. Release posture governs, so this unit claimed everything claimable and worked pins toward a closing read.
- Entry: the game was open on the Alliance Techs screen (Donation Count 9/30, left from the previous donations unit - not worked here, one unit one type). Closed the tech panel and the Alliance overview untouched and returned to the base. The dish was re-grounded fresh from a magnified crop: the first tap at norm (55,689) missed (top edge of the dish circle), the re-grounded centre norm (51,718) opened the radar on the first try. Commented on Issue #484 by this run: (51,718) is a new verified first-try point in this rotation; (55,689) missed high; the (50,740) retro preference is still untested as a direct tap.
- Entry verified on the radar screen itself: Lv.13, radar points 311, stored 0/40, stamina 82, restore line "12 Radar Task(s) will be restored in 02:01:04", NEW! badge on the radar icon. No bottom action bar - nothing stored to execute and no rewards pending to claim.
- Pin work: the left blue axe pin opened a Rare Iron Mine card (Allow Troops to gather incredibly fast, rewards iron 105.6K and radar item 10, timer 04:03:57). Go jumped to a Lv.15 Iron Mine on the world map (Collector N/A, 720,000/720,000, Gathering Speed +10000%, despawns in 04:01:26). The green pickaxe opened the deploy panel (Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, Gathering amount 720.0K/720.0K, Gathering time 00:06:57, Expected to finish at 2026-11-9 03:45 as displayed). March tapped at the grounded low point norm (500,759) and verified real: March Queues 1/4, "Go X:467 Y:432, 00:00:08" on the world map. Gathering costs 0 stamina. The 720K iron lands on squad return and the pin reward (iron 105.6K, radar item 10) is claimed at the radar afterwards - both fall to the next radar unit, not this one.
- Pin inventory at close (radar screen, entry read): blue axe pin centre, two orange skull pins top right, purple axe pin centre, portrait pin left middle - five pins unattempted in this unit. NOTE the record lists the blue axe pin both as the worked pin (Rare Iron Mine dispatched) and in the unattempted inventory; whether the pin persists on the radar after its gathering is dispatched is unresolved - the next radar unit verifies it live rather than assuming either way. Per rule R7 the next unit checks the Iron Mine gathering claim first, then works the orange skulls, the purple axe and the portrait pin, each to a closing read. The skull-timer match test for Issue #498 is still unrun (no skull pin was tapped).
- Closing state (live reads, same unit): Radar Lv.13, radar points 311 (unchanged - no claims were available), stored 0/40, stamina 83 at the gathering dispatch (regen from 82), restore line alternating between the countdown and "Fully restore at 11-9 23:39:11 local time" as displayed.
- Duel delta test still owed: the VS panel was not opened in this unit.
- No diamonds or money spent, no Buy tapped, no other activity worked from this unit. Tracker untouched for partial, per the queue rules.
- Result stats: target 1, achieved 0, resources_gained none in-unit (720K iron and pin reward land on the next unit), costs 0 stamina, verified yes for the dispatch, blocker_category time (unit window, pins unworked), pins_worked 1, pins_inventoried 5, device_takeovers 0.

## What the 2026-11-09 0852 unit added - release day, 3 tasks executed, 11 claims, points 311 to 322, Iron Mine pin claim first next unit

- Unit radar-2026-11-09-0603 by ticker-0842, session cc-246, about 08:52 to 09:00 local, status partial - the ordinary-task release cycle is fully done (stored 0 of 40, 11 claims) but pins were not reached inside the token window, so the release completion standard is not met. Evidence in `_records_/2026-11-09/radar-tasks/0852-queue-run.md` (commit ec55aa585 on records/2026-11-09). Tracker untouched for partial, per the queue rules.
- Entry (measured): dish grounded fresh from the current base screenshot at norm (51,726) (red badge 6 on the dish) and opened the radar on the first tap - the (50,740) retro preference was not needed. The camera was still panned on the Drill Ground cluster from the previous unit; the dish is a HUD icon and the tap landed cleanly without a view restore. A merely panned camera does not block the dish tap; the restore-first rule still binds when a building panel is open (see the entry precondition).
- Entry state, read live: Lv.13, radar points 311, stored 2/40, stamina 120, restore line "12 Radar Task(s) will be restored in 02:46:23" alternating with "Fully restore at 11-10 05:39:11 local time". Bottom bar: "You can complete 3 tasks, requires 30 Stamina." plus Quick Execute. Duel posture at entry (live from _tools_/duel.py): duel day 1, Radar Training, radar posture release, day ends 2026-11-09 18:00 PT.
- Restore-shape datapoint (second, against the batch hypothesis): the 12-task restore the 0335 unit expected around 05:36 PT did NOT land as a batch - stored read 2/40 at 08:52, not 12/40. Recorded in the open questions; the restore line as written does not predict the stored count.
- Quick Execute: tapped at norm (500,952); stamina 120 to 90 (3 tasks, 30 stamina). Bar flipped to Claim All: "11 task rewards can be claimed". Claim All tapped at the same point: CONGRATULATIONS panel - radar item x110, EXP 15.9M, blue item 4.0K, blue triangle 366, iron 5.0M, food 2.3M, coin 2.0M. Radar points 311 to 322 (+11, one per claim, as measured). Stored 2/40 to 0/40.
- After the claim the bar offered Quick Execute again: "You can complete 1 tasks, requires 10 Stamina." with stored reading 0/40 - the 1 task is unexplained (a restore landing mid-unit or a stale count); left for the next radar unit, not chased inside the expiring token window. Recorded in the open questions.
- Pin inventory at close (radar screen, unchanged by this unit): portrait pin top left, blue skull pin top left, blue skull pin top centre, green skull pin right middle, two grey skull pins bottom, gold/pink pin cluster left centre (the 0335 Rare Iron Mine gathering pin - its claim was NOT checked in this unit). Per rule R7 the Iron Mine gathering claim is the first action of the next radar unit, then the skull pins and the portrait pin, each to a closing read.
- Duel delta test still owed: the VS panel was not opened in this unit.
- Token note: the device token expired 09:00:48 PT; the session was ended about 09:00, inside the window; no game input ran after expiry. No diamonds or money spent, no Buy tapped, no other activity worked from this unit.

## What the 2026-11-09 1253 unit added - release day, 6 tasks executed, 14 claims, points 322 to 336, dish grounded (62,727) first tap, 6 pins unworked

- Unit radar-2026-11-09-1003 by ticker-1234, about 12:43 to 12:53 local, status partial - the ordinary-task release cycle is fully done (stored 0 of 40, 14 claims) but at least 6 map pins stand unworked, so the release completion standard is not met. Evidence in `_records_/2026-11-09/radar-tasks/1253-queue-run.md` (commit da81e137e on records/2026-11-09). Tracker untouched for partial, per the queue rules.
- Entry (measured): dish grounded fresh at norm (62,727) (red badge 1) and opened the radar on the first tap at 12:44 PT - the 2026-10-29 measured point works again in this window, so it is not stale after all; the dish still drifts per session, so every unit still re-grounds fresh. Commented on Issue #484 by this run: (62,727) is the newest verified first-tap point, joining (51,718) and (51,726); the (50,740) retro preference remains untested as a direct tap.
- Entry state, read live: Lv.13, radar points 322, stored 3/40, stamina 120, restore line "12 Radar Task(s) will be restored in 04:54:34", "Fully restore at 11-10 11:39:11 local time" (later reads show 17:39:11 - see the restore-line note below). No radar unit had run today before this one; last night's 23:35 unit closed stored 0/40, points 311, stamina 36.
- Quick Execute 1 (12:51 PT): bar offered "You can complete 5 tasks, requires 50 Stamina" while stored read 3/40. Stamina 120 to 70 proves 5 tasks executed. Bar flipped to "11 task rewards can be claimed". Claim All 1 (12:52 PT): 11 rewards claimed, radar points 322 to 333 (+11, one per claim). CONGRATULATIONS rewards: radar discs 110, blue-triangle item 726 (unidentified item, likely drone parts - unverified), EXP 14.5M, chips 2.4K, coin 2.5M, iron 1.9M, food 4.3M, Lv.1 chest x2.
- Quick Execute 2 (12:55 PT): bar offered "You can complete 1 tasks, requires 10 Stamina" while stored read 0/40. Stamina 70 to 61 (60 spent on the two batches, +1 regen in about 5 minutes). Bar flipped to "3 task rewards can be claimed". Claim All 2 (12:56 PT): 3 rewards claimed, radar points 333 to 336 (+3). CONGRATULATIONS rewards: radar discs 30, EXP 6.0M, chips 1.6K, iron 1.7M, food 1.1M, coin 531.6K.
- After the second claim the bottom bar is gone entirely - no Quick Execute offer, no Claim All offer. Ordinary-task cycle fully done: stored 0/40, pending 0.
- Totals in this unit: tasks executed 6 (5 + 1), tasks claimed 14 (11 + 3), radar points 322 to 336 (+14, one per claim). Rewards: radar discs 140, EXP 20.5M, chips 4.0K, coin about 3.0M, iron 3.6M, food 5.4M, blue-triangle item 726, Lv.1 chest x2. Stamina 120 to 61 (60 spent, 1 regenerated). No free stamina claim needed or taken. No diamonds or money spent.
- Bar-vs-stored evidence (open question refined): the bar's completable count exceeded the stored count twice (5 vs 3, then 1 vs 0), and the second Claim All paid 3 rewards for 1 executed task. The consistent reading: pending rewards can hide behind the bar's single offer - when the bar shows Quick Execute, claimable rewards already pending are not shown; after the execute the bar flips to Claim All and shows executed + hidden pending together (1 executed + 2 hidden = 3). The bar's Quick Execute count itself exceeding stored (5 vs 3, 1 vs 0) is still unexplained - possibly tasks restore in a trickle the stored counter does not show, or the bar counts a different pool. Left open for the next unit.
- Restore-line disagreement (new datapoint): the full-restore time read "11-10 11:39:11 local time" at entry and "11-10 17:39:11 local time" at close, six hours apart in the same unit; the close read is the live one. Do not quote a restore time from an entry read without a closing re-read. Recorded in the open questions.
- Radar points 322 at entry against 311 at last night's 23:35 close (+11) with no radar unit in between and 6 rewards still pending at entry. What moved the counter is unverified - possibly the owner's own play this morning; not asserted.
- Pin inventory (release rule, unworked): the map panned between reads, so the same pins reappeared in different screen positions; the inventory merges the unit's three clean map views. First view (12:44): 3 grey skull pins with red dots, 1 green skull pin with a red dot, 1 purple skull pin with a red dot, 1 blue teardrop pin (no dot visible), 1 brown animal-face pin at the southwest edge. Second view (12:54): 1 orange skull pin with a red dot, 1 grey skull pin with a red dot, 1 portrait pin ([AP3x] name label). Closing view (12:53): no pins in frame - the map had panned to an empty sector; the sweep animation was running. At least 6 distinct pins stand. None was tapped: the ordinary cycle took the unit to its close first, and the device token lease ran to 12:57:48, leaving too little time for a pin flow plus closing reads. Per the record, the pins are the same standing set deferred from the 2026-11-08 23:35 unit (6 pins then, also unworked). Per rule R7 the next radar unit starts with the pins, not the ordinary cycle - and the 0335 Rare Iron Mine gathering claim is still unchecked after two units (0852, 1253), so the next unit checks whether that pin still stands and claims it if it does, then works the pins.
- Gold NEW! icon: the gold icon with a NEW! badge at the top of the radar screen (about norm 295,60) is still untouched and its function still unknown (also noted 2026-11-08).
- Duel delta test still owed: this unit did not visit the VS panel, so no before/after duel score was read. If the displayed +30,000 per task held, 14 claims would be about 420,000 duel points - stated as an inference only, not a measurement.
- An "Important: Pr..." toast appeared top-right at close (cut off, unread) - not radar-related, left alone.
- Closing reads: stored 0 of 40, pending rewards 0, bottom bar gone, radar points 336, stamina 61, restore line at close 12 tasks in 04:48:41, "Fully restore at 11-10 17:39:11 local time" (disagrees with the 11:39:11 read at entry - the close read is the live one), tasks executed 6, tasks claimed 14, pins inventoried 6, pins worked 0, free stamina claims taken 0.
- Result stats: target 1, achieved 0, resources_gained coin about 3.0M plus food 5.4M iron 3.6M EXP 20.5M radar-discs 140 chips 4.0K blue-triangle 726 Lv.1-chest x2, costs 60 stamina plus about 10 minutes, verified yes, blocker_category time (unit cap reached with pins unworked), stored_tasks 0, tasks_executed 6, tasks_claimed 14, pins_inventoried 6, pins_worked 0, stamina 61, radar_points 336, restore_in_minutes 289, free_stamina_claims 0, device_takeovers 0.

## What the 2026-11-09 1717 unit added - release day 1, ordinary cycle clear, 12:44 pin set absent, restore lands 12 tasks about 17:40, partial

- Unit radar-2026-11-09-1403 by ticker-1704, about 17:07 to 17:17 local, status partial - the ordinary-task release cycle is fully done (stored 0 of 40, pending 0) but the release completion standard also requires every map pin closed, and the pin set it refers to is no longer standing. Evidence in `_records_/2026-11-09/radar-tasks/1717-queue-run.md` (commit 9806b8352 on records/2026-11-09). Tracker untouched for partial, per the queue rules.
- Entry (measured): dish grounded fresh at norm (62,727) and opened the radar on the first tap at 17:07 PT - the same point as the 1253 unit, so (62,727) is re-confirmed in this window; the dish still drifts per session, so every unit still re-grounds fresh. Commented on Issue #484 by this run. Entry verified on the radar screen itself: Lv.13, radar points 336, stored 0/40, stamina 93, restore line "12 Radar Task(s) will be restored in 00:27:33" at first read, "Fully restore at 11-10 17:39:11 local time". Live duel posture from _tools_/duel.py at entry: duel day 1, Radar Training, radar posture release, day ends 18:00 PT, about 51 minutes left.
- Ordinary cycle already clear from the 12:53 unit close: stored 0/40, no pending rewards, bottom bar gone. Nothing to execute or claim in the ordinary pool.
- Pin sweep, per rule R7 (the 12:53 unit left at least 6 pins unworked, so this unit starts with the pins): three map sectors swept by drag (west, east, north) - no skull pin with a red dot stands anywhere in the swept sectors. The pin set inventoried at 12:44 is absent about 4.5 hours later - 3 grey skull, 1 green skull, 1 purple skull, 1 blue teardrop and 1 portrait pin in the first view, 1 orange skull in the second view, at least 6 distinct pins, none standing - presumably expired or despawned in the gap; the mechanism is unverified, and no expiry was observed live. No pin was tapped or claimed because no tappable pin stands.
- CORRECTION: the 0335 Rare Iron Mine gathering claim carry closes as UNVERIFIABLE, not as done. The claim was never checked by the 0852 or 1253 units, and the pin that carried it is now gone from the map, so the check can no longer be run. The 720K gathering dispatched at 03:35 (finish 03:45) was never attributed to a HUD read either, so whether the iron landed is unverified, not asserted. The R7 first-action carry for the Iron Mine pin is retired on this read; the next radar unit works whatever pins stand at its own entry.
- Brown animal-face circle: the only pin-like mark in the swept sectors, at the southwest edge at entry. Three grounded taps (norm 62,738, then 97,736, then the measured centre 132,762) produced no card and no screen change. It carries no red dot. Treated as a non-tappable map element, not a radar task pin - identified with reason, left alone. Per rule R2 the tap method ended after the second no-change tap; the third tap was the fresh-centre variant and also no-opped. This resolves the 2026-11-07 standing question for this mark: it is not a pin.
- "Violet's Gift received!" toast appeared after the first map tap, and an alliance toast ("Important: President HawksMav appointed Rage inferno as...") crossed the top at the same time. No reward was measured from the gift toast - radar points stayed 336, stamina moved only by regen (93 to 94) - so nothing is claimed as gained. The toast is recorded as observed, not as a reward.
- Gold NEW! icon: the gold icon with a NEW! badge at the top of the radar screen (about norm 295,60) is still untouched and its function still unknown - fourth sighting (2335, 0159, 1253, 1717).
- Restore gap, rule R6: the restore lands 12 tasks at about 17:40 PT, 20 minutes before the 18:00 duel-day roll. No radar unit is scheduled in that window: this unit's lease ends 17:27, the 17:30 zero-sweep unit runs the ledger, and the next radar unit (radar-2026-11-09-1803) is not_before 18:03, after the roll, when the posture flips to stack. Per rule R6 a priority 1 radar successor is enqueued for the pre-roll claim window: radar-2026-11-10-0118, not_before 17:40 PT, expires 18:00 PT, window "duel day 1 - radar release, restored batch claim before 18:00 roll". If the 17:34 tick's pass finishes the sweep in time it can claim the restored batch (12 tasks, about 360,000 duel points at the displayed 30,000 each - inference only, not a measurement); if not, the batch stacks into duel day 3.
- Closing reads: stored 0 of 40, pending rewards 0, bottom bar gone, radar points 336, stamina 94, restore line at close 12 tasks in 00:23:37, "Fully restore at 11-10 17:39:11 local time", tasks executed 0, tasks claimed 0, pins inventoried 1 (brown circle, non-tappable), pins worked 0, pins absent 6 (the 12:44 set), free stamina claims taken 0.
- Duel delta test still owed: the VS panel was not opened in this unit.
- No diamonds or money spent. No priced button tapped. No other activity's rewards touched. The Mission-screen radio icon was not opened. No pin was tapped blindly after the R2 method end.
- Result stats: target 1, achieved 0, resources_gained none, costs 0 stamina plus about 10 minutes, verified yes, blocker_category f (the 12:44 pin set was no longer standing at entry - missing precondition), stored_tasks 0, tasks_executed 0, tasks_claimed 0, pins_inventoried 1, pins_worked 0, pins_absent 6, stamina 94, radar_points 336, restore_in_minutes 24, free_stamina_claims 0, device_takeovers 0.
