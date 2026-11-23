---
title: Execution records for coach on 2026-11-22
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T10:58:00Z
version: 1.0.0
description: Execution records for coach on 2026-11-22, one file per run, with the CSV sidecars the runs cite; the day index lists the runs.
---

# coach records, 2026-11-22

Execution records for coach on 2026-11-22, one file per run, with the CSV
sidecars the runs cite.

## Runs

- [2346-growth-baseline.md](2346-growth-baseline.md) - Story 871, the Total
  Power series, net and daily-maximum pace, the 2026-11-09 outlier, the gain
  ledger and the weekly tracking template.
- [2350-daily-measurement.md](2350-daily-measurement.md) - the first daily
  measurement report after the restart.
- [2354-category-baseline.md](2354-category-baseline.md) - gain per day by
  category against 2026-11-08, recorded versus unattributed, misses, resources.
- [2358-fall-analysis.md](2358-fall-analysis.md) - the 2026-11-09 drop, the
  whole-troop-unit finding, the event reconstruction and the collect-first rule.
- [2359-coin-trace.md](2359-coin-trace.md) - where the coin went.
- [2400-hospital-finding.md](2400-hospital-finding.md) - healed troops waiting behind the Drill Ground cap.
- [0035-conformance-report-1.md](0035-conformance-report-1.md) - the six conformance KPIs and the drift list, first report.
- [0055-run-articles-audit.md](0055-run-articles-audit.md) - audit of the 1,767 run articles against the records.
- [0119-playbook-baselines.md](0119-playbook-baselines.md) - playbook quality baselines, pilot numbers lines, rotation.
- [0125-numbers-line-format.md](0125-numbers-line-format.md) - the fixed numbers line, the ranking rule and the stat names.
- [0255-tag-text-check.md](0255-tag-text-check.md) - the building-read tag text check and its baseline.
- [0236-donations-count.md](0236-donations-count.md) - the donations units counted by policy 2532 and the witnessed tap totals.
- [0145-cross-activity-review.md](0145-cross-activity-review.md) - review of the 100 cross-activity duplicate rows, the 14 not to mark, the donation 1/30 evidence.

## Sidecars

- [total-power-series.csv](total-power-series.csv) - 53 distinct readings.
- [power-gain-ledger.csv](power-gain-ledger.csv) - 18 measured gain rows.
- [power-by-category.csv](power-by-category.csv) - the 2026-11-08 and 2026-11-22 breakdowns.
- [weekly-tracking.csv](weekly-tracking.csv) - W1 to W5 baseline, W6 blank.
- [fixed-state-readings.csv](fixed-state-readings.csv) - slots A and B.
- [misses-log.csv](misses-log.csv) - idle-slot reads on 2026-11-22.
- [resource-deltas.csv](resource-deltas.csv) - food, iron and coin between the two snapshots.
- [troop-events.csv](troop-events.csv) - queues, collections, heal and capacity events.
- [power-dips.csv](power-dips.csv) - steps of 100,000 or more and the whole-unit test.
- [candidate-causes.csv](candidate-causes.csv) - eight candidates, evidence, test, status.
- [coin-series.csv](coin-series.csv) and [coin-windows.csv](coin-windows.csv) - coin reads and spend windows.
- [conformance-kpis.csv](conformance-kpis.csv), [conformance-units.csv](conformance-units.csv), [slot-idle-minutes.csv](slot-idle-minutes.csv), [plan-triggers.csv](plan-triggers.csv) and [drift-list.csv](drift-list.csv) - the conformance loop data.
- [run-articles-audit.csv](run-articles-audit.csv), [run-articles-audit-totals.csv](run-articles-audit-totals.csv) and [run-articles-audit-method.py](run-articles-audit-method.py) - the audit rows, totals by activity and the script.
- [playbook-rules.csv](playbook-rules.csv), [playbook-activity-stats.csv](playbook-activity-stats.csv), [playbook-pilot-numbers.csv](playbook-pilot-numbers.csv), [playbook-worst-three.csv](playbook-worst-three.csv) and [playbook-rotation.csv](playbook-rotation.csv) - the playbook quality data.
- [playbook-numbers-lines.csv](playbook-numbers-lines.csv), [playbook-stats-method.py](playbook-stats-method.py) and [queue-parse.py](queue-parse.py) - the numbers line for all 31 activities and the re-runnable script.
- [run-articles-cross-activity-review.csv](run-articles-cross-activity-review.csv), [run-articles-not-superseded.csv](run-articles-not-superseded.csv) and [run-articles-cross-review-method.py](run-articles-cross-review-method.py) - the 100 reviewed rows, the 14 flagged and the script.
- [donations-units-new-rule.csv](donations-units-new-rule.csv) - each donations unit with taps logged, taps witnessed and the new status.
- [building-read-tag-check.csv](building-read-tag-check.csv) - building-read rows with and without their tag text, by file.
