---
title: System evaluation metrics
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 54
description: This section measures the work; the companion specification evaluation metrics measures the system that does the
---
### System evaluation metrics

This section measures the work; the companion specification
[evaluation metrics](evaluation-metrics.md) measures the system
that does the work - execution efficiency per task type,
perception completeness and discovery generalisation, retro
effectiveness (including the recurrence rate of closed
improvements), the measured impact of the tool developer and
the knowledge organiser, and loop health, including the queue
depth and oldest unit age the 2026-10-31 loop review found
missing. The daily retro computes its core set, the weekly
comparison reads the trend, and threshold breaches are named
the day they are computed. Its computation extends
`_tools_/retro_report.py` as a `system_metrics` object in the
same data appendix, filed in the tool-developer backlog in the
specification's own terms.

Pushes follow the two-tier policy of
[push and PR policy](push-and-pr-policy.md): the records,
queue state and logs this design produces are tier 1 and push
directly to main, while changes to this design, the tools and
the activity profiles are tier 2 and land by pull request, with
the retro's loop-health check auditing that no tier-2 change
reached main unreviewed.

