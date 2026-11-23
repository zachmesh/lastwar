---
title: Evaluation Metrics
version: 1.2.0
status: active
created: 2026-10-31
description: How the play system measures itself - execution efficiency per task type, perception completeness and discovery generalisation, retro effectiveness, and the measured impact of the tool developer and the knowledge organiser
---

# Evaluation Metrics

How the play system measures itself - execution efficiency per task type, perception completeness and discovery generalisation, retro effectiveness, and the measured impact of the... This register stays at this path as an entry page; its text was split verbatim into 11 articles in [evaluation-metrics-sections](evaluation-metrics-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `evaluation-metrics-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](evaluation-metrics-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Articles

- [Evaluation metrics](evaluation-metrics-sections/evaluation-metrics.md) - Owner direction, 2026-10-31 - the system that plays the account
- [A. Execution efficiency, per task type](evaluation-metrics-sections/a-execution-efficiency.md) - a-execution-efficiency - Per regular, per day and rolling 7 days.
- [B. Perception completeness](evaluation-metrics-sections/b-perception-completeness.md) - b-perception-completeness - Per perception day.
- [C. Generalisation and discovery](evaluation-metrics-sections/c-generalisation-and.md) - c-generalisation-and - Per week, with daily counts kept.
- [D. Retro effectiveness](evaluation-metrics-sections/d-retro-effectiveness.md) - d-retro-effectiveness - Per retro and rolling.
- [E. Tool developer impact](evaluation-metrics-sections/e-tool-developer.md) - e-tool-developer - Per tool landing, rolled up weekly.
- [F. Knowledge organiser impact](evaluation-metrics-sections/f-knowledge-organiser.md) - f-knowledge-organiser - Per organiser run, rolled up weekly.
- [G. Loop health](evaluation-metrics-sections/g-loop-health.md) - g-loop-health - Daily snapshot at the retro, from the records the loop
- [Monitoring](evaluation-metrics-sections/monitoring-section.md) - monitoring-section - Daily - the daily retro computes the core set: family
- [Tool route](evaluation-metrics-sections/tool-route.md) - tool-route - The computation extends _tools_/retro_report.py; it does not become a second
- [Changelog](evaluation-metrics-sections/changelog-section.md) - changelog-section - 1.1.2, 2026-11-05 - family A corrected: duration p90 and the

## Changelog

- 1.2.0, 2026-11-23 - Split verbatim by split_doc.py into 11 articles; --check EQUAL, sha256 0ab2ae3b06c5; the unsplit 1.1.2 file is commit 6d019ade
