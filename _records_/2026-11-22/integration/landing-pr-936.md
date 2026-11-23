---
title: Integrator landing - PR 936
created: 2026-11-23T19:43:12Z
modified: 2026-11-23T19:43:12Z
level: L3
version: 0.1.0
description: One landing of the Integrator seat for pull request 936, counts and SHAs only
status: done
activity: integration
run_id: integration-landing-pr-936
verified: gh pr view and git read-back after the merge
---

# Landing, PR 936

Branch land/observation-migrate head fc984c0312. Merged by merge commit 63e32336ab (parents 52e62e9e05 and the branch head, readback ok=1). check --base blocking rc 0; privacy 0 on every count; at or over 500 words 3,407 (new 0) to 3,407 (new 0), over 300 words 5,812 to 5,812. Scope: 3 paths under _tools_ (observation.py, the new test_migrate.py and the observation-tests index); no workflow file. Read before running: dry run by default; refuses unless the committed text is a byte-exact prefix; parts written atomically before the day file is restored; read-back checked; --apply needs an empty claimed folder unless --allow-claimed. Tests: observation-tests, queue-tests, tool-sync OK.  Branch kept.
