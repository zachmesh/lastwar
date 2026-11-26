---
title: Integrator landing - PR 1021
created: 2026-11-26T16:18:29Z
modified: 2026-11-26T16:18:29Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 1021, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-1021
verified: gh pr view and git read-back after the merge
---

# Landing, PR 1021

Branch work/exempt-oneoff head 0c1dde0880. Merged by merge commit 6bccdf3ece (parents 4ad4ae9d57 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 6,193 to 6,193. Scope: 4 paths under _tools_/strategy-conformance; no workflow file. Optional kind column (regular or oneoff) on the exempt list; backward compatible with an existing baseline; no new write. Tests: strategy-conformance, strategist-health, integrator, queue-tests OK.  Branch kept.
