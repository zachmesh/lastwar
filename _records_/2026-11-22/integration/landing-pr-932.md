---
title: Integrator landing - PR 932
created: 2026-11-23T18:20:22Z
modified: 2026-11-23T18:20:22Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 932, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-932
verified: gh pr view and git read-back after the merge
---

# Landing, PR 932

Branch land/playbook-hook head 1f95c7936e. Merged by merge commit 34ead7bdee (parents 8f68348771 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,802 to 5,801. Scope: 3 paths under _tools_/lint-gate; no workflow file. Read before running: only blocks card-shape-lost and card-too-long; fails open (warning) when the tool cannot run; privacy rules untouched. Tests: full lint-gate suite OK under the head gate and the independent pinned gate; playbook-check suite OK. Effect: alliance-donations card at exactly 300 words, any growth blocked; the other two cards have 3 and 9 words of headroom.  Branch kept.
