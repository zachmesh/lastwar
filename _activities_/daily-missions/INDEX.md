---
title: Daily Missions
created: 2026-10-25T18:58:00Z
modified: 2026-11-23T07:43:31Z
level: L1
version: 1.18.0
description: The Mission daily task list and activity chests, one activity folder for mission knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: daily-missions execution record 2026-11-01 1444 queue run
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (missions fix-up expired, attempts 0)
  - source: daily-missions execution record 2026-11-02 0444 queue run
  - source: ticker-0004 daily-missions execution record 2026-11-03 0017 queue run (partial, activity chest claim path unverified, Issue 208)
  - source: "ticker-0904 daily-missions execution record 2026-11-04 0914 queue run (partial, 3 gather tasks claimed on one tap, first verified 200-point activity-chest claim, Issues #171 and #208 commented by the ticker pass)"
  - source: ticker-1734 daily-missions execution record 2026-11-05 1734 queue run (failed, Mac device offline, fifty-sixth consecutive ticker pass with a Mac device-access blocker, seventeenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 10h, unchanged since the 1025 pass; seven invokes, zero responses)
  - source: ticker-1604 daily-missions execution record 2026-11-06 1612 queue run (failed, Mac device offline, eighty-second consecutive ticker pass with a Mac device-access blocker, forty-third in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 32h35m, unchanged since the 1507 and 1534 passes; seven invokes, zero responses)
  - source: ticker-0204 perception-scout execution record 2026-11-08 0229 queue run (partial per R1, daily missions panel walked, full 22-task list read live, 4 completed unclaimed, Next Refresh pointing to about 18:00 local; record commit 6560ff267 on records/2026-11-08)
  - source: ticker-1604 daily-missions execution record 2026-11-08 1628 queue run (partial, 4 completed tasks claimed on one tap, activity 0 to 70, first verified 40-point activity-chest claim with double-rewards receipt, Issues 171 and 208 commented by the ticker pass; record commit d8b700b90 on records/2026-11-08)
  - source: ticker-1724 daily-missions execution record 2026-11-08 1753 queue run (partial, full daily task list re-checked live, nothing newly completed, activity 70, 80-point chest 10 short into the reset, claimed rows sink to the bottom with green checks correcting the 1628 removed-from-list reading, first observed duplicate execution of the same unit id; record commit 5f3a904f4 on records/2026-11-08)
  - source: ticker-1518 daily-missions execution record 2026-11-09 1519 queue run (done, one tap claimed all four completed rows at once and the 40/80/120 chests by cascade, activity 0 to 140, one-tap-multi-claim now verified by before/after reads, slow-drag scroll method measured, activity-star composition open; record commit da249faca3 on records/2026-11-09)
  - source: ticker-1424 daily-missions execution record 2026-11-10 1426 queue run (done, four completed rows claimed, 40/80/120 chests claimed with contents identical to the 1519 read, activity 120, Next Refresh 03:31:56 to the 18:00 reset; record commit edd4659a3 on records/2026-11-10)
  - source: ticker-1634 daily-missions execution record 2026-11-11 1638 queue run (done, two completed rows claimed on one tap, activity 80 to 100, 40/80 chests already claimed with contents previewed, Mission list would not scroll - quick drag, scroll action and slow staged drag all no-change; record commit 1fe3a5e69 on records/2026-11-11)
  - source: ticker-1504 daily-missions execution record 2026-11-22 1504 queue run (partial, 6 completed rows claimed on one tap, activity 0 to 90, 40 and 80 activity chests claimed, seventh one-tap-multi-claim observation, 40-chest receipt read a third distinct time; record commit 06e2febac on records/2026-11-22)
---

# Daily Missions

Read rule-digest.md first.

The Mission daily task list and activity chests, one activity folder for mission knowledge. This document was split verbatim into 34 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - Daily missions to run-20261109-1519
- [Catalog 02](catalog-02.md) - run-20261109-1519 to run-20261122-1504

## Changelog

- 1.16.0, 2026-11-23 - Owner name already replaced on main by the tree-wide pass (commit 0467e3ef), then split verbatim by `split_doc.py` from a 527-line, 9,810-word body into 34 key-named articles and 2 catalog pages, and added `rule-digest.md`. `--check` EQUAL against that file, body sha256 8c7ccb9c16f9; the unsplit 1.15.0 file is commit 0467e3ef.
- 1.18.0, 2026-11-23 - A platform account label (a 'Signed in as' banner) replaced with 'owner account' in 1 line of 1 file; no other change.
