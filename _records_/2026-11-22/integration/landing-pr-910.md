---
title: Integrator landing - PR 910
created: 2026-11-23T14:22:59Z
modified: 2026-11-23T14:22:59Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 910, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-910
verified: gh pr view and git read-back after the merge
---

# Landing, PR 910

Branch land/integrator-wrapper head 61920fa9f8. Merged by merge commit 29d0a9e77a (parents 9a486f9226 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,737 to 5,738. Scope: 8 paths, all under _tools_; no workflow file. Code read before running: no force, squash, rebase, admin, delete-branch or main target; push and merge need a recorded passing check on the same head; credentials only masked. Tests: integrator 28 OK, full lint-gate suite OK, check --base and the replay rc 0 under the head gate and the independent pinned gate. lint_gate.py reproduces the author +24 -0 exactly; index pages resolved as stated in the PR. After this merge the wrapper is available for later landings.  Branch kept.
