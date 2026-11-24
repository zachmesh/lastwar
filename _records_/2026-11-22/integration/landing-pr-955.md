---
title: Integrator landing - PR 955
created: 2026-11-24T09:11:11Z
modified: 2026-11-24T09:11:11Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 955, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-955
verified: gh pr view and git read-back after the merge
---

# Landing, PR 955

Branch work/start-hint head 3194219a79. Merged by merge commit f648172d3d (parents 68f69a68f6 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,857 to 5,857. Scope: 3 paths under _tools_; no workflow file. start prints an approval hint only for a requested app with no record; read-only; tests use a temporary CU_HOME. Pushed as-is. Tests: whole cu-bridge suite, 58 tests, OK with 0 skipped (live claimed folder empty before and after). cu_bridge.py blob dbf48fefd83f to f595c7303f76; sync the live copy; no restart needed.  Branch kept.
