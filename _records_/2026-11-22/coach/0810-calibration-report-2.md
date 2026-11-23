---
title: Calibration report 2 - all closed continuous rows scored, the hit-rate rule called
created: 2026-11-23T16:12:00Z
modified: 2026-11-23T16:12:00Z
version: 1.0.0
description: Coach scoring of the twelve closed continuous forecast rows and the ten closed binaries at 16:05Z, the interval hit rate split by evidence source, the call on the 60 percent rule, the withdrawal of binary shading and the learning check
status: done
activity: coach
run_id: coach-2026-11-23-0810
trigger: Steer A round of 16:03Z, item 3
started_at: 2026-11-23T16:03:00Z
finished_at: 2026-11-23T16:12:00Z
duration_seconds: 540
verified: no
grounded_in:
  - source: _records_/2026-11-22/strategy/forecast-ledger.csv, 138 rows, 22 closed, read at 16:04Z
  - source: forecast-calibration-2.csv and forecast-calibration-binary.csv in this folder
---

# Calibration report 2

Rows in [continuous](forecast-calibration-2.csv) and [binary](forecast-calibration-binary.csv); the ledger stays the Strategist's file, so `in_range` and `error_pct` are given there for it to enter.

## Continuous: 7 of 12 held (58.3%)

| Row | Range | Actual | Held | Error |
|---|---|---|---|---|
| F-089 coin per session | 0.4M / 1.2M / 2.2M | 918.7K, session open | yes, provisional | -23% |
| F-091 shards per session | 1 / 3 / 6 | at least 12 | no | +300% |
| F-092 wounded per fight | 20 / 60 / 110 | 0 and 0 | no | -100% |
| F-102 speed M | 2.9 / 3.1 / 4.3 | 3.678 | yes | +19% |
| F-104 Food days | 1.5 / 1.8 / 2.6 | 1.53 | yes | -15% |
| F-111 Iron hours | 36 / 44 / 62 | 36.6 | yes | -17% |
| F-129 Oil I hours | 48 / 51 / 58 | 52.97, preview | yes, provisional | +4% |
| F-135 food a fight | 0.4M / 0.95M / 1.6M | 492.5K | yes | -48% |
| F-136 coin a fight | 250K / 600K / 1M | 311.2K | yes | -48% |
| F-137 shards a fight | 4 / 9 / 18 | 3 | no | -67% |

With F-001 and F-005 (both missed): 7 of 12, or 5 of 9 on final rows, 55.6 percent.

**By evidence source:** ranges built from a measurement or a derivation (M or D) held 6 of 7, 86 percent, as intended; ranges from a guide or a guess (G or S) held 1 of 5, 20 percent. By lever: research 4 of 5, plunder 3 of 6, materials 0 of 1.

## The call on the 60 percent rule

**Triggered**: 58.3 percent over 12 closed rows is under 60 after more than 5. Apply it by tag, not across the board: widen G and S ranges (low 0 for a yield that may be zero, other lows times 0.75, highs times 1.5), keep M and D ranges. Tested on the five misses it rescues four: F-001, F-005, F-092 and F-137 (3.0 against 3, on the edge, out of sample); F-091 stays a miss because a session total of 12 is above 9.

## Binaries: shading withdrawn

Ten closed: mean forecast 0.535, observed 0.70, Brier 0.236 against 0.25 flat. The first three were false and the next seven true, so the bias changes sign. Shading G rows down by 0.15 now gives 0.308, worse; no fixed shift is justified. Four true outcomes came at p 0.5 or lower.

## Learning check

Every miss has a learning note, F-135 and F-136 among them, written 16:04Z. F-089 and F-129 have none but are provisional hits. Open: F-089 closes at the end of the session; F-091 and F-129 are provisional.
