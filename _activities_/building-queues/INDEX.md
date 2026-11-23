---
title: Building Queues
created: 2026-10-25T18:58:00Z
modified: 2026-11-23T06:47:36Z
level: L1
version: 1.7.0
description: Checking build queues and upgrade state, one activity folder for building knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: ticker-0736 scout-discovery execution record 2026-11-09 0744 queue run (done, building queue read live - Lv.29 Aircraft Center 2d 18:40:11 left, slots 2-4 idle, hammer entry (44,195), 2.5-day clock gap flagged; record commit 36992d92e on records/2026-11-09)
  - source: ticker-0842 scout-discovery execution record 2026-11-09 0848 queue run (done, Builders Hut Lv.26 banner quest measured read-only - Lv.25 to 26, Iron 170.0M, Food 56.9M, Original Time 15d 08:05:18, Upgrade button 7d 07:16:49, Finish Now 18,188 diamonds, owner-decision Issue #517; record commit ec55aa585 on records/2026-11-09)
  - source: ticker-1934 building-queues execution record 2026-11-09 2020 queue run (done, Aircraft Center 2d 06:07:55 left, slots 2-4 idle, hammer entry (44,195); record commit 69d8e38ec on records/2026-11-09)
  - source: ticker-0104 building-queues execution record 2026-11-10 0112 queue run (done, Aircraft Center 2d 01:14:21 left, slots 2-4 idle, banner quest now Build Oil Well; record commit e5272617a on records/2026-11-10)
  - source: ticker-0904 building-queues execution record 2026-11-10 0914 queue run (done, Aircraft Center 1d 17:13:16 left, slots 2-4 idle, clock coherent with the 0112 read, Total Power up about 1.31M; record commit 31892dde on records/2026-11-10)
  - source: ticker-0957 building-queues execution record 2026-11-22 1012 queue run (done, Drill Ground Lv.25 upgrading 07:12:47 left finishing about 17:30 PT, slots 2-4 idle, Lv.29 Aircraft Center upgrade finished, both standing queue claims superseded; record commit e859f4993 on main)
---

# Building Queues

Read rule-digest.md first.

Checking build queues and upgrade state, one activity folder for building knowledge. This document was split verbatim into 13 articles in reading order. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Building queues](building-queues.md)
- [What this activity is and 1 more](what-this-activity.md) - what-this-activity, how-it-is - Checking the four build queues, recording long running upgrades and noting idle slots.
- [What is known from 2026-10-25 part 1](day-20261025-p1.md) - day-20261025 - Four build slots exist.
- [What is known from 2026-10-25 part 2](day-20261025-p2.md) - day-20261025 - Builders Hut Lv.26 quest, measured 2026-11-09 0848 (scout-discovery unit, ticker-0842, read-only): the banner quest...
- [Open questions](open-questions.md) - open-questions - What the idle slots should build next.
- [What the 2026-11-09 0744 scout-discovery unit added -](run-20261109-0744.md) - run-20261109-0744 - Unit scout-scout-discovery-2026-11-09-002 by ticker-0736, about 07:44 to 07:53 local, status done.
- [What the 2026-11-09 0848 scout-discovery unit added -](run-20261109-0848.md) - run-20261109-0848 - Unit scout-scout-discovery-2026-11-09-009 by ticker-0842, about 08:48 to 08:53 local, status done.
- [What the 2026-11-09 2020 unit added - Aircraft](run-20261109-2020.md) - run-20261109-2020 - Unit building-queues-2026-11-09-1803 by ticker-1934, about 20:17 to 20:20 local, status done.
- [What the 2026-11-10 0112 unit added - Aircraft](run-20261110-0112-p1.md) - run-20261110-0112 - Unit building-queues-2026-11-09-2203 by ticker-0104, about 01:08 to 01:12 local, status done.
- [What the 2026-11-10 0112 unit added - Aircraft](run-20261110-0112-p2.md) - run-20261110-0112 - Result stats: target queue state read live, achieved 4 slots read live, resources_gained none,...
- [What the 2026-11-10 0914 unit added - Aircraft](run-20261110-0914.md) - run-20261110-0914 - Unit building-queues-2026-11-10-0603 by ticker-0904, about 09:11 to 09:14 local, status done.
- [What the 2026-11-22 1012 unit added - Drill](run-20261122-1012.md) - run-20261122-1012 - Unit building-queues-2026-11-22-0603 by ticker-0957, about 10:12 to 10:17 local, status done.
- [Changelog](changelog-section.md) - changelog-section - 1.6.0 (2026-11-22): 1012 building-queues unit folded (done, Drill Ground Lv.25 upgrading 07:12:47 left, finishes...

## Changelog

- 1.7.0, 2026-11-23 - Split verbatim, added `rule-digest.md`; body sha256 0d39c77b4560; unsplit 1.6.0 is commit 11d23ccf.
