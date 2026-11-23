---
title: Hidden Treasures
created: 2026-10-26T04:00:00Z
modified: 2026-11-23T06:48:51Z
level: L1
version: 1.24.0
description: Treasure map fragment collection, ally exchange and digging, one activity folder for hidden treasure knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner direction to register each learned task type as metadata, 2026-10-25
  - source: hidden-treasures execution record 2026-11-01 0150 PST
  - source: perception-scout execution record 2026-11-01 0215 PST, cross-check read
  - source: hidden-treasures execution record 2026-11-01 1420 PST
  - source: ticker-0204 hidden-treasures execution record 2026-11-02 0207 queue run
  - source: ticker-0404 hidden-treasures execution record 2026-11-02 0424 queue run (done, checked only)
  - source: ticker-1004 hidden-treasures execution record 2026-11-02 1009 queue run (done, checked only)
  - source: ticker-1336 hidden-treasures execution record 2026-11-02 1352 queue run (done, checked only)
  - source: ticker-2134 hidden-treasures execution record 2026-11-02 2135 queue run
  - source: ticker-0004 hidden-treasures execution record 2026-11-03 0014 queue run (done, checked only, M3 at zero)
  - source: ticker-0334 hidden-treasures execution record 2026-11-03 0349 queue run (done, checked only, counts identical to 0014, M3 at zero)
  - source: ticker-0834 hidden-treasures execution record 2026-11-03 0838 queue run (done, checked only, counts identical to 0349, M3 at zero)
  - source: ticker-1234 hidden-treasures execution record 2026-11-03 1243 queue run (done, checked only, counts identical to 0838, M3 at zero, leftover Gold Mine panel entry)
  - source: ticker-0834 hidden-treasures execution record 2026-11-04 0847 queue run (done, checked only, fragment counts identical to 0838/1243, M3 still binding)
  - source: ticker-1434 hidden-treasures execution record 2026-11-08 1459 queue run (done, one dig executed, fragments M1-M7 each down 1, chest progress 6/15 to 7/15, tab badge 1 while stock allowed 3 digs - badge-equals-digs rule disproved); record commit dfd3c87f9 on records/2026-11-08
  - source: ticker-2235 hidden-treasures execution record 2026-11-08 2255 queue run (done, one dig executed, fragments M1-M7 each down 1, chest progress 7/15 to 8/15, 2 digs remain capped by M3, tab badge 1 re-confirmed not the dig count; record commit 0c9686b4f on records/2026-11-08)
  - source: ticker-0504 hidden-treasures execution record 2026-11-09 0525 queue run (done, 1 dig executed, fragments M1-M7 each down 1, chest progress 9/15 to 10/15, M3 binding at x1, tab badge 1 with exactly 1 dig possible; record commit be01e91134 on records/2026-11-09)
  - source: ticker-0204 hidden-treasures execution record 2026-11-10 0223 queue run (done, 1 dig after the secrets claim restocked M3, chest 11/15; record commit 069a94c7a on records/2026-11-10)
  - source: ticker-0434 hidden-treasures execution record 2026-11-10 0446 queue run (done, checked only, no dig possible, M3 binding at zero, tab badge cleared, Rewards button unopened; record commit 5ba07ce2b4 on records/2026-11-10)
  - source: ticker-1004 hidden-treasures execution record 2026-11-10 1040 queue run (done, checked only, no dig possible, M3 at 0, Rewards button checked and is an odds preview only; record commit 2218eb3cd on records/2026-11-10)
  - source: ticker-1343 hidden-treasures execution record 2026-11-10 1351 queue run (done, checked only, no dig possible, M3 at 0, stock identical to the 10:40 read, chest 11/15; record commit b2c2b7a43 on records/2026-11-10)
  - source: ticker-1834 hidden-treasures execution record 2026-11-10 1855 queue run (done, checked only, fragment stock identical to the 13:51 read, M3 at 0, no dig possible, chest 11/15; record commit af56d36ec on records/2026-11-10)
  - source: ticker-0234 hidden-treasures execution record 2026-11-11 0307 queue run (done, checked only, fragment stock M1 12, M2 11, M3 0, M4 6, M5 1, M6 6, M7 10, chest 12/15, no dig possible, dig odds reward detail read; record commit 2abfb335c on records/2026-11-11)
  - source: ticker-0637 hidden-treasures execution record 2026-11-11 0654 queue run (done, checked only, fragment stock identical to 0307, M3 at zero so no dig, chest 12/15, no tab badge, Skip Animation ticked; record commit f8ee03b36 on records/2026-11-11)
  - source: ticker-0234 hidden-treasures execution record 2026-11-22 0253 queue run (done, checked only, live stocks M1 x2 M2 x3 M3 x0 M4 x0 M5 x0 M6 x8 M7 x3, chest 5/15, no complete set, unattributed movement since 2026-11-11 - at least ~10 digs with no treasures record after 2026-11-11; record commit c5c9b88d6 on delivery branch ticker-0234-records-1122, not on main - provenance noted)
---

# Hidden Treasures

Read rule-digest.md first.

Treasure map fragment collection, ally exchange and digging, one activity folder for hidden treasure knowledge. This document was split verbatim into 34 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - Hidden treasures to run-20261110-1040
- [Catalog 02](catalog-02.md) - run-20261110-1351 to run-20261122-0253

## Changelog

- 1.24.0, 2026-11-23 - Split verbatim by `split_doc.py` from a 687-line, 8,113-word body into 34 key-named articles and 2 catalog pages, and added `rule-digest.md`; no word rewritten, no claim superseded. `--verify` PASS and `--check` EQUAL, body sha256 fde5e70df3cd; the unsplit 1.23.0 file is commit 11d23ccf.
