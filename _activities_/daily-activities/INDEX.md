---
title: Routine Activities
created: 2026-10-25T17:56:00Z
modified: 2026-11-10T02:42:02Z
level: L1
version: 1.22.0
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
