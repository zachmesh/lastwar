---
title: Integrator landing - PR 925
created: 2026-11-23T17:25:01Z
modified: 2026-11-23T17:25:01Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 925, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-925
verified: gh pr view and git read-back after the merge
---

# Landing, PR 925

Branch land/roster-serves head 4e98b7cc75. Merged by merge commit 6a09356e2d (parents afa72fad19 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,406 (new 0) to 3,406 (new 0), over 300 words 5,803 to 5,802. Scope: 5 paths, all under _tools_; no workflow file. Only serves changes on 11 roster entries; tests strengthened (roster held to the ledger by queue.py own check). Checked independently: all 8 plan items the roster serves have rows in the ledger on main. regulars.json blob f0eb7e81d7cc to 1879aba3489b, sync the live copy; must be on main before the 00:05Z forecast flip.  Branch kept.
