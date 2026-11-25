---
title: Integrator landing - PR 999
created: 2026-11-25T22:21:07Z
modified: 2026-11-25T22:21:07Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 999, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-999
verified: gh pr view and git read-back after the merge
---

# Landing, PR 999

Branch work/gate-list-ignored head c2b2ed2151. Merged by merge commit c2f69dc4ce (parents 3be255b59a and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 6,081 to 6,081. Scope: 3 paths under _tools_/lint-gate; no workflow file. check --list-ignored prints path and rule of each ignored finding; read-only; blocking logic and exit code untouched. Tests: the whole lint-gate folder OK under the head gate and the independent pinned gate.  Branch kept.
