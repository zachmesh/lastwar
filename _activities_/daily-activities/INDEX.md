---
title: Routine Activities
created: 2026-10-25T17:56:00Z
modified: 2026-11-12T11:32:17Z
level: L1
version: 1.32.0
description: The umbrella checklist of the every four hours routine, linking one folder per activity type - kept under its original daily-activities folder name for link stability
status: unverified
grounded_in:
  - source: in-game base screen observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner rule on 2026-10-26 - the routine is every four hours, not daily, and every regular is checked and done at every run whenever it is available
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (ended-trade-day close confirmed)
  - source: owner design on 2026-10-26 - remove the single every four hours job and split the routine into segment schedules rotating hourly, each segment looking at a specific set of tasks
  - source: owner refinement on 2026-10-26 - the segments run in the same hour, 15 minutes apart, not one per hour
  - source: owner refinement on 2026-10-26 - the spacing is 18 minutes, so the fires are :03, :21, :39 and :57
  - source: owner refinement on 2026-10-26 - make it 3 segments, 25 minutes apart
  - source: owner refinement on 2026-10-26 - 26 minutes apart
  - source: owner refinement on 2026-10-26 - 27 minutes apart, the final spacing
  - source: pre-reset zero sweep execution record 2026-11-01 1757 queue run (first zero sweep)
  - source: pre-reset zero sweep execution record 2026-11-07 1824 queue run (first pass, partial, first 17:30 sweep to run since 2026-11-02; record commit 840094b6ad on records/2026-11-07)
  - source: pre-reset zero sweep execution record 2026-11-08 1712 queue run (first pass, partial, 11 lines not at zero, 4 at zero, 5 unreadable, duel unmeasured, crystal and glittering not located, server disconnect with clean relaunch, power step-down 641,100 unexplained; record commit 9978e09a8 on records/2026-11-08)
  - source: pre-reset zero sweep execution record 2026-11-08 1740 queue run (second pass, partial, no line moved to zero since 1712, 3 at zero, 1 stack posture, 12 not at zero, 5 unreadable, crystal and glittering not located, power 149,209,253 holds, fifteenth same-day no-train confirmation, scheduling shortfall confirmed a second time; record commit 5f3a904f4 on records/2026-11-08)
  - source: zero-sweep 001 execution record 2026-11-09 1657 queue run (partial, 7 of 23 ledger lines read live, 6 units raised to priority 1; record commit c9a86fa74 on records/2026-11-09)
  - source: zero-sweep 002 execution record 2026-11-09 1748 queue run (partial, 5 of 23 ledger lines read live, pair total 12 of 23; record commit 2f4d783d8 on records/2026-11-09)
  - source: ticker-1822 execution records 2026-11-09 1838 1842 1846 1850 queue runs (mail gifts help done, passes partial, three 1403 units expired unrun; record commit 6761c35d1 on records/2026-11-09)
  - source: zero-sweep 001 execution record 2026-11-10 1634 queue run (partial, 1 of 23 ledger lines read live, coin bubble standing, Secret Command Post read live, remaining lines pass to the 17:30 sweep; record commit 986c1877 on records/2026-11-10)
  - source: zero-sweep 001 execution record 2026-11-11 1726 queue run (partial, 1 of 23 ledger lines read live to a close, trucks dispatch 1/5 and plunder 0/4 shortfall, donations points 4050 live, remaining count unread, skull timer sixth sighting; record commit bec20570e on records/2026-11-11)
  - source: zero-sweep 002 execution record 2026-11-11 1730 queue run (partial, 5 of 23 ledger lines read live, bubbles and mail not at zero, Glacieradon next wave 00:52:52, four fix-up units raised to priority 1, PR 655 conflict resolved and loop-health gap filed as Issue #661; record commit 6cbd479fc on records/2026-11-11)
  - source: ticker-0100 execution records 2026-11-12 0114 and 0126 queue runs (zombie-invasion 022 re-executed from a stale inbox copy, harvest-2203 panel Collects 12,195,086, thirteen stale inbox units reaped expired; record commit 911d317f8 on records/2026-11-12)
  - source: ticker-0134 execution record 2026-11-12 0151 queue run (radar-2203 failed, control channel outcome_unknown lock, Issue #689 second occurrence; record commit 889dda54f on records/2026-11-12)
  - source: ticker-0204 execution record 2026-11-12 0207 queue run (help-2230 failed, control channel outcome_unknown lock, Issue #689 third occurrence; arms-race/donations/survivors/training 2203 expired unexecuted; record commit b23df0eba on records/2026-11-12)
  - source: ticker-0234 zombie-invasion execution record 2026-11-12 0247 queue run (failed, control channel outcome_unknown lock, Issue #689 fourth occurrence, sessions cc-700 to cc-702, no dispatch, 7 stale 2203/2230 inbox copies expired; record commit c4faa2378 on records/2026-11-12)
  - source: ticker-0304 zombie-invasion execution record 2026-11-12 0320 queue run (failed, control channel outcome_unknown lock, Issue #689 fifth occurrence, fourth consecutive blocked pass, sessions cc-703 to cc-705, control-lock blocker recorded per R9 - pool pauses, successor 026 enqueued, 10 worktree + 5 live-pool stale 2230/2257 copies expired, PR #685 conflict resolved branch-side by merging main 0dc85d79; record commit 025264559 on records/2026-11-12)
  - source: queue-planning execution record 2026-11-12 0240 run (12 units staged for the 14:03/14:30 slots, 62 already present, scout diff 6-pass observation 52 observed 11 unexplained with 0 counts, pool inbox 78, done 1646; record commit 63947af68 on records/2026-11-12)
  - source: pr-integration execution records 2026-11-12 0300 run (BATCH, PR #681 merged, PR #685 conflicts with new main - commented, not merged, branch-side resolution for the 07:00 batch; PR #425 owner-gated) and 0330 run (NON-batch, PR #685 re-verified CLEAN against main 0dc85d79, awaits the 07:00 batch; record commits 7c30af3183b and ea3d9d0c5 on records/2026-11-12)
---

# Routine activities

Umbrella checklist for one round of the every four hours routine.
The routine is not a daily round (owner rule, 2026-10-26) - it runs
every four hours, and every regular in it is checked at every run
and done whenever it is available at that moment. Each kind of activity has its own
folder under `_activities_`, and that folder is where knowledge about
that kind accumulates. This page only lists the round in order and links
to those folders. Completion is never ticked here - each execution is
written as its own file in `_records_/<date>/<activity>/`, under the
date it happened and the activity it belongs to.

## The round, in the order worked on 2026-10-25

- [Mail rewards](../mail-rewards/INDEX.md)
- [Alliance help](../alliance-help/INDEX.md)
- [Alliance gifts](../alliance-gifts/INDEX.md)
- [Season warming](../season-warming/INDEX.md)
- [Secret missions](../secret-missions/INDEX.md)
- [Resource collection](../resource-collection/INDEX.md)
- [Research queue](../research-queue/INDEX.md)
- [Building queues](../building-queues/INDEX.md)
- [Radar tasks](../radar-tasks/INDEX.md)
- [Event claims](../event-claims/INDEX.md)
- [Daily missions](../daily-missions/INDEX.md), including
  [alliance donations](../alliance-donations/INDEX.md)
- [Shop claims](../shop-claims/INDEX.md)
- [Hero recruitment](../hero-recruitment/INDEX.md)
- [VIP rewards](../vip-rewards/INDEX.md) - the Daily Freebie, added
  after the evening sweep of 2026-10-25 missed it past the 19:00
  reset and the owner had to claim it himself. Any round after the
  reset claims it, even if it was claimed earlier that day.

## Folded into the round by the owner on 2026-10-25

Named and first executed on 2026-10-25 under the task intake
workflow, then folded into this routine by the owner the same
day. From the next round on they are worked with the list above.

- [Troop training](../troop-training/INDEX.md) - check every barracks
  and requeue any that has finished, at its highest tier.
- [Truck plunder](../truck-plunder/INDEX.md) - dispatch own trucks up
  to the daily trade count and plunder within the daily plunder cap.
  Plunder follows the owner shard rule in that folder - UR and SSR
  trucks only, guards below Squad 1, shards plentiful and right
  sided.
- [Alliance train](../alliance-train/INDEX.md) - if a train is in
  preparation, board carriage 2 with a 3 Trade Contract ticket, per
  the standing rule in that folder (the earlier free Like and Thank
  flow is superseded).
- [Survivor intake](../survivor-intake/INDEX.md) - take in every
  survivor waiting in the line at the front gate (named task 9).
- [Hidden treasures](../hidden-treasures/INDEX.md) - dig whenever a
  full set of seven fragments is on hand (the tab badge counts the
  digs available). Learned in the evening sweep of 2026-10-25.
- [Ghost ops](../ghost-ops/INDEX.md) - Thursdays only; check the tab
  on the event day inside its server time windows.

## The red dot habit

Red dots and numbered badges mean something can be done - sweep
them every round, claims first, and page through every page of a
hub to finish them rather than stopping at the first screen (owner
direction, evening of 2026-10-25). A numbered red badge counts what
can be done - the Hidden Treasures badge 1 was exactly one
affordable dig. The 2026-10-25 sweep found - the
Alliance button dot was waiting helps (Help All), the Season
badge was two pass claims, the radar badge was restored stored
tasks, and the Events badge was only the Frontline challenge
attempt marker. Only free claims are taken; anything priced,
diamond costing or PvP stays untouched without owner approval.

## The regulars list and its tracker

Owner direction, late evening of 2026-10-25 - the four-hourly run
performs all the regulars, not only Arms Race, and a list of the
regulars is kept so it is always visible what is still expected.

- The canonical list is `_tools_/regulars.json` - one entry per
  regular, with its cadence (every run for everything in the
  routine, daily with the 19:00 reset for VIP, Thursdays for
  Ghost Ops) and its segment (1 to 4). Every-run regulars become
  due again at each new cycle of their own segment - a regular
  done or skipped in an earlier cycle is never a reason to skip
  it in the current one.
- Since 2026-10-26 the routine runs as 3 segment schedules in
  the same hour, 27 minutes apart, replacing the single every
  four hours job - segment 1 (production and Arms Race -
  harvest, training, donations, radar, survivors, Arms Race)
  fires at :03, segment 2 (alliance and VIP - mail, help,
  gifts, train, star ceremony, VIP) at :30, segment 3 (missions,
  logistics and claims - secrets, treasures, trucks, Ghost
  Ops, passes, events) at :57, and each segment repeats every
  4 hours, so the whole routine completes inside one hour of
  each cycle. The split was the owner design against the
  device-access error that kept cutting the single long run
  short mid-session - short segment runs finish inside one
  session, and one segment failing loses only that segment.
- The tracker is `_tools_/regulars.py` - `list` shows every regular
  with its status for the day, `todo` shows only what is still due,
  `done <id>` and `skip <id>` record an outcome with a note. State
  is kept per local date in `_tools_/state/`.
- Every run starts from `todo` and ends with `list`, so an expected
  regular is either done, skipped with a reason, or still visibly
  due - never silently dropped. The four-hourly cron instruction
  points at the same list; the list in this folder above is the
  human-readable mirror.

## Standing boundaries for every round

- No purchases, no diamond spending, no PvP, no alliance diplomacy, no
  city moves without the owner approval, per the recording rules.

## Pre-reset zero sweep - first pass, 2026-11-01 1757 (partial)

The first zero sweep ever run, under queue design section 12
and the daily-collection ledger: walk all 23 ledger lines
before the 19:00 reset, enqueue a priority 1 unit of its own
type for every line not at zero, and re-walk the list in the
final sweep at 18:30. This section records the first pass
only; the final sweep is a separate record.

- Unit zero-sweep-pre-reset-sweep-2026-11-01-001 by
  ticker-1738, session cc-72 then cc-75 (the control session
  dropped once and was restarted), window mode 642x951, no
  different-device dialog, session window about 17:46 to
  17:57. Status partial: not all 23 lines were live-read
  inside this unit. Lines rest on a live read in this unit,
  on the day's last live read named per line, or as
  unreadable, and every not-at-zero line names its fix-up
  unit. No other task type was worked inside this unit: no
  bubble collected, no truck dispatched or plundered, no
  donation made, no chest claimed, no secret task tapped.
- Live reads in this unit: base screen about 17:55 showed
  harvest bubbles standing over the central building cluster
  (lines 1-4 not at zero as a group; the per-resource split
  was not read, so no split is claimed per line). Resource
  bar read food 344.7M, iron 532.2M, coin 25.4M. The Events
  icon carried a red x2 badge, so the Events surface is not
  at zero; fix-up events-2026-11-01-1857. The Secret
  Command Post panel, reached by a wrong-entry tap on the
  left rail, read Secret Mobile Squad Assist Allies 2/3,
  Plunder Others 0/3, with UR and SSR tasks standing; no
  task was tapped; fix-up secrets-2026-11-01-1857. The duel
  total line was read in this pass's star-ceremony unit,
  not in the sweep unit itself (League S38 calculating,
  Weekly Ranking Bears Lair rank 190 with 17,240,439
  weekly points, personal daily total unverified);
  re-read fix-up star-ceremony-2026-11-01-1830.
- Count: 23 lines walked - 11 not at zero, 6 unreadable,
  the rest at zero per a last live read or re-check. The
  sweep itself enqueued two fix-ups: vip-2026-11-02-0151
  (priority 1, expires at the 19:00 reset) and
  daily-missions-2026-11-02-0151 (priority 1, expires at
  the 19:00 reset). All other not-at-zero lines already had
  an eligible unit in inbox, so no duplicate was enqueued;
  those units are named per line in the sweep record.
- Gaps the sweep discovered, not new Issues (fix-ups are in
  flight and the final sweep re-walks the list; the retro
  judges any recurrence): VIP lines 12-13 never attempted
  that trade day (no vip entry in the state file, no
  pre-reset vip unit existed); daily activity chests line
  14 at 150 with chests 160 and 200 still ahead and no
  pre-reset missions unit existed; donations line 17 still
  unverified (11:32 tracker note 9 coin donations, 16:06
  unit Donation Count 1 of 30 before donating, final count
  hidden behind the cooldown timer - no closing count,
  consistent with the donations profile); trucks line 18
  shortfall dispatch 1 and plunder 3 from the 1352 close
  (4 of 5, 1 of 4); crystal line 22 age 7 days from
  2026-10-25 and Glittering Market line 23 age 1 day from
  2026-10-31, both with standing priority 1 units already
  in inbox (see Issue #128, not re-filed).
- Open blocker for the next unit: the Secret Command Post
  back arrow resisted three background-click variants (two
  at norm 42,940, one at the re-measured button centre
  66,957); the panel was left open at sweep close. The next
  unit must exit this panel with a fresh method (foreground
  click or another route) before reaching the base screen.
  The panel back control was the only control in this pass
  that resisted background clicks; back arrows from Mail
  and Duel League worked normally earlier in the pass.

## Pre-reset zero sweep - final pass, 2026-11-01 1849 (partial)

Second and final walk of the ledger before the 19:00 reset,
verification-only: no bubble collected, no truck dispatched
or plundered, no donation made, no chest claimed, no secret
task tapped, no pass button tapped inside this unit. Pass
claims cited below were read in this pass's passes unit
(1843 record), not in this unit.

- Unit zero-sweep-pre-reset-sweep-2026-11-01-002 by
  ticker-1834, session cc-78, window mode 642x951, no
  different-device dialog, session window about 18:43 to
  18:49, immediately before the reset.
- Live reads: base screen about 18:47 showed harvest
  bubbles still standing over the central building cluster,
  as in the first sweep's 17:55 view. Resource bar read
  food 344.7M, iron 532.2M, coin 25.4M, unchanged from
  17:55 - nothing was collected between the two sweeps.
  Badges about 18:47: Events icon red x2, Mail icon red
  dot, Season icon red x1, and an "Alliance Gift (SSR)
  received!" banner on the base screen.
- Count: 15 of 23 lines not at zero at 18:47. Gifts line 16
  reversed against the first sweep: the SSR gift banner
  means gifts are not at zero, against the first sweep's
  at-zero read from 17:19; gifts-2026-11-01-1830 was still
  in inbox. Train line 19 stayed at zero per the last
  live read cited as 13:23 (the 1813 banner-only check at
  18:13 also found no train); the sweep did not re-read
  the line, and train-2026-11-01-1830 was still in inbox.
  Duel line 21 stayed unverified with no duel panel read
  in this unit; star-ceremony-2026-11-01-1830 was still in
  inbox. Drone components line 7 stayed unreadable as a
  zero line (the passes unit claimed Drone Parts 20 in
  the free pack, but no drone-component zero read was
  taken). Shop line 10 and pass line 11 were not at zero
  on the passes unit's outcome (Hot Deals free pack and
  Free Supply claimed, but the Weekly Pass page still
  carried its badge and the Coin pickup below was
  unclaimed).
- The risk this sweep surfaces is different from the first
  sweep's: no duplicates were enqueued, because every
  not-at-zero line already had a pre-reset unit in inbox
  - but those fix-up units were still unrun at 18:43,
  about 17 minutes before the reset, so several lines
  were likely to expire unclaimed at 19:00. That is a
  scheduling shortfall, not a sweep finding to fix by
  duplication. The 18:30-slot fix-ups (gifts, help, mail,
  star-ceremony, train) and the 18:03/18:57 units
  (donations, harvest, secrets, events, radar, trucks)
  plus vip-2026-11-02-0151 and
  daily-missions-2026-11-02-0151 were all still in inbox
  at sweep time.
- Truck counter, second read: the truck screen about
  18:35 read "Today's Trade Count: 0/5", recorded as read
  and not reconciled against the 13:52 read of 4/5 and 1/4
  plunder. See truck-plunder 1.12.0 for the standing
  tension and the re-read rule.
- Blocker carried forward: the Coin Weekly Pass Claim
  button unresponsive in the passes unit (see
  shop-claims 1.6.0); if the next passes unit hits the
  same blocker, it is the third consecutive unit with it
  and must change the entry route and write the change
  into the shop-claims metadata (R2).

## Trade-day close - 2026-11-01 19:00 reset (reap confirmed)

- The ticker-1904 sync reap expired 7 units at the reset:
  daily-missions-2026-11-02-0151 and vip-2026-11-02-0151
  (the sweep's own fix-ups, attempts 0),
  donations-2026-11-02-0019, and
  events/secrets/treasures/trucks-2026-11-01-1457 (regular
  units unrun). The reap is recorded in the queue done
  pool, not as execution records, and no unit in the list
  was attempted.
- This confirms the final sweep's scheduling-shortfall
  assessment: the detector worked (VIP lines 12-13 and the
  missions 160/200 gap were found and fix-ups enqueued)
  but the schedule did not run them before the reset, so
  both lines expired unclaimed. See vip-rewards 1.6.0 and
  daily-missions 1.2.0 for the confirmed outcomes; the
  recurrence belongs in the daily retro.
- First new-day execution: radar-2026-11-01-1803 by
  ticker-1904 (19:05 to 19:35, partial, duel day 1 release;
  see radar-tasks 1.9.0). The 1457 expiries do not change
  the standing truck counter tension (truck-plunder
  1.12.0) or the secrets denominator note (secret-missions
  1.4.0); both still await their next live unit reads.

## Pre-reset zero sweep - first pass, 2026-11-07 1824 (partial)

- Unit zero-sweep-2026-11-07-1730 by ticker-1734, session window about 18:06 to 18:24 local. Computer session cc-29 (cc-28, opened for the VIP unit of this same pass, had closed during the gap between units; cc-29 reopened for this unit). Status partial, following the 2026-11-01 and 2026-11-02 first-sweep precedent: not all 23 ledger lines were live-read inside this unit. Lines rest either on a live read in this unit, on the day's last live read named below, or as unreadable, and every not-at-zero line names its fix-up unit. The final sweep at 18:30 re-walks the list. No other task type was worked inside this unit.
- Day context: the Mac mini was offline about 50 hours until about 10:20 today (Issue 284), and the screen-capture channel then failed on every unit through 14:03 (Issue 282, window off-Space). The first successful game reads today were the 16:56 pass (harvest, survivors, training) and the 17:27 pass (help, gifts, VIP, mail). Several ledger lines therefore have no live read at all today.
- Live reads in this unit: base screen at about 18:20 showed food, iron, coin and EXP bubbles standing across the farmland and building clusters (lines 1-4 not at zero as a group; the per-resource split was not read, so the split is not claimed per line). HUD read food 476.8M, iron 800.4M, coin 5.7M, power 149,850,353. A white "?" bubble stands near the front gate. Events carries a red badge 1; Mail, Alliance and the truck icon carry red dots; VS reads "Calculating". Stamina 86, hammers 2 of 4, flasks 2 of 2.
- Count: 23 lines walked - 1 at zero (VIP login chest, claimed live in this pass's VIP unit for plus 60 points), the rest not at zero or unreadable. The sweep itself enqueued two fix-ups: crystal-shop-2026-11-08-0208 (line 22, Crystal not located, age 13 days from 2026-10-25) and glittering-market-2026-11-08-0208 (line 23, Glittering Market not located, age 7 days from 2026-10-31), both priority 1, expiring at the 19:00 reset. All other not-at-zero lines already had an eligible unit in inbox, so no duplicate was enqueued; those units are named per line in the sweep record.
- Gaps the sweep surfaces: donations line 17 and trucks line 18 both still unverified with no live count read today (donations: 0203 and 0603 Mac offline, 1003 capture failed, 1403 navigation detour, count never read; trucks: 0257, 0657 and 1057 all expired unexecuted) - and both rule R3 checkpoints (six-hour and two-hour) passed with the counts still unverified; duel line 21 unverified with no duel total read today and duel-score at 0 done units ever; passes, events, radar, secrets and treasures lines unreadable today after the morning outage.
- Note for the next ticks: the 17:30 sweep pair of 2026-11-03 through 2026-11-06 all expired unexecuted, and this is the first 17:30 sweep to run since 2026-11-02 - the fix-ups above and the inbox units named per line must be picked up by the 18:34 tick or the 18:30 final sweep, or they meet the same fate at the reset.

## Pre-reset zero sweep - first pass, 2026-11-08 1712 (partial)

- Unit zero-sweep-2026-11-08-1630 by ticker-1646, session cc-142,
  window mode 642x951 after a relaunch. Status partial,
  verification-only: no bubble was collected, no truck dispatched
  or plundered, no donation made, no chest claimed, no secret task
  tapped, no pass button tapped inside this unit. Evidence in
  `_records_/2026-11-08/daily-activities/1712-queue-run.md` (commit
  9978e09a8 on records/2026-11-08). Line statuses below cite the
  live base read of this unit plus the same-day execution records
  named per line.
- Live reads in this unit: base screen about 17:12 local, after a
  server disconnect and relaunch (see below): power reads
  149,209,253 as displayed, against 149,850,353 at the 16:58 and
  16:12 reads - a 641,100 step down with no fight, dispatch or
  claim in between in this pass. Recorded as displayed, cause
  unexplained, not asserted as a loss; the next unit that reads
  power should confirm whether the figure holds. Food 490.8M,
  iron 813.3M, coin 12.3M; second row 25.0M, 922.2K; diamonds
  13.22K; cart 4,417; stamina 120. Season II 7d 00:50:41. Wanted
  Boss badge 1, timer 00:00:57 (was 00:00:32 at 16:58 - a new
  cycle, recorded as displayed). Harvest bubbles still standing
  over the central building cluster at 17:12 - gold, food and
  iron bubbles with values in the hundreds of K. Resource totals
  unchanged from 16:58. Badges about 17:12: Events icon red x2,
  Mail icon red dot, Inventory icon red dot, Alliance icon red
  dot, radio badge 4, white truck red dot 1, survivor portrait
  badge 10, megaphone badge 4. No train icon in the left column;
  no "Boarding closes in" banner under the resource bar - the
  banner area shows the "Upgrade Builder's Hut to Lv.26 [0/1]"
  quest line and a Breaking News line instead. Fourteenth
  same-day no-train confirmation (thirteenth in this pass's scout
  unit).
- Server disconnect, recovery observed live: at about 17:06 the
  game showed "Server disconnected. Please restart the game."
  with a Confirm button. The Confirm tap closed the app (target
  app exited); the app was relaunched with open_app and returned
  to the base screen with state intact - no login demanded, no
  different-device dialog. Same class as the earlier Esc/Return
  crashes: state is server-side. The server-disconnect Confirm
  tap and the app relaunch were recovery only. No diamonds or
  money spent, no paid button tapped, no research or building
  started, no player attacked, no assemble or teleport.
- Count: 23 lines walked - 11 not at zero, 4 at zero, 5
  unreadable, duel unmeasured, crystal and glittering not
  located. Lines not at zero: food, iron, coin and EXP bubbles
  (standing 17:12, fix-up harvest-2026-11-08-1803 already in
  inbox); VIP Daily Freebie (no vip-rewards record exists today
  at all, vip-2026-11-07-1900 stalled in inbox, priority 1,
  about 22 hours old; the 0512 observation read the Freebie
  still claimable at about 05:11; fix-up vip-2026-11-08-1800
  already in inbox); VIP login chest (never attempted today,
  same fix-up); daily activity chests (1628 record, activity 70,
  80-point chest 10 points short, tab badge 1 remaining; fix-up
  daily-missions-2026-11-08-1800 already in inbox); mail, six
  categories (Mail badge red dot at 17:12; last mail unit 1423;
  fix-up mail-2026-11-08-1830 already in inbox); alliance gifts
  (the 1406 unit claimed both tabs in full, but the 1615 scout
  read the Alliance Gifts panel dot again at 16:14, so new gifts
  have arrived since; fix-up gifts-2026-11-08-1830 already in
  inbox); alliance donations (no closing count exists today;
  0937 scout read Donation Count 2/30, and the count replenishes
  during the day; donations-2026-11-08-1803 already in inbox);
  trucks dispatch 5 of 5 and plunder 4 of 4 (no live
  trade-counter read exists today; the 0415 "Plunder Others 0/5"
  note is not a trade-counter close; trucks-2026-11-08-1857
  already in inbox). Lines at zero: shop Daily Pickup and Free
  Supply, and pass daily pickups (both per the 1455 passes unit
  read); alliance train per service (no train in preparation,
  fourteenth same-day confirmation; train-2026-11-08-1830 still
  in inbox for the evening check); radar by duel posture (stack
  posture per the 1355 record, stack locked until the release
  day; a stack posture is not a miss; radar-2026-11-08-1803
  already in inbox). Lines unreadable: titanium bubbles (no
  full-base pan in this unit), armed truck (no fully-loaded
  notice or timer read), drone components (no drone-component
  zero read taken; fix-up passes-2026-11-08-1857 already in
  inbox), upgrade ore and screws (no reward popup transcribed;
  no dedicated fix-up type). Duel line 21 unverified (1441
  record: total unmeasured, verified no for that line; fix-ups
  duel-score-2026-11-08-1830 and star-ceremony-2026-11-08-1830
  already in inbox). Crystal line 22 not located, age 14 days
  from 2026-10-25; Glittering Market line 23 not located, age 8
  days from 2026-10-31 (rule R5 owner-named items, no standing
  unit in inbox, no duplicate enqueued by this sweep).
- Fix-up units enqueued by this sweep: none. Every not-at-zero
  line already had a fix-up unit in inbox at sweep time, so
  enqueuing more would have duplicated units. The risk this
  sweep surfaces is the same as the 2026-11-01 final sweep:
  those fix-up units were still unrun at about 17:10, about 50
  minutes before the 18:00 reset, so several lines are likely to
  expire unclaimed at the reset. That is a scheduling shortfall,
  not a sweep finding to fix by duplication. The second sweep,
  zero-sweep-2026-11-08-1730, is still in inbox and repeats this
  walk before the reset.
- Gaps the sweep surfaces: the VIP lines 12-13 were never
  attempted this trade day (no vip-rewards record today, the
  1900 unit stalled about 22 hours); the donations line 17 and
  trucks line 18 both still unverified with no live count read
  today; the duel line 21 still unmeasured. None is filed as a
  new Issue here - the fix-ups are in flight and the second
  sweep re-walks the list; the retro judges any recurrence.

## Pre-reset zero sweep - second pass, 2026-11-08 1740 (partial)

- Unit zero-sweep-2026-11-08-1730 by ticker-1724, session cc-143,
  window about 17:39 to 17:40 local. Status partial,
  verification-only: no bubble was collected, no truck dispatched
  or plundered, no donation made, no chest claimed, no secret task
  tapped, no pass button tapped inside this unit. Evidence in
  `_records_/2026-11-08/daily-activities/1740-queue-run.md` (commit
  5f3a904f4 on records/2026-11-08). It re-walks the 23 ledger lines
  after the 1712 first pass.
- Live reads in this unit: base screen about 17:40 local, power
  reads 149,209,253 as displayed, unchanged from the 17:12 read -
  the 641,100 step down from 149,850,353 at 16:58 holds, cause
  still unexplained, not asserted as a loss. Food 490.8M, iron
  813.3M, coin 12.3M; second row 25.0M, 922.2K; diamonds 13.22K;
  cart 4,417; stamina 120. Season II 7d 00:22:45. Wanted Boss
  badge 1, timer 00:00:51. Harvest bubbles still standing over
  the central building cluster at 17:40 - food, iron and coin
  bubbles with values in the hundreds of K. Resource totals
  unchanged from 17:12. Badges about 17:40: Events icon red x2,
  Mail icon red dot, Inventory icon red dot, Alliance icon red
  dot, radio badge 4, white truck red dot 1, survivor portrait
  badge 10, megaphone badge 4, hammer 2/4, flask 2/2. No train
  icon in the left column; no "Boarding closes in" banner under
  the resource bar - the banner area shows the "Upgrade Builder's
  Hut to Lv.26 [0/1]" quest line and a Breaking News line instead.
  Fifteenth same-day no-train confirmation (fourteenth in the 1712
  first pass). A toast is partly visible at the bottom-left edge,
  cut off by the screen edge ("...ies ... loaded,") - not
  transcribed, not asserted as the armed-truck fully-loaded
  notice. Line 6 stays unreadable on this unit's evidence.
- Count: 23 lines walked - no line moved to zero since 1712, no
  fix-up unit executed in between. At zero: 3 lines (10, 11 per
  the 1455 passes unit read; 19 live, train per live read,
  fifteenth same-day confirmation). Stack posture, not a miss: 1
  line (20, radar per the 1355 record). Not at zero: 12 lines
  (1, 2, 3, 4, 12, 13, 14, 15, 16, 17, 18, 21). Unreadable: 5
  lines (5, 6, 7, 8, 9). Named status, not located: 2 lines (22,
  23, crystal age 14 days, glittering age 8 days). The 12
  not-at-zero lines will expire unclaimed at 18:00 unless a
  currently claimable unit (the overdue 1403-slot units) is run
  in the remaining minutes.
- Fix-up units enqueued by this sweep: none. Every not-at-zero
  line already had a fix-up unit in inbox at sweep time, so
  enqueuing more would have duplicated units. The standing risk
  is unchanged from the first pass and is now confirmed a second
  time: all of those fix-ups carry not_before at or after the
  18:00 reset, so they cannot run before it. The overdue
  1403-slot units (harvest, donations, arms-race, radar;
  not_before 14:03, expires 18:03) are the only units that can
  still run inside the old reset day. That is the scheduling
  shortfall the first sweep flagged, confirmed a second time.
- Gaps the sweep surfaces: the VIP lines 12-13 were never
  attempted this trade day (no vip-rewards record exists today
  at all, vip-2026-11-07-1900 stalled in inbox, priority 1,
  about 23 hours old; the 0512 observation read the Freebie
  still claimable at about 05:11); the donations line 17 and
  trucks line 18 both still unverified with no live count read
  today; the duel line 21 still unmeasured. None is filed as a
  new Issue here - the fix-ups are in flight and the next tick
  re-walks the list in the new reset day; the retro judges any
  recurrence.

## Pre-reset zero sweep - first pass, 2026-11-09 1657 (partial)

- Unit zero-sweep-2026-11-09-1630 by ticker-1635, session about 16:47 to 16:57 local. Status partial, verification-only: nothing claimed, no truck dispatched or plundered, no donation made, no chest claimed, no secret task tapped, no pass button tapped inside this unit. Evidence in `_records_/2026-11-09/daily-activities/1657-queue-run.md` (commit c9a86fa74 on records/2026-11-09). Sweep pair 001 of 2; unit 002 at 17:30 finishes the walk. Target: 23 ledger lines; 7 read live in this unit.
- Live reads, not at zero: food bubbles (line 1) - many wheat bubbles stand over the farmland, regrown since the 12:20 harvest; iron bubbles (line 2) - several blue iron bubbles stand over the mines; coin bubbles (line 3) - several gold coin bubbles stand on the base; alliance donations (line 17) - Tech Donation Today 3,300 live (was 2,250 at the 14:13 donations unit, which had left Donation Count 19/30 remaining with the button still green; no donations unit has run since - the +1,050 rise is unexplained, other members' donations the likely source, unverified); survivors (gate line) - two survivors with question-mark bubbles stand at the front gate, left edge; mail (line 15) - Mail carries a red dot, Battle Report, System and Regular categories still unopened today (Event and Alliance answered "No rewards available." at 10:31); alliance red dots - Help, Alliance Gifts, Alliance Techs and Alliance Events all carry red dots.
- Lines verified at zero by earlier units today (not re-read live): VIP Daily Freebie and login chest claimed 15:39-15:43 (vip unit, done); daily activity chests 40/80/120 claimed 15:19-15:38 (daily-missions unit, done); Secret Command Post checked 14:51, nothing to deploy (secrets unit, done). These stand on their own units' live reads, not on this sweep's.
- Lines not walked this unit (for sweep 002 at 17:30): EXP bubbles, titanium bubbles, Armed Truck loot, trucks dispatch 5/plunder 4 counters, train station, Arms Race phase, daily missions 160/200 chests, radar map pins, Alliance Duel daily total vs 3.6M, Events hub tabs, Crystal, Glittering Market.
- Base HUD at entry: food 556.6M, iron 881.6M, coin 53.6M, diamonds 6,137, power 149,217,331, stamina 87 rising to 88 by close, VIP points 13.22K. VS timer 01:15:42; Events countdown 6d 01:15:42. Build: Oil Well [0/1]; building queue 1/4; research 1/2.
- Skull timer, Issue #498: a red skull icon with badge 4 and a 00:00:37 countdown stood at the right edge of the base screen at 16:56 - unidentified, recorded unverified, no tap made. Badge 4 is new in the sequence.
- Sweep actions taken: six inbox units for lines verified non-zero were raised to priority 1 (their (regular, planned_for) pairs already existed, so no duplicates were enqueued): harvest-2026-11-09-1803, donations-2026-11-09-1403, survivors-2026-11-09-1403, help-2026-11-09-1430, gifts-2026-11-09-1430, mail-2026-11-09-1430. Pool validated after the edits.
- Count: 7 of 23 lines read live this unit; 6 non-zero per the unit stats. The record lists food, iron, coin, donations, survivors, mail and the alliance red-dot roll-up as the seven reads; which one counted as the zero line is not named in the record, so none is claimed zero here. The remaining-count read for donations was blocked: the 2/10 Quick Gathering card is cut off at the bottom of the Techs panel.
- No diamonds or money spent. No speedup or stamina item used. Tracker untouched (partial unit). Blocker category: h (by-design partial - sweep 002 at 17:30 completes the walk). Zombie Invasion: tab still absent from the Events hub as of the 11:52 record today; no chain seeded, per the standing rule.

## Pre-reset zero sweep - second pass, 2026-11-09 1748 (partial)

- Unit zero-sweep-2026-11-09-1730 by ticker-1734, session about 17:38 to 17:48 local. Status partial, verification-only: nothing claimed, no truck dispatched or plundered, no donation made, no chest claimed, no secret task tapped, no pass button tapped inside this unit. Evidence in `_records_/2026-11-09/daily-activities/1748-queue-run.md` (commit 2f4d783d8 on records/2026-11-09). Sweep pair 002 of 2; sweep 001 (16:35) read 7 lines; together the pair read 12 of 23. Target: 23 ledger lines; 5 read live in this unit, 4 of them non-zero.
- Live reads, not at zero: food bubbles (line 1) - many wheat bubbles stand over the farmland, same as at 16:35; iron bubbles (line 2) - several blue iron bubbles stand over the mines; coin bubbles (line 3) - several gold coin bubbles stand on the base; trucks (line 18) - dispatch 4/5, plunder 1/4 read live on the trade screen, shortfall dispatch -1, plunder -3 with the trade day ending at the 19:00 reset; fix-up trucks-2026-11-09-1457 raised to priority 1 (expires 18:57).
- Lines read live, at zero or absent: Events hub tabs - Winter Battlefield, Desert Storm Battlefield (selected), Wanted Boss; no Zombie Invasion tab; no Crystal or Glittering Market tab in the visible row (row may scroll, absence not confirmed). Desert Storm Battlefield: registration ends in 2d 00:14:37, Battle Day 2026-11-13, 03:00-03:30, Participants 20/20, Task Force A (You) vs Task Force B; handed to the events-2026-11-09-1857 unit, no tap made here.
- Lines not read live this unit (handed to queued units): EXP bubbles, titanium bubbles, Armed Truck loot - harvest-2026-11-09-1803 (already priority 1); the 3.9K labelled icons visible over the base look like EXP bubbles but the type was not individually confirmed - unverified. Train station - train-2026-11-09-1430 (due now, expires 18:30) and train-2026-11-09-1830. Arms Race phase - arms-race-2026-11-09-1803. Daily missions 160/200 chests - daily-missions-2026-11-09-1800. Radar map pins - radar-2026-11-09-1803. Alliance Duel daily total vs 3.6M - duel-score-2026-11-09-1830. Crystal (R5, age 15 days from 2026-10-25) and Glittering Market (R5, age 9 days from 2026-10-31) - still not located by any evidence today; no new surface found in this sweep.
- Base HUD at entry: food 556.6M, iron 881.6M, coin 53.6M, diamonds 6,137, VIP 13.22K, power 148,140,193, stamina 99, VS timer 00:20:00, Events countdown 6d 00:20:01. Build: Oil Well [0/1]; building queue 1/4; research 1/2. At close: power 147,469,864, stamina 100, VS 00:15:25, Events 6d 00:15:25.
- Power falling, cause unverified: Total Power read 149,217,331 at 16:35, 148,140,193 at about 17:40 and 147,469,864 at about 17:45 - down about 1.75M in 70 minutes while no battle unit ran (radar 17:07-17:17 and survivors 17:19-17:29 were both partial, no fights). The radar unit read 146,730,949 at about 17:53, so the fall continues to about 2.49M in about 78 minutes. The system feed shows truncated "Mutant Raider has been..." messages. Whether mutant raids drain power is unverified; flagged for the daily retro, no new issue filed on a single observation - the datapoint is commented onto the matching open issue #482 by this run. This is the second day running with an unexplained step-down (641,100 on 2026-11-08, Issue #482).
- Secret Command Post, incidental read: a tap on the left icon column opened the Secret Command Post instead of trade (the two shortcut sets share the slot, per the truck-plunder metadata). Secret Mobile Squad reads Assist Allies 5/5, Plunder Others 0/3, with four SSR task cards all marked PERFECT. Handed to secrets-2026-11-09-1803; nothing tapped further there.
- Entry route learned: in the current icon set the blue truck-front icon at norm y about 573 opens Intercity Trade directly; the jeep below it is the Secret Command Post.
- Skull timer, Issue #498: a red skull icon with badge 1 and a seconds countdown (00:00:09 falling to 00:00:04) and a target icon with badge 1 (00:00:25) stand at the right edge of the base screen - unidentified, recorded unverified, no tap made (same item as sweep 001, which read badge 4 with 00:00:37 at 16:56). Commented on Issue #498 by this run.
- Donations line (line 17) was not re-read this unit: sweep 001 found Donation Count 19/30 remaining at 14:13; donations units donations-2026-11-09-1403 (priority 1) and donations-2026-11-09-1803 cover it.
- Sweep actions taken: one inbox unit raised to priority 1 for a line verified non-zero: trucks-2026-11-09-1457. Pool validated after the edit. No new units enqueued - every unread line already has a queued unit for the 18:00-18:57 slots.
- Count: 5 of 23 lines read live this unit, 4 non-zero; the pair read 12 of 23. The remaining 11 lines are covered by the 18:00-18:57 batch.
- No diamonds or money spent. No speedup or stamina item used. Tracker untouched (partial unit). Blocker category: h (by-design partial - the pair's walk ends here; the 18:00-18:57 batch verifies the remaining lines). Zombie Invasion: tab still absent from the Events hub; no chain seeded, per the standing rule.

## Ended trade day close, 2026-11-09 19:00 - fuller consolidation sweep (this run)

- This run is the first organizer pass after the 19:00 local reset, so it does the fuller consolidation sweep of the ended trade day (2026-11-08 19:00 to 2026-11-09 19:00) in addition to the incremental fold. Sweep verification: the watermark chain is continuous across the day's 19 organizer runs (1432 worked from 1332, 1532 from 1432, 1632 from 1532, 1732 from 1632, 1832 from 1732), and the only substantive commit after the 1832 watermark (2f4d783d8) is the ticker-1822 pass (6761c35d1), folded here. No ended-trade-day record is left unfolded. The pr-integration 1915 pass merged records PR #531 at the 19:00 batch after re-verifying the Issue #544 repair by merged-tree file counts, so the day's records are complete in main.
- Last pass of the day, ticker-1822 (18:22-18:51): mail-1430 done (9 mails), gifts-1430 done (1699 Regular + 95 Premium), help-1430 done (2 ally requests), passes-1457 partial (free pack, Free Supply, monthly Daily Pickup; Weekly Pass scroll not done). The 14:03 arms-race, donations and training units all expired unrun - window passed before execution, reaped 18:27:54 in the same pass.
- Final counters at the reset: trucks 4/5 dispatch, 1/4 plunder (1748 read, unchanged since 02:50) - shortfall dispatch -1, plunder -3; the fix-up trucks-1457 (priority 1, expiry 18:57) has no execution record on the branch and closes unrun. Donations 19/30 remaining at the 1413 close, no later donations unit - 11 of the day's 30 allowance unspent. Arms Race Hero Advancement phase unworked (1403 expired); cumulative chest 7/8 unclaimed at the 1500 read. Training 1403 expired.
- Power at the close: Total Power 146,736,949 at 18:33 (mail entry read), 6,000 above the 146,730,949 at about 17:53 - the day's fall levelled at the close (Issue #482 datapoint, commented by this run). Gift Level 28 progress 198,624,140 / 206,300,000 at the 1842 close. Alliance leader changed during the day: Abyss Apex (was Jerry Apex at the 0417 read).
- Still open at the reset, carried to the next trade day: the Weekly Pass scroll (next passes unit resumes with it); the check-in FREE GIFT foreground-click idea (1449 follow-up, still unattempted); the 0335 Rare Iron Mine gathering pin claim (unchecked after two radar units); the radar map pins (unclosed, handed to radar-1803); Quick Dispatch for the 0926 newcomer (survivors); the Season Battle Pass path in the Week 8 hub (Issue #469); the duel-score closing total for the ended day. No execution record for the 18:00-18:57 batch units (radar-1803, train-1830, daily-missions-1800, duel-score-1830, events-1857, secrets-1803, harvest-1803) has landed on the records branch at run close; their outcomes are not recorded here.
- Next trade day: the planner 1840 staged 12 units (06:03-06:30 slots 2026-11-10: mail, help, gifts, harvest, radar, survivors, train, training, donations, arms-race, star-ceremony, duel-score).
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Pre-reset zero sweep - first pass, 2026-11-10 1634 (partial)

- Unit zero-sweep-2026-11-10-1630 by ticker-1634, session about 16:38 to 16:42 local. Computer session cc-482, windowed 642x951 play throughout. Status partial: sweep 001 of 2 read the base HUD and the Secret Command Post live; the remaining ledger lines were not walked in this unit and pass to the staged 17:30 sweep (zero-sweep-2026-11-10-1730, same chain, seq 2, not_before 17:30, expires at the 19:00 reset). Evidence in `_records_/2026-11-10/daily-activities/1634-queue-run.md` (commit 986c1877 on records/2026-11-10). No device dialog, no login demand, no Touch ID, no password typed.
- Live reads, base screen about 16:45: power 148,787,578; food 631.3M; iron 954.1M; coin 97.8M; diamonds 6,267 (red gem, top right); stamina 120; level 30. A gold 13.22K counter with a blue plus button sits beside the avatar; its meaning was not asserted in this unit. VS timer 01:20:54; Season II 3d 01:30:54; third timer 5d 01:20:54 beside the radar-side icon (meaning unverified, same as the 06:14 and 15:12 reads). Left column: hammer 1/4 (red dot), flask 1/2 (red dot), truck icon with a question marker, radio/broadcast icon badge 11, hero portrait, gift chest. Right column: Events badge 2, VS, Season II, radar-side icon, skull badge 1 with a 00:00:27 countdown, Alliance (red dot), Mail (red dot), Inventory (red dot). Task: "Build: Oil Well [0/1]". Chat ticker: "Breaking News: Alliance War!", 99+ unread.
- CORRECTION - diamonds: the 1555 radar fold's base-screen display read "diamonds 13.22K" is superseded - the 13.22K figure is the separate gold counter beside the avatar, meaning unasserted; diamonds read 6,267 live here and in the 1649 training unit. The radar-tasks profile carries the same correction.
- Ledger lines, this unit: line 3 coin bubbles read live, NOT at zero - one gold coin bubble standing over the purple crystal-like building near the top of the base. Fix-up: the staged harvest unit harvest-2026-11-10-1803 owns collection; no new unit enqueued. Lines 1, 2, 4, 5 food, iron, EXP, titanium bubbles: not individually verified in this unit (panned/fogged base view). The 15:31 harvest unit read all three panel pools Available 0, but per rule R1 that read does not close these lines for this sweep; the 17:30 sweep re-reads them. Line 6 Armed Truck: not read in this unit; still unlocated (Issue #566, 5th deferral at 15:31). Lines 7 to 23 (drone components, ore, screws, shop pickup, pass pickups, VIP freebie and login chest, mission chests, mail, gifts, donations, trucks, train, radar, duel total, crystal, glittering market): not walked in this unit. Prior same-day live reads stand as context only, not as sweep closes: VIP freebie and login chest both claimed 14:38; donations closed 0/30 at 02:53 with the count refilling in bursts; trucks Trade Count 4/5 and Plunder 2/4 at 14:11; missions activity 120, 160/200 unreached at 14:26; duel total 1,650,000 of 3,600,000 at 13:33. The 17:30 sweep re-reads each line live.
- Secret Command Post, about 16:49: entered by tapping the left-column truck icon at its fresh measured centre (norm 44,641). Assist Allies 5/5 at cap; Plunder Others 0/3. Your Tasks, 4 of 8 visible: UR Rescue Test Subject Lv.5 PERFECT, UR Disrupt electric grid Lv.5 PERFECT, SSR Provide Tech Support to Refugees Lv.5 carrying the orange hexagon badge with no PERFECT stamp visible, SSR Protect Refugee Camp Lv.5 PERFECT. No Claim button anywhere on the visible cards. Folded in secret-missions; the staged secrets-2026-11-10-1830 unit re-verifies the full list.
- Zombie Invasion: the Events hub was not opened in this unit, so no fresh Zombie-tab read was taken. The 06:14 scout and 05:19 events reads found no Zombie tab; the event is still ended and no chain was seeded, per the standing rule.
- Fix-ups enqueued: none. The two non-zero observations already have staged units of their own type: harvest-2026-11-10-1803 for the coin bubble, secrets-2026-11-10-1830 for the Command Post re-check. Enqueuing duplicates would violate the (regular, planned_for) invariant. The 17:30 sweep unit is already staged in the same chain.
- Red lines: no diamonds or money spent, no price tag or paid button tapped, no Delete All, no assembly or teleport. Mega Refresh and Mega Deploy untouched. Nothing claimed: the sweep reads only.
- Result stats: target 23 ledger lines read live; achieved 1 line read live (coin bubbles, not at zero); resources_gained none; points 0; costs about 7 minutes, no items spent; verified yes (the HUD, bubble and Command Post figures reported here are same-unit live reads; unwalked lines are reported as unwalked, not as closed); blocker_category h (by-design partial - the sweep is split across the 16:30 and 17:30 chain pair by design).

## Pre-reset zero sweep - first pass, 2026-11-11 1726 (partial)

- Unit zero-sweep-2026-11-11-1630 by ticker-1718, session about 17:18 to 17:27 local. Status partial, verification-only: nothing claimed, no truck dispatched or plundered, no donation made, no chest claimed, no secret task tapped, no pass button tapped inside this unit. Evidence in `_records_/2026-11-11/daily-activities/1726-queue-run.md` (commit bec20570e on records/2026-11-11). Sweep pair 001 of 2; unit 002 at 17:30 finishes the walk. Target: 23 ledger lines; 1 read live to a close in this unit. Computer session cc-644, windowed 642x951 play throughout. No device dialog, no login demand, no Touch ID, no password typed.
- Live reads, base screen about 17:20: power 149,218,973; food 689.4M; iron 1.0G; coin 136.7M; diamonds 13.22K; level 30; VIP 75. Stamina not re-read in this unit (69 at 16:50 per the scout, 67 at 16:40 per the daily-missions unit - context only). VS timer 00:39:26 at 17:20, 00:33:16 at 17:27; Season II 2d 00:45:47; radar-side timer 4d 00:35:47. Task: "Build: Oil Well [0/1]". Chat ticker 99+ unread. Red dots on the base screen: Events badge 2, VS, Alliance, Mail, Inventory, HEROES, left-column mail icon badge 1, skull icon badge 1 with a roughly 60 second cycle timer (00:00:49, then 00:00:21) - the skull timer remains unexplained, carried from the 2026-11-09 and 2026-11-10 observations. A building near the centre carries a "10" beneath it and a red up-arrow rally marker above it (meanings unverified, same as the 16:48 scout read).
- Trade Trucks panel, about 17:24: entered by tapping the left-column top icon. The first two taps missed: they used raw pixel coordinates, but this control channel takes coordinates normalized 0 to 1000 within the window. Re-grounded from the fresh screenshot and retried at normalized 44,576 - the panel opened. The tap also needs a fresh observation_id; a stale one is refused before any input is sent. "Today's Trade Count: 1/5". One truck out (yellow truck with a blue gift-box marker above it - marker meaning unverified); three empty slots with green plus signs; "Mega Mode" button; "Filter out trucks from your Warzone" checked; History top-right. "Others' Trucks" tab: "Your Plunder Count Today: 0/4". Many plunderable trucks visible, including [oawc]Licca B and [TTAL]Portgas D Ace S. The tab badge 4 and the "Recover" red dot were not opened in this unit.
- Alliance Techs, about 17:25: "Tech Donation Today: 4050" points; the reward threshold of 1000 contribution points is met. This screen shows points, not the Donation Count (remaining count) the ledger line closes on, so the count itself was not read in this unit and stays unverified. Five donations units ran today (0107, 0148, 0434, 0541, 0733) - context only.
- Ledger lines, this unit: line 18 trucks read live, NOT at zero - dispatch 1/5, plunder 0/4, with about 95 minutes to the 19:00 reset. This is a rule R3 checkpoint shortfall (the two-hour checkpoint at 17:00 already stood at 1/5 and 0/4, per the 16:52 scout read). Fix-up: the next trucks unit trucks-2026-11-11-1457 was raised to priority 1 in this pass; it is actionable now and the loop picks it up next. Line 17 donations partially read - points 4050 live, remaining count unread. The 17:30 sweep re-reads the count; four donations units stand in inbox (1403, 1803, 2203, 0203). Lines 1 to 16 and 19 to 23 (bubbles, Armed Truck, drone components, ore, screws, shop and pass pickups, VIP freebie and login chest, mission chests, mail, gifts, train, radar, duel total, crystal, glittering market): not walked in this unit. Prior same-day live reads stand as context only, not as sweep closes: daily missions 1638 found tasks incomplete (Defeat any Doom Elite 0/1, Recruit Heroes 0/1, Attack a Commander 0/1, Gather Food 0/10000); mail last ran 1422; the 16:48 scout read the base HUD and the Hero List (9 hero cards with red dots). The 17:30 sweep re-reads each line live. Zombie Invasion: the Events hub was not opened in this unit, so no fresh Zombie-tab read was taken. The event returned 2026-11-10 and runs to about 2026-11-13; one zombie-invasion unit stands in inbox and the chain is live, so no sweep action is owed here.
- Skull timer, Issue #498: sixth sighting - badge 1, countdown 00:00:49 falling to 00:00:21, the roughly 60 second cycle holding. Commented on Issue #498 by this run, together with the seventh sighting from the 1730 sweep.
- Fix-ups enqueued: none as new units. The trucks shortfall is covered by raising the already-staged trucks-2026-11-11-1457 to priority 1 (same regular, same planned slot - no duplicate unit created). The 17:30 sweep unit is already staged in the same chain.
- Red lines: no diamonds or money spent, no price tag or paid button tapped, no Delete All, no assembly or teleport. Nothing claimed: the sweep reads only.
- Result stats: target 23 ledger lines read live; achieved 1 line read live to a close (trucks, not at zero); resources_gained none; points 0; costs about 9 minutes, no items spent; verified yes (the HUD, truck counters and donation points reported here are same-unit live reads; unwalked lines are reported as unwalked, not as closed); blocker_category h (by-design partial - the sweep is split across the 16:30 and 17:30 chain pair by design).

## Pre-reset zero sweep - second pass, 2026-11-11 1730 (partial)

- Unit zero-sweep-2026-11-11-1730 by ticker-1800, session about 17:57 to 18:15 local. Status partial, verification-only: nothing claimed, no truck dispatched or plundered, no donation made, no chest claimed, no secret task tapped, no pass button tapped inside this unit. Evidence in `_records_/2026-11-11/daily-activities/1730-queue-run.md` (commit 6cbd479fc on records/2026-11-11). Sweep pair 002 of 2; sweep 001 (17:18) read 1 line; together the pair read 6 of 23. Target: 23 ledger lines; 5 read live in this unit. Computer session cc-650, windowed 642x951 play throughout. No device dialog, no login demand, no Touch ID, no password typed.
- Live reads, base screen about 18:06: power 149,218,973; food 693.3M; iron 1.0G; coin 136.7M; diamonds 13.22K; level 30; VIP 75. Stamina 82. VS timer 00:00:51; Season II 2d 00:10:51; radar-side timer 4d 00:00:51. Task: "Build: Oil Well [0/1]". Chat ticker 99+ unread. Red dots on the base screen: Events badge 2, VS, Alliance, Mail, Inventory, HEROES, left-column mail icon badge 1, skull icon badge 2 with a roughly 60 second cycle timer (00:00:46) - the skull timer remains unexplained, carried from the 2026-11-09 and 2026-11-10 observations. Food, iron and coin bubbles standing across the base (food 9.6K/9.8K, iron 5.6K, coin 1.5K/1.6K/1.8K read on the screenshot); EXP and titanium bubbles not distinguished in this unit. The food 693.3M read confirms the 1740 harvest unit's +3.9M food collection held.
- Mail, about 18:08: seven categories. Claimable gift icons on Alliance and Event. Red dots on System, Regular and In-app Purchases. Battle Report and Favorite show no indicator.
- Events hub, about 18:13: Zombie Invasion - Glacieradon tab active. Timer 1d 23:58:15 left - the event runs to about 2026-11-13 18:00. "Challenge begins in: 23:58:16", "Your Timezone: 2026-11-12 18:00". Progress bar 40/40. Store carries a red dot. "The next wave of Invading Zombies will arrive in 00:52:52." Alliance Finding: Lv.80 Zombie Bosses at 342km, 138km, 294km and Lv.85 at 208km, despawn about 03:23 to 03:29. Tab bar: Glacieradon badge 1, one more tab badge 1 (left edge, partially visible) - the base Events badge 2 is accounted for by these two.
- Ledger lines, this unit: lines 1 to 3 (food, iron, coin bubbles) read live, NOT at zero - bubbles standing. Fix-up: harvest-2026-11-11-1803 raised to priority 1 (was 3, actionable now). Lines 4 to 5 (EXP, titanium bubbles): not distinguished in this unit; covered by the same harvest fix-up. Line 6 (Armed Truck): not read; covered by the harvest fix-up. Lines 7 to 11 (drone components, ore, screws, shop and pass pickups): not walked; owning units (passes, events) stand in inbox. Lines 12 to 13 (VIP freebie, login chest): not read; the VIP unit vip-2026-11-11-1800 is already priority 1 and actionable now. Line 14 (daily mission chests): not walked; the daily-missions unit stands in inbox. Line 15 (mail) read live, NOT at zero - Alliance and Event gifts unclaimed, three red dots. Fix-up: mail-2026-11-11-1830 raised to priority 1 (was 3, not_before 18:30). Line 16 (alliance gifts): not walked; the gifts unit stands in inbox. Line 17 (donations): points 4050 read live by the seq-1 sweep at 17:25; the remaining Donation Count itself was not re-read in this unit. Fix-up: donations-2026-11-11-1803 raised to priority 1 (was 2, actionable now) so the count is read before the reset. Line 18 (trucks): read live by the seq-1 sweep at 17:24 - dispatch 1/5, plunder 0/4, NOT at zero. The fix-up unit trucks-2026-11-11-1457 is already priority 1 and is the next unit this pass. Line 19 (train): not walked; the train unit stands in inbox. Line 20 (radar): not walked; the radar unit stands in inbox. Line 21 (duel total): not walked; the duel-score unit stands in inbox. Lines 22 to 23 (crystal, glittering market): not walked; named status stands from the day records. Zombie Invasion: event live, next wave in about 53 minutes; the zombie-invasion chain unit stands in inbox.
- Skull timer, Issue #498: seventh sighting - badge 2, countdown 00:00:46, the roughly 60 second cycle holding. Commented on Issue #498 by this run, together with the sixth sighting from the 1726 sweep.
- Loop-health gap found in this pass, filed as Issue #661 (tooling class, owned by lastwar-tool-developer, not this job): while resolving the records PR 655 conflict before game work, the merge showed main already carries _queue_/inbox/trucks-2026-11-11-1457.md WITH raw conflict markers in it (HEAD side trucks-2026-11-11-1057 vs 1457) - some earlier pass merged badly and committed the conflicted file to main; main also lacks _queue_/done/trucks-2026-11-11-1057.md, which the records branch restores. The conflict was resolved by merging main into records/2026-11-11 in a VPS worktree, taking the clean branch version of the 1457 unit (priority 1, planned 2026-11-11T22:57:00Z), merge e535c029a, pushed and verified with git ls-remote; the 19:00 batch merge heals main. The gap: a file with conflict markers passed onto main undetected - tools/queue.py validate (Issue #441) exists as a pre-commit / pre-push hook for exactly this class of corruption but evidently did not run (or does not cover this route) when the bad merge landed. The clean 1457 units for events and secrets were restored in the same pass (commit 253b292c3f, Refs #661).
- Sweep actions taken: four already-staged units raised to priority 1 for lines verified non-zero - harvest-2026-11-11-1803, mail-2026-11-11-1830, events-2026-11-11-1857, donations-2026-11-11-1803. Trucks-2026-11-11-1457 was already priority 1 from the seq-1 sweep. Pool validated after the edits. No new units enqueued - every unread line already has a queued unit for the 18:00-18:57 slots.
- Count: 5 of 23 lines read live this unit, all non-zero; the pair read 6 of 23. The remaining 17 lines are covered by the 18:00-18:57 batch.
- No diamonds or money spent. No speedup or stamina item used. Tracker untouched (partial unit). Blocker category: h (by-design partial - the sweep is split across the 16:30 and 17:30 chain pair by design).

## Ended trade day close, 2026-11-11 19:00 - fuller consolidation sweep (this run)

- This run is the first organizer pass after the 19:00 local reset, so it does the fuller consolidation sweep of the ended trade day (2026-11-10 19:00 to 2026-11-11 19:00) in addition to the incremental fold. Sweep verification: the watermark chain is continuous across the day's 19 organizer runs (0032 worked from the 2332 watermark, each run from the previous run's fold-through, 1832 folding through 6cbd479fc2), and the only substantive commits after the 1832 watermark are the ticker-1822 zombie 018 pass (05b0801ff5), the perception-scout 1850 events group (7b944422a4) and the queue-planning 1840 pass (63165f49a7) - all folded here. No ended-trade-day record is left unfolded. The pr-integration 1900 pass merged records PR #655 at the 19:00 batch (merge 87ea0981f3), so the day's records are complete in main; the post-1900 records PR #665 is open for the next day's batch.
- Last passes of the day: ticker-1822 zombie-invasion unit 018 partial (3 Lv.10 kills sequential, 3 LOOT rows claimed 804,000 coins, coin 136.7M to 137.5M, stamina 88 to 59, successor 019 enqueued); ticker-1843 perception-scout events group partial (Events hub strip walked, Arms Race Base Building score 0 with 03:07:30 left and tier 3 at 30,000, Age of Oil Tech 9475/500 and Base Expansion II 22232/500 exceeded, 4 red dots seen with 0 explained, day total 7 unexplained); queue-planning 1840 done (12 units staged for the 2026-11-12 06:03/06:30 slots, 6 expired 14:30 slots, sweep pair verified by status per #610).
- Sweep pair, per the planner's status verification (#610): both passes are in done, both partial - first pass zero-sweep-2026-11-11-1630 by ticker-1718 (1 of 23 lines, trucks 1/5 dispatch 0/4 plunder), final pass zero-sweep-2026-11-11-1730 by ticker-1800 (5 of 23 lines, all non-zero). The pair is executed but NOT complete in the full-ledger sense: 6 of 23 lines read live, 17 covered only by the 18:00-18:57 batch units. Last night's pair (2026-11-10) stands INCOMPLETE as the 2340 run reported (1630 partial 1/23, 1730 expired unexecuted); not re-verified this run.
- Final counters at the reset: trucks 1/5 dispatch, 0/4 plunder (1726 read, unchanged since the 16:52 scout read) - shortfall dispatch -4, plunder -4; the fix-up trucks-2026-11-11-1457 (priority 1) has no execution record on the branch and closes unrun. Donations points 4050 live, remaining count unread at the close; the fix-up donations-2026-11-11-1803 (priority 1) has no execution record on the branch. VIP freebie and login chest unread since the 1626 claim (freebie +120 points, streak 5 days); the fix-up vip-2026-11-11-1800 has no execution record on the branch. Mail Alliance and Event gifts unclaimed at the 1730 read; the fix-up mail-2026-11-11-1830 has no execution record on the branch. Arms Race Base Building phase score 0 at the 1850 read with tier 3 at 30,000, R4 flag for the arms-race-2026-11-11-1803 unit, which has no execution record on the branch. Age of Oil stage-1 badge 1 with both counters exceeded, claim state unmeasured, handed to the event-claims unit.
- Power at the close: Total Power 149,218,973 (unchanged across the day's reads); coin 137.5M, food 694.1M, iron 1.0G at the 19:01 scout exit read. Zombie Invasion - Glacieradon live with about 1d 23h left at 19:00, next wave about 00:03, challenge opens 2026-11-12 18:00; unit 019 sits in inbox. Six 14:30-slot units expired unrun (train, star-ceremony, mail, help, gifts, duel-score), reaped by the planner.
- Still open at the reset, carried to the next trade day: the trucks shortfall (dispatch -4, plunder -4); the donations remaining count; the VIP and mail fix-ups; the Age of Oil stage-1 badge claim state (Issue #477); the Coin Chest (SSR) row below the fold and the 480-medal tooltip in the Zombie Store; the skull cycle timer (Issue #498); the sync duplicate chain head (tooling Issue #664); the sweep pair incomplete (6 of 23 lines). No execution record for the 18:00-18:57 batch units (harvest-1803, mail-1830, events-1857, donations-1803, vip-1800, arms-race-1803, and the train, radar, daily-missions, duel-score and secrets units the 1730 sweep names as standing in inbox) has landed on the records branch at run close; their outcomes are not recorded here.
- Next trade day: the planner 1840 staged 12 units (06:03/06:30 slots 2026-11-12: mail, help, gifts, harvest, radar, survivors, train, training, donations, arms-race, star-ceremony, duel-score).
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Queue-planning 1940 verification, 2026-11-11 19:40 - sweep pair both partial, 6 staged, Issue #668

- Planner pass queue-planning-2026-11-11-1940, about 19:40 to 20:12 local, status done. Evidence in `_records_/2026-11-11/queue-planning/1940-run.md` (commit 2cf8ce514e on records/2026-11-11). This job only plans: it never controls the device and never plays the game.
- Pre-reset sweep pair, verified BY STATUS per #610: both passes are in done, each carrying `status: partial` - first pass zero-sweep-2026-11-11-1630 by ticker-1718 (1 of 23 lines, trucks 1/5 dispatch 0/4 plunder), final pass zero-sweep-2026-11-11-1730 by ticker-1800 (5 of 23 lines, all non-zero). The pair is executed but NOT complete in the full-ledger sense: 6 of 23 lines read live, 17 covered only by the 18:00-18:57 batch units. No enqueue was needed and no ledger-walk task text was appended.
- Plan: 6 units staged for the 2026-11-12 06:57/07:00 slots (passes, secrets, treasures, trucks, events, scout-midday); 68 already present, 0 reaped, 0 expired; 1 skipped closed (zero-sweep-2026-11-11-1730). Roster stale, carried (issue #198): building-queues, research and zombie-invasion missing from the loaded roster. Pool by_state at 19:47: inbox 78, claimed 0, done 1612.
- Scout diff on the branch-merged 3-pass observation: observed 29, actionable 0, to enqueue 0, raises 0, candidates 0, unexplained red dots 9 (additive day total; 5 distinct still unexplained - see the perception-scout 1946 fold). Applied: 0 enqueued, 0 apply failures, net 0 new units. The diff is idempotent on both copies (live 2-pass: observed 21, unexplained 5). Queue cleanup: 0 withdrawals.
- Issue filed by this run, tooling class, owned by lastwar-tool-developer (not this job): #668 - the scout observation writer replaces the previous continued pass instead of appending (the ticker-1843 section dropped by ticker-1919; the branch copy was repaired by the ticker delivery merge, the live file still holds base + 1919 only). The day-total counters are additive across passes (9 unexplained counts the Zombie Store dot twice and includes three items the 1946 pass later explained); a netting rule for the counters belongs with the same fix.
- New trade day's first executions (after the 19:00 reset): zombie-invasion 019 (ticker-1919, 2 Lv.10 kills in parallel, 536,000 coins, coin 137.5M to 138.0M) and 020 (ticker-2001, 2 kills in parallel, 1 LOOT row claimed 268,000, Squad 1 row lost - third handover-style loss), perception-scout 002 (ticker-1919, events group remainder, 7 red dots, 5 explained, 2 unexplained). See the zombie-invasion 1936/2020 and perception-scout 1946 folds.
- Still open at this run's close (20:32): NO execution record for the 18:00-18:57 batch units (harvest-1803, mail-1830, events-1857, donations-1803, vip-1800, arms-race-1803, and the train, radar, daily-missions, duel-score and secrets units the 1730 sweep names as standing in inbox) has landed on the records branch. Their outcomes are not recorded here - not asserted expired, not asserted executed. The fix-ups the sweeps raised to priority 1 remain unrecorded the same way.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Retro 2026-11-11 final tally - Nov 11 closed at 116 finished, 39 expired, whole types dark, Issues #671 and #673

- This settles the open thread the 2032 run left: the 18:00-18:57 batch units did NOT execute before the 19:00 reset - they expired. The 2026-11-11 daily retro (commit d5561aaa on records/2026-11-11) closes Nov 11 at 116 finished on the branch pool: done 21 (18 percent), partial 54, failed 1, expired 39, skipped 1, unverified 60 (52 percent). Expired 39 is up from 18 on Nov 10 and 17 on Nov 9.
- Whole types went dark: events, train and star-ceremony units all expired - nothing ran in any of the three types - and no daily-missions unit of Nov 11 ran at all. All 3 duel-score units expired, so no duel total was read at all and the day-3 total is unknown (Issue #673, records class; see alliance-duel 1.43.0). The five 1457-slot units (trucks, treasures, secrets, passes, events) sit past-expiry in the branch inbox, unreaped at the retro snapshot (21:16). The failed unit is train-2026-11-10-2230 (finished 02:06 PST); the skipped unit is arms-race-2026-11-11-0203 (Tech Research, 0 of 30,000, OD-20261031-01 pattern).
- Filed by the retro: Issue #671 (records class) - Nov 11 expiry pile-up, 39 expired, events/train/star-ceremony all dark, no daily-missions unit ran. Target: expired under 20 per day and no type fully expired. Verification: a Nov 12 day with expired under 20 and no type fully expired. Recheck: 2026-11-12 retro.
- Account power flat at 149,218,973 all day, read live 51 times across Nov 11 records, from 19:16 PST Nov 10 to 19:44 PST Nov 11 - up 431,395 on the Nov 10 close 148,787,578, with no named cause for the rise, and no new step-down occurred.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## 18:00-18:57 batch reaping, 2026-11-11 23:33 - five 1857 units expired, passes-2257 still pending

- The 18:00-18:57 batch outcome is now settled at queue-file level (commit 11ac21dce on records/2026-11-11, ticker-2333 pass): the five 1857 units (events, passes, secrets, treasures, trucks) were reaped as expired at 23:33 PT - status expired, "window passed before execution" - after the 2026-11-11 retro snapshot (21:16), which had left them sitting past-expiry in the inbox unreaped. The remaining 1803/1830 units resolve as: executed - harvest-1803 partial, radar-1803 done, survivors-1803 partial, training-1803 partial; expired - mail-1830, donations-1803, train-1830, duel-score-1830, gifts-1830, help-1830, star-ceremony-1830; skipped-needs-owner - arms-race-1803. This confirms the retro's 39-expired tally (Issue #671) at unit level and closes the open thread the 2032 run left.
- passes-1857's expiry means the Monthly Pass Claim Reward was NOT claimed by that unit - the claim still rests on passes-2026-11-11-2257, still in inbox at the records tip, unexecuted. The 22:03/22:30/22:57 units (arms-race, donations, harvest, radar, survivors, training, duel-score, events, gifts, help, mail, passes, secrets, star-ceremony, train, treasures, trucks, scout) are still in inbox - their outcomes fall to later runs, in the new trade day's records.
- vip-2026-11-11-1800 and daily-missions-2026-11-11-1800 are still unreaped in inbox at the records tip - neither executed nor expired on the branch yet.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Ticker-0100 reaping, 2026-11-12 01:02 - thirteen stale inbox units expired, duplicate 022 executed, harvest-2203 collected

- The ticker-0100 pass (commit 911d317f8 on records/2026-11-12) reaped 13 stale inbox units as expired at about 01:02 PT - status expired, "window passed before execution": donations-1803, events-1457/1857, passes-1457/1857, radar-1803, secrets-1457/1857, survivors-1803, treasures-1457/1857, trucks-1457/1857 (all 2026-11-11 units). CORRECTION - three of the thirteen are stale-branch artifacts, not new execution facts: radar-1803, survivors-1803 and training-1803 were EXECUTED on the 2026-11-11 branch (radar done, survivors partial, training partial - see the 18:00-18:57 batch section above), and the 0100 reaper on this branch marked their never-updated inbox copies expired. The genuine new expirations on this branch are the ten 1457/1857 units plus donations-1803 (already noted expired in the 0032 run). The 0032 run's "five 1857 units reaped expired 23:33" and this pass's reaping cover the same five 1857 units (events, passes, secrets, treasures, trucks) - the branch copies were reaped once per branch; the expiry itself is one fact.
- The same pass executed the stale inbox copy of zombie-invasion unit 022 (see the zombie-invasion 0114 fold) - its completion rides on PR #681 (records/2026-11-11), unmerged at 01:00, so the branch queue still showed 022 in inbox while 023 was already done. The duplicate execution is a branch-sync artifact; the live pool is consistent (022 done, 023 done, 024 enqueued, 025 enqueued). The 0032 run's follow-up question - whether the 22:03/22:30/22:57 units executed - is now settled in part: harvest-2203 EXECUTED (0126 unit, panel Collects 12,195,086); the rest of the 22:03 batch (arms-race, donations, radar) and the 2230 units (duel-score, gifts, help, mail) and the 2257 units (events, passes) remain in inbox, unexecuted at this run's close. passes-2257 - the Monthly Pass Claim Reward - is still pending.
- vip-2026-11-11-1800 and daily-missions-2026-11-11-1800 remain unreaped in inbox at the records tip - neither executed nor expired on the branch yet.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Ticker-0134/0204, 2026-11-12 01:50-02:07 - control channel lock stops both passes, help-2230 failed, four 2203 units expired

- The ticker-0134 pass (radar 0151, commit 889dda54f) and the ticker-0204 pass (help 0207, commit b23df0eba) both met the control channel outcome_unknown lock filed as Issue #689 and stopped per that issue: radar-2026-11-11-2203 FAILED (no radar work done, nothing claimed) and help-2026-11-11-2230 FAILED (0 helps, nothing claimed). Both are the same lock (second and third occurrences of the night, sessions cc-695-697 and cc-698-699, same window 676414, same error text, read-only inspection live throughout). The 0204 pass reaped four 2203 units as expired at about 02:05 PT - status expired, "window passed before execution": arms-race-2026-11-11-2203, donations-2026-11-11-2203, survivors-2026-11-11-2203, training-2026-11-11-2203. None of the four executed: no Armed Truck location attempt in the arms-race unit, so retro action A-2026-11-11-05 (Issue #566) verification is STILL UNMET - the thirteenth deferral recorded by the 0132 run stands as the last word.
- The 0032 run's follow-up question - whether the 22:03/22:30/22:57 units executed - is now settled further: 22:03 - harvest EXECUTED (0126), arms-race/donations/survivors/training EXPIRED unexecuted, radar FAILED (0151); 22:30 - help FAILED (0207), duel-score/gifts/mail still in inbox, unexecuted; 22:57 - events/passes still in inbox, unexecuted. passes-2026-11-11-2257 - the Monthly Pass Claim Reward - is still pending. duel-score-2026-11-11-2230 still in inbox: the day-4 duel total is still unread (contrast Issue #673, day-3 total unknown).
- New 0230 units are already staged in inbox (duel-score, gifts, help, mail, harvest, radar, arms-race, donations, events, passes) for the next ticks; the zombie-invasion unit 024 stays queued, blocked by the same lock in both passes. vip-2026-11-11-1800 and daily-missions-2026-11-11-1800 remain unreaped in inbox at the records tip - neither executed nor expired on the branch yet.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.

## Ticker-0234/0304, 2026-11-12 02:34-03:20 - control channel lock stops both passes, zombie 024 and 025 failed, pool now pauses (R9), passes-2257 expired unexecuted

- The ticker-0234 pass (zombie 024, commit c4faa2378) and the ticker-0304 pass (zombie 025, commit 025264559) both met the control channel outcome_unknown lock filed as Issue #689 and stopped per that issue: the fourth and fifth occurrences of the night, the third and fourth consecutive blocked passes, sessions cc-700-702 and cc-703-705, three first-input attempts each, no dispatch at all, read-only inspection live throughout. The 0304 pass is the first use of the pool-level control-lock blocker (queue design 0.17.0 rule R9, PR #692 merged 2026-11-12 02:47 PT): the zombie unit recorded the blocker at completion, so the pool hands out nothing while it stands - successor zombie 026 waits instead of burning another failed unit. The next probe comes only after the blocker ages out (4 hours, about 07:20 PT) or input succeeds. This supersedes the 0134/0204 fold's "new 0230 units are already staged for the next ticks" expectation for the morning: staged units due before about 07:20 will not execute while the blocker stands, and the next tick no longer retries blindly.
- Reaping settled in these passes: the 0234 sync reaped 0 and expired 7 stale 2026-11-11 2203/2230 inbox copies already closed on records/2026-11-12; the 0304 sync reaped 0 and expired 10 worktree-pool stale copies (2026-11-11 2230/2257) plus 5 live-pool copies (the 2257 units whose 02:57 PT expiry had passed unexpired in the live pool). Due 25, already queued, produced none in the 0304 pass.
- The 0032 run's follow-up question - whether the 22:03/22:30/22:57 units executed - is now settled further: 22:57 - events/passes EXPIRED unexecuted (the 2257 units expired in the 0304 live-pool sync). passes-2026-11-11-2257 - the Monthly Pass Claim Reward - is still pending, and its unit has now expired; the claim needs a fresh unit, not a retry of the expired one. 22:03 - harvest EXECUTED (0126), arms-race/donations/survivors/training EXPIRED unexecuted, radar FAILED (0151); 22:30 - help FAILED (0207), duel-score/gifts/mail still in inbox, unexecuted. duel-score-2026-11-11-2230 still in inbox: the day-4 duel total is still unread (contrast Issue #673, day-3 total unknown). vip-2026-11-11-1800 and daily-missions-2026-11-11-1800 remain unreaped in inbox at the records tip - neither executed nor expired on the branch yet.
- The 0304 pass also resolved the records PR #685 conflict branch-side before any game work (PR #681 merged 03:02 PT, merge commit 0dc85d79): merged main into records/2026-11-12 (merge 8cdab1cb2f5, 21 files; _queue_/done 2026-11-11 files take main as authoritative - radar-1803 done and survivors-1803 partial kept over this branch's expired copies; stale inbox duplicates scout-006 and zombie-023 removed; action-log union of both tails). The pr-integration 0300 run (BATCH) merged #681 and commented #685 as conflicting, not merged; the 0330 run (NON-batch) re-verified #685 CLEAN against main 0dc85d79 - it awaits the 07:00 batch. The queue-planning 0240 run staged 12 units for the 14:03/14:30 slots (62 already present); the scout diff on the 6-pass observation (52 observed, 11 unexplained) applied with all zero counts, 0 withdrawals, no issues filed. Pool inbox 78, claimed 0, done 1646.
- Retro action A-2026-11-11-05 (Issue #566) verification is STILL UNMET - no arms-race unit has run since the 0132 run, so no Armed Truck location attempt exists; the thirteenth deferral recorded by the 0132 run stands as the last word.
- No diamonds or money spent in the folded units. No game was operated by this run and no queue code or cron definition was edited.
