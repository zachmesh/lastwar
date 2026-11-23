---
title: Integrator landing - PR 905
created: 2026-11-23T13:49:05Z
modified: 2026-11-23T13:49:05Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 905, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-905
verified: gh pr view and git read-back after the merge
---

# Landing, PR 905

Branch work/require-forecast head 8cf9f3be23. Merged by merge commit 5e44f5b064 (parents 36f49cbb5a and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,724 to 5,724. Scope: 5 paths, all under _tools_; no workflow file. Read before running: off by default, scout_diff change is a verbatim refactor, 17 new tests use a temp roster file. Queue guard: queue.py blob 7582acc84485 to aa29aa20c3af and scout_diff.py a74ea107fc7b to 9908ae082a06, live copies to be synced. The switch is OFF until the Coordinator flips it at 2026-11-24T00:05Z.  Branch kept.
