---
title: Integrator landing - PR 956
created: 2026-11-24T09:49:46Z
modified: 2026-11-24T09:49:46Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 956, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-956
verified: gh pr view and git read-back after the merge
---

# Landing, PR 956

Branch work/conformance-exact head 1cf4751671. Merged by merge commit 284eef81eb (parents f648172d3d and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,857 to 5,857. Scope: 3 paths under _tools_/strategy-conformance; no workflow file. The alarm compares the unrounded percentage; one-decimal display never shows a value below the limit as the limit; JSON gains the _exact fields; no other reader of the old fields in the repository. Tests: strategy-conformance, queue-tests, strategist-health, integrator OK.  Branch kept.
