---
title: Integrator landing - PR 935
created: 2026-11-23T19:40:31Z
modified: 2026-11-23T19:40:31Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 935, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-935
verified: gh pr view and git read-back after the merge
---

# Landing, PR 935

Branch land/run-notes-move-polish head 35aa793984. Merged by merge commit 52e62e9e05 (parents cfc81cc04a and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,812 to 5,812. Scope: 1 path under _tools_ (run_notes_move.py); no workflow file. Read before running: writes hoisted from per activity to per block, still through the guarded writer; the already-maps-differently refusal is kept. Tests: run-notes-move suite (28 tests) OK.  Branch kept.
