---
title: A. Execution efficiency, per task type part 2
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 3
description: Thresholds - no universal attainment line; attainment is read per type against its own history.
---
Thresholds - no universal attainment line; attainment is read
per type against its own history. For the quota types with a
hard daily target (trucks, donations) a rolling attainment
under 0.8 is named. The unverified rate is thresholded under
Monitoring below.

Known defects - units executed before the section 14 stats
specification landed (2026-11-01) are legacy-shaped and count
as unverified almost by definition; early windows are dominated
by them, so every unverified figure is read together with the
legacy share of its window. Attainment is undefined for types
whose units carry no numeric target; those types report
attainment_units 0 and are judged on done rate and yield.

