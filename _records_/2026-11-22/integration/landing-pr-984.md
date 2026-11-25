---
title: Integrator landing - PR 984
created: 2026-11-25T04:41:05Z
modified: 2026-11-25T04:41:05Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 984, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-984
verified: gh pr view and git read-back after the merge
---

# Landing, PR 984

Branch work/exempt-list head 689a4d746d. Merged by merge commit 09476c270b (parents f775f9e1c2 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 6,025 to 6,025. Scope: 4 paths under _tools_/strategy-conformance; no workflow file. New alarm exempt-list; the first write of this tool, only by --accept-exempt-list, atomic, reason texts hashed never stored. Tests: strategy-conformance 81 with 1 skip by design (the real list is not on main yet), strategist-health, integrator, queue-tests OK.  Branch kept.
