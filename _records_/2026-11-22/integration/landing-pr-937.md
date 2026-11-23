---
title: Integrator landing - PR 937
created: 2026-11-23T20:03:03Z
modified: 2026-11-23T20:03:03Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 937, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-937
verified: gh pr view and git read-back after the merge
---

# Landing, PR 937

Branch work/owner-idle-restore head 95febb6460. Merged by merge commit 7b0c818513 (parents 63e32336ab and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,812 to 5,812. Scope: 3 paths under _tools_; no workflow file. Owner decision D-066 / OD-20261123-23; the only executable change removes the setdefault of CU_OWNER_IDLE_SECONDS to 0; tests use a fake server. Tests: cu-bridge suite, 36 tests, OK with 0 skipped (live claimed folder empty before and after); a first scan skipped all 36 and was not counted. cu_bridge.py blob 4a0809b7a845 to 6ed827f2abf0; sync the live copy; takes effect only after a bridge restart between runs, on origin and restarted by 22:30Z and never 23:00Z to 00:30Z. Pushed as-is.  Branch kept.
