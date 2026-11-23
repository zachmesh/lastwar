---
title: Integrator landing - PR 882
created: 2026-11-23T09:25:20Z
modified: 2026-11-23T09:25:20Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 882, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-882
verified: gh pr view and git read-back after the merge
---

# Landing, PR 882

Code lane (high priority), PR 882, branch land/spawn-seat head 59fcc2804f (mechanical cherry-pick of the author's commit 97b9b32ce9 onto current main, 5 of 5 files byte-identical): pushed, merged by merge commit 7820adcb6d (parents 97c06ca279 and the branch head, readback ok). 5 paths under _tools_/; spawn-seat 15 OK; check --base blocking rc 0; privacy 0 on every count; watch at or over 500 words 3419, new 0. Tool lesson: never prepend /opt/homebrew/bin to PATH, it hides the python that has markdown_it and makes watch fail; append instead. Branch kept.
