---
title: Alliance Train
created: 2026-10-25T20:12:00Z
modified: 2026-11-23T07:42:47Z
level: L1
version: 1.45.0
description: Boarding the alliance train at the station for carriage rewards, one activity folder for train knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game Train Operation Guidelines text, read 2026-10-25
  - source: owner task request naming a train task, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1325 train unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1813 train unit)
  - source: ticker-2142 train execution record 2026-11-01 2149 queue run
  - source: ticker-0034 train execution record 2026-11-02 0044 queue run (checked only, no train read, superseded same-pass by the 0047 sighting)
  - source: ticker-0334 alliance-train execution record 2026-11-02 0348 queue run (done, checked only)
  - source: ticker-0704 alliance-train execution record 2026-11-02 0715 queue run (done, checked only)
  - source: ticker-0834 alliance-train execution record 2026-11-02 0844 queue run (done as checked only, third Secret Command Post wrong-tap instance, station empty)
  - source: ticker-1234 alliance-train execution record 2026-11-02 1246 queue run (done as checked only, station empty)
  - source: ticker-2034 alliance-train execution record 2026-11-02 2045 queue run (done, station check corrected, already aboard carriage 2)
  - source: alliance train execution record 2026-11-02 2320 queue run
  - source: ticker-0034 alliance-train execution record 2026-11-03 0035 queue run (partial, left-column mapping measured, no station view)
  - source: ticker-0304 alliance-train execution record 2026-11-03 0315 queue run (partial, 52,548 no-pan repeat, grounding mislabels Secret Command Post)
  - source: ticker-1104 alliance-train execution record 2026-11-03 1124 queue run (partial, fourth same-blocker partial today, banner absent, station not viewed, Issue 205)
  - source: ticker-1334 perception-scout execution record 2026-11-03 1345 queue run (partial, station preparation-only surface, LOOT box located on the world map)
  - source: ticker-1734 alliance-train execution record 2026-11-03 1742 queue run (partial, fifth check-only outcome today, banner absent, station not viewed)
  - source: ticker-0204 alliance-train execution record 2026-11-04 0217 queue run (partial, sixth check-only outcome in a row, banner absent, station not viewed)
  - source: ticker-0504 alliance-train execution record 2026-11-04 0509 queue run (partial, seventh check-only outcome in a row, grounding mislabel at 55,563 opened the truck screen)
  - source: ticker-0834 alliance-train execution record 2026-11-04 0839 queue run (partial, check-only, no boarding banner, no train icon, station not viewed)
  - source: ticker-1404 alliance-train execution record 2026-11-04 1404 queue run (failed, Mac screen-capture failure on every capture step, no game input dispatched, fourth consecutive ticker pass to fail this way, Chrome-window observation succeeded in the same session so the fault is specific to the Last War fullscreen window, Issue 284)
  - source: ticker-1818 alliance-train execution record 2026-11-07 1826 queue run (check-only partial, ninth in a row, no banner, station not viewed)
  - source: ticker-2134 perception-scout execution records 2026-11-07 2140/2153 queue runs (partial, station panel re-checked, third no-train confirmation in one pass, check-signals-first entry route; record commit fe5a1e7fd3 on records/2026-11-07)
  - source: ticker-2304 perception-scout execution records 2026-11-07 2311/2317 queue runs (partial, station panel re-checked, fifth no-train confirmation in one pass, Train Conductor appointments in the Record Event tab; record commit 03dc69e0c on records/2026-11-07)
  - source: ticker-0004 perception-scout execution record 2026-11-08 0022 queue run (partial, midday remainder, station panel re-checked, fourth no-train confirmation, no train preparing; record commit e6192726d1 on records/2026-11-08)
  - source: ticker-0104 perception-scout execution record 2026-11-08 0118 queue run (partial, alliance remainder station check, sixth no-train confirmation in the scout-mid-2026-10-31 chain, no train preparing; record commit 33bb20050a on records/2026-11-08)
  - source: ticker-0434 perception-scout execution record 2026-11-08 0440 queue run (partial, station re-check, both preparation signals absent, record commit caa661bab on records/2026-11-08)
  - source: ticker-0434 perception-scout execution record 2026-11-08 0447 queue run (done, alliance remainder, Train Conductor appointments, record commit caa661bab on records/2026-11-08)
  - source: ticker-2201 alliance-train execution record 2026-11-08 2211 queue run (partial, checked only, both preparation signals absent, no train preparing; record commit 8960535c on records/2026-11-08)
  - source: ticker-0204 alliance-train execution record 2026-11-09 0215 queue run (partial, checked only, both preparation signals absent, banner-only check, 37 seconds; record commit facef628c on records/2026-11-09)
  - source: ticker-0404 alliance-train execution record 2026-11-09 0421 queue run (partial, checked only, no train in preparation, both preparation signals absent; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-0134 alliance-train execution record 2026-11-10 0147 queue run (done, boarded carriage 2 of the Abyss Apex train, 3-contract gift missed on the cinematic skip double-tap; record commit e3d186a38 on records/2026-11-10)
  - source: ticker-0404 alliance-train execution record 2026-11-10 0413 queue run (done, boarded carriage 2 of the Missile Apex train, 3-contract gift missed again on the cinematic skip double-tap, second identical occurrence today; record commit 00a39c11 on records/2026-11-10)
  - source: ticker-0934 alliance-train execution record 2026-11-10 0946 queue run (partial, checked only, both preparation signals absent, no train preparing, (905,790) is not a BASE button, (59,428) locomotive label was a mislabel; record commit 226f5c37 on records/2026-11-10)
  - source: ticker-1314 alliance-train execution record 2026-11-10 1322 queue run (partial, checked only, both preparation signals absent, no train preparing, red-badge countdown icon at the right edge is a different event; record commit d781dac9d on records/2026-11-10)
  - source: "ticker-0155 alliance-train execution record 2026-11-11 0209 queue run (failed, boarding missed - plus buttons gone at platform timer 00:04:55, boarding closes about 5 minutes before departure, account not aboard, pick-order gap filed as tooling Issue #623; record commit 72b82b0e3 on records/2026-11-11)"
  - source: "ticker-1352 alliance-train execution record 2026-11-22 1356 queue run (partial, checked only, no train preparing - both preparation signals absent, 10:30 slot may already have departed, duplicate window #822 present with input staying on 127196; record commit 84e1e0ab0, landed via merged records PR #821)"
---

# Alliance Train

Read rule-digest.md first.

Boarding the alliance train at the station for carriage rewards, one activity folder for train knowledge. This document was split verbatim into 58 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Catalog 01](catalog-01.md) - Alliance train to open-questions
- [Catalog 02](catalog-02.md) - open-questions to run-20261110-1322
- [Catalog 03](catalog-03.md) - run-20261111-0209 to run-20261122-1356

## Changelog

- 1.44.0, 2026-11-23 - Split verbatim by `split_doc.py` from a 1200-line, 14493-word body into 58 key-named articles and 3 catalog pages, and added `rule-digest.md`; no word rewritten otherwise. `--verify` PASS and `--check` EQUAL against the unchanged original, body sha256 3d4579ffb151; the unsplit 1.43.0 file is commit 0467e3ef.
