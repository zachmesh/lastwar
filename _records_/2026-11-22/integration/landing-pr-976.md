---
title: Integrator landing - PR 976
created: 2026-11-24T16:34:11Z
modified: 2026-11-24T16:34:11Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 976, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-976
verified: gh pr view and git read-back after the merge
---

# Landing, PR 976

Branch land/forecast-override-count head 6961c7471c. Merged by merge commit 43cf517812 (parents 7bec402039 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,936 to 5,936. Scope: 3 paths under _tools_; no workflow file. forecast_override marker plus a read-only forecast-overrides counter. queue.py blob 647eea93bc21 to 7a4b2f11e3d7; sync the live copy. Tests: queue-tests, queue-guard-tests, tool-sync, strategy-conformance, strategist-health, integrator, log-append-tests OK.  Branch kept.
