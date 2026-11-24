---
title: Integrator landing - PR 957
created: 2026-11-24T10:39:17Z
modified: 2026-11-24T10:39:17Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 957, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-957
verified: gh pr view and git read-back after the merge
---

# Landing, PR 957

Branch work/forecast-refusal-text head e9f66c2ab4. Merged by merge commit 42fa90d951 (parents 284eef81eb and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,857 to 5,857. Scope: 4 paths under _tools_; no workflow file. Text only: the strict forecast rule said once; check logic and reason words unchanged; a refusal never echoes the serves text. Tests: queue-tests (this branch, switch off), queue-guard-tests, tool-sync, strategy-conformance, strategist-health, integrator OK. queue.py blob e6d19073135d to 9d85fd66402f; sync the live copy.  Branch kept.
