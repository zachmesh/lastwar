---
title: Integrator landing - PR 908
created: 2026-11-23T14:05:04Z
modified: 2026-11-23T14:05:04Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 908, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-908
verified: gh pr view and git read-back after the merge
---

# Landing, PR 908

Branch land/gate-ignored head 51af3951b0. Merged by merge commit 0f2d0ef9bd (parents f32ef4feaa and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,724 to 5,724. Scope: 3 paths, all under _tools_/lint-gate; no workflow file. Read before running: only run_linter changes, tracked paths are never treated as ignored, privacy checks untouched. Tests: full lint-gate suite OK on the head with both the head gate and the independent pinned gate.  Branch kept.
