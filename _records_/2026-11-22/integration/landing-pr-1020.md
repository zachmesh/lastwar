---
title: Integrator landing - PR 1020
created: 2026-11-26T16:02:46Z
modified: 2026-11-26T16:02:46Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 1020, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-1020
verified: gh pr view and git read-back after the merge
---

# Landing, PR 1020

Branch land/home-glob-check head 3739a7d890. Merged by merge commit 4ad4ae9d57 (parents 04ffd7e368 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 6,193 to 6,193. Scope: 4 paths under _tools_ (new folder home-glob-check and a row in _tools_/INDEX.md); no workflow file. Read-only source checker; tests use temp folders only. Weakness noted, not changed: positional PATH arguments are walked as given. Tests: home-glob-check (25), tool-sync, integrator OK.  Branch kept.
