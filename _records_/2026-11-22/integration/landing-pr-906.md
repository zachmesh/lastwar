---
title: Integrator landing - PR 906
created: 2026-11-23T13:55:08Z
modified: 2026-11-23T13:55:08Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 906, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-906
verified: gh pr view and git read-back after the merge
---

# Landing, PR 906

Branch land/conformance-capacity head 5ca32b7efb. Merged by merge commit 617d95cdfb (parents 5e44f5b064 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,724 to 5,724. Scope: 3 paths, all under _tools_/strategy-conformance; no workflow file. Read before running: added read-only stats parsing, tests use temp roots. Tests: strategy-conformance suite OK (32 tests incl. the new capacity cases). Replaces the superseded head ef2b8ba9.  Branch kept.
