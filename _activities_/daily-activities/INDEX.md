---
title: Routine Activities
created: 2026-10-25T17:56:00Z
modified: 2026-11-02T02:44:38Z
level: L1
version: 1.16.0
description: The umbrella checklist of the every four hours routine, linking one folder per activity type - kept under its original daily-activities folder name for link stability
status: unverified
grounded_in:
  - source: in-game base screen observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner rule on 2026-10-26 - the routine is every four hours, not daily, and every regular is checked and done at every run whenever it is available
  - source: owner design on 2026-10-26 - remove the single every four hours job and split the routine into segment schedules rotating hourly, each segment looking at a specific set of tasks
  - source: owner refinement on 2026-10-26 - the segments run in the same hour, 15 minutes apart, not one per hour
  - source: owner refinement on 2026-10-26 - the spacing is 18 minutes, so the fires are :03, :21, :39 and :57
  - source: owner refinement on 2026-10-26 - make it 3 segments, 25 minutes apart
  - source: owner refinement on 2026-10-26 - 26 minutes apart
  - source: owner refinement on 2026-10-26 - 27 minutes apart, the final spacing
  - source: pre-reset zero sweep execution record 2026-11-01 1757 queue run (first zero sweep)
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
