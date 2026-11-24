---
title: Integrator landing - PR 963
created: 2026-11-24T12:10:34Z
modified: 2026-11-24T12:10:34Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 963, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-963
verified: gh pr view and git read-back after the merge
---

# Landing, PR 963

Branch land/gate-watch-list head 0696327761. Merged by merge commit 63c637f5d7 (parents 0b14e8b15a and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,891 to 5,891. Scope: 3 paths under _tools_/lint-gate; no workflow file. Read before running: only watch changes (a new list of new, exempt and new-error documents by path and count); check, which blocks commits, is untouched. Tests: full lint-gate suite OK under the head gate and the independent pinned gate.  Branch kept.
