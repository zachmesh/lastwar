---
title: Integrator landing - PR 923
created: 2026-11-23T17:12:33Z
modified: 2026-11-23T17:12:33Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 923, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-923
verified: gh pr view and git read-back after the merge
---

# Landing, PR 923

Branch land/desktop-lock head 4c39e7ceb2. Merged by merge commit 58dfd398ed (parents 8995861631 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,803 to 5,803. Scope: 4 paths, all under _tools_; no workflow file. Code read before running: the lock is only read (status call plus a pid-exists check); nothing creates or breaks a lock; tests use a fake lock CLI and server. Tests: cu-bridge-tests OK with 0 skipped (live claimed folder empty before and after); a first scan skipped all 26 and was not counted. cu_bridge.py blob f90ad0b01229 to 91df754e547c; sync the live copy; the default-seat change needs a restart between runs.  Branch kept.
