---
title: Troop Training
created: 2026-10-25T20:12:00Z
modified: 2026-11-23T07:40:44Z
level: L1
version: 1.50.0
description: Training new troops in the barracks, tier by tier, one activity folder for training knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-16 (2121 training unit, ticker-2102)
  - source: owner task request naming a train task, 2026-10-25
  - source: web guides on barracks and troop tiers, read 2026-10-25
  - source: troop training execution record 2026-11-01 1216 queue run
  - source: troop training execution record 2026-11-01 1651 queue run
  - source: troop-training execution record 2026-11-01 2120 queue run (ticker-2104 unit, partial, barracks tents not located after north and south pans)
  - source: troop-training execution record 2026-11-02 0322 queue run (ticker-0308 unit, partial, pistol tap opened upgrade panel)
  - source: troop-training execution record 2026-11-02 0811 queue run (ticker-0804 unit, partial, action-row taps switched to the world map)
  - source: troop-training execution record 2026-11-02 1146 queue run (ticker-1134 unit, partial, Lv.24 batch queued, Lv.20 pistol route retired)
  - source: troop-training execution record 2026-11-02 1723 queue run (ticker-1703 unit, partial, Lv.24 panel not opened from inherited points)
  - source: troop-training execution record 2026-11-02 1949 queue run (ticker-1934 unit, partial, drag blocked by open radial)
  - source: troop training execution record 2026-11-02 2255 queue run
  - source: ticker-0234 troop-training execution record 2026-11-03 0252 queue run (partial, road drag pans, centre drag does not, no tent)
  - source: ticker-0634 troop-training execution record 2026-11-03 0647 queue run (partial, no tent in four framings, road drags pan)
  - source: ticker-1034 troop-training execution record 2026-11-03 1051 queue run (partial, three framings no tent, road drag pans where centre drag does not, Issue 150)
  - source: ticker-1534 troop-training execution record 2026-11-03 1552 queue run (partial, Lv.27 T9 batch queued and HUD-verified, tent blocker breakthrough, Issue 150)
  - source: ticker-2134 troop-training execution record 2026-11-03 2144 queue run (partial, production grid is factories not tents, 1552 point selects Factory No.3 in this framing, Issue 150)
  - source: ticker-0134 troop-training execution record 2026-11-04 0143 queue run (partial, factories confirmed again, 1552 tent point not re-tried, Tank Base Lv.28 to 29 upgrade in progress, Issue 150)
  - source: ticker-0434 troop-training execution record 2026-11-04 0440 queue run (partial, tent point 585,548 selects Barracks Lv.24, Drill Ground Full confirmed live again, Training Count +666, Issue 150)
  - source: "ticker-0804 troop-training execution record 2026-11-04 0814 queue run (partial, 0440 tent point selects Arena in this framing, Lv.20 verified via Details, framing instability measured, Drill Ground Full neither reconfirmed nor cleared, Issue #150 comment deferred)"
  - source: ticker-1134 troop-training execution record 2026-11-04 1147 queue run (partial, fullscreen framing mismatch, four grounded tent taps opened no panel, centre drag moved no view, session drop reopened, Issue 150)
  - source: ticker-1734 troop-training execution record 2026-11-04 1734 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, eleventh consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0534 troop-training execution record 2026-11-05 0534 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, thirty-fourth consecutive pass, probe classification OFF_SCREEN_WINDOW, Chrome observes normally in the same session, Issue 284)
  - source: ticker-1655 troop-training execution record 2026-11-07 1655 queue run (partial, Lv.27 T9 x726 and Lv.30 T10 x793 requeued at cap, 9.6M food plus 9.6M iron, two upper-right barracks unchecked, Drill Ground Full not seen; record commit 514e333e5b on records/2026-11-07)
  - source: ticker-2006 troop-training execution record 2026-11-07 2026 queue run (partial, Lv.27 verified busy 1d 07:03:33 by panel read, Lv.30 busy by timer bubble only, two upper-right barracks unlocated, south and east pans ruled out; record commit e9bf320c92 on records/2026-11-07)
  - source: ticker-2034 troop-training execution record 2026-11-07 2050 queue run (partial, Lv.30 busy T10 x793 1d 13:41:04, Lv.24 idle but blocked by Drill Ground Full toast, Drill Ground Lv.25 read live Unit Count +7812 Officers Joe/Marcus/Karen/John Quick Dispatch present not tapped, tent-body taps missed twice, no_change_observed flag unreliable; record commit 7a4a104930 on records/2026-11-07)
  - source: ticker-1317 troop-training execution record 2026-11-08 1350 queue run (partial, Lv.30 barracks re-verified busy, Lv.10 batch 793 with 20:47:28 left, tent tap (459,457) opens TRAIN UNITS directly, tent tap (564,510) misses, no batch queued; record commit d272dd711 on records/2026-11-08)
  - source: ticker-2058 troop-training execution record 2026-11-08 2119 queue run (partial, Lv.27 busy, Lv.20 Drill Ground Full re-confirmed live, paw Details route works, long-press retired, T9 stats corrected; record commit 023fb42b6 on records/2026-11-08)
  - source: ticker-0019 troop-training execution record 2026-11-09 0039 queue run (partial, Drill Ground Lv.30 read live, Unit Count +10080, officers Samantha/William/Chloe/Catherine, Quick Dispatch not tapped, fenced structure resolves to Aircraft Center Lv.29, no barracks verified; record commit f99faa9744 on records/2026-11-09)
  - source: ticker-0034 arms-race execution record 2026-11-09 0058 queue run (partial, Unit Progression phase read live 0 points, Events entry (672,132), orange medal is Wall of Honor, back arrow centre (355,944), fill not executed, barracks state carried forward; record commit 77db994162 on records/2026-11-09)
  - source: ticker-0113 arms-race execution record 2026-11-09 0129 queue run (partial, Unit Progression phase read live again 0 points, third consecutive tent-grounding failure, red troop formation resolves to Drill Ground Lv.30, entry route must change, phase ends about 02:00; record commit c0ebf0c4f0 on records/2026-11-09)
  - source: ticker-0404 troop-training execution record 2026-11-09 0413 queue run (partial, fullscreen zoom-out variant tried, no barracks tent verified, View-menu fullscreen exit measured; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-1304 troop-training execution record 2026-11-09 1330 queue run (partial, Lv.27 idle and blocked by Drill Ground Full, tents grounded by a fresh route, blue-roofed tents are Material Workshops; record commit 5108be8d7 on records/2026-11-09)
  - source: ticker-2040 troop-training execution record 2026-11-09 2103 queue run (partial, barracks tent tap no-change x3, no TRAIN UNITS panel, Drill Ground not read, next unit must change entry route per R2; record commit ca96fa0c9 on records/2026-11-09)
  - source: ticker-0034 troop-training execution record 2026-11-10 0034 queue run (partial, formation-yard taps resolve to squads and the Wall, Drill Ground selection route does not reproduce; record commit d3c648601 on records/2026-11-10)
  - source: ticker-0334 troop-training execution record 2026-11-10 0337 queue run (partial, fourth consecutive training partial with the same blocker, R2 process failure, wide-zoom and panned-down tent taps select nothing, Duel screen live read UR truck dispatch +300,000; record commit b7e79a62 on records/2026-11-10)
  - source: ticker-0834 troop-training execution record 2026-11-10 0850 queue run (partial, fifth consecutive training partial, R2 process failure, game found on TECH screen by unexplained navigation, slot-1 timer discrepancy, no barracks requeued; record commit 5473d6845 on records/2026-11-10)
  - source: ticker-1204 troop-training execution record 2026-11-10 1229 queue run (partial, Lv.24 requeued T8 x666 verified running, Drill Ground Full did not block it, R2 five-partial run broken, T8/T10 stats corrected live; record commit 88e51ae5d on records/2026-11-10)
  - source: ticker-1634 troop-training execution record 2026-11-10 1649 queue run (partial, verified no, no barracks tent located after three camera pans, blind-pan method retired under R2, Lv.24 T8 batch still running to about 2026-11-11 16:49; record commit 986c1877 on records/2026-11-10)
  - source: ticker-1503 perception-scout execution record 2026-11-10 1521 queue run (partial, Drill Ground level-up to Lv.27 live, upgrade to Lv.28 available with costs met, not started; record commit f530c19b7 on records/2026-11-10)
  - source: ticker-2122 troop-training execution record 2026-11-10 2146 queue run (partial, Lv.27 finished batch of 313 Lv.9 collected, power +423,176, requeue blocked by Drill Ground Full live toast, tents re-grounded fresh, 1229 point stale for current framing; record commit ccb00e883 on records/2026-11-10)
  - source: ticker-0155 troop-training execution record 2026-11-11 0213 queue run (partial, Lv.30 pistol x2 and paw x1 close the button row with no panel, Drill Ground screen still not read live, fourth consecutive unit on the same blocker, changed entry route needed; record commit 72b82b0e3 on records/2026-11-11)
  - source: ticker-0534 troop-training execution record 2026-11-11 0548 queue run (partial, Lv.24 barracks busy 11:01:26, 1 of 4 checked, radar-entrance wrong turn, Drill Ground live read not done, duration corrected to about 4 minutes; record commit a3ef6b276 on records/2026-11-11)
  - source: ticker-1332 troop-training execution record 2026-11-11 1340 queue run (partial, 0 of 4 barracks checked, tent grounding missed again, Drill Ground tap landed on Iron Mine Lv.27, radar-map exit by back arrow, Home button unresponsive in the fullscreen framing; record commit ed2cb2614 on records/2026-11-11)
  - source: "ticker-2133 troop-training execution record 2026-11-11 2136 queue run (partial, Lv.27 idle, requeue blocked by Drill Ground Full live toast, Building Details route tried - no Drill Ground link, yard tap opened Alliance mail, duration corrected to 603 seconds, Issue #678 filed; record commit bca5a948c on records/2026-11-11)"
  - source: "ticker-1318 troop-training execution record 2026-11-21 1340 queue run (partial, Drill Ground still unlocated, portrait tent is not a barracks, view cannot be panned, Issue #678; record commit 9418b215a4 on records/2026-11-21)"
  - source: "ticker-2104 troop-training execution record 2026-11-21 2124 queue run (partial, Lv.27 selected live, pistol deliberately not tapped, formation-flag tap selects 2nd Squad Lv.20, fifth consecutive partial, Issue #678; record commit e1d4f7c05 on records/2026-11-21)"
  - source: ticker-0134 troop-training execution record 2026-11-22 0134 queue run (partial, Lv.27 requeued T9 x726, Drill Ground Full blocker did not reproduce, Lv.30 Details Training Count +793, button-row tap-precision lesson; record commit 0028b8f92 on records/2026-11-22)
  - source: ticker-0957 troop-training execution record 2026-11-22 0958 queue run (partial, Lv.30 requeued T10 x793 verified by exact food delta, T10 stats corrected live 38.87/7.87, Drill Ground Full did not block; record commit e859f4993 on records/2026-11-22)
  - source: ticker-0957 arms-race execution record 2026-11-22 1005 queue run (partial, Lv.24 finished batch of 143 Lv.8 collected, power +152,009, recorded as observed not reconciled; record commit e859f4993 on records/2026-11-22)
---

# Troop Training

Read rule-digest.md first.

Training new troops in the barracks, tier by tier, one activity folder for training knowledge. This document was split verbatim into 111 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - Troop training to run-20261102-0811
- [Catalog 02](catalog-02.md) - run-20261102-1146 to run-20261104-1147
- [Catalog 03](catalog-03.md) - run-20261104-1734 to run-20261110-0337
- [Catalog 04](catalog-04.md) - run-20261110-0337 to run-20261122-0134
- [Catalog 05](catalog-05.md) - run-20261122-0958 to run-20261122-1005

## Changelog

- 1.49.0, 2026-11-23 - Split verbatim by `split_doc.py` from a 1624-line, 33,393-word body into 111 key-named articles and 5 catalog pages, and added `rule-digest.md`; no word rewritten, no claim superseded. `--verify` PASS and `--check` EQUAL, body sha256 c124a73d51fb; the unsplit 1.48.0 file is commit 11d23ccf.
