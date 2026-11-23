---
title: The regulars list and its tracker
created: 2026-11-23T07:18:13Z
modified: 2026-11-23T07:18:13Z
version: 0.1.0
sequence: 5
description: Owner direction, late evening of 2026-10-25 - the four-hourly run performs all the regulars, not only
---
## The regulars list and its tracker

Owner direction, late evening of 2026-10-25 - the four-hourly run
performs all the regulars, not only Arms Race, and a list of the
regulars is kept so it is always visible what is still expected.

- The canonical list is `_tools_/regulars.json` - one entry per
  regular, with its cadence (every run for everything in the
  routine, daily with the trade-day reset (02:00Z, about 18:00 PST
  in winter, 19:00 PDT in summer) for VIP, Thursdays for
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

