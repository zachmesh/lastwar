---
title: Mail Rewards
created: 2026-10-25T18:58:00Z
modified: 2026-11-23T07:42:51Z
level: L1
version: 1.44.0
description: Claiming reward mail and checking report mail, one activity folder for mail knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1306 mail unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1730 mail unit)
  - source: mail-rewards execution record 2026-11-01 2131 queue run (ticker-2104 unit, partial, Alliance-panel back arrow stalled on background input)
  - source: ticker-0034 mail-rewards execution record 2026-11-02 0042 queue run
  - source: ticker-0334 mail-rewards execution record 2026-11-02 0343 queue run (done, System 50 diamonds)
  - source: ticker-0834 mail-rewards execution record 2026-11-02 0840 queue run (done, all claimable categories answered No rewards available)
  - source: mail-rewards execution record 2026-11-02 1226 queue run (ticker-1204 unit, done, all categories swept, no reward available)
  - source: mail-rewards execution record 2026-11-02 2012 queue run (ticker-2004 unit, done, 7 mails claimed)
  - source: mail rewards execution record 2026-11-02 2313 queue run
  - source: ticker-0304 mail-rewards execution record 2026-11-03 0312 queue run (done, all categories empty, Escape crash recurrence)
  - source: ticker-0704 mail-rewards execution record 2026-11-03 0715 queue run (done, six categories swept, all answered No rewards available)
  - source: ticker-1034 mail-rewards execution record 2026-11-03 1055 queue run (partial, mail entry mis-targeted to Alliance twice then no-change, Issue 230)
  - source: ticker-1734 mail-rewards execution record 2026-11-03 1740 queue run (done, R2 fresh grounding opens Mail first try, Alliance Exercise claim, red dot is unread not claimable)
  - source: ticker-0204 mail-rewards execution record 2026-11-04 0212 queue run (done, Alliance claim verified by checkmarks, Regular notices already credited, notifications prompt declined, Issue 230)
  - source: ticker-0434 mail-rewards execution record 2026-11-04 0445 queue run (done, category rows grounded, Event train arrival reward claimed and verified gone)
  - source: ticker-0804 mail-rewards execution record 2026-11-04 0817 queue run (done, checked only, Claim All no-change in four categories, Event notice opened individually, no claimable mail)
  - source: ticker-1327 mail-rewards execution record 2026-11-04 1333 queue run (failed, Mac screen-capture channel failure on every capture step, no game input dispatched, second consecutive ticker pass to fail this way after help 1235, Issue 282)
  - source: ticker-0134 survivor-intake execution record 2026-11-05 0134 queue run and ticker-0204 alliance-gifts execution record 2026-11-05 0204 queue run (windowed 1920x1080 on an inactive Space, not native fullscreen - corrects the 1333 section wording)
  - source: ticker-1025 mail-rewards execution record 2026-11-05 1025 queue run (failed, Mac device offline, forty-second consecutive pass, zero-response form, Issue 284)
  - source: ticker-1804 mail-rewards execution record 2026-11-05 1804 queue run (failed, Mac device offline, fifty-seventh consecutive ticker pass with a Mac device-access blocker, eighteenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 10h30m, unchanged since the 1025 pass; seven invokes, zero responses)
  - source: ticker-1727 mail-rewards execution record 2026-11-07 1740 queue run (done, all six claimable categories checked, nothing claimable; record commit 69997e12a1 on records/2026-11-07)
  - source: ticker-2006 mail-rewards execution record 2026-11-07 2028 queue run (done, Alliance Daily Donation Rankings and 3 Event mails claimed, other categories clear by list read, verified clean after claims; record commit e9bf320c92 on records/2026-11-07)
  - source: ticker-2034 mail-rewards execution record 2026-11-07 2052 queue run (done, Alliance and Event Claim All answered "No rewards available", nothing claimed, envelope grounded at norm 936,790, "Unclaimed -Daily Task- Reward" is notification-only; record commit 7a4a104930 on records/2026-11-07)
  - source: ticker-2119 mail-rewards execution record 2026-11-08 2132 queue run (done, Alliance and Event mail claimed in full, 10 mails, Claim All both categories; record commit fe08a0907 on records/2026-11-08)
  - source: ticker-0113 mail-rewards execution record 2026-11-09 0138 queue run (partial, Alliance and Event Claim All both "No rewards available", System/Regular/Battle Report not walked, leader row Jerry Apex read live on the Alliance page, Mail button flaky entry (652,793), VIP daily freebie flag; record commit c0ebf0c4f0 on records/2026-11-09)
  - source: ticker-0404 mail-rewards execution record 2026-11-09 0421 queue run (done, all three red-dot categories walked, no claimable attachments, envelope opened at once with no Alliance-first workaround; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-1004 mail-rewards execution record 2026-11-09 1031 queue run (partial, Event and Alliance Claim All both "No rewards available", six train mails carry no attachments, Battle Report/System/Regular not walked, Mail entry (932,791) windowed first try; record commit 09e4f0863 on records/2026-11-09)
  - source: zero-sweep 001 execution record 2026-11-09 1657 queue run (partial, Mail red dot standing, three categories unopened; record commit c9a86fa74 on records/2026-11-09)
  - source: ticker-1822 mail-rewards execution record 2026-11-09 1838 queue run (done, 9 reward mails claimed, Alliance Event System Claim All, leadership transfer to Abyss Apex, Issue 230 entry datapoint, power 146736949; record commit 6761c35d1 on records/2026-11-09)
  - source: ticker-0134 mail-rewards execution record 2026-11-10 0143 queue run (done, Claim All sweep, no claimable rewards, Weekly Pass mail verified already claimed; record commit e3d186a38 on records/2026-11-10)
  - source: ticker-0334 mail-rewards execution record 2026-11-10 0355 queue run (done, Claim All sweep, no claimable rewards, R5 warning mail read; record commit b7e79a62 on records/2026-11-10)
  - source: "ticker-0904 mail-rewards execution record 2026-11-10 0929 queue run (partial, entry blocked by camera framing, Mail panel never opened, fourth unit this reset day with the same blocker, Issue #580; record commit 31892dde on records/2026-11-10)"
  - source: ticker-1234 mail-rewards execution record 2026-11-10 1259 queue run (done, Event train rewards claimed in full, mail-list back arrow re-grounded at norm 62,948; record commit 98abbc761 on records/2026-11-10)
  - source: ticker-0212 mail-rewards execution record 2026-11-11 0222 queue run (done, Alliance Daily Donation Rankings and Event Arms Race rewards claimed, both lists verified empty of gift icons; record commit b0615980f on records/2026-11-11)
  - source: ticker-1012 mail-rewards execution record 2026-11-11 1029 queue run (done, every category walked, Event Zombie Invasion Intel + train mails and System Maintenance + Survey claimed, HUD deltas verify coin/food/diamonds exactly, normalized-coordinates correction; record commit c0c788be on records/2026-11-11)
  - source: ticker-1408 mail-rewards execution record 2026-11-11 1422 queue run (partial, Event Claim All paid medal 280, EXP 2.4M, Battle Data 1.5K, 10-stamina x2, coin 969.0K, food 769.0K, iron 769.0K, other categories unchecked, tap offset measured; record commit d00afba5a on records/2026-11-11)
  - source: ticker-1439 zombie-invasion execution record 2026-11-11 1456 queue run (partial, Glacieradon chain 016, mail already claimed by the 1422 mail unit, Claim All auto-advance to the next unread mail, mail-detail back arrow offset-miss with re-test owed; record commit 34be97f28 on records/2026-11-11)
  - source: ticker-2133 troop-training execution record 2026-11-11 2136 queue run (partial, training unit's mail detour - President Mail 2110 Honoring Our Veterans read live, three unread President Mail, Alliance and Event gift icons unclaimed, nothing claimed; record commit bca5a948c on records/2026-11-11)
  - source: "ticker-0604 mail-rewards execution record 2026-11-22 0619 queue run (done, full sweep, all categories Claim All answered \"No rewards available\", nothing claimed, Zombie Siege reports 2d old corroborate Issue #814, TIPS popup on Mail close dismissed with Cancel; record commit 717f9fd92 on main)"
---

# Mail Rewards

Read rule-digest.md first.

Claiming reward mail and checking report mail, one activity folder for mail knowledge. This document was split verbatim into 57 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - Mail rewards to day-20261105
- [Catalog 02](catalog-02.md) - run-20261105-1025 to run-20261111-1422
- [Catalog 03](catalog-03.md) - run-20261111-1456 to run-20261122-0619

## Changelog

- 1.43.0, 2026-11-23 - Split verbatim by `split_doc.py` from a 1,058-line, 15,530-word body into 57 key-named articles and 3 catalog pages, and added `rule-digest.md`; no word rewritten. `--verify` PASS and `--check` EQUAL against the original, body sha256 08dc639f1dff; the unsplit 1.42.0 file is commit 0467e3ef.
