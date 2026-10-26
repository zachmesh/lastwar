---
title: Routine Activities
created: 2026-10-25T17:56:00Z
modified: 2026-10-26T13:20:00Z
level: L1
version: 1.11.0
description: The umbrella checklist of the every four hours routine, linking one folder per activity type - kept under its original daily-activities folder name for link stability
status: unverified
grounded_in:
  - source: in-game base screen observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner rule on 2026-10-26 - the routine is every four hours, not daily, and every regular is checked and done at every run whenever it is available
  - source: owner design on 2026-10-26 - remove the single every four hours job and split the routine into segment schedules rotating hourly, each segment looking at a specific set of tasks
  - source: owner refinement on 2026-10-26 - the segments run in the same hour, 15 minutes apart, not one per hour
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

- The canonical list is `tools/regulars.json` - one entry per
  regular, with its cadence (every run for everything in the
  routine, daily with the 19:00 reset for VIP, Thursdays for
  Ghost Ops) and its segment (1 to 4). Every-run regulars become
  due again at each new cycle of their own segment - a regular
  done or skipped in an earlier cycle is never a reason to skip
  it in the current one.
- Since 2026-10-26 the routine runs as 4 segment schedules in
  the same hour, 15 minutes apart, replacing the single every
  four hours job - segment 1 (production and Arms Race -
  harvest, training, donations, radar, survivors, Arms Race)
  fires at :12, segment 2 (alliance - mail, help, gifts, train,
  star ceremony) at :27, segment 3 (missions and logistics -
  secrets, treasures, trucks, Ghost Ops) at :42, segment 4
  (claims - passes, events, VIP) at :57, and each segment
  repeats every 4 hours, so the whole routine completes inside
  one hour of each cycle. The split was the owner design
  against the device-access error that kept cutting the single
  long run short mid-session - short segment runs finish inside
  one session, and one segment failing loses only that segment.
- The tracker is `tools/regulars.py` - `list` shows every regular
  with its status for the day, `todo` shows only what is still due,
  `done <id>` and `skip <id>` record an outcome with a note. State
  is kept per local date in `tools/state/`.
- Every run starts from `todo` and ends with `list`, so an expected
  regular is either done, skipped with a reason, or still visibly
  due - never silently dropped. The four-hourly cron instruction
  points at the same list; the list in this folder above is the
  human-readable mirror.

## Standing boundaries for every round

- No purchases, no diamond spending, no PvP, no alliance diplomacy, no
  city moves without the owner approval, per the recording rules.
