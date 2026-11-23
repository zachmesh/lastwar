---
title: Truck Plunder
created: 2026-10-25T20:12:00Z
modified: 2026-11-23T15:33:54Z
level: L1
version: 1.48.0
description: Intercity Trade trucks, dispatching own trucks and plundering the trucks of others, one activity folder for trade knowledge
status: unverified
grounded_in:
  - source: operator plunder fights _records_/2026-11-22/truck-plunder/1405-queue-run.md (fight 1) and _records_/2026-11-22/truck-plunder/1523-queue-run.md (fight 2, the left-half experiment), 2026-11-23
  - source: owner decision OD-20261123-20, trade truck plunder re-enabled with a casualty guard (_records_/retro/owner-decisions-log/od-20261123-20.md)
  - source: coach numbers line _records_/2026-11-22/coach/playbook-numbers-lines.csv and hospital finding _records_/2026-11-22/coach/2400-hospital-finding.md
  - source: plunder fight records _records_/2026-10-27/truck-plunder/1857-segment-3-run.md and _records_/2026-10-31/truck-plunder/0404-queue-run.md, entry and dispatch records _records_/2026-11-22/truck-plunder/0958-queue-run.md and _records_/2026-11-22/truck-plunder/2058-queue-run.md
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming a plunder and truck task, 2026-10-25
  - source: web guides on Intercity Trade and trade trucks, read 2026-10-25
  - source: owner teach-in on plunder target selection and dispatch rules, evening of 2026-10-25
  - source: evening dispatch and plunder executions on the new server day, 2026-10-25
  - source: owner standing rule on non-UR day dispatch - SR or above only, ticket refreshes authorized until reached, 2026-10-26
  - source: owner rule on daily truck quotas - dispatch 5 and plunder 4 every trade day, note it in the metadata and resolve misses, 2026-10-30
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1053 trucks unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1352 trucks unit)
  - source: incidental trucks-view read in the alliance-train execution record 2026-11-01 1813 queue run (not a trucks unit)
  - source: daily retro 2026-11-01, trucks 1457 expiry and counter tension (issues 147 and 148)
  - source: ticker-2212 trucks execution record 2026-11-01 2231 queue run
  - source: ticker-0104 truck-plunder execution record 2026-11-02 0114 queue run (partial, trade-screen entry blocker)
  - source: ticker-0404 truck-plunder execution record 2026-11-02 0416 queue run (partial, trade entry corrected)
  - source: ticker-0934 truck-plunder execution record 2026-11-02 0935 queue run (partial, dispatch quota filled, plunder shortfall 2 remains)
  - source: ticker-1307 truck-plunder execution record 2026-11-02 1325 queue run (partial, leftmost shard stack x3 pays in full, plunder shortfall 1 remains)
  - source: ticker-2104 truck-plunder execution record 2026-11-02 2120 queue run (partial, station-tap entry, counters 4/5 and 4/4, fifth dispatch shortfall)
  - source: ticker-2334 truck-plunder execution record 2026-11-02 2347 queue run (partial, station-tap entry failed, counters not read)
  - source: ticker-0334 truck-plunder execution record 2026-11-03 0344 queue run (partial, station-tap entry failed again, grounding mislabels Furnace and Wall)
  - source: ticker-0334 secret-missions execution record 2026-11-03 0346 queue run (done, unsnapped exact-centre entry lesson; incidental live trade counters 4/5)
  - source: ticker-1204 truck-plunder execution record 2026-11-03 1211 queue run (done, trade quota 5 of 5 and plunder quota 4 of 4 full, UR dispatched as rolled)
  - source: "ticker-1834 truck-plunder execution record 2026-11-03 1846 queue run (partial, new trade day 0 of 5 and 0 of 4 at 18:34 entry, 3 dispatches, 2 plunders, trade counters reset with the about-18:00 rollover, Issue #242 follow-up)"
  - source: ticker-0234 truck-plunder execution record 2026-11-04 0242 queue run (done, quotas full at entry, WORLD-corner entry route)
  - source: ticker-0534 truck-plunder execution record 2026-11-04 0538 queue run (done, quotas full at entry, badged vehicle icon entry, WORLD-corner route qualified)
  - source: ticker-0834 truck-plunder execution record 2026-11-04 0845 queue run (done, quotas full 5/5 and 4/4 at entry, trade-icon grounding mislabel opens Secret Command Post)
  - source: pre-reset zero sweep execution record 2026-11-07 1824 queue run (first pass, trucks line 18 unverified, both R3 checkpoints passed with the counts unread; record commit 840094b6ad on records/2026-11-07)
  - source: ticker-0404 perception-scout execution record 2026-11-08 0415 queue run (partial, alliance remainder, Trucks panel reached by entry tap)
  - source: ticker-0504 perception-scout execution record 2026-11-08 0512 queue run (done, bus icon tap-verified Trucks, dot clears on open, record commit 111f7e954 on records/2026-11-08)
  - source: ticker-0534 perception-scout execution record 2026-11-08 0542 queue run (done, blue truck/bus icon is Trucks, 0/5 trades, 4 own + 4 others waiting, 0022 white-truck mapping corrected); record commit 707bcec0d8 on records/2026-11-08
  - source: ticker-0534 truck-plunder execution record 2026-11-09 0541 queue run (partial, trade entry blocked in current column set, both methods failed, WORLD-corner route re-confirms the 0538 correction, counters not re-read, shortfall carried 4/5 and 1/4; record commit a9b838c5ed on records/2026-11-09)
  - source: zero-sweep 002 execution record 2026-11-09 1748 queue run (partial, 5 of 23 ledger lines read live, trucks 4/5 dispatch 1/4 plunder live, trade entry route measured in the current icon set; record commit 2f4d783d8 on records/2026-11-09)
  - source: ticker-1910 sync record 2026-11-09 (trucks-2026-11-09-1457 fix-up expired unrun, window passed before execution, reaped 19:14 in the ticker-1910 pass; record commit e05c662bd on records/2026-11-09)
  - source: ticker-2230 truck-plunder execution record 2026-11-09 2250 queue run (partial, 4 returned trucks settled 2 UR + 2 SR, 2026-11-9 18:00 Reward Recovery claimed, Trade Count 0/5 on the new trade day, dispatch 5 UR and plunder 4 fall to the next unit; record commit 70248cbb7 on records/2026-11-09)
  - source: ticker-0234 truck-plunder execution record 2026-11-10 0248 queue run (partial, first Mega Mode execution end to end on a UR day, 4 UR dispatched, 1 plunder won, Trade Count 4/5, Plunder Count 1/4; record commit 2802653981 on records/2026-11-10)
  - source: ticker-0504 truck-plunder execution record 2026-11-10 0513 queue run (partial, Reward Recovery 2026-11-7 record claimed, 1 SSR plunder won, Trade Count 4/5, Plunder Count 2/4; record commit 19608e2c9e on records/2026-11-10)
  - source: ticker-0334 troop-training execution record 2026-11-10 0337 queue run (partial, Duel screen read live inside the training unit - Dispatch UR Trade Truck +300,000, Perform 1 UR Secret Task +225,000, superseding the 100,000 Handbook rate; record commit b7e79a62 on records/2026-11-10)
  - source: ticker-1343 truck-plunder execution record 2026-11-10 1411 queue run (partial, all 4 returned UR trucks settled HUD-verified, Trade Count 4/5, Plunder Count not re-read, 5th dispatch and plunders resume next unit; record commit b2c2b7a43 on records/2026-11-10)
  - source: ticker-0637 truck-plunder execution record 2026-11-11 0701 queue run (partial, 1 UR truck dispatched by contract refresh, Trade Count 1/5, Plunder Count 0/4, dice label 148/1 to 145/1 unread, Recover red dot waiting, top left-column icon entry; record commit f8ee03b36 on records/2026-11-11)
  - source: ticker-0234 truck-plunder execution record 2026-11-22 0252 queue run (partial, trade screen never opened, no blue truck-front icon in the 763x1050 column set, bottom yellow/red icon (40,819) panned the map, counters unread - last live reads 2026-11-11 11 days stale; record commit c5c9b88d6 on delivery branch ticker-0234-records-1122, not on main - provenance noted)
  - source: "2026-11-10 daily retro, execution-knowledge action A-2026-11-10-01 (Issue #300): never write an expected or Handbook-rate score into stats.points; points holds live-read scored gains only"
