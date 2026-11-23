---
title: Task intake
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 4
description: How a task the owner names is handled check whether its task type metadata exists, create
---
## Task intake

How a task the owner names is handled — check whether its task type
metadata exists, create it first if it does not, execute and log new
types, and only check and update existing types without executing —
is stated in [task intake workflow](task-intake-workflow.md). Task type
metadata always keeps its own top level folder, `_activities_`, and is
never nested inside `_records_`.

