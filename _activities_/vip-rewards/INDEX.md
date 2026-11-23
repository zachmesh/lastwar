---
title: VIP Rewards
created: 2026-10-25T20:46:00Z
modified: 2026-11-23T07:25:40Z
level: L1
version: 1.22.0
description: Claiming the daily VIP gift and VIP level rewards, one activity folder for VIP claim knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming VIP rewards, 2026-10-25
  - source: pre-reset zero sweep execution record 2026-11-01 1757 queue run (lines 12-13)
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (vip fix-up expired, attempts 0)
  - source: vip-rewards execution record 2026-11-02 0438 queue run
  - source: ticker-2134 vip-rewards execution record 2026-11-02 2138 queue run
  - source: ticker-0834 vip-rewards execution record 2026-11-04 0849 queue run (partial, VIP screen entry itself blocked, badge taps unresponsive, freebie/chest state unread)
  - source: ticker-1634 vip-rewards execution record 2026-11-06 1640 queue run (failed, Mac device offline, eighty-third consecutive ticker pass with a Mac device-access blocker, forty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 33h, unchanged since the 1507, 1534 and 1604 passes; seven invokes, zero responses)
  - source: ticker-1727 vip-rewards execution record 2026-11-07 1747 queue run (partial, Freebie countdown to about 18:02 not the 19:00 reset, login chest already collected, VIP13 points 1,603,930 of 2,000,000, streak 1 day; record commit 69997e12a1 on records/2026-11-07)
  - source: ticker-1734 vip-rewards execution record 2026-11-07 1812 queue run (partial, login chest claimed plus 60 points to 1,603,990, streak 2 days, Freebie unlocked about 18:02 but Claim button unresponsive to four input variants including a foreground click; record commit 840094b6ad on records/2026-11-07)
  - source: ticker-1818 VIP execution record 2026-11-07 1830 queue run (partial, chest already claimed, freebie not retried, popularity popup on the avatar-tap route)
  - source: ticker-0204 perception-scout execution record 2026-11-08 0229 queue run (partial per R1, VIP panel walked, VIP13 progress 1,605,970/2,000,000, Daily Freebie GREEN/claimable NOT claimed, Exclusive pack read; record commit 6560ff267 on records/2026-11-08)
  - source: ticker-0434 perception-scout execution record 2026-11-08 0454 queue run (done, VIP re-check, Freebie still claimable, record commit caa661bab on records/2026-11-08)
  - source: ticker-0504 perception-scout execution record 2026-11-08 0512 queue run (done, Freebie re-check, cart dot is the Store shortcut, record commit 111f7e954 on records/2026-11-08)
  - source: ticker-0534 perception-scout execution record 2026-11-08 0542 queue run (done, VIP panel re-read, Daily Freebie still claimable, cart dot absent, VIP Store full stock); record commit 707bcec0d8 on records/2026-11-08
  - source: ticker-1518 vip-rewards execution record 2026-11-09 1540 queue run (done, Daily Freebie and login chest both claimed in one pass, freebie blocker did NOT recur, plain tap at norm 759,670, VIP points 1,613,660 to 1,613,740 plus 80, freebie countdown to the 18:00 reset superseding the 24-hour-cycle correction; record commit da249faca3 on records/2026-11-09)
  - source: ticker-1424 vip-rewards execution record 2026-11-10 1438 queue run (done, Daily Freebie and login chest both claimed on first taps, VIP points 1,626,930 to 1,627,030 plus 100, streak 4 days; record commit edd4659a3 on records/2026-11-10)
  - source: ticker-1547 vip-rewards execution record 2026-11-11 1626 queue run (done, Daily Freebie and login chest both claimed in one pass, VIP points 1,634,170 to 1,634,290 plus 120, streak 5 days, freebie countdown 01:41:40, 'Alliance Gifts received!' toast twice with no claim tapped; record commit 1d0826931 on records/2026-11-11)
  - source: ticker-1504 vip-rewards execution record 2026-11-22 1522 queue run (done, Daily Freebie and login chest both claimed on first taps, VIP points 1,666,420 to 1,666,520, streak 4 days, freebie-button blocker did not recur a fourth consecutive claiming unit; record commit 06e2febac on records/2026-11-22)
---

# VIP Rewards

Read rule-digest.md first.

Claiming the daily VIP gift and VIP level rewards, one activity folder for VIP claim knowledge. This document was split verbatim into 26 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - VIP rewards to run-20261122-1522

## Changelog

- 1.22.0, 2026-11-23 - Owner name already replaced on main by the tree-wide pass (commit 0467e3ef), then split verbatim by `split_doc.py` from a 432-line, 7,430-word body into 26 key-named articles and 1 catalog pages, and added `rule-digest.md`. `--check` EQUAL against that file, body sha256 9b447516712f; the unsplit 1.21.0 file is commit 0467e3ef.