---

# Truck plunder playbook card

Goal: dispatch and plunder trade trucks within the casualty guard.

## Route

1. Open Intercity Trade by its icon (R4).
2. Settle returned trucks; claim Reward Recovery (R5).
3. Dispatch own trucks.
4. Read the hospital before the first fight.
5. Others' Trucks: pick a truck by R2.
6. Fight; record troops wounded, coin and shards.
7. Stop on the guard or at 4 of 4.
8. After a camera shift: WORLD then BASE, or tap (310,660), never (400,640), a Barracks (2026-11-23).

## Rules

- R1 Trade truck plunder is on (owner override OD-20261123-20); Arena, gold-trophy fights, rallies, General's Trial and base attacks stay forbidden. Status: tested. 2026-11-23. `_records_/retro/owner-decisions-log/od-20261123-20.md`
- R2 Plunder UR or SSR trucks with a UR 500-badge stack in either half, guard under Squad 1 (25.61M), arrival over 30 minutes. Status: tested. 2026-11-23. `_records_/2026-11-22/truck-plunder/1523-queue-run.md`
- R3 Casualty guard: read the hospital before each session; stop if free room falls under 1,000 or two fights in a row wound over 100 troops. Status: unverified. 2026-11-23. `_records_/retro/owner-decisions-log/od-20261123-20.md`
- R4 Find the trade icon by glyph and badge each unit; verify the screen that opened. Status: tested. 2026-11-22. `_records_/2026-11-22/truck-plunder/0958-queue-run.md`
- R5 Claim Reward Recovery at the red dot. Status: verified. 2026-11-22. `_records_/2026-11-22/truck-plunder/2058-queue-run.md`

## Failures

- Icon opens the train station - fix: re-find the icon; verify the screen. `_records_/2026-11-22/truck-plunder/0958-queue-run.md`
- Step cap before any dispatch - fix: continue in a second run. `_records_/2026-11-22/truck-plunder/2058-queue-run.md`

## Open questions

- Does slot position change the shards won? Test: log stack slots and shards per fight; run by operator.
- Does free room fall by the wounded count? Test: read the hospital before and after a fight; run by researcher.

## Numbers

Numbers, 7 days to 2026-11-23: 1 units; done 0%; done-or-by-design 100%; partial 1, failed 0; mean steps 8 (1 of 1 report it); top blocker h by-design partial (1 of 1 non-done).

## Links

- [Rule digest](rule-digest.md)
- [All catalogs](article-catalogs.md)
- [Hospital finding](../../_records_/2026-11-22/coach/2400-hospital-finding.md)
