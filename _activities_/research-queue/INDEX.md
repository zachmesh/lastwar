---
title: Research Queue
created: 2026-10-25T18:58:00Z
modified: 2026-11-23T07:40:44Z
level: L1
version: 1.8.0
description: Completing finished research and keeping research slots working, one activity folder for research knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: "ticker-0736 scout-discovery execution record 2026-11-09 0744 queue run (done, research queue read live - Defense Training VIII completed and unpressed, no owning regular (Issue #513), Lv.1 Missile Mastery II 2d 02:29:17 left, flask centre (59,249); record commit 36992d92e on records/2026-11-09)"
  - source: ticker-1934 research-queue execution record 2026-11-09 2031 queue run (done, Defense Training VIII completed via Complete, power +15,000 to 146,751,949, Missile Mastery II 1d 13:54:11 left; record commit 69d8e38ec on records/2026-11-09)
  - source: ticker-0104 research-queue execution record 2026-11-10 0116 queue run (done, slot 1 in progress 1d 09:04:53, slot 2 Idle, flask tap opens the research tree not a queue panel; record commit e5272617a on records/2026-11-10)
  - source: ticker-0834 research-queue execution record 2026-11-10 0846 queue run (done, slot 1 in progress 1d 01:35:27, slot 2 Idle, flask tap opens the research tree again, slot-1 timer discrepancy with the 0850 TECH-screen read; record commit 5473d6845 on records/2026-11-10)
  - source: ticker-0534 research-queue execution record 2026-11-11 0553 queue run (done, queue read live, slot 1 busy 04:27:41 finishing about 10:21, slot 2 Idle, timer discrepancy resolved in favour of the 0846 read, no-completion evidence for the 0535 arms-race conclusion; record commit a3ef6b276 on records/2026-11-11)
  - source: ticker-0957 research-queue execution record 2026-11-22 1010 queue run (done, both slots read live - Lv.3 Advanced Armor VIII 06:32:07 left, Lv.6 Defense Training VIII 15:51:34 left, carried Lv.1 Missile Mastery II name superseded, flask-entry correction did not reproduce; record commit e859f4993 on main)
  - source: "ticker-1234 research-queue execution record 2026-11-22 1310 queue run (done, both slots read live - Lv.3 Advanced Armor VIII 03:33:29 left, Lv.6 Defense Training VIII 12:52:56 left, carried Lv.1 Missile Mastery II name superseded, flask-entry correction did not reproduce; record commit 1894606e6 on records/2026-11-22, PR #821)"
---

# Research Queue

Read rule-digest.md first.

Completing finished research and keeping research slots working, one activity folder for research knowledge. This document was split verbatim into 16 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Research queue](research-queue.md)
- [What this activity is](what-this-activity.md) - what-this-activity - Checking the research queue, completing finished
- [How it is done part 1](how-it-is-p1.md) - how-it-is - Open the research queue from the
- [How it is done part 2](how-it-is-p2.md) - how-it-is - Press Complete on any finished item
- [What is known from 2026-10-25 part 1](day-20261025-p1.md) - day-20261025 - Two research slots exist.
- [What is known from 2026-10-25 part 2](day-20261025-p2.md) - day-20261025 - The name is still carried as
- [Open questions](open-questions.md) - open-questions - The research tree order that best
- [What the 2026-11-09 0744 scout-discovery unit added -](run-20261109-0744.md) - run-20261109-0744 - Unit scout-scout-discovery-2026-11-09-002 by ticker-0736, about 07:44
- [What the 2026-11-09 2031 unit added - Defense](run-20261109-2031.md) - run-20261109-2031 - Unit research-2026-11-09-1803 by ticker-1934, about 20:25
- [What the 2026-11-10 0116 unit added - slot](run-20261110-0116-p1.md) - run-20261110-0116 - Unit research-2026-11-09-2203 by ticker-0104, about 01:13
- [What the 2026-11-10 0116 unit added - slot](run-20261110-0116-p2.md) - run-20261110-0116 - Result stats: target queue state read
- [What the 2026-11-10 0846 unit added - slot](run-20261110-0846.md) - run-20261110-0846 - Unit research-2026-11-10-0603 by ticker-0834, about 08:45
- [What the 2026-11-11 0553 unit added - queue](run-20261111-0553.md) - run-20261111-0553 - Unit research-2026-11-11-0203 by ticker-0534, about 05:52
- [What the 2026-11-22 1010 and 1310 units added](run-20261122-1010-p1.md) - run-20261122-1010 - Units research-2026-11-22-0603 by ticker-0957 (1010, about
- [What the 2026-11-22 1010 and 1310 units added](run-20261122-1010-p2.md) - run-20261122-1010 - Result stats: 1010 - target 2,
- [Changelog](changelog-section.md) - changelog-section - 1.6.0 (2026-11-22): 1010 and 1310 research

## Changelog

- 1.7.0, 2026-11-23 - Split verbatim into 16 articles, added `rule-digest.md`; `--check` EQUAL, body sha256 6b04543a62c6; unsplit 1.6.0 is commit 11d23ccf.
