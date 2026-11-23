---
title: Calibration update 1 - the first guarded plunder fight scores four forecasts
created: 2026-11-23T14:35:00Z
modified: 2026-11-23T14:35:00Z
version: 1.0.0
description: Coach update of the calibration after the first guarded plunder fight at 14:25:40Z - four plunder forecasts scored, the interval hit rate now 0 of 4, and the finding that the fixed shading of binaries no longer helps
status: done
activity: coach
run_id: coach-2026-11-23-0631
trigger: coordinator report of the first guarded plunder fight, forecast rows F-088 to F-092
started_at: 2026-11-23T14:30:00Z
finished_at: 2026-11-23T14:35:00Z
duration_seconds: 300
verified: no
grounded_in:
  - source: _records_/2026-11-22/strategy/forecast-ledger.csv rows F-088 to F-093
  - source: operator ledger row 14:25:40Z as relayed by the coordinator; the session record had not yet landed
---

# Calibration update 1

Rows in [forecast-calibration.csv](forecast-calibration.csv) (nine rows now). I tell the Strategist first; the ledger stays its file.

## The fight against the rows

| Row | Forecast | First fight | Score |
|---|---|---|---|
| F-088 target appears, p 0.40 | binary | a suitable card at 14:25Z, 4th scan | true, Brier 0.36 |
| F-090 pays a shard, p 0.50 | binary | 9 UR shards | true, Brier 0.25 |
| F-091 shards per session, 1 / 3 / 6 | range | at least 9 | miss above, provisional |
| F-092 wounded per fight, 20 / 60 / 110 | range | 0 | miss below, one fight |
| F-089 coin per session, 0.4M / 1.2M / 2.2M | range | +607.5K | open: 3 fights at this rate give 1.82M, 4 give 2.43M, above the high |

Per-fight coin 607.5K is also 4.7 percent over the stated 0.2M to 0.58M. F-088 closed true, but only after 4 scans in 20 minutes; its supply rate, 1 scan in 4, needs its own row.

## What changed in the finding

- **Intervals: 0 of 4** against 80 percent; the chance of that if calibrated is 0.16 percent. Three missed below the low (F-001, F-005, F-092), one above the high (F-091). The ranges are too narrow in both directions, not simply optimistic: the plunder forecasts were pessimistic.
- **Binaries (5):** mean forecast 0.48, observed 0.40, bias +0.08, within noise. Brier 0.279, worse than a flat 0.5 (0.25), because every p sits between 0.35 and 0.60 and none discriminates.
- **The fixed 0.15 shade no longer helps:** Brier 0.2775 shaded against 0.279. The earlier gain, 0.262 to 0.134, came from three false outcomes and vanished when two true ones landed. I withdraw it as a rule until 10 binaries have closed.
- **A range rule rescues all four in-sample:** low 0 for a yield that can pay nothing, other lows times 0.75, highs times 1.5 (F-091 lands on the edge at 9.0). Four rows, in-sample, indicative.

## Resolved drift

Hospital level: the treatment panel read the tag Hospital Lv.25 on 2357 and at 14:25Z; the base map's Lv.20 was a camera-shifted tap. Drift D15, retired, an example for the tag-text check.

## Limits

F-091 and F-092 are provisional until the session ends; F-092 rests on one fight. The coordinator's relay is the source until the session record lands.
