---
title: Monitoring
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 14
description: Daily - the daily retro computes the core set - family A rolling and by-day, family
---
## Monitoring

- **Daily** - the daily retro computes the core set: family A
  rolling and by-day, family B for the perception day, family D
  snapshot and recurrence check, family G snapshot. The figures
  land in the day's data appendix and the headline movements in
  the retro file's dashboard - top leak, the metric that moved
  most, every threshold breach by name.
- **Weekly** - the first retro of a week compares the window
  against the previous week's data files for every family,
  including the slow ones (C, E, F), and files improvement
  entries for what the comparison shows.
- **Naming** - a threshold breach is named in the retro's Slack
  summary and in the chat report of that retro, by metric and
  value, the same day it is computed. A metric that goes
  data-gap for two consecutive computations is also named -
  silence about a blind metric is how the loop lost whole task
  lines before this specification existed.

First threshold set (each may be revised by a retro, with the
reason written into that retro file):

- unexplained red dots over 0 on any perception day;
- recurrence of any closed improvement's root cause within 7
  days of its closure;
- the unverified rate of post-specification units failing to
  fall week over week, or standing over 20 percent after the
  first full week of post-specification execution;
- oldest open backlog entry over 7 days old;
- any unit expired and unexecuted, or a daily standing job's
  artifact missing;
- ledger coverage under 23 of 23 lines read on a sweep day.

